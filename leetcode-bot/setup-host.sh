#!/usr/bin/env bash
# Run once on the always-on laptop (Mac or Linux) that will host the bot.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

echo "==> Node check"
if ! command -v node >/dev/null; then
  echo "Install Node 20+ first: https://nodejs.org"
  exit 1
fi
node -v

echo "==> npm install"
npm install
npx playwright install chrome 2>/dev/null || npx playwright install chromium

if [[ ! -f src/config.js ]]; then
  echo "==> Creating src/config.js from example — fill credentials, then re-run"
  cp src/config.example.js src/config.js
  echo "Edit: $ROOT/src/config.js"
  exit 1
fi

echo "==> One-time LeetCode login (click CAPTCHA in Chrome if shown)"
npm run login-only

echo ""
echo "==> Done. Test with: npm run daily"
echo ""
echo "Add daily cron at 11:30 AM (Mac local time):"
echo "  crontab -e"
echo "  Then paste:"
if command -v npm >/dev/null; then
  NPM="$(command -v npm)"
else
  NPM="npm"
fi
echo "  30 11 * * * cd $ROOT && $NPM run daily >> /tmp/lc-bot.log 2>&1"
echo ""
echo "Telegram will notify on start / finish / CAPTCHA re-login."
