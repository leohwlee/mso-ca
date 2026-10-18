# Licensing, part by part

This repository holds three kinds of material with three different owners. This
file says which is which.

## 1 · The code, the question bank, the revision pack and the authoring guide — MIT

Everything except the two items below is licensed under MIT. Full text in
[`LICENSE`](LICENSE). That includes:

- the app: `main.go`, `questions_test.go`, `web/app.js`, `web/style.css` and
  `web/index.html`, with the build scripts and the workflows;
- the question bank, `web/questions.json`: authored questions, statements and
  explanations in English and Traditional Chinese, excluding reproduced official wording;
- the revision pack in `revision/`: its generator, and the text and figures of
  its pages;
- the agent-neutral authoring guide in `docs/authoring/exam-prep/`: the method used to build the bank
  and the pack, written for any exam.

Do anything you like with it, including adapting it, translating it and selling
it. The one condition is that copies, and substantial portions such as a set of
questions or a page of the pack, keep the copyright notice and the licence text.

Releases up to and including v1.6.0 licensed the question bank under CC BY 4.0,
and copies taken from them keep those terms.

The questions and the pack are written from the official documents listed in
[`docs/README.md`](docs/README.md), and cite the paragraph each point comes
from. Authored wording, distractors, explanations and pack figures fall under MIT.
The eight marked official sample questions retain official wording; that wording,
quoted passages and reproduced source material remain outside this licence.
The provisions described are also not the author's work — see part 3.

## 2 · The bundled fonts — SIL Open Font License 1.1

`web/fonts/` — DM Sans and DM Mono, Latin subsets, WOFF2.

Copyright 2014 The DM Sans Project Authors and copyright 2020 The DM Mono
Project Authors, licensed under the SIL Open Font License, Version 1.1. Full
text in [`web/fonts/OFL.txt`](web/fonts/OFL.txt).

The fonts are embedded as data URIs in the single-file build, so that build
carries this notice and the full licence text in an HTML comment at the top of
the file. If you redistribute `mso-ca.html`, that comment must stay.

## 3 · The official documents — not licensed here

`docs/EN/` and `docs/TC/` hold the official reading materials listed in the
focused reading directory, including HKSAR Government publications, legislation and
official webpage extracts, and the joint FATF/Egmont trade-based money
laundering risk indicators. Copyright in the latter remains with FATF/OECD
and Egmont Group; its original notice is retained in the PDF. The same
goes for their text as extracted into `docs/text/`, and for the passages from
them in `docs/quotes.json`. The script that extracts the text,
`docs/extract_text.py`, is code and falls under part 1.

The two retained companion laws also sit in `docs/EN/` and `docs/TC/`.
`docs/archive/` preserves materials removed from daily reading, including
the other independently numbered companion publications under
`docs/archive/EN/`, `TC/`, `BI/` and `ZH/`:
FATF guidance and consultation drafts, UN resolutions, Customs manuals and an
official PRC Government webpage. Their original notices remain in the files;
rights remain with the respective publishers. The same applies to the companion
text extracts. These materials are not covered by this repository's MIT licence.

**These are not the author's work and are not covered by any licence in this
repository.** They are reproduced for study reference only, as
[`docs/README.md`](docs/README.md) has always said. Nothing in the MIT licence
above grants you any right in them.

If you redistribute this repository, or reuse the question bank commercially,
satisfy yourself about the terms on which those documents may be copied. Every
one of them is available from the official sources listed in
[`docs/README.md`](docs/README.md), and linking there rather than redistributing
the files avoids the question entirely.

## No warranty

None of this is legal advice, and the question bank is not an official product
of the Customs and Excise Department. It is one person's reading of published
guidance, written to study from. Verify anything that matters against the
source documents, which is why every question cites one.
