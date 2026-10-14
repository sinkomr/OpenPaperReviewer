# Claims registry

Fictional example used to test the validator.

## Group A: Design and measurements

### A-01
- **Text (verbatim):** "Each treatment was applied to six plots in a randomized complete block design."
- **Location:** Methods, paragraph 2
- **Type:** method
- **Tier:** 1, a standard field-trial design
- **Headline:** no
- **Evidence offered in the paper:** Fig. 1
- **References cited for it:** none
- **Depends on:** none
- **Supplementary material:** not needed
- **Checklist items:** P-3

### A-02
- **Text (verbatim):** "Mean yield was 4.1 kg per plant in mulched plots and 3.2 kg per plant in unmulched plots."
- **Location:** Results; Table 1
- **Type:** observation
- **Tier:** 1, a direct measurement
- **Headline:** no
- **Evidence offered in the paper:** Table 1
- **References cited for it:** none
- **Depends on:** A-01
- **Supplementary material:** not needed
- **Checklist items:** P-1

## Group B: Effect size and interpretation

### B-01
- **Text (verbatim):** "Mulching to 10 cm increased yield by 28%."
- **Location:** Abstract; Results
- **Type:** quantity
- **Tier:** 2, the paper's main result
- **Headline:** yes
- **Evidence offered in the paper:** Table 1
- **References cited for it:** none
- **Depends on:** A-02
- **Supplementary material:** not needed
- **Checklist items:** P-1

### B-02
- **Text (verbatim):** "The yield increase is caused by reduced evaporation from the soil."
- **Location:** Abstract; Discussion, paragraph 1
- **Type:** interpretation
- **Tier:** 2, a causal claim
- **Headline:** yes
- **Evidence offered in the paper:** asserted without evidence
- **References cited for it:** [1]
- **Depends on:** B-01
- **Supplementary material:** not needed
- **Checklist items:** P-2

### B-03
- **Text (verbatim):** "This is the largest yield response to mulch reported for tomato."
- **Location:** Discussion, final paragraph
- **Type:** significance
- **Tier:** 2, a priority claim
- **Headline:** no
- **Evidence offered in the paper:** asserted without evidence
- **References cited for it:** [2]
- **Depends on:** B-01
- **Supplementary material:** not needed
- **Checklist items:** none

### B-04
- **Text (verbatim):** "Soil nitrogen did not differ between treatments (Table S2)."
- **Location:** Results, paragraph 3
- **Type:** observation
- **Tier:** 1
- **Headline:** no
- **Evidence offered in the paper:** Table S2
- **References cited for it:** none
- **Depends on:** none
- **Supplementary material:** fully needed; not available
- **Checklist items:** P-4

## Coverage

| Sentence of the abstract or stated conclusion | Claim ids |
|---|---|
| "We compared tomato yield in raised beds mulched to 10 cm with unmulched beds." | A-01, A-02 |
| "Mulching to 10 cm increased yield by 28%." | B-01 |
| "The yield increase is caused by reduced evaporation from the soil." | B-02 |

## Reading list for Phase 4

Reference [2], the outside support for B-03.
