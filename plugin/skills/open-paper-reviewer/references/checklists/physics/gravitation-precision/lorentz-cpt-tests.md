---
id: T-LORENTZ-CPT-TESTS
name: Tests of Lorentz and CPT invariance
type: technique
field: physics/gravitation-precision
applies_when: the paper uses clock comparisons, optical or microwave resonators, comagnetometers, trapped particles or particle-antiparticle comparisons to bound or report violation of Lorentz or CPT symmetry, Standard-Model Extension coefficients, light-speed anisotropy or sidereal modulation
version: "0.1"
---

# Tests of Lorentz and CPT invariance

## 1. Framework, coefficients and reporting frame

**Question.** Does the paper state the framework it tests (for the SME, the sector and the mass dimension of the operators), name the coefficients it constrains, and transform its result from the laboratory into the standard Sun-centred celestial-equatorial frame, giving the conventions it used (time origin, axes, laboratory latitude and orientation)?

**Why it matters.** A laboratory on the Earth is not an inertial frame, so coefficients that are constant in an inertial frame vary in time in the laboratory, and results quoted in a laboratory frame cannot be compared with other experiments. Parameters of kinematic test theories, such as a preferred-frame light-speed anisotropy, say nothing about how the clocks and rods relate to the underlying particles, so the same parameter from two experiments with different clocks and rods need not mean the same thing.

**Resolved by.** The coefficients named in the notation of a standard compilation; the rotation and boost from the laboratory to the Sun-centred frame written out or referenced, with the laboratory latitude and the orientation of the apparatus; where a kinematic test-theory parameter is also quoted, its relation to the SME coefficients stated.

**Benchmark.** [1], [2], [3]

## 2. From the measured quantity to the coefficients

**Question.** Does the paper give the expression that links the measured frequency, frequency difference or spin precession to the coefficients, including any atomic, nuclear or material model it relies on, and does it say which coefficient combinations cancel in the differential measurement or are unobservable, including those that the orientation of its sensitive axis (quantization axis, cavity axis or spin direction) relative to the Earth's rotation axis leaves out of reach?

**Why it matters.** The signal in a clock or spin comparison depends on the species used, and experiments that look alike can bound different, even non-overlapping, combinations of coefficients. Converting a frequency shift into a coefficient needs an atomic or nuclear structure calculation, and simple nuclear models can assign the sensitivity to the wrong particle. Some coefficients can be removed by field or coordinate redefinitions and cannot be measured in a given sector at all. Components that appear only in terms that do not change as the Earth rotates, such as those along the Earth's axis, give no sidereal signal and are left unconstrained by a modulation search, and a sensitive axis parallel to the Earth's axis gives little or no modulated signal.

**Resolved by.** The relation between the observable and the coefficients written out for the species and transitions used; the structure calculation named, with its uncertainty carried into the bound; the terms that cancel in the comparison listed; the angle between the sensitive axis and the Earth's axis stated, with the components bounded and those not bounded listed explicitly, and no bound claimed on components to which the geometry gives no sensitivity; a statement of which particle sectors (electron, proton, neutron, photon) the result constrains.

**Benchmark.** [1], [3], [4], [5], [6]

## 3. Sidereal signal and diurnal systematics

**Question.** Is the search made at the sidereal frequency and its harmonics, with the signal phase referred to the Sun-centred frame, over a data span long enough to separate sidereal from solar-day variations, and are environmental quantities shown not to vary at the sidereal frequency?

**Why it matters.** Temperature, tilt, magnetic field, trap conditions and laboratory activity follow the solar day, which differs from the sidereal day by about four minutes. Over a run of a day or a few days the two frequencies cannot be separated, so a daily systematic can appear as, or cancel, a sidereal signal. A correction applied to the data can itself carry a sidereal component.

**Resolved by.** A data span of several months or longer, or several runs at different times of year; monitored environmental quantities fitted with the same sidereal model and shown to give amplitudes below the bound; independent channels or orientations whose sidereal signals must have a fixed phase relation, checked against each other; consistency between subsets such as different seasons or reversed spin directions.

**Benchmark.** [5], [6], [7]

## 4. Rotation and reversal of the apparatus

**Question.** Where the apparatus is rotated or its sensitive axis reversed, does the paper show the systematic signals at the rotation frequency and its harmonics (tilt of the rotation axis, centrifugal and thermal effects) and their size at the frequency where the signal is sought, and does it use a known signal to calibrate the response?

**Why it matters.** Rotation moves the signal to the rotation frequency or a harmonic of it (twice the rotation frequency for a resonator), away from most systematic signals, but some systematic signals are synchronous with the rotation and reach that frequency too. A small tilt of the rotation platform produces a signal at the analysis frequency that has the same form as some Lorentz-violating terms, which makes those terms hard to measure by this method. In spin comparisons the Earth's rotation produces a large real signal that a reversal must remove.

**Resolved by.** Tilt, rotation rate and balance of the turntable stated and actively controlled; the residual systematic amplitude at the analysis frequency given and compared with the bound; the dependence on rotation rate checked; for comagnetometers, the measured Earth-rotation signal compared with its expected value as a check of scale.

**Benchmark.** [2], [6], [7]

## 5. Boost-suppressed coefficients and annual modulation

**Question.** When the paper constrains coefficients that enter only through the Earth's orbital velocity (parity-odd or time-like components), does it include data over a large part of a year and scale its sensitivity by the boost factor?

**Why it matters.** The Earth's orbital speed is about one ten-thousandth of the speed of light, so coefficients that enter through the boost are suppressed by that factor, and the isotropic coefficient of resonator tests by at least its square. Their signals change with the orbital phase, so a short run gives little or no access to them.

**Resolved by.** The boost-dependent terms included in the signal model with the orbital velocity stated; data spread over the year, or an explicit statement that boost-dependent coefficients were not constrained; bounds on boost-suppressed coefficients quoted with their weaker sensitivity, not as if they were direct.

**Benchmark.** [2], [5], [7]

## 6. Which part of parameter space is covered

**Question.** Does the paper state whether each bound assumes all other coefficients are zero or comes from a simultaneous fit of several coefficients, which coefficients were fixed or taken from other experiments, and does it limit its conclusion to the sectors, coefficients and mass dimensions it actually constrains?

**Why it matters.** Bounds that take one coefficient at a time can be weaker or absent when several coefficients are non-zero and cancel, and tables of such bounds show the reach of a search, not its ability to separate coefficients. A strong bound in one sector or at one mass dimension does not exclude violation in another, and no single method reaches the whole coefficient space.

**Resolved by.** The fitting assumption stated for each bound; coefficients set to zero or taken from other work listed with the reason; correlations between fitted coefficients given; the conclusion worded in terms of the named coefficients, not as a test of Lorentz or CPT invariance in general.

**Benchmark.** [1], [7], [8], [9]

## 7. What a CPT comparison actually tests

**Question.** When a particle-antiparticle comparison is presented as a CPT test, does the paper show that its figure of merit is sensitive to CPT-odd coefficients, and does it keep the time stamps of the data so that orientation-dependent signals can be sought instead of averaged away?

**Why it matters.** Some conventional figures of merit, such as ratios of g-factors or of charge-to-mass ratios, are insensitive at leading order to the CPT-violating terms of the SME, so a null result there need not bound CPT violation. CPT-even Lorentz violation can shift the same frequencies without being a CPT effect. In interacting field theories CPT violation implies Lorentz violation, so the signal can depend on orientation, and averaging over time hides that dependence.

**Resolved by.** The figure of merit derived within a stated framework, with the CPT-odd and CPT-even coefficients it depends on identified; a time-resolved analysis with a sidereal fit, or a statement of which orientation-dependent coefficients the averaged result leaves unconstrained.

**Benchmark.** [8], [10], [11]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | V. A. Kostelecký and N. Russell, Data tables for Lorentz and CPT violation, Rev. Mod. Phys. 83, 11 (2011); read as arXiv:0801.0287 (later revisions) | doi:10.1103/RevModPhys.83.11 |
| 2 | V. A. Kostelecký and M. Mewes, Signals for Lorentz violation in electrodynamics, Phys. Rev. D 66, 056005 (2002); read as preprint arXiv:hep-ph/0205211 | doi:10.1103/PhysRevD.66.056005 |
| 3 | D. Mattingly, Modern tests of Lorentz invariance, Living Rev. Relativ. 8, 5 (2005); read as preprint arXiv:gr-qc/0502097 | doi:10.12942/lrr-2005-5 |
| 4 | V. A. Kostelecký and C. Lane, Constraints on Lorentz violation from clock-comparison experiments, Phys. Rev. D 60, 116010 (1999); read as preprint arXiv:hep-ph/9908504 | doi:10.1103/PhysRevD.60.116010 |
| 5 | T. Pruttivarasin et al., Michelson-Morley analogue for electrons using trapped ions to test Lorentz symmetry, Nature 517, 592 (2015); read as preprint arXiv:1412.2194 | doi:10.1038/nature14091 |
| 6 | J. M. Brown et al., New limit on Lorentz- and CPT-violating neutron spin interactions, Phys. Rev. Lett. 105, 151604 (2010); read as preprint arXiv:1006.5425 | doi:10.1103/PhysRevLett.105.151604 |
| 7 | S. Herrmann et al., Rotating optical cavity experiment testing Lorentz invariance at the 10^-17 level, Phys. Rev. D 80, 105011 (2009); read as preprint arXiv:1002.1284 | doi:10.1103/PhysRevD.80.105011 |
| 8 | J. D. Tasson, What do we know about Lorentz invariance?, Rep. Prog. Phys. 77, 062901 (2014); read as preprint arXiv:1403.7785 | doi:10.1088/0034-4885/77/6/062901 |
| 9 | V. A. Kostelecký and M. Mewes, Electrodynamics with Lorentz-violating operators of arbitrary dimension, Phys. Rev. D 80, 015020 (2009); read as preprint arXiv:0905.0031 | doi:10.1103/PhysRevD.80.015020 |
| 10 | R. Bluhm et al., CPT and Lorentz tests in Penning traps, Phys. Rev. D 57, 3932 (1998); read as preprint arXiv:hep-ph/9809543 | doi:10.1103/PhysRevD.57.3932 |
| 11 | O. W. Greenberg, CPT violation implies violation of Lorentz invariance, Phys. Rev. Lett. 89, 231602 (2002) | doi:10.1103/PhysRevLett.89.231602 |
