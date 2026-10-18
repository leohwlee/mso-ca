# Historical audit evidence

The 18 October 2026 cleanup makes the reading-directory number the only document
ID. Active quotes, text files, transcripts and audit references use it directly.
No old-ID or old-filename lookup is used by the application or audit tools.

`2026-10-18-before-document-number-cleanup.zip` preserves 103 exact pre-cleanup
files, including the original audit records, source catalog, quote snapshots,
text and previous reorganisation evidence. It is immutable historical evidence,
not an input for authoring or a numbering system to maintain. Historical
`before_text` snapshots embedded in active audit records are also kept verbatim.

`2026-10-18-document-number-cleanup.json` records the archive hash, invariants and
derived quote/file hashes. Each original quote baseline was reconstructed and
matched to its recorded hash before deriving its renumbered equivalent. Source
bytes, extracted text, transcript and the entire question bank were checked
unchanged; the only quote changes are document numbers. Review verdicts, question
IDs, retired questions, truth values and historical question hashes are retained.
The usual audit validators continue reconstructing and checking preceding waves
with the unified document numbers; no hash check was disabled.

The subsequent continuous-numbering cleanup is preserved in
`2026-10-18-before-continuous-numbering.zip`. The current register is flat:
01–26 daily reading, including separately numbered companion laws 17 and 23;
27–47 reference publications. The maintenance record
`../maintenance/2026-10-18-zz-continuous-numbering.json` records file moves,
reconstructed quote hashes and unchanged-content checks. The pre-renumbering
download review remains verbatim in
`2026-10-18-download-review-before-continuous-numbering.json`.
