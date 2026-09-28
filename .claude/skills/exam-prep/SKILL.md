---
name: exam-prep
description: Turn a fixed set of source documents (statutes, regulations, guidelines, manuals, course notes; in one language or two) into exam preparation — a cited study pack, a multiple-choice question bank, and a mock exam that draws papers under the real rules — for any exam format the user defines as data. Use when asked to write revision notes, a study guide or pack, practice questions, a question bank, a mock paper or a mock-exam app from documents; to define or change an exam format (sections, question formats, fixed option blocks, pass rule, timing); or to audit existing material for wrong or second-defensible keys, ungrounded or superseded content, duplicates, drift between languages, or answers a candidate can guess from surface form without knowing the material.
license: MIT
metadata:
  version: "2.0.0"
  replaces: "exam-question-bank 1.2.1"
---

# Exam prep from source documents

This skill turns a fixed set of documents into three products:

- a **study pack** the candidate reads, every line cited to its source;
- a **question bank** they practise on, every key cited and checked blind;
- a **mock exam** that draws papers from the bank under the exam's real rules.

The exam's format is data (the *exam spec*, Phase 0), so nothing below assumes a
number of sections, options or languages.

The method comes from one project taken through more than 25 releases: a
bilingual (English and Traditional Chinese) bank of about 1,550 questions and a
21-page study pack for a Hong Kong regulatory exam, written from 23 official
documents. That project, [leohwlee/mso-ca](https://github.com/leohwlee/mso-ca),
is the reference implementation. Its sources and their manifest are in `docs/`,
the pack generator and the decisions register in `revision/`, the bank in
`web/questions.json`, the guards in `questions_test.go` and the app in
`web/app.js`. The numbers quoted below are its measurements. They are evidence
for a rule, not constants, so re-measure on your own material.

## Four principles

1. **Grounded.** Every line of the pack and every key traces to a locator (a
   section, paragraph or item number) in a current source, in the language the
   reader is reading. Where the material and the source differ, the source
   prevails.
2. **Valid.** A question is worth asking only if the sole way to answer it is to
   know the cited passage. It must not be answerable from the shape of the
   options, a hedge word, a length, a semicolon, or what a clause number says.
3. **Measured.** The damaging faults are invisible one item at a time and obvious
   in aggregate. Measure the bank, and ship every measurement as a test.
4. **Decided first.** Every rule the owner settled late cost a sweep of the
   whole bank. Length rules cost 1,194, then 442, then 637 rewrites. Chinese
   terminology cost 169, then 662, then 533. Source conflicts cost 29, then
   93. Superseded sources cost 49, clause-number questions 52, the language
   rule 47 and out-of-scope questions 27. Phase 0 asks all of those questions
   before anything is written.

## Choose the mode

| Mode | Do |
|---|---|
| Build | Phases 0–7 in order. |
| Extend: new questions, pages, sources or formats | Re-read the spec and the register. Run Phase 1 for any new source, then write. Run every guard and the twin check against the whole bank, then Phase 6 on what changed. |
| Audit | Phase 6 and a tell sweep. Measure everything before changing anything. Report findings only unless asked to fix, and let the owner decide each item. |
| Change the format | Edit the spec, add the format's guards and change the draw logic. Only then convert or write items: a draw filter costs one edit, while converting questions costs an agent each. |

---

## Phase 0 — Intake: the spec and the register

Two files govern everything. The **exam spec** says what a paper looks like. The
**decisions register** records every judgment the owner has made. The app, the
guards and every brief read them, and nothing hard-codes them.

**Ask before writing anything.** Put each point to the owner with a
recommendation, and record the answer in the register:

- **Sources.** Ask for the exact list, including every language edition, and
  whether only current editions count. Default: yes. A document that a later
  one covers is superseded. Of a series that replaces itself (watchlists,
  periodic statements), keep only the latest.
- **What is examinable.** Take it from the examiner's own guidance. Circulars,
  FAQs and amendment notices often are, and they are the part nobody archives.
- **Scope: whose rules the exam tests.** Default: a question earns its place
  only if the rule governs the candidate the exam is for. Boundary questions are
  kept on purpose and marked. The section a provision sits in marks scope, not
  its vocabulary: two out-of-scope provisions named no out-of-scope actor.
- **Languages.** Ask which languages, and what each one follows where the
  official editions differ. Default: each language follows its own official
  text, no question turns on a difference, and nothing mentions the other
  language.
- **Conflicts between sources.** The owner decides each one (Phase 2). Never
  pick a side silently.
- **Format.** Look for published sample questions, past papers and the
  syllabus's own worked examples; the newest sample may sit in an appendix. If
  the examiner prints a format, reproduce it character for character. With no
  published format, propose single-best-answer items with four options, and
  ask.
- **Question style.** Default: numbers are never the unknown, stems name topics
  in words, and distractors are wrong on substance (Phase 5).
- **Study-pack style.** Ask how and where the candidate will read it. Phase 4
  has defaults.
- **When reviews stop.** Default: once blind review confirms rather than
  corrects, a further check triggers a fix only for a wrong key or a second
  defensible answer.

### The exam spec

Keep the spec in the project as JSON or YAML. This one describes the reference
exam, cut to two sections:

```json
{
  "name": "Competence Assessment for Money Service Operators",
  "languages": ["en", "zh-Hant"],
  "sections": [
    {"id": "1", "title": {"en": "General knowledge", "zh-Hant": "常識"}, "draw": 5, "bank_min": 123},
    {"id": "2", "title": {"en": "The Ordinance, Parts 1–7", "zh-Hant": "條例第1至7部"}, "draw": 5, "bank_min": 303}
  ],
  "paper": {"minutes": 75, "pass": {"min_score": 25, "max_wrong_per_section": 2}},
  "formats": {
    "single": {"kind": "single-best", "options": 4, "shuffle": true},
    "combo4": {"kind": "fixed-block", "statements": 4, "shuffle": false, "block": [
      {"true": [1, 2, 3],    "en": "1, 2 and 3",       "zh-Hant": "1、2 及 3"},
      {"true": [1, 2, 4],    "en": "1, 2 and 4",       "zh-Hant": "1、2 及 4"},
      {"true": [2, 3, 4],    "en": "2, 3 and 4",       "zh-Hant": "2、3 及 4"},
      {"true": [1, 3, 4],    "en": "1, 3 and 4",       "zh-Hant": "1、3 及 4"},
      {"true": [1, 2, 3, 4], "en": "All of the above", "zh-Hant": "以上皆是"}
    ]}
  },
  "modes": {
    "practice":  {"formats": "all", "feedback": "after each answer"},
    "mock":      {"formats": "all"},
    "realistic": {"formats": ["combo4"]}
  }
}
```

- `draw` is the number of questions per paper. `bank_min` is the bank target,
  sized in Phase 3.
- A fixed block names the set of true statements behind each printed option. The
  key then follows from the statements' truth, and can be checked against the
  explanation.
- `pass` holds whatever the exam uses: a total, a floor per section, a
  percentage, negative marking.
- Where the spec overlaps the QTI test model, the names map directly: `draw`
  is a section's `selection`, `shuffle` its `ordering`, `minutes` a
  `timeLimits` maximum. An export to QTI or a learning platform is then
  mechanical (Phase 7).
- To add a format, add an entry of one of these kinds:

| Kind | Stored | At draw time | Checks of its own |
|---|---|---|---|
| `single-best` | stem, N options, key at a fixed index | options shuffled once, same order in every language | length rules, lexical and punctuation tells, no "all/none of the above", no positional references |
| `fixed-block` (combination, K-type) | stem, numbered statements, the printed block, answer index | never shuffled | block verbatim; spread of answer letters and of which statement is false; absolutes and negation by truth; statements independent; the explanation re-derives the key |
| `true-false` | one statement and its truth | as stored | true share near half in each section; absolutes, negation and hedges by truth |
| `multi-select` | N options, the set of keys, a scoring rule | shuffled | spread of the number of keys; per-option tells, as for statements |
| `numeric`, `cloze` | canonical answer, tolerance, unit | as stored | exactly one defensible answer; the unit stated in the stem |
| `case-set` | a shared scenario and its items | items in order | no item's stem or options answers another item |

---

## Phase 1 — Sources

- **Archive every language edition locally**, under stable numbered filenames,
  with a manifest: number, title, edition date, official URL, date checked and
  hash. Work from the archive, because a citation that moves is worse than none.
  Downloading needs the user's yes each time, naming the file, source and size.
- **Never guess an identifier.** Read the real listing. Translated editions sat
  at an unpredictable offset from the original in 2 cases of 14.
- **Current documents only.** Before adding a document, check whether it
  replaces another or has been overtaken. When one is removed, re-cite its points
  to the current source, and list for the owner any point that only it made.
- **Re-check before each release.** Download again and diff with page footers
  stripped: a word diff for spaced languages, a character diff for CJK. Some
  official sites block scripted downloads with a client check; replaying that
  check with a cookie jar works.
- **Extract the text once, per page, and normalise it before searching.** Map
  CJK compatibility ideographs (U+F900–U+FAFF; one extract stored 行 as U+FA08)
  to their unified forms, and strip whitespace and line breaks from CJK text.
  Otherwise a term that is present looks absent.
- **Build a locator index and a finder.** Segment each document into its
  citable units (section and subsection, chapter and paragraph), with the page
  and the text in each language. Anchoring on a number lands in the table of
  contents, while searching for a distinctive 5–9 word phrase finds the
  provision. Where one language's extract misplaces margin numbers, trust the
  document's cross-references and the other edition's numbering. Every later
  phase, and every subagent, uses the finder.
- **Record each document's volume.** It sizes the blueprint.
- **Say what you covered and what you could not reach.**

---

## Phase 2 — Conflicts, terms and the register

Sweep the sources for contradictions **before writing**. In the reference
project, 95 surfaced after the bank already held 1,500 questions.

- **Look in four places:** between documents; inside one document; between the
  language editions of one document; and apparent conflicts that turn out not to
  be conflicts. Record the last kind too, so nobody raises them again.
- **Write each as a decision the owner can make in a minute.** Give the question
  in plain words, each side quoted with document, page and locator, a
  recommendation with the rule behind it (statute over guidance; later or more
  specific over earlier or general), and a risk level. Dense legal reasoning
  loses owners; plain words do not.
- **Classify each decision.**
  - *One*: one answer everywhere.
  - *Own*: each language follows its own text, and no question may turn on the
    difference.
  - *Both*: both rules are true. A question says which one it tests, and never
    presents one as overriding the other.
  - *None*: not a conflict.
- **Let the owner decide on a page with one control per item**, stored where you
  can read the picks back. Record every pick in the repository, and teach it in
  both products. A conflict found later goes to the owner before either side is
  taught. Never settle one in passing.
- **Keep a terminology table per document and per language.** Documents do not
  share one vocabulary: two guidelines from one regulator used different words
  for "premises". Take each term from the document an item cites, never by
  find-and-replace. Before banning a term, check how the source uses it. A long
  form defined once and a short form used throughout are both correct.
- **The register holds everything decided**: sources, scope, the language rule,
  conflicts, terms and style rules. Briefs cite it, and guards encode it.

---

## Phase 3 — Blueprint and guards

- **Size each section to the volume of source behind it**, not to a round
  number. Equal sections over unequal sources force writers to reword each
  other's questions, which is where duplicates come from.
- **The smallest section bounds how many distinct papers can be drawn.** Count
  it per mode, including only the formats that mode draws. Grow sections in
  parallel.
- **Schema.**
  - Fields per language, and a citation per language that carries a locator.
  - The deciding quote per language, verbatim from the cited unit. A guard then
    proves every key is grounded, and a quote that stops matching flags an
    edited source. The reference bank stored no quotes, so every review had to
    find them again.
  - The key at a fixed index for shuffled formats, and fixed blocks stored
    verbatim.
  - Stable ids for items, and for each option an id shared by all its language
    versions. Store attempts by option id rather than position, so neither a
    reordered option nor a new one can corrupt a candidate's history.
  - Optionally, the locator units an item rests on. That turns coverage and
    twin checks into queries.
- **Formats that earn their place.** Single-best items suit learning, because a
  wrong answer names the rule not yet learnt. The examiner's own format gives
  realism, behind a switch in the app.
- **Write the guards before the first question** (catalogue below). Every guard
  loops over the spec's languages and sections. Three guards in the reference
  project silently checked one language only, and one section reached 54%
  key-is-longest on a green build.
- **Prove each guard can fail.** Keep a fixture with one planted defect per
  guard, and watch each one fail. Four regexes once held a backspace byte where
  `\b` was meant, because a shell had collapsed the backslash, and they passed
  for three weeks.

---

## Phase 4 — The study pack

The pack exists so the candidate recognises a situation and recalls the rule,
not so they can index the source. These defaults came from an owner memorising
for a closed-book exam, so ask about yours.

- **Organise by the sources' own structure**, with a page per Part, Schedule or
  chapter, unless the owner prefers topics. Name on each page the exam sections
  it serves, and keep together what the source keeps together.
- **Put the situation first.** A heading or card states the situation or the
  plain rule, and the citation trails as support. A clause number is never the
  subject: write "Staff reports go straight to the reporting officer,
  unfiltered", not "¶7.13 says…".
- **Choose the form by the content**, in this order:
  - a process or interaction becomes a flowchart;
  - rules that change with the situation become a table whose rows are the
    situations;
  - numbers and deadlines become a table of the number, what it requires, when
    it applies and what follows if it is missed;
  - bullets are the last resort.

  Every page shows its key content visually.
- **Flag what is easy to confuse, where it arises**: two thresholds for two
  duties, or two officials holding different powers. Use a labelled callout or a
  marker in the table cell, ideally side by side.
- **Leave these out:**
  - section-by-section listings and who-is-who tables;
  - standalone sections of numbers;
  - drills, because practice belongs in the bank;
  - an opening paragraph that repeats the page overview. The paragraph above a
    figure says how to read it.
- **Colour and shape carry a stated meaning, keyed beside the figure**, or they
  are not used. One set of kinds serves a whole pack: a duty or deadline, a
  discretion someone else holds, a safe outcome, an end state, background. A
  shape keeps one meaning: a hexagon is a question, never an actor.
- **Accuracy is not negotiable.** Every sentence is grounded and every cell
  cited. Keep conditions, qualifiers and modal strength (must, should, may).
  Never present an invented example, number or list as the source's. Before
  writing, search what other pages already say, and link instead of repeating.
- **One language per view.** Both languages appear together only in a combined
  view. Each view follows its own text: a point found in one edition only
  appears in that view only. No page compares editions.
- **Build it from source, never by hand.** Use a generator with one module per
  page, deterministic output and one offline HTML file. Draw each figure once
  per language view, keep the source's terms from breaking across lines, and
  keep the page's outline in view.
- **Check each page three ways.** Check it mechanically: one language per view,
  dead links, bullets, duplicate ids, figures drawn per view. Render every
  figure and look at it for overlaps, clipping and arrows crossing text. Audit
  the built page at phone and desktop widths.
- **Add a recall mode** that blurs outcomes, penalties and numbers. It turns
  reading into self-testing.
- **Other forms come from the same cited rules**: flashcards, with the situation
  on the front and the rule and its citation on the back; and a one-page sheet
  of numbers and deadlines. Keep each card's id stable across rebuilds, so a
  re-import updates cards instead of duplicating them.

---

## Phase 5 — Writing questions

### What every item satisfies

- **The unknown is substance.** A stem may cite a provision, but says what it
  provides, and the question is about the rule. Never ask what a number says,
  how two numbered provisions relate, where a rule lives, an exact wording, or
  a date for its own sake. Never let an option rely on a number for its
  meaning. The model form is *"Section N requires X. In which situation does Y
  apply?"* Writing by section number produced 44 such items in 1,594.
- **Realistic items look like the examiner's.** If official stems never cite
  paragraphs, realistic stems do not either (an audit found 89% did); the
  citation belongs in the key. Match the official mix of recall and
  application items, and measure yours: the reference bank's share of
  scenarios was 5–15% by section.
- **Distractors are wrong on substance**: the wrong actor, threshold, deadline,
  body or condition. They are never wrong by overstatement ("only", "always"),
  never by a tail citing a provision as if it said the false thing ("per
  section 4.4.2"), and never merely implausible.
- **Write keys and distractors the same way.** When keys paraphrase the source
  and distractors are invented, a reader, or a model, learns to tell them apart.
  Build distractors from real provisions, such as another actor's duty, the
  neighbouring threshold or the procedure's other deadline, in the key's
  register.
- **Exactly one defensible answer.** Before keying, re-read the whole list the
  stem draws on. Most second answers came from swapping one true distractor
  without checking its siblings.
- **Statements stand alone.** No "statement 2", "the above", "the former" or "in
  that case": a statement that leans on another gives their relationship away.
  Each statement is decisively true or false from the source. Vague frequency
  words ("usually", "often") appear only where the source itself uses them.
- **No twins.** Before keying a point, check that it is not already keyed, or
  stated as a true statement, anywhere in the bank. Include its twin provisions,
  the same rule restated for another actor or procedure, because a candidate
  transfers the answer. When a section runs out of unkeyed points, say so.
  Reaching into out-of-scope provisions to fill it is how scope faults start.
- **Keep options in one length band while writing** (the standout rule, below).
  Trim the key rather than pad distractors, and pad only in the source's own
  register.
- **Explanations name the source's deciding words** for each false option or
  statement. They refer to options by content, and never mention another
  language.

### Producing them at scale

- **Subagents return JSON patches and never edit the bank.** Parallel packets
  then cannot collide, and re-running is idempotent.
- **One applier validates and applies each question separately**, so one bad
  item never sinks a batch. A no-op apply must round-trip the bank byte for byte
  (indent, escaping, line endings). Verify that before the first real write.
- **Three commands make hundreds of rewrites tractable.**
  - `list` prints the failing items, with per-option measurements and the
    explanation.
  - `check` prints the resulting measurements, pass or fail, before anything is
    applied.
  - `apply` applies what passes, and accepts a sparse form for one-option edits.

  Forty batches cleared 637 questions this way.
- **Give each packet a disjoint slice** (`cands[i::n]`), and inline the exact
  source chapter it needs. Batches of 16–20 worked best.
- **Save every ~8 items.** Rate limits and an expired login each killed a whole
  wave, and incremental saves plus resuming the same agents lost nothing.
  **Check coverage against the packet's id list** before calling a category
  done: one packet saved 8 of 18 and died silently.
- **All languages of an item travel in one patch entry.** The applier validates
  the merged item.
- **Run the full suite on the merged patches.** Patches that pass one by one can
  jointly break a bank-wide share.
- **Audit each wave** for bolt-on phrases that appear only in distractors. They
  become a tell of their own.
- **Say which model the subagents run on.** The session's model choice does not
  reach them.

---

## Phase 6 — Verification

Reviewing an item with the key in view verifies nothing. The reviewer must answer
it.

- **Review blind, and per language.** Shuffle the options, hide the key and the
  explanation, and inline the cited chapter in the packet's language. The
  reviewer answers from it, one row per item:
  - the answer;
  - a deciding quote of 40 words or fewer, with its locator;
  - any *second* defensible answer (strictly: a tempting distractor is not one);
  - notes.

  For fixed-block items, rule every statement TRUE or FALSE first, then pick
  the option.
- **Where the budget allows, use a panel of three answerers**, on different
  models or seeds. All three agreeing against the key points to a wrong key; a
  split points to an ambiguous item. Label every finding with one fixed code:
  unclear stem, unclear options, no correct answer, several correct answers,
  wrong key.
- **Expect second answers, not wrong keys.** After the first review fixed two
  wrong keys, some 7,000 further blind answers found no wrong key, but about 40
  second defensible answers. Aim at where they breed: enumerations, statements
  drawn from one list, and anything touched by a rewrite.
- **Run mechanical checks on every item**: the whole guard suite, plus the key
  re-derived from the explanation. Collect every "statement N is false", not just
  the first, and map "none is false" to the all-true option.
- **Compare every key with the pack.** Blind answering cannot see a key that is
  merely narrower or wider than its source when the distractors are plainly
  wrong. Reading each item against the pack's statement of the rule found them.
- **Sweep every cross-section pair** for duplicates, comparing stem similarity
  and answer similarity separately, in every language. Shingle tests alone
  missed 35 semantic duplicate pairs.
- **Verify invented falsehoods.** A distractor wrong on substance carries an
  invented fact. Sample those against the source, because an invented fact that
  happens to be true breaks the question silently.
- **Re-verify after a bulk rewrite.** An audit of the old text has not audited
  the bank you now have.
- **Sample once verification confirms rather than corrects**, and state the
  sample size.
- **Treat findings as claims too.** An adjudicator's verdict is not verification:
  of three "criticals", a second look downgraded two. Separate strands re-find
  the same defect, and 51 cross-strand duplicates had to be merged before the
  counts were honest.
- **Run a test-wise adversary**: a model from a different family from the
  writers', in three runs.
  - *Options only*: no stem and no source, with the options in five shuffled
    orders. Flag an item whose key is picked four times or more; by chance that
    happens to about 1.6% of four-option items. Report the accuracy per section
    with a 95% interval against chance. In published work, answering from the
    choices alone beat the majority-class baseline for 11 of 12 model and
    benchmark pairs, by up to 33 points.
  - *Closed book*: stem and options without the source, on a small model. A
    key it finds reliably is either common knowledge or a tell.
  - *Cover the options*: the stem alone, answered in free text. A stem that
    cannot be answered without its options is unfocused.

  Then simulate whole papers with the strongest surface-feature guesser you can
  build, against the real pass rule. Anything far above chance is a tell to
  find (catalogue below).
- **Don't ask a model whether an item is flawed.** Whole-item judges have poor
  precision: rules found 91% of the flaws human reviewers found, against 79%
  for GPT-4, and the best detector of errors in a large public benchmark reached
  an F2 of about 40. Turn the flaws a string check can catch into guards, and
  keep models answering, not grading.
- **Check that each language pair still says one thing.** Embed every item's
  language versions with a cross-lingual model: each version should be the
  other's nearest neighbour. A pair that is not has drifted apart or been
  swapped.
- **Read response data where it exists.** A key with negative discrimination is
  probably wrong. A distractor with positive discrimination is probably a
  second answer. A distractor that under 5% of candidates choose does no work.

---

## Phase 7 — Delivery

**The mock-exam app** reads the spec and the bank.

- **Modes.**
  - Practice by section, with the explanation and citation shown after each
    answer.
  - A mock under the real draw, timer and pass rule, saying why a paper failed:
    the total, or which section's floor.
  - Practice on the candidate's wrong answers. Clear an item only after several
    correct answers in a row, or schedule it by spaced repetition.
  - The realistic-format switch, shown only when every section can fill a
    paper, saying how many papers it can draw.
- **Shuffle once per draw**, and use the same order in every language. A
  bilingual view pairs `options[i]` across languages.
- **History stays on the device**, with export and import to a file.
- **Survive bank changes.** Drop ids the bank no longer holds. Discard any
  stored option order whose length no longer matches, because a four-entry order
  applied to a five-option item hides the key.
- **Ship one offline HTML file.** Embed the fonts with their licence notice, and
  compact the embedded bank.
- **Export on request.**
  - QTI is the only interchange format that can pin individual options
    (`fixed`), which is what a fixed block needs.
  - In Moodle XML, GIFT or quizdown, turn shuffling off for fixed-block items.
    Never export them to Aiken, which holds single answers only.
  - No format has a source field, so carry the citation in the feedback.
  - For flashcards, derive the Anki note's GUID from the item id.

**Releases.** Tag a commit the guards passed, and build the files in CI from
that commit. Use an annotated tag whose message says what changed for a
candidate; keep `--cleanup=whitespace`, or every line starting with `#` vanishes.
Say which release first carries a repair, because anyone holding an earlier
download still has the wrong key. Before tagging, check `git log <last-tag>..HEAD`
for changes that accumulated behind documentation-only commits.

**The README** says what the material is, how to use it, what is in it (in
tables), the disclaimer and the licence. Development notes go elsewhere.

---

## Guard catalogue

These are defaults, run per language and per section; N is the option count. The
reference suite is [`questions_test.go`](https://github.com/leohwlee/mso-ca/blob/main/questions_test.go).

| Guard | Default | Stops |
|---|---|---|
| Section counts reach `bank_min`; every item has every language, its format's fields and a valid key | — | items going missing or half-written |
| Every citation has a locator and resolves in the locator index | — | a document with no paragraph to turn to; drift (one chapter's citations sat two paragraphs high) |
| The deciding quote is found in the cited unit, in each language, and shares the key's deciding words more than any distractor does | normalise (NFKC, spaces, quote marks); exact substring, else a fuzzy partial match ≥ 95 | a key the cited passage does not support |
| No citation of a removed document | the manifest | superseded sources creeping back |
| Key is the longest option | ≤ 45% | "pick the longest" |
| No length rank above chance plus 15 points | ≤ 40% when N = 4 | the same tell moved to second-longest |
| Longest minus shortest within an item | ≤ 40% of the mean; floor 20 Latin / 8 CJK characters | one option carrying visibly more |
| No option more than 15% clear of its nearest neighbour, at either end | floor 8 Latin / 3 CJK characters | the comparison a reader actually makes |
| Punctuation all or none within an item | semicolons, and any mark that correlates | a semicolon marking the fuller answer |
| The key is the option sharing most with the other options no more often than chance | share of items ≤ 1/N + 2 standard errors | convergence: distractors made by varying the key |
| The key is the option sharing most words with the stem no more often than chance | the same test; stop-list the terms every item must use | the key echoing the stem |
| Statements carrying absolutes are true at a healthy rate | ≥ 60% bank-wide, ≥ 45% per section | "mark the absolutes false" |
| No positional references in any field | case-fold the keyword only | "option 2" after a shuffle |
| No "all/none of the above" in shuffled formats | — | a meaningless option |
| A negative stem marks its negation | NOT, EXCEPT; 不, 並非, 除…外 in bold | a negation read past |
| Numeric options in order, and ranges never overlapping | — | two defensible answers; an order that points to the key |
| Fixed blocks verbatim; answer letters and false-statement positions spread | ≤ 40% for any letter | a drifting printed format; "the second is usually false" |
| Fixed-block explanations re-derive the key | — | an explanation arguing for another answer |
| Statements independent | no "statement N", "the above", 上述 | statements leaning on each other |
| A stem citing a fine-grained provision keeps ≥ 4 substantive words; no number-as-object questions; no number-only key; no pair of number-only options | — | clause-number recall |
| No duplicate stems | exact across the bank; within a section, word 4-shingles or CJK character 4-grams, ≥ 0.75 | one question asked twice |
| No key shared across sections (within a section it is often legitimate: several offences carry one penalty) | no length floor | one question in two sections |
| Each language uses its own edition's terms, in every field including citations | banned rendering → the source's term | wording the source never uses |
| Paired terms keep both limbs | e.g. ML/TF | half the concept dropped in translation |
| Script purity; no other-language words the source does not print; no language tags | e.g. simplified characters in Traditional text | a slip from a fixer's draft |
| Locator words match the document | e.g. Chinese 條 for a statute section, 段 for a guideline paragraph | a paragraph cited with the statute's word |
| A translated "the said X" points back to something already met in the item | stem, then statements in order | a determiner referring to nothing |
| Each language version of an item is the other's nearest neighbour | cross-lingual embeddings, calibrated on a hand-labelled sample | two languages drifting into two questions |

**Writing guards.**

- Case-fold the keyword only: `(?i:option|answer)\s+[A-E]`. A whole-pattern
  `(?i)` makes "answer a question" fail the build.
- Put no length floor in a duplicate check that already keys on the cited
  passage. An 11-character shared answer hid behind a 12-character floor.
- Guard correlations statistically, not per item.
- Tune each pattern on the bank until the only hits are items you mean to fix.

---

## The catalogue of tells

The tells are ordered by how much they leaked. Every one was measured, and the
direction differed between languages, so measure rather than assume.

1. **Length, in four rules. Only the last matters to a reader.**
   - *Key-is-longest.* 1,241 of 1,510 keys were the longest option, by a
     median 55 characters, and "pick the longest" passed 64% of simulated
     papers.
   - *Rank.* Trimming keys moved them to second-longest in half the bank, so
     cap every rank.
   - *Spread.* Rank ignores size: 40/41/42/130 ranks like 40/41/42/43.
   - *Standout.* Readers compare an option with its nearest neighbour. With the
     first three rules met, an English option more than 25% longer than its
     nearest rival was the key 1 time in 55 (a reverse tell). One more than 25%
     shorter was the key 47% of the time. In Chinese, standing out long meant
     the key 37% of the time.
   - *The rank-shift trap.* Padding one distractor past the key moves the key to
     rank 2. Pad two, each clearing the key by 2 characters or more, because
     ties sort to the better rank. Better still, trim the bloated option. Rank
     skew left on options differing by a character or two (dates, names) is
     unreadable, so say so instead of chasing it.
2. **Hedges mark true statements.** Drafting hedges what is true: "reasonable"
   or "appropriate" marked the key 71% of the time in English and 62% in
   Chinese. In the mirror image, an option alone saying "only" or "solely" was
   the key 6.5% of the time, and one alone carrying a currency figure 6%. Hedge
   distractors in the same register.
3. **Absolutes mark false statements.** A statement carrying "only", "always",
   "never" or "need not" was true 32% of the time, against a 76% base rate.
   Marking absolutes false scored 66–71% where the rule discriminated, against
   20% for chance, because overstating a true rule is the easiest way to
   falsify it. Make the statement wrong on substance instead, delete incidental
   absolutes, and put accurate absolutes on true statements. Don't dodge the
   regex: "where X, so Y falls short" keeps the exclusivity for a reader.
4. **Negation marks false statements.** After the absolutes repair, statements
   containing a negation were true 59% of the time against a 76% base rate, and
   23–40% in two sections. Negate true statements too.
5. **Punctuation.** A semicolon made an option the key 45% of the time (chance
   25%), and a parenthesis 38–43%. Don't balance the correlation, remove the
   discrimination: every option has the mark, or none does. Most recasts become
   ", and" or ", while", and about 10% need rewriting by hand.
6. **Echo and convergence.** The key alone repeats the stem's words or its
   deciding facts; blind reviewers flagged several. When distractors are made by
   varying the key, the key is also the option sharing most with all the others,
   and test-takers are known to use that (the NBME guide names both cues).
   Neither was measured in the reference bank, so measure both.
7. **Twins and leaning statements.** 77 pairs of near-identical statements were
   found, 19 of them with one true and one false; such a pair tells the
   candidate which statement to doubt. A statement that refers to another (28
   found) exposes their relationship.
8. **Position and grammar.** Positional references break under shuffling, and
   "all of the above" means something only in a fixed block. Answer letters and
   false-statement positions must spread. Agreement with the stem (singular,
   plural, article) marks the option written first. In a fixed block, one
   statement known to be false eliminates every option containing it. Reproduce
   the examiner's block anyway, and put the difficulty in the statements.

**State the ceiling with every percentage.** The strongest lexical guesser
averaged 11.7 of 35 over 4,000 simulated papers, against a pass mark of 25 with
section floors: a 0.00% pass rate. It still got a free elimination on about one
question in eight. Say both.

---

## Languages

- **Options and statements align index for index** across languages, because
  the renderer pairs `options[i]`. Tell every packet, since length tuning tempts
  reordering.
- **When a check in one language drives an edit, re-check the other.** Rewriting
  only the flagged side split 29 questions into two exams: one told English
  candidates a document is acceptable, and Chinese candidates that it never is.
  Align to the side that was not rewritten, keeping its claim and dropping only
  the offending word.
- **A question whose key, or a statement's truth, depends on wording that
  differs between the editions is invalid in a bilingual bank.** Rework it onto
  what both texts share.
- **Terms come from each language's own edition of the cited document**, never
  from translating the other language's term.
- **CJK specifics.**
  - Count characters, not bytes.
  - Compare with character 4-grams, because word shingles collapse a Chinese
    stem into one token.
  - Normalise compatibility ideographs.
  - Model estimates of CJK length run 1–3 characters short, so overshoot by 3–4
    and `check` first.
- **Thresholds and floats.** `207 > 180*1.15` is true in Python.

---

## Repairing without breaking

- **Rewriting a statement invalidates its explanation.** Re-aim every
  explanation you disturb: a candidate who got it wrong reads it to find out why,
  and is answered about something else.
- **Re-aim duplicates rather than delete them when counts are fixed**, and
  re-aim from the source. Histogram the section's cited units, take one with no
  question, and check that it and its twins are not keyed elsewhere. Expand
  citation ranges first (a citation of "s.7(4)–(6)" covers s.7(5)), or a
  provision looks free when it is not.
- **Retiring questions needs the app first**, because saved papers and history
  refer to their ids.
- **Changing an option count breaks stored attempts.** Discard stored orders of
  the wrong length.
- **Before a bank-wide rule, build the tool**: `list`, `check`, `apply`.
- **A bank-wide share sitting at its limit tips on one edit.** When trimming,
  keep a distractor longer than the key.

---

## Working with the owner, and reporting

- **Put decisions on a page the owner can act on**: one item per decision, the
  question in plain words, a recommendation and a control. Read the picks back
  before acting, and ask about blanks and "discuss".
- **Fix what you notice.**
  - A small, clear defect: fix it in the same session, and say so.
  - A pattern: sweep every occurrence, then guard it. Fixing only the items a
    findings list named left the same invented terms in about 160 others.
  - A large class that needs judgment on each item: give the count and a
    sample, and offer the sweep.
- **Measure before you speculate.** Broaden a detector before quoting its count:
  one job was 637 questions, not the 415 first quoted. Triage detector output by
  hand before quoting a number: of 20 flags checked, 2 were real.
- **State the ceiling with the frightening percentage**, and report what you
  checked and found legitimate ("these shared answers are several offences
  carrying one penalty").
- **Answer "is it finished?" by looking.** Reviewing your own rewrite found two
  regressions it had introduced.

---

## Briefs for subagents

Every brief names:

- the job, and the tools and files: the finder, a `show <id>` command, the
  sources, the register;
- what not to open: keys, patches, the bank, other packets;
- the output schema per item, and "save every 8";
- the check to pass before handing back, and the reply format.

Three briefs recur:

- **Blind answer.** Answer from the sources in your language only. Options are
  shuffled, and fixed blocks keep their order. Rule statements TRUE or FALSE
  first. Each row is `{answer, statements, second, quote, note}`.
- **Fix the flags.** The flags come from checkers who can be wrong, so confirm
  each against the source first. The brief lists what to fix: second answers,
  keys or statements the source does not support, wrong terms, garbled text,
  false citation tails, stems that misdescribe the source, missing locators and
  stale explanations. It also lists what the owner chose to leave. Output a
  patch, run `check`, and never apply it.
- **Review applied decisions.** For every changed item, check that the decision
  is implemented in full, the key is right and unique, the languages agree, the
  explanation matches, the citation points at the passage, and nothing else
  moved.

---

## Environment traps

- Force UTF-8 on tool output (`PYTHONIOENCODING=utf-8`), or non-Latin text comes
  back garbled and cannot be edited.
- Write patch files with the file-writing tool, not heredocs; long JSON heredocs
  break.
- `\\` in a shell command can reach the program as `\`. Build backslashes from
  codes (`chr(92)`) or use the file-editing tool, then verify the bytes.
- Keep the bank's line endings (a CRLF checkout is written back CRLF), or no
  apply round-trips byte for byte.
- Delete temporary browser profiles after rendering checks. One project left 200
  of them behind, 2.5 GB.

---

## Prior art

Checked in September 2026. None of these handles fixed option blocks, locators a
reader can turn to, languages kept aligned, or bank-level tells as tests; those
parts of this skill have no ready-made equivalent. Borrow ideas freely, but check
a repository's licence before copying code, because several carry none.

| Project | What to borrow |
|---|---|
| [huggingface/yourbench](https://github.com/huggingface/yourbench) | Citations as data: each question stores verbatim quotes and their source, and export fails when a source does not resolve. Its citation score is fuzzy word overlap, not a check of correctness. |
| [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | The nearest existing skill. Quizzes are drawn from a bank by a script, not by the model. Every graded item says where its question and answer came from. A missing source reads "source unknown", never an invented page. Failing transcripts are kept as tests of the skill. It is a tutor for one learner, with no rules on distractors or guessability. |
| [1EdTech QTI](https://www.1edtech.org/standards/qti/index) (2.1 and 3.0), used by TAO and OpenOLAT | The test vocabulary (selection, ordering, time limits, item session control), and `fixed` on single options, the one standard way to pin a fixed block. |
| Moodle XML, GIFT, [gpoore/text2qti](https://github.com/gpoore/text2qti), [R/exams](https://www.r-exams.org/) | Export targets. R/exams can draw N options from a larger pool, which stops candidates memorising option shapes; every subset it can draw must still pass the length guards. |
| [kerrickstaley/genanki](https://github.com/kerrickstaley/genanki) | Anki decks from code, with stable note ids. |
| [nbalepur/mcqa-artifacts](https://github.com/nbalepur/mcqa-artifacts) | The options-only audit (Balepur, Ravichander and Rudinger, ACL 2024). |
| [MadryLab/platinum-benchmarks](https://github.com/MadryLab/platinum-benchmarks), [aryopg/mmlu-redux](https://github.com/aryopg/mmlu-redux) | Triage by a panel of models, and a fixed set of error codes for items. |
| [NBME Item-Writing Guide, 6th ed.](https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf); Haladyna, Downing and Rodriguez (2002) | The standard lists of item-writing flaws, including convergence, clang, grammatical cues and the wording of true-false statements. Moore et al. (EC-TEL 2023) turned 19 of them into rules. |
| [ekzhu/datasketch](https://github.com/ekzhu/datasketch); LaBSE or [BGE-M3](https://github.com/FlagOpen/FlagEmbedding) | MinHash for duplicate sweeps at scale; cross-lingual embeddings for paraphrased duplicates and language alignment. |
| [ShinyItemAnalysis](https://github.com/patriciamar/ShinyItemAnalysis), mirt, [py-irt](https://github.com/nd-ball/py-irt) | Item analysis once there are responses; Tarrant, Ware and Mohammed (2009) for distractor thresholds. |
| [stanford-oval/storm](https://github.com/stanford-oval/storm), [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook), [Cinnamon/kotaemon](https://github.com/Cinnamon/kotaemon) | For study material: an outline first, then sections written with their citations; kinds of material defined as data; a citation that opens the highlighted source passage. |
| [open-spaced-repetition/ts-fsrs](https://github.com/open-spaced-repetition/ts-fsrs) | A spaced-repetition scheduler for the wrong-answer queue, small enough for a static app. |
