# MSO Competence Assessment — Revision Pack and Mock Exam

[繁體中文版 →](README.zh-Hant.md)

## What it is

Free study material for the Hong Kong Customs and Excise Department's
**Competence Assessment for Money Service Operators**, the exam a licensee's
sole proprietor, partner or director must pass. It comes as two HTML files, a
revision pack and a mock exam, both written only from the official documents.
Each is a single file that works offline, in English, 繁體中文 or both side by
side. There is nothing to install and no account to make.

## How to use it

1. Download `mso-revision-pack.html` and `mso-ca.html` from the
   [latest release](../../releases/latest).
2. Open them in Chrome. Edge and Firefox work too.
3. Read a topic in the revision pack, then drill its module in the mock exam's
   *Practice* mode, where every answer shows its explanation and source.
4. Sit full timed mocks, and use *Practice my wrong answers* on what you missed.
   Near exam day, tick *Exam-realistic paper* for a paper in the combination
   format C&ED prints.

To pass you need **no more than 2 wrong in any module and at least 25/35
overall**, so one weak module fails the paper even with a high total.

Your results never leave your browser. Open the same copy of `mso-ca.html` each
time, and use *Save history to file* to back them up or move them to another
computer. For a shorter drill, add `?minutes=20` after `mso-ca.html` in the
address bar.

To build from source or cut a release, see [DEVELOPMENT.md](DEVELOPMENT.md).

## The content

Both are written from the 23 current official documents in
[`docs/`](docs/README.md), which also maps each module to its sources. Every
point cites its section or paragraph, so you can check it against the source.

| File | What's inside | Organised by |
|---|---|---|
| **Revision pack**<br>`mso-revision-pack.html`<br>about 3 MB | 21 pages of tables and figures on the AMLO's Parts 1–7 and Schedules 1–4, the AML/CFT Guideline, the other C&ED guidelines, and the circulars and FAQ | Source document, with each page naming the exam modules it serves |
| **Mock exam**<br>`mso-ca.html`<br>about 4 MB | 1,594 questions with explanations (1,242 with four options, 352 in the combination format), drawn into 35-question, 75-minute mocks under the real pass rule | The 7 exam modules, below |

| Module | Questions | Revision-pack pages |
|---|---|---|
| 1 · General knowledge on AML/CFT and counter-proliferation financing | 126 | AML/CFT Guideline ch. 1, 6 and 7; AMLO Sch. 1 |
| 2 · Parts 1–7 of the AMLO | 308 | AMLO Parts 1–7 |
| 3 · Schedules to the AMLO | 260 | AMLO Sch. 1–4 |
| 4 · Guidelines promulgated by the C&ED | 310 | C&ED guidelines; AMLO Part 5 |
| 5 · Systems and controls (i): governance and strategy | 96 | AML/CFT Guideline ch. 2 and 3 |
| 6 · Systems and controls (ii): AML/CFT control areas | 340 | AMLO Sch. 2, with AML/CFT Guideline ch. 4, 10 and 11; AML/CFT Guideline ch. 2 and 5–9 |
| 7 · Systems and controls (iii): demonstrating and monitoring compliance | 154 | AML/CFT Guideline ch. 3 and 7–9 |

The pack's Circulars and FAQ page serves modules 1 and 4–7. The questions are
reconstructions for practice, not real exam questions; C&ED has never released a
past paper.

## License

| What | License |
|---|---|
| The code, the question bank (`web/questions.json`) and the revision pack (`revision/`) | [MIT](LICENSE) |
| The bundled fonts, DM Sans and DM Mono | [SIL OFL 1.1](web/fonts/OFL.txt) |
| The official documents in `docs/` | Not licensed here: they are Hong Kong SAR Government publications, included for study reference only |

[LICENSE-CONTENT.md](LICENSE-CONTENT.md) has the detail. This is not an official
product of the Customs and Excise Department, and nothing here is legal advice.
