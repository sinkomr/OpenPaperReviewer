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

## 3. Robustness to processing choices

**Question.** Do the features a claim rests on survive reasonable changes to the processing parameters?

**Why it matters.** A feature that appears only for one choice of window, threshold or fitting range may belong to that choice.

**Resolved by.** The result shown for a range of reasonable parameter choices, or the unprocessed data in which the feature is already visible.

**Benchmark.** None needed: this is a matter of logic.

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | Joint Committee for Guides in Metrology, Evaluation of measurement data: Guide to the expression of uncertainty in measurement, JCGM 100:2008 (2008) | doi:10.59161/JCGM100-2008E |
| 2 | M. Rossner and K. M. Yamada, What's in a picture? The temptation of image manipulation, Journal of Cell Biology 166, 11 (2004) | doi:10.1083/jcb.200406019 |
