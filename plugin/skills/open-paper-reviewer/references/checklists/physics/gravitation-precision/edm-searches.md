---
id: T-EDM-SEARCHES
name: Electric dipole moment searches
type: technique
field: physics/gravitation-precision
applies_when: the paper reports a measurement of, or an upper limit on, a permanent electric dipole moment of the neutron, an atom, a molecule, the electron or another particle, or derives constraints on time-reversal or CP violation, or on new physics, from such a measurement
version: "0.1"
---

# Electric dipole moment searches

## 1. Motional fields and geometric-phase shifts

**Question.** Does the paper estimate, for every species in the measurement volume, the false EDM produced when the motional magnetic field (velocity crossed with the electric field) acts together with magnetic-field non-uniformity or field misalignment, including the geometric-phase effect, and is the estimate tied to measured field gradients or field maps?

**Why it matters.** A particle moving through the electric field sees a motional magnetic field which, combined with field gradients or a misalignment of the electric and magnetic fields, gives a frequency shift linear in the electric field that looks like an EDM. Its size depends on particle velocity, trap size and the gradient, so it can be much larger for fast comagnetometer atoms than for slow neutrons. A correction based on the volume-averaged gradient does not capture localised magnetic sources such as magnetised components or surface contamination, and a source at the edge of the cell is particularly effective at producing the shift.

**Resolved by.** Field maps or gradient measurements with the regime of the model used (adiabatic or not) stated; the dependence of the EDM channel on deliberately applied gradients, or on velocity, shown and used for the correction; a search for or bound on magnetic impurities near the cell; the residual uncertainty from this effect listed in the systematic budget for each species.

**Benchmark.** [1], [2], [3], [4]

## 2. Leakage currents and high-voltage effects

**Question.** Were leakage currents across the cell and electrodes monitored throughout data taking, and does the paper turn the measured currents into a bound on magnetic fields correlated with the electric field, with the current paths it assumed? Does it treat discharges and voltage-induced movement of the cells?

**Why it matters.** A current that flows when the high voltage is applied makes a magnetic field that reverses with the electric field, so it does not average away over many reversals. A nanoampere circulating around a cell tens of centimetres across gives a field of femtotesla order, comparable to the field equivalent of a neutron EDM of 10^-26 e cm, and a comagnetometer compensates it only partly when it samples a slightly different region. Discharges can magnetise parts of the apparatus, and small voltage-induced movements of a cell in a field gradient can also mimic a signal.

**Resolved by.** Leakage current recorded alongside the EDM data, with a worst-case path used to bound the resulting frequency shift; that bound entered in the systematic budget; a stated rule for data taken during or after discharges; checks with cells or regions at zero electric field that see the same magnetic environment.

**Benchmark.** [1], [4]

## 3. Field reversals and the EDM channel

**Question.** Which quantities are reversed or switched (electric field polarity, magnetic field direction, molecular orientation or internal state, laser polarisation), how often, how exactly does each reversal reproduce the field it reverses, and how is the EDM signal separated from the other combinations of switches?

**Why it matters.** Frequent electric-field reversals average down random magnetic drifts but not components correlated with the field. In the most sensitive molecular experiments the leading false signals are often the product of two small imperfections, such as an imperfect electric-field reversal combined with a misalignment, a light shift or a polarisation gradient, and each can look harmless on its own.

**Resolved by.** A table of the switches and how the EDM channel is formed from them; the non-reversing part of each field measured; other switch combinations shown to be consistent with zero or explained; deliberately exaggerated imperfections used to measure each sensitivity, multiplied by the residual imperfection in normal running to give the systematic shift; results consistent across different electric field magnitudes.

**Benchmark.** [1], [4]

## 4. Comagnetometry and magnetic monitoring

**Question.** How is the magnetic field seen by the EDM species tracked, does the comagnetometer or magnetometer sample the same field in the same volume, and does the paper evaluate the comagnetometer's own shifts and its assumed insensitivity to an EDM?

**Why it matters.** A comagnetometer removes magnetic drifts only to the extent that it sees the same field: a difference of millimetres between the centres of mass of two species in a vertical gradient shifts their frequency ratio, and the comagnetometer atoms can carry their own geometric-phase and light shifts. In molecules, internal states with opposite effective field act as a comagnetometer only if they respond identically to magnetic fields. A reference species is assumed to have negligible EDM sensitivity, and that assumption needs support.

**Resolved by.** The offset between species measured or modelled, with the EDM result shown as a function of gradient so that the gradient-dependent part can be separated; light shifts and other comagnetometer shifts measured; external magnetometer readings shown to agree with the comagnetometer; the limit on the reference species' own EDM cited; for internal comagnetometer states, their difference in magnetic moment measured or bounded.

**Benchmark.** [1], [3], [4]

## 5. Blinding of the EDM channel

**Question.** Was the EDM channel itself hidden, for example by an unknown offset added to the electric-field-odd frequency difference, while the other switch combinations, comagnetometer signals and systematic studies stayed visible, and were the systematic corrections and their uncertainties fixed before the offset was removed?

**Why it matters.** An EDM result is a small difference left after many systematic corrections chosen by the analysts, and the search for further systematic effects can stop once the result looks as expected. A hidden offset suits a single precise parameter like an EDM because the systematic work can proceed without it, but it does not remove instrumental false signals, which still need corrections or systematic uncertainties.

**Resolved by.** A statement of which quantity was offset, how the offset and its sign were generated and who held them; the systematic budget completed before unblinding; independent analyses, if any, run with separate offsets and compared before unblinding; any correction or selection applied after unblinding listed separately with the shift it caused.

**Benchmark.** [1], [5]

## 6. From frequency shift to EDM

**Question.** How does the paper convert the measured frequency or energy shift into an EDM: what electric field acts on the particles and how was it measured, what degree of polarisation do atoms or molecules reach, and what calculated effective field or sensitivity coefficient is used, with what theoretical uncertainty?

**Why it matters.** The EDM is the shift divided by the field acting on the particles where they precess, so an error in that field passes straight into the result. For polar molecules the effective internal field grows with the degree of polarisation, which depends on the applied field. Calculated sensitivities are accurate to roughly 5 to 10 per cent for paramagnetic atoms and molecules and roughly 20 per cent for the Schiff-moment sensitivity of diamagnetic atoms; different calculations do not always agree.

**Resolved by.** The applied field, or the field in the precession region, given with its measurement; the polarisation measured or shown to be saturated; the effective field or sensitivity coefficient cited with its spread across calculations; the conversion uncertainty either included or shown to be negligible for the limit quoted.

**Benchmark.** [1], [4]

## 7. From a limit to constraints on new physics

**Question.** When the result is turned into bounds on underlying parameters (the electron EDM, CP-odd electron-nucleon couplings, nuclear Schiff moments, pion-nucleon couplings, the QCD theta parameter or a new-physics mass scale), does the paper say whether one source is assumed at a time, include the hadronic and nuclear theory uncertainties, and state the assumptions behind any mass scale?

**Why it matters.** An atom or molecule measures a combination of several CP-violating parameters, so a limit obtained by assuming only one is non-zero can be an order of magnitude tighter than one allowing all of them. Nuclear and hadronic matrix elements are uncertain enough to weaken some bounds substantially, and mass-scale reach depends on the assumed coupling, CP-violating phase and loop order.

**Resolved by.** Single-source bounds labelled as such, with a combined analysis across systems where available; the range of theoretical coefficients propagated into each bound; the confidence level stated; the coupling, phase and loop order behind any quoted mass scale stated, with the range they imply.

**Benchmark.** [1], [4], [6]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | T. Chupp et al., Electric dipole moments of atoms, molecules, nuclei, and particles, Rev. Mod. Phys. 91, 015001 (2019); read as arXiv:1710.02504 | doi:10.1103/RevModPhys.91.015001 |
| 2 | J. M. Pendlebury et al., Geometric-phase-induced false electric dipole moment signals for particles in traps, Phys. Rev. A 70, 032102 (2004) | doi:10.1103/PhysRevA.70.032102 |
| 3 | G. Pignol and S. Roccia, Electric-dipole-moment searches: Reexamination of frequency shifts for particles in traps, Phys. Rev. A 85, 042105 (2012); read as arXiv:1201.0699 | doi:10.1103/PhysRevA.85.042105 |
| 4 | M. S. Safronova et al., Search for new physics with atoms and molecules, Rev. Mod. Phys. 90, 025008 (2018); read as arXiv:1710.01833 | doi:10.1103/RevModPhys.90.025008 |
| 5 | J. R. Klein and A. Roodman, Blind analysis in nuclear and particle physics, Annu. Rev. Nucl. Part. Sci. 55, 141 (2005); read as preprint SLAC-PUB-12051 | doi:10.1146/annurev.nucl.55.090704.151521 |
| 6 | T. Chupp and M. Ramsey-Musolf, Electric dipole moments: A global analysis, Phys. Rev. C 91, 035502 (2015); read as arXiv:1407.1064 | doi:10.1103/PhysRevC.91.035502 |
