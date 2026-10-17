"""Print items as a candidate sees them, with the key, traps and notes.

    python bank/show.py m3-261 m5-97 ...
    python bank/show.py --lang tc m3-261
    python bank/show.py --patch patch.json [ids...]    # items of a patch, options generated
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import combo  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent


def show(q, lang):
    side = q[lang]
    print(f"=== {q['id']} (module {q['module']}){'  [fixed]' if q.get('fixed') else ''}"
          f"{'  [official: ' + q['official'] + ']' if q.get('official') else ''}")
    print(side["q"])
    traps = q.get("traps") or [None] * len(q["truth"])
    for i, s in enumerate(side["statements"]):
        mark = "T" if q["truth"][i] else "F"
        trap = f" <{traps[i]}>" if traps[i] else ""
        print(f"  {i + 1}. [{mark}{trap}] {s}")
    for i, o in enumerate(q["options"]):
        star = "*" if i == q["answer"] else " "
        print(f"  {star}{'abcde'[i]}) {combo.label(o, lang)}")
    for i, n in enumerate(side.get("notes", [])):
        print(f"  note {i + 1}: {n}")
    if side.get("explain"):
        print(f"  explain: {side['explain']}")
    print(f"  source: {q['source'][lang]}")
    print()


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    args = sys.argv[1:]
    langs = ["en", "tc"]
    if args[:1] == ["--lang"]:
        langs, args = [args[1]], args[2:]
    if args[:1] == ["--patch"]:
        import apply  # noqa: E402  (the same directory)
        patch = json.loads(pathlib.Path(args[1]).read_text(encoding="utf-8"))
        bank = {q["id"]: apply.build(q) for q in patch}
        args = args[2:] or list(bank)
    else:
        bank = {q["id"]: q for q in json.loads((ROOT / "web" / "questions.json").read_text(encoding="utf-8"))}
    for i in args:
        if i not in bank:
            print(f"{i}: not in the bank")
            continue
        for lang in langs:
            show(bank[i], lang)


if __name__ == "__main__":
    main()
