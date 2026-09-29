#!/usr/bin/env bash
set -euo pipefail
repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
export RUNTIME_NODE="${RUNTIME_NODE:-${CODEX_PRIMARY_RUNTIME_NODE:-$(command -v node)}}"
export RUNTIME_NODE_MODULES="${RUNTIME_NODE_MODULES:-${CODEX_PRIMARY_RUNTIME_NODE_MODULES:-}}"
export RUNTIME_PYTHON="${RUNTIME_PYTHON:-${CODEX_PRIMARY_RUNTIME_PYTHON:-$(command -v python3)}}"
export XINEW_PYTHON="$RUNTIME_PYTHON"
export PRESENTATIONS_SKILL="${PRESENTATIONS_SKILL:-/root/.codex/skills/builtins/presentations}"
export RUNTIME_BIN_DIR="${RUNTIME_BIN_DIR:-${CODEX_PRIMARY_RUNTIME_ROOT:-/opt/codex/runtimes/codex-primary-runtime}/dependencies/bin/override}"
export PYTHONPATH="$repo_root/.cloud-deps${PYTHONPATH:+:$PYTHONPATH}"
export PATH="$RUNTIME_BIN_DIR:$(dirname "$RUNTIME_NODE"):$PATH"
if [[ $# -eq 0 ]]; then
  echo 'Usage: ./cloud-runtime.sh python pipeline/academy.py doctor' >&2
  exit 2
fi
"$RUNTIME_PYTHON" "$repo_root/pipeline/restore_shared_assets.py"
if [[ "$1" == python || "$1" == python3 ]]; then
  shift
  exec "$RUNTIME_PYTHON" "$@"
fi
exec "$@"
