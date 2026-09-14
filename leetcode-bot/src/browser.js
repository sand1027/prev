import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { chromium } from "playwright";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

/** Separate profiles so LeetCode / ChatGPT sessions don't step on each other */
export const PROFILES = {
  shared: path.join(__dirname, "..", ".chrome-profile"),
  leetcode: path.join(__dirname, "..", ".chrome-profile-leetcode"),
  chatgpt: path.join(__dirname, "..", ".chrome-profile-chatgpt"),
};

/**
 * Real Chrome + persistent profile = fewer "I'm not a robot" blocks.
 * You still must click the checkbox yourself when it appears.
 */
export async function launchBrowser({
  headless = false,
  persistent = false,
  profile = "shared",
} = {}) {
  const args = [
    "--disable-blink-features=AutomationControlled",
    "--no-first-run",
    "--no-default-browser-check",
  ];

  const common = {
    headless,
    channel: "chrome",
    args,
    ignoreDefaultArgs: ["--enable-automation"],
  };

  if (persistent) {
    const dir = PROFILES[profile] || PROFILES.shared;
    fs.mkdirSync(dir, { recursive: true });
    const context = await chromium.launchPersistentContext(dir, {
      ...common,
      viewport: { width: 1400, height: 900 },
    });
    await stealth(context);
    return { browser: context.browser(), context, persistent: true, profileDir: dir };
  }

  const browser = await chromium.launch(common);
  return { browser, context: null, persistent: false };
}

export async function newStealthContext(browser, { storageState } = {}) {
  const context = await browser.newContext({
    storageState,
    viewport: { width: 1400, height: 900 },
  });
  await stealth(context);
  return context;
}

async function stealth(context) {
  await context.addInitScript(() => {
    Object.defineProperty(navigator, "webdriver", { get: () => undefined });
    // @ts-ignore
    window.chrome = window.chrome || { runtime: {} };
    Object.defineProperty(navigator, "plugins", { get: () => [1, 2, 3] });
    Object.defineProperty(navigator, "languages", { get: () => ["en-US", "en"] });
  });
}
