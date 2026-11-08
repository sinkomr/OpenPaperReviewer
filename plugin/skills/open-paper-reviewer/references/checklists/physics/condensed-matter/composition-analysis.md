---
id: T-COMPOSITION-ANALYSIS
name: Composition and stoichiometry measurement
type: technique
field: physics/condensed-matter
applies_when: the paper states a composition, stoichiometry, oxygen content, dopant level or impurity content, or claims a sample is pure, from ICP-OES or ICP-MS, electron-probe microanalysis, Rutherford backscattering, SIMS, combustion or gas-fusion analysis, or thermogravimetry
version: "0.1"
---

# Composition and stoichiometry measurement

## 1. Measured or nominal composition

**Question.** Is each composition, dopant level or oxygen content that a claim relies on measured on the samples whose properties are reported, after the final processing step, or is it taken from the starting amounts or from structural assumptions?

**Why it matters.** Volatile components can evaporate during synthesis and annealing, reactions can be incomplete, and oxides can take up or lose oxygen, so the composition of the final sample can differ from the weighed-in or formula composition. Where a property depends on carrier count or valence, that difference changes the interpretation.

**Resolved by.** Compositions labelled as measured or nominal throughout; measured values, with uncertainties, for the batch or the individual samples whose properties are reported, taken after the last heat treatment; where measured and nominal values differ, the measured value used in the analysis and the difference discussed.

**Benchmark.** [12]

## 2. Dissolution and preparation for solution methods

**Question.** For ICP-OES or ICP-MS, does the paper state how the solid was brought into solution, show that it dissolved completely, and report procedural blanks and a check against a certified reference material or spike recovery?

**Why it matters.** Refractory phases such as titania, alumina and other oxides may not dissolve in the chosen acids and can retain some of the elements being measured, so the solution no longer represents the solid. Pressurised digestion can vent and lose volatile analytes, and reagents, vessels and handling add contamination that sets the blank. A spike added to a solution is less tightly bound than the native element, so spike recovery alone tends to look better than the true recovery.

**Resolved by.** The digestion route, reagents, temperature and vessel type stated; a statement that no residue remained, or the residue analysed separately; procedural blanks taken through every step and subtracted, with their values given; a certified reference material of similar matrix, or an independent method, giving the expected result.

**Benchmark.** [3], [4]

## 3. Spectral interferences in plasma methods

**Question.** Does the paper name the emission line or isotope used for each element, and say how overlaps from other elements, polyatomic ions and doubly charged ions were identified and removed?

**Why it matters.** In ICP-MS, isobars, doubly charged ions and polyatomic ions formed from the plasma gas, the acids and the sample matrix can sit at the mass of the analyte; in ICP-OES, line overlaps, stray light from abundant elements and molecular bands do the same at the chosen wavelength. Uncorrected, they are reported as analyte, which gives false positives for trace dopants and impurities. A correction that makes up a large part of the signal is itself unreliable.

**Resolved by.** The isotope or line for each element stated, with the interferences that apply to it in the sample matrix; the removal method stated (alternative isotope or line, collision or reaction cell, high resolution, or a correction equation) and checked with an interference check solution of the matrix elements; for trace elements next to a major element, a second isotope or line giving the same result.

**Benchmark.** [1], [2]

## 4. Standards and matrix effects

**Question.** Against what standards was each technique calibrated, how closely do they match the sample, and how were matrix effects corrected: internal standards or matched calibration for ICP, measured standards for EPMA, and relative sensitivity factors from a standard of the same matrix for SIMS?

**Why it matters.** In ICP, dissolved solids and easily ionised elements change the signal through sample transport, plasma conditions and space charge, and standard additions correct only effects proportional to the signal. In electron-probe analysis, standardless quantification has much larger errors than quantification against standards measured under the same conditions. In SIMS, relative sensitivity factors are derived from ion-implanted standards, and the standard method for this applies only to a uniform matrix with the implanted element at no more than about one atomic percent, so a factor cannot be assumed to hold in a layer or phase of different composition or at higher concentration.

**Resolved by.** The standards named, with their composition and how they were measured; for ICP, an internal standard of similar mass and ionisation potential or matrix-matched calibration, with internal-standard recoveries reported; for EPMA, standards measured in the same session and the matrix-correction procedure named; for SIMS, the sensitivity factor's source and matrix stated, and no single factor applied across layers or phases of different composition.

**Benchmark.** [1], [4], [5], [6]

## 5. Light elements, oxygen and the analytical total

**Question.** For elements the main technique cannot measure well, such as oxygen, hydrogen, lithium, carbon or nitrogen, does the paper measure them by a suitable method, and for EPMA does it report the unnormalised analytical total and say whether oxygen was measured or assigned by stoichiometry?

**Why it matters.** EPMA cannot detect hydrogen or lithium and, in routine analysis, cannot tell the oxidation states of an element such as iron apart, so oxide formulae are often completed by assumed stoichiometry. Normalising a result to 100% hides a low total, which is the sign of an unmeasured element or a specimen problem. Oxygen content from thermogravimetry depends on assigning the mass change to one reaction, while mass also changes through evaporation and other reactions, and reduction measurements scatter more than redox titration. In gas-fusion analysis, oxygen picked up on a freshly ground surface raises the result.

**Resolved by.** The analytical total given before any normalisation, close to 100%; oxygen, hydrogen or other light elements measured directly, for example by redox titration, thermogravimetric reduction cross-checked against titration, or gas-fusion analysis of freshly and gently cleaned samples; for thermogravimetry, the atmosphere, final product and its identification stated, and evolved gases analysed where several reactions are possible; oxidation states that enter a formula measured, not assumed.

**Benchmark.** [5], [7], [8], [9], [10]

## 6. Sampled volume and phase specificity

**Question.** Does the paper say what volume each measurement samples, whether that is the phase or region the claim is about, and whether results from different points or depths agree?

**Why it matters.** Electron-probe analysis samples a spot of about one to two micrometres and reveals zoning within grains; ion-beam methods profile the first fraction of a micrometre; solution methods average the whole sample, including any secondary phases, surface layers and inclusions. A bulk average can therefore misstate the composition of the phase that carries a property, and a single spot can misstate the bulk. Surface roughness and topography distort electron-probe intensities.

**Resolved by.** The sampled volume or depth stated for each method; several spots, grains or depths measured, with the spread reported; phase-resolved analysis compared with bulk analysis where secondary phases are present; electron-probe specimens flat and polished, with standards homogeneous at the micrometre scale.

**Benchmark.** [5], [7], [11]

## 7. Detection limits for dopants and impurities

**Question.** Where a claim rests on a low dopant level, or on an impurity being absent or below some level, does the paper give the detection limit of the whole procedure for that element in that matrix, and report the measured value rather than only "not detected"?

**Why it matters.** An instrument detection limit measured on a clean solution omits the blank and variability added by sample preparation, so the detection limit of the whole procedure is higher. Detection limits depend on the element, matrix, dilution and reagent purity, and unresolved interferences can produce an apparent signal at the trace level.

**Resolved by.** A detection limit and a quantification limit estimated from blanks or low-level samples taken through the full procedure; the measured value with its uncertainty, or the stated limit, for every element relevant to the claim, including those reported as absent; a check that the trace signal is free from interferences.

**Benchmark.** [1], [2], [4]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | S. C. Wilschefski and M. R. Baxter, Inductively coupled plasma mass spectrometry: introduction to analytical aspects, Clin. Biochem. Rev. 40, 115 (2019) | doi:10.33176/AACB-19-00024 |
| 2 | US Environmental Protection Agency, Method 200.7: Determination of metals and trace elements in water and wastes by inductively coupled plasma-atomic emission spectrometry, revision 4.4 (1994) | https://www.epa.gov/sites/default/files/2015-08/documents/method_200-7_rev_4-4_1994.pdf |
| 3 | US Environmental Protection Agency, Method 3052: Microwave assisted acid digestion of siliceous and organically based matrices, revision 0 (1996) | https://www.epa.gov/sites/default/files/2015-12/documents/3052.pdf |
| 4 | B. Magnusson and U. Örnemark (eds.), Eurachem Guide: The fitness for purpose of analytical methods, a laboratory guide to method validation and related topics, 2nd edn (2014), ISBN 978-91-87461-59-0 | https://www.eurachem.org/images/stories/Guides/pdf/MV_guide_2nd_ed_EN.pdf |
| 5 | D. E. Newbury and N. W. M. Ritchie, Performing elemental microanalysis with high accuracy and high precision by scanning electron microscopy/silicon drift detector energy-dispersive X-ray spectrometry (SEM/SDD-EDS), J. Mater. Sci. 50, 493 (2015); read as PMC4555346 | doi:10.1007/s10853-014-8685-2 |
| 6 | D. S. Simons, Summary of ISO/TC 201 standard XIII, ISO 18114:2003, Surface chemical analysis, secondary ion mass spectrometry, determination of relative sensitivity factors from ion-implanted reference materials, Surf. Interface Anal. 38, 171 (2006) | doi:10.1002/sia.2316 |
| 7 | J. Goodge, Electron probe micro-analyzer (EPMA), Geochemical Instrumentation and Analysis, Science Education Resource Center, Carleton College (2007) | https://serc.carleton.edu/research_education/geochemsheets/techniques/EPMA.html |
| 8 | M. Karppinen et al., Oxygen content analysis of functional perovskite-derived cobalt oxides, J. Mater. Chem. 12, 1761 (2002) | doi:10.1039/B200770N |
| 9 | N. Saadatkhah et al., Experimental methods in chemical engineering: thermogravimetric analysis, TGA, Can. J. Chem. Eng. 98, 34 (2020) | doi:10.1002/cjce.23673 |
| 10 | O. Menis and J. T. Sterling, Standard reference materials: determination of oxygen in ferrous materials, SRM 1090, 1091 and 1092, NBS Miscellaneous Publication 260-14 (1966) | doi:10.6028/NBS.SP.260-14 |
| 11 | C. Jeynes and J. L. Colaux, Thin film depth profiling by ion beam analysis, Analyst 141, 5944 (2016) | doi:10.1039/c6an01167e |
| 12 | Y. Morita et al., Thermoelectric misfit-layered cobalt oxides (1): oxygen nonstoichiometry and cobalt valence, Trans. Mater. Res. Soc. Jpn. 29, 2749 (2004) | https://www.mrs-j.org/pub/tmrsj/vol29_no6/vol29_no6_2749.pdf |
