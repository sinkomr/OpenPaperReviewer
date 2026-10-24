---
id: T-GATE-BENCHMARKING
name: Gate benchmarking
type: technique
field: physics/quantum-information
applies_when: the paper quotes a single- or two-qubit gate fidelity or error rate, or a circuit or layer fidelity, obtained by randomized benchmarking in any form, gate set tomography or cross-entropy benchmarking, or compares such a figure with a fault-tolerance threshold or other devices
version: "0.1"
---

# Gate benchmarking

Gate benchmarking is used to claim the error rate of quantum logic gates, of layers of gates or of whole circuits, often as a single fidelity that is compared with other devices or with a fault-tolerance threshold. The main methods are randomized benchmarking (RB) in its standard, interleaved and simultaneous forms, gate set tomography (GST) and cross-entropy benchmarking (XEB); each turns measured outcome probabilities into an error rate through a model of the noise, and each must handle state preparation and measurement (SPAM) errors, leakage out of the qubit subspace and crosstalk between qubits.

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

## 7. Gate set tomography: model fit and gauge

**Question.** For results from GST, does the paper report how well the model fits the data, the gauge in which gate errors are quoted, and how the error bars were obtained?

**Why it matters.** GST estimates gates, preparations and measurements together without pre-calibrated references, but the estimates rest on a Markovian model; a large model violation means that no gate set describes all of the data. Fidelity and diamond distance are not gauge invariant, so their values and error bars depend on the gauge optimization used.

**Resolved by.** A model-violation statistic, overall and per circuit; where the violation is significant, a discussion of its likely cause and a quantified allowance for out-of-model error, such as a wildcard error model; the gauge-optimization procedure stated and gauge-invariant quantities given where possible; the method and confidence level of the error bars.

**Benchmark.** [2], [12]

## 8. Cross-entropy benchmarking

**Question.** For a fidelity from XEB, does the paper state the estimator, how the ideal output probabilities were computed, and the assumptions that link the estimator to circuit fidelity and to errors per gate?

**Why it matters.** The estimator equals the circuit fidelity only under assumptions: random circuits deep enough for the ideal outputs to follow the Porter–Thomas distribution, and errors that drive the output towards the uniform distribution. The ideal probabilities must be computed classically, so for circuits beyond simulation the fidelity is extrapolated from simpler circuits, and errors per gate inferred from it rest on a model in which the circuit fidelity is a product of gate, preparation and measurement fidelities.

**Resolved by.** The estimator defined; the circuit family, depths, numbers of circuits and samples stated; the method for the ideal probabilities given; for circuits that cannot be simulated, the simpler circuits used for extrapolation and evidence that they behave like the full circuits; the measured circuit fidelity compared with the prediction from independently measured gate, preparation and measurement errors.

**Benchmark.** [13]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. A. Nielsen, A simple formula for the average gate fidelity of a quantum dynamical operation, Phys. Lett. A 303, 249–252 (2002); read as preprint arXiv:quant-ph/0205035 | doi:10.1016/S0375-9601(02)01272-0 | full text | Eq. (3): average gate fidelity equals (d times entanglement fidelity plus 1) divided by (d + 1), so the two measures differ by a dimension-dependent factor |
| 2 | A. Hashim, L. B. Nguyen, N. Goss, B. Marinelli, R. K. Naik, T. Chistolini, J. Hines, J. P. Marceaux, Y. Kim, P. Gokhale, T. Tomesh, S. Chen, L. Jiang, S. Ferracin, K. Rudinger, T. Proctor, K. C. Young, I. Siddiqi and R. Blume-Kohout, Practical introduction to benchmarking and characterization of quantum computers, PRX Quantum 6, 030202 (2025); read as preprint arXiv:2408.12064, titled A practical introduction to benchmarking and characterization of quantum computers | doi:10.1103/PRXQuantum.6.030202 | full text | Secs. IV.3.3.1–IV.3.3.2 and Table 2: average gate infidelity and entanglement infidelity defined and converted by a dimension factor. Secs. II.5.2 and IV.5.1: gauge freedom; RB error rates relate to the average gate set infidelity in a suitable gauge. Sec. III.6: leakage cannot be described by a trace-preserving qubit map. Sec. V.1.2: compiler rules that prevent parallel gates hide some crosstalk. Sec. V.2.1: unobserved leakage makes the RB decay a mixture of two exponentials. Sec. V.2.4: wildcard error models quantify out-of-model effects in GST |
| 3 | E. Magesan, J. M. Gambetta and J. Emerson, Scalable and robust randomized benchmarking of quantum processes, Phys. Rev. Lett. 106, 180504 (2011); read as preprint arXiv:1009.3639, titled Robust randomized benchmarking of quantum processes | doi:10.1103/PhysRevLett.106.180504 | full text | Eq. (6) and text around it: zeroth-order model A p^m + B, with SPAM errors absorbed into A and B; Eq. (5): error rate from p and dimension. Eq. (4) and Table 1: first-order model for gate-dependent noise; the zeroth-order model holds only when the noise varies little between gates; many lengths needed to estimate p |
| 4 | J. M. Epstein, A. W. Cross, E. Magesan and J. M. Gambetta, Investigating the limits of randomized benchmarking protocols, Phys. Rev. A 89, 062321 (2014); read as preprint arXiv:1308.2928 | doi:10.1103/PhysRevA.89.062321 | full text | Sec. III, Table 1 caption: 1.875 physical generators per Clifford on average. Sec. IV, generator-dependent unitaries: each generator given an equal share, r/1.875, of the Clifford error. Secs. VII and VIII: the interleaved estimate diverges when the interleaved gate's error is about ten times below the average Clifford error. Sec. II, product-twirl assumption: it can underestimate when errors partly cancel |
| 5 | R. Harper, I. Hincks, C. Ferrie, S. T. Flammia and J. J. Wallman, Statistical analysis of randomized benchmarking, Phys. Rev. A 99, 052350 (2019); read as preprint arXiv:1901.00535 | doi:10.1103/PhysRevA.99.052350 | full text | Sec. I and Sec. VI: the variance across random sequences grows with length, so fits over several lengths need weights that are not generally known. Sec. II: the offset removed exactly by randomly compiling a final state flip into the sequences. Secs. III–V: credible regions for the rate and guidance on lengths, sequences and shots |
| 6 | T. Proctor, K. Rudinger, K. Young, M. Sarovar and R. Blume-Kohout, What randomized benchmarking actually measures, Phys. Rev. Lett. 119, 130502 (2017); read as preprint arXiv:1702.01853 | doi:10.1103/PhysRevLett.119.130502 | full text | Abstract and introduction: under gate-dependent errors the RB rate and the average gate infidelity can differ by orders of magnitude; the infidelity depends on a non-unique representation (gauge), while the RB rate does not |
| 7 | J. J. Wallman, Randomized benchmarking with gate-dependent noise, Quantum 2, 47 (2018); read as preprint arXiv:1703.09835 | doi:10.22331/q-2018-01-29-47 | full text | Abstract and Sec. 4, remark: the decay parameter gives the fidelity of the average noise between ideal gates. Sec. 5: larger, possibly oscillating, departures at the shortest lengths. Sec. 8: these can make short sequences depart from the exponential fit, and such lengths should be left out of the fit |
| 8 | R. Kueng, D. M. Long, A. C. Doherty and S. T. Flammia, Comparing experiments to the fault-tolerance threshold, Phys. Rev. Lett. 117, 170502 (2016); read as preprint arXiv:1510.05653 | doi:10.1103/PhysRevLett.117.170502 | full text | Main text: thresholds are mostly stated for worst-case (diamond) error, while RB gives the average error; for unitary errors the worst-case error scales as the square root of the average error; unitarity and average error together bound the worst-case error |
| 9 | E. Magesan, J. M. Gambetta, B. R. Johnson, C. A. Ryan, J. M. Chow, S. T. Merkel, M. P. da Silva, G. A. Keefe, M. B. Rothwell, T. A. Ohki, M. B. Ketchen and M. Steffen, Efficient measurement of quantum gate error by interleaved randomized benchmarking, Phys. Rev. Lett. 109, 080505 (2012); read as preprint arXiv:1203.4550 | doi:10.1103/PhysRevLett.109.080505 | full text | Eqs. (4)–(5): estimate from the ratio of decay parameters with a systematic bound that shrinks with the reference error; exact for depolarizing noise; in the typical case the bounds overestimate; Table 1: bounds widen with coherent over-rotation |
| 10 | C. J. Wood and J. M. Gambetta, Quantification and characterization of leakage errors, Phys. Rev. A 97, 032306 (2018); read as preprint arXiv:1704.03081 | doi:10.1103/PhysRevA.97.032306 | full text | Sec. I: earlier models give a bi-exponential decay and cannot separate leakage and seepage. Sec. III: protocol that measures the computational-subspace population against sequence length to obtain leakage and seepage rates, and an average gate fidelity model that includes leakage |
| 11 | J. M. Gambetta, A. D. Córcoles, S. T. Merkel, B. R. Johnson, J. A. Smolin, J. M. Chow, C. A. Ryan, C. Rigetti, S. Poletto, T. A. Ohki, M. B. Ketchen and M. Steffen, Characterization of addressability by simultaneous randomized benchmarking, Phys. Rev. Lett. 109, 240504 (2012); read as preprint arXiv:1204.6308 | doi:10.1103/PhysRevLett.109.240504 | full text | Protocol section: addressability error defined as the difference between isolated and simultaneous error rates, with a test for correlated errors. Results and conclusion: the error of one qubit roughly doubled under simultaneous operation; benchmarking one component does not show its effect on the larger device |
| 12 | E. Nielsen, J. K. Gamble, K. Rudinger, T. Scholten, K. Young and R. Blume-Kohout, Gate set tomography, Quantum 5, 557 (2021); read as preprint arXiv:2009.07301 | doi:10.22331/q-2021-10-05-557 | full text | Abstract and Sec. 3: gates, preparations and measurements estimated self-consistently without pre-calibrated references; gauge freedom. Sec. 6.1, Eqs. (76)–(77): log-likelihood model-violation statistic overall and per circuit; large violation means no gate set fits all the data. Secs. 6.2 and 6.3.4: fidelity and diamond distance are not gauge invariant; error bars need a fixed gauge |
| 13 | S. Boixo, S. V. Isakov, V. N. Smelyanskiy, R. Babbush, N. Ding, Z. Jiang, M. J. Bremner, J. M. Martinis and H. Neven, Characterizing quantum supremacy in near-term devices, Nat. Phys. 14, 595–600 (2018); read as preprint arXiv:1608.00263 | doi:10.1038/s41567-018-0124-x | full text | Secs. II.1–II.2 and IV: Porter–Thomas output of deep random circuits; cross entropy difference needs classically computed ideal probabilities. Sec. III: circuit fidelity approximately equals the cross entropy difference under errors that make the output near uniform; Eq. (19): digital error model giving the circuit fidelity from gate, preparation and measurement error rates. Sec. II.2 and Sec. VI: fidelity extrapolated from simulable circuits for larger ones |
