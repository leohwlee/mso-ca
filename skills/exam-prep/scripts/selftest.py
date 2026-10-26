#!/usr/bin/env python3
"""Prove the bundled tools work, and that each hard check can fail.

    python scripts/selftest.py

Runs against assets/example/ and a synthetic bank built in memory. Exits 1 on
the first failure. Standard library only.
"""
import copy
import io
import json
import random
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import bank_tool as bt  # noqa: E402

EX = HERE.parent / "assets" / "example"
FAILED = []


def ok(cond, name):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILED.append(name)


def errors_for(spec, bank, **kw):
    return [m for _, m in bt.check(spec, bank, **kw).errors]


def main():
    spec, bank, _ = bt.load(EX / "spec.json", EX / "bank.json")
    clean = errors_for(spec, bank, sources=EX / "sources")
    ok(not clean, f"example bank has no errors {clean[:3]}")

    def planted(name, mutate, expect):
        b = copy.deepcopy(bank)
        s = copy.deepcopy(spec)
        mutate(s, b)
        errs = errors_for(s, b, sources=EX / "sources")
        ok(any(expect in e for e in errs), f"catches {name} ({expect!r})")

    by = lambda b, iid: next(i for i in b["items"] if i["id"] == iid)  # noqa: E731
    planted("a duplicate id", lambda s, b: b["items"].append(copy.deepcopy(by(b, "1-001"))), "id used 2 times")
    planted("a missing language", lambda s, b: by(b, "1-001").pop("zh-Hant"), "no 'zh-Hant' content")
    planted("a missing citation", lambda s, b: by(b, "1-001").pop("source"), "no source citation")
    planted("a key out of range", lambda s, b: by(b, "1-001").update(answer=7), "answer must be an option index")
    planted("unequal option counts", lambda s, b: by(b, "1-001")["zh-Hant"]["options"].pop(), "lengths differ between languages")
    planted("a positional reference", lambda s, b: by(b, "1-001")["en"]["option_notes"].__setitem__(1, "Unlike option A, this is wrong."), "positional reference")
    planted("a statement reference", lambda s, b: by(b, "1-004")["en"]["statement_notes"].__setitem__(1, "False, unlike statement 3."), "positional reference")
    planted("a shuffled all-of-the-above", lambda s, b: by(b, "1-001")["en"]["options"].__setitem__(3, "All of the above"), "all/none")
    planted("a combo key that disagrees with truth", lambda s, b: by(b, "1-004").update(truth=[True, True, True, True, False]), "options equal the true statements")
    planted("a combo answer index", lambda s, b: by(b, "2-007").update(answer=(by(b, "2-007")["answer"] + 1) % 4), "answer is")
    planted("all/none not last", lambda s, b: by(b, "2-007")["options"].insert(0, by(b, "2-007")["options"].pop()), "must come after")
    planted("a statement keyed both ways", lambda s, b: by(b, "2-007")["en"]["statements"].__setitem__(1, by(b, "1-004")["en"]["statements"][0]), "keyed both true and false")
    planted("a cloze without its blank", lambda s, b: by(b, "1-006")["en"].update(stem="No blanks here."), "has no {{1}} blank")
    planted("a rubric short of the points", lambda s, b: by(b, "2-003").update(points=5), "mark scheme allows only")
    planted("a retired id reused", lambda s, b: s.update(retired_ids=["2-001"]), "retired")
    planted("a section that cannot fill its draw", lambda s, b: s["sections"][0].update(draw=50), "cannot fill a draw")
    planted("a quote not in the source", lambda s, b: by(b, "1-001")["quotes"].append({"doc": "01", "lang": "en", "text": "a passage the rules never contain at all"}), "quote not found")
    planted("an unknown section", lambda s, b: by(b, "1-001").update(section="9"), "is not in the spec")
    planted("an unknown kind", lambda s, b: by(b, "1-001").update(kind="poll"), "is not one of")

    def warned(name, mutate, expect):
        b = copy.deepcopy(bank)
        s = copy.deepcopy(spec)
        before = any(expect in m for _, m in bt.check(s, b, sources=EX / "sources").warnings)
        mutate(s, b)
        after = any(expect in m for _, m in bt.check(s, b, sources=EX / "sources").warnings)
        ok(after and not before, f"warns of {name} ({expect!r})")

    warned("near-twin statements keyed both ways", lambda s, b: by(b, "2-007")["en"]["statements"].__setitem__(1, "A card is valid for two years and may be renewed online."), "nearly repeats")

    # Generated option sets: exactly one equals the true set; all/none last; symmetric sizes.
    rng = random.Random(3)
    good = True
    for n in (3, 4, 5, 6):
        for _ in range(300):
            truth = [rng.random() < 0.7 for _ in range(n)]
            opts, ans = bt.generate_options(truth, rng)
            key = frozenset(i + 1 for i, t in enumerate(truth) if t)
            hits = [j for j, o in enumerate(opts) if bt.option_set(o, n) == key]
            sizes = [len(o) for o in opts if o not in (bt.ALL, bt.NONE)]
            if hits != [ans] or opts[-1] not in (bt.ALL, bt.NONE) or len(opts) != 5:
                good = False
            if 0 < len(key) < n and sizes.count(len(key)) < 2:
                good = False
    ok(good, "generated option sets hold the key once, end in all/none, never isolate the key's size")

    # Packet and compare round trip: perfect answers agree; a wrong one is reported.
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "packet-en.md"
        with redirect_stdout(io.StringIO()):
            bt.main(["packet", str(EX / "spec.json"), str(EX / "bank.json"), "--lang", "en", "--out", str(out)])
        mapping = json.loads((Path(tmp) / "packet-en.map.json").read_text(encoding="utf-8"))["items"]
        rows = json.loads((Path(tmp) / "packet-en.answers.json").read_text(encoding="utf-8"))
        packet_text = out.read_text(encoding="utf-8")
        notes = [n for i in bank["items"] for key in ("option_notes", "statement_notes") for n in i["en"].get(key, [])]
        notes += [i["en"]["explain"] for i in bank["items"] if i["en"].get("explain")]
        ok(notes and not any(n in packet_text for n in notes), "packet carries no explanations")
        items = {i["id"]: i for i in bank["items"]}
        for row in rows:
            it, m = items[row["id"]], mapping[row["id"]]
            k = it["kind"]
            if k == "single":
                row["answer"] = "ABCDEFGH"[m["perm"].index(it["answer"])]
            elif k == "multi":
                row["answer"] = ["ABCDEFGH"[m["perm"].index(x)] for x in it["answer"]]
            elif k == "tf":
                row["answer"] = it["answer"]
            elif k == "combo":
                n = len(it["truth"])
                key = frozenset(i + 1 for i, t in enumerate(it["truth"]) if t)
                back = {i + 1: j + 1 for i, j in enumerate(m["perm"])}
                for L, o in zip("ABCDEFGH", m["shown"]):
                    if frozenset(back[x] for x in bt.option_set(o, n)) == key:
                        row["answer"] = L
                row["statements"] = [it["truth"][j] for j in m["perm"]]
            elif k == "match":
                row["answer"] = ["ABCDEFGH"[m["perm"].index(x)] for x in (it.get("answer") or range(len(it["en"]["left"])))]
            elif k == "order":
                row["answer"] = "".join("ABCDEFGH"[m["perm"].index(x)] for x in range(len(m["perm"])))
            elif k == "cloze":
                row["answer"] = [a[0] for a in it["en"]["answers"]]
            elif k == "numeric":
                row["answer"] = it["answer"]
            else:
                row["answer"] = "written"
        ans_path = Path(tmp) / "packet-en.answers.json"
        ans_path.write_text(json.dumps(rows), encoding="utf-8")
        buf = io.StringIO()
        with redirect_stdout(buf):
            bt.main(["compare", str(EX / "spec.json"), str(EX / "bank.json"), str(ans_path), "--json"])
        res = json.loads(buf.getvalue())
        written = sum(1 for i in bank["items"] if i["kind"] in ("short", "essay"))
        ok(res["agree"] == res["total"] - written, f"perfect answers agree ({res['agree']} of {res['total']}, {written} written)")
        row = next(r for r in rows if r["id"] == "1-001")
        row["answer"] = "ABCD"[(mapping["1-001"]["perm"].index(0) + 1) % 4]
        ans_path.write_text(json.dumps(rows), encoding="utf-8")
        buf = io.StringIO()
        with redirect_stdout(buf):
            bt.main(["compare", str(EX / "spec.json"), str(EX / "bank.json"), str(ans_path), "--json"])
        res = json.loads(buf.getvalue())
        ok(any(f[0] == "1-001" and "key is 0" in f[1] for f in res["findings"]), "a wrong answer is reported against the key")

    # A printed paper and its key agree: each single-answer key letter points at the stored key.
    with tempfile.TemporaryDirectory() as tmp:
        paper, key = Path(tmp) / "paper.md", Path(tmp) / "key.md"
        with redirect_stdout(io.StringIO()):
            bt.main(["paper", str(EX / "spec.json"), str(EX / "bank.json"), "--all", "--lang", "en",
                     "--out", str(paper), "--key", str(key), "--seed", "4"])
        ptext, ktext = paper.read_text(encoding="utf-8"), key.read_text(encoding="utf-8")
        good = True
        for n, it in enumerate([i for s in spec["sections"] for i in bank["items"] if i["section"] == s["id"]], 1):
            if it["kind"] != "single":
                continue
            block = ptext.split(f"**{n}.**")[1].split("**")[0]
            letter = ktext.split(f"**{n}.** ")[1][0]
            line = next(x for x in block.splitlines() if x.startswith(f"- {letter}. "))
            good &= line[5:] == it["en"]["options"][it["answer"]]
        ok(good and "Source:" in ktext, "printed paper keys point at the stored answers")

    # The tells report finds a planted length tell, and the learnt guesser beats chance on it.
    words = "rule duty notice period licence record report review officer branch customer system".split()
    synth = {"items": [], "cases": {}}
    srng = random.Random(5)
    for i in range(80):
        opts = [" ".join(srng.choice(words) for _ in range(5)) for _ in range(4)]
        key = srng.randrange(4)
        opts[key] = opts[key] + " " + " ".join(srng.choice(words) for _ in range(4))
        synth["items"].append({"id": f"s-{i}", "section": "1", "kind": "single", "answer": key,
                               "source": "Doc 1 ¶1", "en": {"stem": "Which rule applies?", "options": opts}})
    sspec = {"id": "synthetic", "languages": ["en"], "sections": [{"id": "1", "draw": 10}],
             "paper": {"pass": {"min_percent": 60}}}
    rows = bt.build_rows(sspec, synth, "en")
    hit, chance = bt.heuristic(rows, 1)
    ok(hit > 0.9 and abs(chance - 0.25) < 1e-9, f"'pick the longest' finds the planted tell ({hit:.0%})")
    cv = bt.cross_validate(rows)
    rate = sum(cv.values()) / len(cv)
    ok(rate > 0.8, f"the learnt guesser finds it too ({rate:.0%} against 25%)")
    p, _ = bt.simulate(sspec, synth, lambda it: cv.get(it["id"], 0), 500, 1)
    ok(p > 0.5, f"and passes simulated papers ({p:.0%})")
    with redirect_stdout(io.StringIO()):
        code = bt.cmd_tells(type("A", (), {"spec": EX / "spec.json", "bank": EX / "bank.json", "papers": 50, "seed": 1})())
    ok(code == 0, "the tells report runs on the example")

    print(f"\n{'all checks passed' if not FAILED else str(len(FAILED)) + ' failed'}")
    return 1 if FAILED else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
