---
id: T-QUANTUM-KEY-DISTRIBUTION
name: Quantum key distribution and networks
type: technique
field: physics/quantum-information
applies_when: the paper reports a quantum key distribution experiment, protocol or security proof, a secret key rate or transmission distance, an attack or countermeasure on QKD hardware, or entanglement distribution, quantum memories or quantum repeaters for a quantum network
version: "0.1"
---

# Quantum key distribution and networks

Quantum key distribution (QKD) is used to claim that two parties have generated a secret key whose security rests on quantum physics, at a stated secret key rate over a stated distance or channel loss. Related work on entanglement distribution and quantum repeaters claims to share entangled states between distant nodes, or to beat the rate that direct transmission over the same loss allows.

## 1. Security model and trusted devices

**Question.** Does the paper state the protocol, the class of attacks the key is proved secure against (for example collective or general coherent attacks), the security definition used, and which parts of the equipment are assumed trusted or characterised, including how the classical channel is authenticated?

**Why it matters.** Security proofs assume ideal or fully characterised sources and detectors, an authenticated classical channel and an eavesdropper limited only by quantum physics. Real devices depart from these models, and a rate proved only against a restricted family of attacks, or under a trusted-detector assumption, is not the same claim as a key secure against any attack. Fidelity-type measures are not composable, so the security level is usually stated as a trace-distance parameter.

**Resolved by.** The protocol and its security proof named, with the attack class and the composable security parameter stated; a list of the device assumptions used, such as a characterised source, trusted detectors or untrusted measurement devices as in measurement-device-independent (MDI) or device-independent schemes; the authentication method and any pre-shared key stated.

**Benchmark.** [1], [2]

## 2. Finite-key analysis

**Question.** Is the reported key length or rate computed with a finite-key analysis for the block size actually used, with the security and correctness parameters stated, or is it an asymptotic rate?

**Why it matters.** Asymptotic formulas assume infinitely many signals. With a finite block, error rates and single-photon yields must be bounded from a sample, the failure probabilities add up, and the extractable key is smaller, sometimes far smaller, than the asymptotic value at the same error rate. Below some block size no key can be extracted at all.

**Resolved by.** The block size, the number of signals used for parameter estimation, the abort conditions, and the values of the secrecy and correctness parameters stated; the key length obtained from a named finite-key bound; any asymptotic rate labelled as such and not compared directly with finite-key results.

**Benchmark.** [1], [2], [3]

## 3. Source: multiphoton pulses, decoy states and phase randomisation

**Question.** When the source is an attenuated laser, does the paper use a decoy-state or other analysis that bounds the single-photon contribution, and does it show that the assumptions behind that analysis hold for the source used, such as random phases and stable, correctly set intensities?

**Why it matters.** Weak coherent pulses sometimes contain more than one photon, and a photon-number-splitting attack can extract key information from these pulses without raising the error rate. The decoy-state method bounds the single-photon yield and error rate by varying the intensity, but its estimates rest on phase-randomised pulses with a known photon-number distribution, and imperfect phase randomisation, encoding flaws or light injected from outside open further side channels at the source.

**Resolved by.** The intensities, their probabilities and the measured gains and error rates for each intensity reported; how phase randomisation is achieved and checked; the intensity settings and their stability checked, since the analysis assumes known intensities; measures against light injected into the transmitter, such as isolation and monitoring, stated.

**Benchmark.** [2], [4]

## 4. Detector side channels

**Question.** Does the paper state which detector imperfections its security analysis covers, and does it show how the receiver is protected against known detector attacks such as bright-light blinding, time-shift and efficiency-mismatch attacks, or use a scheme in which the detectors need not be trusted?

**Why it matters.** Single-photon detectors can be blinded by bright light and then triggered by classical pulses, letting an eavesdropper control which detector clicks without raising the error rate. Gated detectors with time-dependent or mismatched efficiencies open similar attacks. A proof that assumes ideal or calibrated detectors does not cover these behaviours unless the countermeasure is part of the analysis.

**Resolved by.** The detector model assumed in the proof stated; countermeasures such as monitoring of incoming optical power described and included in the security argument, with tests showing they work; or an MDI or device-independent configuration in which the detection side is treated as untrusted, with the remaining assumptions on the source stated.

**Benchmark.** [2], [5]

## 5. What the reported key rate includes

**Question.** Is the quoted rate a secret key rate after sifting, error correction and privacy amplification, with the error-correction leakage taken from the code actually run rather than an assumed efficiency, and is it stated per pulse or per second and whether it was obtained in a full run or estimated from measured parameters?

**Why it matters.** The secret key rate is the raw rate multiplied by the secret fraction, and the secret fraction depends on the error rate, the information leaked during error correction and the security analysis. A rate computed from measured detection and error rates with an assumed error-correction efficiency, or a steady-state rate that ignores post-processing time and stability, can differ from the key actually extracted.

**Resolved by.** Raw, sifted and final key lengths reported for a stated acquisition time; the error-correction method, its measured leakage or efficiency and the privacy amplification stated; the units of the rate given; key extracted in real time distinguished from rates simulated from measured parameters.

**Benchmark.** [1], [2], [3]

## 6. Distance, loss and the repeaterless bound

**Question.** How is the channel described (deployed fibre, fibre spool or a variable attenuator, with the loss in dB and what it includes), and when the paper compares its rate with other experiments or with the repeaterless bound, does it count channel uses and losses in the same way for both?

**Why it matters.** Without repeaters, the secret key capacity of a lossy channel is bounded by a function of its transmissivity, about 1.44 times the transmissivity in bits per channel use at high loss. Whether a result beats this bound depends on what is counted as the channel and as a channel use, for example whether detector inefficiency is included in the loss and how many optical modes each pulse occupies. Rates quoted in different units, with different security levels or over low-loss fibre, are not directly comparable.

**Resolved by.** The channel type, length, measured loss and fibre attenuation stated; the transmissivity used in any comparison with the repeaterless bound defined, with the treatment of detector efficiency and modes per pulse stated; comparisons with other work made in the same units and at the same security level.

**Benchmark.** [2], [6], [7], [10]

## 7. Continuous-variable QKD: calibration and noise assumptions

**Question.** For continuous-variable QKD, how was the shot-noise unit calibrated, how were transmittance and excess noise estimated, which noise sources are treated as trusted rather than attributed to the eavesdropper, and what reconciliation efficiency was achieved?

**Why it matters.** All measured variances are expressed in shot-noise units, so an error in that calibration shifts the estimated excess noise and transmittance on which the key rate depends. Treating detector noise as trusted, or transmitting the local oscillator through the channel, adds assumptions that an eavesdropper might exploit. At long distance the key rate is very sensitive to excess noise and to reconciliation efficiency.

**Resolved by.** The calibration procedure for the shot-noise unit and electronic noise described, with how often it was repeated; excess noise reported with the point it is referred to; the trusted-noise assumption stated, ideally with the rate also given without it; the local oscillator scheme stated; the measured reconciliation efficiency and frame-error rate reported.

**Benchmark.** [1], [8]

## 8. Entanglement distribution and quantum repeaters

**Question.** For claims about entanglement distribution, quantum memories or repeaters, does the paper report the heralding scheme, the distribution rate and the fidelity of the shared state, the memory efficiency and storage time compared with the communication time between nodes, and the physical separation of the nodes, and does it compare its rate with direct transmission over the same loss?

**Why it matters.** A repeater helps only if entanglement in each link is heralded and stored until neighbouring links succeed, so memories must hold states for at least the classical communication time and their efficiency enters the rate directly. Nodes in one laboratory joined by fibre spools, or networks of trusted relays that measure and resend signals, do not show the same thing as a repeater between distant nodes. An advantage over direct transmission is shown only when the rate exceeds the repeaterless bound for the same channel.

**Resolved by.** The heralding signal and the rate of heralded events stated; fidelity of the distributed state measured; memory efficiency, coherence or storage time and multimode capacity compared with the link length and communication time; the node separation and channel stated; trusted nodes identified as such; the rate compared with direct transmission and with the repeaterless bound using the same loss accounting.

**Benchmark.** [6], [7], [9]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | V. Scarani, H. Bechmann-Pasquinucci, N. J. Cerf, M. Dušek, N. Lütkenhaus and M. Peev, The security of practical quantum key distribution, Rev. Mod. Phys. 81, 1301 (2009); read as preprint arXiv:0802.4155 | doi:10.1103/RevModPhys.81.1301 | full text | Sec. II.2.1: classical channel must be authenticated, using a pre-shared key for unconditional security. Secs. II.2.4 and II.3: secret key rate as raw rate times secret fraction; composable trace-distance security; finite-key corrections not negligible, with an example of a much lower secret fraction than the asymptotic one. Sec. VII.1 and VII.2: platforms differ in security level, curves are steady-state rates ignoring post-processing time, security must be assessed with measured values; calibrated versus uncalibrated detector scenarios; continuous-variable parameters include electronic noise and reconciliation efficiency. Sec. VIII.1.1: no key below about 10^5 signals |
| 2 | F. Xu, X. Ma, Q. Zhang, H.-K. Lo and J.-W. Pan, Secure quantum key distribution with realistic devices, Rev. Mod. Phys. 92, 025002 (2020); read as preprint arXiv:1903.09051 | doi:10.1103/RevModPhys.92.025002 | full text | Secs. I.3 and II.3: proofs assume ideal sources and detectors, and deviations open loopholes. Secs. II.1 and II.2.1: composable security parameter, fidelity-based measure not composable. Secs. II.4.2, III.5.3 and III.5.4: finite-size bounds on the phase error rate, failure probabilities add. Sec. III.5.1: error-correction cost written with an efficiency factor above one. Secs. IV.1, IV.3 and V: photon-number splitting, decoy states, non-random phase, encoding flaws, and Trojan-horse attacks with isolators as countermeasure and leakage fed into privacy amplification. Sec. IV.2: efficiency-mismatch, time-shift and detector-control attacks; photocurrent-monitoring countermeasures called ad hoc. Sec. VI.2: MDI-QKD removes detection side channels but needs a characterised source. Sec. VI.3: linear rate-loss bound without repeaters, compared with twin-field rates. Secs. VI.2.4, VI.3 and VIII.2: experimental rates quoted in bps, kbps and Mbps, some projected asymptotic values, some over ultralow-loss fibre |
| 3 | M. Tomamichel, C. C. W. Lim, N. Gisin and R. Renner, Tight finite-key analysis for quantum cryptography, Nat. Commun. 3, 634 (2012); read as preprint arXiv:1103.4130 | doi:10.1038/ncomms1631 | full text | Abstract and Introduction: the asymptotic resource assumption cannot be met in practice. Results, security definitions: separate correctness and secrecy parameters adding to the total security parameter; robustness. Results and Supplementary Note 2: statistical deviation in parameter estimation from a sampling bound; error-correction leakage counted. Discussion and Table 2: key rate rises with block size, deviation necessary in any finite-key analysis |
| 4 | H.-K. Lo, X. Ma and K. Chen, Decoy state quantum key distribution, Phys. Rev. Lett. 94, 230504 (2005); read as preprint arXiv:quant-ph/0411004 | doi:10.1103/PhysRevLett.94.230504 | full text | Introduction: multiphoton pulses from attenuated lasers allow a photon-number-splitting attack. Combining decoy state idea with GLLP: earlier analysis limited distance to about 30 km for the parameters studied. General theory and Essence of the decoy state idea: decoy and signal states share yields and error rates, so varying intensity bounds the single-photon yield and error rate; the analysis assumes phase-randomised coherent states with Poisson photon-number statistics |
| 5 | L. Lydersen, C. Wiechers, C. Wittmann, D. Elser, J. Skaar and V. Makarov, Hacking commercial quantum cryptography systems by tailored bright illumination, Nat. Photon. 4, 686–689 (2010); read as preprint arXiv:1008.4593 | doi:10.1038/nphoton.2010.214 | full text | Abstract and main text: bright light blinds avalanche photodiodes into linear mode, and bright trigger pulses then control clicks without raising the error rate or dark counts; the attack is argued to apply to most such systems. Closing paragraphs: a power-meter countermeasure must be included in the security proof; remaining imperfections must be incorporated into security proofs and detectors tested for side channels |
| 6 | S. Pirandola, R. Laurenza, C. Ottaviani and L. Banchi, Fundamental limits of repeaterless quantum communications, Nat. Commun. 8, 15043 (2017); read as preprint arXiv:1510.08863 | doi:10.1038/ncomms15043 | full text | Introduction: the bound is the limit only quantum repeaters can surpass. Results, Fundamental rate-loss scaling in quantum optical communications: secret key capacity of the lossy channel is minus log2 of one minus transmissivity, about 1.44 times transmissivity bits per channel use at high loss; multiplied by bandwidth for a multimode fibre; Fig. 6 compares it with protocol rates such as decoy-state BB84, computed assuming unit detector efficiency |
| 7 | K. Azuma, S. E. Economou, D. Elkouss, P. Hilaire, L. Jiang, H.-K. Lo and I. Tzitrin, Quantum repeaters: from quantum networks to the quantum internet, Rev. Mod. Phys. 95, 045006 (2023); read as preprint arXiv:2212.10820 | doi:10.1103/RevModPhys.95.045006 | full text | Sec. I: trusted-relay networks are secure only if the nodes are trusted, unlike repeaters. Sec. III.1.3: heralded links stored in memories until all succeed; repeaterless bounds. Sec. IV.1: per-pulse bound counting two modes per pulse; memory-assisted schemes keep their advantage only when coherence time is long compared with the required multiplexing time. Sec. V.1: coherence time as main memory figure of merit, link length well below light speed times coherence time. Secs. IV.3, V.3 and V.7: demonstrations with memories metres apart, over fibre spools, or below the direct-transmission limit |
| 8 | F. Laudenbach, C. Pacher, C.-H. F. Fung, A. Poppe, M. Peev, B. Schrenk, M. Hentschel, P. Walther and H. Hübel, Continuous-variable quantum key distribution with Gaussian modulation: the theory of practical implementations, Adv. Quantum Technol. 1, 1800011 (2018); read as preprint arXiv:1703.09278 | doi:10.1002/qute.201800011 | full text | Introduction: transmitting the local oscillator through the channel opens security loopholes; local local oscillator schemes. Ch. 6.3: strict versus loose (trusted-noise) assumptions. Ch. 7: parameter estimation of transmittance and excess noise; calibration of shot-noise units by measuring vacuum and separating receiver noise. Ch. 3: excess noise referred to input or output. Ch. 9: low excess-noise thresholds at long distance and minimum reconciliation efficiency for a positive key |
| 9 | N. Sangouard, C. Simon, H. de Riedmatten and N. Gisin, Quantum repeaters based on atomic ensembles and linear optics, Rev. Mod. Phys. 83, 33 (2011); read as preprint arXiv:0906.2699 | doi:10.1103/RevModPhys.83.33 | full text | Sec. I: memories let heralded entanglement wait for neighbouring links, and one must know when entanglement is established. Secs. II.1 to II.4: storage time must be comparable to the distribution time, memory and detector efficiencies enter swapping probabilities, multi-pair emission reduces fidelity, and limited attempts per link motivate multimode memories (Secs. III.3 and III.4). Secs. II.3.2, III.1.3, III.2.2 and IV.1: repeater rates compared with direct transmission, with cross-over distances of several hundred kilometres |
| 10 | M. Minder, M. Pittaluga, G. L. Roberts, M. Lucamarini, J. F. Dynes, Z. L. Yuan and A. J. Shields, Experimental quantum key distribution beyond the repeaterless secret key capacity, Nat. Photon. 13, 334–338 (2019); read as preprint arXiv:1910.01951 | doi:10.1038/s41566-019-0377-7 | full text | Results, discussion of Fig. 3 and its caption: the repeaterless capacity is plotted both with ideal detectors and with the measured detection efficiency and station losses included; which bound a rate exceeds depends on whether detector and station losses are counted in the channel |
