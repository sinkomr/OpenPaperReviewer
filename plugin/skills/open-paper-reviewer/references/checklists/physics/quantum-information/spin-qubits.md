---
id: T-SPIN-QUBITS
name: Semiconductor spin qubits
type: technique
field: physics/quantum-information
applies_when: the paper reports quantum-dot or donor spin qubits in silicon, germanium or III-V semiconductors, or bases a claim on spin readout fidelity, valley splitting, coherence times (T1, T2*, T2), charge noise, or single- or two-qubit gate fidelities measured in such devices
version: "0.1"
---

# Semiconductor spin qubits

Semiconductor spin qubits store information in the spin of an electron or hole confined in a gate-defined quantum dot or bound to a donor atom, and are read out by spin-to-charge conversion with a nearby charge sensor, such as a single-electron transistor (SET), a quantum point contact (QPC) or a sensor read by radio-frequency (rf) reflectometry. Papers use them to claim a readout fidelity, a valley splitting, relaxation and coherence times (T1, the dephasing time T2* and echo or dynamical-decoupling times T2), a charge-noise level, and single- and two-qubit gate fidelities, often from randomized benchmarking (RB).

## 1. Charge occupation and the identity of the qubit

**Question.** Does the paper show how many electrons or holes occupy each dot, or for a donor, that the signal comes from a single donor of the stated species and charge state?

**Why it matters.** Spin filling, valley and orbital levels, and the meaning of a spin state all depend on the number of charges in the dot. Transport current can fall below the noise floor before the last electron leaves, so the absence of transport does not show that a dot is empty. For donors, the electron resonance is split by the hyperfine interaction with the nucleus, and the number and spacing of the lines are set by the nuclear spin and hyperfine constant, which differ between donor species, so the spectrum shows which donor and which nuclear state are present.

**Resolved by.** Charge-sensor stability diagrams that follow the occupancy down to zero, with no further transitions over a wide gate range; the occupancy stated for each qubit; for donors, the resonance spectrum with the hyperfine splitting expected for the species, and the nuclear spin state stated or controlled during the experiments.

**Benchmark.** [1], [2]

## 2. Spin-to-charge conversion and readout fidelity

**Question.** Which spin-to-charge conversion is used (energy-selective tunnelling to a reservoir, Pauli spin blockade or another scheme), how is the single-shot readout fidelity defined and obtained, and are the error rates for each spin state given separately?

**Why it matters.** Energy-selective readout works only when the Zeeman energy is well above the thermal broadening set by the electron temperature, and when the tunnel rates match the measurement bandwidth: tunnelling that is too fast is missed, and tunnelling that is too slow lets the spin relax first. The threshold that assigns each shot trades missed events against noise counted as events, and the two spin states usually have different errors. A visibility (the sum of the two fidelities minus one), an average fidelity and a fidelity for one state alone are different quantities.

**Resolved by.** The conversion scheme, magnetic field, electron temperature and tunnel rates stated; histograms of the single-shot signal with the threshold marked; fidelities for each state, the definition of any combined figure, and how they were obtained (from a fit or a model of the histograms, or from preparing known states); readout errors stated separately from initialisation errors.

**Benchmark.** [3], [4], [5], [7]

## 3. Measurement time, signal-to-noise and relaxation during readout

**Question.** What integration time and sensor bandwidth were used for single-shot readout, how was the signal-to-noise ratio (SNR) defined, and is relaxation of the excited state during the readout window included in the fidelity?

**Why it matters.** A longer integration lowers the sensor noise but gives the excited state more time to relax, and a relaxed state is counted as the other outcome. The best fidelity therefore lies at a compromise set by the SNR and the relaxation time, and the fidelity of the excited state falls first when T1 is short. Conventions for SNR and charge sensitivity differ between papers, sensitivities measured in the frequency domain can look better than the time-domain performance that matters for readout, and values given for different integration times cannot be compared without conversion.

**Resolved by.** The integration time, bandwidth and sensor type stated with the fidelity; the SNR or sensitivity definition given, preferably from time-domain data; T1 at the readout point measured and its effect on the fidelity shown, for example by fidelity against integration time; the readout time quoted alongside any comparison with other work.

**Benchmark.** [4], [5], [6]

## 4. Valley splitting

**Question.** For silicon devices, does the paper state the valley splitting of the dots that host the qubits, how it was measured, and how it compares with the electron temperature and the Zeeman energy used?

**Why it matters.** Silicon has degenerate conduction-band valleys, and the splitting between the two lowest valley states depends on atomic-scale details of the interface, the alloy and the electric field, so it varies widely from dot to dot even on one wafer. A small splitting adds states outside the qubit subspace, allows thermal population and leakage, can lift Pauli spin blockade, and causes a sharp drop in T1 when the Zeeman energy matches it. A value from one dot, or from a different device, need not hold for the dots used as qubits.

**Resolved by.** The valley splitting measured on the qubit dots, by magnetospectroscopy, excited-state spectroscopy, the field of a relaxation hotspot or another stated method, with its uncertainty; the operating field chosen away from the hotspot and the splitting shown to be large compared with the thermal energy; where several dots are measured, the spread reported.

**Benchmark.** [1], [7], [8]

## 5. Which coherence time, measured how

**Question.** For each coherence time quoted, does the paper say which sequence produced it (Ramsey, Hahn echo or a named dynamical-decoupling sequence with its number of pulses), what decay form was fitted, and, for T2*, over how long the data were averaged?

**Why it matters.** T2*, the Hahn-echo time and dynamical-decoupling times filter the noise spectrum differently, so they differ by orders of magnitude for the same qubit and are not interchangeable. With noise rising towards low frequency, the measured T2* depends on the total averaging time, which sets the low-frequency cut-off, so it is not a fixed property of the qubit. Gaussian and exponential decays are hard to tell apart, and the fitted time depends on which is assumed.

**Resolved by.** Each time labelled with its sequence and pulse number; the fit function stated, with free decay exponents reported where used; for T2*, the total measurement time or number of averages given; comparisons with other work made between times from the same kind of sequence.

**Benchmark.** [2], [5], [7]

## 6. Attributing decoherence to a noise source

**Question.** When the paper names the noise that limits T2* or T2 (nuclear spins, charge noise, or another source), does it support the attribution with a measurement, and does it state the isotopic composition of the host and any magnetic field gradient that couples charge to spin?

**Why it matters.** Nuclear spins of isotopes such as silicon-29 or those in III-V materials give a slowly varying field that limits T2*, and isotopic enrichment reduces it. Charge noise does not act on the spin directly but couples through a micromagnet field gradient or spin-orbit interaction, so the same charge noise gives different dephasing in different devices. The shape of the noise spectrum, which multi-pulse sequences can probe, distinguishes sources that a single coherence time cannot.

**Resolved by.** The isotopic composition, for example the residual silicon-29 concentration, stated; the field gradient or spin-orbit mechanism and the qubit's sensitivity to gate voltage given; the noise spectrum measured by dynamical-decoupling or other noise spectroscopy and compared with the attributed source; where a source is excluded, a measurement or estimate of its contribution.

**Benchmark.** [2], [7]

## 7. Charge-noise figures

**Question.** How was the quoted charge noise measured (from a sensor or dot current on the flank of a Coulomb peak, or from fluctuations of the qubit frequency), at what frequency and over what frequency range, and how was it converted to an energy?

**Why it matters.** Converting current fluctuations into energy fluctuations uses the slope of the Coulomb peak and a lever arm that varies between gates and devices, and the linear conversion holds only when the fluctuation is small compared with the peak width. Charge noise is usually quoted as an amplitude at 1 Hz from a roughly 1/f spectrum, but spectra often contain features from individual fluctuators, and the value depends on temperature and varies from dot to dot. Instrument noise and pickup add to the measured spectrum unless they are checked.

**Resolved by.** The method, lever arm and how it was measured, and the slope or operating point stated; the full spectrum shown with the fit range and exponent; reference measurements, for example at the top of the peak or in Coulomb blockade, showing that the signal is charge noise and not instrument noise; temperature stated and the spread over dots reported.

**Benchmark.** [7], [9]

## 8. Conditions behind a gate fidelity

**Question.** For each single- or two-qubit gate fidelity quoted, does the paper say whether it is per Clifford or per elementary gate, which calibration, recalibration, prepulses, waits between shots or frequency feedback were used while it was measured, and whether shifts of the qubit frequency caused by the control pulses were measured?

**Why it matters.** Many spin-qubit papers quote an error per elementary gate, typically two to three times smaller than the error per Clifford and obtained by a conversion that is not well founded. Microwave and baseband control pulses shift spin-qubit frequencies by amounts that depend on the recent pulse history, so a fidelity reached with prepulses, long waits between shots or qubit-specific calibration may not hold when the qubit runs in a circuit, and idle neighbouring qubits pick up phase errors from these shifts.

**Resolved by.** The Clifford fidelity reported with any per-gate figure and the conversion used; the calibration procedure, how often it was repeated, and any prepulses, waits or feedback on the qubit frequency stated; frequency shifts from the control pulses measured and shown to be small or compensated, including their effect on idle qubits; the protocol for each two-qubit gate fidelity stated.

**Benchmark.** [5], [7], [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | F. A. Zwanenburg, A. S. Dzurak, A. Morello, M. Y. Simmons, L. C. L. Hollenberg, G. Klimeck, S. Rogge, S. N. Coppersmith and M. A. Eriksson, Silicon quantum electronics, Rev. Mod. Phys. 85, 961–1019 (2013); read as preprint arXiv:1206.5202 | doi:10.1103/RevModPhys.85.961 | full text | Secs. IV.3 and IV.4: transport current can fall below the noise level before the last electron leaves, and a charge sensor tracks occupancy down to the last electron, confirmed by no further transitions over a wide gate range. Secs. III.1 and III.2: valley splitting depends on atomic-scale interface details, steps, alloy disorder and electric field, varies widely between devices, and a second valley can lift Pauli spin blockade. Sec. IV.5.2: valley-orbit splitting found from a kink where the Zeeman energy matches it |
| 2 | A. Morello, J. J. Pla, P. Bertet and D. N. Jamieson, Donor spins in silicon for quantum technologies, Adv. Quantum Technol. 3, 2000005 (2020); read as preprint arXiv:2009.04081 | doi:10.1002/qute.202000005 | full text | Sec. II.1 and Table 1: the donor electron resonance frequency depends on the nuclear spin state through the hyperfine interaction, and each group-V donor has its own nuclear spin and hyperfine constant. Sec. II.1: readout by spin-to-charge conversion detected with an SET. Sec. III and Table 2: natural silicon contains about 4.7% silicon-29, enrichment extends coherence, and coherence is quoted separately as T2* (Ramsey), Hahn-echo and CPMG times that differ widely |
| 3 | A. Morello, J. J. Pla, F. A. Zwanenburg, K. W. Chan, K. Y. Tan, H. Huebl, M. Möttönen, C. D. Nugroho, C. Yang, J. A. van Donkelaar, A. D. C. Alves, D. N. Jamieson, C. C. Escott, L. C. L. Hollenberg, R. G. Clark and A. S. Dzurak, Single-shot readout of an electron spin in silicon, Nature 467, 687–691 (2010); read as preprint arXiv:1003.2679 | doi:10.1038/nature09392 | full text | Text with Figs. 1 and 2: energy-selective tunnelling needs a Zeeman splitting larger than thermal broadening at the electron temperature, and the read level must sit between the two spin levels. Fig. 4 and text: fidelities defined separately for each spin state from histograms and a threshold, with visibility as their sum minus one; a low threshold counts noise as events, a high one misses real events; tunnel times compared with the measurement bandwidth |
| 4 | A. West, B. Hensen, A. Jouan, T. Tanttu, C. H. Yang, A. Rossi, M. F. Gonzalez-Zalba, F. E. Hudson, A. Morello, D. J. Reilly and A. S. Dzurak, Gate-based single-shot readout of spins in silicon, Nat. Nanotechnol. 14, 437–441 (2019); read as preprint arXiv:1809.01864 | doi:10.1038/s41565-019-0400-7 | full text | Main text and Methods (single-shot readout fidelity analysis): Pauli spin blockade readout; in the histogram model, triplets that relax during the integration window spread to signals between the two peaks, weighted by integration time over T1, so T1 enters only the triplet distribution; the singlet peak is fixed from singlet-initialised shots and the triplet initialisation fraction is measured separately; singlet and triplet fidelities are defined separately from the threshold, which is chosen at each integration time to maximise their average. Main text with Fig. 2 and Methods: SNR defined and shown against integration time; the shortest usable integration time is set by the noise of the detection chain. Fig. 4b: the optimal integration time is limited by T1, measured by waiting at the readout point before integrating |
| 5 | P. Stano and D. Loss, Review of performance metrics of spin qubits in gated semiconducting nanostructures, Nat. Rev. Phys. 4, 672–688 (2022); read as preprint arXiv:2107.06485 | doi:10.1038/s42254-022-00484-w | full text | Sec. II.1: Ramsey, Hahn echo and multi-pulse dynamical decoupling define different coherence times; the noise spectrum sets the decay envelope, and Gaussian and exponential fits are hard to distinguish. Sec. III.3: measurement time set by sensor sensitivity and the spin-to-charge conversion scheme. Sec. IV.1: readout infidelity as the average of the two error probabilities; RB gives an average over Clifford gates, and quoted infidelities usually refer to elementary gates, a conversion the authors call questionable, with Clifford infidelity typically two to three times larger |
| 6 | F. Vigneau, F. Fedele, A. Chatterjee, D. Reilly, F. Kuemmeth, M. F. Gonzalez-Zalba, E. Laird and N. Ares, Probing quantum devices with radio-frequency reflectometry, Appl. Phys. Rev. 10, 021305 (2023); read as preprint arXiv:2202.10516 | doi:10.1063/5.0088229 | full text | Supplementary Secs. S3.2.2 and S3.2.6: measurement variance falls with integration time, and the SNR scales with acquisition time. Sec. S3.2.4: single-shot readout differs from distinguishing two signal levels because the qubit can decay during the measurement, and the optimal weighting depends on SNR and relaxation time. Sec. S3: nomenclature for spectral densities differs between fields and their definition should be stated; frequency-domain sensitivity often looks better than time-domain, which is more representative for qubit readout. Sec. S4 table: readout fidelities listed with their integration times, and sensitivities at other integration times rescaled to a common basis |
| 7 | G. Burkard, T. D. Ladd, A. Pan, J. M. Nichol and J. R. Petta, Semiconductor spin qubits, Rev. Mod. Phys. 95, 025003 (2023); read as preprint arXiv:2112.08863 | doi:10.1103/RevModPhys.95.025003 | full text | Secs. II.1 and V.1.1: energy-selective readout needs Zeeman energy above thermal energy, and tunnel rates must match the measurement bandwidth, or events are missed or spins relax first. Sec. IV.5: Pauli blockade readout depends on the excited-state gap, which in silicon can be the valley splitting. Sec. III.5: valley splittings vary with interface, well width and field. Sec. VI.1 and VI.1.3: coherence times depend on the sequence through its filter function, and with 1/f noise T2* changes with averaging time. Secs. VI.2 to VI.4: nuclear-spin dephasing and isotopic enrichment; T1 hotspot where Zeeman energy matches valley splitting; charge noise of about 0.1 to 10 µeV per root hertz at 1 Hz, coupled to spin via micromagnet gradients or spin-orbit, probed by multi-pulse noise spectroscopy. Sec. VI.1.6: RF heating can make measured timescales depend on the control sequence |
| 8 | B. Paquelet Wuetz, M. P. Losert, S. Koelling, L. E. A. Stehouwer, A.-M. J. Zwerver, S. G. J. Philips, M. T. Mądzik, X. Xue, G. Zheng, M. Lodari, S. V. Amitonov, N. Samkharadze, A. Sammak, L. M. K. Vandersypen, R. Rahman, S. N. Coppersmith, O. Moutanabbir, M. Friesen and G. Scappucci, Atomic fluctuations lifting the energy degeneracy in Si/SiGe quantum dots, Nat. Commun. 13, 7730 (2022) | doi:10.1038/s41467-022-35458-0 | full text | Introduction: small valley splitting adds leakage channels, complicates initialisation, can affect Pauli blockade readout and coherence, and must be well above the operating temperature. Results and Fig. 1: valley splitting measured by magnetospectroscopy on 22 dots from two wafers, with a wide spread around a mean near 100 µeV and one dot below the detection floor. Results and Discussion: the spread is attributed to random alloy fluctuations at the interface |
| 9 | E. J. Connors, JJ Nelson, H. Qiao, L. F. Edge and J. M. Nichol, Low-frequency charge noise in Si/SiGe quantum dots, Phys. Rev. B 100, 165305 (2019); read as preprint arXiv:1907.07549 | doi:10.1103/PhysRevB.100.165305 | full text | Main text, Eqs. 1 and 2, Table I: current noise on the flank of a Coulomb peak converted to energy using the peak slope and a lever arm from Coulomb diamonds, which differs between dots; values quoted at 1 Hz. Fig. 2: roughly 1/f spectra, some with Lorentzian features from individual fluctuators, with the fit range given. Figs. 3 and 4: noise rises with temperature and varies from dot to dot. Text with Eq. 1 and Supplement: the linear conversion holds only for fluctuations small compared with the peak width. Text with Fig. 2(a): spectra at the peak top and in Coulomb blockade show that potential fluctuations, not instrument noise, dominate |
| 10 | B. Undseth, O. Pietx-Casas, E. Raymenants, M. Mehmandoost, M. T. Mądzik, S. G. J. Philips, S. L. de Snoo, D. J. Michalak, S. V. Amitonov, L. Tryputen, B. Paquelet Wuetz, V. Fezzi, D. Degli Esposti, A. Sammak, G. Scappucci and L. M. K. Vandersypen, Hotter is easier: unexpected temperature dependence of spin qubit frequencies, Phys. Rev. X 13, 041015 (2023); read as preprint arXiv:2304.12984 | doi:10.1103/PhysRevX.13.041015 | full text | Introduction: microwave and baseband control pulses shift spin-qubit frequencies, typically by about 1 MHz, an effect reported across semiconductor qubit platforms and large compared with the detuning tolerated by high-fidelity gates; it is handled by intermediate-frequency calibration, off-resonant prepulses, waits and qubit-specific calibration. The shifts depend on the recent operation history and open a crosstalk channel that affects idle qubits |
