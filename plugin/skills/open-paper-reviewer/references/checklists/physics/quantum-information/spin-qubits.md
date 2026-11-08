---
id: T-SPIN-QUBITS
name: Semiconductor spin qubits
type: technique
field: physics/quantum-information
applies_when: the paper reports quantum-dot or donor spin qubits in silicon, germanium or III-V semiconductors, or bases a claim on spin readout fidelity, valley splitting, coherence times (T1, T2*, T2), charge noise, or single- or two-qubit gate fidelities measured in such devices
version: "0.1"
---

# Semiconductor spin qubits

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

| # | Reference | Identifier |
|---|---|---|
| 1 | F. A. Zwanenburg et al., Silicon quantum electronics, Rev. Mod. Phys. 85, 961 (2013); read as preprint arXiv:1206.5202 | doi:10.1103/RevModPhys.85.961 |
| 2 | A. Morello et al., Donor spins in silicon for quantum technologies, Adv. Quantum Technol. 3, 2000005 (2020); read as preprint arXiv:2009.04081 | doi:10.1002/qute.202000005 |
| 3 | A. Morello et al., Single-shot readout of an electron spin in silicon, Nature 467, 687 (2010); read as preprint arXiv:1003.2679 | doi:10.1038/nature09392 |
| 4 | A. West et al., Gate-based single-shot readout of spins in silicon, Nat. Nanotechnol. 14, 437 (2019); read as preprint arXiv:1809.01864 | doi:10.1038/s41565-019-0400-7 |
| 5 | P. Stano and D. Loss, Review of performance metrics of spin qubits in gated semiconducting nanostructures, Nat. Rev. Phys. 4, 672 (2022); read as preprint arXiv:2107.06485 | doi:10.1038/s42254-022-00484-w |
| 6 | F. Vigneau et al., Probing quantum devices with radio-frequency reflectometry, Appl. Phys. Rev. 10, 021305 (2023); read as preprint arXiv:2202.10516 | doi:10.1063/5.0088229 |
| 7 | G. Burkard et al., Semiconductor spin qubits, Rev. Mod. Phys. 95, 025003 (2023); read as preprint arXiv:2112.08863 | doi:10.1103/RevModPhys.95.025003 |
| 8 | B. Paquelet Wuetz et al., Atomic fluctuations lifting the energy degeneracy in Si/SiGe quantum dots, Nat. Commun. 13, 7730 (2022) | doi:10.1038/s41467-022-35458-0 |
| 9 | E. J. Connors, JJ Nelson, H. Qiao, L. F. Edge and J. M. Nichol, Low-frequency charge noise in Si/SiGe quantum dots, Phys. Rev. B 100, 165305 (2019); read as preprint arXiv:1907.07549 | doi:10.1103/PhysRevB.100.165305 |
| 10 | B. Undseth et al., Hotter is easier: unexpected temperature dependence of spin qubit frequencies, Phys. Rev. X 13, 041015 (2023); read as preprint arXiv:2304.12984 | doi:10.1103/PhysRevX.13.041015 |
