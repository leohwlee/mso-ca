# exam-prep — a skill for turning source material into revision material and mock exams

[繁體中文](README.zh-Hant.md)

`exam-prep` is an [Agent Skill](https://agentskills.io): a folder of instructions,
references, scripts and templates that a coding agent (Claude Code and others that
read `SKILL.md`) loads when someone asks it to turn documents or copy into study
notes, practice questions or a mock exam. It works for any topic, any language or
pair of languages, and any exam format: single-best and multi-select questions,
combination (K-type) items, true/false, matching, ordering, cloze, numeric, short
answers and essays with mark schemes, and case sets.

It was distilled from this repository's own history: 43 releases in eight weeks
of building a bilingual bank and study notes for the Hong Kong MSO Competence
Assessment, and the repairs each release needed. The method and its measurements
are in [`references/case-study.md`](references/case-study.md). The skill is
general-purpose; this repository's own authoring rules remain in
[`docs/authoring/exam-prep/GUIDE.md`](../../docs/authoring/exam-prep/GUIDE.md)
and [`bank/FORMAT.md`](../../bank/FORMAT.md).

## What it produces

| Product | How |
|---|---|
| Study notes | One offline HTML page per exam from [`assets/notes-template.html`](assets/notes-template.html): study tiers, traps beside the rules, list cards with counts, numbers tables, flows, a tier filter, language views and a recall mode |
| A question bank | JSON items in the schema of [`references/formats.md`](references/formats.md), each with a citation, a deciding quote and an explanation for every option or statement |
| A mock exam | One offline HTML file built by `scripts/build_app.py`: timed papers under the real draw and pass rule, practice by section, a wrong-answer book, self-marking for written answers, history with export and import |
| Checks | `scripts/bank_tool.py`: hard errors, a tells report with a surface-feature guesser and simulated papers, blind-review packets and comparison |

## Install

Copy the `exam-prep` folder into your agent's skills folder, for example
`~/.claude/skills/exam-prep/` for Claude Code (all projects) or
`<project>/.claude/skills/exam-prep/` (one project). Then ask in plain words:
"Turn these PDFs into revision notes and a 40-question mock exam".

The scripts need Python 3.9 or later and nothing else; PDF extraction uses
PyMuPDF or pypdf when installed.

## Try the example

```bash
python scripts/selftest.py
python scripts/bank_tool.py check assets/example/spec.json assets/example/bank.json --sources assets/example/sources
python scripts/build_app.py assets/example/spec.json assets/example/bank.json -o example-exam.html
```

Copy `assets/notes-template.html` beside `example-exam.html` as `notes.html` and the
app's "Read this in the notes" links work.

## Tests

`scripts/selftest.py` proves every bundled check can fail. `evals/` holds three
behaviour tests: a policy turned into a 20-question offline mock exam, a
Simplified Chinese biology handout turned into notes and true/false items, and
product copy turned into combination items and a cheat sheet. Each has a prompt,
its input file and graders, in the layout `claude plugin eval` reads; from this
folder, `claude plugin eval . --scaffold --allow-tools Write,Edit,Bash` runs them
with and without the skill. These are real, billed model runs.

## Licence

MIT, like the code in this repository.
