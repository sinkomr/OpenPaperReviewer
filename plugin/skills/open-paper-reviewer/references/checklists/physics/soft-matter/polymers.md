---
id: T-POLYMERS
name: Polymer experiments
type: technique
field: physics/soft-matter
applies_when: the paper reports experiments on polymer solutions, melts, networks or gels, quotes molar mass, dispersity, a concentration regime, solvent quality, a degree of crystallinity or a gel point, or assigns a scaling exponent to polymer data
version: "0.1"
---

# Polymer experiments

## 1. Molar mass and dispersity

**Question.** Which method gave the number- and weight-average molar masses and the dispersity, and for SEC, were they obtained from a calibration with standards of a different chemistry or architecture, or from absolute detection such as light scattering, with the refractive index increment stated?

**Why it matters.** SEC separates by hydrodynamic volume, not molar mass, so a calibration with linear standards of another polymer gives apparent values, and for branched polymers these can be wrong by a large and non-systematic amount. Light-scattering detection avoids the column calibration but depends on the refractive index increment and the concentration detector, and the number and z averages are less reliable than the weight average because they depend on the ends of the chromatogram, where the detector signal is weak.

**Resolved by.** The method, eluent, columns, standards and detectors stated; values labelled as relative (for example polystyrene-equivalent) or absolute; the refractive index increment and its source given for light scattering; the full distribution shown, not only averages; for branched or unusual polymers, the molar mass confirmed by a second, independent method.

**Benchmark.** [1], [2]

## 2. Degradation during preparation and measurement

**Question.** Does the paper show that the polymer measured is the polymer characterised, by checking molar mass or a proxy for it after dissolution, processing and the experiment itself, and does it state the conditions (heating, sonication, shear, strong flow, atmosphere) that could break chains?

**Why it matters.** Heat, sonication and extreme pH used to dissolve a polymer can cut chains, very long chains can be broken by shear in the SEC columns or injector, and strong or turbulent flows stretch chains until they break, leaving shorter fragments with different properties. In melts, time at high temperature causes chain scission, and shear speeds it up, so a property measured at the end of a run may belong to a different material.

**Resolved by.** Molar mass measured before and after the step most likely to degrade the sample, or after the experiment; dissolution conditions stated and shown to dissolve the sample fully without loss of molar mass; for melts, a time sweep at the measurement temperature showing a stable response, with the atmosphere stated; for flow experiments, a check that the response does not drift with repeated passes or time under flow.

**Benchmark.** [1], [3], [4]

## 3. Concentration regime

**Question.** Is each concentration placed relative to the overlap concentration, with c* determined by a stated method for the same polymer, solvent and temperature, and is the claimed regime (dilute, semidilute, entangled) supported for the type of flow or measurement used?

**Why it matters.** Many properties depend on the ratio of concentration to c*, not on concentration alone, and c* itself depends on molar mass and solvent quality. A solution that is dilute at rest need not behave as dilute in a strong flow: in extensional flow the relaxation time can depend on concentration at a small fraction of c*, because stretched chains overlap.

**Resolved by.** c* and, where relevant, the entanglement concentration stated with the definition and data used to obtain them; concentrations reported as c/c* as well as in mass units; for claims of dilute behaviour in flow, data over a range of concentrations showing that the measured property no longer changes with concentration.

**Benchmark.** [5], [6]

## 4. Solvent quality and temperature

**Question.** Does the paper establish the solvent quality for the polymer at the measurement temperature, for example from light-scattering measurements of chain size against temperature or a cited theta temperature, and does it report how far the temperature is from theta?

**Why it matters.** Chain size and its dependence on molar mass change from random-walk to self-avoiding statistics as solvent quality improves, and the crossover is controlled by a parameter that combines the distance from the theta temperature with chain length. At intermediate solvent quality, properties follow effective exponents between the theta and good-solvent limits, so the same polymer can give different exponents at different temperatures or molar masses.

**Resolved by.** The solvent quality measured for the system studied, or taken from a cited source for the same polymer, solvent and temperature range; the temperature controlled and reported; where solvent quality changes with temperature or composition, results compared at a stated value of the solvent-quality parameter.

**Benchmark.** [5], [6]

## 5. Assignment of scaling exponents

**Question.** When a scaling exponent is assigned to a dependence on molar mass or concentration, over what range of the variable was it fitted, is the data range inside a single regime, which molar-mass average was used, and is the value compared with the effective exponent expected for the solvent quality and chain length, not only with the asymptotic value?

**Why it matters.** Asymptotic exponents apply only to long chains far from crossovers, and finite chains at intermediate solvent quality or near a regime boundary give effective exponents that differ from them. Measured exponents in polymer solutions can also depend on solvent quality and on the type of flow, so an exponent from a narrow range, or one that spans a crossover, can be matched to the wrong theory.

**Resolved by.** The fitted range stated in decades of molar mass or concentration, with the regime boundaries marked on the plot; the molar-mass average and the dispersity of each sample given; the exponent quoted with its fitting range and compared with predictions that account for solvent quality and finite chain length; data collapse against the scaling variables shown where the claim is universal behaviour.

**Benchmark.** [2], [5], [6]

## 6. Degree of crystallinity

**Question.** How was the degree of crystallinity obtained: which reference enthalpy of fusion for the fully crystalline polymer was used and from where, how were cold crystallisation and recrystallisation during heating handled, and was the DSC value checked against X-ray diffraction or density?

**Why it matters.** DSC does not give the enthalpy of fusion of a fully crystalline polymer, which must come from an external calibration, and published reference values for a single polymer can differ by a factor of several. During heating the sample can recrystallise while it melts, so the area under the melting peak need not reflect the crystallinity at the start of the scan, and crystallinity itself depends strongly on cooling rate and thermal history.

**Resolved by.** The reference enthalpy and its source stated; integration limits and baseline given; exothermic events during heating subtracted or explained; the thermal history of the sample stated; agreement with an independent method such as X-ray diffraction or density shown, or the method dependence acknowledged when values are compared between studies.

**Benchmark.** [7], [8]

## 7. Gel point

**Question.** When a gel point or gelation time is reported, which rheological criterion located it (crossover of the storage and loss moduli at one frequency, a loss tangent independent of frequency, a peak in the loss tangent, divergence of a relaxation time), at which frequencies and strain amplitude was it measured, and could a physical network, for example of filler, mask the signature?

**Why it matters.** The criteria in common use need not give the same gel point, so a gelation time from a single-frequency crossover can differ from the point at which the loss tangent becomes independent of frequency. A physical network of filler or other components can hide the usual signatures of the chemical gel point, and many gelling systems have a narrow linear viscoelastic range, so large strains can disturb the network being measured.

**Resolved by.** The gel criterion named; moduli measured at several frequencies around the claimed gel point, with the frequency dependence of the loss tangent shown; the strain amplitude shown to be within the linear range; where criteria disagree, the choice justified and the spread between them reported.

**Benchmark.** [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Gaborieau and P. Castignolles, Size-exclusion chromatography (SEC) of branched polymers and polysaccharides, Anal. Bioanal. Chem. 399, 1413 (2011); read on PubMed Central (PMC3026666) | doi:10.1007/s00216-010-4221-7 |
| 2 | J. G. Hernández-Cifre et al., Size-exclusion chromatography of macromolecules: a brief tutorial overview on fundamentals with computational tools for data analysis and determination of structural information, Polymers 17, 582 (2025); read on PubMed Central (PMC11902525) | doi:10.3390/polym17050582 |
| 3 | R. Salehiyan and S. Soleymani Eil Bakhtiari, A review on rheological approaches as a perfect tool to monitor thermal degradation of biodegradable polymers, Korea-Aust. Rheol. J. 36, 295 (2024); abstract read through the Semantic Scholar record | doi:10.1007/s13367-024-00111-3 |
| 4 | D. Vincenzi et al., Polymer scission in turbulent flows, J. Fluid Mech. 912, A18 (2021); read as arXiv:2004.14092 | doi:10.1017/jfm.2020.1092 |
| 5 | J. R. Prakash, Universal dynamics of dilute and semidilute solutions of flexible linear polymers, Curr. Opin. Colloid Interface Sci. 43, 63 (2019); read as arXiv:1901.07116 | doi:10.1016/j.cocis.2019.03.001 |
| 6 | C. Clasen et al., How dilute are dilute solutions in extensional flows?, J. Rheol. 50, 849 (2006) | doi:10.1122/1.2357595 |
| 7 | Y. Kong and J. N. Hay, The measurement of the crystallinity of polymers by DSC, Polymer 43, 3873 (2002) | doi:10.1016/S0032-3861(02)00235-5 |
| 8 | F. J. Lanyi et al., On the determination of the enthalpy of fusion of α-crystalline isotactic polypropylene using differential scanning calorimetry, X-ray diffraction, and Fourier-transform infrared spectroscopy: an old story revisited, Adv. Eng. Mater. 22, 1900796 (2020) | doi:10.1002/adem.201900796 |
| 9 | S. Romberg et al., Identifying the chemical gel point of epoxy-fumed silica composites using optimally windowed chirp measurements, Rheol. Acta 64 (2025); abstract read through the NIST publication record | doi:10.1007/s00397-025-01526-7 |
