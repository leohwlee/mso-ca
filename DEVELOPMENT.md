# Development

[Documentation index](docs/INDEX.md) · [User guide](docs/USAGE.md) · [Question format](bank/FORMAT.md)

[繁體中文版 →](DEVELOPMENT.zh-Hant.md)

## Build and verify

To use the app, [download the HTML](https://github.com/leohwlee/mso-ca/releases/latest/download/mso-ca.html); no development tools are needed.
For maintenance, install Go 1.27 or later, Node.js 22 or later, and Python 3.10 or later.
Run the following from the repository root. They match the CI and release checks.
Python tools use the standard library except source re-extraction, which additionally needs PyMuPDF.
On Windows, use `py -3` if `python` opens the Microsoft Store; add `-X utf8` if the terminal cannot print Chinese.

```bash
go vet ./...
go test ./...
node --test tests/*.test.cjs
python -m unittest discover -s tests -p '*_test.py'
python docs/build_catalog.py --check
python bank/audit/active_scope.py --check
python bank/audit/render_active_scope.py --check
python bank/audit/report.py --check
python bank/audit/terms_report.py --check
python bank/audit/p1_report.py --check
python bank/audit/remaining_report.py --check
go run . -export-html dist/mso-ca.html
python revision/pack_build.py dist/mso-revision-pack.html
```

Open `dist/mso-ca.html` for the release build. For development, run
`python -m http.server 8321 --bind 127.0.0.1 -d web` and visit
`http://127.0.0.1:8321`. The app needs no backend or API keys.
The separately built revision pack retains older source coverage; it is not a third app mode.

## App and question checks

The bank is `web/questions.json`. Every item has the shape of the real paper: a
stem, four to six numbered statements, which of them are true, and five options
naming sets of them. [`bank/FORMAT.md`](bank/FORMAT.md) records the owner's
decisions about that shape and the rules items are written to; the app shuffles
the statements at every draw and renumbers the options to match.

`go test ./...` is more than a shape check: it guards the faults that quietly
ruin a question bank. Most of the checks were added after a review found the
fault in real questions.

| Check | What it stops |
|---|---|
| Per-module counts; 4 to 6 statements in both languages; five options in display order; exactly one option matching the true statements, and it is the key | items going missing, half-written or mis-keyed |
| Option sets are symmetric: any option the size of the key can be renumbered into it | reading the key off the shape of the option set |
| A note per statement and a trap code per false statement on every item the app reorders | an explanation pointing at the wrong statement once the order changes |
| The number of true statements varies across the bank | learning to hunt for the one false statement |
| No kind of trap dominates | learning to check for one kind of defect only |
| Statement length spread and standout | a false statement given away by being the longest or shortest |
| Statements carrying an absolute or a negation are true at a healthy rate | "mark the absolutes false" |
| Citation has a locator; stems name the topic, never a section number | citing a document with no paragraph to turn to; asking what a number says |
| Statutory Chinese terms | wording the official Chinese editions never use |
| Chinese 該 points back to something already named | "the customer" or "the MSO" rendered word for word as 該客戶 or 該經營者, with nothing before it to refer to |
| Guideline paragraphs are 段 in Chinese | a Guideline paragraph called 款, the Ordinance's word for a subsection |
| ML/TF pairing | dropping the terrorist-financing half in Chinese |
| No false statement turns on "Joint Financial Investigation Unit" | keying false the name C&ED's own sample keys true (register B21) |
| No positional references | "statement 2" or "option B" in a note, when statements and options are reordered |
| No duplicate items, no statement made twice | one point asked twice, or a twin that tells a candidate which to doubt |
| Every statement stores its deciding quote, found word for word in a document the item cites | a statement the cited passage does not decide; a document replaced without its text being extracted again |
| C&ED's own samples carry C&ED's words | "official" on a paraphrase |
| Circulars cited are current | a circular that a later document has overtaken coming back |
| Strategies that read only the option set find the key no more often than chance | the most convergent, most popular, largest or last option pointing at the key |
| A guesser that sees only the statements and options, trained on the bank itself | a new surface tell: it may pick at most 45% of keys (chance 20%) and pass at most 0.5% of simulated papers |
| Each language's fields hold that language only | "the Chinese text says…", or an English abbreviation no Chinese source prints |

The quote check reads `docs/text/`, the extracted text of every document in
`docs/EN` and `docs/TC`, and `docs/quotes.json`, which holds the deciding quotes
per question and language. After adding or replacing a document, run
`python docs/extract_text.py` (it needs PyMuPDF). The check then lists every
quote that the new edition no longer supports.

### Writing items

Before editing sources or questions, read [source maintenance](docs/SOURCE-MAINTENANCE.md).
The reading-order number is the only document ID: `EN 03`, filename prefix 03
and quote `"doc": "03"` all mean the AML/CFT Guideline. Filenames and official
sources and current locations are recorded in `docs/catalog.json` (`editions.path`).
The daily folders hold 26 publications; archived sources remain under `docs/archive`
with numbers 27–47; the daily set is continuously numbered 01–26, including
companions. All 47 publications share one sequence. The active question bank is restricted to 01–26. The original 23-source
coverage reports are preserved as historical evidence; current review and
coverage live in `bank/audit/active26-implementation.json`. Run `python docs/build_catalog.py --check`
after source metadata or filename changes.

Items are written as patches and checked before they reach the bank, with the
tools in [`bank/`](bank/) (Python 3, standard library only):

```bash
python bank/find.py EN 03 "target market"        # a passage in a source, with page and context
python bank/apply.py next 3 15                   # the next unused ids in module 3
python bank/apply.py check patch.json            # validate a patch
python bank/apply.py apply patch.json            # generate the options, merge into the bank and quotes
python bank/show.py m3-322                       # an item with its key, traps and notes
python bank/blind.py packet patch.json out.md    # the items without their answers, for a blind reviewer
python bank/blind.py compare patch.json ans.json # the reviewer's verdicts against the truth
python bank/review_packet.py patch.json review.json # keyless bilingual text and binding hashes
```

`bank/combo.py` builds every option set from a catalogue of symmetric templates;
nobody writes options by hand.

The method behind that table, and behind the revision pack, is written up as a
reusable, agent-neutral guide: see [Authoring workflow](#authoring-workflow) below.

Fonts: DM Sans and DM Mono are embedded under the SIL Open Font License; Chinese
text uses the operating system's fonts.

### Historical files

All active items now have per-statement notes and quotes. The temporary
new-format filter, one-off converter and duplicate legacy JSON snapshots
have been removed. That migration and the first repairs reserved 1,511 IDs in
`bank/retired-ids.json`;
`apply.py next` skips them and `apply.py check` rejects their reuse. The final
completion wave reserves 12 further replaced IDs, for 1,523 at that stage. The 01–26 scope change retires three more, for 1,526 in total.
The original questions and quotes remain at commit
`7787e991cc7a5c6eb0e22f1c9216ae133f2daf27` (`v1.7.5`):

```bash
git show v1.7.5:web/questions.json
git show v1.7.5:docs/quotes.json
```

The two later replacements, `m3-261` → `m3-322` and `m1-142` → `m1-177`,
preserve their old questions and quotes in [the implementation record](bank/audit/implementation.json).
The audit reports retain their historical baselines and validate the follow-up
against current statements; run `bank/audit/report.py --check`,
`bank/audit/terms_report.py --check`, `bank/audit/p1_report.py --check` and
`bank/audit/remaining_report.py --check` with Python; CI runs all four.
The later P1 additions and their final blind reviews are recorded in
[`bank/audit/p1-implementation.json`](bank/audit/p1-implementation.json),
which verifies the earlier bank without rewriting its audit history.

The [final completion record](bank/audit/remaining-implementation.json) adds the
remaining P2/P3 coverage and preserves each expanded question's retired snapshot.
The validator reconstructs all preceding bank versions, including replacements,
and binds final blind verdicts to their reviewed text. Document 15's image-only form
labels are in `docs/transcripts/15.json`, bound to raw PDF hashes and independently
checked; `docs/extract_text.py` inserts them on their original pages. Recheck the
transcript whenever the PDF changes; the source tests reject stale bindings.

Keep the numbered sources, extracted text, authoring guide and conflicts
register: they are inputs to authoring and verification, not build leftovers.

## The revision pack

The pack is generated from [`revision/`](revision/README.md) with Python 3's
standard library alone:

```bash
python revision/pack_build.py dist/mso-revision-pack.html
```

[`revision/README.md`](revision/README.md) covers its layout, the rules each page
follows, and the review tools.

## Authoring workflow

[`docs/authoring/exam-prep/GUIDE.md`](docs/authoring/exam-prep/GUIDE.md) is the
method behind both files, written for any exam. It covers choosing and checking
the sources, settling conflicts between them, and writing the study pack and the
question bank. It also covers verifying every answer blind, guarding the bank
with tests, and delivering the mock exam. The exam format is a spec the user
defines, so nothing in the guide is tied to this exam; this repository is its
reference implementation.

Read the Markdown directly with any agent or editor; no plugin or slash command
is required. The former preview-server configuration is replaced by the standard
`python -m http.server 8321 --bind 127.0.0.1 -d web` command.

The method's version is recorded in the guide introduction. Historical method
versions are tagged `skill-vX.Y.Z` on their source commit. Those tags do not
begin with `v`, so they never trigger a release. Source on `main` may be newer
than the latest publicly released files; public releases require authorization.

| Version | Date | First released in | What changed |
|---|---|---|---|
| 2.3.0 | 18 Oct 2026 | v1.9.0 | Adds source-first coverage audits, explicit semantic support checks, image-page and version evidence, scoring-history handling, and scope-aware review costs. Respects settled project decisions and authorization; moves conditional guard/tool detail into references. |
| 2.2.0 | 28 Sep 2026 | v1.7.5 | Adds calibrating a mechanical filter and a cheaper model on a judged sample before a bulk review, with the numbers from this repository's quote sweep. |
| 2.1.0 | 28 Sep 2026 | v1.7.4 | Adds the options-only guesser to the guard catalogue, and what this repository measured once it had the new checks: stored deciding quotes, convergence and echo at chance, and the guesser's results. |
| 2.0.0 | 28 Sep 2026 | v1.7.4 | Renamed `exam-prep`. Covers the study pack and the mock-exam app as well as the bank, and makes the exam format a spec the user defines. Adds the intake questions, the conflicts register, verification against the pack, the negation, echo and twin-statement tells, and briefs for subagents. |
| 1.2.1 | 28 Sep 2026 | v1.7.2 | A translated "the said X" may point back to an earlier statement, or to a kind of X. |
| 1.2.0 | 27 Sep 2026 | v1.7.0 | Prove that a guard can fail. A translated "the said X" must point back to something the item has named. |
| 1.1.0 | 21 Sep 2026 | v1.5.9 | Numbers as the unknown: ask about the rule, not the section number. |
| 1.0.0 | 7 Sep 2026 | v1.5.8 | First version, as `exam-question-bank`, covering the question bank only. |

## Releases

Releases are cut by tag. Pushing a tag beginning with `v` runs
[`release.yml`](.github/workflows/release.yml), which vets and tests the bank,
builds the file from that exact commit, and attaches it to a GitHub release
together with the revision pack built from `revision/`. The tests run before the
build, so a tag that fails never becomes a download.

Use an annotated tag: its message becomes the release notes, so say what
changed for a candidate. Keep `--cleanup=whitespace`, or git drops every line
that starts with `#`, Markdown headings included.

```bash
git tag -a vX.Y.Z --cleanup=whitespace -F notes.md
git push origin vX.Y.Z
```

Before release, update the bilingual `CHANGELOG.md`, counts and candidate-facing changes.
Run the complete checks above and open both HTML outputs. Review `git diff`, commit
and push `main`, then replace `vX.Y.Z` with an unused version number.
Save that version's release notes as `notes.md` and run the annotated-tag commands above.
Confirm both CI and Release succeed in GitHub Actions, then verify the two release
attachments and their download links. A successful tag push alone is not a published release.
Never overwrite a published tag. Distribution is an offline HTML download through
GitHub Releases; no separate server deployment is required.
