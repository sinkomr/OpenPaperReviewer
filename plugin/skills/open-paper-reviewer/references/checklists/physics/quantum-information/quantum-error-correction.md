---
id: T-QUANTUM-ERROR-CORRECTION
name: Quantum error correction
type: technique
field: physics/quantum-information
applies_when: the paper encodes logical qubits in a quantum error-correcting or error-detecting code, or bases a claim on a logical error rate, error suppression with code distance, a threshold, or a logical qubit outperforming physical qubits
version: "0.1"
---

# Quantum error correction

## 1. Logical error rate per cycle

**Question.** How is the logical error rate per cycle obtained: from the decay of the logical fidelity over how many numbers of cycles, with which fit model, and how are the first cycles and the final readout treated?

**Why it matters.** A logical error rate taken from a single number of cycles, or from a fit that includes the first few cycles, mixes state preparation, final measurement and an initial transient in which the decay is not yet exponential. Rates per cycle and per unit time are not interchangeable: the cycle time links them, and the best operating point differs between storage and computation.

**Resolved by.** Logical fidelity plotted against the number of cycles over a range long enough to show the decay; the fit model stated, with the transient handled by an offset or by excluding early cycles; the conversion from fidelity to error per cycle given as a formula; the cycle time stated so that rates per unit time can be compared; uncertainties obtained from the fit or by resampling.

**Benchmark.** [1]

## 2. Logical states, error types and complete circuits

**Question.** Which logical states or bases were prepared and measured, does the code protect against both bit-flip and phase-flip errors, and do the reported figures include encoding, syndrome extraction and final logical readout?

**Why it matters.** A repetition code corrects only one type of error, so its performance shows classical protection, not protection of a quantum state. Results for one favourable input state, or for a circuit with error-free preparation or readout assumed, do not show that the full protocol protects arbitrary logical information.

**Resolved by.** Logical error rates for at least two conjugate bases, or for a set of input states, reported separately and on average; the code and the error types it corrects stated; the complete circuit from preparation to logical measurement included in the figure of merit; the preparation and syndrome-extraction circuits shown to be fault-tolerant, so that one fault cannot cause a logical error unnoticed.

**Benchmark.** [2], [3]

## 3. Post-selection and discarded runs

**Question.** Were any runs discarded because an error was detected, because leakage was flagged, or because a heralding or verification step failed, and if so what fraction was kept as a function of the number of cycles and the code size?

**Why it matters.** Discarding runs with detected errors turns error correction into error detection and lowers the reported logical error rate. The fraction of runs that survive falls with circuit length and code size, so a post-selected result can look favourable while describing a shrinking subset of runs that would not scale.

**Resolved by.** The acceptance fraction reported next to every post-selected logical error rate, for each number of cycles and each code size; results without post-selection shown alongside; break-even or threshold claims made on results without post-selection, or a clear statement that the logical error rate is conditional on acceptance and compared on that basis.

**Benchmark.** [2], [4]

## 4. Leakage and correlated errors

**Question.** Does the paper measure leakage out of the computational states and errors correlated in space or time, show how they evolve over cycles, and state how they were removed or accounted for?

**Why it matters.** The suppression of logical errors with code size assumes errors that are mostly independent and local. Leaked qubits can persist for many cycles and spread to neighbours, producing long-range correlations between detection events that standard decoders do not expect, so the suppression factor can drift down as the experiment runs.

**Resolved by.** Leakage populations measured over cycles for data and measurement qubits; detection-event rates shown against cycle number, with a stable plateau; correlations between detection events shown to be local; the leakage removal or reset scheme stated and its effect on the logical error rate and the suppression factor shown.

**Benchmark.** [3], [5]

## 5. Decoder dependence

**Question.** Which decoder was used, how were its weights or priors obtained and from which data, was decoding done in real time or afterwards, and how do the conclusions change with a different decoder?

**Why it matters.** The same syndrome data give different logical error rates, and different thresholds, with different decoders, and more accurate decoders are usually slower. Matching weights come from an error model or are estimated from measured data, and a neural decoder's training is specific to the noise it was trained on, so where these came from bears on the result. A decoder that cannot keep pace with the syndrome rate is not yet usable for computation.

**Resolved by.** The decoder named and its parameters stated; weights derived from a stated error model or estimated from measured data, with the data used for that estimate, or for training a decoder, identified and kept separate from the data on which the logical error rate is evaluated; results for at least one standard reference decoder alongside any specialised decoder; the decoding latency compared with the cycle time, or a statement that decoding was done offline.

**Benchmark.** [1], [6], [7]

## 6. Threshold and below-threshold claims

**Question.** Does a threshold or below-threshold claim rest on logical error rates measured for several code distances under the same conditions, and is the quoted threshold value tied to the noise model and decoder that apply to the experiment?

**Why it matters.** Below threshold, the logical error rate falls exponentially as the code grows; a single code beating its physical qubits shows only a pseudo-threshold that depends on code size. Threshold values range from about 11 % for a code with perfect measurements to around 1 % for full circuit noise, and change with the decoder, so comparing a measured error rate with a threshold from a different noise model says little.

**Resolved by.** Logical error rates for at least two, preferably three or more, code distances, with the suppression factor between successive distances and its uncertainty; the same decoder and conditions for every distance; the suppression factor shown to be stable over the number of cycles; any threshold value quoted with its noise model and decoder.

**Benchmark.** [3], [5], [6], [8]

## 7. Break-even and the physical baseline

**Question.** For a claim that a logical qubit outperforms physical qubits, which physical qubit or encoding is the baseline, was it measured on the same device at about the same time, and is the comparison for the same task: storage alone or gates as well?

**Why it matters.** A logical qubit can look better than physical qubits if it is compared with an average or poorly performing qubit, or with an encoding that is not the best available in the same system. A memory that outlives its physical qubits over long storage times has not shown that encoded operations have lower error than unencoded ones.

**Resolved by.** The baseline stated as the best physical qubit or simplest encoding in the same system, measured close in time to the logical data; lifetimes or error rates per unit time compared directly, with uncertainties; the comparison made without post-selection; separate figures of merit for memory and for computation where both are claimed.

**Benchmark.** [1], [2], [4]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | T. E. O'Brien et al., Density-matrix simulation of small surface codes under current and projected experimental noise, npj Quantum Inf. 3, 39 (2017) | doi:10.1038/s41534-017-0039-x |
| 2 | D. Gottesman, Quantum fault tolerance in small experiments, arXiv:1610.03507 (2016) | doi:10.48550/arXiv.1610.03507 |
| 3 | B. M. Terhal, Quantum error correction for quantum memories, Rev. Mod. Phys. 87, 307 (2015); read as preprint arXiv:1302.3428 | doi:10.1103/RevModPhys.87.307 |
| 4 | A. Joshi et al., Quantum information processing with bosonic qubits in circuit QED, Quantum Sci. Technol. 6, 033001 (2021); read as preprint arXiv:2008.13471 | doi:10.1088/2058-9565/abe989 |
| 5 | M. McEwen et al., Removing leakage-induced correlated errors in superconducting quantum error correction, Nat. Commun. 12, 1761 (2021) | doi:10.1038/s41467-021-21982-y |
| 6 | A. deMarti iOlius et al., Decoding algorithms for surface codes, Quantum 8, 1498 (2024); read as preprint arXiv:2307.14989, which carries a slightly different title | doi:10.22331/q-2024-10-10-1498 |
| 7 | S. T. Spitz et al., Adaptive weight estimator for quantum error correction in a time-dependent environment, Adv. Quantum Technol. 1, 1800012 (2018); read as preprint arXiv:1712.02360 | doi:10.1002/qute.201800012 |
| 8 | D. S. Wang et al., Surface code quantum computing with error rates over 1%, Phys. Rev. A 83, 020302 (2011); read as preprint arXiv:1009.3686, which carries a different title | doi:10.1103/PhysRevA.83.020302 |
