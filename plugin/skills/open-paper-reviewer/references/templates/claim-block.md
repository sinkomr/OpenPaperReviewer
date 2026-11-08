# Template: claim-block

One block per claim in the Phase 3 scrutiny files. Field values come from the rubric, in its exact words. Leave out the Blocked by line when there are none.

## Full form

```markdown
### A-01: short title

**Claim (verbatim).** "…" (location)

**Internal evidence.** What in the paper supports it, whether it is shown or asserted, whether it is consistent across the paper, and any quantity recomputed.

**Literature.** Whether the cited references and established work agree, with citation ids [C-001].

**Alternatives.** Each ordinary explanation for the same observation, and what in the paper excludes it or that nothing does.

**Standard practice.** What a careful demonstration normally includes compared with what was done, citing checklist items (P-3). Say which gaps the claim needs closed and which are optional.

**Strongest reading.** The most that the evidence shown supports.

- **Verdict:** Supported | Partially Supported | Unsupported | Contradicted | Cannot Evaluate
- **Severity:** Critical | Major | Minor | Cosmetic | none (when Supported)
- **Confidence:** High | Medium | Low
- **Blocked by:** claim ids
- **Basis:** paper: location; C-001
- **Would settle it:** the one experiment, analysis or piece of information that would most directly decide the question (omit when Supported)
```

## Short form

For a routine tier-1 claim whose evidence is plain. Its verbatim text is in the registry, so the block does not repeat it.

```markdown
### A-03: short title

**Check.** One to three sentences covering whichever of the four checks apply.

- **Verdict:** Supported
- **Severity:** none
- **Confidence:** High
```

## Group summary

Each group file ends with:

```markdown
## Group A summary

- Verdicts: n Supported, n Partially Supported, n Unsupported, n Contradicted, n Cannot Evaluate
- Claims that other groups depend on: ids
- Registry changes made in this phase: splits or merges, or none
```
