#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
SITE_DIR="$SCRIPT_DIR/site"
PORT="${1:-8000}"

if [[ ! -d "$SITE_DIR" ]]; then
  printf 'Errore: directory del sito non trovata: %s\n' "$SITE_DIR" >&2
  exit 1
fi

printf 'Sito disponibile su http://localhost:%s/\n' "$PORT"
printf 'Directory pubblicata: %s\n' "$SITE_DIR"
printf 'Premi Ctrl+C per arrestare il server.\n'

exec python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$SITE_DIR"
