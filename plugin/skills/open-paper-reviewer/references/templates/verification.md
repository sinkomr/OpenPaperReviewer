# Template: verification

`07_verification.md` is the log of Phase 7.

```markdown
# Verification log

Done in a fresh context: yes | no (why not)
Web access: yes | no

## 1. Sources

| Citation id | Source | Access reached | Result | Error type | Decision |
|---|---|---|---|---|---|
| C-001 | short citation | full text | valid | none | none |
| C-002 | short citation | abstract | error | unsupported | redo A-04 literature check |

Result is valid, error or could not open. Error type is misattributed, unsupported, nonexistent or other.
Decision for an error is one of: patch in place (a correct source exists and the argument survives); redo the analysis that depended on it; drop the statement.

## 2. Numbers

| Where in the review | Value stated | Recomputed | Calculation | Agrees? |
|---|---|---|---|---|

## 3. Quotations

Which claim texts and quotations were compared with the paper (all, or which sample), and any that were not verbatim or were mislocated.

## 4. Consistency

Any claim whose verdict, severity or confidence differed between its scrutiny block, the synthesis table and `claims.json`.

## 5. Defence pass

For each Critical or Major finding: the strongest reply the authors could make from the paper itself, and whether the review already answers it.

| Finding | Strongest reply for the authors | Answered in the review? | Action |
|---|---|---|---|
| B-02 | … | yes, in Topic 3 \| no | none \| answered with evidence \| verdict lowered |

## 6. Corrections made

| # | What was wrong | Correction | Files changed | Claims affected | Verdict changed? |
|---|---|---|---|---|---|

Final sweep: after corrections, a search of every phase file found no remaining use of a source marked as an error.

## 7. Outcome

Citation verification: all | partial | none.
Sources still unverified and the statements that rest on them:
```
