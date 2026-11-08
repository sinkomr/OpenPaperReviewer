---
id: T-MAGNETOMETRY
name: SQUID and vibrating-sample magnetometry
type: technique
field: physics/condensed-matter
applies_when: the paper reports magnetic moment, magnetisation or dc susceptibility measured with a SQUID or vibrating-sample magnetometer on a bulk, thin-film or nanoscale sample, or bases a claim about magnetic order, moment size, coercivity, anisotropy, a transition or blocking temperature or superconducting screening on them
version: "0.1"
---

# SQUID and vibrating-sample magnetometry

## 1. From detector signal to magnetic moment

**Question.** Does the paper give the sample dimensions, orientation and mounting, and say how the reported moment was obtained from the detector signal (fitting mode or calibration) and whether it was corrected for sample size, shape and position?

**Why it matters.** The moment is not measured directly. It is obtained by fitting or scaling the detection-coil signal against the response expected for a small dipole on the coil axis or for a calibration sample. A sample that is extended, off-axis or differently shaped couples differently to the coils, which changes the reported moment by several per cent, and a moment that is not parallel to the field, or a signal with two spatial origins, can distort the fit and so the shape of the measured loop.

**Resolved by.** Dimensions, orientation and mounting stated; the sample kept within the size for which the dipole approximation holds, or geometry correction factors applied; calibration against a reference of comparable geometry; the same geometry used for samples and references that are compared; for hard-axis loops or composite samples, inspection of the raw detector response or a fit with fixed sample position.

**Benchmark.** [1], [2], [5]

## 2. Substrate and holder background

**Question.** How large is the signal of interest compared with the total measured moment, and how were the contributions of the substrate, matrix and sample holder determined and removed?

**Why it matters.** For a film or nanostructure on a substrate the result is a small difference between two large numbers, so an error of a fraction of a per cent in the background, from geometry, field value or reproducibility, is as large as the result. Taking the background from the high-field slope assumes a purely linear, temperature-independent substrate response, which fails for substrates with paramagnetic impurities or small band gaps, and a correction tuned to give zero residual at high field can also remove a real contribution. A dented, cut or marked holder adds a signal of its own.

**Resolved by.** The as-measured moment shown alongside the corrected data, with the fraction assigned to the sample; a bare substrate or empty holder from the same batch measured with the same geometry, sequence and field history; the field and temperature range used to define the background stated, with evidence that the substrate response is linear and temperature-independent there; the uncertainty of the subtraction carried into the result.

**Benchmark.** [1], [2], [3]

## 3. Contamination from preparation and handling

**Question.** What was done to exclude magnetic contamination introduced during growth, cutting, handling and mounting, and is the measured moment larger than what such contamination typically produces?

**Why it matters.** Contact with steel tools, adhesive tape, airborne dust, inks, silver paint and other mounting materials can each leave ferromagnetic-like signals of roughly 10⁻⁶ to 10⁻⁴ emu. This is comparable to the total moment of many thin-film and nanoscale samples and becomes a large magnetisation once divided by a small mass or volume. A contaminant at one spot on the sample also changes its coupling to the coils when the sample is rotated, which can look like magnetic anisotropy.

**Resolved by.** Non-magnetic tools and clean mounting materials described; control samples (bare substrates, undoped or unprocessed pieces, the mounting materials alone) taken through the same steps and measured; the total moment in absolute units compared with those controls before normalisation; impurity analysis showing concentrations too low to account for the signal; for claimed anisotropy, measurements in more than one mounting orientation, including two in-plane directions.

**Benchmark.** [1], [3], [4]

## 4. Signal size, detection limit and reproducibility

**Question.** Is the absolute size of the measured moment given, and is it shown to exceed the practical detection limit of the instrument and procedure, as established by controls and repeated measurements and not by the specified sensitivity alone?

**Why it matters.** The specified sensitivity refers to ideal conditions. Residual artefacts from the holder, handling, magnet remanence and background subtraction set a practical floor that published assessments place at a few 10⁻⁷ emu for careful routine work, well above the nominal figure. The scatter returned by the instrument's fit is also not the full uncertainty of a measurement.

**Resolved by.** Moments quoted in absolute units (emu or A m²) as well as normalised; the floor of the actual procedure demonstrated with a nominally non-magnetic control measured by the same protocol; repeated runs, including after remounting, and more than one sample; error bars that include background, field and geometry contributions; claims limited to signals clearly above that floor.

**Benchmark.** [1], [2], [3], [4]

## 5. Normalisation and units

**Question.** How was the moment converted to magnetisation, susceptibility or moment per atom (which mass, volume, thickness, density or composition), how was each of those measured, and what uncertainty does it carry?

**Why it matters.** The instrument returns only the total moment. The magnetic volume of a thin film or the number of magnetic atoms must be determined independently, and its uncertainty can exceed that of the magnetic measurement. Results given per gram, per volume, per mole or per atom, in cgs or SI units, are easy to convert wrongly and hard to compare between papers.

**Resolved by.** The mass or volume of the measured sample and the method used to obtain it stated (for films, area and an independently measured thickness); the as-measured moment given so that the normalisation can be checked; units and the basis of normalisation unambiguous, including which formula unit or magnetic ion a molar value refers to; the uncertainty of the normalising quantity included in quoted values.

**Benchmark.** [2], [7]

## 6. Demagnetising field and sample shape

**Question.** Are the sample shape and its orientation in the field stated, and where a claim depends on the internal field or on the absolute susceptibility (for example a superconducting screening fraction), was a demagnetising correction applied and how was the factor obtained?

**Why it matters.** In a finite sample the internal field differs from the applied field by an amount set by shape and magnetisation, and it is uniform only in ellipsoids. The apparent susceptibility is χ/(1 + Nχ), so for a strongly diamagnetic plate in a perpendicular field it can exceed the ideal value several-fold and an uncorrected screening fraction is overestimated. Shortcuts such as taking the factors along three axes to sum to one hold only for ellipsoids, and measured values for superconductors also deviate from the ideal because of inhomogeneity.

**Resolved by.** Sample dimensions and field direction reported; the demagnetising factor stated together with the formula or calculation used for the actual shape; susceptibility or screening fraction given after correction, with its sensitivity to the factor indicated; for superconductors, zero-field-cooled data taken in a small measuring field.

**Benchmark.** [6], [7]

## 7. Quantities derived from temperature-dependent curves

**Question.** For quantities derived from M(T) or χ(T), such as an effective moment, a Weiss temperature or a blocking temperature, does the paper state the definition used, the temperature range and terms included in any fit, the measuring field and the cooling and heating protocol?

**Why it matters.** Curie-Weiss parameters depend on the fitted range and on whether a temperature-independent term is included; even a small such term curves the inverse susceptibility, so a straight-line fit no longer returns the Curie constant and Weiss temperature. The law also presupposes local moments and a linear response to the measuring field. For particle ensembles, the peak of the zero-field-cooled curve, its inflection point and the mean blocking temperature differ by amounts that depend on the size distribution and the heating rate.

**Resolved by.** Inverse susceptibility plotted with the fitted range marked, and the fit made to it; a temperature-independent term included where that plot is curved, with its sign and size shown to be physically reasonable; evidence that the measuring field is in the linear regime; fitted moments compared with expected values; for a blocking temperature, the definition, measuring field and heating rate stated and the size distribution taken into account.

**Benchmark.** [7], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Sawicki et al., Sensitive SQUID magnetometry for studying nanomagnetism, Semicond. Sci. Technol. 26, 064006 (2011); read as preprint arXiv:1101.4764 | doi:10.1088/0268-1242/26/6/064006 |
| 2 | M. Buchner et al., Tutorial: Basic principles, limits of detection, and pitfalls of highly sensitive SQUID magnetometry for nanomagnetism and spintronics, J. Appl. Phys. 124, 161101 (2018) | doi:10.1063/1.5045299 |
| 3 | M. A. Garcia et al., Sources of experimental errors in the observation of nanoscale magnetism, J. Appl. Phys. 105, 013925 (2009); read as preprint arXiv:0811.1127 | doi:10.1063/1.3060808 |
| 4 | L. M. C. Pereira et al., Practical limits for detection of ferromagnetism using highly sensitive magnetometry techniques, J. Phys. D: Appl. Phys. 44, 215001 (2011) | doi:10.1088/0022-3727/44/21/215001 |
| 5 | A. Zieba and S. Foner, Detection coil, sensitivity function, and sample geometry effects for vibrating sample magnetometers, Rev. Sci. Instrum. 53, 1344 (1982) | doi:10.1063/1.1137182 |
| 6 | R. Prozorov and V. G. Kogan, Effective Demagnetizing Factors of Diamagnetic Samples of Various Shapes, Phys. Rev. Applied 10, 014030 (2018); read as preprint arXiv:1712.06037 | doi:10.1103/PhysRevApplied.10.014030 |
| 7 | S. Mugiraneza and A. M. Hallas, Tutorial: a beginner's guide to interpreting magnetic susceptibility data with the Curie-Weiss law, Commun. Phys. 5, 95 (2022) | doi:10.1038/s42005-022-00853-y |
| 8 | I. J. Bruvera et al., Determination of the blocking temperature of magnetic nanoparticles: The good, the bad, and the ugly, J. Appl. Phys. 118, 184304 (2015); read as preprint arXiv:1508.04413 | doi:10.1063/1.4935484 |
