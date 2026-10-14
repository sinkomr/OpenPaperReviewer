# Verification log

Fictional example used to test the validator.

Done in a fresh context: yes
Web access: yes

## 1. Sources

| Citation id | Source | Access reached | Result | Error type | Decision |
|---|---|---|---|---|---|
| C-001 | Fictional and Placeholder (2019) | abstract | valid | none | none |
| C-002 | Imaginary (2015) | full text | valid | none | none |
| C-003 | Madeup (2010) | metadata | could not open | none | statement marked unverified |
| C-004 | Notreal (2012) | abstract | error | misattributed | patch in place: year 2021 changed to 2012 |
| C-005 | Nobody (2018) | none | error | nonexistent | drop the statement |

## 2. Numbers

| Where in the review | Value stated | Recomputed | Calculation | Agrees? |
|---|---|---|---|---|
| B-01 | 28% | 28.1% | 4.1 / 3.2 = 1.281 | yes |
| B-01 | about four standard errors | 4.4 | 0.9 / sqrt(0.3^2/6 + 0.4^2/6) = 0.9 / 0.204 | yes |

## 3. Quotations

All six claim texts were compared with the paper. All are verbatim and correctly located.

## 4. Consistency

No differences between the scrutiny files, the synthesis table and `claims.json`.

## 5. Defence pass

| Finding | Strongest reply for the authors | Answered in the review? | Action |
|---|---|---|---|
| B-02 | Moisture retention is the mechanism the cited review lists first, so it is the natural default. | yes: the same review lists two others that the design does not exclude | none |

## 6. Corrections made

| # | What was wrong | Correction | Files changed | Claims affected | Verdict changed? |
|---|---|---|---|---|---|
| 1 | C-004 was cited with the year 2021 | Year corrected to 2012 | 03_scrutiny/group_B.md | B-02 | no |
| 2 | C-005 could not be found | Sentence citing it removed | 06_synthesis.md | none | no |

Final sweep: after corrections, a search of every phase file found no remaining use of a source marked as an error.

## 7. Outcome

Citation verification: partial.
Sources still unverified and the statements that rest on them: C-003, the sentence on standard design practice in `05_methods.md`, Topic 1.
