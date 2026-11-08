---
id: T-REPRODUCIBILITY-ACROSS-SAMPLES
name: Variation between samples and laboratories
type: technique
field: physics/methods
applies_when: a claim rests on one or a few samples, devices, crystals, films or runs, reports a best or representative sample, compares samples or batches, tracks ageing or degradation, or compares results between laboratories, including round-robin or interlaboratory comparisons
version: "0.1"
---

# Variation between samples and laboratories

## 1. Yield, and the best specimen against the typical one

**Question.** Does the paper state how many samples or devices were made, how many were measured and how many showed the claimed effect, and is the headline value that of the best specimen or of a typical one?

**Why it matters.** A property can vary from sample to sample even when each measurement is precise, so a value taken from a few specimens describes the material or design only if those specimens represent the whole set. A headline taken from the best specimen, with the others unreported, presents a result that holds for a minority of specimens as if it were general.

**Resolved by.** The numbers made, measured and showing the effect stated for each kind of sample; results for all samples, from the best to the worst, in a table or distribution; the headline value given alongside the typical value and the range; the yield and the conditions under which the effect appears stated as part of the result.

**Benchmark.** [1], [2], [3]

## 2. Independent preparations, not pieces of one preparation

**Question.** Do the replicate results come from independently prepared samples (separate growth runs, batches or fabrication rounds), or from pieces of one crystal, devices on one chip, or one sample measured again, and does the paper say which?

**Why it matters.** Replicates made over a short time from the same preparation, under the same conditions, show repeatability only. They leave out the variation that appears between preparation runs, between days and after changes of calibration or operator, which is often the largest part of the spread. A result can recur on every device of one chip and still fail to recur in the next preparation.

**Resolved by.** The conditions that changed and stayed fixed between replicates stated, as metrology vocabulary recommends; results from more than one independent preparation, with the spread within and between preparations given separately; any claim of reproducibility matched to the conditions that were actually varied.

**Benchmark.** [4], [5]

## 3. Sources of variation between samples

**Question.** Does the paper relate the spread between samples, and the presence or absence of the effect, to measured properties of each sample, such as composition, thickness, defect density, substrate or position on a wafer, and were the characterisation data that support the claim taken on the samples that show the effect?

**Why it matters.** Variation within a sample, or between samples from the same batch, can dominate the uncertainty of a result even when the measurement itself is well controlled. Defects, impurities and growth conditions change properties from one specimen to the next, so characterisation of a sister sample, or of one spot, may not describe the specimen whose measurement carries the claim.

**Resolved by.** Structural, compositional or other characterisation reported for the specimens that carry the claim, or a measured spread across the batch showing that a sister sample stands in for them; the effect plotted against the sample parameters most likely to control it; samples that do not show the effect characterised as fully as those that do; where the sample is inhomogeneous, the measured region identified and the variation across the sample measured.

**Benchmark.** [3], [6]

## 4. Preparation and handling details that drive variation

**Question.** Does the paper report the preparation and handling details that control the variation between samples, such as the source and purity of starting materials, substrate, growth or annealing conditions, post-processing and the atmosphere in which samples were handled, in enough detail for another laboratory to make an equivalent sample?

**Why it matters.** Differences between laboratories often trace back to procedural details that neither side thought worth reporting. Precursor purity, contamination and growth substrate change defect densities and therefore measured properties, so a recipe that omits them can produce different samples in another laboratory.

**Resolved by.** Starting materials with supplier, grade or purity; preparation parameters with their tolerances; the steps found to matter, and those found not to matter, stated; handling and storage conditions given; where the recipe is known to be sensitive, the window of conditions in which it works.

**Benchmark.** [2], [6], [7]

## 5. Ageing, degradation and sample history

**Question.** Does the paper state how long after preparation each measurement was made, how samples were stored and exposed in between, and whether the property changes with time, exposure, thermal cycling or the measurement itself?

**Why it matters.** Many materials and devices change after preparation: exposure to air or moisture can alter electrical and optical properties within minutes to months, and some changes reverse when the stress is removed. A comparison between samples measured at different ages, or before and after a stress, can then show ageing instead of the effect claimed.

**Resolved by.** The time between preparation and measurement, and the storage atmosphere and temperature, reported for each data set; the same sample measured again after a stated interval or after the other measurements; reversible and irreversible changes distinguished, for example by a recovery period; ambient-induced changes separated from those caused by light, heat or bias; protective encapsulation or inert handling stated where used.

**Benchmark.** [6], [7]

## 6. Comparison with results from other laboratories

**Question.** When a claim rests on agreeing with, disagreeing with or improving on values measured elsewhere, does the paper compare the difference with the spread found between laboratories and with the combined uncertainties, and does it state how its measurement conditions and samples differ from theirs?

**Why it matters.** Even on a single shared material, the spread between laboratories can reach several per cent for directly measured quantities and more for derived ones, and many times more for samples whose response drifts during measurement. Uncertainties quoted by a single laboratory often leave out this spread: disagreements between independent measurements, scaled by their stated uncertainties, occur far more often than those uncertainties predict.

**Resolved by.** The difference from earlier values expressed in units of the combined uncertainty, with any known spread between laboratories for that quantity included; the measurement procedure, sample source and conditions compared with those of the earlier work; where possible, the same or equivalent samples measured in a second laboratory; a claim of improvement only where the difference exceeds the spread between laboratories.

**Benchmark.** [2], [4], [8], [9], [11]

## 7. Design and reporting of round-robin comparisons

**Question.** For a round-robin or interlaboratory comparison, does the paper state whether the same samples were circulated, how their stability during circulation was checked, whether a common measurement protocol was used, and how the laboratory results were combined, including any treatment of outlying results?

**Why it matters.** A comparison can attribute to laboratories differences that come from samples that changed in transit or from protocols that differed, and in some comparisons the measurement method, not the equipment, has been the largest source of spread. The choices of which laboratories take part, how many replicates each makes and how a common value is formed all change the spread that is reported.

**Resolved by.** The circulation scheme and timeline described, with the samples measured again at the start and end, or a stable reference sample included alongside the test samples; the protocol stated and any departures by individual laboratories reported; every participating laboratory's result shown, with its uncertainty; the method of forming a common value and the treatment of outlying results stated; the main contributions to the spread identified, such as sample dimensions or measurement method.

**Benchmark.** [8], [9], [10], [11]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | P. Bøggild, Research on scalable graphene faces a reproducibility gap, Nat. Commun. 14, 1126 (2023); read in Europe PMC (PMC9974952) | doi:10.1038/s41467-023-36891-5 |
| 2 | Committee on Reproducibility and Replicability in Science, National Academies of Sciences, Engineering, and Medicine, Reproducibility and Replicability in Science, The National Academies Press, Washington, DC (2019), Chapter 5 "Replicability" read in the online edition | doi:10.17226/25303 |
| 3 | NIST/SEMATECH e-Handbook of Statistical Methods, Sec. 2.5.3.2, Material inhomogeneity (web edition, read 2026) | https://www.itl.nist.gov/div898/handbook/mpc/section5/mpc532.htm |
| 4 | Joint Committee for Guides in Metrology (JCGM), International vocabulary of metrology: basic and general concepts and associated terms (VIM), 3rd edition, JCGM 200 (2012), online edition, entries 2.20, 2.22 and 2.24 | https://jcgm.bipm.org/vim/en/2.24.html |
| 5 | NIST/SEMATECH e-Handbook of Statistical Methods, Sec. 2.5.3.1.1, Type A evaluations of time-dependent effects (web edition, read 2026) | https://www.itl.nist.gov/div898/handbook/mpc/section5/mpc5311.htm |
| 6 | C. Dong et al., Air-stable, large-area 2D metals and semiconductors, ACS Nanosci. Au 4, 115 (2024); read in Europe PMC (PMC11027125) | doi:10.1021/acsnanoscienceau.3c00047 |
| 7 | M. V. Khenkin et al., Consensus statement for stability assessment and reporting for perovskite photovoltaics based on ISOS procedures, Nat. Energy 5, 35 (2020) | doi:10.1038/s41560-019-0529-5 |
| 8 | E. Alleno et al., Invited article: A round robin test of the uncertainty on the measurement of the thermoelectric dimensionless figure of merit of Co0.97Ni0.03Sb3, Rev. Sci. Instrum. 86, 011301 (2015) | doi:10.1063/1.4905250 |
| 9 | R. B. Dunbar et al., How reliable are efficiency measurements of perovskite solar cells? The first inter-comparison, between two accredited and eight non-accredited laboratories, J. Mater. Chem. A 5, 22542 (2017) | doi:10.1039/c7ta05609e |
| 10 | W. F. Guthrie, Interlaboratory comparisons, in Encyclopedia of Statistics in Quality and Reliability, Wiley (2007); NIST publication record | https://www.nist.gov/node/662681 |
| 11 | D. C. Bailey, Not normal: the uncertainties of scientific measurements, R. Soc. Open Sci. 4, 160600 (2017); read on arXiv (1612.00778) | doi:10.1098/rsos.160600 |
