# Optional Linux host image. On Mac: skip Docker — use cron + local Chrome (best for CAPTCHA).
FROM mcr.microsoft.com/playwright:v1.50.1-jammy

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY src ./src

# Persistent dirs mounted at runtime
RUN mkdir -p /app/.chrome-profile-leetcode

CMD ["npm", "run", "daily"]
