# User guide

[繁體中文](USAGE.zh-Hant.md) · [Project home](../README.md) · [Documentation index](INDEX.md)

## Download and open

Download **mso-study-bundle.zip** from the
[latest release](https://github.com/leohwlee/mso-ca/releases/latest). Choose that
asset, rather than GitHub's source-code ZIP. Extract everything and open
`index.html` in a browser. Keep the folder structure: the bundle contains the
seven-part notes, the practice app (`dist/mso-ca.html`) and the cited 01–26
originals, and their links work offline only when kept together.

Choose English, Traditional Chinese or the combined view using the language
buttons. Language and light/dark appearance can be changed while using the app.

## Mock exam

Select **Start mock exam**. Each paper has 35 questions: five per part, with
75 minutes in total. Choose the option identifying all the correct statements,
move between questions and flag those you want to revisit. Submit when ready;
the timer also ends an expired paper. A closed tab does not pause the deadline.

Pass requires at least 25 correct answers overall **and** at least three correct
in each part. Unanswered questions are incorrect. Results provide the recorded
score, per-part performance, explanations and source citations.

You can resume a valid unfinished paper in the same browser storage. If a
question-bank update retires one of its questions, the app asks you to start a
new complete paper instead of resuming a shortened one.

## Custom practice

Select one or more **Part 1–7** buttons on the home page, or select **All**.
At least one part remains selected. Select **Start practice** to draw questions
only from that selection. Practice is untimed. After each answer, inspect the
verdict and explanation for every statement, then move to the next question.
The selected pool is shuffled and cycles again after every question has been seen.

Statements can appear in a different order on another attempt. Learn the rule
and its conditions, rather than an option letter or statement number.

## Back up and restore results

1. Expand **Mock exam results and history** on the home page.
2. Select **Save history to file (.md)** and keep the downloaded file.
3. In the new browser or app copy, select **Load history from file** and choose that backup.

The backup includes readable results and the data the app needs to import them.
It is not a backup of an unfinished exam. Practice sessions do not produce
completed mock-exam records.

Browser storage can differ between file paths, browsers and devices. Private
browsing or clearing site data may discard it. Export before upgrading or moving
the extracted bundle. Historical scores remain as originally recorded; explanations
for questions removed from the current bank may no longer be available.

## Sources and question interpretation

The app uses only local documents 01–26. Each answer includes a source locator
(a section, paragraph or page) and per-statement explanation. Read the
[source directory](README.md) for the actual editions and the
[source mapping](QUESTION-SOURCES.md) for the bank's scope.

Document 24 has no official Chinese edition: its Chinese practice text is
labelled a study translation. Document 25 findings refer to the 2022 report.
The separate legacy revision pack has an older scope and is not the source of
truth for the current question bank.

## Troubleshooting

| Problem | What to do |
|---|---|
| A page shows code or a GitHub file listing | Download the release asset `mso-study-bundle.zip`, extract it and open `index.html` in a browser. |
| Opening `web/index.html` directly does not load questions | Use the practice app in the release bundle. Developers can serve `web/` as described in the development guide. |
| An older count appears | Download the latest bundle again; an extracted copy does not update itself. |
| History appears empty after an upgrade | Load your exported history file; the new path or browser may use different storage. |
| A high total score still fails | Check the per-part rule: three wrong in any one part means failure. |
| A statement seems ambiguous | Check the cited local edition and the explanation. Report the question ID, language and deciding passage, without personal customer information. |

For builds and maintenance, see the [development guide](../DEVELOPMENT.md).
