---
id: T-CRYOGENICS-THERMOMETRY
name: Cryogenics and low-temperature thermometry
type: technique
field: physics/methods
applies_when: the paper reports measurements below about 4 K in a cryostat or dilution refrigerator, or bases a claim on a sample temperature, a temperature dependence, a transition temperature, a low-temperature saturation or an electron temperature measured there
version: "0.1"
---

# Cryogenics and low-temperature thermometry

Low-temperature measurements are used to claim the temperature at which a property appears, changes or saturates, and how it depends on temperature down to the millikelvin range in cryostats and dilution refrigerators. Each such claim rests on the reading of a thermometer, usually a secondary sensor such as a ruthenium oxide (RuO2) resistor calibrated on the International Temperature Scale of 1990 (ITS-90) or the Provisional Low Temperature Scale of 2000 (PLTS-2000), or on a primary thermometer such as a Coulomb blockade thermometer (CBT), and on the assumption that the sample is at the temperature the thermometer reads.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | Comité International des Poids et Mesures (CIPM), Recommendation 1 (CI-2000): Extension of the International Temperature Scale below 0.65 K, 89th meeting of the CIPM (2000) | https://bipm.org/committees/ci/cipm/89-2000/resolution-1 | full text | Whole recommendation: the PLTS-2000, based on the helium-3 melting pressure in thermodynamic temperature, is adopted provisionally from about 0.9 mK to 1 K, extending the ITS-90 below its lower limit of 0.65 K |
| 2 | Consultative Committee for Thermometry (CCT), Recommendation 3 (2005): Creation of a mise en pratique of the definition of the kelvin, 23rd meeting of the CCT (2005) | https://www.bipm.org/committees/cc/cct/23-2005/resolution-3 | full text | Considerations: the ITS-90 and PLTS-2000 are the accepted practical scales, whose temperatures approximate thermodynamic temperature, with differences and their uncertainties to be documented |
| 3 | F. Giazotto, T. T. Heikkilä, A. Luukanen, A. M. Savin and J. P. Pekola, Opportunities for mesoscopics in thermometry and refrigeration: Physics and applications, Rev. Mod. Phys. 78, 217–274 (2006); read as preprint arXiv:cond-mat/0508093 | doi:10.1103/RevModPhys.78.217 | full text | Sec. II.4, Eq. 24: power from electrons to phonons scales with the difference of fifth powers of their temperatures, so the two can differ. Sec. II.7: boundary resistance between bulk solids scales as the inverse cube of temperature. Sec. III introduction: primary thermometers need no calibration and are used to calibrate the more common secondary ones; lithographic sensors must keep self-heating very small. Sec. III.1: superconductor-based junctions are field sensitive. Sec. III.2: the CBT is a primary thermometer, essentially immune to fields tested above 20 T, whereas resistance thermometers often have strong magnetoresistance; the CBT's lowest temperature is limited by bias self-heating |
| 4 | S. A. Myers, H. Li and G. A. Csáthy, A ruthenium oxide thermometer for dilution refrigerators operating down to 5 mK, Cryogenics 119, 103367 (2021); read as preprint arXiv:2110.03788 | doi:10.1016/j.cryogenics.2021.103367 | full text | "Cryogenic setup": RuO2 sensors calibrated against a carbon thermometer that was itself calibrated against a helium-3 viscometer. "Calibration curves" and "Low temperature performance": a conventional sensor saturates below about 20 mK, attributed to parasitic rf heating, removed by an rf-tight enclosure with an in situ silver-epoxy filter. "Self-heating analysis": electrons decouple from phonons at about 1 fW at 6.7 mK, so excitation is limited to 100 pA. "Effective temperature of black body radiation": the parasitic power of about 0.45 pW matched to black-body radiation at an effective temperature of about 0.4 K reaching unshielded wiring next to the sensor, possibly leaking through openings in the cold plate. "Equilibration time": the time constant rises steeply as temperature falls, roughly as the inverse 2.8 power below about 40 mK, making the sensor impractical below about 5 mK |
| 5 | M. Watanabe, M. Morishita and Y. Ootuka, Magnetoresistance of RuO2-based resistance thermometers below 0.3 K, Cryogenics 41, 143–148 (2001); read as preprint arXiv:cond-mat/0007399 | doi:10.1016/S0011-2275(01)00066-2 | full text | Introduction: the magnetoresistance of RuO2 thermometers depends on the manufacturing process and can differ in sign between makers, so thermometry in fields needs characterisation. Sec. III.1 and Tables 1 and 2: negative magnetoresistance near 0.5 T that grows rapidly on cooling (about 1.7% at 0.05 K), and positive magnetoresistance of several per cent at 8 T |
| 6 | E. T. Swartz and R. O. Pohl, Thermal boundary resistance, Rev. Mod. Phys. 61, 605 (1989) | doi:10.1103/RevModPhys.61.605 | abstract | Abstract: thermal boundary resistance above 0.1 K at helium-solid and solid-solid interfaces; the helium-solid value depends strongly on the condition of the interface, and the irreproducibility of early solid-solid results is attributed to subsurface disorder and imperfect contact between the solids |
| 7 | C. P. Scheller, S. Heizmann, K. Bedner, D. Giss, M. Meschke, D. M. Zumbühl, J. D. Zimmerman and A. C. Gossard, Silver-epoxy microwave filters and thermalizers for millikelvin experiments, Appl. Phys. Lett. 104, 211106 (2014); read as preprint arXiv:1403.6205 | doi:10.1063/1.4880099 | full text | Introduction: electron temperatures in nanodevices are often well above the refrigerator base temperature because of poor thermalisation, missing high-frequency filtering and low-frequency noise including ground loops, and thermalising sample, holder and wires matters as much as filtering. Results, quantum-dot measurements (Figs. 2 and 3): the dot electron temperature follows the mixing-chamber thermometer above about 40 mK and departs from it below; at base temperature it is about 18 mK with one filter stage and about 75 mK with the filters removed. Later section on further improvement: a ceramic chip carrier prone to heat release replaced, after which metallic CBTs reached about 7.5 mK |
| 8 | S. Krinner, S. Storz, P. Kurpiers, P. Magnard, J. Heinsoo, R. Keller, J. Lütolf, C. Eichler and A. Wallraff, Engineering cryogenic setups for 100-qubit scale superconducting circuit systems, EPJ Quantum Technol. 6, 2 (2019); read as preprint arXiv:1806.07862 | doi:10.1140/epjqt/s40507-019-0072-0 | full text | Sec. 2.2.1: thermal noise from room temperature must be attenuated by about 60 dB, with attenuators at successively colder stages, each adding noise at its own thermalisation temperature, and most of the incident signal is dissipated in the attenuator. Sec. 3.1: attenuators clamped to copper plates for good thermal contact, noting that at low temperature clamping force matters more than contact area for the thermal conductance between metal parts. Secs. 2.1, 4.2 and 6: passive and active heat loads compared with the cooling power of each stage. Secs. 2.3 and 3.2: radiative load and an infrared filter ahead of the mixing-chamber attenuator |
| 9 | J. R. Prance, D. I. Bradley, R. E. George, R. P. Haley, Yu. A. Pashkin, M. Sarsby, J. Penttilä, L. Roschier, D. Gunnarsson, H. Heikkinen and M. Prunnila, Nanoelectronic thermometers optimised for sub-10 millikelvin operation, Nat. Commun. 7, 10455 (2016); read as preprint arXiv:1505.07244 | doi:10.1038/ncomms10455 | full text | Abstract and text around Fig. 4: CBT electron temperature follows the refrigerator above about 7 mK and separates from it below; cooling fins, on-chip filters and a low-noise setup needed. Thermal model (Eq. 3): bias Joule heating and parasitic heating of at least about 300 aW per island included. Text around Fig. 3(a): after brief warming during a helium refill, a sensor in vacuum took over three days to cool back, attributed to a heat leak from a warm object, while a sensor immersed in the helium mixture equilibrated with a time constant of about 570 s |
| 10 | Z. Iftikhar, A. Anthore, S. Jezouin, F. D. Parmentier, Y. Jin, A. Cavanna, A. Ouerghi, U. Gennser and F. Pierre, Primary thermometry triad at 6 mK in mesoscopic circuits, Nat. Commun. 7, 12908 (2016); read as preprint arXiv:1610.03716 | doi:10.1038/ncomms12908 | full text | Introduction: micrometre-scale circuits are hard to cool below about 10 mK because they couple strongly to the measurement lines and weakly to the substrate, so the electron temperature must be measured in situ; three primary thermometers based on different physics agree at about 6 mK. Results, electronic temperature against experimental conditions (Fig. 3), and Discussion: the electron temperature at zero added power rises with magnetic field, matching an extra dissipated power quadratic in field, attributed to eddy currents from pulse-tube vibrations |
