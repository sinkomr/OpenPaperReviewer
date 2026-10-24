---
id: T-COMPOSITION-ANALYSIS
name: Composition and stoichiometry measurement
type: technique
field: physics/condensed-matter
applies_when: the paper states a composition, stoichiometry, oxygen content, dopant level or impurity content, or claims a sample is pure, from ICP-OES or ICP-MS, electron-probe microanalysis, Rutherford backscattering, SIMS, combustion or gas-fusion analysis, or thermogravimetry
version: "0.1"
---

# Composition and stoichiometry measurement

Composition measurements are used to claim what a sample is made of: its stoichiometry, oxygen content, dopant concentration and the level of unwanted impurities. The common methods are inductively coupled plasma optical emission and mass spectrometry (ICP-OES, ICP-MS), electron-probe microanalysis with wavelength-dispersive spectrometry (EPMA-WDS), Rutherford backscattering spectrometry (RBS), secondary ion mass spectrometry (SIMS), combustion and inert-gas fusion analysis, and thermogravimetric analysis (TGA).

## 1. Measured or nominal composition

**Question.** Is each composition, dopant level or oxygen content that a claim relies on measured on the samples whose properties are reported, after the final processing step, or is it taken from the starting amounts or from structural assumptions?

**Why it matters.** Volatile components can evaporate during synthesis and annealing, reactions can be incomplete, and oxides can take up or lose oxygen, so the composition of the final sample can differ from the weighed-in or formula composition. Where a property depends on carrier count or valence, that difference changes the interpretation.

**Resolved by.** Compositions labelled as measured or nominal throughout; measured values, with uncertainties, for the batch or the individual samples whose properties are reported, taken after the last heat treatment; where measured and nominal values differ, the measured value used in the analysis and the difference discussed.

**Benchmark.** [13]

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

**Benchmark.** [5], [7], [12]

## 7. Detection limits for dopants and impurities

**Question.** Where a claim rests on a low dopant level, or on an impurity being absent or below some level, does the paper give the detection limit of the whole procedure for that element in that matrix, and report the measured value rather than only "not detected"?

**Why it matters.** An instrument detection limit measured on a clean solution omits the blank and variability added by sample preparation, so the detection limit of the whole procedure is higher. Detection limits depend on the element, matrix, dilution and reagent purity, and unresolved interferences can produce an apparent signal at the trace level.

**Resolved by.** A detection limit and a quantification limit estimated from blanks or low-level samples taken through the full procedure; the measured value with its uncertainty, or the stated limit, for every element relevant to the claim, including those reported as absent; a check that the trace signal is free from interferences.

**Benchmark.** [1], [2], [4]

## 8. Inputs to ion-beam quantification

**Question.** For RBS, does the paper state the stopping powers, detector energy calibration, beam geometry and fitting code used, report the result as areal density with the density assumed for any thickness, and show that channelling and the limits of RBS for some elements were handled?

**Why it matters.** RBS can be accurate without sample-matched standards, but its accuracy is dominated by the stopping powers and by the detector gain, and the scattering angle and pile-up add further terms. The measured quantity is atoms per unit area, which becomes a thickness only through an assumed density. Channelling in crystalline samples changes the yield, and RBS alone has well-known limits for some elements and depth profiles that other ion-beam methods can remove.

**Resolved by.** An uncertainty budget that includes stopping power and gain calibration; the spectrum shown with its fit; areal densities given and any density used for conversion stated; the sample tilted, rotated or otherwise oriented to avoid channelling, or the effect shown to be small; complementary ion-beam methods such as nuclear reaction analysis or elastic recoil detection used where RBS cannot resolve an element.

**Benchmark.** [11], [12]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | S. C. Wilschefski and M. R. Baxter, Inductively coupled plasma mass spectrometry: introduction to analytical aspects, Clin. Biochem. Rev. 40, 115–133 (2019) | doi:10.33176/AACB-19-00024 | full text | Section on spectral interferences: isobaric, doubly charged and polyatomic ions from matrix, reagents and argon, and their removal by isotope choice, correction equations checked with interference solutions, cool plasma, high resolution and collision or reaction cells. Section on non-spectroscopic interferences: transport and plasma effects and space charge, internal standards of similar mass and ionisation potential, matrix-matched calibration and standard additions. Detection limits depend on element, matrix, dilution and reagent purity |
| 2 | US Environmental Protection Agency, Method 200.7: Determination of metals and trace elements in water and wastes by inductively coupled plasma-atomic emission spectrometry, revision 4.4 (1994) | https://www.epa.gov/sites/default/files/2015-08/documents/method_200-7_rev_4-4_1994.pdf | full text | Sec. 4.1: spectral interferences from background, stray light from abundant elements, line overlap and molecular bands; uncorrected overlaps give false positives; inter-element corrections verified with interference check solutions, and corrections forming a major part of the signal may be inaccurate. Sec. 4.2: physical interferences from high dissolved solids and acid |
| 3 | US Environmental Protection Agency, Method 3052: Microwave assisted acid digestion of siliceous and organically based matrices, revision 0 (1996) | https://www.epa.gov/sites/default/files/2015-12/documents/3052.pdf | full text | Sec. 1.3 and 3.2: total decomposition is the goal, but refractory oxides such as titania and alumina may not dissolve and can sequester analytes. Sec. 3.1: venting can lose sample and analytes. Sec. 5.1: reagent purity sets the blank. Sec. 8: blanks, duplicates, spikes and reference materials with each batch |
| 4 | B. Magnusson and U. Örnemark (eds.), Eurachem Guide: The fitness for purpose of analytical methods, a laboratory guide to method validation and related topics, 2nd edn (2014), ISBN 978-91-87461-59-0 | https://www.eurachem.org/images/stories/Guides/pdf/MV_guide_2nd_ed_EN.pdf | full text | Sec. 5.4.1: reagent blanks, and a footnote defining a procedural blank as one taken through the entire procedure. Sec. 5.4.3: spiked analyte is less closely bound than native analyte, so spike-based bias estimates are over-optimistic. Sec. 6.1.2: proportional and translational interferences, with standard additions correcting only the proportional kind. Sec. 6.2.1: instrument versus method detection limit, the latter from samples taken through the whole measurement procedure. Sec. 6.2.2 to 6.2.4: detection and quantification limits from the standard deviation of replicate results at low levels. Sec. 6.5.2: matrix-matched certified reference materials for bias |
| 5 | D. E. Newbury and N. W. M. Ritchie, Performing elemental microanalysis with high accuracy and high precision by scanning electron microscopy/silicon drift detector energy-dispersive X-ray spectrometry (SEM/SDD-EDS), J. Mater. Sci. 50, 493–518 (2015); read as PMC4555346 | doi:10.1007/s10853-014-8685-2 | full text | Introduction, on EPMA-WDS origins: the k-ratio method against standards measured under identical conditions. "Typical SEM/EDS microanalysis practice", on standardless analysis: a much wider error distribution than standards-based analysis; normalisation loses the information in the analytical total, and a low total can reveal an unmeasured element such as oxygen. "Specimen geometry effects": departures from a flat surface distort intensities and the total. "The steps to successful quantitative SEM/SDD-EDS X-ray microanalysis": highly polished specimens and standards homogeneous on a micrometre scale. "Quantitative X-ray microanalysis of low atomic number elements": direct measurement of C, N, O and F |
| 6 | D. S. Simons, Summary of ISO/TC 201 standard XIII, ISO 18114:2003, Surface chemical analysis, secondary ion mass spectrometry, determination of relative sensitivity factors from ion-implanted reference materials, Surf. Interface Anal. 38, 171–172 (2006) | doi:10.1002/sia.2316 | abstract | Abstract: the standard gives a method for determining SIMS relative sensitivity factors from ion-implanted reference materials, applicable to specimens with a uniform matrix composition in which the implanted species peaks at no more than one atomic percent |
| 7 | J. Goodge, Electron probe micro-analyzer (EPMA), Geochemical Instrumentation and Analysis, Science Education Resource Center, Carleton College (2007) | https://serc.carleton.edu/research_education/geochemsheets/techniques/EPMA.html | full text | "Strengths and Limitations": spots of one to two micrometres on individual phases, resolving zoning within grains; no detection of H, He or Li; ferrous and ferric iron cannot be distinguished; results reported as oxides and recalculated with stoichiometric rules. "Data Collection, Results and Presentation": standards and matrix corrections. "User's Guide": flat polished, coated samples |
| 8 | M. Karppinen, M. Matvejeff, K. Salomäki and H. Yamauchi, Oxygen content analysis of functional perovskite-derived cobalt oxides, J. Mater. Chem. 12, 1761–1764 (2002) | doi:10.1039/B200770N | abstract | Abstract: compares redox methods for oxygen content; three titration methods agree with good reproducibility, and thermogravimetric hydrogen reduction agrees with them but scatters more |
| 9 | N. Saadatkhah, A. Carrillo García, S. L. G. Ackermann, P. Leclerc, M. Latifi, S. Samih, G. S. Patience and J. Chaouki, Experimental methods in chemical engineering: thermogravimetric analysis, TGA, Can. J. Chem. Eng. 98, 34–43 (2020) | doi:10.1002/cjce.23673 | abstract | Abstract: mass falls through decomposition, evaporation of volatiles or reduction, and can rise in reactive atmospheres; TGA cannot see reactions without mass change; evolved gas analysis monitors the gaseous products leaving the furnace during the temperature ramp |
| 10 | O. Menis and J. T. Sterling, Standard reference materials: determination of oxygen in ferrous materials, SRM 1090, 1091 and 1092, NBS Miscellaneous Publication 260-14 (1966) | doi:10.6028/NBS.SP.260-14 | full text | Discussion of sample preparation and Table 1: preparing surfaces with an abrasive wheel and grinder gave higher oxygen results through surface contamination, so samples were filed by hand, degreased and analysed within an hour; surface-to-weight ratio kept small; certificate caution that samples be thoroughly and freshly cleaned |
| 11 | C. Jeynes, N. P. Barradas and E. Szilágyi, Accurate determination of quantity of material in thin films by Rutherford backscattering spectrometry, Anal. Chem. 84, 6061–6069 (2012); read as the submitted manuscript hosted by the University of Surrey | doi:10.1021/ac300904c | full text | Abstract: accuracy dominated by electronic stopping power, with the detector's electronic gain also needing special care. Introduction: uncertainty budgets still not widely used in ion-beam analysis. "Traceability of RBS: fundamental equations": results in thin-film units of atoms per area, equivalent to thickness only through the density; the implanted sample amorphised to exclude channelling. "Traceability of RBS: uncertainty budget": scattering angle, gain and pulse pile-up terms. "IBA Methods and Perspectives": nuclear reaction analysis for C, N and O, and elastic recoil detection for hydrogen |
| 12 | C. Jeynes and J. L. Colaux, Thin film depth profiling by ion beam analysis, Analyst 141, 5944–5985 (2016) | doi:10.1039/c6an01167e | abstract | Abstract: RBS profiles the first fraction of a micrometre non-destructively and can be a traceable reference method; RBS alone has well-known severe limits that combining it with other ion-beam methods (EBS, ERD, NRA, PIXE) largely overcomes |
| 13 | Y. Morita, K. Sakai, I. Asako, T. Konno, T. Motohashi, S. Sugihara, T. Fujii, I. Terasaki, H. Yamauchi and M. Karppinen, Thermoelectric misfit-layered cobalt oxides (1): oxygen nonstoichiometry and cobalt valence, Trans. Mater. Res. Soc. Jpn. 29, 2749–2752 (2004) | https://www.mrs-j.org/pub/tmrsj/vol29_no6/vol29_no6_2749.pdf | full text | Abstract and Sec. 2: valences measured by two titration methods are clearly lower than those assigned from nominal or structural considerations; synthesis adapted to limit sodium evaporation; oxygen content changes with annealing atmosphere |
