---
id: T-DOUBLE-BETA-DECAY
name: Neutrinoless double-beta decay searches
type: technique
field: physics/nuclear
applies_when: the paper searches for neutrinoless double-beta decay and reports a half-life limit or signal, a background index, energy resolution or region of interest at the decay energy, an exposure, a sensitivity or projected sensitivity, or an effective Majorana neutrino mass
version: "0.1"
---

# Neutrinoless double-beta decay searches

Neutrinoless double-beta (0νββ) decay searches are used to claim a lower limit on, or a measurement of, the half-life of a nucleus that emits two electrons and no neutrinos, and from it a limit on the effective Majorana neutrino mass (mββ). The claim rests on counting events in a narrow region of interest (ROI) around the decay energy (Qββ), where the signal is a peak whose width is the energy resolution (full width at half maximum, FWHM), against a background that includes the continuum from ordinary two-neutrino double-beta (2νββ) decay.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. J. Dolinski, A. W. P. Poon and W. Rodejohann, Neutrinoless double-beta decay: status and prospects, Annu. Rev. Nucl. Part. Sci. 69, 219–251 (2019); read as preprint arXiv:1902.04097 | doi:10.1146/annurev-nucl-101918-023407 | full text | Sec. 4, Eqs. 13 and 14: half-life sensitivity scales linearly with exposure without background and as the square root of mass times time over background index times resolution with background; background index per keV, kg and year. Sec. 4.1, Eq. 15: signal-to-2νββ ratio grows as the sixth power of Qββ over resolution; the 2615 keV thallium-208 line and betas from the radon daughter bismuth-214 as backgrounds. Secs. 4.2 and 5.1.3: indices also quoted per FWHM per tonne per year. Sec. 5 intro, Fig. 5 caption: large detectors are not well characterized by a single index. Sec. 3.2 with Fig. 4: matrix element calculations compiled, their uncertainties hard to quantify. Sec. 3.3: quenching of the axial coupling could lengthen the half-life by a factor of 2 to 3 and has no settled theory |
| 2 | M. Agostini, G. Benato, J. A. Detwiler, J. Menéndez and F. Vissani, Toward the discovery of matter creation with neutrinoless ββ decay, Rev. Mod. Phys. 95, 025002 (2023); read as preprint arXiv:2202.01787 (Secs. I to V.3) | doi:10.1103/RevModPhys.95.025002 | full text | Sec. V intro: sensitivity depends critically on the background rate, with an advantage for experiments near the background-free regime. Sec. V.2: the signal is a peak at Qββ on the 2νββ continuum, events count only when fully contained, and a fully calibrated energy response is needed; Sec. V.2.1: containment from 70-95% in solid detectors to near 100% in large liquid detectors; low efficiency in composite designs. Sec. V.3: the signal can be mimicked by cosmic-ray induced processes, decay-chain and anthropogenic isotopes, neutrinos and 2νββ. Sec. IV intro and IV.4: axial-coupling quenching is one of the main theoretical uncertainties. Secs. IV.3.1 and IV.5.1: matrix elements spread by about a factor of three across methods, and two variants of one method that describe the nuclei well predict values a factor of three apart |
| 3 | M. Agostini, G. Benato and J. A. Detwiler, Discovery probability of next-generation neutrinoless double-β decay experiments, Phys. Rev. D 96, 053001 (2017); read as preprint arXiv:1705.02996 | doi:10.1103/PhysRevD.96.053001 | full text | Sec. III, Eq. 5 and Table 1: sensitive exposure is isotope mass times live time scaled by active fraction, signal efficiency and the fraction of signal in the ROI; sensitive background is the count in the ROI after all cuts divided by that exposure; discovery sensitivity defined as a 50% chance of a signal at 3σ. App. B: background-free when the expected count is below about 0.0027; the optimal ROI depends on background and resolution. Sec. II: observed limits strengthened by background under-fluctuations, so sensitivities were used instead |
| 4 | O. Cremonesi and M. Pavan, Challenges in double beta decay, Adv. High Energy Phys. 2014, 951432 (2014); read as preprint arXiv:1310.4692 | doi:10.1155/2014/951432 | full text | Sec. 4.1, Eqs. 7 to 10: sensitivity as the half-life hidden by background fluctuations, proportional to efficiency and isotopic abundance; square-root scaling with background, linear scaling and no dependence on resolution without background; integration window customarily one FWHM; index normalised to isotope mass. Sec. 4.2: thallium-208 and bismuth-214 lines, surface alphas, cosmogenic activation and muons as backgrounds; screening at the required levels is an open problem. Sec. 5: external-source efficiencies of order 30%. Sec. 5 with Fig. 6: 2νββ fraction in a one-FWHM window against resolution. Sec. 7.1: the bismuth-214 line lies within 10 keV of Qββ for xenon-136. Sec. 7.2: periodic calibration, multi-site events used to constrain background components |
| 5 | A. Roodman, Blind analysis in particle physics, in Proceedings of PHYSTAT2003, eConf C030908, TUIT001 (2003); read as arXiv:physics/0312102 | doi:10.48550/arXiv.physics/0312102 | full text | Sec. II: choosing cuts with knowledge of the result can bias it by about the statistical error, including removing a few background-like events to lower a limit or boosting a small signal. Sec. III.1: the hidden signal box for rare searches, with method, cuts and background estimates fixed before opening; the box drawn larger than the final signal region so that final cuts are chosen blind. Sec. IV: review before unblinding |
| 6 | G. J. Feldman and R. D. Cousins, Unified approach to the classical statistical analysis of small signals, Phys. Rev. D 57, 3873–3889 (1998); read as preprint arXiv:physics/9711021 | doi:10.1103/PhysRevD.57.3873 | full text | Sec. VI: sensitivity defined as the average upper limit from an ensemble of experiments with the expected background and no signal; an experiment seeing fewer events than the background should report this sensitivity with its limit, since it gets a lower limit than one seeing the expected background. Sec. III.1: choosing between an upper limit and a two-sided interval after seeing the data undercovers |
| 7 | S. D. Biller and S. M. Oser, Another look at confidence intervals: proposal for a more relevant and transparent approach, Nucl. Instrum. Methods A 774, 103–119 (2015); read as preprint arXiv:1405.5010 | doi:10.1016/j.nima.2014.11.081 | full text | Secs. II.3 and III.3: limits from data below the expected background can suggest a model bound that is not one; Sec. V.4: for a double-beta search, frequentist and Bayesian limits differed by about a factor of two, and frequentist bounds weakened with more exposure. Secs. IX.2 and IX.3: Bayesian limits depend on the prior, uniform in rate recommended as conservative, and the effect of the prior should be shown. Secs. IX.1 and X: publish the likelihood so that results can be combined and checked |
| 8 | G. Cowan, K. Cranmer, E. Gross and O. Vitells, Power-constrained limits, arXiv:1105.3166 (2011) | doi:10.48550/arXiv.1105.3166 | full text | Secs. 1 and 3: with probability of at least the test size, parameter values to which the test has little or no power are excluded (spurious exclusion). Sec. 5: the limit is not allowed below the value where power falls under a set minimum; Sec. 7: that minimum corresponds to data fluctuating about one standard deviation below expectation. Sec. 9: show both constrained and unconstrained limits so a reader can tell agreement with data from lack of sensitivity |
| 9 | J. Engel and J. Menéndez, Status and future of nuclear matrix elements for neutrinoless double-beta decay: a review, Rep. Prog. Phys. 80, 046301 (2017); read as preprint arXiv:1610.06548 | doi:10.1088/1361-6633/aa5bc5 | full text | Sec. II.2.1, Eq. 9: rate assumes light Majorana neutrino exchange and is the product of a phase-space factor, the squared matrix element and mββ squared. Secs. II.3 and III with Fig. 5: matrix elements from different nuclear models differ by factors of two or three; a factor of about three in a published mββ limit is due almost entirely to the matrix element; the axial-coupling renormalisation is not yet explained and its omission means the true uncertainty is larger |
