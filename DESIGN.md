---
name: "MSO Annotated Study Reference"
description: "批注式研讀冊 — bilingual reading and examination reference"
colors:
  ink-blue: "#173f63"
  body-ink: "#263e52"
  muted-ink: "#526a7e"
  faint-ink: "#60758a"
  paper: "#ffffff"
  frame: "#edf2f6"
  panel: "#f1f5f8"
  rule: "#d5e0e8"
  rule-strong: "#aebfcf"
  annotation-paper: "#fff5e3"
  annotation-ink: "#6d491a"
  correct: "#2e7d4f"
  correct-paper: "#eef6f1"
  caution: "#9a6700"
  caution-paper: "#fbf4e4"
  incorrect: "#b3352b"
  incorrect-paper: "#faeeed"
  dark-paper: "#14212e"
  dark-frame: "#0e1924"
  dark-panel: "#1c2e3e"
  dark-heading: "#dceaf5"
  dark-body: "#d0dce5"
  dark-muted: "#a6bdcf"
  dark-faint: "#91a9be"
  dark-rule: "#354a5c"
  dark-rule-strong: "#5c768b"
  dark-action: "#f2f2f2"
  dark-action-ink: "#0f0f0f"
  dark-correct: "#6fbf8f"
  dark-correct-paper: "#16241c"
  dark-caution: "#d9a43b"
  dark-caution-paper: "#2a2314"
  dark-incorrect: "#e07068"
  dark-incorrect-paper: "#2b1a18"
typography:
  masthead:
    fontFamily: "Georgia, Times New Roman, serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.4
  reading-title:
    fontFamily: "Study Sans, Microsoft JhengHei, sans-serif"
    fontSize: "30px"
    fontWeight: 650
    lineHeight: 1.5
    letterSpacing: "-.025em"
  headline:
    fontFamily: "Study Sans, Microsoft JhengHei, sans-serif"
    fontSize: "25px"
    fontWeight: 650
    lineHeight: 1.45
    letterSpacing: "-.02em"
  body-reading:
    fontFamily: "Study Sans, Microsoft JhengHei, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.8
  body-practice:
    fontFamily: "DM Sans, Segoe UI, Helvetica Neue, Arial, PingFang TC, Microsoft JhengHei, Noto Sans TC, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.7
  question:
    fontFamily: "DM Sans, Segoe UI, Helvetica Neue, Arial, PingFang TC, Microsoft JhengHei, Noto Sans TC, sans-serif"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: 1.75
  citation:
    fontFamily: "Study Sans, Microsoft JhengHei, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.65
  button:
    fontFamily: "DM Sans, Segoe UI, Helvetica Neue, Arial, PingFang TC, Microsoft JhengHei, Noto Sans TC, sans-serif"
    fontSize: "14px"
    fontWeight: 500
    lineHeight: "20px"
  numeric:
    fontFamily: "DM Mono, SFMono-Regular, Consolas, Menlo, monospace"
    fontWeight: 500
rounded:
  sheet: "0px"
  control: "3px"
  utility: "4px"
  bubble: "50%"
spacing:
  step-4: "4px"
  step-8: "8px"
  step-12: "12px"
  step-16: "16px"
  step-20: "20px"
  step-24: "24px"
  step-28: "28px"
  step-32: "32px"
  step-36: "36px"
  step-40: "40px"
components:
  button-primary:
    backgroundColor: "{colors.ink-blue}"
    textColor: "{colors.paper}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "10px 18px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink-blue}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "10px 18px"
  button-danger:
    backgroundColor: "transparent"
    textColor: "{colors.incorrect}"
    typography: "{typography.button}"
    rounded: "{rounded.control}"
    padding: "10px 18px"
  language-selected:
    backgroundColor: "{colors.ink-blue}"
    textColor: "{colors.paper}"
    rounded: "{rounded.control}"
    padding: "4px 9px"
  part-chip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.body-ink}"
    rounded: "{rounded.control}"
    padding: "9px 14px"
  reading-sheet:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.body-ink}"
    rounded: "{rounded.sheet}"
    padding: "36px 40px"
  practice-sheet:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.body-ink}"
    rounded: "{rounded.sheet}"
    padding: "32px 36px"
  annotation:
    backgroundColor: "{colors.annotation-paper}"
    textColor: "{colors.annotation-ink}"
    rounded: "{rounded.sheet}"
    padding: "16px"
  option-row:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.body-ink}"
    typography: "{typography.body-practice}"
    rounded: "{rounded.sheet}"
    padding: "16px 12px"
---

# Design System: MSO Annotated Study Reference

## Overview

**Creative North Star: "批注式研讀冊 / The Annotated Study Reference"**

The selected identity is a quiet professional study reference: a blue-gray frame holds white reading paper, ink-blue headings establish hierarchy, and restrained amber annotations distinguish common confusions. A modest serif masthead and readable sans-serif text give reading and practice a shared publication character.

Use the same vocabulary across all seven parts, Traditional Chinese, English and combined-language views. Reading supports sustained comparison; practice supports clear decisions and explicit answer feedback. Preserve complete wording, readable source filenames and useful paragraph or section locators as layouts change.

**Key Characteristics:**

- White paper within a blue-gray frame.
- Ink-blue hierarchy and a quiet serif masthead.
- Restrained amber annotations and explicit green/red answer states.
- Readable bilingual text and traceable filename citations.
- Ruled controls, square sheets and visible keyboard focus.

This captures the implemented B direction selected on 19 October 2026. Tokens come from [shared reading styles](revision/study-notes/style.css) and [practice/exam styles](web/style.css); extensions live in [.impeccable/design.json](.impeccable/design.json). Surface composition belongs in its surface brief, and product behavior in [PRODUCT.md](PRODUCT.md).

## Colors

### Primary

**Ink blue** identifies headings, active navigation, source links and primary actions. **Body ink**, **muted ink** and **faint ink** provide supporting hierarchy without making long passages accent-colored.

### Secondary

**Annotation paper** and **annotation ink** identify study misconceptions. **Caution** and **caution paper** support existing practice warnings; these related roles have separate implemented values. **Correct** and **incorrect**, with matching pale papers, retain green/red answer meanings. Authored diagrams retain explicitly labelled outcome, action and stop treatments without redefining the shared brand.

### Neutral

**Paper** is the reading surface, **frame** surrounds it, and **panel** groups explanations or selection. **Rule** separates ordinary content; **rule strong** distinguishes stronger boundaries.

The `dark-*` tokens record the existing practice/exam dark theme: dark papers, blue-gray boundaries, pale heading/body text, a light action fill and adjusted semantic colors. Apply the role mapping together. Reading currently uses the light-paper treatment.

**The Annotation Rule.** Use amber for a labelled confusion or caution. Tie green and red to explicit outcomes or answer feedback rather than the primary identity.

## Typography

**Masthead:** Georgia with Times New Roman and observed system fallbacks. Keep this a compact publication signature. Practice uses a slightly larger masthead than reading.

**Body:** bundled DM Sans. Reading embeds it as `Study Sans`, with Traditional Chinese system fallback; practice uses the broader `DM Sans` stack above. **Numeric:** bundled DM Mono for timers, scores and answer-sheet numbers. Reading navigation and steps use tabular numerals.

### Hierarchy

- **Reading title:** medium-bold ink-blue sans; reduces for tablet and phone without truncating either language.
- **Headline:** chapter hierarchy, distinct from smaller context and annotation headings.
- **Reading body:** open line spacing; rule paragraphs are slightly looser. English-only reading tightens slightly. Combined views separate the second language and use muted ink.
- **Practice question:** larger than option text; statement numbers stay attached. Question measure is capped at 68ch.
- **Citation:** smaller supporting text, underlined filenames and separate locators. On phones citations step down to 12px and wrap instead of overflowing.

Reading introductions, notes and diagram copy generally cap at 72ch; practice supporting copy allows up to 75ch.

**The Complete Context Rule.** Keep scenario qualifiers, bilingual wording, source filenames and locators readable. Adjust wrapping and layout before abbreviating content.

## Layout

Maintain a surrounding frame, compact persistent top bar and clear paper surface. Use more space between topics than within a rule, explanation or answer group. Spacing tokens describe repeated observed steps rather than one mandatory inset.

Reading uses a centered container up to 1440px, a 190px chapter rail, a 28px gap and flexible paper. At 1050px the rail becomes 165px, the gap narrows, and rule/annotation pairs and the reading overview stack. At 800px the layout becomes one column with horizontal chapter navigation. At 600px insets and type reduce again. Part navigation may scroll horizontally; text and filenames wrap within the page.

Practice uses a centered container up to 1200px. At 960px and above the exam places a flexible question sheet beside a 388px answer/timer rail; below that, the rail joins normal flow and the compact exam header remains available. At 640px the masthead, action rows and paper insets adapt for phones.

Use frontmatter sheet padding on desktop. Phone reading paper uses 24px 18px; phone practice paper uses 24px 20px. Sticky elements must leave content and focus targets visible. Comparison tables keep semantic markup while visibly stacking scenario, rule, misconception and citation in reading order on phones.

Study figures adapt to their own available width, including the space used by
the chapter rail: four-column comparisons reflow below 760px; three-column
comparisons and role relations reflow below 640px. Keep short bilingual field
labels together, with the full conditions immediately below their rule. Visually
hidden table heads retain accessible column meaning, and individual tables use
their figure or subgroup title as an accessible name. True peer comparisons use
equal widths and equal body emphasis. Comparison signs stay with their amounts.

Use a decision tree only for actual branches. CDD triggers that can coexist use
an unnumbered case map with a cross-cutting suspicion requirement; the CDD-extent
and decision-commencement trees retain explicit numbered continuation routes.
Contain inner AND groups within their one outer OR/AND item. Anchor spacing follows
the rendered toolbar height in each language mode, rather than a fixed estimate.

圖表按實際可用寬度調整：四列表於760px以下、三列表及角色關係於640px以下重新排版。
雙語短標籤保持緊湊，完整條件緊貼規則；隱藏的表頭仍供輔助閱讀工具識別。
對等比較採等寬、等強調，數學比較符號與金額不分行。
可同時適用的CDD觸發採無編號情況圖；真正分支保留決策樹，內層AND維持明確包含關係。
跳轉留白依當前語言頂欄的實際高度計算。

## Elevation & Depth

Depth comes primarily from frame/paper contrast and fine internal rules. Major sheets have a restrained blue ambient shadow; the exam rail remains unshadowed. Modals use stronger separation above a dimmed backdrop. Focus outlines indicate interaction rather than elevation. Exact shadow and motion extensions live in the sidecar.

**The Paper Rule.** Use flat white sheets with restrained ambient shadows for major surfaces. Use rules and tonal groups for internal hierarchy instead of nested floating cards.

## Shapes

Reading sheets, option rows, explanation panels and amber annotations are square. Language controls, practice buttons, part chips and flag controls have gently softened control corners. Existing utility panels and result cells may use the utility radius. Answer-sheet bubbles remain circular because their shape carries a task meaning. Borders are fine and functional.

## Components

### Buttons

Compact, deliberate actions. Primary buttons use ink-blue fill and paper text; secondary buttons are transparent with a stronger rule; destructive actions use the incorrect-state stroke and text. Practice primary hover reduces opacity; secondary hover strengthens its border. Disabled actions reduce opacity and use the default cursor. Keep the two-pixel keyboard outline with four-pixel offset.

### Language controls and part chips

Small rectangular controls. Active language and selected practice parts use primary fill with contrasting text. Reading language controls expose pressed state; Part links use an underlined current-page state. Practice chips wrap; reading Part links scroll horizontally when needed. Retain navigation and selection semantics alongside color.

### Paper and internal groups

Reading and practice question surfaces are square paper sheets. Rules separate chapters, metadata, options and citations. Panel tone groups answer explanations; pale amber identifies misconceptions. Keep study explanations visible rather than adding reveal controls.

### Answer options

Full-width ruled buttons with compact letter markers. Selection uses panel tone and a filled marker; correct/incorrect outcomes use corresponding pale rows and colored markers. Written verdicts and statement notes explain the result alongside color. Unchosen options remain fully opaque with muted text. Answered rows retain disabled behavior.

### Navigation

The chapter index uses muted default text, frame-toned hover/current treatment and a stronger current label. It becomes horizontal at narrow widths. Retain the skip link and current-location semantics. Reading/practice links carry Part and language context.

### Annotations and citations

An annotation is a pale amber rectangular inset with an explicit misconception heading. Align it with the interpretation it qualifies and stack it below at narrow widths. Current source-authored study notes show the actual repository filename, paragraph/section locator and applicable language/translation label; concept blocks need not display a raw quotation. Existing practice-answer and legacy reading contexts retain quotations where those contexts provide them. Document 24's study translation retains English-original identification. Citations are wrapping evidence, not decorative badges.

### Fields and motion

The inspected app has a hidden file-import input rather than an established visible text-field family; do not invent one from unused styling. Motion is limited to existing feedback, progress and timer states. Practice removes animation/transitions for reduced-motion preferences; reading disables smooth scrolling. Preserve these accommodations.

### Recall comparisons and diagrams

Source-bound recall aids precede full explanatory prose. Use a 22px heading,
16px table body and 13px column labels. Ink-blue concepts and moderately stronger
rule/value text establish scanning order without coloring bare numbers. A third
column always holds the applicable conditions and exceptions; mobile stacks each
row with its real column labels, never the legacy rule/misconception labels.
Keep thresholds' operators, units and deadline starting events in the value text.

The ML stages use separate mechanism examples for the same proceeds, with an
explicit overlap qualification; do not imply a mandatory sequence. Use decision
trees only for real branches (CDD triggers/extent and specified-decision commencement).
Use labelled relations for roles, separate event/requirement tracks for deadlines,
and bracketed ALL/AND or AT LEAST ONE/OR groups for cumulative or alternative data.
Do not draw a forward time arrow for advance deadlines or mix unrelated clock origins.
The assessment diagram keeps its two pass criteria joined by explicit AND.
Phone layouts stack semantic units with their conditions; identical bilingual
tokens such as MSO are shown once. Teaching examples are labelled as examples.
Selective inline term emphasis supplements complete prose; it does not replace
qualifiers, actor scope or filename citations. These components use the existing
paper, line, ink and accent tokens and add no new brand palette or font family.

## Do's and Don'ts

### Do:

- **Do** use the selected blue annotated-reference identity across reading and practice.
- **Do** label correct interpretation, misconception and source evidence explicitly.
- **Do** wrap complete source filenames and locators within the available width.
- **Do** stack comparisons and controls while retaining bilingual reading order.
- **Do** preserve visible focus, native button semantics and written answer feedback.
- **Do** use bundled fonts and local assets for offline reading and practice.

### Don't:

- **Don't** restore the former green identity as the shared brand palette.
- **Don't** use amber as broad decoration or color as the only answer explanation.
- **Don't** replace actual cited filenames with publication titles alone.
- **Don't** add hidden-answer study modes, oversized controls or promotional decoration to reading.
- **Don't** treat visual documentation or finish review as independent semantic, legal or syllabus verification.

