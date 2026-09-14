/**
 * Telegram notifications — same pattern as .github/workflows/leetcode.yml
 */
export function telegramConfigFrom(CONFIG) {
  return {
    token: CONFIG.TELEGRAM_BOT_TOKEN || process.env.TELEGRAM_BOT_TOKEN || "",
    chatId: CONFIG.TELEGRAM_CHAT_ID || process.env.TELEGRAM_CHAT_ID || "",
  };
}

export async function sendTelegram(cfg, text) {
  const token = (cfg.token || "").trim();
  const chatId = (cfg.chatId || "").trim();
  if (!token || !chatId || token.startsWith("PASTE_")) {
    console.log("Telegram skipped (set TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID)");
    return false;
  }

  const url = `https://api.telegram.org/bot${token}/sendMessage`;
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      chat_id: chatId,
      text,
      disable_web_page_preview: true,
    }),
  });
  const body = await res.text();
  if (!res.ok) {
    console.log(`Telegram failed HTTP ${res.status}: ${body.slice(0, 200)}`);
    return false;
  }
  console.log("Telegram sent");
  return true;
}

export function formatRunSummary({ results, perDay, okCount, error }) {
  if (error) {
    return [
      "❌ LeetCode bot FAILED",
      String(error).slice(0, 500),
      "Update LEETCODE_SESSION / LEETCODE_CSRF if session expired.",
    ].join("\n");
  }

  const lines = (results || []).map(
    (r) => `${r.ok ? "✅" : "❌"} [${r.label}] ${r.title} (${r.difficulty}) — ${r.status}`
  );
  return [
    "🏁 LeetCode bot finished",
    `Accepted ${okCount}/${results?.length ?? 0}`,
    `Pace @ ${perDay}/day × 365 ≈ ${perDay * 365}`,
    "",
    ...lines,
  ].join("\n");
}
