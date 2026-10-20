# Independent design assessment A

Method: isolated Assessment A by `/root/visual_refinement_a`. No detector was run or read, no Assessment B output was read, and no shipping source was edited. This is the pre-refinement design assessment, dated 2026-10-20.

Target: `revision/study-notes/part-1.html` through `part-7.html`, all 33 memory panels. Preserve the selected B blue-gray frame, white paper, ink-blue typography, Traditional Chinese / English / combined views, offline behavior, complete conditions and source filenames.

## Verdict

The visual vocabulary is appropriate for a serious study reference. Keep it. The largest problem is semantic: the CDD trigger figure gives a mutually exclusive decision-tree signal to conditions that can coexist. The main usability problem is that stacked bilingual labels turn comparisons into several screens of serial reading. Five focused fixes would improve understanding without replacing the visual system.

## Current evidence and limits

- Read `AGENTS.md`, `PRODUCT.md`, `DESIGN.md`, the current surface brief, authoring guide, Impeccable skill and critique reference, `visual_panels.py`, `memory_panels.py`, `visual_render.py`, relevant `build.py` rendering, and all of `style.css` through the inspected sections.
- Created new isolated Chromium browser contexts and pages, loading the actual current local HTML files. No existing browser tab or historical review was reused as proof.
- Inspected desktop TC captures of all 33 panels at 1440px width and current 390 × 844 bilingual viewport captures of all 33. Captured complete mobile figures as well, and inspected representative complete figures plus English mobile and combined-language desktop spot checks.
- `assessment-a-evidence/observations.json` records the current source/HTML hashes, capture timestamp, rendered panel text, dimensions and panel inventory. `viewport-evidence.json` records the phone-sized capture positions. Screenshots share those panel IDs.
- Complete figure captures use tall viewports at the same 1440px / 390px widths to avoid sticky toolbar overlap inside screenshots. These are layout evidence; the separate `*-both-mobile-viewport.png` files show the actual 390 × 844 reading experience. Initial poorly framed complete captures were replaced with correctly framed captures.
- The local browser was closed after each run. No local server or persistent process remains. Evidence images and JSON are intentional review artifacts.
- English pages measured 390px document width at a 390px viewport across all seven Parts. This is a narrow overflow check, not a full accessibility audit.
- This assessment evaluates the relationship between existing wording and its visual form. It does not reverify legislation, full publication coverage, or every bilingual legal translation.

## Five prioritized findings

### 1. P1 — CDD triggers look mutually exclusive although the introduction says to handle every applicable trigger

**Panel:** Part 6 `memory-cdd-trigger-tree`.

**Observed:** Each condition has a YES branch to the right and only a `NO ↓ Continue` route down the left numbered spine. This strongly signals “stop when YES.” The first condition, suspicion / doubts about existing identification, can coexist with new or existing relationships. The introduction says every applicable trigger must be addressed, but the geometry supplies a competing instruction. The mobile layout preserves this conflict over approximately 3,658px.

**Impact:** A learner scanning the diagram can learn the wrong relationship between conditions even though the prose is qualified. This is more consequential than a spacing defect.

**Fix:** Separate the suspicion / identification-doubt check as an always-applicable cross-cutting requirement, then present new relationship, existing relationship and occasional-transaction cases as clearly labelled case branches. Alternatively, use an explicit non-exclusive trigger list/matrix with “check every applicable case”; remove the NO-only continuation spine. Keep the tipping-off exception attached to the suspicion outcome and preserve all amount, aggregation and verification qualifications. Do not apply the same change blindly to `memory-review-commencement`, where sequential yes/no branching is useful.

**Evidence:** `p6-memory-cdd-trigger-tree-tc-desktop.png`, `p6-memory-cdd-trigger-tree-both-mobile-viewport.png`, `p6-decision-both-desktop-viewport.png`; `visual_panels.py` CDD trigger nodes and `visual_render.py` decision renderer.

### 2. P2 — Mobile bilingual comparisons require too much memory between corresponding facts

**Panels:** Especially Part 4 `memory-assessment-clocks`, Part 3 `memory-money-boundaries`, Part 2 `memory-licence-clocks`, Part 7 `memory-retention-clocks`; applies to the table / clock families.

**Observed:** Every mobile row repeats its column labels, then each label and each value becomes two separated blocks. For example, the first assessment deadline consumes almost an entire phone viewport before its conditions begin. Complete bilingual heights are approximately 5,808px for assessment clocks, 4,955px for amount boundaries, 3,413px for licence clocks and 3,248px for retention clocks. These measurements include visible source captions, and bilingual content legitimately requires more space; the avoidable part is label repetition and unnecessary separation of the event / requirement pair.

**Impact:** “Compare the starting events” becomes “remember the previous row while scrolling.” The design is readable sentence by sentence but weak as a recall aid.

**Fix:** Keep the existing groups and full conditions visible, but make each mobile item begin with a compact, clearly labelled event–requirement summary. Keep short bilingual metadata labels on one line when they fit, with a smaller translation gap than paragraph copy. Place the trigger and amount, or reference event and deadline, next to one another before the longer qualifications. Use a compact definition-list or equivalent row treatment; retain real table semantics for desktop comparisons. Do not shrink substantive text, hide exceptions, or invent a shared timeline.

**Evidence:** `p4-memory-assessment-clocks-both-mobile-viewport.png`, `p3-memory-money-boundaries-both-mobile-viewport.png`, full figures and heights in `observations.json`; `.cell-label`, `.clock-label`, `.memory-table` and combined-language spacing in `style.css`.

### 3. P2 — A true side-by-side comparison inherits unequal column emphasis

**Panel:** Part 2 `memory-inspection-versus-investigation`.

**Observed:** The inspection column inherits the generic `.memory-value` bold weight, while the investigation column does not. The two peer columns also inherit 35% and 42% widths. On a phone, a long inspection explanation becomes a bold paragraph, followed by a normal-weight investigation explanation.

**Impact:** Typography suggests that inspection is the main answer and investigation is a subordinate qualification, although both are equally important alternatives being compared.

**Fix:** Give true comparison matrices a dedicated semantic variant: narrow dimension column, equally sized peer columns, equal body weights, and selective emphasis only on the distinguishing terms. Preserve the same row headers when stacking on phones. Keep the stronger value styling where a table really is “concept / rule / qualification.”

**Evidence:** `p2-memory-inspection-versus-investigation-tc-desktop.png` and `p2-memory-inspection-versus-investigation-both-mobile-viewport.png`; `render_panel` applying `memory-value` to every second column and the generic 23/35/42 proportions.

### 4. P2 — Nested AND conditions remain prose inside otherwise useful logic groups

**Panels:** Part 3 `memory-shell-bank-and`; Part 6 `memory-transfer-information` and, to a lesser degree, `memory-pep-common-and`.

**Observed:** Outer ALL / AND and AT LEAST ONE / OR groups are clearly bracketed. Inner relationships are plain text: the shell-bank affiliation exception contains multiple cumulative conditions inside one long negative sentence; the wire-information OR option contains “date of birth AND place of birth”; the PEP measure contains “SOW AND SOF.”

**Impact:** The figure explains the outer operator but leaves the most easily confused inner grouping to the reader. On a quick review, the birth date and birthplace can be perceived as two separate OR choices, and the scope of “unaffiliated” takes careful rereading.

**Fix:** Add a restrained nested group within the existing item. For the wire option, keep one outer OR item labelled for an individual and visibly join the two required subitems with AND. For the shell-bank limb, retain the negation as the parent phrase and show its qualifying corporation criteria as one contained cumulative group. For SOW / SOF, two inline sublabels joined by an explicit AND are sufficient. Do not introduce additional branches or change modal wording.

**Evidence:** `p3-memory-shell-bank-and-tc-desktop.png`, `p3-memory-shell-bank-and-both-mobile-viewport.png`, `p6-memory-transfer-information-both-mobile.png`, `p6-memory-pep-common-and-both-mobile-viewport.png`; flat list-only logic rendering in `visual_render.py`.

### 5. P2 — Direct diagram links can land with the title under the persistent bilingual toolbar

**Panels:** All `memory-*` anchors are exposed to the same rule; observed with Part 6 `memory-cdd-trigger-tree`, also relevant to the existing link to `memory-cdd-extent-tree` and the Part 3 link to `memory-party-roles`.

**Observed:** At 1440 × 1000 in combined language mode, opening the CDD diagram directly by its hash places the top of its Chinese title partly beneath the toolbar. The toolbar is taller in this mode, while desktop scroll padding is fixed at 125px; figures do not have their own scroll margin.

**Impact:** A learner following a cross-reference can miss the destination title and lose context. This matters more after the diagrams become better connected.

**Fix:** Base the anchor offset on the current toolbar height, or set sufficient responsive figure scroll margins for all language modes. Verify direct URL hashes, in-page links and cross-Part links in TC, EN and both. This should be a layout adjustment, with no new reading controls.

**Evidence:** `p6-decision-both-desktop-viewport.png`; fixed `html` scroll padding and `.chapter`-only scroll margins in `style.css`.

## Strengths to preserve

- The quiet paper, ink-blue hierarchy, ruled sections and restrained annotation treatment suit sustained reading. No decorative icons or complex canvas interaction distract from the legal conditions.
- The three laundering stages are explicitly presented as potentially overlapping mechanisms, with labelled teaching examples rather than a mandatory numbered pipeline.
- SOW / SOF uses a concrete origin / channel example and preserves neutral meaning. The bank account is correctly presented visually as an intermediate channel in the example.
- Independent clock origins prevent a false shared timeline. Prior approval, advance renewal, subsequent notification and retention are not forced into one chronological arrow.
- The assessment pass criteria have a visible AND. Post-STR responsibilities are explicitly concurrent. Trade value uses a mismatch symbol where a forward-flow arrow would misstate the relationship.
- The current tables and diagrams remain selectable text, source filenames remain present, and mobile reflow keeps actual column labels rather than generic legacy labels.
- Full explanations remain visible. No answer-reveal interaction is needed to understand the content.

## All-panel disposition

All IDs below are the rendered `memory-*` IDs. “Keep” means preserve the semantic form, with the shared readability and anchor refinements above where relevant.

| Part | Panel | Assessment |
|---|---|---|
| 1 | `memory-three-stages` | Keep separate mechanisms and overlap warning; compact repeated bilingual captions rather than add sequence numbers. |
| 1 | `memory-ml-tf-pf` | Keep dimension-based matrix; improve mobile comparison density. |
| 1 | `memory-risk-lists` | Keep clear distinction between risk treatment and legal sanctions. |
| 1 | `memory-cross-sector-mechanisms` | Keep labelled relation / example rows and 2022 date. |
| 1 | `memory-cash-scope` | Keep traveller/cargo distinction; keep specified-control-point and request-based qualifications visually attached to their routes. |
| 2 | `memory-inspection-versus-investigation` | Fix equal-peer typography and proportions, finding 3. |
| 2 | `memory-licence-clocks` | Keep independent origins; compact event/requirement pairing, finding 2. |
| 2 | `memory-penalty-ceilings` | Keep distinct ceilings and visible calculation; preserve daily-penalty qualifications. |
| 2 | `memory-review-commencement` | Keep actual sequential decision structure; preserve notice-sent origin and separate stay concept. |
| 3 | `memory-ownership-boundary` | Keep percentage/control distinction and cross-reference; preserve company/partnership/trust separation. |
| 3 | `memory-money-boundaries` | Keep separate regimes and operators; improve mobile paired summary, finding 2. |
| 3 | `memory-shell-bank-and` | Improve nested affiliation and physical-presence grouping, finding 4. |
| 3 | `memory-fee-components` | Keep additive-fee explanation and non-universal applicability; the main calculation could be brought visually before the table. |
| 4 | `memory-three-places` | Keep comparison of use, applicability and limits; mobile inherited bold paragraphs should remain restrained. |
| 4 | `memory-assessment-pass` | Keep clear two-gate AND and counterexample. |
| 4 | `memory-assessment-clocks` | Highest priority mobile comparison-density improvement, finding 2. |
| 4 | `memory-exchange-rights` | Keep before/after-completion separation and conditional rescission. |
| 5 | `memory-risk-levels` | Keep two layers, labelled effects and feedback note. |
| 5 | `memory-review-frequency` | Keep fixed/triggered/advance distinctions; use the shared mobile density improvement. |
| 5 | `memory-control-responsibilities` | Keep role relations and combined-role caveat; do not turn into a mandatory sequence. |
| 6 | `memory-cdd-trigger-tree` | Change trigger topology, finding 1. |
| 6 | `memory-party-roles` | Keep company/customer as reference and explicit role duties; preserve overlapping-person caveat. |
| 6 | `memory-cdd-extent-tree` | Keep basic measures plus proportionate/added requirements; make the low-risk AND combination scannable and keep separate requirements nearby. |
| 6 | `memory-sow-sof` | Keep concrete two-scope example and channel distinction. |
| 6 | `memory-pep-categories` | Keep status/risk matrix and former-PEP cross-category note. |
| 6 | `memory-pep-common-and` | Keep three cumulative measures; expose nested SOW AND SOF, finding 4. |
| 6 | `memory-reliance-outsourcing` | Keep comparison and retained responsibility; improve shared mobile density. |
| 6 | `memory-transfer-information` | Keep common-plus-additional packet; visually contain the inner birth date/place AND, finding 4. |
| 6 | `memory-wire-responsibilities` | Keep actual payment-chain sequence and risk-based missing-data note. |
| 6 | `memory-trade-value-paths` | Keep mismatch and actual transmission arrows distinct; preserve example/non-proof wording. |
| 7 | `memory-reporting-route` | Clear labels currently preserve alternatives; a shared MLRO node with two outcome branches could make the existing decision more immediately visible. |
| 7 | `memory-after-report-parallel` | Keep concurrent grouping; do not number as successive tasks. |
| 7 | `memory-retention-clocks` | Keep separate starting events; improve compact event/duration pairing, finding 2. |

## Heuristic scores

These score the present Read surface and figures, not the whole practice application.

| # | Heuristic | Score | Reason |
|---|---|---:|---|
| 1 | Visibility of system status | 4 | Selected language and current Part are explicit; static figures do not need progress states. |
| 2 | Match with the real world | 3 | Mostly appropriate concept forms; CDD trigger topology is the main mismatch. |
| 3 | User control and freedom | 3 | Native links and language switching are simple; direct anchors can obscure the destination title. |
| 4 | Consistency and standards | 3 | Cohesive system, with generic value emphasis misapplied to a peer comparison. |
| 5 | Error prevention | 2 | Conditions are preserved, but the CDD tree and nested logic leave avoidable interpretation traps. |
| 6 | Recognition rather than recall | 2 | Desktop comparisons work; long bilingual mobile rows demand remembering earlier facts. |
| 7 | Flexibility and efficiency | 3 | Three language modes and cross-references help; phone comparison and anchor behavior reduce efficiency. |
| 8 | Aesthetic and minimalist design | 3 | Restrained and appropriate; repeated micro-labels and long bold blocks add visual weight. |
| 9 | Error recognition, diagnosis and recovery | n/a | No input/submission/error-recovery workflow is present in these static study figures. |
| 10 | Help and documentation | 4 | Explanations, attached qualifications and original filenames provide strong local context. |

Total: **27/36, 75% — Good**, with the P1 interpretation problem requiring correction.

## Cognitive load and reader checks

- **Single focus:** Pass. The reading surface stays focused on study.
- **Chunking:** Mostly pass. Assessment clocks are grouped 4 / 2 / 2; logic groups are generally three or four. The five independent licence cases could be grouped by prior / after-event obligations if the distinction stays explicit.
- **Grouping:** Pass overall; nested conditions need improvement.
- **Visual hierarchy:** Partial failure. One comparison gives unequal emphasis to its peer columns.
- **One thing at a time:** Partial failure in the CDD diagram because the visible branch route conflicts with its non-exclusive instruction.
- **Minimal choices:** Panel-level decisions do not exceed four visible alternatives. Seven Part navigation items are an established examination taxonomy; do not arbitrarily collapse it to satisfy a generic four-item rule.
- **Working memory:** Fail for the longest bilingual phone comparisons.
- **Progressive disclosure:** Not scored as a failure. The owner explicitly wants full study content visible; hiding conditions would be the wrong remedy.

Relevant reader perspectives: a first-time learner is vulnerable to the false stop-on-YES signal; a distracted phone reader loses cross-row comparison context; a keyboard or low-vision reader benefits from native text/links but needs reliable destination visibility. The emotional low point is repeated scrolling through labels to recover an earlier number, not lack of decoration. The best reassurance is a visible condition next to its rule.

Questions skipped: the user has already authorized direct optimization; this report supplies concrete changes for the parent agent to implement.
