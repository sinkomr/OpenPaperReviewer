---
id: T-GRAVITATIONAL-WAVES
name: Gravitational-wave detection
type: technique
field: physics/astrophysics
applies_when: the paper reports or analyses gravitational-wave candidates from laser interferometer data, quotes a false-alarm rate or probability of astrophysical origin, or bases a claim about source masses, spins, distance, sky position, populations or tests of gravity on such signals
version: "0.1"
---

# Gravitational-wave detection

Ground-based laser interferometers are used to claim that a transient signal is astrophysical, usually through a matched-filter or unmodelled search that assigns it a false-alarm rate (FAR) or a probability of astrophysical origin, and to infer the source's masses, spins, distance and sky position by Bayesian parameter estimation (PE). Both steps rest on a model of non-Gaussian, non-stationary detector noise, on the calibration of the detector response, on waveform models and on prior distributions.

## 1. Background estimation and false-alarm rate

**Question.** How was the noise background for the candidate estimated (time shifts between detectors larger than the light travel time, or another method), how much background time was accumulated, was the candidate itself kept in or removed from the background, and how was the FAR converted into a false-alarm probability or significance?

**Why it matters.** The FAR of a candidate is the rate of background events ranked at least as high, so it can be no smaller than one over the background time searched, and its value depends on how the background was built. Keeping possible signals in the background gives conservative but noisier estimates, while removing them gives unbiased estimates at the cost of self-consistency. Time-shifted backgrounds also do not capture noise that is correlated between sites.

**Resolved by.** The background method, the number of time shifts and the effective background time stated; the FAR given with and without the candidate and other loud events in the background where it matters; the observing time used to turn the FAR into a probability; correlated terrestrial noise between sites addressed separately, for example with environmental sensors.

**Benchmark.** [1], [2]

## 2. Candidates from one detector or near threshold

**Question.** If the candidate was seen in only one detector, or is close to the detection threshold, how was its significance or probability of astrophysical origin obtained, and how does that number depend on the extrapolated noise tail and on the assumed merger rate?

**Why it matters.** Time shifts cannot build a background for a candidate seen in a single detector, and the noise distribution above the loudest background trigger is essentially unconstrained, so it must be extrapolated by a chosen model. A probability of astrophysical origin also depends on the assumed rate and population of real signals, so different but defensible choices give different answers for the same candidate.

**Resolved by.** The background data used and the model for the noise tail stated, with a conservative choice justified; the rate and population assumptions behind any probability of astrophysical origin given, with the result under alternatives; claims scaled to the probability actually obtained.

**Benchmark.** [1], [3]

## 3. Instrumental glitches and data quality at the candidate

**Question.** Does the paper show the data around the candidate (time-frequency maps, data-quality flags, auxiliary and environmental channels) and explain why a known class of instrumental transient, especially short broadband glitches that resemble high-mass binary signals, does not account for it?

**Why it matters.** Glitches from instrumental, environmental and unknown sources can mimic short astrophysical signals in a single detector; one common class of short glitch alone occurs a few times per hour, and some classes have no known coupling to an auxiliary channel and so cannot be vetoed. Data-quality vetoes remove a small fraction of time but a large fraction of loud background triggers, so whether they were applied changes both the background and the candidate's significance.

**Resolved by.** Spectrograms of each detector's data around the candidate; the data-quality categories in force and how vetoes were applied in the search; checks of auxiliary and environmental sensors with measured coupling factors showing that no disturbance was large enough; the candidate's signal morphology compared with known glitch classes; the effect of vetoes on the background reported.

**Benchmark.** [1], [4], [5]

## 4. Glitches overlapping the signal

**Question.** Did any glitch overlap the signal in time or frequency in any detector, and if so how was it removed or mitigated (subtraction, gating, reduced bandwidth or duration), and was the effect of that choice on the source parameters tested?

**Why it matters.** A glitch that overlaps a signal biases the source parameters and model-selection results, most strongly when it coincides with the signal's peak and is louder than the signal. Mitigation is often needed, and gating, which zeroes out a stretch of data, can itself bias the inferred parameters.

**Resolved by.** A statement for each detector of whether a glitch overlapped the signal; the mitigation method, its time and frequency extent and a check, for example with simulated signals, that it does not bias the result; parameters compared with and without the affected detector or data where possible; residuals after subtracting the best-fit signal checked for leftover power.

**Benchmark.** [1], [5], [6]

## 5. Noise model and spectral estimation

**Question.** How was the noise power spectral density (PSD) used in the likelihood estimated (from off-source data or from the analysed segment), and does the paper check that the whitened data around the signal are consistent with stationary Gaussian noise?

**Why it matters.** The standard likelihood assumes stationary, Gaussian noise with a known PSD, but the PSD must be estimated from data and drifts on timescales of tens of seconds to minutes. Different estimation methods give different whitening and so different parameter estimates, and an estimate from data far from the signal may not describe the noise at the signal.

**Resolved by.** The PSD method, the data used and its duration stated; the spectrum shown or its effect tested with a second method; tests of Gaussianity and stationarity of the whitened residuals near the signal reported.

**Benchmark.** [1], [7]

## 6. Detector calibration in amplitude and phase

**Question.** What frequency-dependent uncertainty in the amplitude and phase of the detector response applies at the time and in the frequency band of the signal, and was it marginalised over in PE?

**Why it matters.** The strain is reconstructed from a model of the detector's sensing and actuation, which drifts with time and is least well constrained where the model does not capture the measured response, such as at the low-frequency end of the band. Its error is complex-valued and frequency-dependent, with total uncertainties of several per cent in amplitude and a few degrees in phase, and it passes into the amplitude and phase of the reconstructed signal.

**Resolved by.** The calibration version and uncertainty envelope used for the analysed data stated, including the frequency range over which it is valid; amplitude and phase uncertainty included as parameters marginalised in PE; for very loud signals or claims that rest on amplitude, a check that the result is robust to the calibration model.

**Benchmark.** [1], [8], [9]

## 7. Waveform model systematics

**Question.** Which waveform model or models were used, what physics do they include or omit (precession, higher harmonics, eccentricity, tidal effects, merger and ringdown), and how much do the inferred parameters change with another model?

**Why it matters.** Waveform errors that are small enough for detection can still bias parameters, since the accuracy needed for unbiased measurement tightens as the signal-to-noise ratio grows. The spread between model families is used as an estimate of this systematic, but agreement between models does not prove either is accurate, and leftover signal in the residual can appear as a spurious deviation from general relativity.

**Resolved by.** The model names and versions stated with their physical content; results from at least two independent model families, with the spread treated as a systematic uncertainty; the signal's parameters shown to lie in the region where the models have been checked against numerical relativity; for tests of gravity, residuals and model accuracy considered before attributing a deviation to new physics.

**Benchmark.** [1], [10], [11]

## 8. Priors in parameter estimation

**Question.** Which prior distributions were used for masses, spins, distance and orientation, are the posteriors shown alongside the priors, and do the conclusions change under other reasonable priors?

**Why it matters.** When the data are only mildly informative, as is often the case for spins, posteriors are shaped by the prior, and astrophysically motivated priors can shift credible intervals noticeably. Bayes factors depend on prior volume. For population claims, the inference must also account for selection effects, because detection probability depends strongly on source parameters.

**Resolved by.** All priors stated with their ranges; posteriors plotted against priors for the parameters a claim rests on; key results repeated with alternative priors, or by reweighting the samples; for population or rate inferences, a selection function from injections or an equivalent calculation included in the likelihood.

**Benchmark.** [1], [12], [13]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | LIGO Scientific Collaboration and Virgo Collaboration (B. P. Abbott et al.), A guide to LIGO–Virgo detector noise and extraction of transient gravitational-wave signals, Class. Quantum Grav. 37, 055002 (2020); read as arXiv:1908.11170v3 | doi:10.1088/1361-6382/ab685e | full text | Sec. 8.4: background from time shifts larger than the light travel time or random pairing of single-detector triggers; FAR is the count of louder background triggers over the shifted time; correlated terrestrial noise is handled separately with environmental sensors. Sec. 6.2: glitches can mimic transients in one detector, witness channels, veto categories. Secs. 4.1, 5 and 7: PSD estimated from data by Welch averaging or a spline-and-Lorentzian fit, slow drifts and glitches, likelihood assumes stationary Gaussian noise. Secs. 6.1 and 9.3: frequency-dependent calibration uncertainty modelled by amplitude and phase splines sampled with the source parameters. Secs. 9.1 and 9.6: waveform models compared with numerical relativity and each other, the spread estimating the systematic; a glitch overlapping a signal was removed and checked with injections. Sec. 9.2: priors on masses, spins, orientation and distance |
| 2 | C. Capano, T. Dent, C. Hanna, M. Hendry, Y.-M. Hu, C. Messenger and J. Veitch, Systematic errors in estimation of gravitational-wave candidate significance, Phys. Rev. D 96, 082002 (2017) | doi:10.1103/PhysRevD.96.082002 | abstract | Abstract: keeping possible signals in the background gives self-consistent but conservative, higher-variance p-values; removing coincident candidates gives mean-unbiased p-values but loses self-consistency; a formula for the uncertainty in estimated significance is given |
| 3 | T. A. Callister, J. B. Kanner, T. J. Massinger, S. Dhurandhar and A. J. Weinstein, Observing gravitational waves with a single detector, Class. Quantum Grav. 34, 155007 (2017); read as arXiv:1704.00818 | doi:10.1088/1361-6382/aa7a76 | full text | Sec. II: time slides cannot form a background for single-detector events, so triggers without a coincident trigger in the other detector are used; the signal rate is set from the merger rate. Secs. III and V: no noise triggers above the loudest background event, so the tail must be extrapolated by a chosen model and the most conservative defensible model is argued for; the probability of astrophysical origin depends on the assumed merger rate, whose uncertainty outweighs the ambiguity from the choice of kernel bandwidth |
| 4 | LIGO Scientific Collaboration and Virgo Collaboration (B. P. Abbott et al.), Characterization of transient noise in Advanced LIGO relevant to gravitational wave signal GW150914, Class. Quantum Grav. 33, 134001 (2016); read as arXiv:1602.03844 | doi:10.1088/0264-9381/33/13/134001 | full text | Secs. 2 and 6: auxiliary and environmental channels and injection-measured coupling factors used to show that disturbances were too small to produce the signal; checks for correlated magnetic, lightning, radio and cosmic-ray noise between sites. Sec. 4 and Tables 1 and 2: veto categories and the small fraction of time they remove. Sec. 5.2: vetoes change the loud background and change a weaker candidate's false-alarm probability by about a factor of seven. Secs. 3.1 and 6.4: short broadband glitches with no known coupling overlap very short high-mass templates and populate the loud background |
| 5 | D. Davis et al., LIGO detector characterization in the second and third observing runs, Class. Quantum Grav. 38, 135014 (2021); read as arXiv:2101.11673 | doi:10.1088/1361-6382/abfd85 | full text | Sec. 1: glitches can mimic signals, overlap them and bias source properties. Sec. 4.2.1: one class of short glitch at about two to four per hour, resembling high-mass binary signals. Sec. 5.2: category-2 vetoes removed under 1% of data but 42% of triggers above a ranking-statistic threshold. Sec. 5.3: gating zeroes data and has been shown to bias source-property estimates. Sec. 5.5: event validation and glitch subtraction or reduced bandwidth needed for about ten events in one catalogue |
| 6 | J. Powell, Parameter estimation and model selection of gravitational wave signals contaminated by transient detector noise glitches, Class. Quantum Grav. 35, 155017 (2018) | doi:10.1088/1361-6382/aacf18 | abstract | Abstract: glitches overlapping signals affect parameter estimation and Bayes-factor model selection, worst when the glitch coincides with the signal peak and is louder than the signal; methods to remove glitches are needed |
| 7 | K. Chatziioannou, C.-J. Haster, T. B. Littenberg, W. M. Farr, S. Ghonge, M. Millhouse, J. A. Clark and N. Cornish, Noise spectral estimation methods and their impact on gravitational wave measurement of compact binary mergers, Phys. Rev. D 100, 104004 (2019) | doi:10.1103/PhysRevD.100.104004 | abstract | Abstract: PE assumes Gaussian, stationary noise with known PSD, which in practice is unknown and varies over tens of seconds to minutes; an off-source Welch estimate and an on-source spline-and-Lorentzian fit are compared, and the latter is argued to be more reliable for PE |
| 8 | L. Sun et al., Characterization of systematic error in Advanced LIGO calibration, Class. Quantum Grav. 37, 225008 (2020); read as arXiv:2005.02531 | doi:10.1088/1361-6382/abb14e | full text | Abstract and Sec. 1: complex, frequency-dependent response error; upper limit under 7% in magnitude and 4 degrees in phase (68%) over 20 to 2000 Hz. Secs. 2.3, 3.3 and 4.1: time-dependent correction factors tracked with calibration lines, separate epochs after changes, uncorrected drifts causing larger errors. Secs. 4.2 and 4.3: low-frequency band not captured by the model treated as entirely unknown in the uncertainty estimate |
| 9 | E. Payne, C. Talbot, P. D. Lasky, E. Thrane and J. S. Kissel, Gravitational-wave astronomy with a physical calibration model, Phys. Rev. D 102, 122004 (2020) | doi:10.1103/PhysRevD.102.122004 | abstract | Abstract: inference with a physically motivated calibration error model, its impact negligible for the events studied and projected small even at high signal-to-noise ratio; waveform, prior and noise systematics likely more important |
| 10 | L. Lindblom, B. J. Owen and D. A. Brown, Model waveform accuracy standards for gravitational wave data analysis, Phys. Rev. D 78, 124020 (2008); read as arXiv:0809.3844 | doi:10.1103/PhysRevD.78.124020 | full text | Eqs. 5, 9, 15 and 16 and surrounding text: the accuracy needed for measurement tightens as one over the signal-to-noise ratio, while the detection criterion does not depend on it, so a model adequate for detection may not suffice for measurement |
| 11 | M. Pürrer and C.-J. Haster, Gravitational waveform accuracy requirements for future ground-based detectors, Phys. Rev. Research 2, 023151 (2020); read as arXiv:1912.10055 | doi:10.1103/PhysRevResearch.2.023151 | full text | Secs. III.1 and III.3.2: indistinguishability criterion relating mismatch and signal-to-noise ratio; two model families give similar estimates yet both can be biased, so agreement does not remove the problem. Sec. IV.3 and abstract: coherent residual power after the best-fit template could appear as false deviations from general relativity |
| 12 | E. Thrane and C. Talbot, An introduction to Bayesian inference in gravitational-wave astronomy: parameter estimation, model selection, and hierarchical models, Publ. Astron. Soc. Aust. 36, e010 (2019); read as arXiv:1809.02293 (latest version) | doi:10.1017/pasa.2019.2 | full text | Sec. 2: choice of priors, some not obvious. Sec. 3: evidence and Bayes factors depend on the prior and penalise prior volume. Sec. 5: reweighting samples from a default prior to another prior. Sec. 5 and App. E: detection probability depends on source parameters and population likelihoods must include selection effects, estimated with injections |
| 13 | S. Vitale, D. Gerosa, C.-J. Haster, K. Chatziioannou and A. Zimmerman, Impact of Bayesian priors on the characterization of binary black hole coalescences, Phys. Rev. Lett. 119, 251103 (2017) | doi:10.1103/PhysRevLett.119.251103 | abstract | Abstract: with mildly informative data the prior noticeably changes inferred properties; astrophysically motivated spin priors shift effective-spin credible limits by about 10%, and mass-function priors tighten mass constraints |
