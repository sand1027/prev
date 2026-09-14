/**
 * LeetCode bot — N problems/day via NVIDIA LLM API:
 *   1) Daily challenge (compulsory if not already solved)
 *   2) Rest: random from pool [EASY, MEDIUM, HARD, SQL]
 *
 * Algo → C++ | SQL → MySQL
 * Hosted: GitHub Actions (cookie auth) or local cron
 */
import { CONFIG } from "./config.js";
import { useRealChrome } from "./chrome-cdp.js";
import {
  ensureAuth,
  getDailyChallenge,
  pickUnsolvedProblem,
  PROBLEM_TYPES,
  problemPromptText,
  submitSolution,
  checkSubmission,
  isSessionValid,
  isAlreadySolved,
  loginWithPlaywright,
} from "./leetcode.js";
import {
  buildSolvePrompt,
  buildFixPrompt,
  formatJudgeError,
} from "./chatgpt.js";
import { llmConfigFrom, assertLlmConfig, askLlmForCode } from "./llm.js";
import {
  telegramConfigFrom,
  sendTelegram,
  formatRunSummary,
} from "./telegram.js";

const loginOnly = process.argv.includes("--login-only");

function assertConfig() {
  const bad = (v) => !v || String(v).startsWith("PASTE_");
  const hasSession =
    !bad(CONFIG.LEETCODE_SESSION || process.env.LEETCODE_SESSION) &&
    !bad(CONFIG.LEETCODE_CSRF || process.env.LEETCODE_CSRF);
  const hasPassword = !bad(CONFIG.LEETCODE_USERNAME) && !bad(CONFIG.LEETCODE_PASSWORD);

  if (!loginOnly && !hasSession && !hasPassword) {
    throw new Error(
      "Set LEETCODE_SESSION+LEETCODE_CSRF (hosted) or LEETCODE_USERNAME+PASSWORD (local) in config"
    );
  }
  if (!loginOnly) assertLlmConfig(llmConfigFrom(CONFIG));
}

function shuffle(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

function pickRandomType(pool) {
  return pool[Math.floor(Math.random() * pool.length)];
}

async function buildProblemQueue(auth) {
  const queue = [];
  const exclude = [];
  const target = Number(CONFIG.PROBLEMS_PER_DAY ?? 3);
  const pool = (CONFIG.PROBLEM_POOL || ["EASY", "MEDIUM", "HARD", "SQL"]).filter(
    (t) => PROBLEM_TYPES[t]
  );

  if (CONFIG.SOLVE_DAILY !== false) {
    const daily = await getDailyChallenge(auth);
    exclude.push(daily.titleSlug);
    if (await isAlreadySolved(auth, daily.titleSlug)) {
      console.log(`  DAILY already Accepted — ${daily.title} (counting toward day)`);
      queue.push({
        label: "DAILY",
        q: daily,
        lang: CONFIG.LANG || "cpp",
        skipSolve: true,
      });
    } else {
      const isSql = (daily.codeSnippets || []).some((s) =>
        ["mysql", "mssql", "oraclesql", "postgresql"].includes(s.langSlug)
      );
      queue.push({
        label: "DAILY",
        q: daily,
        lang: isSql ? "mysql" : CONFIG.LANG || "cpp",
        skipSolve: false,
      });
    }
  }

  let guard = 0;
  while (queue.length < target && guard < 20) {
    guard++;
    const typeKey = pickRandomType(pool);
    const type = PROBLEM_TYPES[typeKey];
    try {
      let difficulty = type.difficulty;
      if (typeKey === "SQL") {
        difficulty = shuffle(["EASY", "MEDIUM", "HARD"])[0];
      }
      const q = await pickUnsolvedProblem(auth, difficulty, {
        excludeSlugs: exclude,
        categorySlug: type.categorySlug,
      });
      exclude.push(q.titleSlug);
      queue.push({
        label: type.label,
        q,
        lang: type.lang,
        skipSolve: false,
      });
    } catch (e) {
      console.log(`  Could not pick ${typeKey}: ${e.message} — trying another type`);
    }
  }

  return queue;
}

async function solveOneWithLlm({ auth, llm, q, label, lang, maxRounds }) {
  const starter =
    q.codeSnippets?.find((s) => s.langSlug === lang)?.code ||
    q.codeSnippets?.find((s) => (lang === "mysql" ? s.langSlug === "mysql" : s.langSlug === "cpp"))
      ?.code ||
    "";
  const problemText = problemPromptText(q);

  console.log(`\n████████████████████████████████████████`);
  console.log(`█  ${label}: #${q.questionFrontendId} ${q.title} [${q.difficulty}] (${lang})`);
  console.log(`█  https://leetcode.com/problems/${q.titleSlug}/`);
  console.log(`████████████████████████████████████████`);

  let code = null;
  let lastResult = null;

  for (let round = 1; round <= maxRounds; round++) {
    console.log(`\n── ${label} fix round ${round}/${maxRounds} ──`);

    const prompt =
      round === 1
        ? buildSolvePrompt(problemText, { lang, starterCode: starter })
        : buildFixPrompt(formatJudgeError(lastResult), code, { lang });

    try {
      code = await askLlmForCode(llm, prompt, lang);
    } catch (err) {
      console.error(`  LLM extract failed: ${err.message}`);
      if (round === maxRounds) break;
      continue;
    }

    console.log("--- code preview ---");
    console.log(code.split("\n").slice(0, 12).join("\n"));
    console.log("--------------------");

    console.log("Submitting to LeetCode…");
    const subId = await submitSolution(auth, {
      titleSlug: q.titleSlug,
      questionId: q.questionId,
      code,
      lang,
    });
    console.log(`submission_id=${subId}`);

    lastResult = await checkSubmission(auth, subId);
    const status = lastResult.status_msg || lastResult.state;
    console.log(
      `Judge: ${status} | Runtime: ${lastResult.status_runtime || "N/A"} | Memory: ${lastResult.status_memory || "N/A"}`
    );

    if (status === "Accepted") {
      console.log(`✅ ${label} ACCEPTED — ${q.title}`);
      return { ok: true, title: q.title, difficulty: q.difficulty, label, status };
    }

    console.log("Judge error → LLM fix:\n" + formatJudgeError(lastResult).slice(0, 600));
  }

  console.log(`❌ ${label} FAILED after ${maxRounds} rounds — ${q.title}`);
  return {
    ok: false,
    title: q.title,
    difficulty: q.difficulty,
    label,
    status: lastResult?.status_msg || lastResult?.state || "Failed",
  };
}

async function main() {
  assertConfig();

  const headless = CONFIG.HEADLESS === true;
  const maxRounds = CONFIG.MAX_FIX_ROUNDS ?? 5;
  const perDay = CONFIG.PROBLEMS_PER_DAY ?? 3;
  const llm = llmConfigFrom(CONFIG);
  const tg = telegramConfigFrom(CONFIG);

  console.log(`LeetCode bot — ${perDay}/day (daily + random EASY/MEDIUM/HARD/SQL)`);
  console.log(`LLM: ${llm.provider} / ${llm.model}`);
  console.log(`headless=${headless} maxFixRounds=${maxRounds}`);
  console.log(`pool: ${(CONFIG.PROBLEM_POOL || []).join(", ")}\n`);

  if (loginOnly) {
    const chrome = await useRealChrome({
      profile: "leetcode",
      url: "https://leetcode.com/accounts/login/",
      force: false,
    });
    try {
      const auth = await loginWithPlaywright(null, {
        username: CONFIG.LEETCODE_USERNAME,
        password: CONFIG.LEETCODE_PASSWORD,
        headless: false,
        context: chrome.context,
      });
      if (!(await isSessionValid(auth))) throw new Error("LeetCode session still invalid");
      console.log("\n✅ LeetCode cookies saved. Next: npm run daily");
    } finally {
      await chrome.close();
    }
    return;
  }

  let results = [];
  try {
    await sendTelegram(
      tg,
      `🚀 LeetCode bot STARTED\n${perDay}/day · ${llm.model}`
    );

    const auth = await ensureAuth(null, {
      username: CONFIG.LEETCODE_USERNAME,
      password: CONFIG.LEETCODE_PASSWORD,
      session: CONFIG.LEETCODE_SESSION,
      csrf: CONFIG.LEETCODE_CSRF,
      headless,
      // Always allow Playwright re-login on a real machine (not cookie-only CI)
      allowBrowserLogin: CONFIG.ALLOW_BROWSER_LOGIN !== false,
      notify: (text) => sendTelegram(tg, text),
    });
    if (!(await isSessionValid(auth))) {
      throw new Error("LeetCode session invalid — refresh LEETCODE_SESSION / LEETCODE_CSRF");
    }
    console.log("LeetCode session OK\n");

    console.log("Building today's queue…");
    const queue = await buildProblemQueue(auth);
    for (const item of queue) {
      const skip = item.skipSolve ? " (already done)" : "";
      console.log(
        `  • [${item.label}] #${item.q.questionFrontendId} ${item.q.title} (${item.q.difficulty}) ${item.lang}${skip}`
      );
    }

    const toSolve = queue.filter((x) => !x.skipSolve);
    for (const skipped of queue.filter((x) => x.skipSolve)) {
      results.push({
        ok: true,
        title: skipped.q.title,
        difficulty: skipped.q.difficulty,
        label: skipped.label,
        status: "Accepted (earlier)",
      });
    }

    if (!toSolve.length && !results.length) {
      console.log("\nNothing left to solve today.");
      await sendTelegram(tg, "ℹ️ LeetCode bot — nothing left to solve today.");
      return;
    }

    for (const { label, q, lang } of toSolve) {
      const result = await solveOneWithLlm({
        auth,
        llm,
        q,
        label,
        lang,
        maxRounds,
      });
      results.push(result);
      await new Promise((r) => setTimeout(r, 1500));
    }

    console.log("\n════════ TODAY'S SUMMARY ════════");
    for (const r of results) {
      console.log(`${r.ok ? "✅" : "❌"} [${r.label}] ${r.title} (${r.difficulty}) — ${r.status}`);
    }
    const okCount = results.filter((r) => r.ok).length;
    console.log(`\nAccepted ${okCount}/${results.length}`);
    console.log(`Year pace @ ${perDay}/day × 365 ≈ ${perDay * 365} problems`);

    await sendTelegram(tg, formatRunSummary({ results, perDay, okCount }));

    if (okCount < results.length) process.exitCode = 1;
  } catch (err) {
    await sendTelegram(tg, formatRunSummary({ error: err.message || err, perDay })).catch(() => {});
    throw err;
  }
}

main().catch((err) => {
  console.error("\nFATAL:", err.message || err);
  process.exit(1);
});
