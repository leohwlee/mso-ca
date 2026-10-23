# MSO Competence Assessment — Study and Practice

[繁體中文](README.zh-Hant.md) · [Download the study bundle](https://github.com/leohwlee/mso-ca/releases/latest/download/mso-study-bundle.zip) · [Practice app](https://github.com/leohwlee/mso-ca/releases/latest/download/mso-ca.html) · [Release notes](CHANGELOG.md)

**Seven-part study notes and 552 combination questions** for the Hong Kong Money
Service Operator Competence Assessment. Read and practise offline in Traditional
Chinese, English or both languages. The selected sources are documents **01–26**
of the [reading library](docs/README.md); practice offers mock exam and custom practice.

## Start here

For notes **and** practice, download **[mso-study-bundle.zip](https://github.com/leohwlee/mso-ca/releases/latest/download/mso-study-bundle.zip)**,
extract the whole archive and open `index.html`. It includes the seven-part notes,
practice app and the cited 01–26 originals. Keep the folders together so study,
practice and source links work offline. The standalone file below provides practice;
its study-note links require the complete bundle.

1. Download **[mso-ca.html](https://github.com/leohwlee/mso-ca/releases/latest/download/mso-ca.html)** from the latest release.
2. Open the downloaded file in a browser. No installation, account or server is needed.
3. Choose **EN**, **中文** or **EN+中**, then start a mock exam or select parts for practice.

The HTML file contains the app, question bank and fonts. You do not need to
download the repository or install Go to use it. The official source documents
are available separately in the reading library.

![Current blue-gray practice homepage with mock exam and custom practice](docs/images/app-v1.10.1-en.png)

*Practice homepage, English. Captured from the v1.10.1 app on 20 October 2026.*

[v1.11.0](CHANGELOG.md) adds 27 reviewed questions, ten of them with no true statement, and exam-focus aids in the notes: study tiers, 69 exam traps and new figures. The previews below were captured in v1.10.1.

## Updated study notes in v1.10.1

The seven-part notes now contain 75 topics and 621 bilingual point pairs, with
more complete definitions, lists, conditions and exceptions from the High-priority
originals. All 33 visuals were reviewed: the CDD trigger map now shows cases that
can overlap; two decision trees remain where branches are appropriate. Narrow
screens, table headings and language-switch positioning have also been improved.

Read the [content review](revision/study-notes/depth-review-2026-10-20/REPORT.md),
[visual review and previews](revision/study-notes/visual-refinement-2026-10-20/REPORT.md)
for checked ranges and remaining limits. Counts are not coverage percentages.
That update left the 525 questions, answers and scoring unchanged.

![Part 6 study notes showing when customer due diligence is required, with conditions and source citations](docs/images/study-v1.10.1-en.png)

*Part 6 reading example, English. Captured from the v1.10.1 notes on 20 October 2026; the CDD cases can overlap.*

## Choose how to practise

| Mode | What happens |
|---|---|
| **Mock exam** | 35 random questions, five from each of seven parts, with a 75-minute timer. Submit to see your score, explanations and sources. |
| **Custom practice** | Select one or more Parts 1–7. Work without a timer and see explanations after each answer. |

A mock exam passes only with **at least 25/35 overall and no more than two
wrong in any part**. A score of 32/35 can still fail if all three mistakes are
in one part. The larger sections of the practice bank do not receive more
questions in a mock exam.

Each question has four to six statements and five combination options.
Statements and their option references are reordered together at each draw.
Distractors test conditions, actors, deadlines, thresholds and exceptions;
each statement has its own explanation.

## Review results

Expand **Mock exam results and history** to review completed attempts.
Results are stored locally in the browser.

[Full user guide and troubleshooting](docs/USAGE.md)

## What the bank covers

| Part | Topic | Questions |
|---|---|---:|
| 1 | General AML/CFT and counter-proliferation financing | 63 |
| 2 | AMLO Parts 1–7 | 75 |
| 3 | AMLO Schedules | 66 |
| 4 | C&ED guidelines | 83 |
| 5 | Governance and strategy | 81 |
| 6 | AML/CFT control areas | 116 |
| 7 | Demonstrating and monitoring compliance | 68 |
| **Total** | | **552** |

The bank includes eight official sample questions. The remaining questions are
authored practice material, not released past papers. See [release notes](CHANGELOG.md)
for earlier changes to the bank.

- **01–26:** the only approved sources for active questions. External documents linked by a circular are not automatically included.
- **27–47:** preserved historical reference, excluded from the active bank.
- **Document 24:** English original only; related Chinese questions are labelled **study translations** and retain English deciding quotations.
- **Document 25:** findings are explicitly attributed to the **2022** risk report, not presented as a live risk assessment.

[Source-by-source accounting](docs/QUESTION-SOURCES.md) · [Current review evidence](bank/audit/ACTIVE-SCOPE.md)

## Documentation and maintenance

- **Seven-part study notes:** Included in the study bundle from v1.10.0. [Source and reading pages](revision/study-notes/index.html) contain concepts, definitions, conditions and exceptions from originals 01–26, with actual filename citations. The bank is used only to check omissions. See [scope and maintenance](revision/study-notes/README.md).
- **Study:** [User guide](docs/USAGE.md) and [26-document reading order](docs/README.md).
- **Build and check:** [Development guide](DEVELOPMENT.md).
- **Write or review questions:** [Question format](bank/FORMAT.md), [source maintenance](docs/SOURCE-MAINTENANCE.md) and [agent-neutral authoring workflow](docs/authoring/exam-prep/GUIDE.md).
- **Find other documentation:** [Documentation index](docs/INDEX.md).

Any human or coding agent can begin with [AGENTS.md](AGENTS.md). No particular
agent, plugin or proprietary command is required. Historical reviews remain
verifiable without being presented as reviews of later changes.

The previously released `mso-revision-pack.html` is a **legacy reference
pack with its own older scope**. It is not a third app mode or a complete guide
to the current bank; it is no longer built or included in new releases; see the [archive](revision/README.md).

## Limits and licensing

This is a personal study scope, not the official exam syllabus or a guarantee
of complete coverage. Source checks and independent review reduce errors but
do not guarantee every answer. Refer to original publications and the
[recorded source-conflict decisions](revision/CONFLICT-CALLS.md).
This is not an official C&ED product or legal advice.

Original code and authored material use the [MIT licence](LICENSE). Fonts use
[SIL OFL](web/fonts/OFL.txt). Official publications, sample wording and quotations
retain their publishers' rights; see [content licensing](LICENSE-CONTENT.md).
