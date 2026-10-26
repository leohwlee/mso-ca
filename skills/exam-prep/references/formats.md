# Formats: the exam spec, the item schema, scoring and export

Contents: [The exam spec](#the-exam-spec) · [The bank](#the-bank) ·
[Item kinds](#item-kinds) · [Choosing a format](#choosing-a-format) ·
[Combination items](#combination-items) · [Shuffling](#shuffling) ·
[Scoring and pass rules](#scoring-and-pass-rules) ·
[Written answers and mark schemes](#written-answers-and-mark-schemes) ·
[Versions and history](#versions-and-history) · [Export](#export)

The spec says what a paper looks like; the bank holds the items. The app, the
checks and every brief read both, so nothing hard-codes a section, an option
count or a language. `assets/example/` has a working pair with one item of every
kind; `scripts/bank_tool.py check` validates against the rules below.

## The exam spec

```jsonc
{
  "id": "example-cert",                    // storage namespace; letters, digits, hyphens
  "title": {"en": "Example Certificate — practice", "zh-Hant": "示例證書——練習"},
  "languages": ["en", "zh-Hant"],          // first is the default; one is fine
  "language_names": {"en": "English", "zh-Hant": "繁體中文"},
  "sections": [
    {"id": "1", "title": {"en": "Foundations", "zh-Hant": "基礎"}, "draw": 5},
    {"id": "2", "title": {"en": "Procedures", "zh-Hant": "程序"}, "draw": 5}
  ],
  "paper": {
    "minutes": 30,                          // 0 or absent: untimed
    "pass": {                               // every condition given must hold
      "min_score": 7,                       // absolute points
      "min_percent": null,                  // percentage of available points
      "min_per_section": null,              // points in each section
      "max_wrong_per_section": 2            // wrong or blank objective items per section
    },
    "negative_marking": 0                   // share of an item's points lost for a wrong objective answer
  },
  "kinds": {                                // per-kind defaults; items may override
    "single": {"shuffle": true},
    "multi": {"shuffle": true, "scoring": "all-or-nothing"},
    "combo": {"shuffle_statements": true},
    "match": {"scoring": "partial"},
    "order": {"scoring": "all-or-nothing"},
    "cloze": {"scoring": "partial", "case_sensitive": false}
  },
  "review": {"clear_after": 2},             // wrong-answer book: correct answers in a row to clear
  "notes": {"url": "notes.html"},           // optional; item.notes_anchor links to url#anchor
  "disclaimer": {"en": "…", "zh-Hant": "…"},
  "retired_ids": []                          // ids that must never be reused
}
```

A localised string is either one string (shown in every language) or an object
keyed by language. `draw` is the number of items a mock paper takes from the
section. Where the spec overlaps the QTI test model the names map directly:
`draw` is a section's `selection`, `shuffle` its `ordering`, `minutes` a
`timeLimits` maximum.

## The bank

`bank.json` is either a list of items or an object:

```jsonc
{
  "cases": {                                // optional shared scenarios for case sets
    "c1": {"en": {"title": "A new customer", "text": "…"}, "zh-Hant": {"title": "…", "text": "…"}}
  },
  "items": [ /* … */ ]
}
```

Fields every item has:

| Field | Meaning |
|---|---|
| `id` | Stable and never reused, e.g. `"2-014"`. Retired ids go in `spec.retired_ids`. |
| `section` | A section id from the spec. |
| `kind` | One of the kinds below. |
| `version` | Integer, default 1. Raise it whenever meaning, truth, key or option set changes. |
| `points` | Default 1; for written answers, the mark scheme's total. |
| `source` | Localised citation with a locator a reader can turn to: `"Policy §3.2"`, `"Ch. 4 p. 87"`, `"Lecture 6, slide 14"`. |
| `quotes` | Deciding quotes: `[{"doc": "03", "lang": "en", "text": "…", "for": 2}]`, verbatim from the extracted text; `for` names the statement or option index it decides (omit for the whole item). |
| `traps` | For `combo` and `tf`: the defect kind of each false statement, `null` for a true one (codes in [item writing](item-writing.md#the-trap-taxonomy)). |
| `case` | Optional case id; the case text is shown above the item. |
| `notes_anchor` | Optional anchor in the notes page for "read this in the notes". |
| `tags`, `level`, `official` | Free tags; cognitive level (`recall`, `understand`, `apply`, `analyse`); `official: true` for an examiner's own sample, kept verbatim and never shuffled. |
| `<lang>` | Per-language content, one object per language in the spec: `{"stem": "…", "explain": "…", …}` plus the kind's own fields. |

Language-neutral fields (answers, truth values, option sets) live on the item;
words live under each language, aligned index for index, because the app pairs
`options[i]` across languages.

## Item kinds

| `kind` | Per-language fields | Item fields | Shuffled at draw | Checks of its own |
|---|---|---|---|---|
| `single` (single best answer) | `stem`, `options[]`, `option_notes[]` | `answer` (index), `fixed`, `pin_last` | options, unless `fixed`; the last `pin_last` stay put | length rules; lexical and punctuation tells; no positional references; "all/none of the above" only if pinned |
| `multi` (choose all that apply) | `stem`, `options[]`, `option_notes[]` | `answer` (indices), `scoring` | options | spread of the number of keys; per-option tells as for statements |
| `tf` (true or false) | `stem` (the statement), `explain` | `answer` (true/false), `traps` | — | true share near half per section; absolutes, negation and hedges by truth |
| `combo` (combination, K-type) | `stem`, `statements[]`, `statement_notes[]` | `truth[]`, `options[]`, `answer`, `traps[]`, `fixed` | statements, with options relabelled | exactly one option equals the true set; all/none semantics; truth-count spread; statements independent; option-set structure tells |
| `match` | `stem`, `left[]`, `right[]` | `answer` (index into `right` for each `left`; default identity), `scoring` | right column | right may be longer than left; no pair decidable by grammar |
| `order` (sequence) | `stem`, `items[]` in the correct order | `scoring` | items | exactly one defensible order |
| `cloze` (fill the blanks) | `stem` with `{{1}}`, `{{2}}`…, `answers[][]` (accepted strings per blank), optional `choices[][]` | `scoring`, `case_sensitive` | — | every blank has an answer; accepted variants cover spelling and number formats |
| `numeric` | `stem`, `unit` | `answer`, `tolerance` or `tolerance_pct` | — | one defensible value; unit in the stem |
| `short` | `stem`, `model_answer`, `rubric[]` of `{"text", "marks"}` | `points` = sum of marks | — | self-marked; every rubric point grounded |
| `essay` | `stem`, `model_answer`, `rubric[]` or `levels[]` of `{"marks", "text"}` | `points` | — | self-marked; command word matches the rubric |

`explain` is an optional one-line summary on every kind. Case sets are items
sharing a `case`; a mock draws a case's items together and never splits them.

## Choosing a format

| Purpose | Good fit | Why |
|---|---|---|
| Learning one rule at a time | `single` with four options | A wrong answer names the misconception; options can come from neighbouring rules. |
| Rehearsing a real exam | the examiner's own format, character for character | The format is part of the exam: candidates lose marks to unfamiliar shapes. |
| Fine discrimination under strict reading | `combo` or `tf` | Each statement can carry one small defect; candidates must judge every one. |
| Lists and their exact members | `multi`, `combo` with off-list items | Tests whether the candidate knows the list, not one member. |
| Processes and sequences | `order` | Tests the order itself; one defensible order only. |
| Terms and definitions, actors and duties | `match` | Many pairs per item; add extra right-hand entries to stop elimination. |
| Exact recall of a term or figure | `cloze`, `numeric` | Only where the real exam asks for recall; otherwise put numbers inside statements. |
| Explanation, application, judgment | `short`, `essay`, case sets | The candidate must produce, not recognise; marked against a scheme. |

With no published format, propose single-best items with four options for
learning and ask. Avoid "all of the above" and "none of the above" in shuffled
single-best items: under shuffling they mean nothing, and when pinned they
attract test-wise guesses; use them only where the real exam does.

## Combination items

A combination item has numbered statements and options that each name a set of
statements ("1, 2 and 4"; "All of the above"). Its key follows from the truth of
the statements, so the checks can re-derive it.

- **Store the truth, generate the options.** `bank_tool.py options` fills
  `options` and `answer` from `truth` using symmetric templates: any two options
  of the same size can be swapped by renumbering the statements, so nothing in
  the set's structure singles one out (the option sharing most with the others,
  the statement printed most often, the only subset of its size). The template is
  chosen with odds proportional to how many members of the key's size it has, and
  the key is placed on a random member of its size.
- **An examiner's printed block** is reproduced verbatim and its order kept:
  mark such items `fixed: true` and give `options` yourself.
- **All and none.** `"all"` means every statement is true; `"none"` that none is.
  When present they are the last option. A shuffle never moves them.
- **Vary the number of false statements.** Aim at a spread (for example, roughly
  one item in five all true, two in five with one false, the rest with two or
  three false), and never let "exactly one is false" become a safe assumption.
  The reference exam's paper ranged from none true to all true.
- **Stems that state a count** ("Which three of the following…") take options of
  that size only and no all/none option.

Option sets are language-neutral (`[[1, 2, 4], [1, 3], …, "all"]`); the app writes
them out in each language ("1, 2 and 4" / "1、2 及 4").

## Shuffling

Shuffle once per draw and use the same order in every language. Declare per kind
what reorders and what stays:

- `single` and `multi`: options shuffle unless `fixed`; the last `pin_last`
  options stay where they are.
- `combo`: statements shuffle and are renumbered; each option's set is remapped,
  options a)–d) are sorted by their new sets, and all/none stays last. A letter
  then cannot be memorised, and explanations must never cite a statement number.
- `order`, `match`: items and the right column shuffle; the key is stored in
  canonical order.
- `official` and `fixed` items never shuffle.

Store answers in canonical terms (the stored option index, the chosen set of
statements by content, the right-column index), never by displayed position.
For the same reason, an answer key handed out with a shuffling app names each
answer by its wording; letters belong only to a frozen printed paper.

## Scoring and pass rules

- Objective kinds score all-or-nothing by default. `multi`, `match`, `order` and
  `cloze` may score `partial`: the share of pairs, positions or blanks right (for
  `multi`, correct choices minus wrong choices over the number of keys, floored
  at zero).
- `negative_marking` subtracts that share of the item's points for a wrong
  objective answer; a blank loses nothing.
- Pass conditions combine: total points, percentage, points per section, wrong
  answers per section. The results say which condition failed, because a
  candidate needs to know whether the total or one section sank the paper.
- Written answers are self-marked against the scheme before the paper's result
  is final; the app shows the model answer and the rubric and asks the candidate
  to award marks honestly.

## Written answers and mark schemes

- **Command words** fix what an answer must do: *state* (recall), *explain*
  (reasons), *compare* (both sides on the same dimensions), *apply* (rule to
  facts, with a conclusion), *evaluate* (a judgment with criteria). The rubric
  rewards exactly what the command word asks.
- **Points-based rubrics** list creditable points with marks each; say how many
  are needed for full marks if there are more points than marks.
- **Levels-based rubrics** describe what an answer at each band does, with marks
  per band; the marker picks one.
- **Model answers** are written to full marks within the time the exam allows,
  in the candidate's register, grounded and cited like a key.
- **Alternatives and errors**: list acceptable equivalents and the common wrong
  answers, with why they score nothing.

## Versions and history

- Store every attempt by item id and version, with the response in canonical
  terms. A later bank cannot then re-score an old attempt against a different
  question: an attempt on an older version is shown as historical.
- Raise `version` for any change that could change a candidate's answer or its
  correctness (meaning, truth, key, option set), even when the option count stays
  the same. Typo fixes keep the version.
- Retire an item by moving its id to `spec.retired_ids`; the app drops it from
  new draws, discards unfinished papers that contain it, and keeps old results.

## Export

| Target | Notes |
|---|---|
| QTI 2.1 / 3.0 | The only interchange format that can pin single options (`fixed`), which a combination block or a pinned "all of the above" needs. Map sections to `assessmentSection` with `selection` and `ordering`. |
| Moodle XML, GIFT | Turn shuffling off for combination items and pinned options. Feedback per answer carries the explanation and the citation. |
| Aiken | Single answers only; never export combination or multi items to it. |
| Anki (CSV or genanki) | Derive the note's id from the item id so re-imports update cards instead of duplicating them. Front: the situation or the stem; back: the rule, the explanation and the citation. |
| Print (Markdown, HTML, PDF) | A paper with the items shuffled once, and a separate key with explanations and citations. |

No interchange format has a source field, so carry the citation in the feedback
or the explanation.
