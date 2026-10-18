# Working on MSO sources and questions

- This repository is agent-neutral. Start with this file and
  [the authoring workflow](docs/authoring/exam-prep/GUIDE.md); no agent-specific
  configuration or command is required.
- The owner's active exam scope is ONLY documents 01–26, with approximately
  525 bilingual questions across the existing seven parts. The app has two
  modes: mock exam and custom practice (one or multiple parts).
- Before editing questions, revision content, sources or reading order, read
  [source maintenance](docs/SOURCE-MAINTENANCE.md),
  [question format](bank/FORMAT.md) and the applicable authoring guide.
- Use ONE document number: the reading order in `docs/catalog.json` is also the
  filename prefix, quote `doc`, extracted-text filename and transcript filename.
  `03` is the AML/CFT Guideline; `04` is Cap. 615. Do not add a second source ID.
- The catalog has one flat sequence of 47 publications. Daily reading is 01-26:
  01-09 High, 10-19 Medium Essential, 20-26 Medium Selected. Reference material
  continues as 27-47 under docs/archive. The original coverage audits remain historical evidence for the
  original 23, marked `original_bank_source`. Current coverage is recorded in
  `bank/audit/active26-implementation.json`. Verify edition,
  language, content and citation mapping before using an addition in questions.
  Reading pointers and statutory extracts are not complete source publications.
- Every companion has its own document number. Cap. 34 is 17 after circular 16;
  Cap. 629 is 23 after circular 22. `parent_document` records that relationship.
  Bilingual originals are copied into TC and EN, with identical raw hashes.
  Resolve every source through `editions.path`; text uses text/LANG/NN.txt.
  The periodic-return circular and transcript are 15. The owner has approved 01–26 for questions; verify edition, language
  and citation recognition for each actual use. Document 24 has no official
  Chinese version: TC questions are labelled study translations and their
  deciding quotes retain the English source with `language: "en"`. No runtime old-ID mapping is maintained.
- Preserve question IDs and historical evidence. If reading order changes,
  migrate all document references together and verify the migration. Keep prior
  evidence as history; do not replace hashes merely to silence failures.
- Run `python docs/build_catalog.py --check` and `go test ./...` for source changes.
  For question or evidence changes also run the four audit checks in
  `DEVELOPMENT.md`, `python bank/audit/active_scope.py --check`,
  `python bank/audit/render_active_scope.py --check`, and `node --test tests/*.test.cjs`.
  Build the exam HTML when generation may be affected. The old revision pack is archived.

- Use [the documentation index](docs/INDEX.md) for user and maintainer entry points.
  Keep English and Traditional Chinese instructions consistent.
- Run `python -m unittest discover -s tests -p "*_test.py"` with question/evidence checks.
  Follow [Development](DEVELOPMENT.md) for the complete verification and release procedure.
