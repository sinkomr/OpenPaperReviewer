---
id: T-EXOTIC-SPIN-FORCES
name: Exotic spin-dependent forces
type: technique
field: physics/gravitation-precision
applies_when: the paper searches for or bounds spin-dependent forces from new light bosons, or axion-like dark matter coupling to electron or nuclear spins, using comagnetometers, magnetometers, spin sensors, torsion pendulums or spin-polarised source masses, or converts such a measurement into coupling-constant limits
version: "0.1"
---

# Exotic spin-dependent forces

## 1. Magnetic leakage from the source

**Question.** When the source mass or spin source is moved, rotated or reversed, how large is the ordinary magnetic field it produces at the sensor, how was that field measured, and how does it compare with the claimed sensitivity?

**Why it matters.** An exotic coupling and a real magnetic field both shift spin energies, and a source that is modulated together with a small magnetic field gives a signal at exactly the modulation frequency. Spin-polarised sources made from ferromagnets leak large fields unless their spin and orbital moments are made to cancel or they are shielded, and unpolarised masses can carry ferromagnetic impurities or conductors that produce induced fields.

**Resolved by.** The residual magnetic moment or field of the source measured, for example with a fluxgate magnetometer near the sensor; the sensor's response to a deliberately applied field at the modulation frequency, used to bound the leakage contribution; source materials chosen or screened for low magnetism and conductivity; extra reversals, such as of holding fields or sensor polarisation, that change the sign of the exotic signal but not of the leakage, or the reverse.

**Benchmark.** [1], [2], [3]

## 2. Comagnetometer suppression and calibration

**Question.** For a comagnetometer, how well does it suppress ordinary magnetic fields at the signal frequency and along each axis, and how was its response to a field that couples to only one spin species calibrated?

**Why it matters.** A comagnetometer cancels magnetic fields because both species see the same field, while an exotic coupling is not in general proportional to the magnetic moments. The cancellation is incomplete: in self-compensating devices it works only below the nuclear Larmor frequency and differs between axes, so residual magnetic sensitivity at the signal frequency can remain. Turning an output voltage or frequency into an energy shift needs a calibration with a non-magnetic input.

**Resolved by.** The measured suppression factor for quasi-static and modulated fields in all directions, stated at the signal frequency; a calibration of the response to a non-magnetic coupling, for example by small known rotations of the apparatus, with its accuracy; the species to which the result applies stated.

**Benchmark.** [2], [4], [5]

## 3. Rotation, tilt and gravitational torques

**Question.** Does the paper account for the response of the spins to rotation of the apparatus, including the Earth's rotation, laboratory tilt and changes in orientation, and, for a torsion balance, for gravitational torques on the pendulum from nearby masses, and does it separate these from the claimed signal?

**Why it matters.** Spins in a rotating frame precess as if in an extra field, so nuclear-spin comagnetometers act as gyroscopes and a spin-polarised torsion pendulum feels a torque from the Earth's rotation. A shift that depends on the angle between the holding field and the Earth's axis turns tilts and orientation changes into apparent signals, and signals sought with daily or sidereal modulation are exposed to this directly. In a torsion balance, residual mass moments of the pendulum coupled to gravity gradients, including those of a moved source mass, can give a torque with the same dependence on orientation as a spin coupling.

**Resolved by.** Tilt and orientation monitored, for example with tilt meters, and their coupling to the signal measured with deliberately applied tilts or bounded; the Earth-rotation shift computed and subtracted, or used as a calibration; the sensitive axis reversed or rotated and the residual after reversal reported; for a torsion balance, the pendulum's residual mass moments and the local gravity gradients measured, with gradients compensated or enlarged on purpose to measure the coupling.

**Benchmark.** [1], [4], [5]

## 4. Field gradients and spatial overlap

**Question.** What are the magnetic field gradients across the sensor, and how does the paper show that the spin species, cells or pendulum elements sample the same field and that gradients do not mimic the signal?

**Why it matters.** Comagnetometry cancels the field only to the extent that both species sample the same volume. Overlapping species never sample it identically, because of surface effects and gradients in temperature and polarisation, and separated cells sample different fields, so field gradients and their drifts leave residual shifts. Interactions of the spin ensembles with themselves and effects of the pump and probe lasers can add further drifts.

**Resolved by.** Gradients measured and set with gradient coils; the residual shift expressed per unit gradient and bounded; gradient drift tracked, for example with several cells combined so that gradients cancel; self-interaction and laser-related effects estimated or measured during data taking.

**Benchmark.** [4], [5]

## 5. Response of magnetic shields to the exotic field

**Question.** For a coupling to electron spins, does the paper consider how the soft magnetic shields around the sensor respond to the exotic field and include that response when deriving the limit?

**Why it matters.** Superconducting and conducting shields do not respond to a coupling to intrinsic spin, and the response to a nuclear-spin coupling is negligible. A soft ferromagnetic or ferrimagnetic shield, however, has polarised electrons that react to an electron-spin coupling as to a weak magnetic field, producing an induced field inside the shield. Inside the shield this can nearly cancel the effect on electron spins alone, and it can make a nucleus-only sensor respond to an electron coupling.

**Resolved by.** The shield materials stated; for electron-spin couplings, an estimate of the induced field and its effect on the signal; where a comagnetometer is used, the combined response of both species to the exotic field and the induced field worked out.

**Benchmark.** [6]

## 6. Spin content of sensor and source

**Question.** How many polarised electrons, protons or neutrons do the sensor atoms and the source carry, and which model or measurement gives that number?

**Why it matters.** A limit on a coupling to a nucleus becomes a limit on a coupling to protons or neutrons only through a model of how the nuclear spin is shared between them. Simple valence-nucleon models, semi-empirical models and shell-model calculations can differ by factors of two or more, especially for non-valence nucleons in heavy nuclei. For polarised electron sources, part of the magnetisation is orbital, so the spin density does not follow simply from the field, and conventions for the spin fraction differ between papers.

**Resolved by.** The nuclear spin fractions used, their source, and an uncertainty that reflects the spread between models; species with well-determined spin content preferred for the coupling claimed; the electron spin density of a source measured, for example by calibrating against the Earth's rotation, or derived with orbital contributions included; the convention for the polarisation fraction stated.

**Benchmark.** [1], [3], [7]

## 7. From a measured shift to coupling constants

**Question.** Which interaction potential, coupling convention and range does the paper use to convert its measurement into limits on coupling constants, and does it integrate the potential over the actual geometry and spin distribution of source and sensor?

**Why it matters.** Published forms of the spin-dependent potentials have differed in signs, missing terms and normalisation, and some potentials vanish for identical fermions, so constraints derived with an inconsistent form may need revision. An experiment constrains a product of two couplings, not each one alone, and the bound on that product depends on the boson mass through the Yukawa factor and on the source volume and distance. Comparisons with other experiments hold only when the conventions match.

**Resolved by.** The potential written out with its source and coupling convention; the integral over source and sensor geometry and spin density described; the limit given as a function of boson mass or range, with the coupling product constrained named; any assumptions, such as only one coupling being non-zero, stated; comparisons with other bounds converted to the same convention.

**Benchmark.** [3], [8]

## 8. Signal model for axion-like dark matter

**Question.** For a dark-matter search, what does the paper assume for the field amplitude, local dark-matter density, coherence time and direction of the relative velocity, and does the analysis allow for the stochastic nature of the field when the measurement is shorter than the coherence time?

**Why it matters.** The field of ultralight dark matter is a sum of many modes, so its amplitude within one coherence time is a random draw rather than a fixed value. Assuming the mean amplitude when the measurement lasts less than a coherence time has overstated limits by factors of about three to ten. A spin coupling to the gradient of the field also depends on the direction of the relative velocity, which varies daily, and dark-matter limits weaken if the boson is only part of the dark matter.

**Resolved by.** The dark-matter density, halo model and coherence time stated; for short measurements, an analysis that marginalises over the amplitude distribution, and for gradient couplings over velocity direction and phase; the assumption that the boson makes up all the dark matter stated, or limits given for a smaller fraction.

**Benchmark.** [3], [5], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | B. R. Heckel et al., Preferred-frame and CP-violation tests with polarized electrons, Phys. Rev. D 78, 092006 (2008); read as arXiv:0808.2673 | doi:10.1103/PhysRevD.78.092006 |
| 2 | G. Vasilakis et al., Limits on new long range nuclear spin-dependent forces set with a K-3He comagnetometer, Phys. Rev. Lett. 103, 261801 (2009); read as arXiv:0809.4700 | doi:10.1103/PhysRevLett.103.261801 |
| 3 | L. Cong et al., Spin-dependent exotic interactions, Rev. Mod. Phys. 97, 025005 (2025); read as arXiv:2408.15691 | doi:10.1103/RevModPhys.97.025005 |
| 4 | T. W. Kornack et al., Nuclear spin gyroscope based on an atomic comagnetometer, Phys. Rev. Lett. 95, 230801 (2005) | doi:10.1103/PhysRevLett.95.230801 |
| 5 | W. A. Terrano and M. V. Romalis, Comagnetometer probes of dark matter and new physics, Quantum Sci. Technol. 7, 014001 (2022); read as arXiv:2106.09210 | doi:10.1088/2058-9565/ac1ae0 |
| 6 | D. F. Jackson Kimball et al., Magnetic shielding and exotic spin-dependent interactions, Phys. Rev. D 94, 082005 (2016); read as arXiv:1606.00696 | doi:10.1103/PhysRevD.94.082005 |
| 7 | D. F. Jackson Kimball, Nuclear spin content and constraints on exotic spin-dependent couplings, New J. Phys. 17, 073008 (2015); read as arXiv:1407.2671 | doi:10.1088/1367-2630/17/7/073008 |
| 8 | P. Fadeev et al., Revisiting spin-dependent forces mediated by new bosons: potentials in the coordinate-space representation for macroscopic- and atomic-scale experiments, Phys. Rev. A 99, 022113 (2019); read as arXiv:1810.10364 | doi:10.1103/PhysRevA.99.022113 |
| 9 | G. P. Centers et al., Stochastic fluctuations of bosonic dark matter, Nat. Commun. 12, 7321 (2021); read as arXiv:1905.13650 | doi:10.1038/s41467-021-27632-7 |
