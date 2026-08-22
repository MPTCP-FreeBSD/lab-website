#!/usr/bin/env bash
# Launch Hugo dev server for this site.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

if ! command -v hugo >/dev/null 2>&1; then
  echo "hugo not found. Install it: https://gohugo.io/installation/" >&2
  exit 1
fi

hugo server --buildDrafts --buildFuture --disableFastRender "$@"
