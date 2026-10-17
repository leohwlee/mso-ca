---
name: exam-prep
description: Turn a fixed set of source documents (statutes, regulations, guidelines, manuals, course notes; in one language or two) into exam preparation — a cited study pack, a multiple-choice question bank, and a mock exam that draws papers under the real rules — for any exam format the user defines as data. Use when asked to write revision notes, a study guide or pack, practice questions, a question bank, a mock paper or a mock-exam app from documents; to define or change an exam format (sections, question formats, fixed option blocks, pass rule, timing); or to audit existing material for wrong or second-defensible keys, ungrounded or superseded content, duplicates, drift between languages, or answers a candidate can guess from surface form without knowing the material.
license: MIT
metadata:
  version: "2.3.0"
  replaces: "exam-prep 2.2.0"
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
   in aggregate. Measure the bank. Enforce stable, decisive rules as tests; calibrate style diagnostics to the format and reviewed examples.
4. **Decided first.** Every rule the owner settled late cost a sweep of the
   whole bank. Length rules cost 1,194, then 442, then 637 rewrites. Chinese
   terminology cost 169, then 662, then 533. Source conflicts cost 29, then
   93. Superseded sources cost 49, clause-number questions 52, the language
   rule 47 and out-of-scope questions 27. Phase 0 asks all of those questions
   before anything is written.

## Existing decisions and authorization

Read the project's exam spec, source scope, authoring guide and decisions register
before applying defaults. The owner's settled choices override generic examples,
including format, strict reading, terminology and exclusions. Reuse decisions and
authorization already supplied in the session; do not repeat intake or download
permission questions for routine work inside that scope. Ask only when a material
decision is missing or a genuine conflict changes scope or what will be taught.
Permission to author or review does not itself authorize external publication.

## Choose the mode

| Mode | Do |
|---|---|
| Build | Phases 0–7 in order. |
| Extend: new questions, pages, sources or formats | Re-read the spec and the register. Run Phase 1 for any new source, then write. Run every guard and the twin check against the whole bank, then Phase 6 on what changed. |
| Coverage audit | Source-first coverage mapping below, then a prioritized, deduplicated gap list. Report findings without changing the bank unless repairs or additions are authorized. |
| Answer audit | Phase 6 and a tell sweep. Measure everything before changing anything. Report findings only unless asked to fix, and let the owner decide each item. |
| Change the format | Edit the spec, add the format's guards and change the draw logic. Only then convert or write items: a draw filter costs one edit, while converting questions costs an agent each. |

---

## Phase 0 — Intake: the spec and the register

Two files govern everything. The **exam spec** says what a paper looks like. The
**decisions register** records every judgment the owner has made. The app, the
guards and every brief read them, and nothing hard-codes them.

**Resolve genuinely missing decisions before writing.** Read existing answers first.
For unresolved material choices, give a recommendation and record the decision:

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
  Routine downloads within the user-authorized source scope may proceed; seek a decision for a new source or material scope change.
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
    verifies source identity and text occurrence, not semantic support. A quote
    that stops matching flags a changed source; reading the surrounding rule
    still decides whether the key follows from it. The reference bank added its quotes only after 1,500
    questions existed, recovering most from the answer files of earlier blind
    reviews. Every recovered quote came from the right passage, but a random
    sample found a fifth stopping short of the deciding words. Write the quote
    with the question, and have the blind reviewer confirm it.
  - The key at a fixed index for shuffled formats, and fixed blocks stored
    verbatim.
  - Stable ids for items, and for each option an id shared by all its language
    versions. Store attempts by option id rather than position, so neither a
    reordered option nor a new one can corrupt a candidate's history.
  - Source units and decision points the item directly tests, with statement
    references where applicable. Background mentions and explanation-only
    material must be distinguished from tested content.
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
  - section-by-section listings and unsupported institution directories;
    retain cited comparisons of examinable functions, powers and boundaries;
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
  body or condition. Avoid surface giveaways from overstatement ("only", "always");
  if the project explicitly tests strict qualifiers, preserve that choice and
  check the distribution of such wording across true and false statements. They
  must not use a tail citing a provision as if it said the false thing ("per
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
  genuine restatements in another actor or procedure. Distinguish separate
  legal subjects whose obligations must each be learned; similar wording alone
  is not duplication. Deliberate spaced practice requires the project's approval
  when its deduplication rule would otherwise exclude it. When a section runs out of unkeyed points, say so.
  Reaching into out-of-scope provisions to fill it is how scope faults start.
- **Keep options in one length band while writing** (the standout rule in the guard catalogue).
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
- **Record the model the subagents actually use.** Check the environment's
  inheritance and override behavior; do not assume that a different reviewer
  means a different model or model family.

---

## Coverage audit — before filling gaps

Build the checklist from each source, including definitions, purposes, functions,
powers, conditions, exceptions, footnotes, appendices and forms. For institutions
and roles, list nature/purpose, specific duties, decision authority and easily
confused identities; a name appearing in a stem proves none of these is tested.
Never invent missing functions from general knowledge or expand to other sectors
without the owner's scope decision.

Map each decision point to a direct question/statement in the whole bank. Record
covered, partial, missing or reference/out of scope; include the exact missing
aspect, source locator, primary module and cross-module evidence. Distinguish
an overall bank gap from insufficient practice in a particular module. Do not
count known wrong-key or unsupported statements as valid evidence. A correctly
keyed false statement can directly test the rule it departs from. Record exclusions from the
register alongside the positive scope, and check for out-of-scope content too.

Keep an image-page reading account. Render and inspect pages containing diagrams,
screenshots or scans; missing extracted text does not mean the point is absent.
Any manually transcribed labels must retain page, language and source version,
and be checked against the original image by a different reviewer.

Merge the same gap across statutes, guidance, FAQs and circulars into one task,
while preserving each source's mapping. Prioritize by importance of the duty,
decision-changing conditions and error consequences, not guessed exam frequency.
Reuse existing direct evidence, then author only the residual decision points.
Do not pad a question with duplicates to meet a batch size or format minimum.

Preserve the audit baseline and subsequent implementation records: source, bank,
quotes and register versions/hashes; question ID, statement index, exact text and
truth; task status and final review evidence. Bind a blind verdict to the actual
final text. After changes, reconstruct or retain historical snapshots rather
than silently updating old hashes. Validate new mappings against active content.
Coverage is a proportion of a declared checklist, never a claim of exam coverage
or a probability of passing.

## Phase 6 — Verification

Required for each changed question: relevant source context in each language,
independent blind answers, unique key, final explanation and deciding evidence,
pack comparison, whole-bank semantic deduplication and applicable mechanical
guards. Re-review changed final text; unchanged content keeps its prior evidence.

Review semantic support separately from quote occurrence: actor, scope, condition,
exception, modal strength, AND/OR lists and cross-references. For a true statement,
actively look for a compliant counterexample that would make it false. For an
invented false statement, check that it is not true under another permitted route.

Use additional panels, different-family adversaries, embeddings and simulations
when material changes, detected risks, project requirements and available tools
justify them. Existing project hard checks remain required; do not silently
downgrade them to diagnostics. State which checks ran, their scope and limitations.
Do not claim unavailable or unrun checks passed.

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
- **Calibrate before a bulk review, on a sample the best model has judged.**
  First a mechanical filter: the reference bank scored each stored quote by the
  share of the key's words it contained, set the threshold so that no defect in
  a judged sample of 120 slipped through, and skipped 57% of 2,862 quotes.
  Then the cheapest model that matches the best one on that same sample: Sonnet
  caught all 24 defects the best model had found, while Haiku caught 18 and
  flagged a fifth of the good quotes. A calibration costs two packets; a model
  that misses a quarter of the defects wastes the whole sweep.
- **Treat findings as claims too.** An adjudicator's verdict is not verification:
  of three "criticals", a second look downgraded two. Separate strands re-find
  the same defect, and 51 cross-strand duplicates had to be merged before the
  counts were honest.
- **For a deeper tell audit, run a test-wise adversary**: a model from a different family from the
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
  find (catalogue below). The strongest is one learnt from the bank itself: a
  conditional logit over each option's length, standout, overlap with the other
  options and word-level cues, cross-validated so it is scored only on items it
  never saw. In the reference bank it picked 44% of four-option keys in English
  and 46% in Chinese, against 25%, almost all through the absolutes and hedges
  the owner chose to leave. It passed one simulated paper in 4,000, so it runs
  as a test there, bounding both numbers.
- **Don't ask a model whether an item is flawed.** Whole-item judges have poor
  precision: rules found 91% of the flaws human reviewers found, against 79%
  for GPT-4, and the best detector of errors in a large public benchmark reached
  an F2 of about 40. Turn the flaws a string check can catch into guards, and
  keep models answering, not grading.
- **For a deeper language-drift audit,** embed every item's
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
  bilingual view pairs `options[i]` across languages. The spec must declare
  whether options, statements or both reorder, how numeric subsets are remapped,
  what all/none means and what must stay fixed. A format with remapped statements
  may keep all/none at the last position; immutable official samples follow the
  project's explicit preservation rule.
- **History stays on the device**, with export and import to a file.
- **Survive bank changes.** Version scoring-relevant content: a changed meaning,
  truth or option set can invalidate attempts even when the option count stays
  the same. Use a new stable ID or content version; preserve the original scored
  attempt as historical, or explicitly invalidate it under the owner's rule.
  Drop retired IDs from new draws and discard incompatible stored orders. Never
  silently re-score an old attempt against a different question.
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

Read [guard catalogue](references/guards.md) when adding, changing or interpreting
checks. It separates deterministic requirements from calibrated style diagnostics;
the project's approved hard checks still govern.

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
- **Scoring-relevant edits need history handling**, even with an unchanged
  option count. Version or replace the question and preserve old scores; discard
  incompatible stored orders before resuming a paper.
- **Before a bank-wide rule, build the tool**: `list`, `check`, `apply`.
- **A bank-wide share sitting at its limit tips on one edit.** When trimming,
  keep a distractor longer than the key.

---

## Working with the owner, and reporting

- **Put decisions on a page the owner can act on**: one item per decision, the
  question in plain words, a recommendation and a control. Read the picks back
  before acting, and ask about blanks and "discuss".
- **Fix within the authorized mode.** In a report-only audit, record findings
  and recommendations without editing the audited material. In authorized
  extension or repair work:
  - A small, clear defect: fix it in the same session, and say so.
  - A pattern: sweep every occurrence, then guard it. Fixing only the items a
    findings list named left the same invented terms in about 160 others.
  - A large class that needs judgment on each item: measure and report scope;
    complete it if already authorized, otherwise recommend the additional work.
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

## Tooling and reference implementations

Read [tooling and prior art](references/tooling.md) only for environment problems,
tool selection or background research. Historical measurements are examples,
not universal thresholds or evidence about the current bank.
