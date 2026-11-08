---
id: CL-ANOMALOUS-NUCLEAR-EFFECTS
name: Claims of anomalous nuclear effects in condensed matter
type: claim
field: physics/nuclear
applies_when: the paper claims excess heat beyond known chemical sources, emission of neutrons, charged particles or gamma rays, production of tritium or helium, or a change in elemental or isotopic composition, from electrolysis, gas loading, electrical discharge or other low-energy processes in solids or liquids
version: "0.1"
---

# Claims of anomalous nuclear effects in condensed matter

## 1. Complete energy accounting

**Question.** Does the paper account for every energy input and output over the whole run, including how the input power was measured and how the enthalpy carried away by gases or vapour was treated, and does it report the total energy produced and consumed, not only peak or instantaneous power?

**Why it matters.** Reported excesses are often small compared with the input power and with the correction for enthalpy leaving an open cell, so small errors in either can create or remove the whole effect. Averaging voltage and current separately misses the power in any alternating or pulsed component, and a power excess over part of a run does not show that the total energy output exceeds the total input.

**Resolved by.** Input power measured as the time average of the instantaneous product of voltage and current, with the bandwidth of the measurement stated for pulsed or noisy supplies; the open or closed condition of the cell stated and the enthalpy correction justified for it; total input and output energy integrated over the full run, including periods of loading, unloading and shutdown; the excess compared with the combined uncertainty of these terms.

**Benchmark.** [1]

## 2. Calorimeter calibration under operating conditions

**Question.** Was the calorimeter calibrated in the same configuration, over the same range of power and temperature and at intervals during the run, and does the paper show that the calibration holds while the conditions that set the heat transfer (liquid level, gas flow, stirring, temperature) change?

**Why it matters.** The quantity needed is the heat transfer coefficient that relates total power to temperature at the operating point; a coefficient obtained from small changes around another point, or one that drifts as the liquid level falls or the cell ages, gives a biased excess. Temperature sensors can acquire offsets from corrosion or electrical pickup that differ between active and reference cells. Published reports of excess heat have not always excluded systematic calorimetric errors of this kind.

**Resolved by.** Calibration with a resistive heater or a known chemical or electrical source over the full operating range, repeated during the run; a demonstration that the calibration is linear or a stated non-linear model; sensor offsets checked in place; the same calorimeter run with an otherwise identical cell in which the effect is not expected, showing a zero excess within the stated uncertainty.

**Benchmark.** [1], [2]

## 3. Chemical sources of heat

**Question.** Does the paper show that recombination of evolved gases, current efficiency below 100% and other chemical reactions in the cell cannot supply the claimed excess, and does it measure these terms instead of assuming them?

**Why it matters.** Hydrogen and oxygen that recombine inside the cell, or current spent on reactions other than gas evolution, release heat that the usual enthalpy correction counts as excess. Cells built to mimic published designs have shown apparent excess heat that disappeared once gas migration was blocked or the current efficiency was measured.

**Resolved by.** The gases leaving the cell collected and measured, or recombined and weighed, to give the current efficiency; barriers between electrodes or a closed cell with full recombination where appropriate; an estimate of the largest energy that any chemical process in the cell could release, from the amounts of reactants present, compared with the integrated excess.

**Benchmark.** [1], [2], [3]

## 4. Nuclear products in proportion to the claimed energy

**Question.** For the reaction the paper proposes, how many reactions per second does the claimed excess power imply, which products and radiation should those reactions give, and were they measured at the same time as the heat with a sensitivity that could see them?

**Why it matters.** A watt from reactions that each release a few to about 20 MeV requires of order 10^11 to 10^12 reactions per second, which would give products and secondary radiation far above detection limits. The main branches of deuterium-deuterium fusion occur at nearly equal rates, so a claim of heat without the expected neutrons, gamma rays or other products requires a change in branching by many orders of magnitude. Heat and products measured in different runs cannot show that they come from the same process.

**Resolved by.** The proposed reaction stated, with the expected rate of each product for the measured excess power; products searched for during the heat-producing runs with stated efficiency and detection limits; the measured ratio of products to excess energy compared with the expected value, with uncertainties; where the expected products are absent, a quantitative statement of how far below expectation they are.

**Benchmark.** [1]

## 5. Radiation detector artefacts and background

**Question.** How does the paper show that counts attributed to neutrons, gamma rays or charged particles are not caused by changes in background or by the detector's response to the experiment's electrical, thermal or mechanical conditions?

**Why it matters.** The cosmic-ray neutron background changes with barometric pressure and solar activity by amounts that can mimic a small excess. Some counters respond to humidity, vibration or electrical noise, and these conditions can change when a cell or discharge is switched on.

**Resolved by.** Background measured before, during and after the active periods, with pressure and other environmental variables recorded and corrected; the detector calibrated with a source in the experimental geometry; the same detector run with the apparatus powered but inactive, or with a dummy sample, to show that electrical and thermal conditions alone give no signal; pulse-shape or energy spectra shown, not only count rates; a second detector of a different type, or shielding tests, confirming the signal.

**Benchmark.** [1], [4]

## 6. Tritium and helium: initial content, enrichment and ingress

**Question.** For claims of tritium or helium production, does the paper report the initial content of every material and gas, account for enrichment or loss during the process, and show that the sealed apparatus excludes helium from the air?

**Why it matters.** Commercial heavy water contains tritium, and electrolysis concentrates it in the remaining liquid, so a rise in tritium concentration can occur with no production. Air contains helium, which enters through leaks, seals and glass walls, so helium found in gas samples or metals may come from outside. Deuterium molecules and helium-4 both have nominal mass 4 and differ by only about 0.026 atomic mass units, so a mass spectrometer that does not resolve them can count one as the other.

**Resolved by.** Initial tritium in the liquid, electrodes and gas measured, and a full tritium inventory at start and end that accounts for electrolytic enrichment and losses; helium measured in blanks taken through the same sampling and analysis, with leak rates and wall permeation estimated; a mass analysis that separates helium-4 from deuterium molecules; the amount found compared with the amount expected from the claimed energy, as in item 4.

**Benchmark.** [1], [5], [8]

## 7. New elements and isotope shifts

**Question.** For claims of transmutation or changed isotopic ratios, does the paper analyse the same materials before and after with the same method, include every possible source of the new species (electrolyte, other electrode, cell walls, gases, handling), and show that the analysis is free of isobaric and molecular interferences?

**Why it matters.** Electrodes collect deposits from the electrolyte, the counter-electrode and glass walls during a run, so species found at the surface after a run may have been deposited there. In mass spectrometry, isotopes of other elements and molecular ions can fall at the same mass as the species claimed. Isotopic compositions vary naturally between materials, so a ratio that differs from tabulated values is not by itself evidence of a nuclear change.

**Resolved by.** Elemental and isotopic analysis of all starting materials and of unused pieces from the same batches, with detection limits; depth profiles or bulk analysis distinguishing deposits from changes within the material; interferences identified and removed, for example by high mass resolution, reaction cells or measuring several isotopes; measured ratios compared with the natural range and with reference materials run in the same session.

**Benchmark.** [1], [6], [7]

## 8. State of the material

**Question.** Does the paper characterise the material in which the effect is claimed (composition, impurities, microstructure, surface condition and, where relevant, the measured hydrogen or deuterium loading) and say how each was measured?

**Why it matters.** Claims often state that the effect appears only above a threshold loading or in material with a particular preparation, but loading is often not measured, or is estimated in ways biased by surface deposits and by losses before measurement. Without this information other laboratories cannot tell whether a failure to reproduce the effect reflects a different material.

**Resolved by.** Source, purity and treatment of each material stated; composition and microstructure measured before and after; loading measured by a stated method, such as weight gain, resistance or gas volume, with handling to limit losses described and corrections for surface deposits made; the dependence of the claimed effect on these properties shown across samples.

**Benchmark.** [1]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | Energy Research Advisory Board, Cold Fusion Research: a report of the Energy Research Advisory Board to the United States Department of Energy, DOE/S-0073 (1989); read as the internet edition prepared by National Capital Area Skeptics (1999) | https://files.ncas.org/erab/ |
| 2 | J. E. Jones et al., Faradaic efficiencies less than 100% during electrolysis of water can account for reports of excess heat in cold fusion cells, J. Phys. Chem. 99, 6973 (1995) | doi:10.1021/j100018a033 |
| 3 | Z. Shkedi et al., Calorimetry, excess heat, and Faraday efficiency in Ni-H2O electrolytic cells, Fusion Technol. 28, 1720 (1995) | doi:10.13182/FST95-A30436 |
| 4 | P. Davies et al., On the variability of the barometric effect and its relation to cosmic-ray neutron sensing, Sensors 26, 925 (2026) | doi:10.3390/s26030925 |
| 5 | V. O. Altemose, Helium diffusion through glass, J. Appl. Phys. 32, 1309 (1961) | doi:10.1063/1.1736226 |
| 6 | J. Meija et al., Isotopic compositions of the elements 2013 (IUPAC Technical Report), Pure Appl. Chem. 88, 293 (2016) | doi:10.1515/pac-2015-0503 |
| 7 | S. Wilschefski and M. Baxter, Inductively coupled plasma mass spectrometry: introduction to analytical aspects, Clin. Biochem. Rev. 40, 115 (2019) | doi:10.33176/AACB-19-00024 |
| 8 | J. S. Coursey et al., Atomic Weights and Isotopic Compositions with Relative Atomic Masses, NIST Physical Measurement Laboratory, last updated (2015) | https://www.nist.gov/pml/atomic-weights-and-isotopic-compositions-relative-atomic-masses |
