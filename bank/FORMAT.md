# The question format

Every question in `web/questions.json` is written to the shape of the real
Competence Assessment paper. This file is the register of what the owner decided
about that shape, the schema an item follows, and the rules a writer works to.
`go test ./...` enforces what can be checked mechanically.

## What the paper looks like

- 35 multiple-choice questions, seven modules of five, 75 minutes, one correct
  answer each (Guidance Notes ¶5.1–5.3). Pass: no more than 2 wrong in any
  module and at least 25 overall.
- Every published sample is a combination item: a stem, numbered statements,
  and five options a)–e) naming subsets of them. Sample set MSSB/CA_01/2021
  prints seven, with four statements and the block
  `a) 1, 2 and 3  b) 1, 2 and 4  c) 2, 3 and 4  d) 1, 3 and 4  e) All of the above`;
  Guidance Notes ¶7.1 prints one with five statements, every option a
  three-statement subset.
- The papers the owners sat (October 2026) went further: 4 to 6 statements, the
  number of true statements anywhere from one to all, option sets that differ
  from item to item, and distractors that differ from the source by a single
  word. An "all of the above" or "none of the above" option is always the last.

## The owner's decisions (16–17 October 2026)

| Decision | Rule |
|---|---|
| Format | Every item is a combination item. No single-answer items. A trap that a single-answer item would test (near-identical agency names, for one) is written as a statement. |
| Strict reading | A statement is true only if it matches its source in scope, conditions, qualifiers, actors, numbers, time limits and modal strength. Changing any one of those makes it false, and so does adding an item that the source's list does not contain, even when the item is true elsewhere. The explanation names the defect. |
| Languages | English and Traditional Chinese, both complete for every item, each following its own official text. |
| Option layout | "All of the above" (以上皆是) or "None of the above" (以上皆非), when present, is always option e). The other options list statement numbers. |
| Statement order | The app shuffles the statements of every item at every draw and renumbers the options to match, so a letter cannot be memorised. Every statement has its own explanation without positional references. |
| Retired | The 1,206 four-option items and 303 superseded combination items are out of the app. Their ids remain reserved in `bank/retired-ids.json`; their text and quotes are preserved in Git at `v1.7.5`. The remaining 38 old combination items have been migrated in place with their ids retained. |
| Sources | The 23 documents in `docs/` (the five categories of Guidance Notes ¶6.1). C&ED's seminar slides were considered on 17 October 2026 and left out. |

## Schema

```jsonc
{
  "id": "m3-201",                       // m<module>-<n>; ids are never reused
  "module": 3,
  "truth": [true, false, true, true, false],
  "options": [[1, 3, 4], [1, 2, 3, 4], [3, 4, 5], [1, 4], "all"],
  "answer": 0,                          // index of the option equal to the true set
  "traps": [null, "period", null, null, "offlist"],
  "source": {"en": "AMLO Sch. 2 s.13(2)–(3)", "tc": "《打擊洗錢條例》附表2第13(2)至(3)條"},
  "en": {
    "q": "stem",
    "statements": ["…", "…", "…", "…", "…"],
    "notes": ["why statement is true or false, quoting the deciding words", "…"],
    "explain": "optional one-line summary"
  },
  "tc": { "q": "…", "statements": ["…"], "notes": ["…"], "explain": "…" }
}
```

- `options` are language-neutral. Each is a sorted list of statement numbers,
  or `"all"` / `"none"` (index 4 only). The app writes them out in each
  language (`1, 3 and 4` / `1、3 及 4`, `2 only` / `只有 2`). They are generated
  by `bank/combo.py`, never written by hand. When migrating an existing item
  without changing its truth values, retain its options and answer index so
  saved answers still refer to the same sets.
- `notes` hold one entry per statement, in each language. They never refer to
  a statement or an option by number, because the app renumbers them.
- `traps` give, for each false statement, the kind of defect (below); `null`
  for a true statement.
- `fixed` is no longer used: all items have independent notes and may be reordered.
- `official` marks C&ED's own sample items, kept verbatim.
- Quotes live in `docs/quotes.json`: one per statement and language,
  `{"doc": "02", "text": "…"}`, copied verbatim from `docs/text/`. For a true
  statement it is the passage that supports it; for a false one, the passage
  it departs from.

## Writing an item

**The stem** names a topic in words, as C&ED's stems do: "Which of the
following are correct about…", "…should include:", "Which of the following
should be kept?". It never asks what a section number says.

**Statements**

- Four to six, each decisively true or false on its own under the strict
  reading. A statement never refers to another ("the above", "statement 2").
- True statements paraphrase the source faithfully and keep every qualifier.
  Write some that look wrong but are right: an accurate "must", a rule that
  surprises, a narrow-sounding source the statute does name.
- Each false statement has exactly one defect, and it is a small one: the
  sentence a careless reader accepts. Use these kinds, all seen in C&ED's
  samples or the papers sat:

| Code | Defect | Example |
|---|---|---|
| `offlist` | An item the source's list does not contain, though plausible | "The profitability of the MSO's business" among the risk factors (sample 1); "shortlisting internal reports by the frontline staff before reporting to the MLRO" among the STR systems (sample 5); 公司秘書 among a legal person's identification data (sample 7) |
| `added` | A word or phrase added that changes the rule | "the original **or the copy** of the licence" (sample 2) |
| `scope` | The rule widened or narrowed | "licensees operating **with or without** particular premises must maintain a local management office" (sample 4) |
| `reversed` | The rule turned around | the tipping-off provisions **do not** cover a suspicion raised inside the MSO but not yet reported to the JFIU (the Guideline says they do) |
| `qualifier` | A limiting condition dropped | "independent of all operational and business functions", without "subject to the size of the MSO" |
| `number` | A sum, share or threshold changed so that the statement claims what the source does not: a duty or permission reaching cases the source leaves out, or a stricter requirement | $8,000 for $120,000; 25% for 10%. Not $120,000 for $8,000 in "for a transfer of $X or more, the MSO should verify": the source implies that statement, so it is true |
| `period` | A time limit changed, on the same test as `number` | within one month, 7 days, 45 days before expiry, 5 years. Not "may apply within 7 days" where the source allows 14: the source implies it |
| `actor` | The duty given to the wrong person or body | the compliance officer for the MLRO; C&ED for the JFIU |
| `modal` | must / should / may, or reduce / avoid, changed | 減低風險 made 避免或移除風險 |
| `name` | A near-identical name | 聯合財務情報組 for 聯合財富情報組. Never "Joint Financial Investigation Unit": C&ED's own sample keys it true, so the register (B21) judges such a statement on the rest of what it says |
| `condition` | The rule moved to the wrong case | the wire-transfer rule applied to a remittance that is not one |

- How many are true: vary it. Across the bank aim at roughly one item in five
  all true, two in five with one false, and the rest with two or three false.
  Never make "exactly one is false" a safe assumption.
- Keep the statements of an item close in length, and put absolutes and
  negations on true statements as often as on false ones.
- No twins: a statement that another item already asserts, or a near copy
  of one with the opposite truth, teaches a candidate which to doubt.

**Notes** say, for each statement, whether it is true or false and why, in
the source's own words, with its locator: "False: ¶4.3.2 lists full name, date
of birth, nationality and identity number; sex is not among them."

**Citations and terms** follow `revision/AUTHOR_GUIDE.md`: a locator in every
citation, each language's own official terms, no word from the other language.

## Tools

```bash
python bank/find.py EN 02 "target market"       # find a passage in a source, with page and context
python bank/apply.py next 3 15                  # the next 15 unused ids in module 3
python bank/apply.py check patch.json           # validate a patch of new or changed items
python bank/apply.py apply patch.json           # generate options, merge into the bank and quotes
python bank/show.py m3-261                      # print an item with its key, traps and notes
python bank/combo.py check web/questions.json   # validate every item's options
python bank/blind.py packet patch.json out.md   # the items without their answers, for a blind reviewer
python bank/blind.py compare patch.json ans.json  # the reviewer's verdicts against the truth
```

Every new item is reviewed blind before it goes into the bank: a reviewer who
sees only the stems, statements and citations rules each statement from the
sources, and every disagreement, doubt or difference between the languages is
settled against the source.

A patch is a JSON list of items without `options` or `answer`; `apply`
generates both from `truth`, and takes each statement's quotes from a
`quotes` field it moves into `docs/quotes.json`.

## Historical material

The migration is complete. The old snapshots and one-off converter are no longer
needed in the working folder. `retired-ids.json` records their original commit
and reserves every retired id, so a new item cannot inherit an old saved answer.
To consult the old material, read `git show v1.7.5:web/questions.json` and
`git show v1.7.5:docs/quotes.json`. The source documents, terminology guide and
conflict decisions remain in the working tree because they still govern new items.
