---
id: T-RYDBERG-ATOMS
name: Rydberg atoms and atom arrays
type: technique
field: physics/amo
applies_when: the paper excites atoms to Rydberg states, uses Rydberg blockade or interactions, assembles atoms in optical tweezer arrays, reports Rydberg excitation, preparation, detection, entanglement or gate fidelities, or measures electric fields with Rydberg atoms in vapour cells
version: "0.1"
---

# Rydberg atoms and atom arrays

Atoms excited to Rydberg states (states of high principal quantum number n) interact strongly and respond strongly to electric fields. They are used to claim Rydberg blockade, entanglement and quantum gates between atoms held in optical tweezer arrays, many-body dynamics of spin models in such arrays, and calibrated or highly sensitive measurements of radio-frequency (RF) and microwave fields, usually through electromagnetically induced transparency (EIT) and Autler-Townes (AT) splitting in vapour cells.

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

## 6. Many-body dynamics and the spin model

**Question.** When a many-body phase or dynamics is claimed, does the paper state the spin model the system is mapped onto, with the Rabi frequency, detuning and blockade radius relative to the spacing, and compare the data with simulations that include the measured imperfections?

**Why it matters.** The mapping onto a two-level spin model is an approximation of the multilevel Rydberg structure, and detection errors, dephasing, Rydberg decay and position disorder all change what is measured. A comparison with an ideal model can attribute these effects to many-body physics. Exact simulation is possible only for small arrays, so larger arrays are compared with approximate theory whose validity has to be argued.

**Resolved by.** The model and its parameters stated, with how each was calibrated; simulations with measured detection errors, dephasing and decay included and compared with the data for sizes where exact calculation is possible; the approximation used for larger arrays named and checked against exact results at small size; the size of the array and the duration of the dynamics compared with the Rydberg lifetime.

**Benchmark.** [2], [6]

## 7. Electric field amplitude from Autler-Townes splitting

**Question.** When a field amplitude is obtained from EIT and AT splitting, does the paper give the transition and dipole moment used, the correction for the Doppler mismatch between probe and coupling wavelengths, the range of fields over which the splitting is resolved and linear, and an estimate of how the vapour cell perturbs the field?

**Why it matters.** The splitting gives the field through Planck's constant and a calculated dipole moment, which is what makes the method self-calibrating, but only while the splitting is larger than the EIT linewidth; at weaker fields the relation departs from linearity and amplitude methods need other calibrated quantities. In thermal vapour the splitting observed while scanning the probe is scaled by the ratio of the laser wavelengths, and the dielectric cell can alter the field inside it unless it is small compared with the wavelength.

**Resolved by.** The Rydberg transition, polarisations, dipole moment and its source stated; the wavelength scaling given; data showing linear splitting over the range used and the EIT linewidth for comparison; cell dimensions compared with the wavelength, with modelling or measurements of the cell's effect; agreement with an independently calculated or calibrated field, with its uncertainty.

**Benchmark.** [5], [12], [13], [14], [15]

## 8. Sensitivity and its limits

**Question.** Does the paper define its sensitivity and minimum detectable field, with units, integration time, detection bandwidth and how the noise floor was measured, and does it compare the result with the photon shot-noise and atomic projection-noise limits?

**Why it matters.** A sensitivity per root hertz and a minimum detectable field after a given integration time are different figures and are not interchangeable. Heterodyne schemes with a local-oscillator field improve sensitivity, but add a reference field to the measurement and have a limited instantaneous bandwidth and dynamic range. Laser linewidth and other technical noise usually set the measured sensitivity above the photon shot-noise limit, which itself lies well above the atomic projection-noise limit, so a claim of quantum-limited or record performance needs the comparison.

**Resolved by.** Sensitivity in field per root hertz with the method of measurement and the minimum detectable field with its integration time; the noise spectrum shown; bandwidth and linear dynamic range stated; where a local oscillator is used, its field strength and the conversion from signal to field reported; the shot-noise and projection-noise limits for the apparatus estimated and compared with the result.

**Benchmark.** [12], [15], [16]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Saffman, T. G. Walker and K. Mølmer, Quantum information with Rydberg atoms, Rev. Mod. Phys. 82, 2313–2363 (2010); read as preprint arXiv:0909.4777 | doi:10.1103/RevModPhys.82.2313 | full text | Sec. II.1: lifetimes scale roughly as n cubed and blackbody transitions shorten them at room temperature; quadratic Stark shift grows as n to the seventh, so field stability of about 10 mV/cm at n = 100 keeps shifts below 1 MHz. Secs. I.2 and III.1: double-excitation probability falls as the square of the Rabi frequency over the blockade shift, with weakly interacting pair states dominating; collective Rabi frequency enhanced by the square root of N. Secs. II.2 and II.3: Förster zeros and angular dependence weaken blockade. Sec. III.2: technical gate errors include Doppler broadening, intermediate-state scattering and position variation |
| 2 | A. Browaeys and T. Lahaye, Many-body physics with individually controlled Rydberg atoms, Nat. Phys. 16, 132–142 (2020); read as preprint arXiv:2002.07413 | doi:10.1038/s41567-019-0733-z | full text | Box 1: blockade radius defined from C6 and the Rabi frequency. Box 2 in Sec. IV: distance and angular dependence of interactions measured; online calculators such as ARC available for interaction strengths. Sec. III: stochastic loading with occupation near one half, defect-free probability falling with N, assembly by rearrangement. Sec. V: a 20-atom chain compared with a simulation that includes experimental imperfections, a larger array with approximate theory because exact calculation is out of reach. Sec. VII: mapping multilevel Rydberg structure onto two-level systems |
| 3 | A. Gaëtan, Y. Miroshnychenko, T. Wilk, A. Chotia, M. Viteau, D. Comparat, P. Pillet, A. Browaeys and P. Grangier, Observation of collective excitation of two individual atoms in the Rydberg blockade regime, Nat. Phys. 5, 115–118 (2009); read as preprint arXiv:0810.2960 | doi:10.1038/nphys1183 | full text | Fig. 3: double-excitation probability equals the product of single-atom probabilities at large separation and is suppressed at short separation. Fig. 4: collective Rabi frequency ratio near the square root of two. Text: residual double excitation attributed to stray fields, polarisation imperfections and axis misalignment |
| 4 | L. Béguin, A. Vernier, R. Chicireanu, T. Lahaye and A. Browaeys, Direct measurement of the van der Waals interaction between two Rydberg atoms, Phys. Rev. Lett. 110, 263201 (2013); read as preprint arXiv:1302.4262 | doi:10.1103/PhysRevLett.110.263201 | full text | Fig. 3 and Table 1: interaction measured against distance follows the inverse sixth power, C6 compared with calculation; distance calibrated to within 5%; stray field reduced with electrodes because transverse fields mix states and degrade blockade; departure from the inverse sixth power at short distance from neighbouring pair states |
| 5 | N. Šibalić, J. D. Pritchard, C. S. Adams and K. J. Weatherill, ARC: An open-source library for calculating properties of alkali Rydberg atoms, Comput. Phys. Commun. 220, 319–331 (2017); read as arXiv:1612.05529 | doi:10.1016/j.cpc.2017.06.015 | abstract | Abstract: library computes dipole matrix elements, radiative and blackbody-limited lifetimes, Stark maps and pair interaction potentials, checked against measured energy levels, for gates, many-body simulation and microwave electrometry |
| 6 | S. de Léséleuc, D. Barredo, V. Lienhard, A. Browaeys and T. Lahaye, Analysis of imperfections in the coherent optical excitation of single atoms to Rydberg states, Phys. Rev. A 97, 053803 (2018); read as preprint arXiv:1802.10424 | doi:10.1103/PhysRevA.97.053803 | full text | Sec. II: Rydberg atoms detected as loss; false positives from background collisions, imaging loss and escape while traps are off; false negatives from Rydberg decay and recapture; optical pumping error bounded separately; these reduce contrast without damping. Sec. III: laser phase noise, Doppler dephasing, intermediate-state scattering, Rydberg lifetime, intensity noise and stray fields each estimated. Sec. IV: a model with independently measured inputs reproduces damping from several few-per-cent effects whose weight varies with Rabi frequency |
| 7 | M. Morgado and S. Whitlock, Quantum simulation and computing with Rydberg-interacting qubits, AVS Quantum Sci. 3, 023501 (2021); read as preprint arXiv:2011.03031 | doi:10.1116/5.0036562 | full text | Sec. II.1: readout by fluorescence with Rydberg atoms removed or transferred, detection efficiencies quoted. Secs. II.2 and II.3: coherence limited by laser phase noise, thermal motion, intermediate-state scattering and Rydberg decay including blackbody-induced transitions; Sec. II.4 names Doppler dephasing for two-qubit gates. Sec. II.4 with Figs. 9 and 10: one gate fidelity quoted uncorrected and another corrected for preparation and measurement errors; shaped pulses suppress leakage to other Rydberg states; repeated pulses increase loss and dephasing |
| 8 | M. Saffman, Quantum computing with atomic qubits and Rydberg interactions: progress and challenges, J. Phys. B 49, 202001 (2016); read as preprint arXiv:1605.05207 | doi:10.1088/0953-4075/49/20/202001 | full text | Sec. 5.2 and Table 1: Bell fidelities from parity oscillations listed both raw and post-selected, corrected for atom loss; Sec. 5.5 states these include SPAM errors. Sec. 4: readout with blow-away light before fluorescence detection removes atoms. Sec. 5.3: intrinsic gate errors from Rydberg decay, finite blockade and leakage. Sec. 5.5: Doppler dephasing, laser noise and pointing, and background electric fields from nearby surfaces. Sec. 2.2: trap lifetime limited by background-gas collisions |
| 9 | M. Endres, H. Bernien, A. Keesling, H. Levine, E. R. Anschuetz, A. Krajenbrink, C. Senko, V. Vuletić, M. Greiner and M. D. Lukin, Atom-by-atom assembly of defect-free one-dimensional cold atom arrays, Science 354, 1024–1027 (2016); read as preprint arXiv:1607.03044, which carries a different title | doi:10.1126/science.aah3752 | full text | Fig. 3: loading probability near 0.6, occupation after rearrangement near 0.99, defect-free probability falling with array length. Text on Fig. 3B and Supplementary Sec. III.6: vacuum-limited lifetime sets the dominant loss, so array success falls exponentially with N times rearrangement time. Supplementary Sec. II.2 and Fig. S1: bimodal count histograms with a threshold |
| 10 | D. Barredo, S. de Léséleuc, V. Lienhard, T. Lahaye and A. Browaeys, An atom-by-atom assembler of defect-free arbitrary two-dimensional atomic arrays, Science 354, 1021–1023 (2016); read as preprint arXiv:1607.03042 | doi:10.1126/science.aah3778 | full text | Fig. 3: filling fraction after assembly above 96% while defect-free arrays occur in about 40% of runs, compared with random loading. Supplement S.3: a defect-free array of N atoms lives about the vacuum lifetime divided by N, limiting size. Supplement S.2: single transfer success probability measured |
| 11 | J. P. Covey, I. S. Madjarov, A. Cooper and M. Endres, 2000-times repeated imaging of strontium atoms in clock-magic tweezer arrays, Phys. Rev. Lett. 122, 173201 (2019) | doi:10.1103/PhysRevLett.122.173201 | abstract | Abstract: imaging fidelity and survival probability reported as separate figures, and state-resolved detection with its own survival and fidelity |
| 12 | J. A. Sedlacek, A. Schwettmann, H. Kübler, R. Löw, T. Pfau and J. P. Shaffer, Microwave electrometry with Rydberg atoms in a vapour cell using bright atomic resonances, Nat. Phys. 8, 819–824 (2012); read as preprint arXiv:1205.4461, which carries a different title | doi:10.1038/nphys2423 | full text | Sec. II: field from the AT splitting and a calculated dipole moment, with the splitting scaled by the probe-to-coupling wavelength ratio in thermal vapour; agreement with a field calculated from horn antenna parameters within about 10%; sensitivity per root hertz and minimum detected field quoted as separate figures. Abstract and Sec. I: sensitivity limited mainly by laser linewidth, with transit-time broadening and shot noise also listed |
| 13 | C. L. Holloway, M. T. Simons, J. A. Gordon, A. Dienstfrey, D. A. Anderson and G. Raithel, Electric field metrology for SI traceability: Systematic measurement uncertainties in electromagnetically induced transparency in atomic vapor, J. Appl. Phys. 121, 233106 (2017) | doi:10.1063/1.4984201 | abstract | Abstract: AT splitting is linear in the RF field only while the EIT linewidth is smaller than the splitting, with systematic departures from linearity outside that range; hot-atom and cold-atom behaviour differ in a Doppler-mismatched scheme |
| 14 | H. Fan, S. Kumar, J. Sheng, J. P. Shaffer, C. L. Holloway and J. A. Gordon, Effect of vapor-cell geometry on Rydberg-atom-based measurements of radio-frequency electric fields, Phys. Rev. Applied 4, 044015 (2015) | doi:10.1103/PhysRevApplied.4.044015 | abstract | Abstract: cell geometry affects measurement accuracy, and the effect of the cell on the measured field is smallest when the cell is small compared with the RF wavelength |
| 15 | C. S. Adams, J. D. Pritchard and J. P. Shaffer, Rydberg atom quantum technologies, J. Phys. B 53, 012002 (2020); read as preprint arXiv:1907.09231 | doi:10.1088/1361-6455/ab52ef | full text | Sec. 4: AT splitting gives the field from the transition dipole moment and Planck's constant; for small fields measured from amplitude changes, the coupling Rabi frequency must be known; sensitivity set by probe shot noise, dephasing and residual Doppler shifts, with photon shot noise preventing the projection-noise limit from being reached; cell material and geometry limit accuracy |
| 16 | J. Yuan, W. Yang, M. Jing, H. Zhang, Y. Jiao, W. Li, L. Zhang, L. Xiao and S. Jia, Quantum sensing of microwave electric fields based on Rydberg atoms, Rep. Prog. Phys. 86, 106001 (2023); read as preprint arXiv:2401.01655 | doi:10.1088/1361-6633/acf22f | full text | Sec. 3: sensitivity per root hertz and minimum detectable field defined separately, limited mainly by technical noise; small cells suppress Fabry-Perot effects. Sec. 4: superheterodyne detection with a local-oscillator field, its instantaneous bandwidth and dynamic range; a measured sensitivity and a projection-noise-limited sensitivity given as separate figures, the latter nearly two orders of magnitude lower |
