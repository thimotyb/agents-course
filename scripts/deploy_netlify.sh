#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PUBLISH_DIR="${ROOT_DIR}/site"
DEPLOY_MSG="${1:-manual deploy from agents-course}"

if [[ ! -d "${PUBLISH_DIR}" ]]; then
  echo "[error] Missing publish directory: ${PUBLISH_DIR}" >&2
  exit 1
fi

if [[ -z "${NETLIFY_AUTH_TOKEN:-}" ]]; then
  echo "[error] NETLIFY_AUTH_TOKEN is not set." >&2
  echo "        Use the same token/account used for ai-ttt-course." >&2
  exit 1
fi

if [[ -z "${NETLIFY_SITE_ID:-}" ]]; then
  echo "[error] NETLIFY_SITE_ID is not set." >&2
  echo "        Set it to the target Netlify site id." >&2
  exit 1
fi

echo "[info] Deploying ${PUBLISH_DIR} to Netlify site ${NETLIFY_SITE_ID}"
npx --yes netlify-cli deploy \
  --prod \
  --dir "${PUBLISH_DIR}" \
  --site "${NETLIFY_SITE_ID}" \
  --auth "${NETLIFY_AUTH_TOKEN}" \
  --message "${DEPLOY_MSG}"
