---
id: T-HALF-LIVES
name: Half-life and decay measurements
type: technique
field: physics/nuclear
applies_when: the paper reports a half-life, decay constant, branching ratio or emission probability of a radionuclide or nuclear state, obtained by following a count rate over time or by counting decays, or bases a claim on such a value
version: "0.1"
---

# Half-life and decay measurements

## 1. Decay model and fitting method

**Question.** Which function was fitted to the decay curve (number of exponential components, background, daughter activity), by which method (Poisson likelihood, or least squares with which weights), over which time window, and does the paper show the residuals and a test of the procedure on simulated data?

**Why it matters.** Common least-squares variants applied to Poisson counts, especially with few counts per time bin, give biased estimates, and half-lives analysed without a maximum-likelihood treatment have been judged likely to be biased, with uncertainties that are too small. A background term or a decay component left out of the model shifts the fitted half-life without necessarily spoiling the fit.

**Resolved by.** The fitted function and every free and fixed parameter stated; a maximum-likelihood fit, or an iterated weighted least-squares fit that converges to it; residuals plotted against time; the analysis checked on Monte Carlo data that reproduce the counting conditions, including dead time.

**Benchmark.** [2], [3], [4]

## 2. Dead time, pile-up and decay during each count

**Question.** What dead time (extending or non-extending, and its length) and pile-up conditions applied, at what initial count rate, how were the losses corrected, and does the paper show that the half-life does not change when the dead time or the initial rate is changed?

**Why it matters.** Count loss from dead time and pile-up depends on the rate, which falls as the source decays, so an imperfect correction distorts the shape of the decay curve and shifts the half-life. At high rates a 10% error in the dead time gives errors of a few percent in the corrected rate; an imposed dead time does not fully remove pile-up; and a live-time correction that applies one average factor is in error when the activity changes noticeably during a single count.

**Resolved by.** The type and length of the dead time stated and measured; the initial rate and dead-time fraction given; consistent half-lives from runs with different imposed dead times and lower initial rates; for short-lived activities, corrections applied over short intervals or by loss-free counting, with decay during each count accounted for; the uncertainty of the loss correction propagated into the half-life.

**Benchmark.** [1], [2], [3]

## 3. Rate-dependent detector response

**Question.** Does the paper show that the detector efficiency does not change with count rate, for example by repeating the measurement with different detector bias, discriminator thresholds and gain settings and obtaining the same half-life?

**Why it matters.** Thresholds or gains that shift with rate, delayed signals and afterpulses change the counting efficiency as the source decays, and so mimic a different half-life. Such effects give no obvious sign of their size, or even their presence, in a single decay curve.

**Resolved by.** Results from runs with different bias voltages, discriminator levels and dead times that agree within their uncertainties; the half-life unchanged when successive early time bins, recorded at the highest rates, are removed from the fit; where digital pulse records were kept, the same data reanalysed with varied thresholds and dead times; an imposed dead time long enough to cover delayed signals and afterpulses; the loss-correction method tested at several count rates.

**Benchmark.** [1], [2], [7]

## 4. Source purity and contaminant activities

**Question.** How was the source shown to be free of other radionuclides with different half-lives, with what detection limit, and how were any contaminants that were found corrected for?

**Why it matters.** A detector that does not resolve energy, such as a beta counter, cannot tell one decaying nuclide from another, so an undetected impurity adds a component with a different half-life and can invalidate the result. Gating on a characteristic gamma-ray line reduces this sensitivity, at the price of lower efficiency and larger dead-time and pile-up corrections.

**Resolved by.** The production and separation method stated, with a measurement that identifies and quantifies remaining contaminants, or an upper limit on them; their contribution included in the fit or the uncertainty; where possible, half-lives from a characteristic gamma-ray line and from total counting compared.

**Benchmark.** [2], [3]

## 5. Daughter activities and decay chains

**Question.** If a radioactive daughter is counted together with the parent, how is its growth and decay modelled: is the daughter half-life fixed from an independent measurement, is the initial daughter activity known, and are the different detection efficiencies for parent and daughter radiation taken into account?

**Why it matters.** The recorded curve is then the sum of the parent decay and the growth and decay of the daughter, and when the half-lives are similar the daughter can largely mask the parent. Results that ignored the difference in detection efficiency between parent and daughter have been excluded from data evaluations for that reason.

**Resolved by.** The full decay-chain model written out; the daughter half-life taken from an independent, precise measurement; the purity of the parent and the rate at which it was deposited measured; the relative efficiencies for parent and daughter radiation determined and their uncertainty propagated.

**Benchmark.** [2], [3]

## 6. Long-term stability of the measurement

**Question.** For measurements lasting weeks to years, how were the stability of the detector response and of the source position monitored, and does the paper test the residuals for slow trends and periodic or autocorrelated structure?

**Why it matters.** A slow change in efficiency, for example from a source holder that moves over time, biases the half-life, most strongly for long-lived nuclides. Normalising to a reference source reduces the effect of electronic drift but not of changes that depend on geometry and photon energy, and a drift found only later can need corrections larger than the originally quoted uncertainty. When residuals are autocorrelated, the uncertainty from a least-squares fit, which assumes independent points, is too small.

**Resolved by.** A reference source measured alternately with the sample, with the limits of that normalisation discussed; source position and geometry fixed and checked over the campaign; residuals tested for autocorrelation; an uncertainty budget that includes components from medium- and long-term instabilities, not only the statistical uncertainty of the fit.

**Benchmark.** [5], [6]

## 7. Branching ratios and emission probabilities

**Question.** When a branching ratio or emission probability is reported, or used to convert counts into decays, is it absolute (relative to the total number of decays), how was the total number of decays determined, how was the detector efficiency calibrated, and how were branches without a gamma-ray signature, coincidence summing, dead time and pile-up handled?

**Why it matters.** Relative gamma-ray intensities give absolute branching ratios only if every branch is observed, and branches to a ground or isomeric state emit no gamma ray. An absolute value needs a pure source, so that the total number of decays can be trusted, and a precise absolute efficiency calibration. Weak branches near sum or pile-up peaks, such as a line at twice the annihilation energy, are easily contaminated.

**Resolved by.** The total number of decays measured independently, for example with a near-100% efficient beta counter, on a source of demonstrated purity; the absolute efficiency of the gamma-ray detector calibrated with standard sources and simulation, with its uncertainty; corrections for dead time, pile-up and coincidence summing stated; any branch obtained by subtraction from 100% identified as such; upper limits given for expected but unobserved branches.

**Benchmark.** [2], [3]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | S. Pommé et al., Uncertainty of nuclear counting, Metrologia 52, S3–S17 (2015); read as the copy hosted by NIST (publication 917522) | doi:10.1088/0026-1394/52/3/S3 |
| 2 | J. C. Hardy and I. S. Towner, The measurement and interpretation of superallowed 0+→0+ nuclear β decay, J. Phys. G 41, 114004 (2014); read as preprint arXiv:1312.3587 | doi:10.1088/0954-3899/41/11/114004 |
| 3 | J. C. Hardy and I. S. Towner, Superallowed 0+→0+ nuclear β decays: 2014 critical survey, with precise results for Vud and CKM unitarity, Phys. Rev. C 91, 025501 (2015); read as preprint arXiv:1411.5987 | doi:10.1103/PhysRevC.91.025501 |
| 4 | H. Dembinski et al., Application of the iterated weighted least-squares fit to counting experiments, Nucl. Instrum. Methods Phys. Res. A 940, 135 (2019); read as preprint arXiv:1807.07911 | doi:10.1016/j.nima.2019.05.086 |
| 5 | S. Pommé et al., Protocol for uncertainty assessment of half-lives, J. Radioanal. Nucl. Chem. 276, 335 (2008) | doi:10.1007/s10967-008-0508-y |
| 6 | R. Fitzgerald, NIST ionization chamber "A" sample-height corrections, J. Res. Natl. Inst. Stand. Technol. 117, 80 (2012) | doi:10.6028/jres.117.003 |
| 7 | S. Sharma et al., High-precision half-life determination of ¹⁴O via direct β counting, Eur. Phys. J. A 58, 83 (2022); read as preprint arXiv:2204.06668 | doi:10.1140/epja/s10050-022-00730-w |
