# MSO competence assessment preparation

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Leo is preparing for the MSO Competence Assessment and uses Traditional Chinese
and English study material and practice questions.

## Product Purpose

Organize preparation around the examination's seven parts. Explain concepts,
definitions, requirements, conditions and exceptions directly from the approved
original sources, with useful visualizations and traceable repository citations.
Keep question practice available as a separate activity.

## Operating Context

The repository contains a local/offline exam application and a seven-part reading
reference. The primary reading entry is `revision/study-notes/index.html`, with
individual pages `part-1.html` through `part-7.html`. The earlier Part 6 sample is
retained as historical authored material, not the primary seven-part entry or the
current manuscript source.

The user selected B, the blue annotated study reference, for reading and practice
on 19 October 2026. The current content rewrite preserves that visual world while
replacing bank-derived explanations with source-first manuscripts.

## Capabilities and Constraints

- Preserve the existing mock-exam and custom-practice workflows, including
  selection of one or multiple examination parts.
- Preserve question IDs, question/answer content, historical evidence and saved
  results. A visual redesign does not authorize changing exam content or scoring.
- Active exam source scope is documents 01–26. Resolve original editions through
  `docs/catalog.json`. Study citations must display actual repository filenames
  and useful paragraph/section locators, not only publication titles.
- Author reading content from source passages into concepts, definitions,
  requirements, conditions and exceptions. Keep qualifying conditions beside the
  requirement they limit. Do not organize reading pages around question stems,
  answer options, question IDs or a ledger of correct/incorrect statements.
- The reading builder consumes the seven source-authored manuscripts and the
  catalog; it does not read the question bank. Use the bank only in a separate
  gap check after authoring, not as the source of reading copy or page structure.
- Preserve Chinese and English content, including a combined bilingual reading
  view. Document 24's Chinese study translations retain the English
  original as their source.
- Preserve offline reading and practice. Use the existing implementation and
  local assets; a new framework or hosted service is not a requirement.
- Keep study-note content visible. The owner removed hidden-answer study modes,
  oversized controls, the print button, search area, sample metadata, introductory
  scope panel and the final source-summary section. Do not restore them as design
  decoration. Existing quiz answering remains part of the practice application.
- Visualizations should clarify real relationships and sequences. Do not impose
  a decision-flow response pattern on material that is clearer as a comparison.

## Brand Commitments

The reading-page brand text is `MSO Competence Assessment Study Note`.
The examination's actual part titles, rather than promotional slogans, identify
the study material. The user has requested a replacement visual design and has
selected option B, the blue annotated study reference, for all seven reading parts and the existing practice/exam interface.

## Evidence on Hand

- `revision/study-notes/part1.py` through `part7.py`: current source-authored
  bilingual manuscripts organized by topic and concept.
- `revision/study-notes/build.py`: reading-page generator and source/citation
  checks; it does not consume the bank.
- `revision/study-notes/coverage.json`: current manuscript sections, source
  references and source-text hashes; not a claim of complete official-syllabus
  coverage or independent semantic review.
- `revision/study-notes/gap_check.py`: separate bank comparison for gaps after
  source-led authoring; it does not supply page content.
- `revision/part6-sample/`: historical authored sample and its own review evidence.
- `web/questions.json`, `web/app.js`, `web/style.css`: existing questions and app.
- `bank/FORMAT.md` and `docs/authoring/exam-prep/GUIDE.md`: authoring constraints.
- `docs/catalog.json`: source identities and original edition paths.

## Product Principles

- Help the learner understand and distinguish conditions, exceptions and similar
  rules before or alongside practice.
- Let source concepts determine the reading structure; keep practice questions
  and post-authoring gap checks separate from the reading explanation.
- Make original evidence easy to find by the repository's own filenames.
- Use a coherent experience across the seven parts, languages and reading/practice.
- Keep visual decisions separate from source authority and question correctness.

## Open Decisions

The B visual direction is confirmed; the current rewrite changes reading content
architecture. Reading and practice link by Part and retain the chosen language.
No new learning-progress claims, analytics, account service or gamification
features have been requested. Verification of the current manuscripts is recorded
separately from earlier visual or sample reviews.
