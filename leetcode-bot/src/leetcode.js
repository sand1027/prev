import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { launchBrowser } from "./browser.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const COOKIE_PATH = path.join(__dirname, "..", ".cookies.json");
const BASE = "https://leetcode.com";
const GRAPHQL = `${BASE}/graphql`;

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

export function loadSavedCookies() {
  if (!fs.existsSync(COOKIE_PATH)) return null;
  try {
    return JSON.parse(fs.readFileSync(COOKIE_PATH, "utf8"));
  } catch {
    return null;
  }
}

export function saveCookies(cookies) {
  fs.writeFileSync(COOKIE_PATH, JSON.stringify(cookies, null, 2));
}

function cookieJar(cookies) {
  const map = Object.fromEntries(cookies.map((c) => [c.name, c.value]));
  return {
    session: map.LEETCODE_SESSION || "",
    csrf: map.csrftoken || "",
    header: cookies.map((c) => `${c.name}=${c.value}`).join("; "),
  };
}

async function hasSessionCookie(context) {
  const cookies = await context.cookies(BASE);
  return cookies.some((c) => c.name === "LEETCODE_SESSION" && c.value);
}

/**
 * Login with real Chrome persistent profile.
 * Bot fills username/password — YOU click "I'm not a robot" if shown.
 */
export async function loginWithPlaywright(
  _browser,
  { username, password, headless, context: existingContext, notify } = {}
) {
  let context = existingContext;
  let ownsContext = false;
  let disconnect = null;

  if (!context) {
    // Prefer real Chrome via CDP (Cloudflare clicks work). Fallback: Playwright Chrome.
    try {
      const { useRealChrome } = await import("./chrome-cdp.js");
      const chrome = await useRealChrome({
        profile: "leetcode",
        url: `${BASE}/accounts/login/`,
      });
      context = chrome.context;
      ownsContext = true;
      disconnect = () => chrome.close();
    } catch (e) {
      console.log("CDP Chrome unavailable, falling back:", e.message);
      const launched = await launchBrowser({
        headless: false,
        persistent: true,
        profile: "leetcode",
      });
      context = launched.context;
      ownsContext = true;
      disconnect = () => context.close();
    }
  }

  const cleanup = async () => {
    if (ownsContext && disconnect) await disconnect().catch(() => {});
  };

  const page = context.pages()[0] || (await context.newPage());

  console.log("Opening LeetCode login (real Chrome)…");
  await page.goto(`${BASE}/accounts/login/`, { waitUntil: "domcontentloaded", timeout: 60000 });
  await sleep(1500);

  // Already logged in via profile cookies?
  if (await hasSessionCookie(context)) {
    const cookies = await context.cookies();
    const jar = cookieJar(cookies.filter((c) => c.domain.includes("leetcode")));
    if (jar.session && (await isSessionValid(jar))) {
      saveCookies(cookies.filter((c) => c.domain.includes("leetcode")));
      console.log("LeetCode already logged in via Chrome profile — cookies saved");
      await cleanup();
      return jar;
    }
  }

  try {
    const btn = page.getByRole("button", { name: /accept|agree|got it/i }).first();
    if (await btn.isVisible({ timeout: 2000 })) await btn.click();
  } catch {
    /* ignore */
  }

  const userInput = page
    .locator('input[name="login"], input[name="username"], input[autocomplete="username"], input[type="text"]')
    .first();
  const passInput = page.locator('input[name="password"], input[type="password"]').first();

  await userInput.waitFor({ state: "visible", timeout: 30000 });
  await userInput.click();
  await userInput.fill("");
  await userInput.fill(username);
  await passInput.click();
  await passInput.fill("");
  await passInput.fill(password);

  console.log("\n╔════════════════════════════════════════════════════════════╗");
  console.log("║  LEETCODE LOGIN — do this in the Chrome window:            ║");
  console.log("║  1) If you see “I'm not a robot” → click the checkbox      ║");
  console.log("║     yourself (bot will NOT click it)                       ║");
  console.log("║  2) Complete any image challenge if shown                  ║");
  console.log("║  3) Click Sign In if it didn't already                     ║");
  console.log("║  Bot waits up to 10 minutes.                               ║");
  console.log("╚════════════════════════════════════════════════════════════╝\n");

  if (typeof notify === "function") {
    await notify(
      "🔐 LeetCode login needs you (CAPTCHA?)\nOpen the Chrome window, click robot if shown, wait for login."
    ).catch(() => {});
  }

  // Click Sign In — CAPTCHA may block; user finishes manually
  try {
    const signIn = page.getByRole("button", { name: /sign in|log in/i }).first();
    if (await signIn.isVisible({ timeout: 3000 })) await signIn.click();
  } catch {
    /* user can click */
  }

  const deadline = Date.now() + 10 * 60 * 1000;
  let lastPing = 0;
  while (Date.now() < deadline) {
    if (await hasSessionCookie(context)) {
      await sleep(1500);
      break;
    }
    // Also detect leaving login page
    const url = page.url();
    if (!url.includes("/accounts/login") && (await hasSessionCookie(context))) break;

    if (Date.now() - lastPing > 15000) {
      const left = Math.ceil((deadline - Date.now()) / 1000);
      console.log(`  …waiting for LeetCode login (${left}s left). Click robot checkbox if shown.`);
      lastPing = Date.now();
    }
    await sleep(2000);
  }

  const cookies = await context.cookies();
  const lcCookies = cookies.filter((c) => c.domain.includes("leetcode"));
  const jar = cookieJar(lcCookies);

  if (!jar.session) {
    const shot = path.join(__dirname, "..", "screenshots");
    fs.mkdirSync(shot, { recursive: true });
    const file = path.join(shot, `leetcode-login-fail-${Date.now()}.png`);
    await page.screenshot({ path: file, fullPage: true });
    await cleanup();
    throw new Error(
      `LeetCode login failed (robot checkbox / wrong password?). Screenshot: ${file}\n` +
        `Re-run: npm run open-chrome leetcode && npm run login-only`
    );
  }

  saveCookies(lcCookies);
  console.log("LeetCode logged in — cookies saved to .cookies.json");

  await cleanup();
  return jar;
}

/**
 * Auth from LEETCODE_SESSION + csrftoken (env / config) — for CI / hosted runs.
 */
export function authFromSessionCookies({ session, csrf } = {}) {
  const s = (session || "").trim();
  const c = (csrf || "").trim();
  if (!s || !c) return null;
  return {
    session: s,
    csrf: c,
    header: `LEETCODE_SESSION=${s}; csrftoken=${c}`,
  };
}

/**
 * Prefer saved cookies; when expired → Playwright Chrome login (username/password).
 * That is the point of Playwright: no manual session/csrf refresh every ~2 weeks.
 */
export async function ensureAuth(browser, opts = {}) {
  const fromEnv = authFromSessionCookies({
    session: opts.session || process.env.LEETCODE_SESSION,
    csrf: opts.csrf || process.env.LEETCODE_CSRF,
  });
  if (fromEnv) {
    if (await isSessionValid(fromEnv)) {
      console.log("Using LEETCODE_SESSION + LEETCODE_CSRF");
      return fromEnv;
    }
    console.log("LEETCODE_SESSION/CSRF expired — will re-login with Playwright");
    if (typeof opts.notify === "function") {
      await opts.notify("⚠️ LeetCode session expired — opening Chrome to re-login…").catch(() => {});
    }
  }

  const saved = loadSavedCookies();
  if (saved?.length) {
    const jar = cookieJar(saved);
    if (jar.session && (await isSessionValid(jar))) {
      console.log("Using saved LeetCode cookies (.cookies.json)");
      return jar;
    }
    console.log("Saved cookies expired — Playwright re-login (click robot box if shown)");
    if (typeof opts.notify === "function") {
      await opts.notify("⚠️ LeetCode cookies expired — opening Chrome to re-login…").catch(() => {});
    }
  }

  // Cookie-only hosts (GitHub Actions) — no Chrome available
  if (opts.allowBrowserLogin === false) {
    throw new Error(
      "No valid LeetCode session and browser login disabled. " +
        "Host on a machine with Chrome so Playwright can re-login."
    );
  }

  if (!opts.username || !opts.password) {
    throw new Error("Set LEETCODE_USERNAME + LEETCODE_PASSWORD so Playwright can re-login");
  }

  return loginWithPlaywright(browser, opts);
}

async function gql(auth, query, variables = {}) {
  const res = await fetch(GRAPHQL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Referer: BASE,
      Origin: BASE,
      Cookie: auth.header,
      "x-csrftoken": auth.csrf,
      "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    },
    body: JSON.stringify({ query, variables }),
  });
  const text = await res.text();
  let json;
  try {
    json = JSON.parse(text);
  } catch {
    throw new Error(`GraphQL HTTP ${res.status}: ${text.slice(0, 300)}`);
  }
  if (!res.ok) {
    throw new Error(`GraphQL HTTP ${res.status}: ${text.slice(0, 400)}`);
  }
  if (json.errors?.length) throw new Error(JSON.stringify(json.errors));
  return json.data;
}

export async function isSessionValid(auth) {
  try {
    const data = await gql(auth, `query { userStatus { isSignedIn username } }`);
    return Boolean(data?.userStatus?.isSignedIn);
  } catch {
    return false;
  }
}

export async function getDailyChallenge(auth) {
  const data = await gql(
    auth,
    `query questionOfToday {
      activeDailyCodingChallengeQuestion {
        date
        link
        question {
          questionId
          questionFrontendId
          title
          titleSlug
          difficulty
          content
          codeSnippets { lang langSlug code }
        }
      }
    }`
  );
  const daily = data.activeDailyCodingChallengeQuestion;
  if (!daily?.question) throw new Error("No daily challenge returned");
  return { date: daily.date, link: daily.link, ...daily.question };
}

export async function getProblemDetail(auth, titleSlug) {
  const data = await gql(
    auth,
    `query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        questionFrontendId
        title
        titleSlug
        difficulty
        content
        status
        codeSnippets { lang langSlug code }
      }
    }`,
    { titleSlug }
  );
  if (!data?.question) throw new Error(`No problem detail for ${titleSlug}`);
  return data.question;
}

/** true if already Accepted on LeetCode */
export async function isAlreadySolved(auth, titleSlug) {
  try {
    const q = await getProblemDetail(auth, titleSlug);
    return q.status === "ac";
  } catch {
    return false;
  }
}

/**
 * Pick a random unsolved free problem.
 * @param {string|null} difficulty EASY | MEDIUM | HARD | null (any)
 * @param {{ excludeSlugs?: string[], limit?: number, categorySlug?: string }} opts
 *   categorySlug: "" algorithms, "database" for SQL
 */
export async function pickUnsolvedProblem(
  auth,
  difficulty,
  { excludeSlugs = [], limit = 50, categorySlug = "" } = {}
) {
  const skip = Math.floor(Math.random() * 100);
  const filters = {};
  if (difficulty) filters.difficulty = difficulty;

  const listQuery = `query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
    problemsetQuestionList: questionList(
      categorySlug: $categorySlug
      limit: $limit
      skip: $skip
      filters: $filters
    ) {
      questions: data {
        difficulty
        titleSlug
        title
        paidOnly: isPaidOnly
        status
        frontendQuestionId: questionFrontendId
      }
    }
  }`;

  const fetchList = async (vars) => {
    const data = await gql(auth, listQuery, vars);
    return data?.problemsetQuestionList?.questions || [];
  };

  const exclude = new Set(excludeSlugs);
  let questions = await fetchList({
    categorySlug,
    limit,
    skip,
    filters: { ...filters, status: "NOT_STARTED" },
  });
  let candidates = questions.filter((q) => !q.paidOnly && !exclude.has(q.titleSlug));

  if (!candidates.length) {
    questions = await fetchList({
      categorySlug,
      limit: 100,
      skip: 0,
      filters,
    });
    candidates = questions.filter(
      (q) => !q.paidOnly && q.status !== "ac" && !exclude.has(q.titleSlug)
    );
  }

  const label = categorySlug === "database" ? `SQL/${difficulty || "ANY"}` : difficulty || "ANY";
  if (!candidates.length) {
    throw new Error(`No unsolved free ${label} problems found`);
  }

  const pick = candidates[Math.floor(Math.random() * candidates.length)];
  console.log(`  Picked ${label}: #${pick.frontendQuestionId} ${pick.title}`);
  return getProblemDetail(auth, pick.titleSlug);
}

/** Map pool type → LeetCode list + submit lang */
export const PROBLEM_TYPES = {
  EASY: { difficulty: "EASY", categorySlug: "", lang: "cpp", label: "EASY" },
  MEDIUM: { difficulty: "MEDIUM", categorySlug: "", lang: "cpp", label: "MEDIUM" },
  HARD: { difficulty: "HARD", categorySlug: "", lang: "cpp", label: "HARD" },
  SQL: { difficulty: null, categorySlug: "database", lang: "mysql", label: "SQL" },
};

function stripHtml(html) {
  return (html || "")
    .replace(/<[^>]+>/g, " ")
    .replace(/&nbsp;/g, " ")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&amp;/g, "&")
    .replace(/&quot;/g, '"')
    .replace(/\s+/g, " ")
    .trim();
}

export function problemPromptText(question) {
  return [
    `Title: ${question.title}`,
    `Slug: ${question.titleSlug}`,
    `Difficulty: ${question.difficulty}`,
    "",
    stripHtml(question.content),
  ].join("\n");
}

export async function submitSolution(auth, { titleSlug, questionId, code, lang }) {
  const res = await fetch(`${BASE}/problems/${titleSlug}/submit/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Referer: `${BASE}/problems/${titleSlug}/`,
      Origin: BASE,
      Cookie: auth.header,
      "x-csrftoken": auth.csrf,
      "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    },
    body: JSON.stringify({
      lang,
      question_id: String(questionId),
      typed_code: code,
    }),
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`Submit failed HTTP ${res.status}: ${body.slice(0, 300)}`);
  }
  const json = await res.json();
  return json.submission_id;
}

export async function checkSubmission(auth, submissionId, { retries = 20, delayMs = 2500 } = {}) {
  for (let i = 0; i < retries; i++) {
    await new Promise((r) => setTimeout(r, delayMs));
    const res = await fetch(`${BASE}/submissions/detail/${submissionId}/check/`, {
      headers: {
        Cookie: auth.header,
        "x-csrftoken": auth.csrf,
        Referer: BASE,
        "User-Agent":
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
      },
    });
    if (!res.ok) continue;
    const result = await res.json();
    if (result.state === "SUCCESS") return result;
    if (!["PENDING", "STARTED"].includes(result.state)) return result;
  }
  return { state: "TIMEOUT", status_msg: "Timeout waiting for judge" };
}
