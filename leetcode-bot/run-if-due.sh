#!/usr/bin/env bash
# Runs the daily bot if it hasn't succeeded yet today (local date).
# Safe to call from launchd every few minutes + at the scheduled hour.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
STAMP="$ROOT/.last-success-date"
LOG="${LOG:-/tmp/lc-bot.log}"
TODAY="$(date +%F)"

# Only after this hour:minute (local). Override via env if needed.
TARGET_HOUR="${TARGET_HOUR:-8}"
TARGET_MIN="${TARGET_MIN:-0}"

now_hm=$((10#$(date +%H) * 60 + 10#$(date +%M)))
target_hm=$((10#$TARGET_HOUR * 60 + 10#$TARGET_MIN))

if (( now_hm < target_hm )); then
  exit 0
fi

if [[ -f "$STAMP" ]] && [[ "$(cat "$STAMP")" == "$TODAY" ]]; then
  exit 0
fi

echo "===== $(date) starting daily =====" >>"$LOG"
cd "$ROOT"

# Keep Mac awake while solving
if /usr/bin/caffeinate -dims /opt/homebrew/bin/npm run daily >>"$LOG" 2>&1; then
  echo "$TODAY" >"$STAMP"
  echo "===== $(date) success =====" >>"$LOG"
else
  echo "===== $(date) failed (exit $?) =====" >>"$LOG"
  exit 1
fi
