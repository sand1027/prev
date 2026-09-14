export const CONFIG = {
  // Playwright re-login (required for long-term hosting — no 15-day cookie paste)
  LEETCODE_USERNAME: "PASTE_LEETCODE_USERNAME_OR_EMAIL",
  LEETCODE_PASSWORD: "PASTE_LEETCODE_PASSWORD",

  LLM_PROVIDER: "nvidia",
  LLM_API_KEY: "PASTE_NVIDIA_API_KEY",
  LLM_BASE_URL: "https://integrate.api.nvidia.com/v1",
  LLM_MODEL: "meta/llama-3.1-70b-instruct",

  TELEGRAM_BOT_TOKEN: "PASTE_TELEGRAM_BOT_TOKEN",
  TELEGRAM_CHAT_ID: "PASTE_TELEGRAM_CHAT_ID",

  LANG: "cpp",
  MAX_FIX_ROUNDS: 5,
  HEADLESS: false,
  KEEP_OPEN_ON_FAIL: true,
  ALLOW_BROWSER_LOGIN: true,

  SOLVE_DAILY: true,
  PROBLEMS_PER_DAY: 3,
  PROBLEM_POOL: ["EASY", "MEDIUM", "HARD", "SQL"],
};
