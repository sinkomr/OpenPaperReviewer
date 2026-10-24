---
id: T-ENTANGLEMENT-BELL-TESTS
name: Entanglement and Bell tests
type: technique
field: physics/quantum-information
applies_when: the paper claims entanglement, genuine multipartite entanglement or nonlocality from an entanglement witness, a reconstructed state, an entanglement measure or a Bell-inequality violation such as CHSH, or claims a loophole-free or device-independent result
version: "0.1"
---

# Entanglement and Bell tests

Entanglement witnesses, entanglement measures and Bell tests are used to claim that a prepared state is entangled, how strongly or among how many parties, and that measured correlations cannot be explained by any local hidden-variable (LHV) model. A Bell test compares correlations with a bound such as that of the Clauser-Horne-Shimony-Holt (CHSH) inequality, and its conclusion holds only as far as the experiment closes the detection, locality and freedom-of-choice loopholes.

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

**Benchmark.** [2], [7]

## 6. Measurement settings behind a witness

**Question.** For a witness or fidelity that assumes particular measurement bases, how well were the bases characterised, how large is the residual misalignment, and is the witness threshold corrected for it?

**Why it matters.** A witness built for ideal measurements can return a negative value for a separable state when the bases are slightly misaligned, so small, common calibration errors can produce false detections. The error grows with the number of parties, and the same misalignment lowers the fidelity of a reconstructed state.

**Resolved by.** The measurement bases characterised independently, for example with known reference states, and the residual misalignment reported; a witness bound shifted to remain valid for all separable or biseparable states at that misalignment; or a device-independent or semi-device-independent test that does not rely on the calibration.

**Benchmark.** [4], [5]

## 7. Entanglement from a reconstructed state

**Question.** When fidelity, negativity or another measure is computed from a state reconstructed by tomography, which estimator was used, and are the uncertainties and entanglement bounds valid given the bias of that estimator?

**Why it matters.** Reconstructions that force a physical density matrix, such as maximum likelihood or least squares, are biased: they tend to underestimate fidelity and overestimate entanglement, most at low counts and for many qubits, and can show entanglement for a separable state. Bootstrapped error bars around such estimates inherit the bias and often fail to cover the true value.

**Resolved by.** Linear quantities such as fidelity evaluated directly from the data; nonlinear measures given as lower bounds with one-sided confidence regions, using a bounding operator chosen independently of the data; the estimator, counts per setting and error method stated; for larger systems, a witness that needs fewer measurements than full tomography.

**Benchmark.** [4], [6]

## 8. Multipartite and quantitative claims

**Question.** For a claim about many parties, a high dimension or an amount of entanglement, does the criterion used certify that specific property, such as genuine multipartite entanglement, entanglement depth or Schmidt number, and is any quantity reported as a bound rather than an exact value?

**Why it matters.** A state of N parties can be entangled without being genuinely N-partite entangled, for example as a product of entangled pairs, and different thresholds certify different properties. A fidelity above one half with a Greenberger-Horne-Zeilinger (GHZ) or graph state certifies genuine multipartite entanglement, but other fidelity thresholds certify other things. Most entanglement measures cannot be computed exactly from partial data, so measured values give bounds.

**Resolved by.** The property claimed defined, and the witness or criterion shown to certify exactly that property with its threshold derived or cited; the measured value compared with the threshold together with its uncertainty; entanglement measures reported as bounds derived from measured expectation values, with the assumptions stated.

**Benchmark.** [3], [4]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani and S. Wehner, Bell nonlocality, Rev. Mod. Phys. 86, 419 (2014); read as preprint arXiv:1303.2849 | doi:10.1103/RevModPhys.86.419 | full text | Secs. I.1 and I.2 (preprint numbering): locality defined through space-like separated events, with settings assumed independent of the hidden variable; a Bell violation acts as an entanglement detector robust to experimental imperfection. Sec. III.1.1: some entangled (Werner) states admit a local model. Sec. III.3.1: post-selection is to be treated as a nonlocal resource, linked to the detection loophole. Sec. IV.3.3, footnote 16: for device-independent randomness, isolation such as shielding can stand in for space-like separation. Sec. IV.3.4: device-independent key distribution needs a genuine violation, meaning the detection loophole closed |
| 2 | J.-Å. Larsson, Loopholes in Bell inequality tests of local realism, J. Phys. A: Math. Theor. 47, 424003 (2014); read as preprint arXiv:1407.0363 | doi:10.1088/1751-8113/47/42/424003 | full text | Sec. 1.4: subtracting accidentals opens a loophole and should be avoided. Sec. 1.5: finite samples need a proper hypothesis test. Secs. 2.1 to 2.3: fast switching, unpredictable settings, memory between runs handled by a supermartingale bound, active choices space-like separated from emission. Secs. 3.1 to 3.4: fair sampling differs from constant efficiency; thresholds of about 82.8 percent for CHSH and 2/3 for Clauser-Horne with non-maximally entangled states; event-ready setups. Secs. 3.5 to 3.7: coincidence loophole and bounds; post-selection built into some interferometers allows a local model. Sec. 4: state all extra assumptions and report whole-setup efficiency; loophole-free tests matter for device-independent cryptography |
| 3 | O. Gühne and G. Tóth, Entanglement detection, Phys. Rep. 474, 1–75 (2009); read as preprint arXiv:0811.2803 | doi:10.1016/j.physrep.2009.02.004 | full text | Sec. 3.3 (preprint numbering): full separability, m-separability and genuine N-partite entanglement defined; a product of entangled pairs is entangled but not genuinely N-partite entangled. Sec. 3.6.2: witnesses of the form one half minus the GHZ or graph-state projector, so fidelity above 1/2 certifies genuine multipartite entanglement; Secs. 3.1.2 and 3.6.1: a different threshold, 3/4, certifies three-qubit GHZ-class entanglement. Sec. 5.1.2: a violation implies entanglement, but some entangled states violate no Bell inequality, so Bell inequalities are non-optimal witnesses |
| 4 | N. Friis, G. Vitagliano, M. Malik and M. Huber, Entanglement certification from theory to experiment, Nat. Rev. Phys. 1, 72–87 (2018); read as preprint arXiv:1906.10929 | doi:10.1038/s42254-018-0003-5 | full text | Introduction: which methods apply depends on the assumptions made about states and measurements; estimation is distinguished from certification. Entanglement quantification and bounding witnessed entanglement: computing most measures is hard even with the full density matrix, so lower bounds from a few expectation values are used. Statistical error and finite data: tomography scales poorly; ignoring errors in reconstruction can overestimate entanglement and underestimate fidelity; confidence bounds such as Hoeffding's. Multipartite and high-dimensional sections: genuine multipartite entanglement, entanglement depth and Schmidt-number witnesses |
| 5 | D. Rosset, R. Ferretti-Schöbitz, J.-D. Bancal, N. Gisin and Y.-C. Liang, Imperfect measurement settings: implications for quantum state tomography and entanglement witnesses, Phys. Rev. A 86, 062325 (2012); read as preprint arXiv:1203.0911 | doi:10.1103/PhysRevA.86.062325 | full text | Secs. IV.1 to IV.3: with misaligned bases a two-qubit witness certifies a separable state as entangled for any non-zero misalignment; GHZ-type witnesses show similar errors that depend on the number of qubits times the misalignment; a witness shifted by a misalignment-dependent term stays valid. Sec. III: misalignment of a few degrees lowers tomographic fidelity at first order |
| 6 | C. Schwemmer, L. Knips, D. Richart, T. Moroder, M. Kleinmann, O. Gühne and H. Weinfurter, Systematic errors in current quantum state tomography tools, Phys. Rev. Lett. 114, 080403 (2015); read as preprint arXiv:1310.8465 | doi:10.1103/PhysRevLett.114.080403 | full text | Abstract and Figs. 1 to 3: maximum-likelihood and least-squares reconstructions underestimate fidelity, more so at low counts and for more qubits; any method that always returns a physical state is biased. Fig. 4: they overestimate negativity and can show entanglement for a separable state. Bootstrap appendix: bootstrapped error bars inherit the bias and often miss the true value. Proposed method: linear evaluation and linearised bounds with Hoeffding confidence regions, operator chosen independently of the data |
| 7 | D. Elkouss and S. Wehner, (Nearly) optimal P values for all Bell inequalities, npj Quantum Inf. 2, 16026 (2016); read as preprint arXiv:1510.07233 | doi:10.1038/npjqi.2016.26 | full text | Sec. I (preprint numbering): counting standard deviations from the best local model assumes Gaussian statistics and independent attempts, leaving the memory loophole open; the p-value is the largest probability of data at least as extreme under any local model. Sec. III.1.2: a binomial bound valid for local models with arbitrary memory. Sec. III.2: a general bound from a supermartingale argument. Sec. IV.1: the number of trials must not depend on the data |
