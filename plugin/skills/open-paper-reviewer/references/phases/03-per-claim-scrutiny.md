# Phase 3: Per-claim scrutiny

Purpose: give every registered claim the same four checks and a verdict from the rubric.

Work through the groups in order, foundations first, writing one file per group in `03_scrutiny/` (`group_A.md`, `group_B.md`, …). Before each group, re-read the passages, figures and tables its claims point to. Verdicts written from the memory of a first reading are where reviews go wrong.

## The four checks

1. **Internal evidence.** What in the paper supports the claim: which figure, table, number or derivation. Is the evidence shown, or only asserted? Is it consistent between abstract, text, captions and supplementary material? Where it matters, look at signal against noise, whether uncertainties are given and carried through, sample size, and evidence of calibration. Recompute simple quantities yourself (unit conversions, ratios, values read from a plot) and say whether they agree. Look at the figures themselves: where two figures or panels are presented as separate measurements, compare them and check that they show different data, and check that the data scatter as much as the stated measurement should make them. Check quoted and plotted values against limits you know to be established. Where one of these checks fails, describe what is seen and what it does to the claim, and say nothing about how it came about.
2. **Literature.** A citation is not itself support. Check that the references cited for this claim say what they are cited for, and whether established work agrees, including later work that tested the claim. Give each source a citation id (`C-001`, …) and record it in the citations table with the access level you actually reached. A source you are recalling and have not opened in this run is recorded as unverified and cannot be the basis for a negative verdict. Blogs, news and forum comments can lead you to a source but are not evidence; cite the underlying work.
3. **Alternatives.** List the ordinary explanations that would produce the same observation (instrumental, statistical, artefactual, or simply a better-known mechanism), and for each say what in the paper rules it out, or that nothing does. For a claim of interpretation this is the check that matters most.
4. **Standard practice.** What a careful demonstration of this kind of claim normally includes (controls, calibration, statistics, replication) against what was done. Use the Phase 1 checklist items that apply and cite them by number. Separate what the claim needs from what would merely be good to have: a missing optional control is a note, not a reason to lower a verdict.

If a verdict turns on what a reference on the reading list says, read that reference now, following Phase 4, and write its file before you give the verdict.

## Before the verdict

State the strongest reading: the most that the evidence shown does support. If that is the claim as written, the verdict is Supported. If it is something narrower, say exactly what.

## Verdict block

Give the verdict, severity, confidence, blocked-by and basis defined in the rubric, in its exact words. All of the rubric's rules apply. The ones that matter most in practice:

- One verdict per claim. If part of a claim holds and part does not, go back to the registry, split the claim, and judge the parts separately.
- Severity is the consequence for the paper's headline if the claim fails. It is empty when the verdict is Supported.
- A headline claim that does not stand is itself Critical. If a narrower form of it stands, it is Major.
- If a claim fails only because a claim it depends on fails, list that claim under blocked-by, and still judge this one on its own evidence as far as you can.
- Contradicted, or a severity of Critical, needs a basis anyone can check: a location in the paper, or a citation whose source you opened.
- Evidence that a correction or retraction notice on the paper has withdrawn counts as absent. A claim that rested on it is Unsupported, with the notice as its basis.
- Cannot Evaluate is the verdict when the evidence is said to be somewhere you cannot see, such as supplementary material that was not supplied. Do not guess what it shows.
- For any verdict other than Supported, name the one experiment, analysis or piece of information that would most directly settle the question.

Supported is an ordinary verdict, and most routine claims in most papers earn it. A review that finds a problem with every claim has usually stopped telling strong evidence from weak.

## Form and length

Use the `claim-block` template. A routine tier-1 claim whose evidence is plain takes the short form. Other claims stay within the word budget in the rubric, with the larger budget for headline and tier-3 claims.

End each group file with its summary. If you split or merged claims, apply the same change to `02_claims_registry.md`.
