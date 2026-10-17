"""Option sets for combination items: generate them, check them, write them out.

An item states which of its statements are true (`truth`); everything about its
options follows from that. This module builds the five options from a catalogue
of templates and is the only thing that ever writes them, so no option set is
designed by hand.

    python bank/combo.py check web/questions.json

Why templates. A test-wise candidate who knows nothing can still read an option
set: the option that shares most with the others, the statement printed in the
most options, the one subset of its size. Every template here is symmetric in
the sense that matters: any two options of the same size can be swapped by
renumbering the statements, so nothing in the set's structure singles out one
of them. The key is placed on a template member of its size chosen at random,
and the template itself is chosen with odds proportional to how many members of
that size it has, so that within any template each member is about equally
likely to be the key. go test measures what is left (guessing_test.go).

C&ED's own block, a) 1, 2 and 3  b) 1, 2 and 4  c) 2, 3 and 4  d) 1, 3 and 4
e) All of the above, is the four-statement template of three-statement
subsets, and is printed in C&ED's order whenever it occurs.
"""
import itertools
import json
import random
import sys

ALL, NONE = "all", "none"

# C&ED's printed blocks, in the order C&ED prints them.
OFFICIAL4 = [[1, 2, 3], [1, 2, 4], [2, 3, 4], [1, 3, 4]]           # MSSB/CA_01/2021, then e) all
GN71 = [[1, 2, 3], [2, 3, 4], [1, 3, 4], [1, 2, 5], [3, 4, 5]]     # Guidance Notes ¶7.1, no e)

# Templates for options a)-d), by statement count, with prior weights. Every size
# class in each template is one orbit of the template's automorphism group. The
# weights make the truth counts the templates imply close to the counts the
# writing rules aim at (bank/FORMAT.md): for four statements about 58% of the
# items that are not all true have three true, 30% two and 12% one.
TEMPLATES = {
    4: [
        ("official", [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]], 0.45),
        ("pairs", [[1, 2], [1, 3], [2, 4], [3, 4]], 0.15),
        ("pairs-triples", [[1, 2], [1, 2, 3], [1, 3, 4], [3, 4]], 0.15),
        ("ones-triples", [[1], [1, 2, 3], [2, 3, 4], [4]], 0.10),
        ("ones-pairs", [[1], [1, 2], [3], [3, 4]], 0.15),
    ],
    5: [
        ("fours", [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5]], 0.41),
        ("triples-fours", [[1, 2, 3], [1, 2, 4], [1, 3, 4, 5], [2, 3, 4, 5]], 0.20),
        ("triples", [[1, 2, 3], [1, 2, 4], [1, 3, 5], [1, 4, 5]], 0.13),
        ("pairs-triples", [[1, 2], [1, 3], [2, 4, 5], [3, 4, 5]], 0.09),
        ("pairs-triples-b", [[1, 2], [1, 3, 4], [2, 3, 5], [4, 5]], 0.09),
        ("ones-pairs", [[1], [2], [3, 4], [3, 5]], 0.08),
    ],
    6: [
        ("fives", [[1, 2, 3, 4, 5], [1, 2, 3, 4, 6], [1, 2, 3, 5, 6], [1, 2, 4, 5, 6]], 0.40),
        ("fours-fives", [[1, 2, 3, 4], [1, 2, 3, 5, 6], [1, 2, 4, 5, 6], [3, 4, 5, 6]], 0.20),
        ("fours", [[1, 2, 3, 4], [1, 2, 3, 5], [1, 4, 5, 6], [2, 4, 5, 6]], 0.20),
        ("triples-fours", [[1, 2, 3], [1, 2, 3, 4], [1, 4, 5, 6], [4, 5, 6]], 0.15),
        ("triples", [[1, 2, 3], [1, 4, 5], [2, 4, 6], [3, 5, 6]], 0.05),
    ],
}

# Items whose stem says how many statements are true ("Which three…") take five
# subsets of that size and no e) option, as Guidance Notes ¶7.1 does.
COUNTED = {
    (5, 3): [[1, 2, 3], [2, 3, 4], [3, 4, 5], [1, 4, 5], [1, 2, 5]],
    (5, 2): [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]],
}

# How often an item that is neither all true nor all false gets "None of the above"
# as e). Writers aim at about one item in fifty with no true statement, and this
# keeps a None option the key about one time in five that it appears. Six-statement
# items never have none true, so they never show it.
NONE_SHARE = {4: 0.05, 5: 0.05, 6: 0.0}


def true_set(truth):
    return [i + 1 for i, t in enumerate(truth) if t]


def option_set(opt, n):
    """The statements an option says are true."""
    if opt == ALL:
        return frozenset(range(1, n + 1))
    if opt == NONE:
        return frozenset()
    return frozenset(opt)


def canonical(options, n):
    """Options in display order: C&ED's order for C&ED's blocks, otherwise smaller
    subsets first and then by number, with All/None of the above last."""
    sets = [o for o in options if o not in (ALL, NONE)]
    tokens = [o for o in options if o in (ALL, NONE)]
    as_sets = sorted(tuple(sorted(o)) for o in sets)
    if n == 4 and as_sets == sorted(tuple(o) for o in OFFICIAL4):
        ordered = [list(o) for o in OFFICIAL4]
    elif n == 5 and not tokens and as_sets == sorted(tuple(o) for o in GN71):
        ordered = [list(o) for o in GN71]
    else:
        ordered = [list(o) for o in sorted(as_sets, key=lambda o: (len(o), o))]
    return ordered + tokens


def relabel(members, member, key, n, rng):
    """Renumber a template so that `member` becomes `key`: a random bijection that
    maps the member's statements onto the key's and the rest onto the rest."""
    src_in, src_out = sorted(member), [i for i in range(1, n + 1) if i not in member]
    dst_in, dst_out = sorted(key), [i for i in range(1, n + 1) if i not in key]
    rng.shuffle(dst_in)
    rng.shuffle(dst_out)
    m = dict(zip(src_in + src_out, dst_in + dst_out))
    return [sorted(m[x] for x in s) for s in members]


def generate(truth, seed, count=None):
    """Five options and the answer index for an item with this truth vector.
    `count` is the number of true statements when the stem states it."""
    n = len(truth)
    rng = random.Random(seed)
    key = set(true_set(truth))
    k = len(key)

    if count is not None:
        if count != k:
            raise ValueError(f"the stem says {count} are true but the truth vector has {k}")
        if (n, k) not in COUNTED:
            raise ValueError(f"no counted template for {k} of {n} statements")
        members = COUNTED[(n, k)]
        member = rng.choice(members)
        options = canonical(relabel(members, member, key, n, rng), n)
    else:
        if n not in TEMPLATES:
            raise ValueError(f"{n} statements; items have 4 to 6")
        templates = TEMPLATES[n]
        if 0 < k < n:
            weights = [w * sum(1 for s in mem if len(s) == k) for _, mem, w in templates]
            if not any(weights):
                raise ValueError(f"no template has a {k}-statement option for {n} statements")
            _, members, _ = rng.choices(templates, weights=weights)[0]
            member = rng.choice([s for s in members if len(s) == k])
            body = relabel(members, member, key, n, rng)
            token = NONE if rng.random() < NONE_SHARE[n] else ALL
        else:
            _, members, _ = rng.choices(templates, weights=[w for _, _, w in templates])[0]
            perm = list(range(1, n + 1))
            rng.shuffle(perm)
            body = [sorted(perm[x - 1] for x in s) for s in members]
            token = ALL if k == n else NONE
        options = canonical(body + [token], n)

    answer = [i for i, o in enumerate(options) if option_set(o, n) == frozenset(key)]
    if len(answer) != 1:
        raise AssertionError(f"generated options {options} do not hold the key {sorted(key)} exactly once")
    return options, answer[0]


def label(opt, lang):
    if opt == ALL:
        return "All of the above" if lang == "en" else "以上皆是"
    if opt == NONE:
        return "None of the above" if lang == "en" else "以上皆非"
    xs = [str(x) for x in opt]
    if lang == "en":
        if len(xs) == 1:
            return f"{xs[0]} only"
        return ", ".join(xs[:-1]) + " and " + xs[-1]
    if len(xs) == 1:
        return f"只有 {xs[0]}"
    return "、".join(xs[:-1]) + " 及 " + xs[-1]


def automorphisms(sets, n):
    fs = {frozenset(s) for s in sets}
    out = []
    for p in itertools.permutations(range(1, n + 1)):
        if all(frozenset(p[x - 1] for x in s) in fs for s in fs):
            out.append(p)
    return out


def symmetric_key(options, answer, n):
    """True when every option the same size as the key can be turned into the key
    by renumbering statements in a way that maps the option set onto itself."""
    if options[answer] in (ALL, NONE):
        return True
    sets = [o for o in options if o not in (ALL, NONE)]
    key = frozenset(options[answer])
    orbit = {frozenset(p[x - 1] for x in key) for p in automorphisms(sets, n)}
    return all(frozenset(s) in orbit for s in sets if len(s) == len(key))


def problems(q):
    """What is wrong with one item's truth and options; an empty list if nothing."""
    out = []
    truth, options, n = q.get("truth"), q.get("options"), None
    if not isinstance(truth, list) or not all(isinstance(t, bool) for t in truth):
        return ["truth must be a list of true/false"]
    n = len(truth)
    if not 4 <= n <= 6:
        out.append(f"{n} statements; items have 4 to 6")
    for lang in ("en", "tc"):
        if len(q.get(lang, {}).get("statements", [])) != n:
            out.append(f"{lang}: {len(q.get(lang, {}).get('statements', []))} statements, truth has {n}")
    if not isinstance(options, list) or len(options) != 5:
        return out + ["options must be a list of five"]
    seen = set()
    for i, o in enumerate(options):
        if o in (ALL, NONE):
            if i != 4:
                out.append(f"option {i}: {o!r} must be the last option")
            key = o
        elif isinstance(o, list) and o and all(isinstance(x, int) for x in o):
            if o != sorted(set(o)) or o[0] < 1 or o[-1] > n:
                out.append(f"option {i}: {o} is not a sorted list of statement numbers 1-{n}")
            if len(o) == n:
                out.append(f"option {i}: {o} lists every statement; write it as 'all'")
            key = tuple(o)
        else:
            out.append(f"option {i}: {o!r} is neither a list of statement numbers nor all/none")
            continue
        if key in seen:
            out.append(f"option {i}: {o} appears twice")
        seen.add(key)
    if options != canonical(options, n):
        out.append(f"options are not in display order: {options}, want {canonical(options, n)}")
    hits = [i for i, o in enumerate(options) if option_set(o, n) == frozenset(true_set(truth))]
    if len(hits) != 1:
        out.append(f"{len(hits)} options match the true statements {true_set(truth)}")
    elif q.get("answer") != hits[0]:
        out.append(f"answer is {q.get('answer')}, but the option matching the truth is {hits[0]}")
    elif not q.get("official") and not symmetric_key(options, hits[0], n):
        out.append(f"the key {options[hits[0]]} is not symmetric with the other options of its size")
    return out


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) != 3 or sys.argv[1] != "check":
        print(__doc__.splitlines()[2])
        sys.exit(2)
    bank = json.load(open(sys.argv[2], encoding="utf-8"))
    bad = 0
    for q in bank:
        for p in problems(q):
            print(f"{q.get('id')}: {p}")
            bad += 1
    print(f"{len(bank)} items, {bad} problems")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
