---
id: C-STATISTICS
name: Statistics and sample size
type: core
field: any
applies_when: always
version: "0.1"
---

# Statistics and sample size

Whether the amount of data, and the way it was analysed, can carry the conclusions drawn.

## 1. Sample size and the unit of replication

**Question.** For each result, is the number of independent samples stated, with what counts as one sample and how the number was decided?

**Why it matters.** Repeated readings of one sample are not independent samples. A result from a small number of independent units is more likely to be a chance finding and to overstate the size of the effect.

**Resolved by.** The exact number of independent units behind each result, the unit named, and the basis for the sample size.

**Benchmark.** [1], [2]

## 2. Effect sizes, not only thresholds

**Question.** Are conclusions based on the size of effects with their uncertainties, and not only on whether a significance threshold was passed?

**Why it matters.** Passing a threshold says nothing about how large or how important an effect is, and a conclusion that rests on the threshold alone can be right or wrong for reasons the test does not capture.

**Resolved by.** Effect sizes with intervals or uncertainties, the test named, and conclusions worded to match.

**Benchmark.** [3]

## 3. Analysis choices disclosed

**Question.** Were the choices that affect the result (which data to exclude, when to stop collecting, which comparisons to report) fixed in advance, or are all of them disclosed?

**Why it matters.** When these choices are made after seeing the data and not reported, the chance of a false positive rises well above the nominal rate.

**Resolved by.** A statement of the exclusion rules and whether they were set in advance, the stopping rule, and every comparison that was made.

**Benchmark.** [1], [4]

## 4. Scatter that fits the measurement

**Question.** Is the spread in the data what the stated measurement should give: no larger than the quoted uncertainties, and no smaller than counting statistics, differences between samples and instrument noise allow?

**Why it matters.** Independent observations scatter. Data that follow a curve or a distribution more closely than the measurement allows call for an explanation: they may have been selected, smoothed or averaged, or a calculated curve may be plotted as data. Each of these is a step the paper should state.

**Resolved by.** Scatter and error bars in keeping with the number of samples and the noise of the method, all of the data shown or the rule for choosing them stated, and calculated curves marked as such.

**Benchmark.** [5], [6]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | N. Percie du Sert, V. Hurst, A. Ahluwalia et al., The ARRIVE guidelines 2.0: Updated guidelines for reporting animal research, PLoS Biology 18(7), e3000410 (2020) | doi:10.1371/journal.pbio.3000410 | full text | Table "ARRIVE Essential 10": item 1b asks for the experimental unit; item 2 for the exact number of units per group and how the sample size was decided; item 3 for inclusion and exclusion criteria and whether they were set in advance |
| 2 | K. S. Button, J. P. Ioannidis, C. Mokrysz et al., Power failure: why small sample size undermines the reliability of neuroscience, Nature Reviews Neuroscience 14, 365-376 (2013) | doi:10.1038/nrn3475 | abstract | Abstract: low statistical power lowers the likelihood that a significant result reflects a true effect and leads to overestimated effect sizes |
| 3 | American Statistical Association, American Statistical Association releases statement on statistical significance and p-values, press release (7 March 2016) | https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf | full text | Principles 3 and 5: conclusions should not rest only on whether a p-value passes a threshold, and a p-value does not measure the size or importance of an effect |
| 4 | J. P. Simmons, L. D. Nelson and U. Simonsohn, False-positive psychology: undisclosed flexibility in data collection and analysis allows presenting anything as significant, Psychological Science 22, 1359-1366 (2011) | doi:10.1177/0956797611417632 | abstract | Abstract: flexibility in data collection, analysis and reporting sharply raises false-positive rates; the remedy proposed is disclosure |
| 5 | Joint Committee for Guides in Metrology, Evaluation of measurement data: Guide to the expression of uncertainty in measurement, JCGM 100:2008 (2008) | doi:10.59161/JCGM100-2008E | full text | Clause 4.2.2: individual observations of a quantity differ because of random effects, and the experimental standard deviation describes their dispersion about the mean |
| 6 | J. B. Carlisle, Data fabrication and other reasons for non-random sampling in 5087 randomised, controlled trials in anaesthetic and general medical journals, Anaesthesia 72, 944-952 (2017) | doi:10.1111/anae.13938 | abstract | Abstract: the probability of a set of reported means can be calculated from their standard deviations and group sizes; across the trials examined there was an excess of baseline means more alike than chance allocation would give |
