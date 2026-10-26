# Producing at volume

Contents: [Patches and one applier](#patches-and-one-applier) · [Packets](#packets) ·
[Briefs](#briefs) · [Order of operations](#order-of-operations) ·
[Repairs and sweeps](#repairs-and-sweeps) · [Releases](#releases) ·
[Environment traps](#environment-traps)

## Patches and one applier

- **Subagents return patches and never edit the bank.** A patch is a JSON list of
  complete items (new or replacing an id). Parallel packets cannot collide, and
  re-running is idempotent.
- **One applier validates and merges each item separately**, so one bad item
  never sinks a batch. `bank_tool.py check` on the merged result is the gate.
- **A no-op apply must round-trip the bank byte for byte** (indent, escaping, key
  order, line endings). Verify that before the first real write, or every apply
  shows as a whole-file diff.
- **Three commands make hundreds of rewrites tractable**: `list` the failing
  items with their measurements; `check` a patch's resulting measurements before
  applying; `apply` what passes. Forty batches cleared 637 items this way in the
  reference project.
- **All languages of an item travel in one patch entry.**
- **Run every check on the merged patches**: patches that pass one by one can
  jointly break a bank-wide share.

## Packets

- Give each packet a disjoint slice of ids (`ids[i::n]`) and inline the exact
  source passage or chapter it needs, in its language. Batches of 16–20 items
  worked best.
- Save every ~8 items. Rate limits and expired sessions each killed a whole wave
  once; incremental saves plus resuming the same agent lost nothing.
- Check coverage against the packet's id list before calling it done: one packet
  saved 8 of 18 items and stopped silently.
- Audit each wave for bolt-on phrases that appear only in distractors; they become
  a tell of their own.

## Briefs

Every brief names:

- the job; the tools and files (the finder, `bank_tool.py`, the sources, the spec
  and the register);
- what not to open: keys, notes and quotes for blind work; the bank and other
  packets for writing work;
- the output schema per item, and "save every 8";
- the check to pass before handing back, and the reply format.

**Write a packet.** "Write N items for section S from these source passages
(inlined). Follow the spec, the register and the rules in item-writing.md: the
unknown is substance; one defensible answer; distractors from the material, one
defect each, of the kinds listed; options in one length band; every statement
and option explained with its locator; the deciding quote per statement,
verbatim. Before writing a point, run `find` to check the bank does not already
key it. Return a patch file; run `bank_tool.py check` on a copy of the bank with
your patch; never edit the bank."

**Blind answer.** "Answer each item from the cited sources, in your language only.
Options are shuffled. Rule every statement true or false before choosing. For
each item return `{id, answer, statements, second, quote, locator, code, note}`;
`second` is a second defensible answer, never a merely tempting one. Do not look
for keys, notes or the bank."

**Fix the flags.** "The flags come from checkers who can be wrong: confirm each
against the source first. Fix second answers, unsupported keys or statements,
wrong terms, garbled text, stems that misdescribe the source, missing locators
and stale explanations. Leave what the owner chose to keep (listed). Output a
patch, run `check`, never apply."

**Review applied decisions.** "For every changed item, check the decision is
implemented in full, the key is right and unique, the languages agree, the
explanation matches the final text, the citation points at the passage, and
nothing else moved."

## Order of operations

The order that makes a batch pass blind review in one or two rounds instead of
four:

1. Write, then run every mechanical check (including the project's own style
   checks) and fix what fails.
2. Search the bank for the same facts, so a new item does not repeat an existing
   one sentence for sentence.
3. Make every language state the same claim with the same qualifiers; each added
   gloss costs a re-review.
4. Build the blind packets from the final text; review; settle; re-review only
   what changed.
5. Apply, run everything again, rebuild the products.

## Repairs and sweeps

- **A pattern, not an instance.** Sweep every occurrence, then add a check.
- **Measure the job before quoting it**: broaden the detector first (one job was
  637 items, not the 415 first quoted), and triage its hits by hand.
- **Re-verify after a bulk rewrite**, including the explanations the rewrite
  disturbed and the other language.
- **Retire through the app**: saved papers and history refer to ids.

## Releases

- Tag a state the checks passed, and build the products from that state (in CI
  where there is one).
- Release notes say what changed for a candidate: which items were repaired,
  whether any key changed, and which release first carries a repair, because
  anyone holding an earlier download still has the wrong key.
- Ship the products as one bundle (notes, app, originals where allowed) with a
  README; refresh any screenshots from the new version.
- Before tagging, read the log since the last release for changes that
  accumulated behind documentation-only commits.

## Environment traps

- Force UTF-8 on tool output (`PYTHONIOENCODING=utf-8`, or `python -X utf8`), or
  non-Latin text comes back garbled and cannot be edited.
- Write patch files with a file-writing tool, not shell heredocs; long JSON
  heredocs break.
- `\\` in a shell command can reach the program as `\`; build backslashes in code
  or edit the file directly, then verify the bytes.
- Keep the bank's line endings, or no apply round-trips.
- Delete temporary browser profiles after rendering checks: one project left 200
  behind, 2.5 GB.
- On Windows, `python` may be a Store stub that exits silently; call a real
  interpreter by its full path and check the exit code.
- Prefer timestamps from one clock reading when an app computes both a start and
  an end; two readings straddling a millisecond made a timer test fail at random.
