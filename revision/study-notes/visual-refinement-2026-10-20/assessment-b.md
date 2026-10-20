# Assessment B — independent detector and browser evidence

Reviewed 20 October 2026. This assessment did not read Assessment A. No shipping UI or manuscript was edited. Findings were withheld from the parent until A could finish.

Targets: `revision/study-notes/part-1.html` through `part-7.html`, exactly seven generated files. The blue annotated-reference design is the preserved baseline. PRODUCT.md, DESIGN.md, the surface brief, AGENTS.md and Impeccable's Assessment B instructions were read. Historical visual reports were not used as current verification.

## Outcome

The current figures are functional offline and contain no measured horizontal overflow or clipped containers in the tested matrix. The main actionable defect is the loss of accessible column headings in mobile tables. The clearest visual refinement opportunity is keeping comparison operators and amounts together at intermediate widths. The long bilingual figures are a composition opportunity; their height is not itself a clipping defect.

## Coverage and reproducible evidence

- 63 page states: seven Parts × TC/EN/Both × desktop 1440×1000, intermediate 900×1000, mobile 390×844.
- 297 figure instances measured across those states, representing 33 figures.
- 228 screenshots from the main matrix, plus one focused threshold screenshot. Viewport screenshots retain the real sticky toolbar. Figure-only exports hide that toolbar only for capture; all assertions precede that screenshot-only change.
- 21 additional keyboard/accessibility states: seven Parts × 390/900/1440. Tab → Enter activates the skip link; keyboard language selection changes to English in every case.
- Browser contexts and temporary profiles were newly created for B. All HTTP/HTTPS requests were blocked in the final offline file-based checks. No user tab was reused.
- Exact SHA-256 fingerprints for seven target HTML files, style.css and visual_render.py are in `assessment-b-browser.json`.

Artifacts:

- `assessment-b-detector.json`: complete raw CLI findings.
- `assessment-b-browser.json`: measurements, keyboard focus samples, screenshot index and file hashes.
- `assessment-b-browser-summary.json`: zero-overflow/error summary.
- `assessment-b-accessibility.json`: all table headers, mobile hidden labels, branch DOM order and keyboard results.
- `assessment-b-browser.cjs`, `assessment-b-accessibility.cjs`: reproduction scripts.
- `previews-b/`: screenshots named by Part, figure, language and width.

The screenshots were sampled visually across all seven Parts, all three languages and all three widths. All 297 figure instances were measured; this is not a claim that all 229 saved screenshots received a separate manual review.

## Verified defects and priorities

### P2 — Mobile tables remove both ways of discovering column meaning

At 390px, the table head is `display:none`, while every visible per-cell label has `aria-hidden="true"`. Chromium's accessibility tree retains table/row/cell roles and row headings but exposes **zero column headings** across Parts 1–6. There are 52 column headings across those Parts at 900px and 1440px, all of which are exposed at those widths. Part 7 has no comparison tables.

Example: the mobile ML/TF/PF row exposes a cell named “犯罪得益 Criminal proceeds”, without “資金來源 / Origin”. The distinction among origin, core concern and legal conditions is visible on screen but absent from the accessible column structure. The inspection/investigation table likewise loses the labels that distinguish the two powers.

Source: `style.css:145`, `style.css:231` hide the head; `build.py:165` hides the replacement labels from assistive technology. Explicit table roles at `build.py:161` do not restore the hidden headings.

Fix: visually hide rather than remove the semantic header row on phones, and keep valid header associations. Alternatively expose the per-cell labels in the stacked representation without duplicate desktop announcements. Add accessible names using the existing figure/subgroup headings for the individual tables. Verify the resulting accessibility tree at 390px; the expected column associations must remain available. Native NVDA/VoiceOver speech was not tested, so this finding is based on the observed Chromium accessibility tree and shipped markup.

Evidence: `assessment-b-accessibility.json`; `previews-b/part-3-tc-mobile.png` shows the visible labels that are currently hidden from the accessibility tree.

### P2 — Intermediate tables strand threshold operators on their own line

At 900px the page retains the chapter rail, leaving a 611px figure. Four-column tables still use 20% / 22% / 24% / 34% column widths. In Part 3's money-boundary comparison, `≥` or `>` appears alone above `HK$120,000` / `HK$100,000`. This is visible in English, and the two-language view adds further vertical separation. The operator remains present and no text is clipped, but the relation that the user must compare is split into separate lines.

Source: `style.css:247–253`, the four-column proportions and unrestricted wrapping. This is not a request to alter the values or legal qualifiers.

Fix: preserve each comparison operator + currency amount as one typographic unit, and let the explanatory sentence wrap separately. If the four columns cannot contain that unit at an intermediate width, switch that comparison to labelled stacked rows earlier or give the value column more room. Preserve all qualifiers.

Evidence: `previews-b/figure-p3-memory-money-boundaries-en-intermediate.png` and `previews-b/threshold-wrap-en-900-viewport.png`.

## Composition opportunity, not a proven failure

The phone layouts preserve all content, but many bilingual figures become several screens long. Measured at 390px, the assessment-clock figure is 5808px high, the money-boundary comparison 4955px, and the CDD-trigger tree 3658px. At 900px, the first two remain 3292px and 3118px high respectively.

Useful refinement would emphasize the start event and time/amount in each semantic unit, then put its full condition immediately below. Use existing subgroups to separate independent regimes. Preserve visible source content and the chosen B design; do not solve this by shrinking body text, adding hidden answers, or making all figures generic cards. These measurements support a layout improvement, not a claim about learner retention, abandonment or actual confusion.

The stage examples at 900px also squeeze 13px relationship labels into narrow central lanes. “Move, split” and “Reappear as” wrap more than their endpoint concepts. Earlier stacking based on the available figure width would keep the relation easier to scan. No endpoint or relation label was clipped.

Evidence: `previews-b/figure-p1-memory-three-stages-both-intermediate.png`, `previews-b/figure-p4-memory-assessment-clocks-both-mobile.png`, `previews-b/figure-p6-memory-cdd-trigger-tree-both-intermediate.png`.

## What passed

- No document-width overflow, page spills, figure spills or clipped scroll containers in any of the 63 page states.
- No wrong-language visibility, page errors or HTTP/HTTPS requests in those states.
- Figure body copy remains 15–17px, with relation/branch labels at 13px. The only measured figure text below 13px is the 12px mobile source citation/locator treatment documented in DESIGN.md.
- All figures retain source links. This check confirms presence, not independent legal/source correctness.
- Keyboard focus is visible: sampled links and language buttons expose a 2px ink-blue outline with a 4px offset. Language switching and skip-to-content activation succeeded in all 21 additional states.
- All tested decision trees keep DOM order as condition → YES outcome → NO continuation. Mobile stacking follows that same order. The arrows are supplemented with written branch labels, so meaning is not carried by color alone.
- Thresholds, comparison rows and source filenames wrap rather than disappear.
- The explicit AND between the two assessment pass requirements remains readable.

The 28px-high language controls are compact and narrower than the skill's preferred 44px comfort target, but they exceed the 24px WCAG 2.2 minimum size dimension and the product explicitly preserves compact controls. This is not reported as a WCAG failure or a priority visualization defect.

## Detector reconciliation

CLI completed with exit code 2 and **159 findings**:

| Rule | Count | Reconciliation |
|---|---:|---|
| `cramped-padding` | 5 | Part 1 only. Rendered stage groups use intentional open rules and internal padding. The rule treats visual-path wrappers as boxes; no text was actually flush/clipped in the sampled stage screenshots. No confirmed defect from these five. |
| `design-system-color` | 77 | Eleven shared CSS values repeated across seven generated files. These include old/unused rules, the selection color and annotation/list-marker extensions. Real documentation or CSS-cleanup mismatches, but not 77 independent visible color defects. The current figures preserve the B colors. |
| `design-system-font` | 7 | One per page. The detector reports a truncated `sans","microsoft jhenghei",sans-serif` family. The actual CSS declares `"Study Sans", "Microsoft JhengHei", sans-serif`, matching DESIGN.md. False positive. |
| `design-system-font-size` | 70 | Ten repeated sizes per generated file. Several are explicitly documented responsive/diagram sizes; others are overridden legacy rules or arrow glyphs. No measured diagram body uses tiny text. Do not normalize every size merely to silence the detector. |

Per-file counts: Part 1 = 27; Parts 2–7 = 22 each. The raw JSON retains exact file locations, CSS lines and snippets. The main confirmed accessibility/threshold issues are browser/source findings and were not identified by these detector categories.

## Run limitations and cleanup

- Native browser attempt was made first. The sandbox-local server was inaccessible. A local-only server was then started with the approved escalation; native IAB creation returned `IAB visibility is not supported in a subagent thread`.
- Fallback: independent headless Chromium with fresh contexts and explicit offline file support. Its initial sandbox launch failed; the approved isolated-browser escalation succeeded.
- No live overlay was injected. No user-visible overlay or detector browser-console result is claimed. The fallback evidence is the completed CLI output plus browser screenshots, dimensions and accessibility trees.
- Both temporary local server sessions were stopped; browser contexts and browser processes were closed by the scripts. No standalone presentation service remains running.
- No `.impeccable/critique/ignore.md` file was present.
- The context loader reported an unset design `buildPath` for Persuade/Experience mode. This is unrelated to the established Read surface and was not changed.
- A reporting assertion initially expected skip-link target ID `main`; the actual target is `content`. Raw browser evidence correctly records `MAIN#content` in all 21 cases. The report assertion was corrected; this was a test expectation error, not a site defect.
- This assessment makes no legal, syllabus-completeness, learning-outcome or cross-browser/screen-reader certification claim.
