"""Blind review: hand a reviewer items without their answers, then compare.

    python bank/blind.py packet <patch.json> <packet.md>      # items from a patch
    python bank/blind.py compare <patch.json> <answers.json>  # reviewer's verdicts against the truth

The packet holds each item's stem, statements and citations in both languages,
and nothing that gives the answer away: no truth, traps, notes, quotes or
options. The reviewer rules every statement true or false from the sources and
writes answers.json:

    [{"id": "m3-262", "verdicts": ["T", "F", "T", "T"],
      "quotes": ["deciding words, with locator", ...],
      "doubts": ["", "why this one could be read either way", ...],
      "tc_mismatch": ["", "how the Chinese statement differs from the English", ...]}]

`compare` prints every statement where the reviewer and the writer disagree,
every doubt and every language mismatch, so each can be settled against the
source before the items go into the bank.
"""
import json
import pathlib
import sys


def packet(items, out):
    lines = ["# Blind review packet", "",
             "Rule every statement TRUE or FALSE under the strict reading in bank/FORMAT.md, from the cited",
             "sources only (bank/find.py). Judge the English statement against the English text, then check",
             "that the Chinese statement says the same thing and is equally true or false against the Chinese text.", ""]
    for q in items:
        lines.append(f"## {q['id']} (module {q['module']})")
        lines.append(f"Source: {q['source']['en']} | {q['source']['tc']}")
        lines.append("")
        lines.append(f"EN: {q['en']['q']}")
        for i, s in enumerate(q["en"]["statements"]):
            lines.append(f"  {i + 1}. {s}")
        lines.append(f"TC: {q['tc']['q']}")
        for i, s in enumerate(q["tc"]["statements"]):
            lines.append(f"  {i + 1}. {s}")
        lines.append("")
    pathlib.Path(out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(items)} items to {out}")


def compare(items, answers):
    by = {a["id"]: a for a in answers}
    agree = total = 0
    for q in items:
        a = by.get(q["id"])
        if not a:
            print(f"{q['id']}: no answer")
            continue
        for i, t in enumerate(q["truth"]):
            total += 1
            v = (a.get("verdicts") or [None] * len(q["truth"]))[i]
            ok = v in ("T", "F") and (v == "T") == t
            agree += ok
            doubt = (a.get("doubts") or [""] * len(q["truth"]))[i]
            mis = (a.get("tc_mismatch") or [""] * len(q["truth"]))[i]
            if not ok or doubt or mis:
                print(f"{q['id']} statement {i + 1}: writer {'T' if t else 'F'}, reviewer {v}")
                print(f"   EN: {q['en']['statements'][i]}")
                if not ok:
                    print(f"   reviewer's quote: {(a.get('quotes') or [''] * len(q['truth']))[i]}")
                    print(f"   writer's note: {q['en']['notes'][i]}")
                if doubt:
                    print(f"   doubt: {doubt}")
                if mis:
                    print(f"   language: {mis}")
    print(f"{agree} of {total} statements agree")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 4 or sys.argv[1] not in ("packet", "compare"):
        print(__doc__)
        sys.exit(2)
    items = json.loads(pathlib.Path(sys.argv[2]).read_text(encoding="utf-8"))
    if sys.argv[1] == "packet":
        packet(items, sys.argv[3])
    else:
        compare(items, json.loads(pathlib.Path(sys.argv[3]).read_text(encoding="utf-8")))


if __name__ == "__main__":
    main()
