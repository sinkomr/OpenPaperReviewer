---
id: T-TRANSPORT
name: Electrical transport measurements
type: technique
field: physics/condensed-matter
applies_when: the paper reports resistance or resistivity, current-voltage characteristics, Hall effect or magnetoresistance data, or bases a claim about conductivity, carrier type, carrier density, mobility, contact resistance or an electronic transition on them
version: "0.1"
---

# Electrical transport measurements

## 1. Terminal configuration and contacts

**Question.** Does the paper state which contacts carried the current and which sensed the voltage for each data set, and does it show that the contacts are ohmic (linear current-voltage characteristics) under the measurement conditions?

**Why it matters.** A two-terminal resistance includes the contacts and leads in series with the sample and is usually not the sample resistance. A four-terminal measurement removes them only if the voltage probes draw negligible current, and contacts that are non-linear, or much more resistive than the others, are a recognised source of error in resistivity and Hall measurements.

**Resolved by.** A diagram or image of the contact layout with the configuration named for each data set; four-terminal data wherever a resistivity is quoted; contact current-voltage curves, or a comparison of two- and four-terminal resistance, showing linear contacts of similar resistance; where only two terminals are possible, a measurement or argument showing that the contact contribution is negligible.

**Benchmark.** [1], [3]

## 2. Geometry and conversion to resistivity

**Question.** How was the measured resistance converted to a resistivity or sheet resistance (which formula and geometric factor), how were the sample dimensions and the thickness of the conducting layer measured, and do the sample and contacts meet the assumptions of that formula?

**Why it matters.** The simple four-probe formulas assume a sample much larger than the probe spacing, and the van der Pauw relation assumes a thin, homogeneous, isotropic sample without holes and with small contacts on its edge. Finite thickness, a nearby edge and contacts of finite size each change the factor, by up to a factor of two near an edge and by far more when isotropic factors are applied to an anisotropic sample. Any error in the thickness passes directly into the resistivity.

**Resolved by.** The formula and correction factors stated together with the dimensions that enter them; contact size and position given relative to the sample size; for van der Pauw samples, both characteristic resistances reported and shown to satisfy the current-reversal and reciprocity checks; the thickness measured and its uncertainty propagated; for anisotropic materials, a configuration that separates the resistivity components instead of a single isotropic formula.

**Benchmark.** [1], [2], [4]

## 3. Hall signal and offsets

**Question.** How was the Hall voltage separated from offset voltages (which field polarities and current directions were measured), and is the raw transverse signal shown so that the Hall signal can be compared with the offset and its drift?

**Why it matters.** The transverse voltage contains an offset from non-symmetric contact placement, sample shape and temperature non-uniformity that can be much larger than the Hall voltage, as is typical for low-mobility films and for thick, heavily doped samples. Subtracting data taken at opposite field polarities removes the offset only if it is the same in both. When the Hall signal is small compared with the offset, simple field reversal often does not give reliable results, and temperature fluctuations and slow settling in resistive samples add to the difficulty.

**Resolved by.** Raw transverse voltage for both field polarities and both current directions, with the zero-field offset stated; evidence that the offset was stable over the reversal, such as repeated sweeps, settling times and temperature stability, or a correction scheme designed for small signals; the field at the sample measured or calibrated; for ac methods, a check that the result does not depend on frequency.

**Benchmark.** [2], [4], [5]

## 4. From Hall data to carrier density and mobility

**Question.** Which model converts the Hall data into carrier density and mobility, and does the paper show the Hall resistance against field and test the model's assumptions of a single carrier type and a uniform sample?

**Why it matters.** The single-carrier relations return the actual density and mobility only for one carrier type in a uniform sample. With several carrier types or with grain boundaries they return apparent values, and the apparent Hall mobility can be far below the actual mobility. The usual two-carrier analysis has four free parameters and assumed carrier signs, which makes the fitted values ambiguous unless they are constrained.

**Resolved by.** Hall resistance plotted against field over the full range, not a value at one field; where it is non-linear or changes sign, an analysis that uses the longitudinal and Hall data together, states which parameters were free or constrained and gives their uncertainties; agreement between Hall voltages from different contact pairs as a uniformity check.

**Benchmark.** [2], [5], [6]

## 5. Current distribution and homogeneity

**Question.** Does the paper show that the current flows uniformly through the region between the voltage contacts, in particular for magnetoresistance measured with the field along the current in high-mobility samples, and that the result does not depend on which contact pairs are used?

**Why it matters.** Converting a voltage to a resistivity assumes a known, uniform current density. In a high-mobility conductor a field along the current suppresses the transverse conductivity and focuses the current into a narrow jet between the current contacts; voltage contacts at the sample edge then read a falling voltage that mimics a negative magnetoresistance, and its sign can change with contact placement. In an inhomogeneous sample, different contact pairs likewise give different answers.

**Resolved by.** Voltage pairs at different positions across the sample, for example on the line joining the current contacts and at the edge, showing the same field dependence; the result unchanged when the voltage contacts are moved; an estimate of the field at which mobility times field reaches about five, compared with the field range of the claimed effect; agreement between contact configurations as a homogeneity check.

**Benchmark.** [1], [2], [7]

## 6. Excitation level, heating and thermoelectric offsets

**Question.** What excitation current or voltage and, for ac measurements, what frequency were used, and does the paper show that the result does not depend on them?

**Why it matters.** Too large a current heats the sample or the contacts, most readily where the contact resistance is high, and changes the quantity being measured. Thermoelectric voltages from temperature gradients across dissimilar lead materials add to dc readings, and non-uniform sample temperature adds to Hall offsets. In ac measurements the detected voltage can depend on frequency.

**Resolved by.** The excitation stated for each data set; the same resistance obtained at two or more current levels; dc readings averaged over both current polarities; the dissipated power kept to a stated low level; for lock-in measurements, a frequency-dependence check; illumination and atmosphere during the measurement stated.

**Benchmark.** [2], [3], [4]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | I. Miccoli et al., The 100th anniversary of the four-point probe technique: the role of probe geometries in isotropic and anisotropic systems, J. Phys.: Condens. Matter 27, 223201 (2015) | doi:10.1088/0953-8984/27/22/223201 |
| 2 | National Institute of Standards and Technology (NIST), Physical Measurement Laboratory, Resistivity and Hall Measurements, web page in the series Hall Effect Measurements (created 2010, updated 2022, archived) | https://www.nist.gov/pml/nanoscale-device-characterization-division/popular-links/hall-effect/resistivity-and-hall |
| 3 | National Institute of Standards and Technology (NIST), Physical Measurement Laboratory, Hall Effect Measurements Sources of Error, web page in the same series (created 2010, updated 2022, archived) | https://www.nist.gov/pml/nanoscale-device-characterization-division/popular-links/hall-effect/resistivity-and-hall/hall |
| 4 | 16NRM01 EMPIR GRACE consortium, Good Practice Guide on the electrical characterisation of graphene using contact methods, edited by A. Fabricius, A. Catanzaro and A. Cultrera, version 1.0 (2020), ISBN 978-88-945324-0-1; read as arXiv:2007.13348 | doi:10.48550/arXiv.2007.13348 |
| 5 | F. Werner, Hall measurements on low-mobility thin films, J. Appl. Phys. 122, 135306 (2017) | doi:10.1063/1.4990470 |
| 6 | G. Eguchi and S. Paschen, Robust scheme for magnetotransport analysis in topological insulators, Phys. Rev. B 99, 165128 (2019); read as preprint arXiv:1609.04134 | doi:10.1103/PhysRevB.99.165128 |
| 7 | N. P. Ong and S. Liang, Experimental signatures of the chiral anomaly in Dirac–Weyl semimetals, Nat. Rev. Phys. 3, 394 (2021); read as preprint arXiv:2010.08564, which carries a different title | doi:10.1038/s42254-021-00310-9 |
