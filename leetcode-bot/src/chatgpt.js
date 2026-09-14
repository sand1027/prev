import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { chromium } from "playwright";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const CHATGPT_URL = "https://chatgpt.com/";

const LANG_LABEL = {
  python3: "Python 3",
  cpp: "C++",
  java: "Java",
  javascript: "JavaScript",
  mysql: "MySQL",
};

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

async function screenshot(page, name) {
  const dir = path.join(__dirname, "..", "screenshots");
  fs.mkdirSync(dir, { recursive: true });
  const file = path.join(dir, `${name}-${Date.now()}.png`);
  await page.screenshot({ path: file, fullPage: true });
  console.log(`  screenshot → ${file}`);
  return file;
}

async function hasComposer(page) {
  const composers = [
    page.locator("#prompt-textarea"),
    page.locator('div[contenteditable="true"]#prompt-textarea'),
    page.locator('[data-testid="composer-text-input"]'),
    page.locator('textarea[placeholder*="Message"]'),
    page.locator('div[contenteditable="true"][id*="prompt"]'),
    page.locator('div[contenteditable="true"][data-placeholder]'),
    page.locator('[contenteditable="true"].ProseMirror'),
  ];
  for (const loc of composers) {
    try {
      if (await loc.first().isVisible({ timeout: 1200 })) return true;
    } catch {
      /* next */
    }
  }
  return false;
}

async function dismissGuestPrompts(page) {
  const labels = [
    /stay logged out/i,
    /continue without/i,
    /skip/i,
    /not now/i,
    /accept.*cookie/i,
    /got it/i,
  ];
  for (const re of labels) {
    try {
      const btn = page.getByRole("button", { name: re }).first();
      if (await btn.isVisible({ timeout: 800 })) {
        await btn.click();
        await sleep(500);
      }
    } catch {
      /* ignore */
    }
  }
}

/**
 * Fresh Chrome — no profile, no Google login.
 * Just open ChatGPT and paste.
 */
export async function openChatGPTGuest({ headless = false } = {}) {
  console.log("Opening ChatGPT (guest mode — no login / no profile)…");
  const browser = await chromium.launch({
    channel: "chrome",
    headless,
    args: ["--disable-blink-features=AutomationControlled"],
    ignoreDefaultArgs: ["--enable-automation"],
  });
  const context = await browser.newContext({
    viewport: { width: 1400, height: 900 },
  });
  const page = await context.newPage();
  await page.goto(CHATGPT_URL, { waitUntil: "domcontentloaded", timeout: 90000 });
  await sleep(2000);
  await dismissGuestPrompts(page);

  const deadline = Date.now() + 45000;
  while (Date.now() < deadline) {
    await dismissGuestPrompts(page);
    if (await hasComposer(page)) {
      console.log("ChatGPT composer ready");
      return {
        browser,
        context,
        page,
        async close() {
          await browser.close().catch(() => {});
        },
      };
    }
    await sleep(1000);
  }

  await screenshot(page, "chatgpt-guest-no-composer");
  await browser.close().catch(() => {});
  throw new Error(
    "ChatGPT message box not found in guest mode. Check screenshot in screenshots/"
  );
}

export async function openChatGPT(_browser, opts = {}) {
  return openChatGPTGuest({ headless: opts.headless === true });
}

async function getComposer(page) {
  const candidates = [
    page.locator("#prompt-textarea"),
    page.locator('[data-testid="composer-text-input"]'),
    page.locator('div[contenteditable="true"]').last(),
    page.locator("textarea").last(),
  ];
  for (const loc of candidates) {
    try {
      const el = loc.first();
      if (await el.isVisible({ timeout: 2000 })) return el;
    } catch {
      /* next */
    }
  }
  throw new Error("ChatGPT message box not found");
}

async function sendMessage(page, text) {
  const box = await getComposer(page);
  await box.click();
  await page.keyboard.press(process.platform === "darwin" ? "Meta+A" : "Control+A");
  await page.keyboard.press("Backspace");

  const tag = await box.evaluate((el) => el.tagName.toLowerCase());
  if (tag !== "textarea") {
    await box.evaluate((el, value) => {
      el.focus();
      el.innerText = value;
      el.dispatchEvent(new InputEvent("input", { bubbles: true }));
    }, text);
  } else {
    await box.fill(text);
  }

  await sleep(400);

  const sendBtn = page
    .locator(
      '[data-testid="send-button"], button[aria-label*="Send"], button[data-testid="composer-send-button"]'
    )
    .first();
  try {
    if (await sendBtn.isVisible({ timeout: 2000 })) await sendBtn.click();
    else await page.keyboard.press("Enter");
  } catch {
    await page.keyboard.press("Enter");
  }
}

async function waitForReplyDone(page, { timeoutMs = 180000 } = {}) {
  const start = Date.now();
  let sawStreaming = false;
  while (Date.now() - start < timeoutMs) {
    const stop = page.locator(
      'button[aria-label*="Stop"], button[data-testid="stop-button"], button:has-text("Stop generating")'
    );
    const streaming = await stop.first().isVisible().catch(() => false);
    if (streaming) sawStreaming = true;
    if (sawStreaming && !streaming) {
      await sleep(1200);
      return;
    }
    const assistant = page.locator('[data-message-author-role="assistant"]').last();
    const hasMsg = await assistant.isVisible().catch(() => false);
    if (hasMsg && !streaming && Date.now() - start > 8000) {
      const t1 = await assistant.innerText().catch(() => "");
      await sleep(2500);
      const t2 = await assistant.innerText().catch(() => "");
      if (t1 && t1 === t2 && t1.length > 40) return;
    }
    await sleep(1000);
  }
  throw new Error("Timed out waiting for ChatGPT reply");
}

async function lastAssistantText(page) {
  const assistant = page.locator('[data-message-author-role="assistant"]').last();
  try {
    await assistant.waitFor({ state: "visible", timeout: 30000 });
    return (await assistant.innerText()).trim();
  } catch {
    return (await page.locator("main").innerText().catch(() => "")).trim();
  }
}

async function lastAssistantCodeBlocks(page) {
  const root = page.locator('[data-message-author-role="assistant"]').last();
  try {
    await root.waitFor({ state: "visible", timeout: 15000 });
  } catch {
    return [];
  }
  const blocks = await root.locator("pre code").allTextContents().catch(() => []);
  return blocks.map((b) => b.trim()).filter(Boolean);
}

function scoreCode(s, lang) {
  let score = 0;
  if (lang === "mysql") {
    if (/\bSELECT\b/i.test(s)) score += 8;
    if (/\bFROM\b/i.test(s)) score += 3;
    if (/\bJOIN\b/i.test(s)) score += 2;
    if (/\bGROUP\s+BY\b/i.test(s)) score += 2;
    if (/\bWHERE\b/i.test(s)) score += 1;
  } else {
    if (/class\s+Solution/.test(s)) score += 8;
    if (/public\s*:/.test(s)) score += 3;
    if (/#include/.test(s)) score += 1;
    if (/int\s+\w+\s*\(/.test(s)) score += 2;
    if (/vector\s*</.test(s)) score += 2;
    if (/def\s+\w+\(/.test(s)) score += lang === "python3" ? 5 : 0;
  }
  if (s.length > 40) score += 1;
  if (s.length > 120) score += 1;
  return score;
}

export function extractCode(reply, lang = "cpp") {
  const fenceLang =
    lang === "python3"
      ? "python|py|python3"
      : lang === "cpp"
        ? "cpp|c\\+\\+|cplusplus|c"
        : lang === "mysql"
          ? "sql|mysql|sqlite"
          : lang;
  const preferred = new RegExp("```(?:" + fenceLang + ")\\s*([\\s\\S]*?)```", "i");
  const m1 = reply.match(preferred);
  if (m1?.[1]?.trim()) return m1[1].trim();

  const any = [...reply.matchAll(/```(?:\w+)?\s*([\s\S]*?)```/g)].map((m) => m[1].trim());
  if (any.length) {
    any.sort((a, b) => scoreCode(b, lang) - scoreCode(a, lang));
    if (scoreCode(any[0], lang) > 0) return any[0];
  }

  if (lang === "mysql") {
    const sql = reply.match(/((?:WITH|SELECT)\b[\s\S]+)/i);
    if (sql?.[1] && scoreCode(sql[1], lang) >= 8) return sql[1].trim();
  } else {
    const bare =
      reply.match(/(class\s+Solution\s*\{[\s\S]*?\n\};?)/) ||
      reply.match(/(class\s+Solution[\s\S]+)/) ||
      reply.match(/(def\s+\w+\([\s\S]+)/);
    if (bare?.[1] && scoreCode(bare[1], lang) >= 5) return bare[1].trim();
  }

  throw new Error("Could not extract code from ChatGPT reply");
}

export function buildSolvePrompt(problemText, { lang, starterCode }) {
  const label = LANG_LABEL[lang] || lang;
  if (lang === "mysql") {
    return [
      "Solve this LeetCode SQL problem in MySQL.",
      "Return ONLY one complete SQL query in a single markdown ```sql code fence.",
      "No explanation.",
      "",
      problemText,
      starterCode ? `\nStarter:\n\`\`\`\n${starterCode}\n\`\`\`` : "",
    ]
      .filter(Boolean)
      .join("\n");
  }
  return [
    `Solve this LeetCode problem in ${label}.`,
    "Return ONLY one complete solution in a single markdown ```cpp code fence.",
    "Use class Solution. No explanations outside the fence.",
    "",
    problemText,
    starterCode ? `\nStarter:\n\`\`\`\n${starterCode}\n\`\`\`` : "",
  ]
    .filter(Boolean)
    .join("\n");
}

export function buildFixPrompt(errorText, previousCode, { lang }) {
  const label = LANG_LABEL[lang] || lang;
  const fence = lang === "mysql" ? "sql" : "cpp";
  return [
    `My LeetCode submission in ${label} failed. Fix it.`,
    `Return ONLY the full corrected solution in one markdown \`\`\`${fence} fence.`,
    "",
    "=== JUDGE ERROR ===",
    errorText,
    "",
    "=== MY CODE ===",
    "```",
    previousCode,
    "```",
  ].join("\n");
}

export function formatJudgeError(result) {
  const parts = [
    `Status: ${result.status_msg || result.state || "Unknown"}`,
    result.status_runtime ? `Runtime: ${result.status_runtime}` : "",
    result.status_memory ? `Memory: ${result.status_memory}` : "",
  ];
  if (result.total_correct != null && result.total_testcases != null) {
    parts.push(`Passed: ${result.total_correct}/${result.total_testcases}`);
  }
  if (result.last_testcase) parts.push(`Last testcase:\n${result.last_testcase}`);
  if (result.code_output != null) {
    const out = Array.isArray(result.code_output)
      ? result.code_output.join("\n")
      : String(result.code_output);
    if (out.trim()) parts.push(`Your output:\n${out}`);
  }
  if (result.expected_output) parts.push(`Expected:\n${result.expected_output}`);
  if (result.runtime_error) parts.push(`Runtime error:\n${result.runtime_error}`);
  if (result.compile_error) parts.push(`Compile error:\n${result.compile_error}`);
  return parts.filter(Boolean).join("\n");
}

export async function askChatGPTForCode(page, prompt, lang) {
  console.log("  → pasting prompt into ChatGPT…");
  await sendMessage(page, prompt);
  console.log("  → waiting for ChatGPT to finish…");
  await waitForReplyDone(page);
  console.log("  → extracting code from reply…");

  const domBlocks = await lastAssistantCodeBlocks(page);
  if (domBlocks.length) {
    domBlocks.sort((a, b) => scoreCode(b, lang) - scoreCode(a, lang));
    if (scoreCode(domBlocks[0], lang) >= 5) {
      console.log(`  → got ${domBlocks[0].split("\n").length} lines (from code block)`);
      return domBlocks[0];
    }
  }

  const reply = await lastAssistantText(page);
  try {
    const code = extractCode(reply, lang);
    console.log(`  → got ${code.split("\n").length} lines of code`);
    return code;
  } catch {
    console.log("  → retrying with code-only ask…");
    await sendMessage(
      page,
      lang === "mysql"
        ? "Return ONLY the complete MySQL query as one markdown ```sql fence. No explanation."
        : `Return ONLY the complete LeetCode ${LANG_LABEL[lang] || lang} solution as one markdown code fence. class Solution required.`
    );
    await waitForReplyDone(page);
    const dom2 = await lastAssistantCodeBlocks(page);
    if (dom2.length) {
      dom2.sort((a, b) => scoreCode(b, lang) - scoreCode(a, lang));
      if (scoreCode(dom2[0], lang) >= 5) return dom2[0];
    }
    return extractCode(await lastAssistantText(page), lang);
  }
}

export async function startFreshChat(page) {
  try {
    const neu = page
      .getByRole("link", { name: /new chat/i })
      .or(page.getByRole("button", { name: /new chat/i }));
    if (await neu.first().isVisible({ timeout: 2000 })) {
      await neu.first().click();
      await sleep(1500);
      return;
    }
  } catch {
    /* ignore */
  }
  await page.goto(CHATGPT_URL, { waitUntil: "domcontentloaded", timeout: 60000 }).catch(() => {});
  await sleep(2000);
  await dismissGuestPrompts(page);
}
