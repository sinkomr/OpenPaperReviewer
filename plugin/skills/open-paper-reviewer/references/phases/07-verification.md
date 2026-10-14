# Phase 7: Verification

Purpose: check the review itself before anyone relies on it. The most damaging error an AI-assisted review makes is a citation that is misattributed, misdescribed or does not exist, stated with full confidence. The second is a finding the authors could answer from their own paper. This phase looks for both.

Where your tool allows, do this phase in a fresh context, or give it to a separate agent, that has the phase files but not the reasoning that produced them. A checker that remembers why a sentence was written tends to see what it expects.

## Steps

1. **Collect.** List every outside source cited anywhere in phases 1 to 6, and make sure each has an entry in the citations table.
2. **Check each source.** Open it. Confirm the record (authors, title, venue, year, identifier), and confirm that it supports the specific statement the review attaches to it. Record the access level reached, a supporting quotation and the URL. The result is one of: valid; error (misattributed, unsupported, nonexistent or other); could not open.
3. **Decide what to do about each error.** Patch in place, if a correct source exists and the argument survives; redo the analysis that depended on it, if it does not; or drop the statement.
4. **Check the numbers.** Recompute every figure the review itself derived: conversions, ratios, estimates, orders of magnitude. Show each calculation.
5. **Check the quotations.** Every claim text and every quotation from the paper must be verbatim and correctly located.
6. **Check consistency.** Each claim has the same verdict, severity and confidence in its scrutiny block, in the synthesis table and in `claims.json`.
7. **Defence pass.** For each Critical or Major finding, write the strongest reply the authors could make from the paper itself. If the review does not already answer it, either answer it with evidence or lower the verdict.
8. **Repair.** Make every correction everywhere it applies, re-judge any verdict that leaned on an error, and log what changed. Then search all the phase files to confirm that no source marked as an error is still in use.
9. **Finalize.** Write `claims.json` and `citations.json` following the `claims-and-citations` template. Set each source's status as the rubric defines it: confirmed, corrected, removed or unverified. Set the citation-verification line in the synthesis to `all`, `partial` or `none`. Complete `run.json`.

## What unverified means for the review

A statement that rests on an unverified source stays marked as such in the synthesis. A verdict of Contradicted, or a severity of Critical, may not rest on an unverified source: verify it, find another basis, or lower the verdict.

Without web access every outside source is unverified, the verification line is `none`, and the synthesis says so in its first lines. Never describe a recalled citation as checked.

Write the log to `07_verification.md` using the `verification` template.
