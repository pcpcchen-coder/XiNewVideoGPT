#!/usr/bin/env bash
# Run from anywhere; Python dependencies remain inside academy/.venv.
set -euo pipefail
root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
python_bin="${RUNTIME_PYTHON:-python3}"
"$python_bin" -c 'import sys; assert sys.version_info >= (3,11), "Python 3.11+ required"'
[[ -x "$root/.venv/bin/python" ]] || "$python_bin" -m venv "$root/.venv"
"$root/.venv/bin/python" -m pip install -r "$root/requirements-cloud.txt"
if command -v fc-cache >/dev/null; then
  font_dir="${XDG_DATA_HOME:-$HOME/.local/share}/fonts/xinew"
  mkdir -p "$font_dir"
  cp "$root/assets/fonts/NotoSansCJKtc-Regular.otf" "$font_dir/"
  fc-cache -f "$font_dir"
fi
"$root/.venv/bin/python" "$root/pipeline/restore_shared_assets.py" --verify
"$root/.venv/bin/python" "$root/pipeline/preflight.py"
