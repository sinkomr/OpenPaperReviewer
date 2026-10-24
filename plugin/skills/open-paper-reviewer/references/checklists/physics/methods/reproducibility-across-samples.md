---
id: T-REPRODUCIBILITY-ACROSS-SAMPLES
name: Variation between samples and laboratories
type: technique
field: physics/methods
applies_when: a claim rests on one or a few samples, devices, crystals, films or runs, reports a best or representative sample, compares samples or batches, tracks ageing or degradation, or compares results between laboratories, including round-robin or interlaboratory comparisons
version: "0.1"
---

# Variation between samples and laboratories

Many experimental claims rest on a handful of samples, devices or runs, and assert that a property belongs to a material or a device design, not to one specimen measured once in one laboratory. Round-robin and interlaboratory comparisons, in which the same or equivalent samples are measured in several laboratories, are used to show how far a result carries from one laboratory to another.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | P. Bøggild, Research on scalable graphene faces a reproducibility gap, Nat. Commun. 14, 1126 (2023); read in Europe PMC (PMC9974952) | doi:10.1038/s41467-023-36891-5 | full text | Section "We followed all procedures, but it doesn't work": an example of reporting all samples and measurements from best to worst to give an honest picture of yield. "Slow adoption of graphene technology": statistically relevant amounts of data are needed. "The power of independent verification" and "Hardwiring reproducibility into publications": methods papers should report yield, robustness, operating windows and repeatability, and results reproduced by an independent group carry more weight |
| 2 | Committee on Reproducibility and Replicability in Science, National Academies of Sciences, Engineering, and Medicine, Reproducibility and Replicability in Science, The National Academies Press, Washington, DC (2019), Chapter 5 "Replicability" read in the online edition | doi:10.17226/25303 | full text | Ch. 5: whether results replicate depends on the proximity of the results and their uncertainties, and a repeated-significance criterion is limited because the threshold is arbitrary; avoidable sources of non-replicability include publication bias and incomplete reporting; Box 5-1: two laboratories obtained different results because of a handling detail (stirring versus shaking) that neither had reported; Recommendation 5-1: communicate all recognised uncertainties |
| 3 | NIST/SEMATECH e-Handbook of Statistical Methods, Sec. 2.5.3.2, Material inhomogeneity (web edition, read 2026) | https://www.itl.nist.gov/div898/handbook/mpc/section5/mpc532.htm | full text | Whole section: when a lot is assigned one value from a few samples but varies from sample to sample, inhomogeneity can dominate the uncertainty even for a precise, controlled measurement; random inhomogeneity is assessed by measuring several items chosen at random; no added uncertainty only if users measure at the characterised site |
| 4 | Joint Committee for Guides in Metrology (JCGM), International vocabulary of metrology: basic and general concepts and associated terms (VIM), 3rd edition, JCGM 200 (2012), online edition, entries 2.20, 2.22 and 2.24 | https://jcgm.bipm.org/vim/en/2.24.html | full text | Entry 2.20: repeatability condition keeps procedure, operators, system, conditions and location fixed over a short period. Entry 2.22: intermediate precision condition spans an extended period and may include new calibrations, operators and systems. Entry 2.24: reproducibility condition includes different locations, operators and measuring systems; Note 2 of 2.22 and 2.24: a specification should state the conditions changed and unchanged |
| 5 | NIST/SEMATECH e-Handbook of Statistical Methods, Sec. 2.5.3.1.1, Type A evaluations of time-dependent effects (web edition, read 2026) | https://www.itl.nist.gov/div898/handbook/mpc/section5/mpc5311.htm | full text | Whole section: three levels of time-dependent variation (short-term repeatability, day-to-day reproducibility, long-term stability); day-to-day changes are frequently the dominant source of uncertainty, and an uncertainty based only on short-term repeats on the test item does not cover them; nested designs over days and runs separate the levels |
| 6 | C. Dong, L.-S. Lu, Y.-C. Lin and J. A. Robinson, Air-stable, large-area 2D metals and semiconductors, ACS Nanosci. Au 4, 115–127 (2024); read in Europe PMC (PMC11027125) | doi:10.1021/acsnanoscienceau.3c00047 | full text | Sections on degradation in air: many two-dimensional materials react with water or oxygen, with changes in optical contrast, sheet resistance and device current over minutes to months, and encapsulation preserving properties; oxidation starts at vacancies and grain boundaries, and precursor purity, carbon contamination and growth substrate affect defect density; samples compared shortly after synthesis and after months in air |
| 7 | M. V. Khenkin, E. A. Katz, A. Abate, G. Bardizza, J. J. Berry, C. Brabec, F. Brunetti, V. Bulović, Q. Burlingame, A. Di Carlo et al., Consensus statement for stability assessment and reporting for perovskite photovoltaics based on ISOS procedures, Nat. Energy 5, 35–49 (2020) | doi:10.1038/s41560-019-0529-5 | abstract | Abstract: inconsistent experimental procedures and reported parameters make stability results hard to reproduce and compare; the consensus adds procedures for reversible degradation and for separating ambient-induced degradation from other stresses, and lists the procedural information to report |
| 8 | E. Alleno, D. Bérardan, C. Byl, C. Candolfi, R. Daou, R. Decourt, E. Guilmeau, S. Hébert, J. Hejtmanek, B. Lenoir, P. Masschelein, V. Ohorodnichuk, M. Pollet, S. Populoh, D. Ravot, O. Rouleau and M. Soulier, Invited article: A round robin test of the uncertainty on the measurement of the thermoelectric dimensionless figure of merit of Co0.97Ni0.03Sb3, Rev. Sci. Instrum. 86, 011301 (2015) | doi:10.1063/1.4905250 | abstract | Abstract: several laboratories measured one material; data processed statistically into uncertainties that grow with temperature; relative standard uncertainties of about 6% (Seebeck coefficient), 8% (resistivity), 11% (thermal conductivity) and 19% (figure of merit); sample dimensions probably dominate the resistivity and diffusivity uncertainties |
| 9 | R. B. Dunbar, B. C. Duck, T. Moriarty, K. F. Anderson, N. W. Duffy, C. J. Fell, J. Kim, A. Ho-Baillie, D. Vak, T. Duong, Y. Wu, K. Weber, A. Pascoe, Y.-B. Cheng, Q. Lin, P. L. Burn, R. Bhattacharjee, H. Wang and G. J. Wilson, How reliable are efficiency measurements of perovskite solar cells? The first inter-comparison, between two accredited and eight non-accredited laboratories, J. Mater. Chem. A 5, 22542–22558 (2017) | doi:10.1039/c7ta05609e | abstract | Abstract (read on the Monash University repository record): two accredited and eight research laboratories measured a perovskite cell and a silicon control cell; for a slowly responding cell the spread between laboratories was nearly ten times that for a stable silicon control cell; the measurement method, not the equipment, was the main source of variation; a method chosen to suit the cell's stabilisation and degradation behaviour is recommended |
| 10 | W. F. Guthrie, Interlaboratory comparisons, in Encyclopedia of Statistics in Quality and Reliability, Wiley (2007); NIST publication record | https://www.nist.gov/node/662681 | abstract | Abstract: interlaboratory comparisons assess random variation across laboratories, systematic differences among a fixed set of laboratories, or the property value of an artefact; design issues include the choice of laboratories, the number and stability of artefacts, the time frame and the number of replicate measurements |
| 11 | D. C. Bailey, Not normal: the uncertainties of scientific measurements, R. Soc. Open Sci. 4, 160600 (2017); read on arXiv (1612.00778) | doi:10.1098/rsos.160600 | abstract | Abstract: about 41,000 measurements of 3,200 quantities, including interlaboratory comparisons; differences between measurements of the same quantity, scaled by their stated uncertainties, have heavy tails, and 5-standard-deviation disagreements occur far more often than a normal distribution predicts, so outlying results are common |
