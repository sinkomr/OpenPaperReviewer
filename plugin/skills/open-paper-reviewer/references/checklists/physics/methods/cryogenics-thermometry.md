---
id: T-CRYOGENICS-THERMOMETRY
name: Cryogenics and low-temperature thermometry
type: technique
field: physics/methods
applies_when: the paper reports measurements below about 4 K in a cryostat or dilution refrigerator, or bases a claim on a sample temperature, a temperature dependence, a transition temperature, a low-temperature saturation or an electron temperature measured there
version: "0.1"
---

# Cryogenics and low-temperature thermometry

## 1. Thermometer, calibration and temperature scale

**Question.** Which thermometer gives each quoted temperature, against what reference and on which temperature scale was it calibrated, and does the calibrated range cover the temperatures at which the claims are made?

**Why it matters.** Most thermometers used at low temperature are secondary devices whose reading is only as good as their calibration against a primary thermometer or a defined scale; the defined scales, the ITS-90 and below 0.65 K the PLTS-2000, are themselves practical approximations to thermodynamic temperature, and the PLTS-2000 is adopted only provisionally. Calibrations are often passed down a chain of thermometers, and a reading outside the calibrated range rests on extrapolation.

**Resolved by.** The type and position of each thermometer named; the calibration reference stated, such as a primary thermometer or a thermometer calibrated on the ITS-90 or the PLTS-2000, with each step of the chain; the calibrated range shown to cover the data, or the lowest temperatures labelled as extrapolated or as nominal refrigerator temperatures.

**Benchmark.** [1], [2], [3], [4]

## 2. Sensor temperature and sample temperature

**Question.** Where is the thermometer relative to the sample, what is the thermal path between them, and does the paper show that the sample is at the thermometer's temperature under the conditions of the measurement?

**Why it matters.** A thermometer on the mixing chamber or sample stage reads its own temperature, not the sample's. Thermal boundary resistance between materials rises steeply as temperature falls and depends on the condition of the interface, so any heat reaching the sample, including heat dissipated by the measurement itself, leaves it warmer than the sensor.

**Resolved by.** The thermal link from sample to cold stage described: materials, joints, clamping and contact area; the power dissipated in the sample estimated and combined with the thermal resistance of the link to bound the temperature difference; a thermometer on the sample or its holder agreeing with the stage thermometer over the range of the claims.

**Benchmark.** [3], [6], [8]

## 3. Electron temperature in devices

**Question.** For electrical measurements on small devices at millikelvin temperatures, is the electron temperature of the sample measured in the same setup, or is it assumed to equal the refrigerator temperature?

**Why it matters.** The coupling between electrons and phonons weakens steeply as temperature falls, so a small heat input keeps the electrons hotter than the lattice. Electron temperatures in devices are often well above the base temperature of the refrigerator, and they separate from it below a temperature that depends on filtering, thermal anchoring and the sample holder.

**Resolved by.** The electron temperature measured with a primary electron thermometer such as a CBT in the same setup, or extracted from a thermally broadened feature of the sample, and plotted against the refrigerator temperature to show where the two agree and where they separate; temperatures below that point given as electron temperatures, or the claim limited to the range where the two agree.

**Benchmark.** [3], [7], [9], [10]

## 4. Self-heating of the thermometer

**Question.** What excitation current, voltage or power was used to read each thermometer, and does the paper show that the reading does not change when the excitation is reduced?

**Why it matters.** The measuring current dissipates power in the sensor, and at millikelvin temperatures a power of the order of femtowatts can decouple the electrons of a resistance sensor from its lattice. The thermometer then reads high, and the lowest temperature reached appears to depend on the excitation.

**Resolved by.** The excitation stated for each thermometer; a self-heating test, reading against excitation power at the lowest temperature used, with the chosen excitation in the range where the reading does not depend on it; for electron thermometers, bias heating included in the analysis.

**Benchmark.** [3], [4], [9]

## 5. Radio-frequency heating and thermalization of wiring

**Question.** How are the measurement and control lines filtered, attenuated and thermally anchored on the way to the sample and the thermometers, and does the paper show that radio-frequency noise and radiation do not raise their temperature?

**Why it matters.** Wires carry heat, electrical noise and thermal radiation from warmer stages. Without filtering and thermal anchoring at each stage, this noise heats the electrons of the sample and of the thermometers, and a thermometer reading that flattens at low temperature can reflect such parasitic heating rather than the true temperature. Attenuators and drive signals dissipate power that the stage where they sit must absorb.

**Resolved by.** A wiring diagram giving the filters, attenuators, thermal anchoring and radiation shields at each stage; measured temperatures shown unchanged when filtering is added or drive power is varied; for driven experiments, the dissipated power compared with the cooling power of the stage where it is dissipated.

**Benchmark.** [4], [7], [8]

## 6. Thermometers in a magnetic field

**Question.** When measurements are made in a magnetic field, is the magnetoresistance of the thermometer known for the sensor used, and was the temperature corrected for it or measured with a thermometer outside the field or insensitive to it, and was heating that comes with the field checked?

**Why it matters.** Resistance thermometers often have a strong magnetoresistance that depends on the sensor type and manufacturing process, can change sign with field and grows at the lowest temperatures, so a zero-field calibration used in a field gives a temperature error. Thermometers based on superconductors are strongly field dependent, while a CBT is largely insensitive to field. In a field, eddy currents induced in metal parts, for example by vibration, also add heating that grows with the field.

**Resolved by.** A field-dependent calibration for the sensor used, a thermometer in a field-compensated region with a stated thermal link to the sample, or a field-insensitive thermometer; the size of any correction stated; the sample or electron temperature checked at each field used, and during field sweeps, with the refrigerator settings unchanged.

**Benchmark.** [3], [5], [10]

## 7. Time to reach equilibrium

**Question.** How long was the system left to settle after each change of temperature, field or power, and how was that time chosen?

**Why it matters.** Thermal time constants of thermometers and samples lengthen steeply as temperature falls, and a slow heat leak can keep a sensor from reaching equilibrium for hours or days. A reading taken before equilibrium, or data taken while sweeping faster than the thermal response, assigns the wrong temperature to what is measured.

**Resolved by.** Settling times stated and based on the measured relaxation of the thermometer and of a temperature-sensitive property of the sample; swept data compared with data at fixed temperature, or warming and cooling sweeps at more than one rate shown to agree; the time since cool-down given where slow heat release matters.

**Benchmark.** [4], [7], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | Comité International des Poids et Mesures (CIPM), Recommendation 1 (CI-2000): Extension of the International Temperature Scale below 0.65 K, 89th meeting of the CIPM (2000) | https://bipm.org/committees/ci/cipm/89-2000/resolution-1 |
| 2 | Consultative Committee for Thermometry (CCT), Recommendation 3 (2005): Creation of a mise en pratique of the definition of the kelvin, 23rd meeting of the CCT (2005) | https://www.bipm.org/committees/cc/cct/23-2005/resolution-3 |
| 3 | F. Giazotto et al., Opportunities for mesoscopics in thermometry and refrigeration: Physics and applications, Rev. Mod. Phys. 78, 217 (2006); read as preprint arXiv:cond-mat/0508093 | doi:10.1103/RevModPhys.78.217 |
| 4 | S. A. Myers et al., A ruthenium oxide thermometer for dilution refrigerators operating down to 5 mK, Cryogenics 119, 103367 (2021); read as preprint arXiv:2110.03788 | doi:10.1016/j.cryogenics.2021.103367 |
| 5 | M. Watanabe et al., Magnetoresistance of RuO2-based resistance thermometers below 0.3 K, Cryogenics 41, 143 (2001); read as preprint arXiv:cond-mat/0007399 | doi:10.1016/S0011-2275(01)00066-2 |
| 6 | E. T. Swartz and R. O. Pohl, Thermal boundary resistance, Rev. Mod. Phys. 61, 605 (1989) | doi:10.1103/RevModPhys.61.605 |
| 7 | C. P. Scheller et al., Silver-epoxy microwave filters and thermalizers for millikelvin experiments, Appl. Phys. Lett. 104, 211106 (2014); read as preprint arXiv:1403.6205 | doi:10.1063/1.4880099 |
| 8 | S. Krinner et al., Engineering cryogenic setups for 100-qubit scale superconducting circuit systems, EPJ Quantum Technol. 6, 2 (2019); read as preprint arXiv:1806.07862 | doi:10.1140/epjqt/s40507-019-0072-0 |
| 9 | D. I. Bradley et al., Nanoelectronic primary thermometry below 4 mK, Nat. Commun. 7, 10455 (2016); read as preprint arXiv:1505.07244, titled Nanoelectronic thermometers optimised for sub-10 millikelvin operation | doi:10.1038/ncomms10455 |
| 10 | Z. Iftikhar et al., Primary thermometry triad at 6 mK in mesoscopic circuits, Nat. Commun. 7, 12908 (2016); read as preprint arXiv:1610.03716 | doi:10.1038/ncomms12908 |
