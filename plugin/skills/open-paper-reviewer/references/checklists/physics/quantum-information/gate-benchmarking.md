---
id: T-GATE-BENCHMARKING
name: Gate benchmarking
type: technique
field: physics/quantum-information
applies_when: the paper quotes a single- or two-qubit gate fidelity or error rate, or a circuit or layer fidelity, obtained by randomized benchmarking in any form, gate set tomography or cross-entropy benchmarking, or compares such a figure with a fault-tolerance threshold or other devices
version: "0.1"
---

# Gate benchmarking

## 1. Which fidelity is quoted

**Question.** Does the paper state which quantity its quoted gate fidelity is (average gate fidelity or process fidelity), which operation it refers to (a Clifford operation, a native gate or a circuit layer), and how any conversion between these was made?

**Why it matters.** Average gate fidelity and process fidelity differ by a factor that depends on the dimension, so the same gate gives different numbers: the process infidelity is 3/2 of the average infidelity for one qubit and 5/4 for two. Standard RB returns an error per Clifford operation, and turning it into an error per native gate assumes how the error is shared among the native gates that make up each Clifford.

**Resolved by.** The fidelity measure named with its definition and the dimension it refers to; the operation it applies to; any conversion stated, such as the average number of native gates per Clifford, with the unconverted value also given; the same measure used whenever the result is compared with other work.

**Benchmark.** [1], [2], [4]

## 2. Decay model, fit and SPAM

**Question.** Is the benchmarking decay shown against sequence length, with the fit model, which parameters were free, the sequence lengths, the numbers of random sequences and shots, and the way the uncertainty of the fitted rate was obtained?

**Why it matters.** RB is insensitive to SPAM errors because they are absorbed into the amplitude and offset of the fitted decay, so fixing those parameters, or using too few or too short sequences, lets SPAM errors into the rate. Gate-dependent noise can distort the decay at the shortest lengths, and the scatter between random sequences grows with length, so an unweighted fit can misstate the rate and its uncertainty.

**Resolved by.** Survival probability against sequence length plotted with the fit, over lengths long enough for the decay to be well resolved; amplitude and offset left free, or the offset removed by the sequence design; the shortest sequences checked for departures from the fitted decay; the numbers of sequences and shots stated; uncertainties from a method that allows for the unequal scatter, such as a weighted fit or an estimator designed for benchmarking data.

**Benchmark.** [3], [5], [7]

## 3. From the decay rate to the error of a gate

**Question.** Does the paper justify reading the RB rate as the average error of its gates, and where it compares the result with a fault-tolerance threshold, does it consider coherent errors, for which average and worst-case error can differ widely?

**Why it matters.** When the noise depends on the gate, the RB rate is a well-defined property of the device but can differ by orders of magnitude from the average gate infidelity computed from a representation of the gates, which is not unique. Fault-tolerance thresholds are mostly stated for the worst-case error, which for coherent errors scales as the square root of the average error, so a small average error can go with a much larger worst-case error.

**Resolved by.** The rate described as an average error over the gate set, not as the fidelity of each gate; comparisons with tomographic estimates made in a stated and suitable gauge; for threshold claims, evidence on how coherent the errors are, such as a unitarity measurement or tomographic estimates, or a bound on the worst-case error, not the average error alone.

**Benchmark.** [2], [6], [7], [8]

## 4. Interleaved benchmarking of a single gate

**Question.** For a gate fidelity from interleaved RB, does the paper show the reference and interleaved decays, and quote the estimate with its systematic bounds and with the error per Clifford of the reference sequence?

**Why it matters.** The interleaved estimate is exact only in special cases such as depolarizing noise; in general the true error lies within bounds that grow with the reference error and widen with coherent errors. The estimate becomes unreliable, and can understate the error, when the interleaved gate is much better than the average Clifford or when its error partly cancels the error of the neighbouring gates.

**Resolved by.** Both decay curves with their fits; the estimate quoted with its systematic interval as well as its statistical uncertainty; the reference error per Clifford reported; where the interleaved gate's error is much smaller than the reference error, that limitation stated or a second method used.

**Benchmark.** [4], [9]

## 5. Leakage

**Question.** For qubits with states outside the computational subspace, does the paper measure or bound the rates of leakage into those states and of return from them, and does its fit model allow for leakage?

**Why it matters.** Leakage cannot be described by a trace-preserving map on the qubit subspace, and when it is not observed it turns the benchmarking decay into a mixture of exponentials. A single-exponential fit then mixes leakage with other errors, and the leakage and return rates cannot be separated without measuring the population of the computational subspace.

**Resolved by.** A readout that distinguishes leaked states, or a protocol that tracks the population of the computational subspace against sequence length; leakage and return rates per gate or per Clifford reported; the fidelity taken from a model that includes them.

**Benchmark.** [2], [10]

## 6. Crosstalk and isolated benchmarking

**Question.** Were the quoted fidelities measured with neighbouring qubits idle or with operations running on them at the same time, and does the paper report simultaneous RB or another crosstalk test under the conditions used for its circuits?

**Why it matters.** A qubit benchmarked alone does not show the errors caused by driving its neighbours, and its error rate can rise markedly when they are benchmarked at the same time. Correlated errors between qubits are also hidden from isolated benchmarks, and compiler rules that prevent parallel gates keep some crosstalk from being probed.

**Resolved by.** Isolated and simultaneous error rates given side by side for each qubit or pair; a test for correlated errors; the benchmark run under the same operating conditions as the circuits the paper reports, with the compilation rules stated.

**Benchmark.** [2], [11]

## 7. Cross-entropy benchmarking

**Question.** For a fidelity from XEB, does the paper state the estimator, how the ideal output probabilities were computed, and the assumptions that link the estimator to circuit fidelity and to errors per gate?

**Why it matters.** The estimator equals the circuit fidelity only under assumptions: random circuits deep enough for the ideal outputs to follow the Porter–Thomas distribution, and errors that drive the output towards the uniform distribution. The ideal probabilities must be computed classically, so for circuits beyond simulation the fidelity is extrapolated from simpler circuits, and errors per gate inferred from it rest on a model in which the circuit fidelity is a product of gate, preparation and measurement fidelities.

**Resolved by.** The estimator defined; the circuit family, depths, numbers of circuits and samples stated; the method for the ideal probabilities given; for circuits that cannot be simulated, the simpler circuits used for extrapolation and evidence that they behave like the full circuits; the measured circuit fidelity compared with the prediction from independently measured gate, preparation and measurement errors.

**Benchmark.** [12]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. A. Nielsen, A simple formula for the average gate fidelity of a quantum dynamical operation, Phys. Lett. A 303, 249 (2002); read as preprint arXiv:quant-ph/0205035 | doi:10.1016/S0375-9601(02)01272-0 |
| 2 | A. Hashim et al., Practical introduction to benchmarking and characterization of quantum computers, PRX Quantum 6, 030202 (2025); read as preprint arXiv:2408.12064, titled A practical introduction to benchmarking and characterization of quantum computers | doi:10.1103/PRXQuantum.6.030202 |
| 3 | E. Magesan et al., Scalable and robust randomized benchmarking of quantum processes, Phys. Rev. Lett. 106, 180504 (2011); read as preprint arXiv:1009.3639, titled Robust randomized benchmarking of quantum processes | doi:10.1103/PhysRevLett.106.180504 |
| 4 | J. M. Epstein et al., Investigating the limits of randomized benchmarking protocols, Phys. Rev. A 89, 062321 (2014); read as preprint arXiv:1308.2928 | doi:10.1103/PhysRevA.89.062321 |
| 5 | R. Harper et al., Statistical analysis of randomized benchmarking, Phys. Rev. A 99, 052350 (2019); read as preprint arXiv:1901.00535 | doi:10.1103/PhysRevA.99.052350 |
| 6 | T. Proctor et al., What randomized benchmarking actually measures, Phys. Rev. Lett. 119, 130502 (2017); read as preprint arXiv:1702.01853 | doi:10.1103/PhysRevLett.119.130502 |
| 7 | J. J. Wallman, Randomized benchmarking with gate-dependent noise, Quantum 2, 47 (2018); read as preprint arXiv:1703.09835 | doi:10.22331/q-2018-01-29-47 |
| 8 | R. Kueng et al., Comparing experiments to the fault-tolerance threshold, Phys. Rev. Lett. 117, 170502 (2016); read as preprint arXiv:1510.05653 | doi:10.1103/PhysRevLett.117.170502 |
| 9 | E. Magesan et al., Efficient measurement of quantum gate error by interleaved randomized benchmarking, Phys. Rev. Lett. 109, 080505 (2012); read as preprint arXiv:1203.4550 | doi:10.1103/PhysRevLett.109.080505 |
| 10 | C. J. Wood and J. M. Gambetta, Quantification and characterization of leakage errors, Phys. Rev. A 97, 032306 (2018); read as preprint arXiv:1704.03081 | doi:10.1103/PhysRevA.97.032306 |
| 11 | J. M. Gambetta et al., Characterization of addressability by simultaneous randomized benchmarking, Phys. Rev. Lett. 109, 240504 (2012); read as preprint arXiv:1204.6308 | doi:10.1103/PhysRevLett.109.240504 |
| 12 | S. Boixo et al., Characterizing quantum supremacy in near-term devices, Nat. Phys. 14, 595 (2018); read as preprint arXiv:1608.00263 | doi:10.1038/s41567-018-0124-x |
