#!/bin/bash
# Run the in-browser audit at a given frame width; prints the findings.
cd "$(dirname "$0")"
C="${CHROME:-/c/Program Files/Google/Chrome/Application/chrome.exe}"
W=$(cygpath -w "$PWD")
"$C" --headless=new --disable-gpu --allow-file-access-from-files --user-data-dir="$W\audit-prof" --window-size=1400,1000 \
  --virtual-time-budget=${2:-60000} --dump-dom "file:///$(cygpath -m "$PWD")/audit.html?w=$1" 2>/dev/null \
  | python -c "import sys,html,re; t=sys.stdin.read(); m=re.search(r'<pre id=\"out\">(.*?)</pre>',t,re.S); print(html.unescape(m.group(1)) if m else t[-500:])"
