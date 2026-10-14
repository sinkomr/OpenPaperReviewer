---
id: C-PROCESSING
name: Data processing
type: core
field: any
applies_when: the paper shows or quotes data that were processed after acquisition
version: "0.1"
---

# Data processing

Whether what happened between the raw data and the published figure or number is visible to the reader.

## 1. Every step described

**Question.** Is each step between the raw data and the plotted or quoted result described well enough to repeat: background subtraction, smoothing, filtering, normalization, fitting?

**Why it matters.** Processing can create features, remove them or move them. A reader who does not know what was done cannot tell a property of the sample from a property of the processing.

**Resolved by.** The procedure and its parameters for each step, in the methods or the figure legend.

**Benchmark.** [1], [2]

## 2. Unprocessed data available

**Question.** For the results that carry the headline, is the unprocessed data shown or available alongside the processed version?

**Why it matters.** Processing that removes information present in the original cannot be assessed from the processed version alone.

**Resolved by.** Raw and processed data side by side for the key results, or a pointer to where the raw data can be obtained.

**Benchmark.** [2]

## 3. Selection and exclusion

**Question.** Were any data excluded, or shown as representative of a larger set, and by what rule?

**Why it matters.** Choosing which data to show or keep after seeing them can produce an effect that the full set does not support.

**Resolved by.** The rule for exclusion and whether it was set in advance, the number excluded, and how the examples shown were chosen.

**Benchmark.** [3]

## 4. Robustness to processing choices

**Question.** Do the features a claim rests on survive reasonable changes to the processing parameters?

**Why it matters.** A feature that appears only for one choice of window, threshold or fitting range may belong to that choice.

**Resolved by.** The result shown for a range of reasonable parameter choices, or the unprocessed data in which the feature is already visible.

**Benchmark.** None needed: this is a matter of logic.

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | Joint Committee for Guides in Metrology, Evaluation of measurement data: Guide to the expression of uncertainty in measurement, JCGM 100:2008 (2008) | doi:10.59161/JCGM100-2008E | full text | Clause 7.1.4: present the data analysis so that each important step can be followed and the calculation of the reported result can be repeated independently |
| 2 | M. Rossner and K. M. Yamada, What's in a picture? The temptation of image manipulation, Journal of Cell Biology 166, 11-15 (2004) | doi:10.1083/jcb.200406019 | full text | Section "Journal guidelines": adjustments are acceptable if applied to the whole image and if they do not obscure or eliminate information in the original; nonlinear adjustments must be disclosed in the legend |
| 3 | N. Percie du Sert, V. Hurst, A. Ahluwalia et al., The ARRIVE guidelines 2.0: Updated guidelines for reporting animal research, PLoS Biology 18(7), e3000410 (2020) | doi:10.1371/journal.pbio.3000410 | full text | Table "ARRIVE Essential 10", item 3: describe the criteria for excluding units or data points, say whether they were set in advance, and report exclusions |
