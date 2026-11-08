---
id: T-GRAVITATIONAL-WAVES
name: Gravitational-wave detection
type: technique
field: physics/astrophysics
applies_when: the paper reports or analyses gravitational-wave candidates from laser interferometer data, quotes a false-alarm rate or probability of astrophysical origin, or bases a claim about source masses, spins, distance, sky position, populations or tests of gravity on such signals
version: "0.1"
---

# Gravitational-wave detection

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

## 3. Instrumental glitches at and in the signal

**Question.** Does the paper show the data around the candidate (time-frequency maps, data-quality flags, auxiliary and environmental channels) and explain why a known class of instrumental transient, especially short broadband glitches that resemble high-mass binary signals, does not account for it, and if a glitch overlapped the signal in time or frequency in any detector, how was it removed or mitigated (subtraction, gating, reduced bandwidth or duration) and was the effect of that choice on the source parameters tested?

**Why it matters.** Glitches from instrumental, environmental and unknown sources can mimic short astrophysical signals in a single detector; one common class of short glitch occurs a few times per hour, and some classes have no known coupling to an auxiliary channel and so cannot be vetoed. Vetoes remove a small fraction of time but a large fraction of loud background triggers, so whether they were applied changes both the background and the candidate's significance. A glitch that overlaps a signal biases the source parameters and model selection, most strongly when it coincides with the signal's peak and is louder than the signal, and gating, which zeroes out a stretch of data, can itself bias them.

**Resolved by.** Spectrograms of each detector's data around the candidate; the data-quality categories in force, how vetoes were applied in the search and their effect on the background; checks of auxiliary and environmental sensors with measured coupling factors showing that no disturbance was large enough; the signal morphology compared with known glitch classes; for each detector, whether a glitch overlapped the signal, and the mitigation method, its time and frequency extent and a check, for example with simulated signals, that it does not bias the result; parameters compared with and without the affected detector or data where possible; residuals after subtracting the best-fit signal checked for leftover power.

**Benchmark.** [1], [4], [5], [6]

## 4. Noise model and spectral estimation

**Question.** How was the noise power spectral density (PSD) used in the likelihood estimated (from off-source data or from the analysed segment), and does the paper check that the whitened data around the signal are consistent with stationary Gaussian noise?

**Why it matters.** The standard likelihood assumes stationary, Gaussian noise with a known PSD, but the PSD must be estimated from data and drifts on timescales of tens of seconds to minutes. Different estimation methods give different whitening and so different parameter estimates, and an estimate from data far from the signal may not describe the noise at the signal.

**Resolved by.** The PSD method, the data used and its duration stated; the spectrum shown or its effect tested with a second method; tests of Gaussianity and stationarity of the whitened residuals near the signal reported.

**Benchmark.** [1], [7]

## 5. Detector calibration in amplitude and phase

**Question.** What frequency-dependent uncertainty in the amplitude and phase of the detector response applies at the time and in the frequency band of the signal, and was it marginalised over in PE?

**Why it matters.** The strain is reconstructed from a model of the detector's sensing and actuation, which drifts with time and is least well constrained where the model does not capture the measured response, such as at the low-frequency end of the band. Its error is complex-valued and frequency-dependent, with total uncertainties of several per cent in amplitude and a few degrees in phase, and it passes into the amplitude and phase of the reconstructed signal.

**Resolved by.** The calibration version and uncertainty envelope used for the analysed data stated, including the frequency range over which it is valid; amplitude and phase uncertainty included as parameters marginalised in PE; for very loud signals or claims that rest on amplitude, a check that the result is robust to the calibration model.

**Benchmark.** [1], [8], [9]

## 6. Waveform model systematics

**Question.** Which waveform model or models were used, what physics do they include or omit (precession, higher harmonics, eccentricity, tidal effects, merger and ringdown), and how much do the inferred parameters change with another model?

**Why it matters.** Waveform errors that are small enough for detection can still bias parameters, since the accuracy needed for unbiased measurement tightens as the signal-to-noise ratio grows. The spread between model families is used as an estimate of this systematic, but agreement between models does not prove either is accurate, and leftover signal in the residual can appear as a spurious deviation from general relativity.

**Resolved by.** The model names and versions stated with their physical content; results from at least two independent model families, with the spread treated as a systematic uncertainty; the signal's parameters shown to lie in the region where the models have been checked against numerical relativity; for tests of gravity, residuals and model accuracy considered before attributing a deviation to new physics.

**Benchmark.** [1], [10], [11]

## 7. Priors in parameter estimation

**Question.** Which prior distributions were used for masses, spins, distance and orientation, are the posteriors shown alongside the priors, and do the conclusions change under other reasonable priors?

**Why it matters.** When the data are only mildly informative, as is often the case for spins, posteriors are shaped by the prior, and astrophysically motivated priors can shift credible intervals noticeably. Bayes factors depend on prior volume. For population claims, the inference must also account for selection effects, because detection probability depends strongly on source parameters.

**Resolved by.** All priors stated with their ranges; posteriors plotted against priors for the parameters a claim rests on; key results repeated with alternative priors, or by reweighting the samples; for population or rate inferences, a selection function from injections or an equivalent calculation included in the likelihood.

**Benchmark.** [1], [12], [13]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | LIGO Scientific Collaboration and Virgo Collaboration (B. P. Abbott et al.), A guide to LIGO–Virgo detector noise and extraction of transient gravitational-wave signals, Class. Quantum Grav. 37, 055002 (2020); read as arXiv:1908.11170v3 | doi:10.1088/1361-6382/ab685e |
| 2 | C. Capano et al., Systematic errors in estimation of gravitational-wave candidate significance, Phys. Rev. D 96, 082002 (2017) | doi:10.1103/PhysRevD.96.082002 |
| 3 | T. A. Callister et al., Observing gravitational waves with a single detector, Class. Quantum Grav. 34, 155007 (2017); read as arXiv:1704.00818 | doi:10.1088/1361-6382/aa7a76 |
| 4 | LIGO Scientific Collaboration and Virgo Collaboration (B. P. Abbott et al.), Characterization of transient noise in Advanced LIGO relevant to gravitational wave signal GW150914, Class. Quantum Grav. 33, 134001 (2016); read as arXiv:1602.03844 | doi:10.1088/0264-9381/33/13/134001 |
| 5 | D. Davis et al., LIGO detector characterization in the second and third observing runs, Class. Quantum Grav. 38, 135014 (2021); read as arXiv:2101.11673 | doi:10.1088/1361-6382/abfd85 |
| 6 | J. Powell, Parameter estimation and model selection of gravitational wave signals contaminated by transient detector noise glitches, Class. Quantum Grav. 35, 155017 (2018) | doi:10.1088/1361-6382/aacf18 |
| 7 | K. Chatziioannou et al., Noise spectral estimation methods and their impact on gravitational wave measurement of compact binary mergers, Phys. Rev. D 100, 104004 (2019) | doi:10.1103/PhysRevD.100.104004 |
| 8 | L. Sun et al., Characterization of systematic error in Advanced LIGO calibration, Class. Quantum Grav. 37, 225008 (2020); read as arXiv:2005.02531 | doi:10.1088/1361-6382/abb14e |
| 9 | E. Payne et al., Gravitational-wave astronomy with a physical calibration model, Phys. Rev. D 102, 122004 (2020) | doi:10.1103/PhysRevD.102.122004 |
| 10 | L. Lindblom et al., Model waveform accuracy standards for gravitational wave data analysis, Phys. Rev. D 78, 124020 (2008); read as arXiv:0809.3844 | doi:10.1103/PhysRevD.78.124020 |
| 11 | M. Pürrer and C.-J. Haster, Gravitational waveform accuracy requirements for future ground-based detectors, Phys. Rev. Research 2, 023151 (2020); read as arXiv:1912.10055 | doi:10.1103/PhysRevResearch.2.023151 |
| 12 | E. Thrane and C. Talbot, An introduction to Bayesian inference in gravitational-wave astronomy: parameter estimation, model selection, and hierarchical models, Publ. Astron. Soc. Aust. 36, e010 (2019); read as arXiv:1809.02293 (latest version) | doi:10.1017/pasa.2019.2 |
| 13 | S. Vitale et al., Impact of Bayesian priors on the characterization of binary black hole coalescences, Phys. Rev. Lett. 119, 251103 (2017) | doi:10.1103/PhysRevLett.119.251103 |
