---
id: T-DOUBLE-BETA-DECAY
name: Neutrinoless double-beta decay searches
type: technique
field: physics/nuclear
applies_when: the paper searches for neutrinoless double-beta decay and reports a half-life limit or signal, a background index, energy resolution or region of interest at the decay energy, an exposure, a sensitivity or projected sensitivity, or an effective Majorana neutrino mass
version: "0.1"
---

# Neutrinoless double-beta decay searches

## 1. Exposure and signal efficiency

**Question.** Is the exposure given as mass of the double-beta isotope times live time, and are the isotopic fraction, the active or fiducial fraction, and the signal efficiency (full containment of both electrons, every event selection cut, and the fraction of the peak inside the ROI) each stated with an uncertainty?

**Why it matters.** The half-life limit scales with the number of isotope nuclei watched times the probability that a decay is recorded in the ROI. Detection efficiency ranges from about 30% in external-source designs, through 70-95% containment in solid detectors, to nearly 100% containment in large liquid detectors, and selection cuts remove further signal, so an exposure quoted in detector mass or before cuts overstates what was searched.

**Resolved by.** Isotope mass, enrichment, active fraction, live time and each efficiency factor listed separately with uncertainties, and combined into one effective exposure that is the one used in the half-life calculation; cut efficiencies measured with calibration sources or 2νββ events and compared with simulation.

**Benchmark.** [2], [3], [4]

## 2. Energy scale, resolution and peak shape at Qββ

**Question.** How was the energy scale calibrated near Qββ, what are the resolution and peak shape at Qββ and how stable were they over the data-taking period, and how much 2νββ continuum and how many nearby gamma lines fall in or near the ROI at that resolution?

**Why it matters.** The signal is expected at a known energy, so a shift of the energy scale or a broader peak than assumed moves signal out of the ROI and lets more background in. The 2νββ continuum ends at Qββ and its leakage into the ROI falls steeply as the resolution improves, and for some isotopes a gamma line from natural radioactivity lies within about 10 keV of Qββ.

**Resolved by.** Calibration lines that bracket Qββ, with the residual of the energy scale at Qββ and the resolution there interpolated and quoted with uncertainties; calibrations repeated through the run, with the stability of scale and resolution shown; the expected 2νββ and gamma-line contributions in the ROI computed at the measured resolution and included in the background model.

**Benchmark.** [1], [2], [4]

## 3. Region of interest and background index

**Question.** How was the ROI chosen (its width relative to the resolution, and whether it was fixed before the data in it were seen), and is the background index stated with its units, the mass it is normalised to (detector or isotope), and the cuts applied before it was computed?

**Why it matters.** The number of background counts expected in the ROI is what limits the half-life reach, and the best ROI width depends on both background and resolution. A background index per keV per kilogram of detector, before cuts, is not comparable with one per kilogram of isotope after all cuts, and in large homogeneous detectors the background varies with position so that a single index describes the experiment poorly.

**Resolved by.** The ROI and the rule that set it stated in advance; the background index given in counts per keV, per kilogram of a named mass, per year, after named cuts, together with the expected background count in the ROI for the quoted exposure; for position-dependent backgrounds, the background shown as a function of fiducial volume or the expected count in the region actually analysed.

**Benchmark.** [1], [3], [4]

## 4. Background model near Qββ

**Question.** Which background sources contribute near Qββ (gamma rays and betas from the thorium and uranium chains, surface alpha emitters, radon, cosmogenic activation, muon-induced events, neutrino interactions, 2νββ), and is the contribution of each constrained by data independent of the ROI, such as material screening, sideband energies, multi-site events or calibration with known sources?

**Why it matters.** The expected background in the ROI is usually inferred from a model, not measured there, so an unconstrained or missing component changes both the limit and any apparent excess. The dominant sources differ between detector technologies, and a reliable assay of trace contamination at the levels now reached is itself hard.

**Resolved by.** A list of background components with their activities from screening, and the fit or extrapolation that carries them into the ROI; the model checked against energy regions and event classes outside the ROI; the background in the ROI predicted before unblinding and compared with what was observed.

**Benchmark.** [1], [2], [4], [5]

## 5. Blinding of the region of interest

**Question.** Was the ROI hidden while event selection, energy calibration, the background model and the statistical procedure were developed, and does the paper say which, if any, of these changed after the data in the ROI were seen?

**Why it matters.** In a rare-event search a few counts decide the result. Choosing cuts or calibrations with the signal region in view, for example to remove a few background-like events or to enhance a small excess, biases the half-life limit or the significance by an amount comparable with the statistical uncertainty.

**Resolved by.** A blinded window wider than the final ROI, so that the final ROI is also chosen blind; a statement of what was fixed before unblinding; any change after unblinding reported together with the result it would have given otherwise.

**Benchmark.** [5]

## 6. Statistical method for the half-life limit

**Question.** Which statistical procedure turns the observed counts into the half-life limit (frequentist with which ordering, Bayesian with which prior), how are systematic uncertainties included, and how does the quoted limit behave when fewer events are seen than the background predicts?

**Why it matters.** With a handful of counts, limits from different procedures applied to the same data can differ by about a factor of two. A frequentist limit can become stronger, and can exclude half-lives the experiment had little power to probe, when the background fluctuates downwards, while a Bayesian limit depends on the prior.

**Resolved by.** The method, ordering or prior, and the treatment of nuisance parameters stated and fixed in advance; the observed limit given alongside the expected limit (the sensitivity) and its spread; where the observed limit is much stronger than the sensitivity, the paper says so; the likelihood or the counts and expected backgrounds published so others can recompute the limit.

**Benchmark.** [6], [7], [8]

## 7. Sensitivity and projected sensitivity

**Question.** When the paper quotes a sensitivity, or projects one for a future experiment, does it define it (median limit expected without signal, or half-life for a given chance of a discovery at stated significance), and state the exposure, background and efficiency assumed and whether the experiment is background-free or background-limited?

**Why it matters.** Without background the half-life reach grows linearly with exposure, but with background it grows only as the square root of exposure divided by background and resolution, so the regime assumed controls a projection. Exclusion and discovery sensitivities are different numbers, and a sensitivity quoted without its definition and inputs cannot be compared with others.

**Resolved by.** The definition and confidence level stated; the effective exposure and the background expected in the ROI given as the inputs; the regime identified, with the background count in the ROI over the full exposure; for projections, the assumed background and efficiency justified by measurements, and a sensitivity computed with the same method used for the observed limit.

**Benchmark.** [1], [3], [4], [6]

## 8. Conversion to an effective Majorana mass

**Question.** When a half-life limit is converted to a limit on mββ, does the paper state the decay mechanism assumed, the phase-space factor, the nuclear matrix elements and the axial coupling used, and quote a range across matrix element calculations instead of one value?

**Why it matters.** The conversion assumes exchange of light Majorana neutrinos and needs a nuclear matrix element that cannot be measured. Calculations from different nuclear models differ by a factor of two to three, and the possible quenching of the axial coupling adds further uncertainty, so the mββ limit inherits a spread of about a factor of three that is unrelated to the experiment.

**Resolved by.** The mechanism, phase-space factor and its source, and the set of matrix elements with their references and axial-coupling values stated; mββ given as a range spanning the matrix elements; the half-life limit kept as the primary result.

**Benchmark.** [1], [2], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. J. Dolinski et al., Neutrinoless double-beta decay: status and prospects, Annu. Rev. Nucl. Part. Sci. 69, 219 (2019); read as preprint arXiv:1902.04097 | doi:10.1146/annurev-nucl-101918-023407 |
| 2 | M. Agostini et al., Toward the discovery of matter creation with neutrinoless ββ decay, Rev. Mod. Phys. 95, 025002 (2023); read as preprint arXiv:2202.01787 (Secs. I to V.3) | doi:10.1103/RevModPhys.95.025002 |
| 3 | M. Agostini et al., Discovery probability of next-generation neutrinoless double-β decay experiments, Phys. Rev. D 96, 053001 (2017); read as preprint arXiv:1705.02996 | doi:10.1103/PhysRevD.96.053001 |
| 4 | O. Cremonesi and M. Pavan, Challenges in double beta decay, Adv. High Energy Phys. 2014, 951432 (2014); read as preprint arXiv:1310.4692 | doi:10.1155/2014/951432 |
| 5 | A. Roodman, Blind analysis in particle physics, in Proceedings of PHYSTAT2003, eConf C030908, TUIT001 (2003); read as arXiv:physics/0312102 | doi:10.48550/arXiv.physics/0312102 |
| 6 | G. J. Feldman and R. D. Cousins, Unified approach to the classical statistical analysis of small signals, Phys. Rev. D 57, 3873 (1998); read as preprint arXiv:physics/9711021 | doi:10.1103/PhysRevD.57.3873 |
| 7 | S. D. Biller and S. M. Oser, Another look at confidence intervals: proposal for a more relevant and transparent approach, Nucl. Instrum. Methods A 774, 103 (2015); read as preprint arXiv:1405.5010 | doi:10.1016/j.nima.2014.11.081 |
| 8 | G. Cowan et al., Power-constrained limits, arXiv:1105.3166 (2011) | doi:10.48550/arXiv.1105.3166 |
| 9 | J. Engel and J. Menéndez, Status and future of nuclear matrix elements for neutrinoless double-beta decay: a review, Rep. Prog. Phys. 80, 046301 (2017); read as preprint arXiv:1610.06548 | doi:10.1088/1361-6633/aa5bc5 |
