/**
 * Opens real Google Chrome with remote debugging (for Cloudflare-safe login).
 * Usage:
 *   node src/open-chrome.js chatgpt   → port 9222
 *   node src/open-chrome.js leetcode  → port 9223
 */
import { startRealChrome, PROFILE_PORTS } from "./chrome-cdp.js";

const which = (process.argv[2] || "chatgpt").toLowerCase();
const profile = which === "leetcode" ? "leetcode" : "chatgpt";
const url =
  profile === "leetcode"
    ? "https://leetcode.com/accounts/login/"
    : "https://chatgpt.com/";

const port = PROFILE_PORTS[profile];
await startRealChrome({ profile, port, url, force: true });
console.log(`\n${profile} Chrome is open on :${port}`);
console.log("Log in there if needed, then run:");
console.log(profile === "leetcode" ? "  npm run login-only" : "  npm run chatgpt-login");
process.exit(0);
