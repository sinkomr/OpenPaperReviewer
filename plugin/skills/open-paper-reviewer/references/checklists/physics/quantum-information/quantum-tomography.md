---
id: T-QUANTUM-TOMOGRAPHY
name: Quantum state and process tomography
type: technique
field: physics/quantum-information
applies_when: the paper estimates a density matrix, process matrix or gate set from measurement data by tomography, compressed sensing, gate set tomography or classical shadows, or quotes a fidelity, entanglement measure or other figure derived from such an estimate
version: "0.1"
---

# Quantum state and process tomography

## 1. Measurement set and reduced schemes

**Question.** Is the set of measurement settings informationally complete for the state or process reconstructed, and where a reduced scheme is used (compressed sensing, an MPS or other ansatz, a restricted subspace), are its assumptions stated and is the result certified without relying on them?

**Why it matters.** Linear reconstruction needs a set of settings whose outcome probabilities determine every parameter of the density matrix; with fewer settings the estimate is fixed partly by the method rather than the data. Reduced schemes cut the number of settings by assuming that the state is close to low rank or to an MPS of small bond dimension, and if that assumption fails the reconstruction error grows with the part of the state the ansatz leaves out.

**Resolved by.** The list of measurement bases or settings, the number of outcomes per setting and an argument that they are complete; for reduced schemes, the assumed rank or bond dimension stated and a certificate, such as a fidelity lower bound from the data or a direct fidelity estimate, that holds whether or not the assumption is true.

**Benchmark.** [1], [2], [3]

## 2. Reconstruction method and positivity

**Question.** Which estimator produced the density or process matrix (linear inversion, maximum likelihood, least squares or Bayesian mean), was positivity imposed, and are fidelities and entanglement measures computed in a way that is not biased by that constraint?

**Why it matters.** Linear inversion can return a matrix with negative eigenvalues, and maximum-likelihood and least-squares fits fix this by projecting onto physical states, which often gives a rank-deficient estimate with zero eigenvalues that finite data cannot justify. Any estimator that always returns a physical state is biased: with few counts per setting, maximum-likelihood and least-squares estimates tend to understate the fidelity with a pure target and overstate entanglement, enough to show entanglement for a separable state, and the bias grows with the number of qubits.

**Resolved by.** The estimator and its constraints named; the number of repetitions per setting given; linear quantities such as fidelity with a pure target also computed from the unconstrained linear estimate, or bounded directly from the data; for entanglement and other nonlinear quantities, a bound derived without the positivity projection or a comparison of estimators showing the conclusion does not depend on the choice; any witness or bounding operator chosen independently of the data used to evaluate it.

**Benchmark.** [1], [4], [5]

## 3. Error bars on reconstructed quantities

**Question.** How was the uncertainty of the quoted fidelity or derived quantity obtained, and is the method valid for a constrained estimator near the boundary of the set of physical states?

**Why it matters.** Error bars from resampling around a maximum-likelihood or least-squares estimate capture only the statistical scatter, not the bias from the positivity constraint, and can be smaller than that bias so that the interval excludes the true value. Methods that assume a Gaussian likelihood or asymptotic behaviour can also misstate the uncertainty when the estimate sits near the boundary.

**Resolved by.** The uncertainty method named, with its assumptions; confidence regions or intervals for the figure of merit itself, for example from concentration inequalities on a linear estimator or from a prior-free confidence-region construction; uncertainty from setting errors, such as waveplate or pulse-angle errors, included alongside counting statistics.

**Benchmark.** [1], [5], [6], [10]

## 4. Measurement model and its calibration

**Question.** Does the reconstruction use the measurements actually performed, including measured setting errors, detector efficiencies, readout errors and, for optical modes, the mode selected by the detector, and if the state is corrected for detection loss, is the uncorrected result also shown?

**Why it matters.** Tomography returns the state that best explains the data under an assumed measurement model, so a misaligned basis or an unmodelled detector imperfection appears as an error in the state. Small setting errors lower the fidelity in a way that can accumulate with the number of qubits, and can make a separable state violate an entanglement witness. Correcting for detection inefficiency gives an estimate of the state before loss, which is a different claim from the state detected.

**Resolved by.** The measurement operators used in the reconstruction stated, with how setting angles, readout and detection efficiency were calibrated; where the misalignment is known, reconstruction with the actual settings, or witnesses shifted to allow for it; for homodyne tomography, the detection efficiency built into the reconstruction, the mode defined by the local oscillator described, the phase reference of each quadrature sample and the photon-number truncation stated, with a check that raising the truncation changes nothing, and corrected and uncorrected results both given.

**Benchmark.** [1], [7], [8]

## 5. State preparation and measurement errors in process tomography

**Question.** For a process or gate fidelity from tomography, does the paper say how errors in preparing the input states and measuring the outputs were handled, and how large they are compared with the gate error claimed?

**Why it matters.** Standard process tomography assumes that the input states and measurements are known exactly, but they are made with the same imperfect gates. State preparation and measurement (SPAM) errors then set a floor on the reconstruction error that more repetitions or a positivity constraint cannot remove, and for coherent errors the distortion grows relative to the gate error as the gate improves.

**Resolved by.** The SPAM error measured and stated next to the gate error; for gates whose error is comparable to or smaller than the SPAM error, a self-consistent method such as gate set tomography, or a comparison with randomized benchmarking, in place of standard process tomography alone; any SPAM correction stated with how and when it was measured.

**Benchmark.** [9], [10]

## 6. Model fit and gauge in self-consistent tomography

**Question.** When gate set tomography or another self-consistent method is used, does the paper report how well the model fits the data, and was the gauge fixed in a stated way before computing gate fidelities?

**Why it matters.** Self-consistent methods fit a Markovian model of the whole gate set; drift, leakage, pulse spillover and other context dependence violate it, and a poor fit means the reported gates do not describe the device fully. The gate set is defined only up to a gauge transformation that leaves all predicted probabilities unchanged, so fidelities to target gates depend on how that gauge is chosen.

**Resolved by.** A goodness-of-fit statistic, such as the log-likelihood ratio against its expected chi-squared value, reported with any per-circuit model violation; gauge-invariant quantities, or the gauge-optimisation procedure stated alongside gauge-dependent ones; error bars computed with the gauge handled consistently.

**Benchmark.** [9], [10]

## 7. Which fidelity is quoted

**Question.** Does the paper define the fidelity it quotes (squared or unsquared state fidelity, process fidelity or average gate fidelity), and is any comparison with other work made on the same definition?

**Why it matters.** Both the squared and the unsquared form of the state fidelity are in common use and give different numbers for the same states. For a unitary target, average gate fidelity and process fidelity are related by a formula involving the dimension, and the average gate fidelity is always the larger of the two, so mixing them makes a result look better or worse than another.

**Resolved by.** The formula for each fidelity stated; the conversion given when comparing process and average gate fidelities, and the same definition used for every value compared.

**Benchmark.** [11]

## 8. Classical shadows

**Question.** For estimates from classical shadows or other randomized measurements, does the paper state the measurement ensemble, the number of snapshots, the estimator and the observables predicted, and how noise in the random unitaries and readout was calibrated?

**Why it matters.** The number of snapshots needed is set by the worst observable in the set, through a shadow norm that depends on the ensemble: random single-qubit Pauli measurements suit local observables, while global quantities such as fidelity with an entangled state need random Clifford circuits or many more snapshots. The standard estimators assume ideal unitaries and readout, and noise in either biases the estimates unless it is calibrated, for example on a known reference state.

**Resolved by.** The ensemble, number of snapshots and estimator (such as median of means) stated with the resulting guarantee for the observables claimed; a noise calibration step with its assumptions, or evidence that noise in the measurement channel is small enough not to matter.

**Benchmark.** [12], [13]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | D. F. V. James et al., Measurement of qubits, Phys. Rev. A 64, 052312 (2001); read as preprint arXiv:quant-ph/0103121 | doi:10.1103/PhysRevA.64.052312 |
| 2 | M. Cramer et al., Efficient quantum state tomography, Nat. Commun. 1, 149 (2010); read as preprint arXiv:1101.4366 | doi:10.1038/ncomms1147 |
| 3 | S. T. Flammia et al., Quantum tomography via compressed sensing: error bounds, sample complexity and efficient estimators, New J. Phys. 14, 095022 (2012); read as preprint arXiv:1205.2300 | doi:10.1088/1367-2630/14/9/095022 |
| 4 | R. Blume-Kohout, Optimal, reliable estimation of quantum states, New J. Phys. 12, 043034 (2010); read as preprint arXiv:quant-ph/0611080 | doi:10.1088/1367-2630/12/4/043034 |
| 5 | C. Schwemmer et al., Systematic errors in current quantum state tomography tools, Phys. Rev. Lett. 114, 080403 (2015); read as preprint arXiv:1310.8465 | doi:10.1103/PhysRevLett.114.080403 |
| 6 | P. Faist and R. Renner, Practical and reliable error bars in quantum tomography, Phys. Rev. Lett. 117, 010404 (2016); read as preprint arXiv:1509.06763 | doi:10.1103/PhysRevLett.117.010404 |
| 7 | D. Rosset et al., Imperfect measurement settings: implications for quantum state tomography and entanglement witnesses, Phys. Rev. A 86, 062325 (2012); read as preprint arXiv:1203.0911 | doi:10.1103/PhysRevA.86.062325 |
| 8 | A. I. Lvovsky and M. G. Raymer, Continuous-variable optical quantum-state tomography, Rev. Mod. Phys. 81, 299 (2009); read as preprint arXiv:quant-ph/0511044 | doi:10.1103/RevModPhys.81.299 |
| 9 | S. T. Merkel et al., Self-consistent quantum process tomography, Phys. Rev. A 87, 062119 (2013); read as preprint arXiv:1211.0322 | doi:10.1103/PhysRevA.87.062119 |
| 10 | E. Nielsen et al., Gate set tomography, Quantum 5, 557 (2021); read as preprint arXiv:2009.07301 | doi:10.22331/q-2021-10-05-557 |
| 11 | A. Gilchrist et al., Distance measures to compare real and ideal quantum processes, Phys. Rev. A 71, 062310 (2005); read as preprint arXiv:quant-ph/0408063 | doi:10.1103/PhysRevA.71.062310 |
| 12 | H.-Y. Huang et al., Predicting many properties of a quantum system from very few measurements, Nat. Phys. 16, 1050 (2020); read as preprint arXiv:2002.08953 | doi:10.1038/s41567-020-0932-7 |
| 13 | S. Chen et al., Robust shadow estimation, PRX Quantum 2, 030348 (2021); read as preprint arXiv:2011.09636 | doi:10.1103/PRXQuantum.2.030348 |
