---
id: T-NEW-PARTICLE-SEARCHES
name: Searches for new particles
type: technique
field: physics/particle
applies_when: the paper searches collider data for a new particle, resonance or other signal beyond known processes, or reports an excess over an estimated background, a local or global significance, a look-elsewhere correction, or upper limits on a cross-section, coupling or mass
version: "0.1"
---

# Searches for new particles

Searches at colliders are used to claim an excess of events over the expected background, often a narrow peak (resonance) in an invariant-mass spectrum, with a stated local and global significance, or, when no excess is seen, an exclusion limit at a stated confidence level (CL) on the production cross-section, couplings or masses of a proposed particle. Both kinds of claim rest on a statistical model of signal and background, usually a profile likelihood with nuisance parameters for the systematic uncertainties.

## 1. Background model and its functional form

**Question.** How was the background shape in the signal region modelled (simulation, a parametric fit function or another smooth model), over what fit range, and does the paper show how much a different reasonable choice of model would change the fitted signal?

**Why it matters.** The true background shape is rarely known, and an ad hoc fit function chosen from several candidates can bias the fitted signal and give intervals that undercover. Such functions also fit worse as the data set grows, so terms are added without a physical basis. A model flexible enough to absorb a localised excess has no power to discover it.

**Resolved by.** The fit function or template, the fit range and the fit procedure stated, with best-fit parameters and goodness of fit; bias tests with pseudo-experiments generated from alternative background models, with and without an injected signal; the uncertainty from the choice of function included in the result, for example by treating the choice as a discrete nuisance parameter, and a stated rule for the number of parameters.

**Benchmark.** [5], [6], [10]

## 2. Backgrounds estimated from control regions

**Question.** Where a background is taken from control regions in data, what assumptions carry the estimate into the signal region, and is each assumption tested?

**Why it matters.** A control-region estimate is only as good as the bridge to the signal region: a transfer factor from simulation or an assumption, the absence of signal in the control region, and for methods that use two variables and four regions, the assumption that the background factorises in those variables. If an assumption fails, the background in the signal region is wrong while the method appears data-driven.

**Resolved by.** Each control region defined, with its expected signal contamination; the transfer factor or extrapolation and its uncertainty stated, with its source; the factorisation or other assumption checked in validation regions close to the signal region, with the agreement shown.

**Benchmark.** [7]

## 3. Look-elsewhere effect and global significance

**Question.** Over what range of masses and other signal parameters (width, channels, signal regions) was the search made, was that range fixed in advance, and does the paper quote a global significance alongside the local one and say how it was obtained?

**Why it matters.** An excess at the best-fitting mass must be judged against the chance of a similar fluctuation anywhere in the range searched. The global p-value is larger than the local one by a trial factor that grows with the effective number of independent regions in the range searched, and with every extra free parameter such as the width. The global value depends on how the search region is defined, so it means little unless that definition is stated.

**Resolved by.** The search range and every scanned parameter stated; local and global significances both quoted, with the method for the global value, for example background-only pseudo-experiments or the upcrossing and Euler-characteristic estimates calibrated on a small number of simulations; the headline claim based on the global value, or the local value clearly labelled as local.

**Benchmark.** [1], [2], [3]

## 4. Test statistic and its distribution

**Question.** Which test statistic was used for the discovery significance and for the limits, and was its distribution taken from asymptotic formulae or from pseudo-experiments, with a check that the asymptotic formulae hold for the event counts in the analysis?

**Why it matters.** The usual asymptotic distributions of the profile likelihood ratio are exact only for large samples. With an expected background of a few events they can underestimate or overestimate the significance, and the departures appear first in the far tails on which a discovery claim rests. Different test statistics, for example one- or two-sided, give different numbers from the same data.

**Resolved by.** The test statistic defined, including how negative fitted signals are treated; the method for its distribution stated; where expected backgrounds are small or the claimed significance is large, a comparison of the asymptotic result with pseudo-experiments in the relevant tail.

**Benchmark.** [4], [10]

## 5. Systematic uncertainties in the likelihood

**Question.** Which systematic uncertainties enter the likelihood as nuisance parameters, with what constraint terms, shape variations and correlations between channels, and how much does each change the significance or the limit?

**Why it matters.** Systematic effects are harder to estimate than statistical ones, and an excess that rests mainly on them is less secure: where they dominate, underestimating them by a factor of two can halve a quoted significance. Effects on the shape of a distribution depend on how templates are interpolated between their varied versions, and limited simulated samples add their own uncertainty in each bin. Theory uncertainties have no auxiliary measurement behind their constraint terms.

**Resolved by.** A table of the systematic sources with their size and treatment (normalisation only, or normalisation and shape); the constraint form and the interpolation used; correlations across channels and signal regions stated; the statistical uncertainty of simulated templates included; the effect of each major source on the result, and the size by which the systematics would have to grow to remove the claimed significance.

**Benchmark.** [3], [4], [7]

## 6. Exclusion limits and sensitivity

**Question.** By which method were the limits set (for example the CLs method, a ratio of p-values that guards against excluding signals the search cannot see, a power constraint or a Bayesian limit), and are the observed limits shown with the expected limits and their bands?

**Why it matters.** A plain frequentist limit can exclude a signal to which the experiment has little or no sensitivity when the background fluctuates low, and with many models and parameter points this happens often. The CLs method prevents it at the cost of overcoverage that varies with the signal size, and other methods differ again, so limits are comparable only when the method is stated. An observed limit much stronger than the expected one can come from a downward fluctuation of the background, not from greater sensitivity.

**Resolved by.** The limit procedure and the confidence level stated; observed limits plotted with the median expected limit and its one- and two-standard-deviation bands; any region where the observed limit is much stronger than expected discussed; where a power constraint or other remedy is used, the unconstrained limit also given.

**Benchmark.** [7], [8], [9]

## 7. Signal model assumptions and reinterpretation

**Question.** Does the paper state the assumptions of the signal model behind each limit or significance, such as the width, spin, branching fractions and reference cross-sections, and does it give the acceptance, efficiency and background information needed to apply the result to other models?

**Why it matters.** A resonance limit holds only for the width, spin and decay pattern assumed, and limits drawn as excluded regions in a two-dimensional parameter plane, or normalised to a reference cross-section that is not given, cannot be checked or reused. Limits that combine final states with fixed branching fractions are more model-dependent than limits for each final state.

**Resolved by.** Upper limits on cross-section, or cross-section times branching fraction, as a function of mass for each stated width and spin; the reference cross-sections and their source; acceptance times efficiency, cut-flows and background estimates with uncertainties for each signal region; observed and expected limits, and where possible the full likelihood, in a public repository.

**Benchmark.** [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | E. Gross and O. Vitells, Trial factors for the look elsewhere effect in high energy physics, Eur. Phys. J. C 70, 525–530 (2010); read as arXiv:1005.1891 | doi:10.1140/epjc/s10052-010-1470-8 | full text | Sec. 1: an excess must be judged against the chance of a fluctuation anywhere in the mass range. Sec. 2.1: the trial factor, the ratio of the anywhere-in-range to the fixed-mass probability, grows with the effective number of independent search regions. Secs. 2 and 3: the global p-value bounded from upcrossings counted in 100 background simulations and checked against about a million |
| 2 | O. Vitells and E. Gross, Estimating the significance of a signal in a multi-dimensional search, Astropart. Phys. 35, 230–234 (2011); read as arXiv:1105.4355 | doi:10.1016/j.astropartphys.2011.08.005 | full text | Secs. 1 and 2: scanning a continuous parameter space gives a look-elsewhere effect, and brute-force simulation for a 5 sigma claim needs of order ten million searches. Secs. 3 and 4.1: the global p-value approximated by the expected Euler characteristic, with coefficients fitted from about 20 background simulations and checked against full simulations |
| 3 | L. Lyons, Discovering the significance of 5 sigma, arXiv:1310.1284 (2013) | doi:10.48550/arXiv.1310.1284 | full text | Sec. 2, look-elsewhere bullet: global p-value larger than local; it depends on the definition of the search region, which should be fixed in advance and stated; footnote 1: a free width or shape adds to the effect. Sec. 2, systematics bullet: effects resting on systematics are less convincing; in a systematics-dominated analysis a factor-two underestimate shrinks 5 sigma to about 2.5 sigma; ask how much systematics must grow to remove the claim. Sec. 4: report local and, where relevant, global p-values |
| 4 | G. Cowan, K. Cranmer, E. Gross and O. Vitells, Asymptotic formulae for likelihood-based tests of new physics, Eur. Phys. J. C 71, 1554 (2011); read as arXiv:1007.1727 | doi:10.1140/epjc/s10052-011-1554-0 | full text | Sec. 2: nuisance parameters for background normalisation and shape handled by the profile likelihood; Secs. 2.3 and 2.4: discovery and upper-limit test statistics and their treatment of negative or large fitted signals. Sec. 5.1: at very low background the asymptotic significance is underestimated and near five background events slightly overestimated, with departures in the tails. Sec. 7: formally valid for large samples, to be checked with Monte Carlo for very small samples |
| 5 | P. D. Dauncey, M. Kenzie, N. Wardle and G. J. Davies, Handling uncertainties in background shapes: the discrete profiling method, J. Instrum. 10, P04015 (2015); read as arXiv:1408.6865 | doi:10.1088/1748-0221/10/04/P04015 | full text | Sec. 1 and Sec. 2.2: the background functional form is often unknown and its choice is a systematic uncertainty, treated as a discrete nuisance parameter. Sec. 3.3: fitting with a function other than the generating one gives large bias and undercoverage in pseudo-experiments. Secs. 4.1 and 4.3: without a penalty for the number of parameters the highest-order function always fits best and defines the result, so a penalty is applied |
| 6 | M. Frate, K. Cranmer, S. Kalia, A. Vandenberg-Rodes and D. Whiteson, Modeling smooth backgrounds and generic localized signals with Gaussian processes, arXiv:1709.05681 (2017) | doi:10.48550/arXiv.1709.05681 | full text | Secs. I and II.1: parametric background functions are ad hoc, mismatches appear as luminosity grows and terms have been added on pragmatic grounds. Sec. IV.1: goodness of fit of the ad hoc function worsens with luminosity in toy studies. Sec. IV.2: a background model flexible enough to absorb a signal has no discovery power |
| 7 | K. Cranmer, Practical statistics for the LHC, arXiv:1503.07622 (2015), lectures also published in CERN-2014-003, pp. 267–308 | doi:10.48550/arXiv.1503.07622 | full text | Secs. 2.2 and 4.2: control-region estimates rely on a transfer factor from assumption or simulation, on negligible signal in the control region, and for the four-region method on factorisation of the background. Secs. 4.1.3 to 4.1.5: systematics as nuisance parameters with constraint terms, shape variations and interpolation conventions. Sec. 4.1.6: theory uncertainties have no real auxiliary measurement behind their constraint terms. Sec. 4.1.7: per-bin uncertainty from limited simulation. Secs. 5.3 and 5.5.4: median expected limit and its one- and two-sigma bands. Sec. 5.8: plain one-sided limits can exclude arbitrarily small signals; CLs overcovers; power-constrained limits |
| 8 | T. Junk, Confidence level computation for combining searches with small statistics, Nucl. Instrum. Methods Phys. Res. A 434, 435–443 (1999); read as arXiv:hep-ex/9902006 | doi:10.1016/S0168-9002(99)00498-2 | full text | Sec. 2: after noting that the signal-plus-background confidence level alone can exclude even the background when too few events are observed, CLs is defined as its ratio to the background confidence level. Sec. 5: the false-exclusion rate falls below the nominal 5% at low signal rates. Sec. 4: systematic uncertainties on signal and background included |
| 9 | G. Cowan, K. Cranmer, E. Gross and O. Vitells, Power-constrained limits, arXiv:1105.3166 (2011) | doi:10.48550/arXiv.1105.3166 | full text | Sec. 3: spurious exclusion of parameter values to which the experiment has little or no sensitivity, frequent when many models and points are tested. Sec. 4: CLs is conservative and its overcoverage varies with the parameter and is rarely reported. Sec. 9: report both constrained and unconstrained limits |
| 10 | W. Abdallah et al. (LHC Reinterpretation Forum), Reinterpretation of LHC results for new physics: status and recommendations after Run 2, SciPost Phys. 9, 022 (2020); read as arXiv:2003.07868 | doi:10.21468/SciPostPhys.9.2.022 | full text | Sec. II.1.1: background estimates for every signal region, and for bump hunts the fit function, fit range, procedure, best-fit values and uncertainties. Secs. II.1 and II.1.6: specify the test statistic and how its distribution was obtained, by pseudo-experiments or asymptotic approximation, and quantify the difference from the asymptotic result. Sec. II.1.5: resonance limits given for assumed widths and spins; upper limits on cross-section preferred to exclusion lines; fixed branching ratios add model dependence; give reference cross-sections; observed and expected limits. Secs. II.1.3, II.1.4 and II.1.7: efficiencies, full likelihoods and cut-flows |
