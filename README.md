# MSO Competence Assessment — Revision Pack and Mock Exam

[繁體中文版 →](README.zh-Hant.md)

## What it is

Free study material for the Hong Kong Customs and Excise Department's
**Competence Assessment for Money Service Operators**, the exam a licensee's
sole proprietor, partner or director must pass. It comes as two HTML files, a
revision pack and a mock exam, both written only from the official documents.
Each is a single file that works offline, in English, 繁體中文 or both side by
side. There is nothing to install and no account to make.

The method behind both is published too, as a skill for Claude Code. Give it
another exam's documents and it builds a revision pack and a mock exam the same
way, in whatever exam format you define.

## How to use it

1. Download `mso-revision-pack.html` and `mso-ca.html` from the
   [latest release](../../releases/latest).
2. Open them in Chrome. Edge and Firefox work too.
3. Read a topic in the revision pack, then drill its module in the mock exam's
   *Practice* mode. Every question has the real paper's shape — numbered
   statements and five options naming which of them are correct — and after
   each answer every statement is marked correct or not, with the trap a false
   one sets and its source.
4. Use the *Statement drill* to judge one statement at a time, since a question
   is lost on a single misjudged statement; it keeps the ones you get wrong for
   another round. Sit full timed mocks, and use *Practice my wrong answers* on
   what you missed.

To pass you need **no more than 2 wrong in any module and at least 25/35
overall**, so one weak module fails the paper even with a high total.

Your results never leave your browser. Open the same copy of `mso-ca.html` each
time, and use *Save history to file* to back them up or move them to another
computer. For a shorter drill, add `?minutes=20` after `mso-ca.html` in the
address bar.

To build the same for another exam, copy
[`.claude/skills/exam-prep/`](.claude/skills/exam-prep/SKILL.md) into your
project's `.claude/skills/` folder, or into `~/.claude/skills/` to use it in
every project. Then ask Claude Code for a revision pack and a mock exam from
your documents, or type `/exam-prep`. It starts by asking about your sources and
your exam's format.

To build from source or cut a release, see [DEVELOPMENT.md](DEVELOPMENT.md).

## The content

The revision pack and the mock exam are written from the 23 archived official
documents in [`docs/`](docs/README.md), which also maps each module to its
sources. Every point cites its section or paragraph, so you can check it against
the source.

| File | What's inside | Organised by |
|---|---|---|
| **Revision pack**<br>`mso-revision-pack.html`<br>about 3 MB | 21 pages of tables and figures on the AMLO's Parts 1–7 and Schedules 1–4, the AML/CFT Guideline, the other C&ED guidelines, and the circulars and FAQ | Source document, with each page naming the exam modules it serves |
| **Mock exam**<br>`mso-ca.html`<br>about 1.6 MB | 338 combination questions, including 8 official samples, with bilingual explanations for every statement, drawn into 35-question, 75-minute mocks under the real pass rule | The 7 exam modules, below |
| **Skill**<br>`.claude/skills/exam-prep/SKILL.md`<br>version 2.2.0 | The method that built both, written for any exam: collecting and checking the sources, settling conflicts between them, writing the pack and the questions, checking every answer blind, and tests that stop answers being guessable. You define the exam format. | The build, phase by phase |

| Module | Questions | Revision-pack pages |
|---|---|---|
| 1 · General knowledge on AML/CFT and counter-proliferation financing | 31 | AML/CFT Guideline ch. 1, 6 and 7; AMLO Sch. 1 |
| 2 · Parts 1–7 of the AMLO | 50 | AMLO Parts 1–7 |
| 3 · Schedules to the AMLO | 42 | AMLO Sch. 1–4 |
| 4 · Guidelines promulgated by the C&ED | 50 | C&ED guidelines; AMLO Part 5 |
| 5 · Systems and controls (i): governance and strategy | 56 | AML/CFT Guideline ch. 2 and 3 |
| 6 · Systems and controls (ii): AML/CFT control areas | 69 | AMLO Sch. 2, with AML/CFT Guideline ch. 4, 10 and 11; AML/CFT Guideline ch. 2 and 5–9 |
| 7 · Systems and controls (iii): demonstrating and monitoring compliance | 40 | AML/CFT Guideline ch. 3 and 7–9 |

The pack's Circulars and FAQ page serves modules 1 and 4–7. Apart from the 8
official samples retained verbatim, the questions are
reconstructions for practice; C&ED has never released a past paper.

The [coverage audit](bank/audit/README.md) maps the archived sources to actual
question statements and tracks remaining work. Following the FATF supplement,
the previous review added 21 questions and 92 statements on responsibility boundaries,
related-person distinctions and key definitions, and replaced two defective
questions. The pack also separates chasing missing transfer information from
mitigating the risk of incomplete or meaningless information. All P1/P2 gaps in
the [specialist review](bank/audit/TERMS-AND-ROLES.md)
now have tested statements; other procedural gaps and optional P3 details remain.
The [implementation record](bank/audit/implementation.json) preserves the final
bilingual blind reviews, replacement history and coverage evidence.

The remaining 16 P1 process, condition and exception tasks are now complete,
with 18 new questions and 79 statements. Existing statements cover the
already-tested details. The [P1 follow-up](bank/audit/P1-PROCESSES.md) records
each result; other P2 and P3 tasks remain in the general backlog.

## Disclaimer

C&ED publishes no answers beyond a few sample questions, so neither file can be
guaranteed correct. Every answer has been checked against the sources, but the
documents sometimes contradict each other or are unclear. Where they do, both
files follow the reading judged most defensible, and
[`revision/CONFLICT-CALLS.md`](revision/CONFLICT-CALLS.md) records each
decision. Where anything here differs from a source, the source prevails.

This is not an official product of the Customs and Excise Department. It does
not speak for C&ED or any regulator, it does not replace the official texts, and
nothing here is legal advice.

## License

| What | License |
|---|---|
| The code, the question bank (`web/questions.json`), the revision pack (`revision/`) and the skill (`.claude/skills/exam-prep/`) | [MIT](LICENSE) |
| The bundled fonts, DM Sans and DM Mono | [SIL OFL 1.1](web/fonts/OFL.txt) |
| The official documents in `docs/` | Not licensed here: they are Hong Kong SAR Government publications, included for study reference only |

[LICENSE-CONTENT.md](LICENSE-CONTENT.md) has the detail.
