# Development

[繁體中文版 →](DEVELOPMENT.zh-Hant.md)

## The mock exam

The repository holds the app's parts (`web/`) and a small Go program that folds
them into the single file. Requires Go ≥ 1.27 and nothing else.

```bash
go test ./...                          # question-bank checks + vet
go run . -export-html dist/mso-ca.html # build the single file
go run .                               # or: serve web/ while developing
```

`build.cmd` (Windows) or `./build.sh` (Mac/Linux) does the same.

The bank is `web/questions.json`. `go test ./...` is more than a shape check: it
guards the faults that quietly ruin a question bank, each one added after a
review found it in real questions.

| Check | What it stops |
|---|---|
| Per-module counts, 4 or 5 options, both languages, a citation | questions going missing or half-written |
| Option length balance, rank, spread and standout | "always pick the longest" — it once passed 64% of simulated papers |
| Citation has a locator | citing a document with no paragraph to turn to |
| Statutory Chinese terms | wording the official Chinese editions never use |
| ML/TF pairing | dropping the terrorist-financing half in Chinese |
| No positional references | "option 2" in an explanation, when options are shuffled |
| No duplicate stems, no shared answer across modules | one question asked twice |
| Absolutes in combination statements | "always" and "never" marking the false statement |
| Even option punctuation | a stray semicolon marking the right answer |
| Combination format | the printed option block, verbatim, and a spread of answer letters |
| Stems state the provision; no number-only options | asking what a section number says, or which number a rule lives under |

The method behind that table — how to write a bilingual bank from a fixed set of
documents, verify it blind, and measure the surface tells that let a candidate
guess without knowing the material — is written up as a reusable skill in
[`.claude/skills/exam-question-bank/SKILL.md`](.claude/skills/exam-question-bank/SKILL.md).
It is not specific to this exam.

Fonts: DM Sans and DM Mono are embedded under the SIL Open Font License; Chinese
text uses the operating system's fonts.

## The revision pack

The pack is generated from [`revision/`](revision/README.md) with Python 3's
standard library alone:

```bash
python revision/pack_build.py dist/mso-revision-pack.html
```

[`revision/README.md`](revision/README.md) covers its layout, the rules each page
follows, and the review tools.

## Releases

Releases are cut by tag. Pushing a tag beginning with `v` runs
[`release.yml`](.github/workflows/release.yml), which vets and tests the bank,
builds the file from that exact commit, and attaches it to a GitHub release
together with the revision pack built from `revision/`. The tests run before the
build, so a tag that fails never becomes a download.

```bash
git tag v1.6.1
git push origin v1.6.1
```
