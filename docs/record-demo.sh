#!/usr/bin/env bash
# Regenerate docs/images/i18n-security-lint-demo.{cast,gif} from a live linter run.
# Requires: python3, agg (brew install agg), optional gifsicle.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TOOL="$ROOT/tools/i18n-security-lint"
VENV="$TOOL/.venv"
LINT="$VENV/bin/i18n-security-lint"
IMG="$ROOT/docs/images"
DEMO_LOCALES="$ROOT/docs/demo-locales"

mkdir -p "$IMG" "$DEMO_LOCALES"
if [[ ! -x "$LINT" ]]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -e "$TOOL" -q
fi

# Keep demo fixtures in sync with the tool corpus
cp "$TOOL"/tests/corpus/* "$DEMO_LOCALES/"

python3 - "$LINT" "$DEMO_LOCALES" "$IMG/i18n-security-lint-demo.cast" <<'PY'
import json, sys, time, pathlib, subprocess
lint, locales, cast_path = sys.argv[1], pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
files = sorted(str(p) for p in locales.glob("*") if p.is_file())
proc = subprocess.run([lint, "--strict", *files], capture_output=True, text=True)
output = (proc.stdout or "") + (proc.stderr or "")
output = output.replace(str(locales.parent) + "/", "").replace(str(locales) + "/", "locales/")
# Also collapse absolute leftover paths to locales/
import re
output = re.sub(r"/[^\s\n]+/docs/demo-locales/", "locales/", output)
if not output.endswith("\n"):
    output += "\n"

header = {
    "version": 2,
    "width": 80,
    "height": 26,
    "timestamp": int(time.time()),
    "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"},
    "title": "i18n-security-lint — 60-second locale scan",
}
events, t = [], 0.1

def emit(delay, text):
    global t
    t += delay
    events.append([round(t, 3), "o", text])

emit(0.0, "\u001b[1;32m$\u001b[0m pip install i18n-security-lint\n")
emit(0.55, "\u001b[90mSuccessfully installed i18n-security-lint-0.1.0\u001b[0m\n")
emit(0.45, "\u001b[1;32m$\u001b[0m i18n-security-lint --strict locales/\n")
emit(0.55, "")
for line in output.splitlines(True):
    emit(0.07, line)
emit(0.35, f"\n\u001b[1;31m# exit {proc.returncode} — fails CI under --strict\u001b[0m\n")
emit(1.0, "")

with cast_path.open("w", encoding="utf-8") as f:
    f.write(json.dumps(header) + "\n")
    for ev in events:
        f.write(json.dumps(ev) + "\n")
print(f"wrote {cast_path} (linter exit {proc.returncode})")
PY

agg --font-size 13 --speed 1.25 --theme monokai \
  "$IMG/i18n-security-lint-demo.cast" \
  "$IMG/i18n-security-lint-demo.gif"

if command -v gifsicle >/dev/null 2>&1; then
  gifsicle -O3 --colors 128 \
    "$IMG/i18n-security-lint-demo.gif" \
    -o "$IMG/i18n-security-lint-demo.gif"
fi

ls -lh "$IMG/i18n-security-lint-demo.gif"
echo "Done. Embed path: docs/images/i18n-security-lint-demo.gif"
