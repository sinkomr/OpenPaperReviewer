---
id: T-POLYMERS
name: Polymer experiments
type: technique
field: physics/soft-matter
applies_when: the paper reports experiments on polymer solutions, melts, networks or gels, quotes molar mass, dispersity, a concentration regime, solvent quality, a glass transition temperature, a degree of crystallinity or a gel point, or assigns a scaling exponent to polymer data
version: "0.1"
---

# Polymer experiments

Polymer experiments are used to claim how the size, dynamics, gelation and thermal transitions of chain molecules depend on molar mass, concentration, solvent and temperature, often summarised as a scaling exponent. The claims rest on characterisation by size-exclusion chromatography (SEC), light scattering, viscometry, rheology, differential scanning calorimetry (DSC) and dynamic mechanical analysis (DMA), and on placing the sample in the right regime relative to the overlap concentration (c*) and the theta temperature.

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

## 6. Glass transition temperature

**Question.** How was the glass transition temperature (Tg) measured: which technique, which heating or cooling rate or frequency, which point of the transition was taken, after what thermal history, and for which molar mass?

**Why it matters.** Tg depends on how it is measured: DSC and DMA give different values for the same polymer, and the value from DMA rises with test frequency. Thermal history and physical ageing change the glassy state, and Tg rises with molar mass for short chains. In thin films, methods that weight different parts of the film can give Tg shifts of different size and even opposite sign.

**Resolved by.** The technique, rate or frequency and the definition of Tg stated (onset, midpoint or another criterion); the thermal history erased by a stated protocol, such as a second heating after controlled cooling; the molar mass of the sample given; Tg values compared only between data taken by the same method and protocol; for thin films, the Tg definition stated and interpreted in terms of the part of the film it reflects.

**Benchmark.** [7], [8]

## 7. Degree of crystallinity

**Question.** How was the degree of crystallinity obtained: which reference enthalpy of fusion for the fully crystalline polymer was used and from where, how were cold crystallisation and recrystallisation during heating handled, and was the DSC value checked against X-ray diffraction or density?

**Why it matters.** DSC does not give the enthalpy of fusion of a fully crystalline polymer, which must come from an external calibration, and published reference values for a single polymer can differ by a factor of several. During heating the sample can recrystallise while it melts, so the area under the melting peak need not reflect the crystallinity at the start of the scan, and crystallinity itself depends strongly on cooling rate and thermal history.

**Resolved by.** The reference enthalpy and its source stated; integration limits and baseline given; exothermic events during heating subtracted or explained; the thermal history of the sample stated; agreement with an independent method such as X-ray diffraction or density shown, or the method dependence acknowledged when values are compared between studies.

**Benchmark.** [9], [10]

## 8. Gel point

**Question.** When a gel point or gelation time is reported, which rheological criterion located it (crossover of the storage and loss moduli at one frequency, a loss tangent independent of frequency, a peak in the loss tangent, divergence of a relaxation time), at which frequencies and strain amplitude was it measured, and could a physical network, for example of filler, mask the signature?

**Why it matters.** The criteria in common use need not give the same gel point, so a gelation time from a single-frequency crossover can differ from the point at which the loss tangent becomes independent of frequency. A physical network of filler or other components can hide the usual signatures of the chemical gel point, and many gelling systems have a narrow linear viscoelastic range, so large strains can disturb the network being measured.

**Resolved by.** The gel criterion named; moduli measured at several frequencies around the claimed gel point, with the frequency dependence of the loss tangent shown; the strain amplitude shown to be within the linear range; where criteria disagree, the choice justified and the spread between them reported.

**Benchmark.** [11]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Gaborieau and P. Castignolles, Size-exclusion chromatography (SEC) of branched polymers and polysaccharides, Anal. Bioanal. Chem. 399, 1413–1423 (2011); read on PubMed Central (PMC3026666) | doi:10.1007/s00216-010-4221-7 | full text | Introduction and "Separation of branched polymers": SEC separates by hydrodynamic volume, branched and linear chains of different molar mass co-elute, and molar masses are local averages. "Important prerequisites": apparent molar masses from linear standards give significant non-systematic errors for branched polymers; complete dissolution is essential and heat, sonication or extreme pH can degrade chains; ultrahigh-molar-mass polymers can be degraded by shear during separation, and excessive injection concentration causes shear degradation and band broadening. Conclusion: validate molar masses with two independent methods |
| 2 | J. G. Hernández-Cifre, M. Collado-González, F. G. Díaz Baños and J. García de la Torre, Size-exclusion chromatography of macromolecules: a brief tutorial overview on fundamentals with computational tools for data analysis and determination of structural information, Polymers 17, 582 (2025); read on PubMed Central (PMC11902525) | doi:10.3390/polym17050582 | full text | Sec. 2.1: conventional calibration with standards such as polystyrene gives molar masses relative to the standards; universal calibration through hydrodynamic volume and the intrinsic viscosity. Secs. 2.2 and 3: light scattering gives molar mass through an optical constant containing the refractive index increment, which is also needed for the concentration from the refractive-index detector. Secs. 4.1.3 and 5.4: definitions of the number-, weight- and z-average molar masses; Mn and Mz are less reliable than Mw because they come from the ends of the elution range, where detector signal-to-noise is poor |
| 3 | R. Salehiyan and S. Soleymani Eil Bakhtiari, A review on rheological approaches as a perfect tool to monitor thermal degradation of biodegradable polymers, Korea-Aust. Rheol. J. 36, 295–317 (2024); abstract read through the Semantic Scholar record | doi:10.1007/s13367-024-00111-3 | abstract | Abstract (Semantic Scholar record): molecular weight reduction by chain scission is a common degradation mechanism; time sweep tests monitor stability, frequency sweeps reveal effects of processing and thermal history, and higher-shear tests that simulate processing show that shear accelerates degradation |
| 4 | D. Vincenzi, T. Watanabe, S. S. Ray and J. R. Picardo, Polymer scission in turbulent flows, J. Fluid Mech. 912, A18 (2021); read as arXiv:2004.14092 | doi:10.1017/jfm.2020.1092 | abstract | Abstract: turbulence stretches and breaks polymers; the effect of polymers on the flow is transient because it disappears as they break; fragments can break again, giving a population of chains with a range of relaxation times |
| 5 | J. R. Prakash, Universal dynamics of dilute and semidilute solutions of flexible linear polymers, Curr. Opin. Colloid Interface Sci. 43, 63–79 (2019); read as arXiv:1901.07116 | doi:10.1016/j.cocis.2019.03.001 | full text | Sec. 2.1: the solvent-quality parameter combines the distance from the theta temperature with the square root of chain length; chains follow random-walk statistics at theta and self-avoiding statistics in athermal solvent, with a crossover between; universal predictions hold only in the long-chain limit. Sec. 2.2: definition of c* and the scaling of properties with c/c*. Sec. 2.3: in the semidilute regime at intermediate solvent quality, properties follow an effective exponent that depends on solvent quality, and viscosity data collapse when plotted against both variables |
| 6 | C. Clasen, J. P. Plog, W.-M. Kulicke, M. Owens, C. Macosko, L. E. Scriven, M. Verani and G. H. McKinley, How dilute are dilute solutions in extensional flows?, J. Rheol. 50, 849–881 (2006) | doi:10.1122/1.2357595 | abstract | Abstract (MIT group publication page): between about 0.01 and 1 times c* the relaxation time in extensional flow is much larger than the value from oscillatory shear or Zimm theory, and its power-law dependence on c/c* has an exponent that varies with solvent quality; a minimum concentration below which viscoelasticity cannot be resolved |
| 7 | T. Qu, G. Nan, Y. Ouyang, B. Bieketuerxun, X. Yan, Y. Qi and Y. Zhang, Structure-property relationship, glass transition, and crystallization behaviors of conjugated polymers, Polymers 15, 4268 (2023); read on PubMed Central (PMC10649048) | doi:10.3390/polym15214268 | full text | Section on Tg measurement methods and Table 1: DMA Tg rises with test frequency; DSC protocol of heating above the melt to erase thermal history, controlled cooling and reheating at the same rate; different testing methods give different Tg values for the same polymer; thermal history and physical ageing change the glassy state; Tg rises with number-average molar mass by the Fox–Flory relation |
| 8 | W. Zhang, J. F. Douglas and F. W. Starr, Why we need to look beyond the glass transition temperature to characterize the dynamics of thin supported polymer films, Proc. Natl. Acad. Sci. USA 115, 5641–5646 (2018); read on PubMed Central (PMC5984511) | doi:10.1073/pnas.1722024115 | full text | Abstract and Introduction: reported Tg shifts in thin films vary in size and sign; thermodynamic and dynamic methods can disagree because they weight the slow layer near the substrate differently. Conclusions: Tg estimates from different approaches are sensitive to different regions of the film, so a single Tg value does not characterize film dynamics |
| 9 | Y. Kong and J. N. Hay, The measurement of the crystallinity of polymers by DSC, Polymer 43, 3873–3878 (2002) | doi:10.1016/S0032-3861(02)00235-5 | abstract | Abstract (University of Birmingham repository record): the main difficulty in DSC crystallinity is that the sample recrystallises while it melts on heating, and enthalpies and crystallinity change with temperature; an arbitrary choice of the liquid heat capacity introduces systematic errors; DSC results compared with density |
| 10 | F. J. Lanyi, N. Wenzke, J. Kaschta and D. W. Schubert, On the determination of the enthalpy of fusion of α-crystalline isotactic polypropylene using differential scanning calorimetry, X-ray diffraction, and Fourier-transform infrared spectroscopy: an old story revisited, Adv. Eng. Mater. 22, 1900796 (2020) | doi:10.1002/adem.201900796 | abstract | Abstract (university research record): the enthalpy of fusion cannot be determined directly by DSC and must be calibrated by external methods such as X-ray diffraction or density; literature values for polypropylene range from about 60 to 260 J/g; crystallinity varied widely with cooling rates between 1 and about 3500 K/min |
| 11 | S. Romberg, S. Lehrman, J. Seppala and A. Kotula, Identifying the chemical gel point of epoxy-fumed silica composites using optimally windowed chirp measurements, Rheol. Acta 64 (2025); abstract read through the NIST publication record | doi:10.1007/s00397-025-01526-7 | abstract | Abstract: four gel criteria compared (crossover of the moduli, frequency-independent loss tangent, loss-tangent peak, divergence of relaxation time); a physical filler network can mask the usual gel indicators; many composites have a narrow linear viscoelastic range; with a weak filler network the frequency-independent loss tangent best matched the neat resin gel point, and with a strong network the loss tangent was not frequency independent |
