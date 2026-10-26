---
name: exam-prep
description: Turn source material — documents, textbooks, lecture slides, manuals, policies, statutes, standards, transcripts, product or marketing copy, in any language or several — into revision material and practice assessments - study notes, comparison tables, figures, flashcards, question banks, quizzes, printed mock papers and an offline mock-exam app. Works for any topic, any exam format and any question style (single-best or multi-select MCQ, combination/K-type, true/false, matching, ordering, cloze, numeric, short answer, essay or case questions with mark schemes). Use whenever someone wants to revise, study, teach, train or test from documents or copy - preparing for a certification, licensing, school or internal exam; writing practice or quiz questions or a mock paper; defining an exam format; or auditing existing questions or notes for wrong or ambiguous keys, unsupported claims, coverage gaps, duplicates, language drift or answers guessable without knowing the material.
license: MIT
metadata:
  version: "3.0.0"
  replaces: "exam-prep 2.3.0"
---

# Exam prep from source material

This skill turns a fixed body of material into preparation for an assessment:

- **study material** the learner reads (notes, tables, figures, flashcards), every
  line traceable to the source;
- **questions** they practise on (a bank, a quiz, a printed mock paper), every
  key traceable and checked by someone who did not write it;
- **a mock exam** that draws papers from the bank under the real rules, offline,
  in one HTML file.

Any of the three can be made alone. Nothing below assumes a topic, a language, a
number of options, or even multiple choice: the assessment's shape is data (the
*exam spec*), and the owner's judgments are recorded once (the *decisions
register*).

The method was distilled from one project taken through 43 releases in eight
weeks: a bilingual (English and Traditional Chinese) question bank and
seven-part study notes for a Hong Kong licensing exam, written from up to 47
official documents, and the repairs each release needed.
[references/case-study.md](references/case-study.md) tells that story with the
measurements. Its numbers are evidence for a rule, not constants: re-measure on
your own material.

## Principles

1. **Grounded.** Every sentence of the notes and every key traces to a locator
   (section, paragraph, page, slide, timestamp) in the material, in the language
   the reader reads. Where your own knowledge and the material differ, the
   material prevails or the difference goes to the owner. Never fill a gap from
   general knowledge without labelling it.
2. **Valid.** A question is worth asking only if the sole way to answer it is to
   know the material. It must not fall to the shape of the options, a hedge word,
   a length, a semicolon or common sense.
3. **Realistic.** Practice is at least as hard as the real assessment and shaped
   like it. In the reference project, candidates who sat the real paper found it
   far harder than a large, carefully checked bank: the paper varied how many
   statements were false, changed single words, and changed its option sets from
   item to item, and the bank did none of that. Calibrate difficulty with someone
   who has seen the real thing before producing at volume.
4. **Measured.** The damaging faults are invisible one item at a time and obvious
   in aggregate: 1,241 of 1,510 keys were the longest option, and "mark the
   absolutes false" scored 66–71% against 20% for chance. Measure the bank, and
   turn the stable rules into checks.
5. **Decided first.** Every rule settled late cost a sweep of the whole bank:
   length rules 1,194, then 442, then 637 rewrites; terminology 169, then 662,
   then 533; source conflicts 29, then 93; superseded sources 49. Ask the
   decision questions before writing anything.
6. **Proportionate.** Match the process to the stakes. A ten-question quiz from a
   two-page memo needs grounding and a blind re-answer, not a review panel and an
   audit trail.

## Choose the job and the scale

| Job | Do |
|---|---|
| Build | Phases 0–6 in order, for the products asked for. |
| Extend: new items, notes, sources or formats | Re-read the spec and the register. Run Phase 1 for any new source, then write. Run every check against the whole bank, then Phase 5 on what changed. |
| Answer audit | Phase 5 and a tell sweep. Measure before changing anything; report findings unless asked to fix them, and let the owner decide each one. |
| Coverage audit | Build the source-first checklist (Phase 2), map it to the bank, report a prioritized, deduplicated gap list. |
| Change the format | Edit the spec, the checks and the draw logic first; convert items after. A draw filter costs one edit, while converting items costs a review each. |
| Convert or export | Map the bank to the target ([formats](references/formats.md#export)) and report what the target cannot represent. |

| Scale | Typical | Required | Add when warranted |
|---|---|---|---|
| Quick | up to ~30 items or a few pages of notes, one user, one sitting | the quick path below | the tells report once the bank has 20 or more items of one kind |
| Standard | a course or exam; 50–1,000 items; notes per section | Quick, plus spec and register files, archived sources, a source-first checklist, a calibration batch, independent blind review of every item, the tells report, the app | review panels, adversarial audits |
| Rigorous | high stakes, public, several languages, long-lived, many writers | Standard, plus stored deciding quotes checked against the sources, verdicts bound to the final text, versioned items and history, a release process | different-model panels, cross-lingual embeddings, item analysis of real responses |

Say which scale you are working at and why. Move up when the owner asks, or when
the stakes, the size or a finding call for it. Process costs the owner time and
money: at the Quick scale, a source archive with hashes, a register file,
planted-defect tests (the bundled checks already prove themselves in
`selftest.py`), screenshots of pages nobody asked for and repeated tells runs
are waste, and they made test runs of this skill three times slower without
improving a single key.

### The quick path

Most requests are Quick: "make a quiz from this", "turn these notes into
flashcards", "a mock paper from chapter 5".

1. **Read the whole source once** and decide the open questions yourself with
   the defaults in Phase 0; list the assumptions in your reply. Ask first only
   when an answer would change what you build (the exam's real format, which
   language, who sits it).
2. **Write a short checklist** of what the source makes examinable (Phase 2),
   in your working notes, and aim the items at it.
3. **Write the items into `bank.json`** (schema in [formats](references/formats.md))
   with a citation, a deciding quote and an explanation per option or
   statement, following Phase 4. Keep `spec.json`, `bank.json` and any script
   in one `work/` folder: they let anyone regenerate the products.
4. **Check**: `bank_tool.py check` (with `--sources` if you extracted the text,
   and `--notes` when you made notes), then answer every item yourself once from
   a `packet` with the key hidden, and `compare`. Fix what that finds and
   re-answer only the items you changed; a second full round, and the tells
   report below 20 items, cost more than they find at this scale.
5. **Deliver exactly what was asked, in the form asked**: the app
   (`build_app.py`) when they want an exam to sit on screen, a paper and key
   (`bank_tool.py paper`) when they want something to print or check, notes from
   the template when they asked for notes. Offer anything else in one line
   instead of building it.
6. **Report in a few lines**: what you made, what you checked and how
   (a self re-answer is not an independent review), what you assumed, and what
   the owner should decide.

---

## Phase 0 — Intake: the spec and the register

Read what is already decided (project files, earlier messages, an existing spec
or register) before asking anything. The owner's settled choices override every
default in this skill. For each material decision still open, ask with a
recommendation: people decide quickly between clear options. With many open
items, put them on one page with one control each, and read the picks back
before acting.

Settle:

- **Purpose and audience.** Preparing for an *external* exam (match its format
  and difficulty; the examiner's sources define the scope), *setting* an
  assessment from the material (you design the format; validity and fairness come
  first), self-study, or staff training. Who sits it, in which language, with how
  long to prepare, open or closed book.
- **Sources and scope.** The exact list, every language edition, and whether only
  current editions count (default: yes). What is examinable: take it from the
  examiner's guidance; circulars, FAQs, errata and appendices often are, and they
  are the part nobody archives. Whose rules or knowledge the exam tests: a point
  earns its place only if it applies to the person the exam is for.
- **Format.** Look for an official specification, sample questions, past papers
  and worked examples in the syllabus, and ask anyone who has sat the exam.
  Reproduce a printed format character for character. With no format to follow,
  propose one that suits the purpose ([formats](references/formats.md)) and ask.
- **Difficulty and reading.** How literally a statement is judged (*strict*: a
  dropped qualifier makes it false, while a faithful rewording stays true; or
  *ordinary*), which trap kinds are fair, the
  mix of recall and application, and whether numbers, dates and names may be the
  unknown.
- **Languages and terms.** Which languages, and what each follows where the
  editions differ. Default: each language follows its own official text, and no
  item turns on a difference between them.
- **Conflicts.** Contradictions within or between sources go to the owner one by
  one (Phase 1). Never settle one silently.
- **Deliverables.** Which products, in which medium (offline HTML, print,
  Markdown, flashcards, a learning platform), and how the learner will use them.
- **Review depth and the stop rule.** Default: once blind review confirms rather
  than corrects, a further check triggers a fix only for a wrong key or a second
  defensible answer.

Record the answers in two files that the app, the checks and every brief read:
the **exam spec** (`spec.json`; schema in [formats](references/formats.md),
example in `assets/example/spec.json`) and the **decisions register**
(`DECISIONS.md`; skeleton in `assets/templates/DECISIONS.md`). At the Quick
scale both can be a short block at the top of the deliverable.

**When the material is copy, not documents** (marketing pages, product sheets,
sales scripts, pitch decks): separate the verifiable facts (features,
specifications, prices, policies, procedures, claims with a stated basis) from
the persuasion (slogans, superlatives, tone). Test what the learner must state or
do correctly. Never key a slogan as a fact, and flag claims the copy makes but
does not support. The copy is the authority for what the organisation says, not
for what is true; record that in the register.

## Phase 1 — Sources

- **Archive every source locally** under stable numbered names, with a manifest:
  number, title, edition or date, origin, date checked, hash. Work from the
  archive, because a citation that moves is worse than none.
  `python scripts/sources.py extract FILE… --out text --lang en` writes
  `text/en/NN.txt` with a marker per page (the layout `bank_tool.py check
  --sources text` reads), and `manifest` the hashes.
- **Extract once and normalise before searching**: Unicode compatibility forms,
  whitespace and line breaks inside CJK text, ligatures, soft hyphens. Otherwise a
  term that is present looks absent. `python scripts/sources.py find` searches the
  normalised text and prints document, page and context; every later phase and
  every subagent uses it. Search for a distinctive 5–9 word phrase rather than a
  section number, which lands in the table of contents.
- **Read poorly extracted pages as images**: scans, tables, diagrams,
  screenshots, forms. A failed text search never proves a point is absent.
- **Current editions only.** When a source is removed, re-cite its points to the
  current one, and list for the owner any point that only it made.
- **Sweep for conflicts before writing**: between documents, within one, between
  language editions, and apparent conflicts that are not. Write each as a
  decision the owner can make in a minute: both sides quoted with their locators,
  a recommendation and the rule behind it (statute over guidance; later or more
  specific over earlier or general). Record the outcome as **one** answer
  everywhere; each language keeps its **own** text and nothing may turn on the
  difference; **both** are true and an item must say which it tests; or **none**
  (not a conflict, recorded so nobody raises it again).
- **Keep a terminology table per source and language.** Take each term from the
  document an item cites, never by find-and-replace across the bank.
- **Record each source's volume**, which sizes the blueprint, and say what you
  covered and what you could not reach.

Details: [sources](references/sources.md).

## Phase 2 — Blueprint

- **Build the checklist from the sources, not from questions**: definitions,
  purposes, lists (with how many items each has), conditions, exceptions, numbers
  and time limits, actors and their powers, processes, and easily confused pairs.
  Give each point a priority. The checklist drives the notes, the bank and every
  later coverage audit.
- **Size each section to the material behind it**, not to a round number. Equal
  sections over unequal sources make writers reword each other's questions, which
  is where duplicates come from.
- **Size the bank to the draw.** The smallest section bounds how many distinct
  papers can be drawn. Aim at several times the draw in every section, so that a
  candidate sitting several mocks reasons rather than recognises (the reference
  bank grew from 20 to about 200 items per section for this reason).
- **Choose formats by purpose.** Single-best items teach, because a wrong answer
  names the rule not yet learnt; the examiner's own format rehearses. Both can
  live in one bank behind a mode switch.
- **Write the checks before the first item.** `python scripts/bank_tool.py check`
  covers the generic ones. Add the project's own (banned renderings, required
  terms, scope rules), and prove each check can fail by planting one defect.

## Phase 3 — Study material

The notes exist so the learner recognises a situation and recalls the rule, not
so they can index the source. Write them from the sources, never from the
question bank: a bank is a sample of the material, worded around its
distractors. Use the bank only afterwards, to find gaps.

- **Organise by the exam's own sections**, keeping together what the source keeps
  together. A heading states the situation or the plain rule, and the citation
  trails as support. A clause number is never the subject.
- **Choose the form by the content.** A process becomes a flow; rules that change
  with the situation become a table whose rows are the situations; numbers and
  time limits become a table of the number, what it governs, when it starts and
  what follows; a source list becomes a card that shows its count; easily
  confused pairs sit side by side. Bullets come last. Draw the relationship the
  source states: overlapping cases are not a decision tree.
- **Keep every condition, exception, qualifier and modal strength** (must,
  should, may) beside the rule it limits, and complete every enumerated list: a
  partial list teaches a wrong list.
- **Give every block a study tier**: *Remember* (lists, numbers and names to
  recall exactly), *Understand* (reasoning and conditions), *Recognise* (enough to
  spot it in an option), *Reference* (context). Offer a filter by tier.
- **Put the traps where they arise**: the near-identical name, the neighbouring
  threshold, the other actor, the owner's conflict rulings. State the rule and
  the word to watch, never the wrong version: notes that spell out the bank's
  false statements hand over the paper, and practice becomes recognition
  (`bank_tool.py check --notes` warns of it).
- **One language per view**, plus a combined view when there are two. No page
  compares the editions.
- **Prefer aids that change how the content is read** (a tier filter, a numbers
  table, deep links from each question to its notes section, a wrong-answer book)
  over another layer of prose. The reference owner removed a 60-fact quick sheet
  per part because it only restated the tiers and figures. Ask before adding a
  feature, and do not re-propose a removed one in the same form.

`assets/notes-template.html` is a single offline page with these components, a
tier filter, a language switch, a recall mode and a contents list;
`python scripts/notes_check.py` checks its citations, tiers, anchors and language
pairs. Details: [study material](references/study-material.md).

## Phase 4 — Writing questions

**Calibrate first.** Write about two items per section in the intended style,
show them to the owner (ideally someone who has sat the exam), adjust difficulty
and trap style, and only then produce at volume.

Every item, in every format:

- **The unknown is substance.** Ask about the rule, the concept, the consequence;
  not what a clause number says, where a rule lives or its exact wording, unless
  the real exam does. Stems name the topic in words. Ask about the subject, not
  the source: "the page gives no evidence for its slogan" is a finding for the
  owner, not a statement to key true.
- **Apply where the source has rules on dates, quantities or conditions**: at
  least two items open with a situation the candidate must decide, whatever the
  format.
- **Exactly one defensible answer** under the reading the register declares.
  Before keying, re-read the whole list or passage the item draws on: most second
  answers came from swapping in one true option without checking its siblings.
- **Distractors are wrong on substance and drawn from the material**: another
  actor's duty, the neighbouring threshold, another procedure's deadline, an item
  from a related list. Write them in the key's register; when keys paraphrase the
  source and distractors are invented, readers (and models) learn to tell them
  apart.
- **Under strict reading, each false statement carries one small defect of a
  named kind** (off-list item, added words, widened or narrowed scope, reversal,
  dropped qualifier, changed number or period, wrong actor, changed modal, a
  near-identical name, the rule moved to the wrong case). A changed number or
  period makes a statement false only if the source no longer implies it: where
  the source requires a check from 8,000, "a check is required from 10,000" is
  still true.
- **Make the defect one a careful but under-prepared reader accepts.** The
  hardest and fairest traps change the source's own qualifiers and degree words
  (mainly → only, least → not at all, no longer rises → falls, within a range →
  always), its neighbouring numbers and its near-identical actors. Swapping in
  an unrelated term (mitochondria for chloroplast) is an easy mark, not a trap.
  Where the source grades its claims and the owner wants detail traps, aim about
  half the false statements at its degree words; a short answer on a section is
  no reason to leave that section's degree words untested.
- **Paraphrase true statements**, keeping every qualifier. A true statement
  copied word for word from the source can be recognised by matching rather than
  understood, and next to reworded false statements it becomes a tell.
- **Statements and options stand alone**: no "statement 2", "the above", "the
  former", nothing that breaks when the app shuffles them. Frequency words
  ("usually", "often") appear only where the source uses them.
- **No twins.** Before keying a point, check it is not already keyed, or stated
  as true, elsewhere in the bank. A new application of a known rule is welcome
  when the decision turns on different facts; a restatement is not new coverage.
  Nor may one item answer another on the same paper ("holds 4 litres" keyed true
  beside "holds 1.2 litres" keyed false), and no statement may assert a scoring
  point, or a premise the mark scheme rewards, of a written question on that
  paper. An overlap you notice is rewritten, not shipped as a "weak hint".
- **Parity.** Keep options (or statements) in one length band, trimming the key
  rather than padding distractors. Put absolutes, negations and hedges on true and
  false statements alike.
- **Explanations** say, for every option or statement, why it is right or wrong
  in the source's deciding words, with the locator. They refer to content, never
  to a letter or number that shuffling changes.
- **Capture the deciding quote with the item**, verbatim from the cited passage
  (for a false statement, the passage it departs from). Quotes recovered later
  stopped short of the deciding words about a fifth of the time.
- **Constructed-response items** (short answer, essay, case analysis, calculation)
  carry a model answer, a mark scheme of points or levels, acceptable
  alternatives and common wrong answers, each grounded like a key.

At volume, subagents write in disjoint packets and return patches; one applier
validates and merges each item; packets save every ~8 items and are checked
against their id lists; every check runs on the merged bank. Briefs and tooling:
[production](references/production.md). Writing guidance, the trap taxonomy,
tells and language rules: [item writing](references/item-writing.md).

## Phase 5 — Verification

Reviewing an item with the key in view verifies nothing. The reviewer must
answer it.

1. **Mechanical checks first**, before any review packet, because every wording
   change after review voids that review. `bank_tool.py check` reports hard
   errors (schema, keys, option sets, positional references, citations,
   duplicates, quotes missing from the source text); `bank_tool.py tells` reports
   diagnostics (length tells, absolutes, hedges and negation by truth, answer
   spread, and a guesser that learns surface features from the bank and sits
   simulated papers under the pass rule).
2. **Blind review.** `bank_tool.py packet` writes keyless, shuffled packets per
   language. A reviewer who did not write the items answers each one from the
   cited source: every statement ruled true or false first, a deciding quote of 40
   words or fewer with its locator, any *second* defensible answer, notes.
   `bank_tool.py compare` lists the disagreements; settle each against the source,
   never by majority.
3. **Semantic support is not quote occurrence.** A quote that exists may still not
   support the claim: check actor, scope, condition, exception, modal strength,
   AND/OR and cross-references. For each true statement look for a compliant
   counterexample; for each invented falsehood check that it is not true by
   another route.
4. **Compare every key with the notes.** Blind answering cannot see a key that is
   merely narrower or wider than the rule when the distractors are plainly wrong.
5. **Sweep for duplicates across sections**, in every language, by meaning as
   well as by wording.
6. **Re-review changed text, and bind each verdict to the text it judged** (a
   hash). After a bulk rewrite, re-verify: an audit of the old text has not
   audited the bank you now have.
7. **Report honestly**: which checks ran, on what, by which model. The same model
   in a fresh context gives a blind check, not an independent one. Counts are not
   coverage, and a checklist proportion is not a chance of passing.

After the first review, expect second defensible answers rather than wrong keys,
and look where they breed: enumerations, statements drawn from one list, and
anything a rewrite touched. Panels, options-only and closed-book adversaries,
calibrating a cheaper reviewer, language drift, coverage audits and item
analysis: [verification](references/verification.md).

## Phase 6 — Delivery

- **The mock-exam app.** `python scripts/build_app.py spec.json bank.json -o
  exam.html` validates both, then embeds them in `assets/exam-app.html`: one
  offline file with a timed mock under the real draw and pass rule (saying why a
  paper failed), practice by section with feedback after each answer and unseen
  items first, a wrong-answer book that clears an item after two correct answers
  in a row, self-marking against the mark scheme for written answers, history on
  the device with export and import, a language switch, and a link from each item
  to its notes. It shuffles per draw (options, or statements with the options
  relabelled) identically in every language, and stores answers by stable id and
  version, so a bank change cannot corrupt history. Each question shows its
  item id, during the paper and in the review, and the printed key gives it
  too, so a trainer can match a question to the key. Before handing it
  over, sit one paper: submit it, check the score and the pass rule either side
  of the pass mark, and let a copy built with `"minutes": 1` run out to see it
  submit itself.
- **Printed papers**: `python scripts/bank_tool.py paper spec.json bank.json
  --out paper.md --key key.md` draws one paper under the spec (or `--all`
  items) and writes the question paper and a separate key with explanations
  and citations, shuffled once and frozen. A key that accompanies the app must
  identify answers by their wording, not by letter, because the app reshuffles
  options at every draw; or set `"shuffle": false` for that paper. An owner who
  does not work in Markdown gets the key as a page to open and print (HTML or
  PDF), not raw `.md`. Instructions
  that tell candidates how statements are judged say that a faithful rewording
  is still true ([item writing](references/item-writing.md#the-trap-taxonomy)).
- **Other targets** (flashcards, QTI, Moodle XML, GIFT): see
  [formats](references/formats.md#export).
- **Bundle** the notes, the app and, where the licence allows, the originals in
  one folder or zip, with a short README: what it is, how to open it, the
  disclaimer.
- **Change without breaking.** Ids are never reused. A change of meaning, truth
  or option set is a new version. Retire items in the app before deleting them,
  and say which release first carries a repair.
- **Disclaimer**: not an official product; where the sources conflict or are
  unclear, the answer follows the most defensible reading of the cited text; not
  professional advice where that applies.

## Working with the owner

- One decision per item, in plain words, with a recommendation and the rule
  behind it. Read the picks back before acting, and ask about blanks.
- Stay inside the job you were given: an audit reports, a repair fixes. Fix a
  small, clear defect and say so. Sweep a pattern everywhere, then add a check
  for it (fixing only the items a findings list named left the same fault in
  about 160 others). For a large class that needs judgment on each item, measure
  it, report it and recommend.
- Measure before you quote a number: triage a detector's output by hand first (of
  20 flags checked once, 2 were real), and broaden a detector before trusting its
  count.
- Asked "is it finished?", look. Reviewing one's own rewrite once found two
  regressions it had introduced.
- Use third-party papers of unknown provenance as a style reference only; never
  copy their questions into anything that will be shared.

## Files in this skill

| File | Read or run when |
|---|---|
| [references/formats.md](references/formats.md) | defining the spec or the item schema; choosing or adding a question format; scoring; exporting |
| [references/item-writing.md](references/item-writing.md) | writing or repairing items: distractors, the trap taxonomy, tells, items in two languages |
| [references/study-material.md](references/study-material.md) | writing notes, figures and flashcards; filling the notes template |
| [references/sources.md](references/sources.md) | archiving, extracting and searching sources; conflicts; terminology; language editions |
| [references/verification.md](references/verification.md) | blind review, checks, adversarial audits, coverage audits, evidence and reporting |
| [references/production.md](references/production.md) | working at volume with subagents; briefs; repairs; environment traps |
| [references/case-study.md](references/case-study.md) | why a rule exists, and the measurements behind it |
| `scripts/sources.py` | `extract`, `manifest`, `find` |
| `scripts/bank_tool.py` | `check`, `tells`, `options`, `packet`, `compare`, `paper`, `stats` |
| `scripts/build_app.py` | building the offline mock-exam app |
| `scripts/notes_check.py` | checking a notes page built from the template |
| `scripts/selftest.py` | after changing the scripts: proves each check can fail |
| `assets/exam-app.html`, `assets/notes-template.html` | the templates the scripts and you fill |
| `assets/example/` | a small spec and bank with one item of every kind |
| `assets/templates/DECISIONS.md` | the decisions register skeleton |

The scripts need only Python 3.9 or later; PDF extraction uses PyMuPDF or pypdf
when one is installed. Run any script with `-h` for its options.
