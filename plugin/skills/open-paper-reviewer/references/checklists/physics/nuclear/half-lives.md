---
id: T-HALF-LIVES
name: Half-life and decay measurements
type: technique
field: physics/nuclear
applies_when: the paper reports a half-life, decay constant, branching ratio or emission probability of a radionuclide or nuclear state, obtained by following a count rate over time or by counting decays, or bases a claim on such a value
version: "0.1"
---

# Half-life and decay measurements

Decay measurements are used to claim the half-life (or decay constant) of a radionuclide or nuclear state and the branching ratios and emission probabilities of its decay modes. Most half-lives are inferred by fitting the fall of a count rate over time, which assumes that the detector efficiency, the count loss and the composition of the source either stay constant or are corrected while the activity changes.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | S. Pommé, R. Fitzgerald and J. Keightley, Uncertainty of nuclear counting, Metrologia 52, S3–S17 (2015); read as the copy hosted by NIST (publication 917522) | doi:10.1088/0026-1394/52/3/S3 | full text | Sec. 1: extended dead time needed to cover saturation pulses, delayed signals and afterpulses; classical live-time counting with an average correction is in error for short-lived activities. Sec. 2.1: pile-up, extending and non-extending dead time are distinct loss mechanisms. Sec. 2.3: a 10% dead-time error at a rate of 0.3 per dead time gives 3 to 4.3% rate errors. Sec. 3.5: loss-free counting handles rapidly varying rates. Sec. 4.1: an imposed dead time does not fully compensate pile-up. Sec. 5: Poisson statistics hold only if the half-life is long compared with the count; live-time throughput biased as the source decays. Sec. 6: test loss corrections at several count rates and propagate their uncertainty |
| 2 | J. C. Hardy and I. S. Towner, The measurement and interpretation of superallowed 0+→0+ nuclear β decay, J. Phys. G 41, 114004 (2014); read as preprint arXiv:1312.3587 | doi:10.1088/0954-3899/41/11/114004 | full text | Sec. 2.2: impurity activities, rate-dependent thresholds, dead time and pile-up and flawed statistical analyses give no obvious signal of their size. Sec. 2.2.1: beta detection cannot distinguish nuclides, so an undetected impurity can invalidate a result; contaminants identified and monitored; dead time, bias and discriminator levels varied and fitting checked on Monte Carlo data; digital pulse records reanalysed; parent-daughter composite decay needs a known daughter half-life, a pure source and a known deposition rate. Sec. 2.2.2: gamma detection eases purity but adds dead-time and pile-up uncertainty; beta and gamma results compared. Sec. 2.3: absolute branching needs total decays from a pure source, absolute efficiency, dead-time, pile-up and summing corrections; ground-state branch by subtraction; annihilation pile-up contaminating a peak at 1022 keV |
| 3 | J. C. Hardy and I. S. Towner, Superallowed 0+→0+ nuclear β decays: 2014 critical survey, with precise results for Vud and CKM unitarity, Phys. Rev. C 91, 025501 (2015); read as preprint arXiv:1411.5987 | doi:10.1103/PhysRevC.91.025501 | full text | Sec. II: half-life results rejected because they were not analysed by maximum likelihood, whose importance was recognised in 1969. Table VII: half-lives rejected for small uncertainties and likely bias without maximum likelihood, for inadequately treated pile-up, and for ignoring the difference in beta-detection efficiency between parent and daughter; a branching ratio rejected because of numerous impurities |
| 4 | H. Dembinski, M. Schmelling and R. Waldi, Application of the iterated weighted least-squares fit to counting experiments, Nucl. Instrum. Methods Phys. Res. A 940, 135–141 (2019); read as preprint arXiv:1807.07911 | doi:10.1016/j.nima.2019.05.086 | full text | Abstract and Sec. 2: standard weighted least-squares variants (Neyman and Pearson forms) give biased estimates for Poisson data with small counts; an iterated weighted least-squares fit converges to the maximum-likelihood estimate |
| 5 | S. Pommé, J. Camps, R. Van Ammel and J. Paepen, Protocol for uncertainty assessment of half-lives, J. Radioanal. Nucl. Chem. 276, 335–339 (2008) | doi:10.1007/s10967-008-0508-y | abstract | Abstract (JRC repository record JRC45544): half-life uncertainties tend to be underestimated; the uncertainty from a least-squares decay-curve fit is prone to error; activity series are often autocorrelated, so tests that assume random data do not apply; components grouped by the frequency at which they occur; more complete reporting proposed |
| 6 | R. Fitzgerald, NIST ionization chamber "A" sample-height corrections, J. Res. Natl. Inst. Stand. Technol. 117, 80–95 (2012) | doi:10.6028/jres.117.003 | full text | Abstract and Sec. 1: a slipping source-positioning ring changed the response by about 10⁻⁵ to 10⁻³ per year. Sec. 2: the ratio to a radium reference source mitigates variations in electrometer response but does not remove the height effect. Sec. 3.3: model checked against half-life residuals. Sec. 4.2 and Table 6: largest relative corrections for long-lived nuclides; 18 of 63 half-life corrections exceed the original uncertainty |
| 7 | S. Sharma et al., High-precision half-life determination of ¹⁴O via direct β counting, Eur. Phys. J. A 58, 83 (2022); read as preprint arXiv:2204.06668 | doi:10.1140/epja/s10050-022-00730-w | full text | Sec. 3.1: bias voltage, discriminator threshold and imposed dead time varied between runs with consistent results. Sec. 3.3: leading channels removed in steps and the fit repeated; a half-life independent of the initial rate taken to show that rate-dependent effects, including trace contaminants, are negligible. Sec. 3.4: refit with dead times shifted by their uncertainty |
