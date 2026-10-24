---
id: T-EDM-SEARCHES
name: Electric dipole moment searches
type: technique
field: physics/gravitation-precision
applies_when: the paper reports a measurement of, or an upper limit on, a permanent electric dipole moment of the neutron, an atom, a molecule, the electron or another particle, or derives constraints on time-reversal or CP violation, or on new physics, from such a measurement
version: "0.1"
---

# Electric dipole moment searches

Searches for a permanent electric dipole moment (EDM) look for a shift in a spin-precession frequency that reverses with an applied electric field, and are used to claim a value of, or an upper limit on, the EDM of the neutron, an atom, a molecule or the electron, and from it bounds on violation of time-reversal (T) and charge-parity (CP) symmetry beyond the Standard Model. The shifts sought are tiny, so each claim rests on showing that no magnetic or other effect correlated with the electric field mimics the signal.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | T. Chupp, P. Fierlinger, M. Ramsey-Musolf and J. Singh, Electric dipole moments of atoms, molecules, nuclei, and particles, Rev. Mod. Phys. 91, 015001 (2019); read as arXiv:1710.02504 | doi:10.1103/RevModPhys.91.015001 | full text | Sec. I.B to I.C: measured EDMs depend on several parameters; sole-source limits versus global analysis; mass reach depends on phase, coupling and loop order, with exceptions. Sec. III.B: random field noise averages with reversals but fields correlated with the electric field, such as from leakage currents, do not; magnetometer light shifts. Sec. IV.A, "Neutron-EDM systematics": leakage current of 1 nA around the cell gives about 3 fT and is only partly compensated by a comagnetometer offset by about 3 mm; geometric-phase false EDM from motional field and gradients, with adiabatic and non-adiabatic regimes, larger for the 199Hg comagnetometer than for neutrons; magnetised components, surface contamination and electrodes magnetised by high-voltage discharges as limits; varying gradients and velocities to study the effect; gradient-dependent analysis using the centre-of-mass offset; expectation that future experiments use blind analysis. Sec. IV.B: motional field, field misalignment and leakage currents in atomic beams; leakage currents measured directly to set the systematic. Sec. IV.C: effective field depends on molecular polarisation; opposite molecular orientations act as an internal comagnetometer; more than 40 parameters varied; dominant systematics combine two small effects such as imperfect electric-field reversal. Sec. IV.E: field-free outer cells used to remove fields correlated with leakage currents. Sec. V.A: sole-source limits at 95% c.l. taken with the smallest coefficient in the theoretical range. Sec. V.B: global analysis across systems, with constraints depending on the range of theoretical uncertainties in the coefficients; significant spread in coefficients from different authors |
| 2 | J. M. Pendlebury, W. Heil, Yu. Sobolev, P. G. Harris, J. D. Richardson, R. J. Baskin, D. D. Doyle, P. Geltenbort, K. Green, M. G. D. van der Grinten, P. S. Iaydjiev, S. N. Ivanov, D. J. R. May and K. F. Smith, Geometric-phase-induced false electric dipole moment signals for particles in traps, Phys. Rev. A 70, 032102 (2004) | doi:10.1103/PhysRevA.70.032102 | abstract | Abstract: geometric-phase Larmor frequency shifts in trapped-particle EDM experiments include a part proportional to the electric field that can be mistaken for an EDM; predictions agree with experiment within 15%; some experiments need stringent precautions; buffer gas suppression examined |
| 3 | G. Pignol and S. Roccia, Electric-dipole-moment searches: Reexamination of frequency shifts for particles in traps, Phys. Rev. A 85, 042105 (2012); read as arXiv:1201.0699 | doi:10.1103/PhysRevA.85.042105 | full text | Abstract and Sec. I: geometric-phase shifts in non-uniform fields are a false-EDM source, relevant to atomic comagnetometers in neutron EDM experiments. Sec. III.A: for large-scale inhomogeneities the false EDM is corrected using the volume-averaged gradient. Sec. III.B: the correction can fail for localised inhomogeneities; a magnetic dipole at the circumference is particularly effective, which sets requirements on control of magnetic impurities |
| 4 | M. S. Safronova, D. Budker, D. DeMille, D. F. Jackson Kimball, A. Derevianko and C. W. Clark, Search for new physics with atoms and molecules, Rev. Mod. Phys. 90, 025008 (2018); read as arXiv:1710.01833 | doi:10.1103/RevModPhys.90.025008 | full text | Sec. V.D.1: electric-field reversal to suppress magnetic noise; fields correlated with the electric field from leakage currents and motional effects mimic the signal; comagnetometers using a lighter species or an opposite-polarisation state. Sec. V.D.2: measurement in both molecular orientations and at several field magnitudes; limits quoted assuming only one of electron EDM or electron-nucleon coupling is non-zero. Sec. V.D.3: low leakage currents; voltage-induced cell movements with gradients as leading systematic. Sec. V.D.4: calculated sensitivities accurate to about 5% (paramagnetic atoms), 10% (molecules) and 20% (diamagnetic Schiff moment); hadronic uncertainties not negligible |
| 5 | J. R. Klein and A. Roodman, Blind analysis in nuclear and particle physics, Annu. Rev. Nucl. Part. Sci. 55, 141–163 (2005); read as preprint SLAC-PUB-12051 | doi:10.1146/annurev.nucl.55.090704.151521 | full text | Sec. 2: stopping bias when analysis continues until the result agrees with expectation; blind analysis does not remove instrumental biases; publications should state which selections were applied after unblinding. Sec. 3.2: hidden-answer methods suit single precise parameters. Sec. 3.2.2: hidden random offset and sign added to the fitted parameter, leaving the other analysis steps unimpeded; separate offsets for independent analyses, switched to a common one for comparison before unblinding |
| 6 | T. Chupp and M. Ramsey-Musolf, Electric dipole moments: A global analysis, Phys. Rev. C 91, 035502 (2015); read as arXiv:1407.1064 | doi:10.1103/PhysRevC.91.035502 | full text | Sec. I: paramagnetic systems are sensitive mainly to the electron EDM and an electron-nucleon coupling, and fitting both gives bounds an order of magnitude weaker than the single-source assumption; nuclear theory uncertainties prevent a significant limit on one pion-nucleon coupling. Sec. IV: mass-scale bounds assume a one-loop coupling and a CP-violating phase, and hadronic uncertainty may weaken them |
