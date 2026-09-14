/**
 * OpenAI-compatible LLM client (OpenRouter, NVIDIA NIM, OpenAI, etc.)
 * No ChatGPT browser — just HTTP.
 */
import { extractCode } from "./chatgpt.js";

export function llmConfigFrom(CONFIG) {
  const provider = (CONFIG.LLM_PROVIDER || "nvidia").toLowerCase();
  const key = CONFIG.LLM_API_KEY || CONFIG.NVIDIA_API_KEY || "";

  const defaults = {
    nvidia: {
      baseUrl: "https://integrate.api.nvidia.com/v1",
      model: "meta/llama-3.1-70b-instruct",
    },
    openrouter: {
      baseUrl: "https://openrouter.ai/api/v1",
      model: "qwen/qwen3-coder:free",
    },
    openai: {
      baseUrl: "https://api.openai.com/v1",
      model: "gpt-4o-mini",
    },
  };

  const d = defaults[provider] || defaults.nvidia;
  return {
    provider,
    apiKey: key,
    baseUrl: (CONFIG.LLM_BASE_URL || d.baseUrl).replace(/\/$/, ""),
    model: CONFIG.LLM_MODEL || d.model,
    siteUrl: CONFIG.LLM_SITE_URL || "https://github.com/leetcode-bot",
    siteName: CONFIG.LLM_SITE_NAME || "leetcode-bot",
  };
}

export function assertLlmConfig(cfg) {
  if (!cfg.apiKey || String(cfg.apiKey).startsWith("PASTE_")) {
    throw new Error("Set LLM_API_KEY in src/config.js (NVIDIA nvapi-…). See config.example.js");
  }
}

/**
 * Chat Completions — works with OpenRouter, NVIDIA NIM, OpenAI.
 */
export async function chatComplete(cfg, messages, { temperature = 0.2, maxTokens = 8192 } = {}) {
  const url = `${cfg.baseUrl}/chat/completions`;
  const headers = {
    Authorization: `Bearer ${cfg.apiKey}`,
    "Content-Type": "application/json",
  };
  // OpenRouter optional ranking headers
  if (cfg.provider === "openrouter") {
    headers["HTTP-Referer"] = cfg.siteUrl;
    headers["X-Title"] = cfg.siteName;
  }

  const res = await fetch(url, {
    method: "POST",
    headers,
    body: JSON.stringify({
      model: cfg.model,
      messages,
      temperature,
      max_tokens: maxTokens,
    }),
  });

  const raw = await res.text();
  let data;
  try {
    data = JSON.parse(raw);
  } catch {
    throw new Error(`LLM HTTP ${res.status}: ${raw.slice(0, 300)}`);
  }

  if (!res.ok) {
    const msg = data?.error?.message || data?.message || raw.slice(0, 300);
    throw new Error(`LLM HTTP ${res.status}: ${msg}`);
  }

  const content = data?.choices?.[0]?.message?.content;
  if (!content) throw new Error("LLM returned empty content");
  return content;
}

export async function askLlmForCode(cfg, prompt, lang) {
  console.log(`  → LLM (${cfg.provider}/${cfg.model})…`);
  const system =
    lang === "mysql"
      ? "You are a LeetCode SQL expert. Reply with ONLY one complete MySQL query in a ```sql fence. No explanation."
      : "You are a LeetCode C++ expert. Reply with ONLY one complete solution in a ```cpp fence using class Solution. No explanation.";

  const reply = await chatComplete(cfg, [
    { role: "system", content: system },
    { role: "user", content: prompt },
  ]);

  try {
    const code = extractCode(reply, lang);
    console.log(`  → got ${code.split("\n").length} lines of code`);
    return code;
  } catch {
    console.log("  → retry: asking for code-only fence…");
    const retry = await chatComplete(cfg, [
      { role: "system", content: system },
      { role: "user", content: prompt },
      { role: "assistant", content: reply },
      {
        role: "user",
        content:
          lang === "mysql"
            ? "Return ONLY the complete MySQL query as one markdown ```sql fence. No explanation."
            : "Return ONLY the complete C++ LeetCode solution as one markdown ```cpp fence. class Solution required. No explanation.",
      },
    ]);
    const code = extractCode(retry, lang);
    console.log(`  → got ${code.split("\n").length} lines of code`);
    return code;
  }
}
