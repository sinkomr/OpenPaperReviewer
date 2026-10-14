# Phase 2: Claims registry

Purpose: turn the paper into a list of separately checkable claims. Everything after this phase is organized by claim id, so a claim missing here is never reviewed, and a claim that bundles two assertions cannot be given a clean verdict.

## How to decompose

- One claim is one assertion that could be true or false on its own.
- Take claims from the abstract, results, figure captions, discussion and conclusions. Include statements made in passing if a conclusion depends on them, claims about methods ("the detection limit is 5 ng/mL"), claims imported by citation ("as shown in [12]"), and claims of novelty or significance.
- Separate an observation from its interpretation. "The signal doubles after treatment" and "the doubling is caused by X" are two claims.
- Separate a value from what it is said to mean.
- Quote each claim verbatim, within the rubric's quote limit. Trim with an ellipsis; never paraphrase.
- A full-length paper usually yields 20 to 60 claims, a letter fewer. Far more than that means you are splitting too finely; far fewer, that you are bundling.

## Groups and ids

Sort the claims into three to eight groups that follow the paper's own logic, lettered A, B, C, …, with foundations before the claims built on them. Number claims within each group: `A-01`, `A-02`. Typical groupings:

- Experimental paper: samples and preparation; one group for each main measurement; quantitative analysis; interpretation and mechanism; significance.
- Clinical or field study: population and design; outcomes; statistical analysis; interpretation and generalization.
- Computational or modelling paper: data and setup; method; results and benchmarks; ablations and robustness; claims of generality.

## Each entry

Use the `claim-entry` template. Take the type and the tier from the rubric. Tier says how much evidence a claim needs, not whether it is right. Mark as headline the claims the title and abstract depend on.

## Coverage check

End the registry with a table that maps every sentence of the abstract and every stated conclusion to the claim ids that cover it. A sentence with no id means a claim is missing.

## Reading list

Then fix the reading list for Phase 4: every reference given high priority in Phase 1, plus any reference this registry shows to be the main outside support for a headline or tier-3 claim.

Write the registry to `02_claims_registry.md`.
