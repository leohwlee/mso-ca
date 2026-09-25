# Revision pack

A bilingual (English / Traditional Chinese) revision pack for the MSO Competence
Assessment, built as a single HTML page: AMLO Parts 1–7 and Schedules 1–4, the
AML/CFT Guideline chapters, the other C&ED guidelines, and the circulars with the
FAQ. Every release attaches the built page as `mso-revision-pack.html`, next to the
mock-exam app.

## Build

```
python revision/pack_build.py [output.html]
```

Python 3 standard library only. Without an argument the page is written to
`revision/mso-revision-pack.html` (gitignored), which is where the review tools
look for it. On Windows, set `PYTHONIOENCODING=utf-8` so the build's warnings print.
The build is deterministic: the same sources give the same bytes on any platform.

## Layout

- `pack_build.py` assembles the pages: the document list, the switcher, the outline.
- One module per page, figures in the matching `*_fig.py`:
  - `p1`–`p7` and `p6a` are the AMLO Parts (`p3_sec`, `p4_sec`, `p5_sec` for
    Parts 3–5).
  - `s1`–`s4` are the Schedules; Schedule 2 is `s2page`, built from `bl_sec1`,
    `bl_sec2`, `s2x` and `s2appx`, with figures in `bl_figs` and `bl_figs2`.
  - `g1`–`g8` are the Guideline chapters; `g8` covers chapters 8 and 9, and
    there is no `g4`, because chapters 4, 10 and 11 sit on the Schedule 2 page.
  - `gl` covers the C&ED guidelines, and `ci` the circulars and the FAQ.
- `bl_core.py` and `ui.py` hold the shared building blocks; `pack_css.css` and
  `pack_js.js` hold the page's style and behaviour.
- `AUTHOR_GUIDE.md` is how to write or change a page.
- `CONFLICT-CALLS.md` records how the pack settles conflicting sources.

## Rules the owner set

- Each language view follows its own source text. The English view is English
  only, the Chinese view Chinese only, and both appear together only in the combined
  view. No page compares the two language versions.
- Where two official documents disagree, the owner's call decides, in both views.
  See `CONFLICT-CALLS.md`.
- Only current documents are sources: the 23 in [`docs/`](../docs/README.md).

## Check

- `review/page_check.py <module> <VAR>_BODY <VAR>_NAV <page>`, run from
  `revision/`, checks one page: language purity, dead links, figures drawn per
  view, bullets, duplicate ids. It also renders each figure to `review/preview/`
  so you can look at it. It needs Chrome; set `CHROME` if Chrome is not at the
  Windows default path.
- `review/render_all.sh` runs the checker on all 21 pages.
- `review/audit.sh <width>` audits the built page in a browser at that width:
  language purity per view, overflow, figure text inside its box. It expects Git Bash on Windows.
- `review/extract.py` dumps each section's English and Chinese text for review.
  It needs `beautifulsoup4`.

## Release

`.github/workflows/release.yml` builds the pack from this folder when a `v*` tag is
pushed and attaches it to the release; CI builds it on every push.
