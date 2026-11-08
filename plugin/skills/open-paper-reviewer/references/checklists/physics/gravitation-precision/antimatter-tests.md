---
id: T-ANTIMATTER-TESTS
name: Antimatter gravity and spectroscopy
type: technique
field: physics/gravitation-precision
applies_when: the paper reports spectroscopy, charge-to-mass or charge comparisons, or free-fall or deflection measurements with antihydrogen, antiprotons or other antimatter, or bases a claim about CPT symmetry, the weak equivalence principle or antimatter gravity on annihilation counts or trapped antiparticles
version: "0.1"
---

# Antimatter gravity and spectroscopy

## 1. Magnetic field at the atoms

**Question.** How was the magnetic field seen by the trapped atoms or particles measured (method, position, and when relative to the data), how strongly does each measured transition depend on it, and does the paper choose or combine transitions to reduce that dependence?

**Why it matters.** Trapped antihydrogen sits in a field of the order of a tesla, so its transition frequencies carry Zeeman shifts that differ between transitions and must be calculated from the field, so an error in the field passes into the result. A field measured at one place or time, for example by electron cyclotron resonance (ECR) on the trap axis, need not be the field the atoms sample, and its precision and absolute accuracy can differ.

**Resolved by.** The field measurement method, its precision and absolute accuracy stated; the field checked at the start of each run and its drift during the data given; the field dependence of each transition written out, with the shift it causes in the result; field-insensitive transitions or differences of transitions used where possible; for beam experiments, the field dependence measured over a range and extrapolated to zero field.

**Benchmark.** [1], [5], [7]

## 2. Trajectory simulations and the energy distribution of the atoms

**Question.** Where the result depends on simulations of atoms moving through the trap fields (line shapes, escape curves, deflections), does the paper state the field model, the initial energy distribution and the other inputs, show how they were validated against measurements, and vary them to give a modelling uncertainty?

**Why it matters.** Atoms moving through an inhomogeneous trap field give asymmetric, broadened lines and escape patterns that only a simulation can relate to the quantity of interest, so the result can be no better than the model. The energy distribution of the trapped atoms is not measured directly but inferred, and the off-axis field is the least well known part of the field model; the resulting modelling uncertainty can be comparable with the statistical error.

**Resolved by.** The simulation method, the number of simulated atoms and the field model described, with the field model compared with independent field measurements; the energy distribution chosen to match data such as release-time distributions, with alternative distributions tried; perturbations of the field model propagated into a separately quoted modelling uncertainty; the paper says in which way the comparison with matter is model dependent.

**Benchmark.** [1], [2], [3]

## 3. Forces other than gravity

**Question.** In a free-fall or deflection measurement, does the paper estimate every force on the antimatter other than gravity (magnetic gradient forces on the magnetic moment, electric and magnetic forces on any residual charge, stray fields from nearby equipment), compare each with the gravitational force, and calibrate the dominant one in place?

**Why it matters.** Gravity on a single atom or antiproton is extremely weak: for ground-state hydrogen it equals the force from a field gradient of about two millitesla per metre, and on a charged antiproton a stray field of a few gauss, or of tens of volts per centimetre, gives a far larger force. A deflection measured with no means of separating these forces cannot be attributed to gravity.

**Resolved by.** The non-gravitational forces listed with their estimated size in units of the gravitational force; the field imbalance or gradient measured before and after the release and its uncertainty converted to an acceleration; data taken at several deliberate offsets, including large ones that drive all atoms one way, so that the response to the applied force is measured; for charged particles, stray fields measured or a reference with a known zero-force position.

**Benchmark.** [2], [4]

## 4. Annihilation detection efficiency and background

**Question.** What are the detection efficiency and background rate for each observation window and each region of the detector, how were they measured, and how were the selection criteria that separate annihilations from cosmic rays set?

**Why it matters.** With a few events per trial, the background from cosmic rays and from annihilations of stray antiparticles can be comparable with the signal, and a selection tuned to the signal region can raise or lower the apparent rate. When the result depends on where or when atoms annihilate, as in up-down comparisons or position shifts, any difference in efficiency between regions enters the result directly.

**Resolved by.** Efficiency and background given for each window and region, with uncertainties; background measured in runs with an empty trap or with conditions in which no antiatoms can form; selection criteria trained or fixed on separate calibration samples; efficiency differences between regions calibrated with samples known to annihilate in one region, and their uncertainty carried into the result.

**Benchmark.** [1], [2], [3], [6], [9]

## 5. What is annihilating

**Question.** Does the paper show that the counted annihilations come from neutral antiatoms in the stated internal state, not from bare antiprotons or other charged particles held by the trap fields, or from atoms in excited or other hyperfine states?

**Why it matters.** Magnetic traps can also hold charged antiparticles, which annihilate in the same detector. Antihydrogen forms mostly in highly excited states, and only a fraction of the atoms reaching an apparatus may be in the ground state or the selected hyperfine state, so both the signal size and its interpretation depend on the state mixture.

**Resolved by.** Electric clearing or bias fields applied to remove or deflect charged particles, with a test or simulation showing their effect; field-ionisation or other analysis of the state distribution, with the range of states that can reach the detector stated; the fraction of atoms in the measured state estimated and included in the expected signal; control runs in which antiatom formation is suppressed, showing that the signal disappears.

**Benchmark.** [3], [6], [7], [9]

## 6. Few atoms per trial and normalisation between trials

**Question.** How many atoms were trapped or detected per trial and per frequency point or setting, how was variation in that number between trials handled, and do independent detection channels (appearance during the probe, disappearance afterwards) agree?

**Why it matters.** Trapped antihydrogen numbers range from fewer than one to about a hundred atoms per trial, and the trapping rate can drift with the state of the apparatus, so a change in rate between frequency points or settings can look like a change in the signal. The attainable precision is limited by the total count, which sets how finely a line centre or escape curve can be located.

**Resolved by.** The number of atoms per trial and in total stated for each setting; reference points or reference releases repeated within each data set and used to normalise it; settings interleaved over the run so that drift does not follow the setting; appearance and disappearance signals, or other independent channels, reported and compared; the count needed for the quoted precision shown to be consistent with the counts obtained.

**Benchmark.** [1], [2], [7], [9]

## 7. The matter reference

**Question.** Is the matter value against which the antimatter result is compared measured in the same apparatus, under the same conditions and by the same method, or is it taken from another experiment or from a calculation and corrected; and are those corrections and their uncertainties given?

**Why it matters.** A trapped antihydrogen frequency is compared with a hydrogen value calculated for the trap field from measurements under different conditions, so the agreement depends on that calculation. In Penning traps the proton is often replaced by a negative hydrogen ion, whose extra electrons, binding energies and polarisability must be corrected for, and a difference in the energy or temperature of the two particles shifts the measured ratio. Where the comparison is with theory, as for antiprotonic atoms, the result also rests on the calculation and its uncertainty, and on the conditions of the target, such as its density.

**Resolved by.** Where possible, the matter system measured with the same apparatus and analysis; otherwise the reference value, its source and every correction listed with uncertainties; in Penning traps, both particles measured in the same trap and field in rapid alternation, with differences in particle energy, trap voltages and position measured and corrected; the analysis tested by comparing identical particles; for comparisons with theory, the calculation, its stated uncertainty and the dependence of the result on target conditions given.

**Benchmark.** [1], [7], [8], [9]

## 8. What the comparison constrains

**Question.** Does the paper state which quantity its result constrains (free-fall acceleration, a clock or redshift effect, charge, mass or magnetic moment) and the assumptions needed to turn the measurement into that constraint, and does it limit its conclusion accordingly?

**Why it matters.** Free-fall tests and clock comparisons test different parts of the equivalence principle. Limits on antimatter gravity inferred from spectroscopy or charge-to-mass comparisons depend on an assumed gravitational potential, often the absolute potential of distant mass, and on the range of the hypothetical interaction, and these assumptions are debated. Charge limits from trajectory data rest on the simulation and on assumptions about the atom's motion and mass.

**Resolved by.** The tested principle or parameter named; for indirect gravity limits, the assumed potential, its source and the range of interaction to which the limit applies stated; the assumptions behind a derived bound listed; conclusions worded in terms of the parameter constrained, not as a general test of antimatter gravity or CPT symmetry.

**Benchmark.** [3], [5], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Ahmadi et al. (ALPHA Collaboration), Characterization of the 1S–2S transition in antihydrogen, Nature 557, 71 (2018); read as the open-access version in Europe PMC (PMC6784861) | doi:10.1038/s41586-018-0017-2 |
| 2 | E. K. Anderson et al. (ALPHA Collaboration), Observation of the effect of gravity on the motion of antimatter, Nature 621, 716 (2023); read as the open-access version in Europe PMC (PMC10533407) | doi:10.1038/s41586-023-06527-1 |
| 3 | C. Amole et al. (ALPHA Collaboration), An experimental limit on the charge of antihydrogen, Nat. Commun. 5, 3955 (2014) | doi:10.1038/ncomms4955 |
| 4 | S. Aghion et al. (AEgIS Collaboration), A moiré deflectometer for antimatter, Nat. Commun. 5, 4538 (2014) | doi:10.1038/ncomms5538 |
| 5 | M. Charlton et al., Testing fundamental physics in antihydrogen experiments, arXiv:2002.09348 (2020, revised 2022) | doi:10.48550/arXiv.2002.09348 |
| 6 | N. Kuroda et al. (ASACUSA Collaboration), A source of antihydrogen for in-flight hyperfine spectroscopy, Nat. Commun. 5, 3089 (2014) | doi:10.1038/ncomms4089 |
| 7 | M. Diermaier et al., In-beam measurement of the hydrogen hyperfine splitting and prospects for antihydrogen spectroscopy, Nat. Commun. 8, 15749 (2017) | doi:10.1038/ncomms15749 |
| 8 | M. J. Borchert et al. (BASE Collaboration), A 16-parts-per-trillion measurement of the antiproton-to-proton charge-mass ratio, Nature 601, 53 (2022); read as arXiv:2311.16006, which carries a different title | doi:10.1038/s41586-021-04203-w |
| 9 | M. Hori and J. Walz, Physics at CERN's Antiproton Decelerator, Prog. Part. Nucl. Phys. 72, 206 (2013); read as arXiv:1304.3721 | doi:10.1016/j.ppnp.2013.02.004 |
