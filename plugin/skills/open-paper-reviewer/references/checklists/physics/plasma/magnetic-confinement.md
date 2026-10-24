---
id: CL-MAGNETIC-CONFINEMENT
name: Claims of fusion performance in magnetic confinement
type: claim
field: physics/plasma
applies_when: the paper reports fusion gain, fusion power or neutron yield, a fusion triple product, an energy confinement time or a confinement enhancement factor for a tokamak, stellarator or other magnetic-confinement device, or claims a record, breakeven or progress toward ignition
version: "0.1"
---

# Claims of fusion performance in magnetic confinement

A claim of fusion performance in a magnetic-confinement device, such as a tokamak or stellarator, asserts that a plasma reached a stated fusion power, fusion gain (Q, fusion power divided by a heating power), energy confinement time (τE, stored energy divided by the power lost) or triple product (density times temperature times confinement time, the Lawson parameter). Each of these numbers rests on definitions and on inferred quantities, so a careful demonstration states which definition it uses, how each input was measured, and how long the performance lasted.

## 1. Which gain, and which powers enter it

**Question.** Which definition of gain does the paper use: fusion power over the heating power delivered at the vessel boundary, over the power absorbed by the fuel, or an engineering or wall-plug gain that counts electrical input? Which heating sources are counted, and for fuels other than deuterium-tritium, is a deuterium-tritium-equivalent value labelled as such?

**Why it matters.** Gains defined against delivered, absorbed or electrical power differ by the absorption and heating efficiencies, so one plasma can have a gain above one under one definition and far below it under another. Losses such as neutral-beam shine-through count against the scientific gain but not against the fuel gain. A gain also inherits the uncertainty of the heating power as well as that of the fusion power.

**Resolved by.** The gain named and defined by an equation; each heating power, ohmic power included, listed with how it was measured; where absorbed power is used, how absorption and losses were estimated; the heating-power uncertainty carried into the gain; equivalent or extrapolated gains labelled and kept apart from measured ones.

**Benchmark.** [1], [2]

## 2. Measuring fusion power

**Question.** How was the fusion power or yield obtained from detector signals: which detectors, how were they calibrated absolutely in place and at the relevant neutron energy, and how was the calibration transferred from the calibration source to the plasma?

**Why it matters.** Detectors see a tiny fraction of the neutrons produced, so the fusion power depends on an absolute calibration that converts counts into emitted neutrons. A calibration made with a point source inside the vessel must be transferred to an extended plasma source by neutron-transport modelling, because scattering in the surrounding structure changes the response. Reported total uncertainties of such calibrations range from below ten to nearly twenty per cent.

**Resolved by.** Detector types and positions; the method, source and date of the in-vessel calibration; the neutronics model used to transfer it; a total uncertainty with its main contributions; agreement between independent systems such as fission chambers, activation foils and spectrometers; corrections for scattered-neutron and gamma-ray backgrounds.

**Benchmark.** [2], [3]

## 3. Thermonuclear and non-thermal fusion

**Question.** What share of the fusion reactions comes from a thermal fuel population, and what share from beam ions or ions accelerated by radiofrequency heating reacting with the plasma, and how was that split determined?

**Why it matters.** With neutral-beam or ion-cyclotron heating the fuel ions are not Maxwellian, and fast ions reacting with the bulk add reactions that the thermal plasma alone would not produce. These reactions do not show that the thermal plasma reached the stated temperature and confinement, and they do not extrapolate to gain in the same way, since beam ions usually slow down before they fuse. Ion temperatures and fuel ratios inferred from neutron spectra assume a thermal distribution unless the non-thermal parts are modelled.

**Resolved by.** Thermal and non-thermal contributions to the fusion rate given separately, from modelling of the fast-ion distribution checked against neutron spectra or other fast-ion measurements; the distribution assumed when an ion temperature is taken from a spectrum; conclusions about thermal plasma performance based on the thermal part.

**Benchmark.** [1], [2]

## 4. Inputs to the triple product

**Question.** Which density, temperature and confinement time enter the quoted triple product: central or volume-averaged values, ion or electron temperature, fuel-ion or electron density? Is each one measured directly or inferred from another quantity, and is the triple product compared with a requirement evaluated at the temperature actually reached?

**Why it matters.** Central values exceed volume averages by profile factors, so a triple product built from central values is not comparable with one built from averages, or with a criterion derived for a uniform plasma. Setting the ion temperature equal to the electron temperature holds only when equilibration is fast and nothing heats ions and electrons differently, and impurities dilute the fuel so that the fuel-ion density is below the electron density. The triple product needed for a given gain depends on temperature, so a triple product without its temperature does not fix how close a plasma is to breakeven or ignition.

**Resolved by.** Each quantity defined as central or averaged, ion or electron, with the diagnostic that measured it; the profiles shown; where ion values are inferred from electron data, the assumption stated and justified, with the effective charge or dilution measured; the temperature stated alongside the triple product and any breakeven or ignition requirement taken at that temperature; comparisons made only with values built in the same way.

**Benchmark.** [1]

## 5. Stored energy: thermal or total

**Question.** How was the stored energy behind the confinement time obtained (diamagnetic measurement, magnetic equilibrium reconstruction, or integration of measured density and temperature profiles), does it refer to the thermal plasma or include fast particles, and how was any fast-particle part estimated and removed?

**Why it matters.** Magnetic measurements respond to the pressure of all particles, including the fast ions produced by heating, and in heated high-confinement plasmas the fast-ion energy can be as large as the thermal energy. The thermal energy is then usually the measured energy minus a modelled fast-particle term, so the confinement time depends on that model. Stored energies from magnetic and from profile measurements of the same plasmas can differ by tens of per cent.

**Resolved by.** The method and diagnostics behind the stored energy named; thermal and fast-particle parts given separately, with the code and assumptions used for the fast-particle part; magnetic and profile-based estimates compared and any difference reported; the thermal energy used whenever the result is compared with thermal confinement times.

**Benchmark.** [4], [5]

## 6. Transient or sustained performance

**Question.** Is the quoted performance reached at one instant or sustained, for how long compared with the energy confinement time and with the time the current profile takes to settle, and how is the rate of change of stored energy treated in the confinement time and the gain?

**Why it matters.** While the stored energy is still rising, part of the heating power goes into it, and different conventions place this term either in the confinement time or in the absorbed power, so values computed under different conventions are not comparable. A value at a peak instant does not show that the plasma can stay in that state; sustained performance means conditions held for many confinement times with the current profile settled.

**Resolved by.** Time traces of fusion power, stored energy, heating power and the quantities in the triple product; the duration of the reported state in units of the confinement time; the convention for the rate of change of stored energy stated, with values given both ways where other devices are compared; peak and time-averaged values distinguished.

**Benchmark.** [1], [6]

## 7. Comparison with confinement scaling laws

**Question.** When confinement is compared with an empirical scaling law through an enhancement factor, does the paper name the scaling, give the values of each variable it used, compute the confinement time with the same definitions of stored energy and heating power as the database behind the scaling, and say whether the plasma lies within the range of that database?

**Why it matters.** Confinement scalings are regressions over multi-device databases; their fitted dependences change with the subset of data chosen, and their predictions carry large uncertainties when extrapolated. An enhancement factor computed with total instead of thermal energy, or with a different treatment of the heating power, is not comparable with the scaling.

**Resolved by.** The scaling cited with its input values; definitions of stored energy and power matched to those of the scaling's database; the scaling's own uncertainty acknowledged when an enhancement factor is used as evidence; enhancement factors against more than one scaling where they differ.

**Benchmark.** [1], [4], [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | S. E. Wurzel and S. C. Hsu, Progress toward fusion energy breakeven and gain as measured against the Lawson criterion, Phys. Plasmas 29, 062103 (2022); read as arXiv:2105.10954 | doi:10.1063/5.0083990 | full text | Sec. I: Maxwellian populations assumed; beam reactants usually slow down faster than they fuse. Secs. III.4 and III.8: scientific gain (heating power at the vessel boundary, counting losses such as beam shine-through), fuel gain (absorbed power), engineering and wall-plug gains; Fig. 2 caption: deuterium-tritium-equivalent gain for other fuels. Sec. III.7: a triple product does not correspond to a unique gain unless the temperature is specified. Sec. IV.1.1: flat-top must exceed the confinement time. Secs. IV.1.2 and IV.1.4: peak versus volume-averaged values and profile factors. Secs. IV.1.3 and IV.1.5: impurity dilution; ion temperature equal to electron temperature only with fast equilibration. Sec. IV.1.6: two conventions for the rate of change of stored energy, folded into a modified confinement time or into absorbed power |
| 2 | R. A. Tinguely, A. Rosenthal, R. Simpson et al., Neutron diagnostics for the physics of a high-field, compact, Q ≥ 1 tokamak, Fusion Eng. Des. 143, 212–225 (2019); read as arXiv:1903.09479 | doi:10.1016/j.fusengdes.2019.03.148 | full text | Flux-monitor section: detectors see a tiny fraction of neutrons, so precise calibration converts detected to produced neutrons; calibration sources and reported total errors of about 7 to 18 per cent across devices; gain needs the external heating power, with a 10 per cent heating-power uncertainty combined in the test for Q ≥ 1. Spectrometer section: with beam or ion-cyclotron heating the ions are non-thermal and Maxwellian fits break down. Neutron-camera and modelling sections: scattered-neutron and gamma backgrounds |
| 3 | P. Batistoni, S. Popovichev, A. Cufar et al., 14 MeV calibration of JET neutron detectors—phase 1: calibration and characterization of the neutron source, Nucl. Fusion 58, 026012 (2018) | doi:10.1088/1741-4326/aa98f6 | abstract | Abstract: in-vessel calibration of neutron monitors with a 14 MeV generator to a target accuracy of ±10 per cent; the generator characterised with several independent detectors; a validated neutronics model needed to derive detector response to plasma neutrons from the generator calibration |
| 4 | G. Tardini, M. Weiland, C. Angioni, M. Cavedon, F. Ryter, P. A. Schneider and the ASDEX Upgrade Team, New assessment of the fast ion energy in ASDEX Upgrade H-mode discharges, Nucl. Fusion 61, 036030 (2021) | doi:10.1088/1741-4326/abd3eb | abstract | Abstract: confinement scalings are used to project performance; thermal energy is usually the measured magnetohydrodynamic energy minus a simulated fast-ion energy; with beam or ion-cyclotron heating the fast-ion energy can be as high as the thermal energy, so its accuracy matters |
| 5 | T. Gerbaud, S. Schmuck, B. Alper et al., Large-scale drifts observed on electron temperature measurements on JET plasmas, arXiv:1205.2969 (2012) | doi:10.48550/arXiv.1205.2969 | full text | Sec. VI: thermal energy from profiles compared with the diamagnetic energy minus the perpendicular fast-particle energy; profile-based values about 20 to 30 per cent below the magnetic value, with the cause unresolved |
| 6 | A. J. Creely, M. J. Greenwald, S. B. Ballinger et al., Overview of the SPARC tokamak, J. Plasma Phys. 86, 865860502 (2020) | doi:10.1017/S0022377820001257 | full text | Sec. 3: a 10 s flat-top spanning more than ten energy confinement times, with the current profile equilibrated within about 5 s; Sec. 4.1: higher power for shorter periods would likely come with lower gain |
| 7 | G. Verdoolaege, S. M. Kaye, C. Angioni, O. J. W. F. Kardaun, M. Maslov, M. Romanelli, F. Ryter and K. Thomsen, The updated ITPA global H-mode confinement database: description and analysis, Nucl. Fusion 61, 076006 (2021); abstract read on the dataset record OSTI 1814950 | doi:10.1088/1741-4326/abdb91 | abstract | Abstract: power-law scalings fitted to several subsets (by wall material and confinement regime) with ordinary least squares and two robust methods, with dependences that differ between devices and subsets; conversion to dimensionless form gives large error bars on predictions; extrapolation to ITER gives a somewhat lower confinement time than the IPB98(y,2) scaling, and comparison with more flexible regression models is called for |
