# Template: claim-entry

One entry per claim in `02_claims_registry.md`. Group entries under a heading per group (`## Group A: name`). Leave out the References cited, Depends on and Checklist items lines when they would say none; every entry keeps its Headline and Supplementary material lines.

```markdown
### A-01
- **Text (verbatim):** "…"
- **Location:** section, page, figure, table or equation
- **Type:** observation | quantity | method | model | interpretation | citation | comparison | significance
- **Tier:** 1 | 2 | 3, with a one-line reason
- **Headline:** yes | no
- **Evidence offered in the paper:** the figures, tables, equations or supplementary items it points to, or "asserted without evidence"
- **References cited for it:** [n], [m]
- **Depends on:** claim ids
- **Supplementary material:** not needed | partly needed | fully needed, and whether it was available
- **Checklist items:** P-n, …
```

The registry ends with the coverage table. Identify each sentence by where it is and its first words; `00_extraction.md` has the abstract in full.

```markdown
## Coverage

| Sentence: where it is, and its first words | Claim ids |
|---|---|
| Abstract 2: "The yield rose by…" | A-01, B-02 |
```
