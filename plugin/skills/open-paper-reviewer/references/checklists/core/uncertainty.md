---
id: C-UNCERTAINTY
name: Calibration and uncertainty
type: core
field: any
applies_when: the paper reports measured or derived quantities
version: "0.1"
---

# Calibration and uncertainty

Whether the numbers the paper reports come with enough information to judge how far they can be trusted.

## 1. Uncertainty stated

**Question.** Does each reported quantity carry an uncertainty, and does the paper say how it was obtained?

**Why it matters.** A value with no uncertainty cannot be compared with another value, with a prediction or with a reference, so no claim of agreement or difference can rest on it.

**Resolved by.** An uncertainty on each headline quantity, with its components listed and the way each was evaluated.

**Benchmark.** [1]

## 2. Uncertainty carried through

**Question.** Are uncertainties propagated into derived quantities, including those from calibration, from corrections and from the assumptions of any model used?

**Why it matters.** A derived quantity inherits the uncertainty of everything that went into it. Quoting only the statistical scatter of the final step understates it.

**Resolved by.** A combined uncertainty for each derived quantity, with the corrections and constants used and where they came from.

**Benchmark.** [1]

## 3. Calibration described

**Question.** Is the calibration of each instrument described: the reference used, when it was done, and how the calibration enters the result?

**Why it matters.** An uncalibrated or miscalibrated instrument shifts every value it produces, and the shift does not show up as scatter.

**Resolved by.** The calibration procedure and reference for each quantitative measurement, described so that the analysis could be repeated.

**Benchmark.** [1]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | Joint Committee for Guides in Metrology, Evaluation of measurement data: Guide to the expression of uncertainty in measurement, JCGM 100:2008 (2008) | doi:10.59161/JCGM100-2008E |
