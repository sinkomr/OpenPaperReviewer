---
id: T-TRAPPED-IONS
name: Trapped ions
type: technique
field: physics/amo
applies_when: the paper confines ions in a radio-frequency (Paul) or Penning trap and reports motional temperature, heating rates, micromotion, sideband cooling, state preparation or detection fidelity, coherence times, quantum gate fidelities, or transition frequencies measured on trapped ions
version: "0.1"
---

# Trapped ions

## 1. Excess micromotion

**Question.** For an rf trap, does the paper say how excess micromotion was detected and minimised, along which directions it was probed, and what residual amplitude remains under the conditions of the main measurements?

**Why it matters.** Stray static fields or an rf phase difference between electrodes push the ion off the rf null, adding driven motion at the trap drive frequency. This motion shifts transition frequencies through time dilation and the Stark effect, can heat the ion and lowers gate fidelity. Each detection method is sensitive only to the motion projected on its probe beam or its trap axis, and some methods miss particular causes, such as an rf phase difference.

**Resolved by.** The method named (rf-photon correlation, resolved micromotion sidebands or parametric excitation) with its sensitivity; probe directions that together cover all three dimensions, or an argument why a direction cannot carry micromotion; the residual modulation index or field converted into the size of its effect on the quantity claimed; compensation monitored during the measurements, or checked again over their duration.

**Benchmark.** [3], [6], [9]

## 2. Motional temperature from sideband spectra

**Question.** How was the mean motional occupation obtained (sideband ratio, sideband Rabi flopping, carrier suppression or Doppler recooling), and does the paper test the assumption of a thermal distribution that the chosen method makes?

**Why it matters.** The ratio of red to blue sideband excitation gives the mean occupation only for a thermal distribution in the Lamb-Dicke regime. Sideband cooling can leave population trapped in high motional levels, so the ratio reads too low and the heating rate derived from it is understated; coherent excitation from electrode noise and collisions also leave non-thermal states, for which the ratio gives a wrong value. For larger Lamb-Dicke parameters or occupations the simple ratio formula no longer applies and a fuller model of the excitation is needed.

**Resolved by.** The method and its assumptions stated, together with the Lamb-Dicke parameter and the mode measured; for low occupations, sideband Rabi flopping fitted to a population distribution, or a comparison of two methods that make different assumptions; the residual occupation of every mode that enters the claim, not only the one cooled best.

**Benchmark.** [1], [2]

## 3. Heating rates and electric-field noise

**Question.** For a reported heating rate, does the paper give the mode, trap frequency, ion species, ion-electrode distance and electrode temperature, and does it show that technical noise from the electronics does not set the measured rate?

**Why it matters.** Heating rates depend strongly on frequency, distance and temperature, and are comparable between traps only once converted to an electric-field noise spectral density at a stated frequency, with a stated one- or two-sided convention. Noise from voltage supplies and digital-to-analogue converters, Johnson noise in filters and electromagnetic pickup can each exceed surface noise unless heavily filtered at the trap frequency. Different sources give different scaling with frequency, distance and temperature, so a single value does not identify the mechanism.

**Resolved by.** The rate measured by a stated method at several delays, with the conversion to field noise given; scaling with trap frequency and, where possible, distance or temperature reported with uncertainties; a test that changes the filtering or electronics and shows whether the rate changes; for surface-treatment claims, a comparison with an untreated region or before-and-after data in the same apparatus.

**Benchmark.** [1], [6]

## 4. State preparation and detection fidelity

**Question.** How was the readout fidelity determined (prepared states, number of trials, detection time, threshold or likelihood method), and are preparation and detection errors reported for each state separately?

**Why it matters.** Readout separates bright and dark states by photon counts, and the two count distributions overlap because of limited collection efficiency and detector dark counts or background counts. Over the detection window the dark state can decay or be pumped off-resonantly into the bright state, so the error depends on the detection time and on which state was prepared. Preparation and detection errors cannot be separated by repetition, because readout destroys the state; quoting one figure can hide a large error in one of the two states or in the shelving step.

**Resolved by.** Count histograms for both prepared states with the threshold, or the likelihood model, and the detection time; the error given for each prepared state and averaged; the split between preparation and readout supported by an error budget or an independent test; for multi-ion registers, readout error and crosstalk measured with neighbouring ions present.

**Benchmark.** [4], [5], [6]

## 5. How gate fidelity was estimated

**Question.** Which method gives the quoted gate fidelity (randomized benchmarking, process or gate set tomography, or Bell-state fidelity from populations and parity), is the SPAM correction stated and justified, and does the quoted figure match what that method measures?

**Why it matters.** The methods answer different questions and their numbers are not interchangeable. Process tomography is distorted by SPAM errors, while randomized benchmarking separates gate errors from SPAM but captures systematic, coherent errors poorly; coherent errors can add up over repeated gates, so a single-gate fidelity can look better than the gate performs in a circuit. Least-squares fitting of a parity fringe can understate the gate error, and a SPAM-corrected value depends on how and when the SPAM error was measured.

**Resolved by.** The fidelity definition and the method named, with the number of sequences, sequence lengths and shots; uncorrected and SPAM-corrected values both given, with the SPAM figure measured on the same day and register; for two-qubit gates, a second estimate such as repeated gates or benchmarking, and the fitting method for parity fringes; leakage out of the qubit subspace and crosstalk to spectator ions measured or bounded.

**Benchmark.** [5], [6], [7]

## 6. Gate error budget

**Question.** Does the paper give an error budget that accounts for the measured gate error, with each term estimated from an independent measurement, including photon scattering, motional heating and dephasing, spin dephasing, laser intensity and phase noise, and off-resonant excitation?

**Why it matters.** For laser-driven gates, spontaneous Raman and Rayleigh scattering from the gate beams sets a limit that depends on the detuning from the excited states; Raman scattering decoheres the qubit, Rayleigh scattering mainly kicks the ion, and for some ions decay into low-lying levels sets a floor that more laser power cannot remove. Motional heating during the gate, drift of mode frequencies and field noise add further errors. A measured error well above the budget points to a source that has not been identified, and a fidelity at one gate time does not show the trade-off with speed.

**Resolved by.** A table of error terms with the input measurements behind each, compared with the measured error; the gate time, detuning and beam power stated; the error shown as a function of gate time or detuning where speed is part of the claim; a statement of which terms are fundamental and which are technical.

**Benchmark.** [6], [7], [8]

## 7. Coherence time

**Question.** Is the quoted coherence time from free Ramsey precession or from a sequence with spin echo or dynamical decoupling, what is the qubit's sensitivity to magnetic field, and does the paper say what limits the coherence and how the field was stabilised?

**Why it matters.** Ramsey contrast decay (often called T2*) includes slow field and local-oscillator drifts that spin echo and dynamical decoupling remove, so the two give different numbers and only one is relevant to a given use. Qubits with a first-order Zeeman shift need shielding or decoupling to reach coherence times of a fraction of a second to seconds, while field-insensitive clock transitions reach seconds to minutes; residual second-order shifts, rf-induced shifts and oscillator phase noise then dominate. Readout error can also grow with delay when the ion heats, mimicking loss of contrast.

**Resolved by.** The sequence stated, with the fit model and the range of delays; the field, its stability and any feedback used to stay at a field-insensitive point; the limiting mechanism identified or bounded; readout error checked at the longest delay; for decoupled memories, the number and type of pulses.

**Benchmark.** [5], [6], [7]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Brownnutt et al., Ion-trap measurements of electric-field noise near surfaces, Rev. Mod. Phys. 87, 1419 (2015); read as preprint arXiv:1409.6572 | doi:10.1103/RevModPhys.87.1419 |
| 2 | A. J. Rasmusson et al., Optimized pulsed sideband cooling and enhanced thermometry of trapped ions, Phys. Rev. A 104, 043108 (2021); read as preprint arXiv:2107.11802 | doi:10.1103/PhysRevA.104.043108 |
| 3 | J. Keller et al., Precise determination of micromotion for trapped-ion optical clocks, J. Appl. Phys. 118, 104501 (2015); read as preprint arXiv:1505.05907 | doi:10.1063/1.4930037 |
| 4 | A. H. Myerson et al., High-fidelity readout of trapped-ion qubits, Phys. Rev. Lett. 100, 200502 (2008); read as preprint arXiv:0802.1684 | doi:10.1103/PhysRevLett.100.200502 |
| 5 | T. P. Harty et al., High-fidelity preparation, gates, memory, and readout of a trapped-ion quantum bit, Phys. Rev. Lett. 113, 220501 (2014); read as preprint arXiv:1403.1524 | doi:10.1103/PhysRevLett.113.220501 |
| 6 | C. D. Bruzewicz et al., Trapped-ion quantum computing: Progress and challenges, Appl. Phys. Rev. 6, 021314 (2019); read as preprint arXiv:1904.04178 | doi:10.1063/1.5088164 |
| 7 | C. J. Ballance et al., High-fidelity quantum logic gates using trapped-ion hyperfine qubits, Phys. Rev. Lett. 117, 060504 (2016); read as preprint arXiv:1512.04600 | doi:10.1103/PhysRevLett.117.060504 |
| 8 | R. Ozeri et al., Errors in trapped-ion quantum gates due to spontaneous photon scattering, Phys. Rev. A 75, 042329 (2007); read as preprint arXiv:quant-ph/0611048 | doi:10.1103/PhysRevA.75.042329 |
| 9 | A. D. Ludlow et al., Optical atomic clocks, Rev. Mod. Phys. 87, 637 (2015); read as preprint arXiv:1407.3493 | doi:10.1103/RevModPhys.87.637 |
