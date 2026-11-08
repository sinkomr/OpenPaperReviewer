---
id: T-VACUUM-SURFACES
name: Vacuum, surface preparation and contamination
type: technique
field: physics/methods
applies_when: the result depends on a clean surface or a controlled gas environment: measurements in high or ultra-high vacuum, surfaces prepared by sputtering, annealing or cleaving, gas dosing, air exposure or transfer between instruments, or a claim that a surface is free of contamination
version: "0.1"
---

# Vacuum, surface preparation and contamination

## 1. Base pressure and pressure during the measurement

**Question.** Does the paper give both the base pressure and the pressure while the data were taken (with heaters, sources, beams and cooling running), and say which gauge gave each reading, where it sits relative to the sample, and whether the value is a nitrogen-equivalent reading or corrected for the gas present?

**Why it matters.** A base pressure reached after a long pump-down with everything switched off can rise when the sample, sources or evaporators are heated, because heating drives gas off the walls and the gauge itself gives off gas and heat. Ionisation gauges are not perfectly stable and their readings depend strongly on the gas species, so an uncorrected reading is a nitrogen-equivalent value, not the true pressure of the gas present.

**Resolved by.** Base and operating pressures reported separately for each data set; the gauge type and its position stated; readings identified as nitrogen-equivalent or corrected with a stated gas factor; the pressure logged during heating, deposition or beam exposure, not only before.

**Benchmark.** [1], [4]

## 2. Composition of the residual gas

**Question.** Is the composition of the residual gas known, for example from a residual gas analyser (RGA) spectrum taken under the measurement conditions, including the partial pressures of the species the surface reacts with, and is the analyser's calibration stated or its readings treated as qualitative?

**Why it matters.** The total pressure does not say which gases reach the surface. Water is present in almost all vacuum systems, hydrogen is usually the main gas left at ultra-high vacuum base pressures, and reactive gases such as oxygen, carbon monoxide and methane can be present at low levels. The partial pressures indicated by a quadrupole mass spectrometer depend on the instrument settings, the total pressure and the gas mixture, and its sensitivity drifts, so uncalibrated readings give composition only roughly.

**Resolved by.** An RGA spectrum, or the partial pressures of the relevant reactive species, recorded under the measurement conditions; a check that there is no air leak; the analyser's calibration and its date stated where partial pressures are quoted as numbers, or the readings described as relative.

**Benchmark.** [1], [2], [3]

## 3. Bake-out and outgassing

**Question.** Was the chamber baked, and were the sample, sample holder and sources degassed, with the temperatures and durations given, and does the paper consider gas given off by the sample and by materials near it during the measurement?

**Why it matters.** The outgassing rate of a chamber depends on its material and heat treatment and can differ by a factor of a hundred or more between chambers of the same shape. Outgassing rates measured by different laboratories and methods are comparable only when the method, conditions and reporting are the same, so a stated rate or a statement that outgassing is negligible means little without them.

**Resolved by.** Bake temperature and duration, and the pressure reached afterwards; degassing of the sample, holder and sources described; materials near the sample named, with any adhesives or polymers justified; where an outgassing rate supports a claim, the method, temperature, time after pump-down and reporting basis (per unit area or mass, nitrogen-equivalent or by species) given.

**Benchmark.** [1], [2], [4]

## 4. Preparation recipe and how cleanliness was checked

**Question.** Is the preparation recipe given in full (ion species, energy and dose for sputtering; annealing or flashing temperatures, durations and how the temperature was measured; cleaving conditions), and was the cleanliness of the prepared surface checked by a surface-sensitive method, with the detection limit of that check stated?

**Why it matters.** Heating drives impurities dissolved in the bulk to the surface, and sputtering removes them but roughens the surface, so the final anneal can bring impurities back. A diffraction pattern averaged over a large area can look as expected while parts of the surface carry impurity phases, and spectroscopic checks have detection limits, often near 0.1 atomic per cent but varying by up to a factor of a hundred between elements. A statement that a surface is clean therefore means clean to the limit of the check used.

**Resolved by.** The full recipe, with the temperature calibration; spectra of the prepared surface showing the contaminant signals of concern below a stated limit; an area-averaging method combined with a local probe where local contamination matters; the fraction of clean surface estimated where it is incomplete; the recipe shown to give the same surface on repeated preparation.

**Benchmark.** [5], [6]

## 5. Air exposure, handling and transfer

**Question.** Was the sample exposed to air, solvents or a glove-box atmosphere between preparation and measurement, or between instruments, and does the paper state for how long and measure what that exposure did to the surface?

**Why it matters.** Adventitious carbon, a hydrocarbon layer, forms on almost every surface exposed to air, and its amount keeps rising with exposure time from minutes to months. Reactive surfaces oxidise within minutes in air, and transfer or storage at about 10⁻⁶ mbar can still be above the partial pressure at which surface reactions such as oxidation set in. Surface-analysis standards therefore ask that the handling and storage of a specimen are recorded and reported.

**Resolved by.** The atmosphere, duration and containers for every step between preparation and measurement reported; transfer under UHV or inert gas where the surface is reactive, with the pressure during transfer; a surface-sensitive check before and after transfer, or a comparison with a surface prepared in situ; any cleaning after air exposure described and its effect on the surface shown.

**Benchmark.** [6], [7], [8], [9]

## 6. Ageing of the surface in vacuum

**Question.** How long after preparation was each data set taken, at what pressure and sample temperature, and does the paper show that the measured property did not change over that time?

**Why it matters.** A surface keeps adsorbing residual gas in vacuum, and storage under vacuum alone does not prevent oxidation of reactive materials. Some adsorbates, such as hydrogen, are hard to detect and may show only under particular measurement conditions, so a surface that looks unchanged can still have changed.

**Resolved by.** The time since preparation recorded for each data set; repeated measurements over time, or on a freshly prepared surface, giving the same result; the key result taken soon after preparation; where adsorption matters, a test in which a known amount of the relevant gas is dosed on purpose and its effect measured.

**Benchmark.** [5], [8]

## 7. Contamination and damage caused by the measurement

**Question.** Could the probe (an electron, X-ray or ion beam, or a hot filament nearby) have deposited carbon, desorbed species or changed the surface chemistry, and does the paper test this, for example by repeating the measurement as the dose builds up or on a fresh area?

**Why it matters.** Under an electron beam, mobile hydrocarbon molecules from preparation, storage or the residual gas diffuse into the irradiated area and are polymerised into a carbon-rich deposit that can cover the structure of interest and degrade spectra. X-ray, electron and ion exposure can also destroy the chemical-state information a measurement seeks.

**Resolved by.** Spectra or images taken in sequence showing no change with dose, or a dose limit stated; comparison of irradiated and fresh areas; mitigation such as cleaning, baking, beam showering or cooling described, with its effect checked.

**Benchmark.** [6], [10]

## 8. Controlled gas exposure

**Question.** Where a claim rests on a gas exposure (a dose in langmuirs, a partial pressure or a reaction environment), how was the exposure determined: which gauge and gas correction were used, was the purity of the admitted gas checked, and is the result shown as a function of exposure?

**Why it matters.** Ionisation gauge sensitivity depends on the gas, so an exposure computed from an uncorrected reading is wrong by the gauge's relative sensitivity for that gas. Many gases stick to chamber walls and are released slowly, and mass-spectrometer readings of the dosed gas depend on the instrument settings and the gas mixture, so the gas reaching the sample may differ in amount and purity from what was admitted.

**Resolved by.** The gauge, its gas correction factor and the pressure-time record used to compute each exposure; the gas purity and any impurities checked with an RGA during dosing; the effect shown over a range of exposures, with a background measurement without dosing.

**Benchmark.** [1], [3]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | D. S. Barker et al., Roadmap on quantum sensors for vacuum metrology, preprint arXiv:2609.06626 (2026); read as the arXiv HTML version | doi:10.48550/arXiv.2609.06626 |
| 2 | J. A. Fedchak et al., Outgassing rate comparison of seven geometrically similar vacuum chambers of different materials and heat treatments, J. Vac. Sci. Technol. B 39, 024201 (2021); read as preprint arXiv:2009.10560 | doi:10.1116/6.0000657 |
| 3 | ISO/TS 20175:2018, Vacuum technology — Vacuum gauges — Characterization of quadrupole mass spectrometers for partial pressure measurement (International Organization for Standardization, 2018); scope read in the Institute for Standardization of Serbia catalogue entry | https://www.iso.org/standard/67207.html |
| 4 | ISO/TS 20177:2018, Vacuum technology — Vacuum gauges — Procedures to measure and report outgassing rates (International Organization for Standardization, 2018); scope read in the SNV and SIS catalogue entries | https://www.iso.org/standard/67208.html |
| 5 | A. B. Odobesko et al., On the preparation and electronic properties of clean superconducting Nb(110) surfaces, Phys. Rev. B 99, 115437 (2019); read as preprint arXiv:1906.07796 | doi:10.1103/PhysRevB.99.115437 |
| 6 | D. R. Baer et al., Practical guides for X-ray photoelectron spectroscopy: first steps in planning, conducting and reporting XPS measurements, J. Vac. Sci. Technol. A 37, 031401 (2019); read in PubMed Central (PMC6774202) | doi:10.1116/1.5065501 |
| 7 | G. Greczynski and L. Hultman, C 1s peak of adventitious carbon aligns to the vacuum level: dire consequences for material's bonding assignment by photoelectron spectroscopy, ChemPhysChem 18, 1507 (2017); read in PubMed Central (PMC5484993) | doi:10.1002/cphc.201700126 |
| 8 | L. T. Stephenson et al., The Laplace Project: an integrated suite for preparing and transferring atom probe samples under cryogenic and UHV conditions, PLoS One 13, e0209211 (2018); read on the journal's article page | doi:10.1371/journal.pone.0209211 |
| 9 | ISO 20579-1:2024, Surface chemical analysis — Sample handling, preparation and mounting — Part 1: Documenting and reporting the handling of specimens prior to analysis (International Organization for Standardization, 2024); scope read in the Normservis catalogue entry | https://www.iso.org/standard/83685.html |
| 10 | M. Hugenschmidt et al., Electron-beam-induced carbon contamination in STEM-in-SEM: quantification and mitigation, Microsc. Microanal. 29, 219 (2023) | doi:10.1093/micmic/ozac003 |
