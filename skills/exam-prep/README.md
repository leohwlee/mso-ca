# exam-prep — turn any source into revision notes and mock exams

[繁體中文](README.zh-Hant.md) · [Download the skill](https://github.com/leohwlee/mso-ca/releases/download/exam-prep-v3.0.0/exam-prep-v3.0.0.zip) · [How it was built](references/case-study.md)

`exam-prep` is an [Agent Skill](https://agentskills.io): a folder of instructions,
references, scripts and templates that a coding agent (Claude Code, and others
that read `SKILL.md`) loads when someone asks it to turn documents or copy into
study notes, practice questions or a mock exam. It works for any subject, any
language or pair of languages, and any exam format.

It was distilled from this repository's own history: 43 releases in eight
weeks of building a bilingual question bank and study notes for the Hong Kong
MSO Competence Assessment, and the repairs each release needed. In five rounds
of side-by-side tests, the same model produced clearly better papers and notes
with the skill than without it (34 of 36 checks against 25 of 36; details
[below](#test-results)).

## What to ask it for

| You have | Ask for | You get |
|---|---|---|
| A policy, procedure or handbook | "A 20-question mock exam for new starters, 30 minutes, pass mark 80%, offline" | One offline HTML exam (timed paper, practice by section, wrong-answer book) and a separate printable key that names every answer and its clause |
| A textbook chapter or handout, in any language | "Revision notes and 15 true/false questions with traps like the teacher's" | Notes organised by the source's sections, with study tiers and traps beside the rules; a paper and a key with an explanation and citation for every statement |
| Product pages, sales copy or a spec sheet | "Certification practice questions in our format, and a one-page cheat sheet" | Items in your exact option block, a cheat sheet with every condition and exclusion, and a list of the claims the copy does not support |
| Statutes, guidelines, a professional syllabus | "A bank for the whole exam, drawn papers under the real pass rule" | A versioned bank of hundreds of items, papers drawn per section, blind review, coverage audits, notes per section |
| An existing bank | "Check these questions for give-aways" | Hard errors, a report of surface tells with a learnt guesser and simulated papers, blind-review packets |

Formats: single best answer, choose-all-that-apply, combination (K-type)
items, true/false, matching, ordering, cloze, numeric, short answers and
essays with mark schemes, and case sets. Export to QTI, Moodle XML, GIFT, Aiken
or Anki.

**Not the right tool** for secure or proctored testing (the offline app holds
its answers in the page), for scanned sources without a text layer (run OCR
first), or for judging work no mark scheme can describe.

## What makes it different

- **Every item is grounded.** Each question carries a citation with a locator
  and the verbatim sentence that decides it; the bundled check finds every
  stored quote in the extracted source text.
- **Traps that test reading, not luck.** Each false statement carries one
  small defect of a named kind: a degree word moved (*mainly* → *only*), a
  neighbouring number, the wrong actor, a dropped condition. Unrelated terms
  swapped in, which anyone can eliminate, are ruled out.
- **Measured against test-wise guessing.** A tells report scores "pick the
  longest", "pick the one most like the others" and a guesser trained on the
  bank itself, then simulates papers under the real pass rule. Combination
  options are generated so their structure gives nothing away.
- **Checks for what reviewers miss.** It warns when:
  - a key copies the source while its distractors are reworded;
  - a true statement is the source sentence cut down or joined;
  - one item's true statement gives away another item's false one;
  - the notes echo a false statement;
  - an explanation says "option B", which breaks when options are shuffled.
- **Notes written from the source, never from the questions.** They follow the
  source's structure, put traps beside the rules they protect, count the
  members of every list, keep qualifiers exactly, and offer a tier filter and a
  recall mode.
- **The exam's real format, decided first.** It reproduces a printed option
  block exactly, works out what that block lets candidates infer, and draws
  papers under the real per-section rules.
- **Proportionate.** A ten-question request takes the quick path; a full bank
  gets independent review, versioning and audits.
- **An offline exam app included.** It offers:
  - a timed mock with an answer sheet;
  - practice by section;
  - a wrong-answer book;
  - self-marking for written answers;
  - history export;
  - item ids on screen that match the printed key.

## Test results

Three realistic requests were each run with and without the skill by the same
model (Claude Opus 5.5). A separate grader judged every output against written
checks:
- an English infosec policy made into a 20-question offline mock exam;
- a Simplified Chinese biology handout made into notes, 15 true/false items and 3 short answers;
- product copy made into 10 combination items and a cheat sheet.

The checks were tightened after every round, so later rounds are harder.

| Round | With the skill | Without | Skill changes since the round before |
|---|---|---|---|
| 1 | 24/24 | 24/24 | First version. The checks were too easy to tell the runs apart |
| 2 | 31/31 | 27/31 | A quick path for small jobs, traps a half-prepared reader falls for, reworded true statements, notes that never copy the questions |
| 3 | 31/35 | 26/35 | A check for one item giving away another, scenario stems, item ids in the review and the key, a time-out check |
| 4 | 34/36 | 26/36 | Checks for copied keys, copied true statements and leaking notes; degree-word traps |
| 5 | 34/36 | 25/36 | A stricter copy rule, the leak check in both languages, short answers protected from give-aways |

Round five, per request:

| Request | With the skill | Without | Tokens (with / without) | Time (with / without) |
|---|---|---|---|---|
| Policy → offline mock exam | 11/11 | 10/11 | 230k / 180k | 18 / 16 min |
| Chinese handout → notes and true/false | 12/13 | 9/13 | 286k / 116k | 28 / 9 min |
| Product copy → combination items | 11/12 | 6/12 | 292k / 120k | 43 / 8 min |

What the runs without the skill got wrong in round five:
- **Policy exam:** six keys copied the policy word for word among reworded distractors.
- **Chinese notes:**
  - they turned the handout's 主要 ("mainly") into 只 ("only");
  - they spelled out the wrong version of all eight false statements;
  - true items copied the handout;
  - several true/false items gave away short-answer marks.
- **Product items:**
  - no stem gave a customer situation to apply;
  - at least ten statements copied the page;
  - one item gave away another ("the tank holds 4 litres" beside "1.2 litres");
  - explanations named no section of the page;
  - two statements were about the copy rather than the product.

What the skill still missed:
- **Chinese handout:** one true item kept the handout sentence's structure with synonyms swapped in.
- **Product items:** the run noted that the user's option block allows at most one false statement, but not that this lets candidates stop at the first false one.

Both now have explicit guidance, which has not yet been re-measured.

**Cost.** With the skill, a run uses 1.3 to 2.5 times the tokens and takes
longer. Almost all of the extra is the model's own reasoning about the checks,
not reading files.

**Limits of these numbers.**
- Each configuration ran once per round, and a model graded it.
- Each skill run's re-answer of its own paper is a self-check, not an
  independent review.
- The runs without the skill were made once and regraded each round.

The test cases are in [`evals/`](evals/), in the layout `claude plugin eval`
reads, so anyone can re-run them.

## Install

Download [exam-prep-v3.0.0.zip](https://github.com/leohwlee/mso-ca/releases/download/exam-prep-v3.0.0/exam-prep-v3.0.0.zip)
and unzip it into your agent's skills folder. For Claude Code, use one of:
- `~/.claude/skills/exam-prep/`, for all projects;
- `<project>/.claude/skills/exam-prep/`, for one project.

Then ask in plain words, for example:
"Turn these PDFs into revision notes and a 40-question mock exam".

The scripts need Python 3.9 or later and nothing else. PDF extraction uses
PyMuPDF or pypdf when either is installed.

## Try the example

```bash
python scripts/selftest.py
python scripts/bank_tool.py check assets/example/spec.json assets/example/bank.json --sources assets/example/sources
python scripts/build_app.py assets/example/spec.json assets/example/bank.json -o example-exam.html
```

Copy `assets/notes-template.html` beside `example-exam.html` as `notes.html`,
and the app's "Read this in the notes" links work.

## What is in the folder

| Path | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The method: principles, scales and the quick path, phases from intake to delivery |
| [`references/`](references/) | Formats and the item schema, item writing and the trap taxonomy, study material, sources, verification, production at volume, and the case study |
| [`scripts/bank_tool.py`](scripts/bank_tool.py) | Check a bank, report tells, generate combination options, make and compare blind-review packets, print papers with keys |
| [`scripts/sources.py`](scripts/sources.py) | Extract and search PDF, DOCX, HTML and text sources |
| [`scripts/build_app.py`](scripts/build_app.py), [`scripts/notes_check.py`](scripts/notes_check.py) | Build the offline exam app; check a notes page |
| [`scripts/selftest.py`](scripts/selftest.py) | Plants a defect for every check and confirms each one catches it |
| [`assets/`](assets/) | The exam app, the notes template, a decisions register and a worked bilingual example |
| [`evals/`](evals/) | The three behaviour tests above, with their inputs and graders |

This repository's own authoring rules remain in
[`docs/authoring/exam-prep/GUIDE.md`](../../docs/authoring/exam-prep/GUIDE.md)
and [`bank/FORMAT.md`](../../bank/FORMAT.md).

## Licence

MIT, like the code in this repository.
