#!/usr/bin/env bash
set -euo pipefail
root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
py="${RUNTIME_PYTHON:-$root/.venv/bin/python}"
[[ -x "$py" ]] || { echo 'Run ./setup-portable.sh first (Python 3.11+)' >&2; exit 2; }
export XINEW_PYTHON="$py"
export PYTHONPATH="$root/pipeline${PYTHONPATH:+:$PYTHONPATH}"
"$py" "$root/pipeline/restore_shared_assets.py"
[[ $# -gt 0 ]] || { echo 'Usage: ./portable-runtime.sh python pipeline/preflight.py' >&2; exit 2; }
if [[ "$1" == python || "$1" == python3 ]]; then shift; exec "$py" "$@"; fi
exec "$@"
