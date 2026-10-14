---
id: T-TRANSPORT
name: Electrical transport measurements
type: technique
field: physics
applies_when: the paper reports resistance or resistivity, current-voltage characteristics, Hall effect or magnetoresistance data, or bases a claim about conductivity, carrier type, carrier density, mobility, contact resistance or an electronic transition on them
version: "0.1"
---

# Electrical transport measurements

Transport measurements are used to claim a resistivity and its dependence on temperature, field or gate voltage, the type, density and mobility of carriers, contact resistances, and transitions between electronic states. All of these are inferred from currents and voltages at a few contacts on a sample of finite size.

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

**Resolved by.** Voltage pairs at different positions across the sample, for example on the line joining the current contacts and at the edge, showing the same field dependence; the result unchanged when the voltage contacts are moved; an estimate of the field at which the product of mobility and field becomes large, compared with the field range of the claimed effect; agreement between contact configurations as a homogeneity check.

**Benchmark.** [1], [2], [7]

## 6. Excitation level, heating and thermoelectric offsets

**Question.** What excitation current or voltage and, for ac measurements, what frequency were used, and does the paper show that the result does not depend on them?

**Why it matters.** Too large a current heats the sample or the contacts, most readily where the contact resistance is high, and changes the quantity being measured. Thermoelectric voltages from temperature gradients across dissimilar lead materials add to dc readings, and non-uniform sample temperature adds to Hall offsets. In ac measurements the detected voltage can depend on frequency.

**Resolved by.** The excitation stated for each data set; the same resistance obtained at two or more current levels; dc readings averaged over both current polarities; the dissipated power kept to a stated low level; for lock-in measurements, a frequency-dependence check.

**Benchmark.** [2], [3], [4]

## 7. Parameters extracted from transistor characteristics

**Question.** When mobility, threshold voltage or contact resistance are extracted from field-effect device characteristics, does the paper show the full transfer and output curves, state the model and the bias range of each fit, and separate the contact contribution from the channel?

**Why it matters.** The standard transistor equations assume an ideal channel with ohmic contacts. A contact resistance that depends on gate voltage produces a steep, non-linear turn-on, and fitting that region can overestimate mobility by an order of magnitude or more. Field-effect mobility can be under- or overestimated depending on the bias, contact resistance, channel length and gate capacitance used, and a contact resistance from a transfer-length series is unreliable when channel resistance dominates every device.

**Resolved by.** Transfer curves on linear and logarithmic scales with forward and backward sweeps, and output curves; mobility plotted against gate voltage or carrier density, not only a peak value; a measured gate capacitance; contact resistance determined independently, for example by a transfer-length series that includes contact-dominated devices, gated four-probe or impedance measurements; the method behind each quoted mobility stated and cross-checked with a second method.

**Benchmark.** [8], [9], [10]

## 8. Reproducibility, uncertainty and reporting

**Question.** How many samples or devices were measured, how reproducible are the results between them and between repeated runs, and are uncertainties and measurement conditions reported for the quantities on which the claims rest?

**Why it matters.** Transport properties vary between nominally identical samples and with ambient conditions, illumination and sweep history, so one sample or one sweep may not be representative. A derived quantity such as mobility combines the uncertainties of several measured quantities, including geometry and field, and these are often interdependent.

**Resolved by.** The number of samples or devices stated and the spread shown (error bars or distributions), not only the best result; repeated measurements giving a statistical uncertainty that is combined with instrument and geometry contributions for derived quantities; sweep direction, rate and any hysteresis reported; temperature, atmosphere and illumination during the measurement recorded; the analysis procedure described in enough detail to be repeated.

**Benchmark.** [3], [4], [9]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | I. Miccoli, F. Edler, H. Pfnür and C. Tegenkamp, The 100th anniversary of the four-point probe technique: the role of probe geometries in isotropic and anisotropic systems, J. Phys.: Condens. Matter 27, 223201 (2015) | doi:10.1088/0953-8984/27/22/223201 | full text | Sec. 1: a two-probe resistance includes the contacts and is usually not the sample resistance; four probes remove them if the voltage probes draw no current. Sec. 3: correction factors for finite thickness, edge proximity (up to a factor of two) and lateral size. Sec. 4: the van der Pauw theorem needs a thin, homogeneous, isotropic sample without holes and small contacts on the periphery. Sec. 5: isotropic correction factors do not carry over to anisotropic samples, where errors can be much larger |
| 2 | National Institute of Standards and Technology (NIST), Physical Measurement Laboratory, Resistivity and Hall Measurements, web page in the series Hall Effect Measurements (created 2010, updated 2022, archived) | https://www.nist.gov/pml/nanoscale-device-characterization-division/popular-links/hall-effect/resistivity-and-hall | full text | "Sample Geometry": contact size and thickness must be much smaller than the contact spacing, with error of order D/L. "Definitions for Resistivity Measurements": same lead wire and contact material to limit thermoelectric effects. "Resistivity Measurements": power limit of 5 mW (preferably 1 mW), current-reversal and reciprocity checks to within 5%. "Definitions for Hall Measurements" to "Hall Calculations": the Hall voltage can be only microvolts in thick, heavily doped samples, and the larger problem is the offset voltage from non-symmetric contacts, sample shape and non-uniform temperature, removed by reversing the field; eight readings over both field and current directions; Hall voltages from the two diagonal contact sets agree for a uniform sample; single-carrier formulas and the quantities to report |
| 3 | National Institute of Standards and Technology (NIST), Physical Measurement Laboratory, Hall Effect Measurements Sources of Error, web page in the same series (created 2010, updated 2022, archived) | https://www.nist.gov/pml/nanoscale-device-characterization-division/popular-links/hall-effect/resistivity-and-hall/hall | full text | Whole page (eight checks): linear contact current-voltage characteristics; no contact much more resistive than the others; voltages settling after current reversal; sample kept in the dark; uniform sample temperature; dissimilar wiring materials under temperature gradients |
| 4 | 16NRM01 EMPIR GRACE consortium, Good Practice Guide on the electrical characterisation of graphene using contact methods, edited by A. Fabricius, A. Catanzaro and A. Cultrera, version 1.0 (2020), ISBN 978-88-945324-0-1; read as arXiv:2007.13348 | doi:10.48550/arXiv.2007.13348 | full text | Secs. 1.1.1 and 1.2.2: correction factors when the sample is small or probes are near an edge; readings at opposite current polarity averaged to reduce thermoelectric effects. Secs. 1.1.4 and 1.2.3: ambient conditions recorded; uncertainty from repeatability, instrument specification and geometry. Sec. 2.2.2: heating identified by measuring at two current levels. Sec. 2.2.4: corrections for contact size and position. Secs. 3.2.2 to 3.2.4: field measured at the sample position, frequency test for ac measurements, mobility uncertainty combining sheet resistance, Hall resistance and field |
| 5 | F. Werner, Hall measurements on low-mobility thin films, J. Appl. Phys. 122, 135306 (2017) | doi:10.1063/1.4990470 | abstract | Abstract: when the Hall signal is small compared with offset voltages, simple field reversal often does not give reliable results; temperature fluctuations and long settling times matter for resistive samples; grain boundaries and multi-carrier conduction can give apparent Hall mobilities well below the actual mobility |
| 6 | G. Eguchi and S. Paschen, Robust scheme for magnetotransport analysis in topological insulators, Phys. Rev. B 99, 165128 (2019); read as preprint arXiv:1609.04134 | doi:10.1103/PhysRevB.99.165128 | full text | Opening paragraphs and Fig. 1: the common two-carrier analysis of longitudinal and Hall resistance has four free parameters plus assumed carrier types, and so many open parameters make the fits unreliable; slope and sign changes of the Hall trace as multi-carrier signatures |
| 7 | N. P. Ong and S. Liang, Experimental signatures of the chiral anomaly in Dirac–Weyl semimetals, Nat. Rev. Phys. 3, 394–404 (2021); read as preprint arXiv:2010.08564, which carries a different title | doi:10.1038/s42254-021-00310-9 | full text | Preprint Sec. IV: in high-mobility samples a field along the current focuses the current into a narrow jet, lowering the voltage at edge contacts and mimicking a negative magnetoresistance whose sign can change with contact placement; a test compares voltage pairs on the current axis and at the edge; rule of thumb based on the field at which mobility times field exceeds about 5 |
| 8 | E. G. Bittle, J. I. Basham, T. N. Jackson, O. D. Jurchescu and D. J. Gundlach, Mobility overestimation due to gated contacts in organic field-effect transistors, Nat. Commun. 7, 10908 (2016) | doi:10.1038/ncomms10908 | full text | Abstract, Results and Discussion: a gate-voltage-dependent contact resistance gives non-ideal transfer curves, and applying the ideal transistor model to them overestimates mobility by an order of magnitude or more; standard extraction methods suit devices with ohmic contacts; contact and channel separated by impedance measurements |
| 9 | Z. Cheng, C.-S. Pang, P. Wang, S. T. Le, Y. Wu, D. Shahrjerdi, I. Radu, M. C. Lemme, L.-M. Peng, X. Duan, Z. Chen, J. Appenzeller, S. J. Koester, E. Pop, A. D. Franklin and C. A. Richter, How to report and benchmark emerging field-effect transistors, Nat. Electron. 5, 416–423 (2022); read as the author manuscript hosted by NIST (publication record 933042) | doi:10.1038/s41928-022-00798-8 | full text | Section "Field-effect transistor structure and key parameters" with Table 1: forward and backward sweeps with sweep conditions listed, measured gate capacitance, field-effect mobility under- or overestimated depending on bias, contact resistance and channel length, cross-validation by several methods, statistics and variation shown. Discussion of Fig. 3d: transfer-length contact resistance is of doubtful validity when channel resistance dominates. Conclusions: uncertainty and spread reported for derived parameters, procedures described in detail |
| 10 | H. H. Choi, K. Cho, C. D. Frisbie, H. Sirringhaus and V. Podzorov, Critical assessment of charge mobility extraction in FETs, Nat. Mater. 17, 2–7 (2018) | doi:10.1038/nmat5035 | abstract | Abstract: extracting mobility from field-effect transistor measurements has common pitfalls that lead to erroneous reported values, and the article gives practical recommendations to avoid them |
