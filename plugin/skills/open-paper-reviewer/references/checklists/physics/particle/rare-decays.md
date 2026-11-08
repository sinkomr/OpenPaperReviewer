---
id: T-RARE-DECAYS
name: Rare decays and lepton-flavour violation
type: technique
field: physics/particle
applies_when: the paper measures the branching fraction of a rare decay or sets a limit on a forbidden one, including lepton-flavour-violating decays and muon-to-electron conversion, using a normalisation channel or a count of produced particles and a background estimate in a signal window
version: "0.1"
---

# Rare decays and lepton-flavour violation

## 1. Normalisation channel and ratio of efficiencies

**Question.** Which normalisation channel, or which count of produced or stopped particles, converts the signal yield into a branching fraction, and how similar are the signal and normalisation selections in trigger, topology and kinematics?

**Why it matters.** Measuring relative to a well-known decay removes the need to know how many parent particles were produced, and with it the production cross section and luminosity, and lets selection effects common to both channels cancel. The cancellation is only as good as the similarity of the two channels: different triggers, numbers of tracks, particle identification or momentum spectra leave efficiency ratios that rest on simulation.

**Resolved by.** The normalisation formula written out, with each factor and its uncertainty, and the single-event sensitivity given; a normalisation channel chosen to share the trigger and as much of the selection as possible; the residual efficiency differences evaluated with data-driven corrections; where two normalisation channels are available, the ratio of their yields compared with the known ratio of their branching fractions as a cross-check.

**Benchmark.** [1], [4]

## 2. External inputs to the normalisation

**Question.** Which external inputs enter the branching fraction (the normalisation channel's branching fraction, production fractions of different hadron species, cross sections, luminosity, or the number of stopped muons), what values were used, and does the quoted uncertainty include theirs?

**Why it matters.** When the signal and normalisation decays come from different hadron species, the ratio of their production fractions enters directly, and this ratio depends on transverse momentum and collision energy. It and the normalisation branching fraction can be the largest systematic uncertainties in the result. At lepton colliders and muon facilities the count of produced taus or stopped muons plays the same role, and the single-event sensitivity scales inversely with it.

**Resolved by.** Each external input given with its value, source and uncertainty, propagated into the result and listed separately so the result can be updated when the input improves; production fractions taken at the kinematics and energy of the analysis; the number of produced or stopped particles derived from a stated luminosity and cross section or from an independent beam monitor, with the single-event sensitivity quoted.

**Benchmark.** [1], [2], [3], [4]

## 3. Peaking backgrounds from misidentified and partially reconstructed decays

**Question.** Which known decays can produce candidates inside or next to the signal window, through hadrons misidentified as leptons, missing particles or wrong mass assignments, and how was each of these contributions estimated?

**Why it matters.** Decays much more common than the signal, such as two-body hadronic decays with both hadrons misidentified, or semileptonic and partially reconstructed decays, can form a peak close to the signal mass that a smooth background model does not absorb. Their rate is the product of a large branching fraction and a small misidentification probability, so a modest error in that probability changes the expected background considerably.

**Resolved by.** A list of the exclusive backgrounds considered, with the expected yield of each in the signal window; misidentification rates measured in data with calibration samples, not taken from simulation alone; the estimate checked in a region enriched in misidentified candidates; specific vetoes stated with their effect on the signal efficiency; the shape of each peaking component included in the fit.

**Benchmark.** [1]

## 4. Combinatorial and accidental background in the signal region

**Question.** How was the background from random combinations or accidental coincidences in the signal region estimated, from which sidebands or control samples, and with what assumption about its shape when extrapolated into the signal window?

**Why it matters.** The expected background in a narrow window is usually extrapolated from sidebands, assuming a shape such as a flat or linear distribution. Selection variables that are correlated with mass or decay time can sculpt that shape. Where several uncorrelated particles can mimic the signal, as in muon LFV searches, the accidental background grows with the square or higher power of the beam rate and depends strongly on the resolutions.

**Resolved by.** The sideband or control regions defined and shown; the assumed shape justified and an alternative shape tried; the classifier or selection shown not to sculpt the background in the variable that defines the signal window; for coincidence experiments, the accidental rate measured with time or energy sidebands and the prompt (correlated) background estimated separately, for example by extrapolation from a region where it dominates.

**Benchmark.** [1], [3], [4]

## 5. Signal window, mass scale, resolution and radiation

**Question.** How were the position and width of the signal window set, and how were the mass or energy scale, the resolution and its non-Gaussian tails, and losses from final-state radiation determined?

**Why it matters.** The signal window is set from the expected resolution, so an error in the mass scale or the width moves signal out of the window or background into it. Real resolution functions have long non-Gaussian tails, and photon radiation from the final-state leptons shifts candidates to lower mass by an amount that depends on the mass cut; the corrections for this can reach about ten per cent of a rate.

**Resolved by.** The mass or energy scale and resolution calibrated with known resonances or physical processes near the signal region, with any interpolation stated; the tails modelled and the fraction of signal outside the window given; the treatment of final-state radiation in the simulation stated and checked; the effect of the window definition on the efficiency included in the uncertainty.

**Benchmark.** [1], [4], [6]

## 6. Dependence of the efficiency on the assumed signal model

**Question.** What decay distribution or lifetime was assumed in the simulation used to compute the signal efficiency, and how much does the efficiency, and with it the branching fraction or limit, change for other plausible assumptions?

**Why it matters.** The efficiency depends on where the signal sits in phase space and in decay time. Limits on lepton-flavour-violating three-body decays are often computed for a phase-space distribution, while different new-physics operators give different distributions. For neutral mesons with a width difference between mass eigenstates, a selection on decay time makes the efficiency depend on the assumed effective lifetime, which can shift the branching fraction by several per cent.

**Resolved by.** The signal model stated; the efficiency given for alternative decay distributions or for the extremes of the allowed lifetime, or a model uncertainty included; where the dependence is large, results or efficiency maps provided for several models so that others can reinterpret them.

**Benchmark.** [1], [3], [5], [7]

## 7. Definition of the reported quantity

**Question.** Does the paper state exactly what quantity it reports (time-integrated or at zero decay time, averaged over charge-conjugate modes, including or excluding final-state radiation, or normalised to the muon capture rate in a named nucleus), and is the comparison with predictions or earlier results made for the same quantity?

**Why it matters.** Rare-decay results are compared with predictions at the level of a few per cent or with limits from other experiments, so a mismatch in definition matters. For neutral mesons the untagged, time-integrated branching fraction can differ from the one defined at zero decay time by about ten per cent, and muon-to-electron conversion rates depend on the target nucleus.

**Resolved by.** The measured quantity defined in words or by a formula; any conversion to the quantity predicted by theory stated, with its inputs; for conversion searches, the target nucleus and the normalisation named; comparisons drawn only between results with the same definition.

**Benchmark.** [1], [4], [6], [7]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | K.-F. Chen et al., Analysis of B(s)0 → μ+μ− decays at the Large Hadron Collider, Symmetry 16, 251 (2024); read as arXiv:2402.09901 | doi:10.3390/sym16020251 |
| 2 | R. Aaij et al. (LHCb collaboration), A precise measurement of the fs/fd fragmentation-fraction ratio and of B0s decay branching fractions, Phys. Rev. D 104, 032005 (2021); read as arXiv:2103.06810 | doi:10.1103/PhysRevD.104.032005 |
| 3 | K. Hayasaka et al. (Belle collaboration), Search for lepton flavor violating τ decays into three leptons with 719 million produced τ+τ− pairs, Phys. Lett. B 687, 139 (2010); read as arXiv:1001.3221 | doi:10.1016/j.physletb.2010.03.037 |
| 4 | L. Calibbi and G. Signorelli, Charged lepton flavour violation: an experimental and theoretical introduction, Riv. Nuovo Cimento 41, 71 (2018); read as arXiv:1709.00294 | doi:10.1393/ncr/i2018-10144-0 |
| 5 | B. M. Dassinger et al., Model-independent analysis of lepton flavour violating tau decays, J. High Energy Phys. 10, 039 (2007); read as arXiv:0707.0988 | doi:10.1088/1126-6708/2007/10/039 |
| 6 | M. Bordone et al., On the Standard Model predictions for RK and RK*, Eur. Phys. J. C 76, 440 (2016); read as arXiv:1605.07633 | doi:10.1140/epjc/s10052-016-4274-7 |
| 7 | K. De Bruyn et al., Branching ratio measurements of Bs decays, Phys. Rev. D 86, 014027 (2012); read as arXiv:1204.1735 | doi:10.1103/PhysRevD.86.014027 |
