---
id: CL-MAGNETIC-CONFINEMENT
name: Claims of fusion performance in magnetic confinement
type: claim
field: physics/plasma
applies_when: the paper reports fusion gain, fusion power or neutron yield, a fusion triple product, an energy confinement time or a confinement enhancement factor for a tokamak, stellarator or other magnetic-confinement device, or claims a record, breakeven or progress toward ignition
version: "0.1"
---

# Claims of fusion performance in magnetic confinement

## 1. Which gain, and which powers enter it

**Question.** Which definition of gain does the paper use: fusion power over the heating power delivered at the vessel boundary, over the power absorbed by the fuel, or an engineering or wall-plug gain that counts electrical input? Which heating sources are counted, and for fuels other than deuterium-tritium, is a deuterium-tritium-equivalent value labelled as such?

**Why it matters.** Gains defined against delivered, absorbed or electrical power differ by the absorption and heating efficiencies, so one plasma can have a gain above one under one definition and far below it under another. Losses such as neutral-beam shine-through count against the scientific gain but not against the fuel gain. A gain also inherits the uncertainty of the heating power as well as that of the fusion power.

**Resolved by.** The gain named and defined by an equation; each heating power, ohmic power included, listed with how it was measured; where absorbed power is used, how absorption and losses were estimated; the heating-power uncertainty carried into the gain; equivalent or extrapolated gains labelled and kept apart from measured ones.

**Benchmark.** [1], [2]

## 2. Inputs to the triple product

**Question.** Which density, temperature and confinement time enter the quoted triple product: central or volume-averaged values, ion or electron temperature, fuel-ion or electron density? Is each one measured directly or inferred from another quantity, and is the triple product compared with a requirement evaluated at the temperature actually reached?

**Why it matters.** Central values exceed volume averages by profile factors, so a triple product built from central values is not comparable with one built from averages, or with a criterion derived for a uniform plasma. Setting the ion temperature equal to the electron temperature holds only when equilibration is fast and nothing heats ions and electrons differently, and impurities dilute the fuel so that the fuel-ion density is below the electron density. The triple product needed for a given gain depends on temperature, so a triple product without its temperature does not fix how close a plasma is to breakeven or ignition.

**Resolved by.** Each quantity defined as central or averaged, ion or electron, with the diagnostic that measured it; the profiles shown; where ion values are inferred from electron data, the assumption stated and justified, with the effective charge or dilution measured; the temperature stated alongside the triple product and any breakeven or ignition requirement taken at that temperature; comparisons made only with values built in the same way.

**Benchmark.** [1]

## 3. Stored energy: thermal or total

**Question.** How was the stored energy behind the confinement time obtained (diamagnetic measurement, magnetic equilibrium reconstruction, or integration of measured density and temperature profiles), does it refer to the thermal plasma or include fast particles, and how was any fast-particle part estimated and removed?

**Why it matters.** Magnetic measurements respond to the pressure of all particles, including the fast ions produced by heating, and in heated high-confinement plasmas the fast-ion energy can be as large as the thermal energy. The thermal energy is then usually the measured energy minus a modelled fast-particle term, so the confinement time depends on that model. Stored energies from magnetic and from profile measurements of the same plasmas can differ by tens of per cent.

**Resolved by.** The method and diagnostics behind the stored energy named; thermal and fast-particle parts given separately, with the code and assumptions used for the fast-particle part; magnetic and profile-based estimates compared and any difference reported; the thermal energy used whenever the result is compared with thermal confinement times.

**Benchmark.** [3], [4]

## 4. Transient or sustained performance

**Question.** Is the quoted performance reached at one instant or sustained, for how long compared with the energy confinement time and with the time the current profile takes to settle, and how is the rate of change of stored energy treated in the confinement time and the gain?

**Why it matters.** While the stored energy is still rising, part of the heating power goes into it, and different conventions place this term either in the confinement time or in the absorbed power, so values computed under different conventions are not comparable. A value at a peak instant does not show that the plasma can stay in that state; sustained performance means conditions held for many confinement times with the current profile settled.

**Resolved by.** Time traces of fusion power, stored energy, heating power and the quantities in the triple product; the duration of the reported state in units of the confinement time; the convention for the rate of change of stored energy stated, with values given both ways where other devices are compared; peak and time-averaged values distinguished.

**Benchmark.** [1], [5]

## 5. Comparison with confinement scaling laws

**Question.** When confinement is compared with an empirical scaling law through an enhancement factor, does the paper name the scaling, give the values of each variable it used, compute the confinement time with the same definitions of stored energy and heating power as the database behind the scaling, and say whether the plasma lies within the range of that database?

**Why it matters.** Confinement scalings are regressions over multi-device databases; their fitted dependences change with the subset of data chosen, and their predictions carry large uncertainties when extrapolated. An enhancement factor computed with total instead of thermal energy, or with a different treatment of the heating power, is not comparable with the scaling.

**Resolved by.** The scaling cited with its input values; definitions of stored energy and power matched to those of the scaling's database; the scaling's own uncertainty acknowledged when an enhancement factor is used as evidence; enhancement factors against more than one scaling where they differ.

**Benchmark.** [1], [3], [6]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | S. E. Wurzel and S. C. Hsu, Progress toward fusion energy breakeven and gain as measured against the Lawson criterion, Phys. Plasmas 29, 062103 (2022); read as arXiv:2105.10954 | doi:10.1063/5.0083990 |
| 2 | R. A. Tinguely et al., Neutron diagnostics for the physics of a high-field, compact, Q ≥ 1 tokamak, Fusion Eng. Des. 143, 212 (2019); read as arXiv:1903.09479 | doi:10.1016/j.fusengdes.2019.03.148 |
| 3 | G. Tardini et al., New assessment of the fast ion energy in ASDEX Upgrade H-mode discharges, Nucl. Fusion 61, 036030 (2021) | doi:10.1088/1741-4326/abd3eb |
| 4 | T. Gerbaud et al., Large-scale drifts observed on electron temperature measurements on JET plasmas, arXiv:1205.2969 (2012) | doi:10.48550/arXiv.1205.2969 |
| 5 | A. J. Creely et al., Overview of the SPARC tokamak, J. Plasma Phys. 86, 865860502 (2020) | doi:10.1017/S0022377820001257 |
| 6 | G. Verdoolaege et al., The updated ITPA global H-mode confinement database: description and analysis, Nucl. Fusion 61, 076006 (2021); abstract read on the dataset record OSTI 1814950 | doi:10.1088/1741-4326/abdb91 |
