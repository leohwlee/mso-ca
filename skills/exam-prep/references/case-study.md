# Case study: how the method was learnt

The rules in this skill come from one project,
[leohwlee/mso-ca](https://github.com/leohwlee/mso-ca): a bilingual (English and
Traditional Chinese) question bank, mock-exam app and seven-part study notes for
the Hong Kong Customs and Excise Department's Competence Assessment for Money
Service Operators, written from official documents. Between 1 September and 24
October 2026 it went through 166 commits and 43 releases. Almost every rule was
added after a review found the fault in real items, so the order in which the
faults surfaced is itself the lesson: each one found late cost a sweep of
everything already written.

The numbers are that project's measurements. They are evidence for a rule, not
constants for yours.

## Timeline

| When | Release | What happened | What it taught |
|---|---|---|---|
| 1–2 Sep | v1.0 | An app and 140 bilingual questions in two days; a single offline HTML file; local history with export | Ship the delivery format early; candidates use what opens offline |
| 3 Sep | v1.1 | 20 questions per section was too thin: candidates began recognising items. Grew to 1,510, each section sized to its source volume | Size the bank to the draw and the material, not to a round number |
| 5–6 Sep | v1.2 | A repair against the official documents rewrote 1,354 questions; a re-verification found 16 more, a second review 187. Seven second answers came from one habit: drawing every option from the list the stem asked about | Generated items carry errors; verify blind against the source; re-verify after every bulk rewrite |
| 6 Sep | v1.3 | The README had said the examiner published no samples. It had published eight, every one a combination item, and twelve examinable circulars were missing | Find the official format and the full examinable scope *before* writing |
| 6 Sep | v1.3.1–2 | Duplicates that the stem test could not see: the same fact asked in different words in different sections | Compare cited passage and answer, across sections, not just stems |
| 6–7 Sep | v1.4–1.5 | A realistic-paper switch; then the tells: keys longest (1,241 of 1,510), standout options, absolutes marking false statements (true 32% of the time against 76%), semicolons marking keys. 550, then 637, then 149 items rewritten | Measure the bank as a test-wise candidate would; make distractors wrong on substance |
| 7 Sep | v1.5.5–7 | The absolutes rewrite left two regressions: per-language rewriting split 29 items into two exams, and 23 explanations still rebutted words that were gone | Edit every language together; re-aim every explanation a rewrite disturbs |
| 7 Sep | skill 1.0 | The method written up as a skill | Write the reasoning down while it is fresh |
| 21 Sep | v1.5.9 | A candidate met "What is the relationship between section 3(1)(a) and section 3(2)?" — 44 items made a number the unknown | Ask about the rule, not the section number |
| 22–25 Sep | v1.5.10–1.6 | Items on rules that did not govern the candidate; 49 citing superseded circulars; each language not following its own text; Chinese terms and modal verbs swept three times (169, 662, 533) | Decide scope, currency, language policy and terminology first |
| 25–28 Sep | v1.6.2–1.7 | 95 source conflicts found after 1,500 items existed; the owner decided all of them on one page in two days; the bank and the pack re-applied the decisions | Sweep conflicts before writing; one-minute decisions with a recommendation |
| 28 Sep | v1.7.4–5, skill 2.0–2.2 | Every statement got a stored deciding quote checked against the sources; a re-read found 573 of 3,094 stopped short of the deciding words; an options-only guesser became a test | Capture the quote with the item; calibrate a filter and a cheaper reviewer on a judged sample |
| Oct | — | The owners sat the real paper. It was far harder than the bank: four to six statements, anywhere from none to all true, option sets varying per item, distractors one word from the source | Calibrate realism with someone who sat the exam; official samples can understate it |
| 16–18 Oct | v1.8–1.9, skill 2.3 | The whole bank rebuilt in the real format: combination items only, strict reading, a named trap per false statement, statements reshuffled per draw. A source-first coverage audit (functions, roles, definitions, conditions). Scope narrowed to the owner's 26 priority documents and about 525 items; two app modes only | Realism beats volume; coverage is audited from the sources; the owner prunes, and the product gets simpler |
| 19–20 Oct | v1.10 | Study notes rewritten source-first in the exam's seven parts, with three language views; figures reviewed one by one (a forced decision tree replaced by overlapping cases); independent audits; checked at five widths in three languages | Notes come from sources, never from the bank; draw the relationship the source states |
| 22–23 Oct | v1.11–1.13 | Study tiers, traps beside the rules, list cards with counts, a numbers page, ruling marks hidden by default, a tier filter, a wrong-answer book, unseen-first practice; 63 gap and trap items; a 60-fact quick sheet tried and removed | Structural aids that change how content is read beat another layer of prose |
| 23 Oct | v1.13.0 | A 36-item batch needed four blind-review rounds because style checks ran only after the first | Run every mechanical check before building review packets |
| 24 Oct | v1.13.1–4 | Dead test branches, duplicate helpers and unused styles removed with byte-identical output; a timer test that failed at random traced to two clock readings | Simplify once the content is stable, proving nothing visible moved |

## The costs of deciding late

| Rule settled late | Items swept |
|---|---|
| Option length (three rules) | 1,194, then 442, then 637 |
| Terminology in one language | 169, then 662, then 533 |
| Source conflicts | 29, then 93 |
| Superseded sources | 49 |
| Clause numbers as the unknown | 52 |
| Each language follows its own text | 47 |
| Out-of-scope rules | 27 |
| The real exam's format | the whole bank |

## Measurements worth remembering

- "Pick the longest" passed 64% of simulated papers before the length rules.
- An option standing out short was the key 47% of the time; one standing out long
  in English was the key 1 time in 55 (a reverse tell).
- Hedged options ("reasonable", "appropriate") were the key 71% of the time in
  English and 62% in Chinese.
- After the first review, about 7,000 further blind answers found no wrong key but
  about 40 second defensible answers.
- A learnt surface-feature guesser picked 32% of combination keys in English and
  39% in Chinese against 20% for chance, through tells the owner chose to keep,
  and passed about one simulated paper in 2,500.
- A quote filter skipped 57% of 2,862 quotes with no missed defect in a judged
  sample of 120; a cheaper model caught 24 of 24 defects, a smaller one 18.
- Three guards silently checked one language only; one section reached 54%
  key-is-longest on a green build.

## What the owner kept and removed

Kept and asked for: study tiers; traps tied to conflict rulings; list cards with
counts; a numbers page; ruling marks hidden by default; a tier filter; a
wrong-answer book that clears an item after two correct answers in a row;
practice that draws unseen items first; two app modes (mock and custom
practice).

Removed after trying: a per-part 60-fact quick sheet; a statement-by-statement
drill; hidden-answer study modes; oversized controls; a print button; a search
box; sample metadata; an introductory scope panel; a closing source summary; a
mock-exam score reminder; a standalone HTML download beside the bundle.
