# Development

[繁體中文](DEVELOPMENT.zh-Hant.md) · [Documentation index](docs/INDEX.md)

## What is necessary

Users need only the released `mso-ca.html` and a browser. There is no server,
database, account system, package manager or API key.

| Files | Purpose |
|---|---|
| `web/` | App screens, behaviour, styles, fonts and 525 bilingual questions. |
| `main.go`, `go.mod` | Combine the app into one offline HTML file. No third-party Go dependencies. |
| Four `*_test.go` files | Check the exported file, answers, source quotations, language and guessing patterns. |
| `tests/` | JavaScript app behaviour and Python source/review constraints. |
| `bank/` | Authoring tools, retired IDs and review evidence. |
| `docs/` | Approved sources, extracted text, quotations and focused instructions. |
| `revision/` | Only the archive pointer and still-applicable source-conflict decisions. |

Go is a build and verification tool, not an app backend. Rewriting the four test
files in another language would duplicate working checks. JavaScript runs the app;
Python handles source extraction, authoring and review records.

## Build and checks

Install Go 1.27+, Node.js 22+ and Python 3.10+. Run from the repository root:

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
```

Python tools use the standard library; only source re-extraction needs PyMuPDF.
On Windows, use `py -3` if `python` opens the Store, or `-X utf8` for Chinese output.
Open `dist/mso-ca.html`. For live development, run
`python -m http.server 8321 --bind 127.0.0.1 -d web` and visit `http://127.0.0.1:8321`.

## Questions, sources and evidence

Read [the format](bank/FORMAT.md), [authoring workflow](docs/authoring/exam-prep/GUIDE.md)
and [source maintenance](docs/SOURCE-MAINTENANCE.md) before changing the bank.
The current scope report validates 525 questions from documents 01–26; the four
older reports reconstruct their historical bank rather than claim current coverage.
All 1,526 retired IDs remain reserved. Keep verified historical sources and reviews.

When changing a file bound by an older review, preserve the prior bytes in an
immutable archive and add a maintenance record linking old and new hashes.
Never edit an old hash merely to silence a failure. Archived pack sources are
checked against their original review hashes without rebuilding the discontinued pack.

## Release

Update bilingual `CHANGELOG.md`, run the checks and inspect the HTML. Review and
commit changes, then push the branch. When publication is authorized, save the
version's notes in a file and create a new annotated tag:

```bash
git tag -a vX.Y.Z --cleanup=whitespace -F notes.md
git push origin vX.Y.Z
```

Replace `vX.Y.Z` with an unused version. The release workflow checks and builds
`mso-ca.html` from that exact commit. Confirm CI and Release succeeded, then download
and verify the asset. Never overwrite a published tag. The old revision pack is
available from earlier releases and the [archive](revision/README.md); new releases
contain only the exam app. `dist/` and Python caches are local build outputs.
