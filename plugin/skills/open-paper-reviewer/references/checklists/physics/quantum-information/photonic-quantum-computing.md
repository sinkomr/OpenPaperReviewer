---
id: T-PHOTONIC-QUANTUM-COMPUTING
name: Photonic quantum computing and boson sampling
type: technique
field: physics/quantum-information
applies_when: the paper sends single photons or squeezed light through a linear-optical interferometer and counts photons at the output, as in boson sampling, Gaussian boson sampling or linear-optical gates, or bases a claim on multiphoton interference or on samples from such a device
version: "0.1"
---

# Photonic quantum computing and boson sampling

## 1. Photon indistinguishability

**Question.** How was the indistinguishability of the input photons measured, for example by Hong-Ou-Mandel (HOM) interference between every pair of sources or time bins that feed the circuit, and how does the measured value enter the model against which the output is compared?

**Why it matters.** With partly distinguishable photons the output can be approximated classically by keeping interference among only a limited number of photons, set by the indistinguishability, so beyond some photon number adding photons raises the classical cost only polynomially. A HOM visibility is lowered by multiphoton components as well as by imperfect overlap, so the overlap must be extracted with a model of the source, and pairwise overlaps do not fully fix how three or more photons interfere.

**Resolved by.** HOM visibilities reported for the photon pairs actually used, with the multiphoton contribution measured and accounted for when the overlap is inferred; the indistinguishability compared with the level that known classical algorithms tolerate for the photon number claimed; the measured distinguishability included in the theoretical prediction, or the effect of leaving it out estimated.

**Benchmark.** [1], [2], [3]

## 2. Multiphoton emission and heralding

**Question.** For single-photon inputs, what are the second-order autocorrelation at zero delay, the generation and heralding efficiencies, and the probability of extra photons in an input mode, and how were events with the wrong number of photons per input excluded or modelled?

**Why it matters.** Heralded sources based on parametric down-conversion must be run at low pair probability, because multiple pairs put more than one photon into a mode, and with spontaneous sources the probability of the intended multiphoton input falls exponentially with the number of photons. Extra photons from multiple pairs are absent from a model of the intended input and can account for differences between measured and predicted interference, while losses in the heralding and heralded arms and dark counts give false or missing heralds. Even nominally deterministic sources become probabilistic as their extraction losses grow.

**Resolved by.** The autocorrelation at zero delay, heralding efficiency and pair-generation probability reported at the pump power used; the heralding and post-selection logic stated; the residual rate of multiple-photon inputs estimated and either included in the prediction or shown to be negligible; the per-photon source efficiency given, not only the rate of detected events.

**Benchmark.** [2], [4], [5], [11]

## 3. Squeezed-light inputs

**Question.** For GBS, how were the squeezing parameter, the purity and the number of spectral or temporal modes of each squeezed source measured, and do the values used in the theoretical model come from those measurements or from a fit to the sampling data?

**Why it matters.** A real squeezer can emit into several spectral modes at once, so each input is a set of independent squeezers rather than the single squeezed mode a model may assume; the effective number of modes can be read from the second-order correlation of one arm. Added classical noise moves squeezed input towards light that can be modelled classically, and whether a noisy GBS device can be simulated efficiently depends on the squeezing together with the transmission and detector quality.

**Resolved by.** Squeezing, mean photon number and effective mode number reported for each source with uncertainties, for example from loss-tolerant correlation measurements; the purity or excess noise of the input stated; any model parameters fitted to the output data identified as such, with their values compared with the independent source measurements.

**Benchmark.** [6], [7], [8]

## 4. Loss budget and post-selection

**Question.** What is the transmission of each stage, from source and coupling through the circuit to the detectors, in each mode, and how does the analysis treat lost photons and failed operations: by post-selecting on events with all photons detected, by heralding, or by including loss in the model?

**Why it matters.** Each photon reaches a detector only with the overall transmission, so the rate of events with every photon detected falls exponentially with the number of photons, and in circuits whose depth grows with the number of modes the survival probability of each photon also falls exponentially with depth. When too few photons survive, or loss is high compared with squeezing and detector quality, the output can be simulated efficiently. Post-selection removes loss from single-photon boson sampling at the cost of rate, but in GBS loss must be modelled explicitly; a linear-optical gate whose success is known only from detecting its output photons is probabilistic, and a circuit of such gates succeeds with a probability that falls exponentially with the number of gates.

**Resolved by.** A loss budget giving source, coupling, circuit and detection efficiencies and the overall transmission per mode, with how each was measured; the number of photons generated compared with the number detected; the post-selection rule stated together with the fraction of events it keeps, and for gates whether success is heralded or post-selected and with what probability; loss included in the predicted distribution where it is not removed by post-selection; the experiment placed relative to the known loss conditions under which classical simulation becomes efficient.

**Benchmark.** [7], [8], [9], [10]

## 5. Characterisation of the linear-optical circuit

**Question.** How was the transfer matrix of the interferometer measured, including moduli, phases and mode-dependent loss, was the reconstruction checked independently, and is the measured matrix, rather than the design, used to predict and validate the output?

**Why it matters.** A built circuit differs from its design through fabrication tolerances, drifts and loss, and its matrix is in general not unitary. Moduli alone do not fix the phases for more than three modes, so phase-sensitive probes are needed. Boson sampling assumes transformations drawn at random from all unitaries, and a circuit with few free parameters or imperfect components may reach only part of that set.

**Resolved by.** The characterisation method stated, with phase-sensitive measurements and repeated runs giving uncertainties; the reconstructed matrix validated by an independent measurement, such as two-photon interference visibilities compared with those predicted from the matrix; the treatment of non-unitarity and path-dependent loss described; stability over the data-taking period shown; the degree to which the implemented transformation is programmable or random stated.

**Benchmark.** [11], [12]

## 6. Detectors and photon-number resolution

**Question.** What are the efficiency, dark-count rate, dead time and photon-number resolution of the detectors, and does the model of the output account for threshold detectors that cannot tell one photon from several, and for dark counts?

**Why it matters.** Many single-photon detectors register only zero or at least one photon, and even number-resolving detectors do not report the true photon number when their efficiency is below one; dark counts add further disagreement between detected and incident photons. With threshold detectors the output probabilities are given by a different function from that for photon counting, and the hardness argument for threshold detection assumes that two or more photons rarely reach the same output mode.

**Resolved by.** Detector efficiency, dark-count rate, dead time and timing window stated with how they were measured; the detection model used in the predictions matched to the detectors, with threshold detection modelled where it applies; the fraction of events with more than one photon in a mode estimated; the ratio of dark-count rate to efficiency reported where classical-simulability conditions depend on it.

**Benchmark.** [4], [7], [13]

## 7. Validation against classical models

**Question.** Which classically computable alternative models is the output compared with, for example uniform sampling, distinguishable photons, mean-field states, thermal or coherent inputs, and samplers that reproduce the low-order marginals of the ideal distribution, and which tests and statistics separate the data from each?

**Why it matters.** In the regime of interest the ideal output probabilities cannot be computed for each sample, so validation instead tests the data against specific classical models. Coarse-grained tests such as bunching can be passed by a mean-field sampler, and thermal input can be sampled efficiently. Classical samplers built from one- and two-mode marginals can score better than an experiment on benchmarks computed over few-mode marginals, because the experiment's higher-order correlations are measured with less precision.

**Resolved by.** Each alternative model named and the test that rejects it described with its statistical strength, for example likelihood ratios, correlator statistics or suppression laws for interferometers with known symmetry; comparisons that include samplers matched to the measured low-order correlations, not only uniform or distinguishable models; the reference distribution stated, including whether it contains the measured loss, distinguishability and noise; evidence that features beyond low-order marginals agree with the quantum prediction.

**Benchmark.** [8], [14], [15], [16]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | J. J. Renema et al., Efficient classical algorithm for boson sampling with partially distinguishable photons, Phys. Rev. Lett. 120, 220502 (2018); read as arXiv:1707.02793 | doi:10.1103/PhysRevLett.120.220502 |
| 2 | H. Ollivier et al., Hong-Ou-Mandel interference with imperfect single photon sources, Phys. Rev. Lett. 126, 063602 (2021); read as arXiv:2005.01743 | doi:10.1103/PhysRevLett.126.063602 |
| 3 | A. J. Menssen et al., Distinguishability and many-particle interference, Phys. Rev. Lett. 118, 153603 (2017); read as arXiv:1609.09804 | doi:10.1103/PhysRevLett.118.153603 |
| 4 | M. D. Eisaman et al., Invited Review Article: Single-photon sources and detectors, Rev. Sci. Instrum. 82, 071101 (2011); read as the author copy hosted by NIST | doi:10.1063/1.3610677 |
| 5 | A. P. Lund et al., Boson sampling from a Gaussian state, Phys. Rev. Lett. 113, 100502 (2014); read as arXiv:1305.4346 | doi:10.1103/PhysRevLett.113.100502 |
| 6 | A. Christ et al., Probing multimode squeezing with correlation functions, New J. Phys. 13, 033027 (2011); read as arXiv:1012.0262 | doi:10.1088/1367-2630/13/3/033027 |
| 7 | H. Qi et al., Regimes of classical simulability for noisy Gaussian boson sampling, Phys. Rev. Lett. 124, 100502 (2020); read as arXiv:1905.12075 | doi:10.1103/PhysRevLett.124.100502 |
| 8 | D. S. Phillips et al., Benchmarking of Gaussian boson sampling using two-point correlators, Phys. Rev. A 99, 023836 (2019); read as arXiv:1807.11294 | doi:10.1103/PhysRevA.99.023836 |
| 9 | M. Oszmaniec and D. J. Brod, Classical simulation of photonic linear optics with lost particles, New J. Phys. 20, 092002 (2018); read as arXiv:1801.06166 | doi:10.1088/1367-2630/aadfa8 |
| 10 | P. Kok et al., Linear optical quantum computing with photonic qubits, Rev. Mod. Phys. 79, 135 (2007); read as arXiv:quant-ph/0512071 | doi:10.1103/RevModPhys.79.135 |
| 11 | S. Rahimi-Keshari et al., Direct characterization of linear-optical networks, Opt. Express 21, 13450 (2013); read as arXiv:1210.6463 | doi:10.1364/OE.21.013450 |
| 12 | N. J. Russell et al., Direct dialling of Haar random unitary matrices, New J. Phys. 19, 033007 (2017); read as arXiv:1506.06220 | doi:10.1088/1367-2630/aa60ed |
| 13 | N. Quesada et al., Gaussian boson sampling using threshold detectors, Phys. Rev. A 98, 062322 (2018); read as arXiv:1807.01639 | doi:10.1103/PhysRevA.98.062322 |
| 14 | M. C. Tichy et al., Stringent and efficient assessment of boson-sampling devices, Phys. Rev. Lett. 113, 020502 (2014); read as arXiv:1312.3080 | doi:10.1103/PhysRevLett.113.020502 |
| 15 | M. Walschaers et al., Statistical benchmark for BosonSampling, New J. Phys. 18, 032001 (2016); read as arXiv:1410.8547 | doi:10.1088/1367-2630/18/3/032001 |
| 16 | B. Villalonga et al., Efficient approximation of experimental Gaussian boson sampling, preprint arXiv:2109.11525 (2021, revised 2022) | doi:10.48550/arXiv.2109.11525 |
