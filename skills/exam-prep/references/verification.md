# Verification

Contents: [What each check proves](#what-each-check-proves) · [Mechanical checks](#mechanical-checks) ·
[Blind review](#blind-review) · [Semantic review](#semantic-review) ·
[Panels and calibration](#panels-and-calibration) · [Adversarial audits](#adversarial-audits) ·
[Duplicates and drift](#duplicates-and-drift) · [Coverage audit](#coverage-audit) ·
[Response data](#response-data) · [Evidence and versions](#evidence-and-versions) ·
[Reporting](#reporting)

## What each check proves

| Check | Proves | Does not prove |
|---|---|---|
| Schema and key checks | every item is complete and its key is consistent with its own data | that the key is right |
| Quote occurrence | the quoted words exist in the cited source | that they support the claim |
| Blind answer | a reader with the source reaches the key | that the item is not also guessable, or that the key is as wide as the rule |
| Semantic review | the claim matches actor, scope, conditions and modality | coverage |
| Tells report and guesser | surface form does not point at the key, up to the strength of the guesser | correctness |
| Coverage map | which checklist points have a direct item | that the checklist covers the real exam |

Run the checks that the scale requires ([SKILL.md](../SKILL.md#choose-the-job-and-the-scale)),
add the others when a change, a finding or the stakes call for them, and say
which ran.

## Mechanical checks

`python scripts/bank_tool.py check spec.json bank.json [--sources text/]`

Hard errors (the build should fail):

- schema: every item has every language, its kind's fields, a valid key, a
  citation; ids unique and not retired; sections exist;
- combination items: exactly one option equals the true set; all/none used as
  defined and last; options are sets of valid statement numbers;
- positional references in any field of a shuffled item ("option B", "statement
  2", "the above", 上述, 以上…項);
- exact duplicate stems and exact twin statements;
- with `--sources`: every stored quote found in its document after
  normalisation;
- every section can fill its draw.

Diagnostics (calibrate, then decide which become hard): the length rules, the
truth rates of statements with absolutes, hedges and negation, answer-letter
spread, the true-count spread of combination items, near-duplicate stems by
shingles (word 4-grams for spaced languages, character 4-grams for CJK), and
near-identical statements in different items keyed opposite ways, where one
gives the other away on a shared paper.

Add the project's own checks: banned renderings and the required term, paired
terms, script purity (no Simplified characters in Traditional text), locator
words, a scope list. Writing them well:

- Loop over every language and every section. Three guards in the reference
  project silently checked one language only, and one section reached 54%
  key-is-longest on a green build.
- Prove each check can fail: keep a fixture with one planted defect per check.
  Four regexes once held a backspace byte where `\b` was meant, because a shell
  collapsed the backslash, and passed for three weeks.
- Case-fold the keyword only: `(?i:option|answer)\s+[A-E]`; a whole-pattern
  `(?i)` makes "answer a question" fail.
- Do not put a length floor on a duplicate check that already keys on the cited
  passage: an 11-character shared answer hid behind a 12-character floor.
- Guard correlations statistically across the bank, not per item, and tune each
  pattern until its only hits are items you mean to fix.
- Watch float comparisons on thresholds: `207 > 180 * 1.15` is true in Python.

## Blind review

Run the mechanical checks first, then build packets. Every wording change after a
review voids it for that item.

1. `python scripts/bank_tool.py packet spec.json bank.json --lang en --out
   packet-en.md --ids-file ids.txt` writes the items without keys, notes, traps
   or quotes, options shuffled, statements numbered as shown, and an answer
   template `packet-en.answers.json`.
2. A reviewer who did not write the items answers from the cited source, in the
   packet's language only, one row per item:
   `{"id", "answer", "statements": [true, false, …], "second": null, "quote", "locator", "code", "note"}`.
   For combination items the reviewer rules every statement first, then picks
   the option. `second` names a *second defensible* answer, strictly: a tempting
   distractor is not one.
3. `python scripts/bank_tool.py compare spec.json bank.json packet-en.answers.json`
   maps the shown positions back and lists every disagreement on the key or on a
   statement's truth, every `second`, and every note.
4. Settle each against the source. The reviewer can be wrong; so can the key.
   Record the resolution.
5. After any wording change, re-review that item's final text.

Error codes for findings (one per finding): `unclear-stem`, `unclear-options`,
`no-correct-answer`, `several-correct`, `wrong-key`, `unsupported`,
`language-mismatch`, `out-of-scope`.

Expect second answers rather than wrong keys once the first review is done. In
the reference bank, after the first review fixed two wrong keys, some 7,000
further blind answers found no wrong key but about 40 second defensible answers.

## Semantic review

Quote matching checks that text exists; it does not show the passage supports
the whole claim. For every changed item:

- check actor, scope, condition, exception, modal strength, AND versus OR, and
  cross-references to other provisions;
- for a true statement, look for a compliant counterexample that would make it
  false (an alternative route, an exception, an exemption);
- for an invented falsehood, check it is not true under another rule;
- compare the key with the notes' statement of the rule: a key narrower or wider
  than the rule passes blind review when the distractors are plainly wrong.

## Panels and calibration

- **Panels**: where the budget allows, three answerers on different models or
  seeds. All three against the key points to a wrong key; a split points to an
  ambiguous item.
- **Record the model actually used.** Several subagents on one model are not
  cross-model verification; check how the environment assigns models rather than
  assuming.
- **Calibrate a cheaper reviewer before a bulk review**, on a sample the strongest
  model has judged. In the reference project, a mechanical filter (the share of
  the key's words found in its stored quote) was set so that no defect in a
  judged sample of 120 slipped through, and skipped 57% of 2,862 quotes; then one
  cheaper model caught all 24 defects the best model had found, while a smaller
  one caught 18 and flagged a fifth of the good quotes. A calibration costs two
  packets; a reviewer that misses a quarter of the defects wastes the sweep.
- **Treat findings as claims.** Of three "critical" findings, a second look
  downgraded two. Separate strands re-find the same defect; merge duplicates
  before counting.
- **Do not ask a model whether an item is flawed.** Whole-item judges have poor
  precision. Turn the flaws a string check can catch into checks, and keep models
  answering, not grading.

## Adversarial audits

For a deeper tell audit, use a model from a different family from the writers':

- **Options only**: no stem, no source, options in several shuffled orders. Flag an
  item whose key is picked in most orders; report accuracy per section with a 95%
  interval against chance.
- **Closed book**: stem and options without the source, on a small model. A key it
  finds reliably is either common knowledge or a tell.
- **Cover the options**: the stem alone, answered in free text. A stem that cannot
  be answered without its options is unfocused.

Then simulate whole papers with the strongest surface-feature guesser you can
build, against the real pass rule. `python scripts/bank_tool.py tells spec.json
bank.json` fits one from the bank itself (a conditional logit over each option's
length, standout, overlap with the stem and the other options, and word cues),
scores it only on items it never saw, and sits simulated papers. Anything far
above chance is a tell to find. Report both the pick rate and the pass rate.

## Duplicates and drift

- Sweep every cross-section pair for duplicates, comparing stem similarity and
  answer similarity separately, in every language. Two items citing the same
  passage and keying the same answer are one item; the same answer from a
  different passage within a section is often legitimate (several offences carry
  one penalty), but across sections it lets a candidate meet one question twice
  in a paper. Shingle tests alone missed 35 semantic duplicate pairs.
- Distinguish separate subjects whose duties must each be learned: similar
  wording is not duplication.
- For language drift, embed every item's language versions with a cross-lingual
  model: each should be the other's nearest neighbour.

## Coverage audit

1. Build the checklist from each source: definitions, purposes, functions,
   powers, conditions, exceptions, footnotes, appendices, forms, lists with their
   counts, numbers and periods. For institutions and roles: nature and purpose,
   specific duties, decision authority, easily confused identities. A name in a
   stem proves none of these is tested.
2. Map each point to items that test it directly, recording covered, partial
   (say which aspect is missing), missing, reference only, or out of scope.
   Distinguish a bank-wide gap from thin practice in one section. A known wrong
   or unsupported statement is not evidence; a correctly keyed false statement
   can test the rule it departs from. Background mentions and explanation-only
   material are not direct tests.
3. Keep an image-page account: which pages hold diagrams or scans, which were
   read as images, which could not be.
4. Merge the same gap across sources into one task, keeping each source's mapping.
   Prioritise by the importance of the duty and the consequence of error, not by
   guessed exam frequency.
5. Reuse existing items first, then write only the residual points. Never pad
   with duplicates to meet a batch size.
6. Check the other direction too: items on what the register excludes.

Coverage is a proportion of a declared checklist, never a claim about the real
exam or a chance of passing.

## Response data

Where real candidates' answers exist: a key with negative discrimination is
probably wrong; a distractor with positive discrimination is probably a second
answer; a distractor chosen by under 5% of candidates does no work.

## Evidence and versions

At the Rigorous scale:

- keep the audit baseline: source, bank, quotes and register versions or hashes;
- bind every blind verdict to the exact final text it judged (a hash of the
  item's text), so a later edit visibly invalidates it;
- keep findings, resolutions and their item ids and statement indexes;
- never replace an old hash to make a check pass; add a new record that explains
  the change;
- re-run coverage after changes rather than editing old reports.

## Reporting

- Say what ran, on what scope, by which model, with sample sizes; say what did not
  run. Never imply an unrun check passed.
- "Tests pass", "blind-reviewed" and "covered" prove different things; name which.
- Give the frightening percentage with its ceiling, and report what you checked and
  found legitimate.
- Once verification confirms rather than corrects, sample, and state the sample
  size.
