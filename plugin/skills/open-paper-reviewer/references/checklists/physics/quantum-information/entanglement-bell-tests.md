---
id: T-ENTANGLEMENT-BELL-TESTS
name: Entanglement and Bell tests
type: technique
field: physics/quantum-information
applies_when: the paper claims entanglement, genuine multipartite entanglement or nonlocality from an entanglement witness, a reconstructed state, an entanglement measure or a Bell-inequality violation such as CHSH, or claims a loophole-free or device-independent result
version: "0.1"
---

# Entanglement and Bell tests

## 1. What the test certifies and under which assumptions

**Question.** Does the paper say which conclusion its data support (entanglement assuming trusted, well-characterised measurements, violation of local realism, or a device-independent result), and does it list every assumption that conclusion needs beyond those of the test itself?

**Why it matters.** A witness or a reconstructed state certifies entanglement only if the measurements are what the model says they are, whereas a Bell violation certifies entanglement without trusting the devices but only once the loopholes are closed. Not every entangled state violates a Bell inequality, so a missing violation does not show separability, and a violation obtained with extra assumptions such as fair sampling does not support a device-independent claim.

**Resolved by.** The class of claim stated plainly; a list of the assumptions used, such as fair sampling, fair coincidences, independent trials or calibrated settings; claims about device independence, randomness or key distribution made only when the corresponding loopholes are closed.

**Benchmark.** [1], [2], [3], [4]

## 2. Detection efficiency and fair sampling

**Question.** What is the overall detection efficiency of the whole setup, from source to detector, how was it measured, and is it above the threshold for the inequality and state used, or does the result rely on the fair-sampling assumption?

**Why it matters.** When only some pairs are detected, the correlations among detected events can violate a Bell inequality even though a local model describes all events. Fair sampling assumes that the detected pairs are representative of all pairs emitted, which is not the same as constant detector efficiency. Without that assumption the CHSH inequality needs an efficiency above about 83 percent, and with a non-maximally entangled state and a Clauser-Horne inequality above two thirds.

**Resolved by.** The full-setup efficiency and how it was estimated reported for each party; a Clauser-Horne or Eberhard-type inequality evaluated on raw counts that include non-detections, or a heralded (event-ready) source; where fair sampling is assumed, a plain statement that the detection loophole is open.

**Benchmark.** [1], [2]

## 3. Coincidence windows, post-selection and subtraction

**Question.** How were events paired into coincidences (the window and how it was chosen), were any events removed by post-selection built into the setup, and was the violation obtained from raw counts or after subtracting accidental coincidences or background?

**Why it matters.** Pairing by a time window can produce a violation in a local model if the chance of a coincidence depends on the settings, which is a separate loophole from detection efficiency. Some interferometric schemes discard events by design, and then a local model can reproduce the ideal quantum correlations. Subtracting accidental coincidences can turn raw data that admit a local description into apparent violations.

**Resolved by.** The coincidence window and the coincidence efficiency reported, and the violation either bounded without assuming fair coincidences or the fair-coincidence assumption stated; post-selection avoided, or the assumptions that remove the resulting loophole stated; the violation shown on raw data, with accidentals made rare rather than subtracted.

**Benchmark.** [2]

## 4. Locality and choice of settings

**Question.** Does the paper give the space-time arrangement of the experiment (distances, the times of setting choice, measurement and outcome recording), and does it show how settings were chosen, how random they were and that each choice was space-like separated from the other party's measurement and from the emission event?

**Why it matters.** If settings change slowly or follow a pattern, a signal travelling no faster than light, or a local model that predicts the settings, can explain the correlations. Settings chosen passively, or chosen before the pair was emitted, do not ensure that they are independent of the hidden variables. For device-independent tasks in a quantum setting, isolation by other means can replace space-like separation, but a claim about local realism needs the timing.

**Resolved by.** A space-time diagram or timing budget showing space-like separation, with delays in electronics and detectors included; settings from an active random source whose generation time and quality are reported; where the locality loophole is open, a statement saying so and, for device-independent claims, how the devices were isolated.

**Benchmark.** [1], [2]

## 5. Statistical evidence for a violation

**Question.** Is the strength of the violation given as a p-value, or another bound on the probability of the data under any LHV model, that does not assume independent and identically distributed trials, rather than only as a number of standard deviations?

**Why it matters.** Quoting standard deviations assumes Gaussian statistics and independent trials. A local model with memory can exploit correlations between trials, so independent-trial statistics can overstate the evidence. A small violation in a finite sample can also arise from fluctuations.

**Resolved by.** A hypothesis test with a stated significance level, such as a martingale or binomial bound that holds for local models with memory; the number of trials stated; any assumption of independent trials stated.

**Benchmark.** [2], [6]

## 6. Measurement settings behind a witness

**Question.** For a witness or fidelity that assumes particular measurement bases, how well were the bases characterised, how large is the residual misalignment, and is the witness threshold corrected for it?

**Why it matters.** A witness built for ideal measurements can return a negative value for a separable state when the bases are slightly misaligned, so small, common calibration errors can produce false detections. The error grows with the number of parties, and the same misalignment lowers the fidelity of a reconstructed state.

**Resolved by.** The measurement bases characterised independently, for example with known reference states, and the residual misalignment reported; a witness bound shifted to remain valid for all separable or biseparable states at that misalignment; or a device-independent or semi-device-independent test that does not rely on the calibration.

**Benchmark.** [4], [5]

## 7. Multipartite and quantitative claims

**Question.** For a claim about many parties, a high dimension or an amount of entanglement, does the criterion used certify that specific property, such as genuine multipartite entanglement, entanglement depth or Schmidt number, and is any quantity reported as a bound rather than an exact value?

**Why it matters.** A state of N parties can be entangled without being genuinely N-partite entangled, for example as a product of entangled pairs, and different thresholds certify different properties. A fidelity above one half with a Greenberger-Horne-Zeilinger (GHZ) or graph state certifies genuine multipartite entanglement, but other fidelity thresholds certify other things. Most entanglement measures cannot be computed exactly from partial data, so measured values give bounds.

**Resolved by.** The property claimed defined, and the witness or criterion shown to certify exactly that property with its threshold derived or cited; the measured value compared with the threshold together with its uncertainty; entanglement measures reported as bounds derived from measured expectation values, with the assumptions stated.

**Benchmark.** [3], [4]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | N. Brunner et al., Bell nonlocality, Rev. Mod. Phys. 86, 419 (2014); read as preprint arXiv:1303.2849 | doi:10.1103/RevModPhys.86.419 |
| 2 | J.-Å. Larsson, Loopholes in Bell inequality tests of local realism, J. Phys. A: Math. Theor. 47, 424003 (2014); read as preprint arXiv:1407.0363 | doi:10.1088/1751-8113/47/42/424003 |
| 3 | O. Gühne and G. Tóth, Entanglement detection, Phys. Rep. 474, 1 (2009); read as preprint arXiv:0811.2803 | doi:10.1016/j.physrep.2009.02.004 |
| 4 | N. Friis et al., Entanglement certification from theory to experiment, Nat. Rev. Phys. 1, 72 (2018); read as preprint arXiv:1906.10929 | doi:10.1038/s42254-018-0003-5 |
| 5 | D. Rosset et al., Imperfect measurement settings: implications for quantum state tomography and entanglement witnesses, Phys. Rev. A 86, 062325 (2012); read as preprint arXiv:1203.0911 | doi:10.1103/PhysRevA.86.062325 |
| 6 | D. Elkouss and S. Wehner, (Nearly) optimal P values for all Bell inequalities, npj Quantum Inf. 2, 16026 (2016); read as preprint arXiv:1510.07233 | doi:10.1038/npjqi.2016.26 |
