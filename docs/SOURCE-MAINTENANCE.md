# Maintaining the source documents

[繁體中文版 →](SOURCE-MAINTENANCE.zh-Hant.md)

## One publication, one document number

The reading directory, filename prefix, quote `doc`, extracted text and transcript
use the same two-digit number. `catalog.json` is one flat sequence:

- 01-09: High.
- 10-19: Medium Essential.
- 20-26: Medium Selected.
- 27-47: reference archive, continuing the same sequence.

Companions have their own numbers. **17** is the full Cap. 34 after circular **16**;
**23** is the full Cap. 629 after circular **22**. `parent_document` records their
relationship, not another source ID. The AML/CFT Guideline is **03**, Cap. 615 **04**,
and the periodic-return circular and its image transcript **15**. There are no
gaps or runtime old-number aliases.

## Sources and text

Resolve originals through each edition's `path`, relative to `docs/`. Daily files
are directly in `TC/` and `EN/`; references are in `archive/LANG/`. Every edition
has `text_file: text/LANG/NN.txt` and a text hash. BI means bilingual, ZH official
Simplified Chinese. Item **24** puts the English original in both reading folders,
explicitly labelled in TC; it is not a Chinese translation. The bilingual laws
have identical raw PDF bytes in both folders.

PDF, DOCX and HTML hashes preserve raw bytes; Markdown hashes fold CRLF to LF.
`extract_text.py` handles all 47 publications. `text_mode: companion` retains the
previous companion extraction rules, preserving unchanged source text.
`extract_related.py` remains a compatibility entry point for the same process.
Image labels in `transcripts/15.json` stay bound to their exact source PDFs.

The original 23 bank sources are marked `original_bank_source`. Other publications,
including the two full laws, are reading aids: numbering does not approve them
for questions. Verify edition, language, scope and citation patterns in
`sources_test.go` before extending bank coverage. Archived bank sources remain
available for quote and evidence checks.

## Changing sources or order

After replacing a source, update its raw hash, regenerate text and review affected
quotes and image transcripts. `build_catalog.py` generates all four directories.
`reading_status`, `study_focus` and bilingual `archive_reason` record the selection.

If order changes, migrate filenames, catalog numbers, text, manifest, quotes,
transcripts, citation patterns, reports and examples together. Preserve question
IDs, wording, truth values, options, answers and saved-answer compatibility.
Prior evidence stays in immutable ZIP snapshots under `bank/audit/history/`.
First reconstruct each prior quote version and match its recorded hash; only then
derive its renumbered hash. Never replace hashes merely to silence failures.
Compressed prior text snapshots are checked against their archive and current
successor. Historical mappings are evidence only, not authoring lookups.

## Checks

```bash
python docs/extract_text.py
python docs/build_catalog.py --check
go test ./...
python bank/audit/report.py --check
python bank/audit/terms_report.py --check
python bank/audit/p1_report.py --check
python bank/audit/remaining_report.py --check
go run . -export-html dist/mso-ca.html
python revision/pack_build.py dist/mso-revision-pack.html
```

The mock exam stores progress by question ID. Document renumbering does not change
question IDs or saved answers. See [historical evidence](../bank/audit/history/README.md).
