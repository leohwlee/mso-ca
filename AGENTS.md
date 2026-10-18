# Working on MSO sources and questions

- Before editing questions, revision content, sources or reading order, read
  [source maintenance](docs/SOURCE-MAINTENANCE.md),
  [question format](bank/FORMAT.md) and the applicable authoring guide.
- Use ONE document number: the reading order in `docs/catalog.json` is also the
  filename prefix, quote `doc`, extracted-text filename and transcript filename.
  `03` is the AML/CFT Guideline; `04` is Cap. 615. Do not add a second source ID.
- The catalog has one flat sequence of 47 publications. Daily reading is 01-26:
  01-09 High, 10-19 Medium Essential, 20-26 Medium Selected. Reference material
  continues as 27-47 under docs/archive. The bank and coverage audits cover the
  original 23, marked `original_bank_source` in the catalog. Verify edition,
  language, content and citation mapping before using an addition in questions.
  Reading pointers and statutory extracts are not complete source publications.
- Every companion has its own document number. Cap. 34 is 17 after circular 16;
  Cap. 629 is 23 after circular 22. `parent_document` records that relationship.
  Bilingual originals are copied into TC and EN, with identical raw hashes.
  Resolve every source through `editions.path`; text uses text/LANG/NN.txt.
  The periodic-return circular and transcript are 15. Numbering alone does not
  make a companion an approved question-bank source; verify edition, language
  and citation recognition first. No runtime old-ID mapping is maintained.
- Preserve question IDs and historical evidence. If reading order changes,
  migrate all document references together and verify the migration. Keep prior
  evidence as history; do not replace hashes merely to silence failures.
- Run `python docs/build_catalog.py --check` and `go test ./...` for source changes.
  For question or evidence changes also run the four audit checks in
  `DEVELOPMENT.md`. Build both HTML outputs when generation may be affected.
