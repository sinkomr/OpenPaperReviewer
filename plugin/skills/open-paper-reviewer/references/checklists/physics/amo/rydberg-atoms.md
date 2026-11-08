---
id: T-RYDBERG-ATOMS
name: Rydberg atoms and atom arrays
type: technique
field: physics/amo
applies_when: the paper excites atoms to Rydberg states, uses Rydberg blockade or interactions, assembles atoms in optical tweezer arrays, reports Rydberg excitation, preparation, detection, entanglement or gate fidelities, or measures electric fields with Rydberg atoms in vapour cells
version: "0.1"
---

# Rydberg atoms and atom arrays

## 1. Interaction strength and blockade

**Question.** Does the paper state the Rydberg state, the interaction coefficient and how it was obtained (calculated or measured), the calibrated interatomic distances, and the ratio of the interaction to the Rabi frequency, and does it show blockade directly rather than assume it?

**Why it matters.** Blockade holds only while the interaction shift is large compared with the Rabi frequency, so the claimed regime depends on the interaction coefficient, the distance and the drive strength. The interaction can depart from its simple long-range form at short distance, depends on angle, and weakens where nearby pair states or stray fields mix the target state, which leaves residual double excitation. A faster collective oscillation is a consequence of blockade, not proof of it on its own.

**Resolved by.** The interaction coefficient calculated with a stated method or measured, and compared where possible; distances calibrated with an uncertainty; the blockade radius compared with the spacing; double excitation measured and compared with the product of single-atom probabilities at large separation; the collective enhancement of the Rabi frequency shown alongside it; residual double excitation reported and its causes discussed.

**Benchmark.** [1], [2], [3], [4], [5]

## 2. Coherence of the ground-Rydberg excitation

**Question.** Does the paper give an error budget for the damping and loss of contrast of ground-Rydberg oscillations, with each term estimated from an independent measurement: laser phase noise, Doppler dephasing from atomic temperature, scattering from the intermediate state, Rydberg decay including blackbody transitions, intensity and pointing fluctuations, and stray electric fields?

**Why it matters.** Several small effects, each of a few per cent, usually add up to the observed damping, and their relative size changes with the Rabi frequency, so a single fit parameter does not identify what limits the system. Rydberg levels are highly polarisable, so stray fields from nearby surfaces shift and broaden the line. Lifetimes depend on the state and on the temperature of the surroundings through blackbody radiation.

**Resolved by.** The laser linewidths or noise spectra, atomic temperature, excitation geometry, intermediate-state detuning, Rydberg lifetime and residual stray field each stated; a model with these measured inputs compared with the data; the dominant term identified; dependence on Rabi frequency shown where speed or fidelity is claimed.

**Benchmark.** [1], [6], [7], [8]

## 3. Detecting Rydberg population as atom loss

**Question.** When Rydberg population is inferred from atoms missing after the sequence, does the paper give the probability that a ground-state atom is lost anyway and the probability that a Rydberg atom decays and is recaptured, and does it say whether the reported populations are corrected for them?

**Why it matters.** Rydberg atoms are usually detected because they are expelled from the trap, so any other loss, such as background-gas collisions, loss during imaging or atoms escaping while the tweezers are off, counts as Rydberg population. Rydberg atoms that decay before they leave are counted as ground-state atoms. The two errors are not equal, depend on the state and the timing, and reduce oscillation contrast without any loss of coherence.

**Resolved by.** Both detection error probabilities measured or estimated, with their causes; the state-preparation error, such as imperfect optical pumping, stated separately; raw populations shown alongside any corrected values, with the correction method; the effect of these errors on correlations or fidelities that the claims rest on.

**Benchmark.** [6], [7], [8]

## 4. Loading, imaging and array assembly

**Question.** Does the paper report the loading probability, the imaging fidelity and the survival probability per image, the filling fraction after rearrangement, and the fraction of runs that give a defect-free array, and does it say whether data were post-selected on fully filled arrays?

**Why it matters.** Tweezers load stochastically, so arrays are assembled by imaging and moving atoms, and the chance of a defect-free array falls quickly with atom number. Imaging fidelity (telling a filled site from an empty one) and survival (keeping the atom through the image) are distinct figures, and one can be high while the other is not. Atoms are lost during rearrangement and the experiment at a rate set by the vacuum lifetime, so a defect-free array decays faster as it grows.

**Resolved by.** Count histograms with the threshold, imaging fidelity and survival stated separately; filling fraction and defect-free probability given for the array sizes used; the vacuum-limited lifetime and the sequence duration stated; any post-selection on initial or final occupancy declared, with the fraction of runs kept.

**Benchmark.** [2], [9], [10], [11]

## 5. Entanglement and gate fidelity

**Question.** For a claimed entangled state or gate, which method gives the fidelity, is the value raw or corrected for state preparation and measurement (SPAM) errors and for atom loss, and are leakage out of the qubit states and loss during the gate reported?

**Why it matters.** Loss of an atom during the sequence is common in tweezer arrays, and a fidelity post-selected on atoms that survive is higher than the raw value and answers a different question. Corrections for SPAM errors can change the quoted value considerably, and rest on preparation and detection errors measured separately. Leakage to other Rydberg levels and loss from repeated excitation are errors that a fidelity computed only within the qubit states can miss.

**Resolved by.** The method named, such as populations with parity oscillations or benchmarking, with the number of repetitions; raw and corrected fidelities both given, with the correction method and the SPAM figures used; loss and leakage measured or bounded and counted as errors; an error budget compared with the measured infidelity.

**Benchmark.** [7], [8]

## 6. Electric field amplitude from Autler-Townes splitting

**Question.** When a field amplitude is obtained from EIT and AT splitting, does the paper give the transition and dipole moment used, the correction for the Doppler mismatch between probe and coupling wavelengths, the range of fields over which the splitting is resolved and linear, and an estimate of how the vapour cell perturbs the field?

**Why it matters.** The splitting gives the field through Planck's constant and a calculated dipole moment, which is what makes the method self-calibrating, but only while the splitting is larger than the EIT linewidth; at weaker fields the relation departs from linearity and amplitude methods need other calibrated quantities. In thermal vapour the splitting observed while scanning the probe is scaled by the ratio of the laser wavelengths, and the dielectric cell can alter the field inside it unless it is small compared with the wavelength.

**Resolved by.** The Rydberg transition, polarisations, dipole moment and its source stated; the wavelength scaling given; data showing linear splitting over the range used and the EIT linewidth for comparison; cell dimensions compared with the wavelength, with modelling or measurements of the cell's effect; agreement with an independently calculated or calibrated field, with its uncertainty.

**Benchmark.** [5], [12], [13], [14], [15]

## 7. Sensitivity and its limits

**Question.** Does the paper define its sensitivity and minimum detectable field, with units, integration time, detection bandwidth and how the noise floor was measured, and does it compare the result with the photon shot-noise and atomic projection-noise limits?

**Why it matters.** A sensitivity per root hertz and a minimum detectable field after a given integration time are different figures and are not interchangeable. Heterodyne schemes with a local-oscillator field improve sensitivity, but add a reference field to the measurement and have a limited instantaneous bandwidth and dynamic range. Laser linewidth and other technical noise usually set the measured sensitivity above the photon shot-noise limit, which itself lies well above the atomic projection-noise limit, so a claim of quantum-limited or record performance needs the comparison.

**Resolved by.** Sensitivity in field per root hertz with the method of measurement and the minimum detectable field with its integration time; the noise spectrum shown; bandwidth and linear dynamic range stated; where a local oscillator is used, its field strength and the conversion from signal to field reported; the shot-noise and projection-noise limits for the apparatus estimated and compared with the result.

**Benchmark.** [12], [15], [16]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Saffman et al., Quantum information with Rydberg atoms, Rev. Mod. Phys. 82, 2313 (2010); read as preprint arXiv:0909.4777 | doi:10.1103/RevModPhys.82.2313 |
| 2 | A. Browaeys and T. Lahaye, Many-body physics with individually controlled Rydberg atoms, Nat. Phys. 16, 132 (2020); read as preprint arXiv:2002.07413 | doi:10.1038/s41567-019-0733-z |
| 3 | A. Gaëtan et al., Observation of collective excitation of two individual atoms in the Rydberg blockade regime, Nat. Phys. 5, 115 (2009); read as preprint arXiv:0810.2960 | doi:10.1038/nphys1183 |
| 4 | L. Béguin et al., Direct measurement of the van der Waals interaction between two Rydberg atoms, Phys. Rev. Lett. 110, 263201 (2013); read as preprint arXiv:1302.4262 | doi:10.1103/PhysRevLett.110.263201 |
| 5 | N. Šibalić et al., ARC: An open-source library for calculating properties of alkali Rydberg atoms, Comput. Phys. Commun. 220, 319 (2017); read as arXiv:1612.05529 | doi:10.1016/j.cpc.2017.06.015 |
| 6 | S. de Léséleuc et al., Analysis of imperfections in the coherent optical excitation of single atoms to Rydberg states, Phys. Rev. A 97, 053803 (2018); read as preprint arXiv:1802.10424 | doi:10.1103/PhysRevA.97.053803 |
| 7 | M. Morgado and S. Whitlock, Quantum simulation and computing with Rydberg-interacting qubits, AVS Quantum Sci. 3, 023501 (2021); read as preprint arXiv:2011.03031 | doi:10.1116/5.0036562 |
| 8 | M. Saffman, Quantum computing with atomic qubits and Rydberg interactions: progress and challenges, J. Phys. B 49, 202001 (2016); read as preprint arXiv:1605.05207 | doi:10.1088/0953-4075/49/20/202001 |
| 9 | M. Endres et al., Atom-by-atom assembly of defect-free one-dimensional cold atom arrays, Science 354, 1024 (2016); read as preprint arXiv:1607.03044, which carries a different title | doi:10.1126/science.aah3752 |
| 10 | D. Barredo et al., An atom-by-atom assembler of defect-free arbitrary two-dimensional atomic arrays, Science 354, 1021 (2016); read as preprint arXiv:1607.03042 | doi:10.1126/science.aah3778 |
| 11 | J. P. Covey et al., 2000-times repeated imaging of strontium atoms in clock-magic tweezer arrays, Phys. Rev. Lett. 122, 173201 (2019) | doi:10.1103/PhysRevLett.122.173201 |
| 12 | J. A. Sedlacek et al., Microwave electrometry with Rydberg atoms in a vapour cell using bright atomic resonances, Nat. Phys. 8, 819 (2012); read as preprint arXiv:1205.4461, which carries a different title | doi:10.1038/nphys2423 |
| 13 | C. L. Holloway et al., Electric field metrology for SI traceability: Systematic measurement uncertainties in electromagnetically induced transparency in atomic vapor, J. Appl. Phys. 121, 233106 (2017) | doi:10.1063/1.4984201 |
| 14 | H. Fan et al., Effect of vapor-cell geometry on Rydberg-atom-based measurements of radio-frequency electric fields, Phys. Rev. Applied 4, 044015 (2015) | doi:10.1103/PhysRevApplied.4.044015 |
| 15 | C. S. Adams et al., Rydberg atom quantum technologies, J. Phys. B 53, 012002 (2020); read as preprint arXiv:1907.09231 | doi:10.1088/1361-6455/ab52ef |
| 16 | J. Yuan et al., Quantum sensing of microwave electric fields based on Rydberg atoms, Rep. Prog. Phys. 86, 106001 (2023); read as preprint arXiv:2401.01655 | doi:10.1088/1361-6633/acf22f |
