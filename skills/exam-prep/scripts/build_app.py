#!/usr/bin/env python3
"""Build the offline mock-exam app: one HTML file holding the spec and the bank.

    build_app.py SPEC BANK -o exam.html [--force] [--template assets/exam-app.html]

The bank is checked first (bank_tool.py check); the build stops on any error
unless --force is given. The result opens from disk in any modern browser, with
no network access, and keeps its history in the browser's local storage under
the spec's id.
"""
import argparse
import html
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bank_tool as bt  # noqa: E402

TEMPLATE = HERE.parent / "assets" / "exam-app.html"


def embed(value):
    """JSON safe inside a <script> element: no '<' can open a tag or a comment."""
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")


def main(argv=None):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("spec")
    p.add_argument("bank")
    p.add_argument("-o", "--out", required=True)
    p.add_argument("--template", default=str(TEMPLATE))
    p.add_argument("--force", action="store_true", help="build even when the check finds errors")
    a = p.parse_args(argv)

    spec, bank, raw = bt.load(a.spec, a.bank)
    rep = bt.check(spec, bank)
    for iid, msg in rep.errors[:40]:
        print(f"ERROR {iid}: {msg}")
    if rep.errors and not a.force:
        print(f"{len(rep.errors)} errors: not building (fix them, or pass --force)")
        return 1
    page = Path(a.template).read_text(encoding="utf-8")
    for marker in ("/*SPEC*/", "/*BANK*/"):
        if page.count(marker) != 1:
            print(f"template must contain {marker} exactly once")
            return 1
    title = bt.loc(spec.get("title"), bt.langs(spec)[0]) or "Mock exam"
    page = page.replace("<title>Mock exam</title>", f"<title>{html.escape(title)}</title>", 1)
    page = page.replace('<html lang="en">', f'<html lang="{html.escape(bt.langs(spec)[0])}">', 1)
    page = page.replace("/*SPEC*/", embed(spec), 1).replace("/*BANK*/", embed(raw), 1)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8", newline="\n")
    print(f"{len(bank['items'])} items, {len(rep.warnings)} warnings -> {out} ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
