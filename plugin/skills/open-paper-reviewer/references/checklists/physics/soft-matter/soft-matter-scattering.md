---
id: T-SOFT-MATTER-SCATTERING
name: Scattering from soft matter
type: technique
field: physics/soft-matter
applies_when: the paper uses dynamic or static light scattering, small-angle X-ray scattering or small-angle neutron scattering on colloids, polymers, micelles, vesicles or proteins in solution, melts or gels to claim a size, size distribution, molar mass, shape, internal structure, aggregation state or interaction
version: "0.1"
---

# Scattering from soft matter

## 1. Aggregates, dust and sample change during exposure

**Question.** What shows that the scattering comes from the species the claim is about, without large aggregates, dust or particles formed during the measurement: how was the sample cleaned, and are the low-angle data, repeated exposures and an independent separation or sizing method consistent with a single population?

**Why it matters.** Scattered intensity rises steeply with particle size, roughly as the sixth power of radius for small particles in light scattering, so a trace of aggregates or dust can dominate the signal and the mean size. A linear Guinier plot is necessary but not sufficient to show that a sample is monodisperse, and X-ray exposure can itself create aggregates.

**Resolved by.** Filtration or centrifugation and clean cells described; Guinier plots shown with their fit range and quality; inline size-exclusion separation or a second method used to check the composition; successive exposures compared and combined only when they agree, with the dose stated; intensity-weighted size distributions shown alongside any volume- or number-weighted ones, so that a small population of large particles is visible.

**Benchmark.** [1], [2], [5]

## 2. Concentration and interparticle interference

**Question.** Were the measurements made at several concentrations, and are the quoted size, radius of gyration and forward intensity per unit concentration extrapolated to infinite dilution or shown not to depend on concentration?

**Why it matters.** At finite concentration, interparticle interactions add a structure factor to the scattering: repulsion lowers the low-angle intensity and the apparent size, and attraction or association raises them. A single-concentration measurement cannot tell these effects apart from a change in the particles themselves. The interaction parameters, such as the second virial coefficient, are themselves sensitive to errors in concentration.

**Resolved by.** A concentration series with the forward intensity per unit concentration and the radius of gyration or hydrodynamic radius plotted against concentration; extrapolation to zero concentration, or a structure-factor model stated and justified; the method and uncertainty of each concentration measurement given; solvent conditions, such as ionic strength for proteins and charged colloids, chosen with interference in mind.

**Benchmark.** [1], [2], [5], [8]

## 3. Multiple scattering

**Question.** Is the sample thin and dilute enough that each detected photon or neutron has been scattered only once, and does the paper show this, for example through the transmission, a dilution or thickness series, or a cross-correlation or backscattering geometry for light?

**Why it matters.** Standard analyses of light, X-ray and neutron scattering assume single scattering. In turbid suspensions multiply scattered light corrupts both static and dynamic results, and for X-rays or neutrons multiple scattering grows in thick, strongly scattering samples, where it is worth testing once the transmission falls below about one over e.

**Resolved by.** The sample transmission or turbidity stated; results shown to be unchanged on dilution or with a thinner cell or a different wavelength; for turbid light-scattering samples, a method that suppresses multiple scattering, such as cross-correlation, described with its settings; for X-rays and neutrons, multiple scattering included in the model when it cannot be avoided.

**Benchmark.** [3], [5], [7]

## 4. Background and buffer subtraction

**Question.** What was subtracted as background, how well does it match the sample (same buffer, cell and conditions), and were sample and background each corrected for transmission and thickness before subtraction?

**Why it matters.** Small-angle signals from dilute solutions are often a small difference between two large numbers, so a slightly mismatched buffer, a different cell or an uncorrected transmission distorts the high-angle data on which shape and internal structure depend. In SANS the incoherent scattering from hydrogen gives a large flat background that differs between sample and solvent, and an ad hoc constant subtracted to remove it changes the fit.

**Resolved by.** The blank stated and matched to the sample, such as the final dialysate or column eluent; transmissions measured and applied; the background remeasured whenever the cell, geometry or solvent changes; any constant background adjusted in fitting reported with its value; the data before and after subtraction available for inspection.

**Benchmark.** [1], [2], [3]

## 5. Absolute intensity and the inputs to molar mass

**Question.** For any molar mass, aggregation number, volume fraction or number density, is the intensity on an absolute scale against a stated standard, and are the concentration, contrast, partial specific volume or refractive index increment used in the conversion given with their sources and uncertainties?

**Why it matters.** Molar mass and related quantities follow from the forward intensity only through the concentration and the square of the contrast, or in light scattering through the refractive index increment, so a small error in these inputs gives a large error in the result. Tabulated or calculated refractive index increments can be inaccurate for a given solute, solvent and wavelength, and scaling to a protein standard rather than an absolute standard adds further assumptions.

**Resolved by.** The calibration standard named, such as water or a certified glassy carbon reference for SAXS, with the calibration factor and its uncertainty; sample thickness and transmission measured; the refractive index increment measured at the instrument's wavelength and conditions, or the contrast and partial specific volume calculated from a stated composition; the uncertainties of these inputs carried into the molar mass; a cross-check such as the Porod volume or an independent mass measurement.

**Benchmark.** [1], [2], [4], [8]

## 6. From a correlation function to a size

**Question.** For DLS, which analysis turned the correlation function into a size (cumulants or a distribution inversion, with what regularisation and fit range), which weighting and mean are quoted, and what viscosity, temperature and refractive index were used?

**Why it matters.** The cumulant mean is intensity-weighted and suits a single, narrow population; distribution inversions are ill-posed, depend on the regulariser and can differ from the cumulant mean by more than 15 per cent, and they can fail to separate populations of similar size, such as a monomer and a dimer. Polydispersity indices from DLS are an unreliable measure of distribution width, conversion from intensity to volume or number weighting assumes spherical, homogeneous particles, and the Stokes-Einstein radius is only as accurate as the viscosity and temperature that enter it.

**Resolved by.** The correlation functions and fits shown; the analysis method, its settings and the weighting of each quoted size stated; the cumulant result reported alongside any distribution; claims of more than one population supported by evidence beyond a single inversion; temperature, solvent viscosity and refractive index stated; the hydrodynamic radius described as the size of an equivalent sphere, not a geometric size.

**Benchmark.** [5], [6]

## 7. Contrast variation and deuteration

**Question.** For SANS contrast variation or matching, are the deuteration levels of each component and of the solvent measured, are the match points determined experimentally, and are forward intensity and radius of gyration reported at each contrast and checked against what the composition predicts?

**Why it matters.** Separating the components of a complex relies on knowing their scattering length densities, which depend on the degree of deuteration and on exchange of labile hydrogens with the solvent. A mismatch in the assumed match point leaves a residual signal from a component meant to be invisible, and heavy water can itself induce aggregation.

**Resolved by.** Deuteration levels measured, for example by mass spectrometry, and solvent composition stated; exchange with the solvent controlled, such as dialysate kept closed; the match point of each component found from a contrast series; forward intensity and radius of gyration reported at every contrast and compared with the values predicted from composition; a Stuhrmann analysis or equivalent where internal density variation is claimed.

**Benchmark.** [1], [2]

## 8. How unique the model fit is

**Question.** How many structural parameters does the model fitted to the scattering curve have compared with the information in the data, does the measured range of scattering vector cover the sizes claimed, were other plausible models tried and rejected on the data, and is the uncertainty and ambiguity of the fitted shape, size distribution or structure reported?

**Why it matters.** Orientation averaging reduces the scattering to a one-dimensional curve with limited information, so different shapes, size distributions and degrees of polydispersity can fit the same data equally well. The data constrain only sizes between roughly pi over the highest and pi over the lowest scattering vector measured. That a model fits does not show that it is the right model, and ab initio shapes, ensembles and size distributions are especially open to over-interpretation.

**Resolved by.** The model and its free and fixed parameters stated; the scattering-vector range of each fit, including the Guinier range, given and shown to reach about pi over the largest dimension claimed; residuals over the full range and not only a chi-squared value; alternative models, such as different shapes or polydispersity, compared on the same data; repeated reconstructions or Monte Carlo fits with their spread, or an ambiguity estimate; constraints from independent methods such as microscopy or known atomic structures stated; conclusions limited to features that all acceptable models share.

**Benchmark.** [1], [2], [3], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | J. Trewhella et al., 2017 publication guidelines for structural modelling of small-angle scattering data from biomolecules in solution: an update, Acta Cryst. D73, 710 (2017); read through PubMed Central (PMC5586245) | doi:10.1107/S2059798317011597 |
| 2 | D. A. Jacques and J. Trewhella, Small-angle scattering for structural biology: expanding the frontier while avoiding the pitfalls, Protein Sci. 19, 642 (2010); read through PubMed Central (PMC2867006) | doi:10.1002/pro.351 |
| 3 | B. R. Pauw, Everything SAXS: small-angle scattering pattern collection and correction, J. Phys.: Condens. Matter 25, 383201 (2013); read as preprint arXiv:1306.0637 | doi:10.1088/0953-8984/25/38/383201 |
| 4 | A. J. Allen et al., NIST Standard Reference Material 3600: absolute intensity calibration standard for small-angle X-ray scattering, J. Appl. Cryst. 50, 462 (2017); read through PubMed Central (PMC5377342) | doi:10.1107/S1600576717001972 |
| 5 | J. Stetefeld et al., Dynamic light scattering: a practical guide and applications in biomedical sciences, Biophys. Rev. 8, 409 (2016); read through PubMed Central (PMC5425802) | doi:10.1007/s12551-016-0218-6 |
| 6 | N. Farkas and J. A. Kramar, Dynamic light scattering distributions by any means, J. Nanopart. Res. 23 (2021); abstract read through the NIST publication record | doi:10.1007/s11051-021-05220-6 |
| 7 | I. D. Block and F. Scheffold, Modulated 3D cross-correlation light scattering: improving turbid sample characterization, Rev. Sci. Instrum. 81, 123107 (2010); read as preprint arXiv:1008.0615 | doi:10.1063/1.3518961 |
| 8 | F. Yin et al., Bayesian analysis of static light scattering data for globular proteins, PLoS ONE 16, e0258429 (2021) | doi:10.1371/journal.pone.0258429 |
| 9 | B. R. Pauw et al., Improvements and considerations for size distribution retrieval from small-angle scattering data by Monte Carlo methods, J. Appl. Cryst. 46, 365 (2013); read as preprint arXiv:1210.5304 | doi:10.1107/S0021889813001295 |
