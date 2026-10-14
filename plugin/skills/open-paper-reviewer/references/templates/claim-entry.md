# Template: claim-entry

One entry per claim in `02_claims_registry.md`. Group entries under a heading per group (`## Group A: name`).

```markdown
### A-01
- **Text (verbatim):** "…"
- **Location:** section, page, figure, table or equation
- **Type:** observation | quantity | method | model | interpretation | citation | comparison | significance
- **Tier:** 1 | 2 | 3, with a one-line reason
- **Headline:** yes | no
- **Evidence offered in the paper:** the figures, tables, equations or supplementary items it points to, or "asserted without evidence"
- **References cited for it:** [n], [m], or none
- **Depends on:** claim ids, or none
- **Supplementary material:** not needed | partly needed | fully needed, and whether it was available
- **Checklist items:** P-n, …, or none
```

The registry ends with the coverage table:

```markdown
## Coverage

| Sentence of the abstract or stated conclusion | Claim ids |
|---|---|
| "…" | A-01, B-02 |
```
