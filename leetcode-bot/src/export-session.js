/**
 * Print LEETCODE_SESSION + csrftoken from .cookies.json for GitHub secrets.
 * Usage: node src/export-session.js
 */
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const root = path.join(path.dirname(fileURLToPath(import.meta.url)), "..");
const file = path.join(root, ".cookies.json");
if (!fs.existsSync(file)) {
  console.error("No .cookies.json — run: npm run login-only");
  process.exit(1);
}
const cookies = JSON.parse(fs.readFileSync(file, "utf8"));
const session = cookies.find((c) => c.name === "LEETCODE_SESSION")?.value;
const csrf = cookies.find((c) => c.name === "csrftoken")?.value;
if (!session || !csrf) {
  console.error("Missing LEETCODE_SESSION or csrftoken in .cookies.json");
  process.exit(1);
}
console.log("Add these as GitHub Actions secrets:\n");
console.log("LEETCODE_SESSION=");
console.log(session);
console.log("\nLEETCODE_CSRF=");
console.log(csrf);
console.log("\nAlso set secret NVIDIA_API_KEY=nvapi-…");
console.log("Telegram: repo Variables TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID (already used by old workflow)");
