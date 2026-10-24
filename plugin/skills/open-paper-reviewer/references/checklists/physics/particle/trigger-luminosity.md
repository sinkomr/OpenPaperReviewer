---
id: T-TRIGGER-LUMINOSITY
name: Trigger, selection efficiency and luminosity
type: technique
field: physics/particle
applies_when: the paper reports a cross section, event rate, branching fraction or limit at a collider that depends on trigger or selection efficiencies, tag-and-probe or data-to-simulation scale factors, integrated luminosity, or the modelling of pile-up
version: "0.1"
---

# Trigger, selection efficiency and luminosity

At a collider, a cross section, rate or limit is a count of selected events divided by the efficiency of the trigger and selection and by the integrated luminosity. Trigger and selection efficiencies are measured with reference samples, often by the tag-and-probe method (a well-identified "tag" object selects an unbiased "probe" object), the luminosity scale is set by van der Meer (vdM) beam-separation scans, and both are affected by pile-up (additional collisions in the same or nearby bunch crossings).

## 1. Reference sample for trigger efficiency

**Question.** How was each trigger efficiency measured (tag-and-probe, a lower-threshold "bootstrap" trigger, or an independent reference trigger), and does the paper show that the reference selection is independent of the trigger being measured, or correct for any correlation between them?

**Why it matters.** An efficiency measured on events selected by another trigger equals the true efficiency only if the two selections are independent. Shared hardware, shared trigger elements or physically linked variables make them correlated, and the measured efficiency is then biased. The probability that the reference fires given the studied trigger cannot be measured from those data alone.

**Resolved by.** The method named for each trigger, with the reference trigger and offline selection stated; an argument or a check, for example in simulation, that the reference does not share inputs with the trigger under study; where it does, a correction using conditional efficiencies with its uncertainty; efficiencies measured relative to offline-selected objects, with the data-to-simulation ratio applied as a correction factor.

**Benchmark.** [1], [2], [3]

## 2. Turn-on, plateau and prescales

**Question.** Are the offline thresholds placed on the efficiency plateau of each trigger, is the efficiency parametrised in the variables that actually drive the trigger response, and are prescales accounted for in the event weights?

**Why it matters.** Near threshold the efficiency rises steeply, so small differences between online and offline energy scales or between data and simulation produce large corrections. Efficiency depends on event kinematics and topology, so a value averaged over one sample does not transfer to a sample with different kinematics. Prescales that change during data taking change the effective luminosity of a trigger, and very small efficiencies give large event weights.

**Resolved by.** Turn-on curves in data and simulation against the offline variable, with the offline threshold shown to lie where the efficiency has reached its plateau; efficiencies binned in the variables that govern the trigger, such as transverse momentum and pseudorapidity, and in regions of reduced coverage; prescale factors included in the weights or the effective luminosity of prescaled triggers stated; regions of very low efficiency excluded or handled explicitly.

**Benchmark.** [1], [2]

## 3. Tag-and-probe selection and background

**Question.** For each tag-and-probe measurement, does the paper state the tag selection, the mass window and how the background under the probe sample was estimated and subtracted, and does it show how the efficiency changes when these choices are varied?

**Why it matters.** The probe sample contains background as well as the resonance decays it is meant to select, and the efficiency is computed after subtracting it. The answer depends on the tag requirements, the mass window, the sideband ranges and the background template. A probe requirement that is too tight can bias the very quantity being measured.

**Resolved by.** The tag and probe definitions given, with the probe left loose in the quantity under study; the background estimate described, for example sideband fits, same-charge events or templates from inverted selections; the systematic uncertainty taken from the spread of results under variations of the tag selection, mass window, sidebands, templates and fit model; efficiencies and data-to-simulation scale factors shown in two-dimensional bins of the relevant kinematic variables.

**Benchmark.** [2], [4]

## 4. Uncertainty of efficiencies and use of scale factors

**Question.** How were the statistical uncertainties of efficiencies near zero or one computed, and are the data-to-simulation scale factors applied in the same kinematic bins in which they were measured, with their uncertainties propagated?

**Why it matters.** The simple binomial error is zero when every or no event passes and gives intervals that can extend beyond zero or one. Efficiencies computed from events with non-integer weights cannot be assumed to follow the binomial model. Scale factors derived from a resonance sample apply to a signal only to the extent that they are binned in the variables on which the efficiency depends.

**Resolved by.** Intervals with known coverage, such as Clopper-Pearson, Wilson or Bayesian intervals with a stated prior, especially in bins with few events or efficiencies near one; efficiencies measured on unit-weight samples; scale factors applied per object in the bins used to measure them, and the remaining kinematic difference between calibration and signal samples addressed; the scale-factor uncertainty propagated into the final result.

**Benchmark.** [1], [3], [4]

## 5. Combinations of triggers

**Question.** Where events are accepted by more than one trigger, or by triggers whose prescales differ or change over the data-taking period, does the paper state how the phase space was divided between triggers or how events were weighted, and how the efficiency of the combination was obtained?

**Why it matters.** The efficiency of a logical OR of triggers follows from the individual efficiencies only if they are independent, and triggers that share elements or respond to related quantities are not. A single efficiency measured for the whole combination is tied to the selection in which it was measured and has to be redetermined when the selection changes. Weights for combined prescaled triggers that assume independent prescaling are wrong where prescaling is deterministic and triggers are nearly identical.

**Resolved by.** The method stated: a division of phase space so that each region uses one trigger, or event weights built from the prescales and efficiencies of every trigger that could have accepted the event; efficiencies of the individual triggers measured as functions of the relevant variables, with conditional efficiencies where triggers are correlated; the independence of prescaling checked, or the raw trigger decisions used, where several prescaled triggers are combined.

**Benchmark.** [1]

## 6. Absolute luminosity calibration

**Question.** Is the integrated luminosity and its uncertainty taken from a stated calibration for the data set used, and, where the paper derives the calibration itself, are the beam-separation scans and their systematic corrections described?

**Why it matters.** The luminosity uncertainty is often one of the leading uncertainties in a cross-section measurement. The vdM calibration depends on the measured bunch populations, including ghost and satellite charge, on beam orbit drift and position jitter during the scan, on the length scale of the beam displacement, on beam-beam effects and on whether the transverse beam profiles factorise in x and y. Each needs a correction or an uncertainty, and single corrections can reach about one per cent.

**Resolved by.** The luminosity and its uncertainty quoted with the reference that determined it, for the same data set and data-quality selection; where the calibration is new, the scan conditions, the fit model and each correction stated with its uncertainty, and a table of contributions to the total; reproducibility between scans shown.

**Benchmark.** [5], [6]

## 7. Transfer to physics running, stability and correlations

**Question.** How was the calibration carried from the low pile-up vdM fills to physics running, how was the stability of the luminosity scale over the data-taking period checked, and are the luminosity uncertainties of different years combined with their correlations?

**Why it matters.** A luminometer calibrated at low pile-up with isolated bunches can respond non-linearly at high pile-up and within bunch trains, and its response can drift with radiation damage, activation or detector problems over a year. When several years are combined, some uncertainty components are correlated and others are not, and treating them all one way misstates the total.

**Resolved by.** Comparisons between independent luminometers as a function of pile-up and over time, with any non-linearity corrected and a calibration-transfer and a stability uncertainty assigned; out-of-time and afterglow corrections described where they apply; the correlations between years stated, or a covariance given, and used when data sets are combined; where available, an independent cross-check such as counting Z-boson decays.

**Benchmark.** [5], [6]

## 8. Pile-up modelling and dependence

**Question.** Does the paper state how the distribution of interactions per bunch crossing in data was obtained and matched in simulation, and does it show that efficiencies, isolation and missing transverse momentum behave the same in data and simulation as a function of pile-up?

**Why it matters.** The number of interactions per crossing in data is computed from the per-bunch luminosity and an assumed inelastic cross section, and simulated events are reweighted to match it, so the assumed cross section enters every reweighted quantity. Pile-up degrades jet and missing transverse momentum resolution, adds energy to isolation sums and changes trigger and identification efficiencies, and these effects are not always reproduced by simulation.

**Resolved by.** The assumed inelastic cross section and the reweighting procedure stated, with the effect of varying them on the result; distributions of the number of reconstructed vertices compared between data and simulation; key efficiencies and resolutions shown as functions of the number of vertices or interactions in data and simulation; the pile-up mitigation method named.

**Benchmark.** [7], [2], [4], [6]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | V. Lendermann, J. Haller, M. Herbst, K. Krüger, H.-C. Schultz-Coulon and R. Stamen, Combining triggers in HEP data analysis, Nucl. Instrum. Meth. A 604, 707–718 (2009); read as arXiv:0901.4118 | doi:10.1016/j.nima.2009.03.173 | full text | Sec. 2: efficiency from a sample collected by a reference trigger using independent information, binned in event parameters and fitted. Sec. 4.3.1: technical or kinematic correlations between trigger efficiencies; efficiencies can be made independent by choosing the right kinematic variables. Sec. 3: weights of downscale factor over efficiency, run-averaged when downscale factors vary between runs. Sec. 4.3.2: using a trigger where its efficiency is very small gives large weights. Secs. 4.1 to 4.3.4: division, exclusion and inclusion methods for combining triggers; a global efficiency for a combination is not universal; conditional efficiencies for correlated triggers; independent downscaling fails for deterministic downscaling of near-identical triggers. Sec. 6: store raw trigger bits |
| 2 | ATLAS Collaboration (M. Aaboud et al.), Performance of the ATLAS trigger system in 2015, Eur. Phys. J. C 77, 317 (2017); read as arXiv:1611.09661 | doi:10.1140/epjc/s10052-017-4852-3 | full text | Sec. 6 opening: tag-and-probe and bootstrap give unbiased efficiencies, measured against offline-selected objects, with the data-to-simulation ratio used as a correction factor. Sec. 6.2.3 and Fig. 26: offline threshold above the trigger threshold, sharp turn-on, losses in the barrel/end-cap transition. Sec. 6.3.3: reduced muon trigger acceptance in some sectors. Sec. 4.3: prescales changed during a run. Sec. 6.5.3: tau tag-and-probe with background subtracted and its uncertainty taken as a systematic uncertainty. Sec. 6.6.3: missing transverse momentum trigger efficiency degrades with the number of vertices |
| 3 | D. Casadei, Estimating the selection efficiency, JINST 7, P08021 (2012); read as arXiv:0908.0130 | doi:10.1088/1748-0221/7/08/P08021 | full text | Sec. 2: the binomial variance vanishes when all or no events pass and its intervals can leave [0, 1]; Clopper-Pearson, Wilson and Bayesian reference intervals compared; footnote: histograms must be filled with unit weights. Sec. 4: only integer weights reduce to the binomial scheme. Sec. 4.3: trigger efficiency from a sample selected by another trigger needs the probability of the reference given the studied trigger, which cannot be estimated from real data alone |
| 4 | ATLAS Collaboration (M. Aaboud et al.), Electron reconstruction and identification in the ATLAS experiment using the 2015 and 2016 LHC proton–proton collision data at √s = 13 TeV, Eur. Phys. J. C 79, 639 (2019); read as arXiv:1902.04655 | doi:10.1140/epjc/s10052-019-7140-6 | full text | Sec. 4: tag-and-probe with Z and J/ψ decays; scale factor as the ratio of data to simulated efficiency applied as a weight. Sec. 4.2: probe isolation kept very loose so as not to bias the measurement. Sec. 4.1: background from sideband fits, same-charge events and templates from inverted selections; systematic uncertainty from variations of tag selection, mass window, sidebands, templates and background subtraction. Sec. 5.3: measurements binned in two dimensions. Sec. 6.3: identification adjusted with the number of primary vertices to limit pile-up dependence |
| 5 | ATLAS Collaboration (G. Aad et al.), Luminosity determination in pp collisions at √s = 13 TeV using the ATLAS detector at the LHC, Eur. Phys. J. C 83, 982 (2023); read as arXiv:2212.09379 | doi:10.1140/epjc/s10052-023-11747-w | full text | Sec. 1: luminosity uncertainty often one of the leading uncertainties in cross sections. Secs. 4.4 to 4.10: vdM corrections for bunch population, ghost and satellite charge, orbit drift, non-factorisation, beam-beam effects, emittance growth, length scale and magnetic non-linearity. Sec. 4.11: scan-to-scan reproducibility. Sec. 5.1: luminometer non-linearity with pile-up and with bunch-train position. Secs. 6 and 7: calibration-transfer uncertainty and long-term stability uncertainty from comparisons between luminometers. Secs. 8.1 and 8.2: correlations between years and a covariance for combinations. Sec. 8.3: comparison with Z-boson counting |
| 6 | CMS Collaboration (A. M. Sirunyan et al.), Precision luminosity measurement in proton-proton collisions at √s = 13 TeV in 2015 and 2016 at CMS, Eur. Phys. J. C 81, 800 (2021); read as arXiv:2104.01927 | doi:10.1140/epjc/s10052-021-09538-2 | full text | Sec. 1: luminosity uncertainty often dominant in electroweak and top-pair cross sections; an assumed inelastic cross section relates luminosity and pile-up. Secs. 4.3 and 4.4: beam current, spurious charge, orbit drift, beam-beam, length-scale and factorisation corrections with uncertainties, single corrections of about one per cent. Sec. 5: out-of-time pile-up and afterglow corrections. Secs. 6 and 7: cross-detector stability and linearity uncertainties; table of normalisation and integration uncertainties marked as correlated or uncorrelated between years |
| 7 | CMS Collaboration (A. M. Sirunyan et al.), Pileup mitigation at CMS in 13 TeV data, JINST 15, P09018 (2020); read as arXiv:2003.00503 | doi:10.1088/1748-0221/15/09/P09018 | full text | Sec. 3: number of interactions in data computed from luminosity and an assumed inelastic cross section; simulation reweighted to reproduce that distribution. Sec. 4: CHS and PUPPI mitigation methods. Secs. 4.1 and 5.3: data-to-simulation differences in pile-up-dominated regions; uncertainty in the number of interactions shown. Secs. 5, 7 and 8: pile-up effects on jet and missing transverse momentum resolution and on isolation, shown against the number of vertices or interactions |
