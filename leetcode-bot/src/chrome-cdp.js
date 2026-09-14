import fs from "fs";
import os from "os";
import path from "path";
import { spawn, execSync } from "child_process";
import { chromium } from "playwright";
import { PROFILES } from "./browser.js";

/** Separate CDP ports so ChatGPT Chrome ≠ LeetCode Chrome */
export const PROFILE_PORTS = {
  chatgpt: 9222,
  leetcode: 9223,
  shared: 9224,
};

function portFor(profile, port) {
  if (port) return port;
  return PROFILE_PORTS[profile] || PROFILE_PORTS.chatgpt;
}

function chromeExecutable() {
  const mac = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  if (fs.existsSync(mac)) return mac;
  throw new Error(
    "Google Chrome not found at /Applications/Google Chrome.app — install Chrome first"
  );
}

async function isCdpUp(port) {
  try {
    const res = await fetch(`http://127.0.0.1:${port}/json/version`, {
      signal: AbortSignal.timeout(800),
    });
    return res.ok;
  } catch {
    return false;
  }
}

function sleep(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

function isPlainChromeRunning() {
  try {
    execSync('pgrep -x "Google Chrome"', { stdio: "ignore" });
    return true;
  } catch {
    return false;
  }
}

export function killCdpPort(port) {
  try {
    const out = execSync(`lsof -nP -iTCP:${port} -sTCP:LISTEN -t`, {
      encoding: "utf8",
    }).trim();
    if (!out) return false;
    for (const pid of out.split("\n")) {
      const n = Number(pid);
      if (!n || n === process.pid) continue;
      try {
        process.kill(n, "SIGTERM");
        console.log(`Stopped Chrome listener on :${port} (pid ${n})`);
      } catch {
        /* already dead */
      }
    }
    return true;
  } catch {
    return false;
  }
}

/** Quit all Google Chrome apps so the system profile unlocks. */
export function quitGoogleChrome() {
  try {
    execSync(`osascript -e 'tell application "Google Chrome" to quit'`, {
      stdio: "ignore",
      timeout: 8000,
    });
  } catch {
    /* ignore */
  }
  try {
    execSync('killall "Google Chrome"', { stdio: "ignore" });
  } catch {
    /* ignore */
  }
  for (const p of Object.values(PROFILE_PORTS)) {
    killCdpPort(p);
  }
}

function clearChromeLocks(userDataDir) {
  for (const name of ["SingletonLock", "SingletonSocket", "SingletonCookie"]) {
    try {
      fs.unlinkSync(path.join(userDataDir, name));
    } catch {
      /* ignore */
    }
  }
}

/**
 * Resolve which user-data-dir to use for a profile name.
 * ChatGPT can use your real macOS Chrome profile (Google already logged in).
 */
export async function resolveUserDataDir(profile) {
  if (profile !== "chatgpt") {
    const dir = PROFILES[profile] || PROFILES.shared;
    fs.mkdirSync(dir, { recursive: true });
    return { userDataDir: dir, profileDirectory: null, systemChrome: false };
  }

  let CONFIG = {};
  try {
    CONFIG = (await import("./config.js")).CONFIG;
  } catch {
    /* defaults */
  }

  if (CONFIG.CHATGPT_USE_SYSTEM_CHROME) {
    const userDataDir =
      CONFIG.CHROME_USER_DATA_DIR ||
      path.join(os.homedir(), "Library/Application Support/Google/Chrome");
    const profileDirectory = CONFIG.CHROME_PROFILE_DIRECTORY || "Default";
    if (!fs.existsSync(userDataDir)) {
      throw new Error(`Chrome user data not found: ${userDataDir}`);
    }
    return { userDataDir, profileDirectory, systemChrome: true };
  }

  const dir = PROFILES.chatgpt;
  fs.mkdirSync(dir, { recursive: true });
  return { userDataDir: dir, profileDirectory: null, systemChrome: false };
}

/**
 * Open system Chrome profile via Playwright persistent context
 * (more reliable than spawn + remote-debugging-port on macOS).
 */
async function launchSystemChromePersistent({ userDataDir, profileDirectory }, url) {
  console.log("Opening SYSTEM Chrome profile via Playwright…");
  console.log(`  profile: ${userDataDir}`);
  if (profileDirectory) console.log(`  profile-directory: ${profileDirectory}`);

  if (isPlainChromeRunning()) {
    console.log("Quitting Chrome so the profile unlocks…");
    quitGoogleChrome();
    await sleep(3500);
  }
  clearChromeLocks(userDataDir);

  if (isPlainChromeRunning()) {
    throw new Error(
      "Chrome is still running. Press Cmd+Q, then re-run: npm run chatgpt-login"
    );
  }

  const args = ["--disable-blink-features=AutomationControlled"];
  if (profileDirectory) args.push(`--profile-directory=${profileDirectory}`);

  let context;
  try {
    context = await chromium.launchPersistentContext(userDataDir, {
      channel: "chrome",
      headless: false,
      args,
      ignoreDefaultArgs: ["--enable-automation"],
      viewport: { width: 1400, height: 900 },
      timeout: 60000,
    });
  } catch (e) {
    throw new Error(
      `Failed to open system Chrome profile: ${e.message}\n` +
        "Quit Chrome (Cmd+Q) and retry. If it keeps failing, set CHATGPT_USE_SYSTEM_CHROME: false."
    );
  }

  if (url && url !== "about:blank") {
    const page = context.pages()[0] || (await context.newPage());
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 90000 }).catch(() => {});
  }

  return {
    browser: context.browser(),
    context,
    async close() {
      // Saves profile (cookies / Google session) to disk
      await context.close().catch(() => {});
    },
  };
}

export async function startRealChrome({
  profile = "chatgpt",
  port,
  url = "about:blank",
  force = false,
} = {}) {
  port = portFor(profile, port);

  if (force) {
    killCdpPort(port);
    await sleep(1200);
  } else if (await isCdpUp(port)) {
    console.log(`Reusing ${profile} Chrome on :${port}`);
    return { port, started: false, profile };
  }

  if (await isCdpUp(port)) {
    console.log(`Reusing ${profile} Chrome on :${port}`);
    return { port, started: false, profile };
  }

  const { userDataDir, profileDirectory } = await resolveUserDataDir(profile);
  fs.mkdirSync(userDataDir, { recursive: true });

  const exe = chromeExecutable();
  console.log(`Starting ${profile} Chrome (CDP :${port})…`);
  console.log(`  profile: ${userDataDir}`);

  const args = [
    `--remote-debugging-port=${port}`,
    `--user-data-dir=${userDataDir}`,
    "--no-first-run",
    "--no-default-browser-check",
    "--disable-blink-features=AutomationControlled",
    "--new-window",
  ];
  if (profileDirectory) args.push(`--profile-directory=${profileDirectory}`);
  args.push(url);

  const child = spawn(exe, args, { detached: true, stdio: "ignore" });
  child.unref();

  const deadline = Date.now() + 30000;
  while (Date.now() < deadline) {
    if (await isCdpUp(port)) {
      console.log("Chrome CDP ready");
      return { port, started: true, pid: child.pid, profile };
    }
    await sleep(400);
  }
  throw new Error(`Chrome did not open CDP on port ${port}`);
}

export async function connectRealChrome({ port, profile = "chatgpt" } = {}) {
  port = portFor(profile, port);
  if (!(await isCdpUp(port))) {
    throw new Error(`No Chrome on port ${port}. Run: npm run open-chrome ${profile}`);
  }

  const browser = await chromium.connectOverCDP(`http://127.0.0.1:${port}`, {
    timeout: 20000,
  });

  const contexts = browser.contexts();
  if (!contexts.length) {
    await browser.close().catch(() => {});
    throw new Error(
      `CDP Chrome has no default context. Quit Chrome on :${port}, then retry.`
    );
  }

  return { browser, context: contexts[0], port };
}

/**
 * ChatGPT + system Chrome → Playwright persistent context (reliable).
 * LeetCode / bot profiles → CDP spawn (as before).
 */
export async function useRealChrome({
  profile = "chatgpt",
  port,
  url = "about:blank",
  force = false,
} = {}) {
  const resolved = await resolveUserDataDir(profile);

  if (profile === "chatgpt" && resolved.systemChrome) {
    return launchSystemChromePersistent(resolved, url);
  }

  port = portFor(profile, port);
  await startRealChrome({ profile, port, url, force });

  try {
    const { browser, context } = await connectRealChrome({ port, profile });
    return wrap(browser, context);
  } catch (err) {
    const msg = String(err?.message || err);
    if (!/context management|setDownloadBehavior|connectOverCDP/i.test(msg)) {
      throw err;
    }

    console.log(`\nCDP attach broken on :${port} — restarting ${profile} Chrome…\n`);
    await startRealChrome({ profile, port, url, force: true });
    const { browser, context } = await connectRealChrome({ port, profile });
    return wrap(browser, context);
  }
}

function wrap(browser, context) {
  return {
    browser,
    context,
    async close() {
      await browser.close().catch(() => {});
    },
  };
}
