---
id: T-MAGNETOMETRY
name: SQUID and vibrating-sample magnetometry
type: technique
field: physics
applies_when: the paper reports magnetic moment, magnetisation or dc susceptibility measured with a SQUID or vibrating-sample magnetometer on a bulk, thin-film or nanoscale sample, or bases a claim about magnetic order, moment size, coercivity, anisotropy, a transition or blocking temperature or superconducting screening on them
version: "0.1"
---

# SQUID and vibrating-sample magnetometry

Magnetometry is used to claim the size of magnetic moments, the kind of magnetic order, hysteresis parameters, anisotropy, transition and blocking temperatures and superconducting screening. All of these are inferred from the total magnetic moment of the sample together with its substrate and holder, recorded against a nominal field and temperature.

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

## 4. Field accuracy and magnet history

**Question.** For low-field results (coercive field, loop shift, remanence, zero-field cooling, low-field susceptibility), does the paper say how the actual field at the sample was known, given the remanent field of a superconducting magnet?

**Why it matters.** Magnetometers with superconducting magnets commonly report a field calculated from the magnet current, not a measured one. Flux trapped in the magnet leaves a remanent field opposing the last high field applied, of order 1 to 3 mT at low field after an excursion to several tesla, and it depends on the magnet's history. Plotted against the nominal field this gives an apparent hysteresis for a diamagnet, inverted loops for paramagnets and soft ferromagnets, shifted loops and incorrect coercive fields, and a nominally zero-field cooling that is not at zero field.

**Resolved by.** The field history before each low-field measurement stated (largest field reached, magnet reset or degaussing, field-setting mode); the remanent field quantified with a paramagnetic or diamagnetic reference run through the same sequence, and the data corrected or the limitation stated; low-field loops recorded separately after a magnet reset; coercive fields and loop shifts interpreted only where they exceed the field uncertainty.

**Benchmark.** [1], [2]

## 5. Signal size, detection limit and reproducibility

**Question.** Is the absolute size of the measured moment given, and is it shown to exceed the practical detection limit of the instrument and procedure, as established by controls and repeated measurements and not by the specified sensitivity alone?

**Why it matters.** The specified sensitivity refers to ideal conditions. Residual artefacts from the holder, handling, magnet remanence and background subtraction set a practical floor that published assessments place at a few 10⁻⁷ emu for careful routine work, well above the nominal figure. The scatter returned by the instrument's fit is also not the full uncertainty of a measurement.

**Resolved by.** Moments quoted in absolute units (emu or A m²) as well as normalised; the floor of the actual procedure demonstrated with a nominally non-magnetic control measured by the same protocol; repeated runs, including after remounting, and more than one sample; error bars that include background, field and geometry contributions; claims limited to signals clearly above that floor.

**Benchmark.** [1], [2], [3], [4]

## 6. Normalisation and units

**Question.** How was the moment converted to magnetisation, susceptibility or moment per atom (which mass, volume, thickness, density or composition), how was each of those measured, and what uncertainty does it carry?

**Why it matters.** The instrument returns only the total moment. The magnetic volume of a thin film or the number of magnetic atoms must be determined independently, and its uncertainty can exceed that of the magnetic measurement. Results given per gram, per volume, per mole or per atom, in cgs or SI units, are easy to convert wrongly and hard to compare between papers.

**Resolved by.** The mass or volume of the measured sample and the method used to obtain it stated (for films, area and an independently measured thickness); the as-measured moment given so that the normalisation can be checked; units and the basis of normalisation unambiguous, including which formula unit or magnetic ion a molar value refers to; the uncertainty of the normalising quantity included in quoted values.

**Benchmark.** [2], [7]

## 7. Demagnetising field and sample shape

**Question.** Are the sample shape and its orientation in the field stated, and where a claim depends on the internal field or on the absolute susceptibility (for example a superconducting screening fraction), was a demagnetising correction applied and how was the factor obtained?

**Why it matters.** In a finite sample the internal field differs from the applied field by an amount set by shape and magnetisation, and it is uniform only in ellipsoids. The apparent susceptibility is χ/(1 + Nχ), so for a strongly diamagnetic plate in a perpendicular field it can exceed the ideal value several-fold and an uncorrected screening fraction is overestimated. Shortcuts such as taking the factors along three axes to sum to one hold only for ellipsoids, and measured values for superconductors also deviate from the ideal because of inhomogeneity.

**Resolved by.** Sample dimensions and field direction reported; the demagnetising factor stated together with the formula or calculation used for the actual shape; susceptibility or screening fraction given after correction, with its sensitivity to the factor indicated; for superconductors, zero-field-cooled data taken in a small measuring field.

**Benchmark.** [6], [7]

## 8. Quantities derived from temperature-dependent curves

**Question.** For quantities derived from M(T) or χ(T), such as an effective moment, a Weiss temperature or a blocking temperature, does the paper state the definition used, the temperature range and terms included in any fit, the measuring field and the cooling and heating protocol?

**Why it matters.** Curie-Weiss parameters depend on the fitted range and on whether a temperature-independent term is included; even a small such term curves the inverse susceptibility, so a straight-line fit no longer returns the Curie constant and Weiss temperature. The law also presupposes local moments and a linear response to the measuring field. For particle ensembles, the peak of the zero-field-cooled curve, its inflection point and the mean blocking temperature differ by amounts that depend on the size distribution and the heating rate.

**Resolved by.** Inverse susceptibility plotted with the fitted range marked, and the fit made to it; a temperature-independent term included where that plot is curved, with its sign and size shown to be physically reasonable; evidence that the measuring field is in the linear regime; fitted moments compared with expected values; for a blocking temperature, the definition, measuring field and heating rate stated and the size distribution taken into account.

**Benchmark.** [7], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Sawicki, W. Stefanowicz and A. Ney, Sensitive SQUID magnetometry for studying nanomagnetism, Semicond. Sci. Technol. 26, 064006 (2011); read as preprint arXiv:1101.4764 | doi:10.1088/0268-1242/26/6/064006 | full text | Preprint Sec. II.A: the moment comes from fitting a point-dipole response, adequate to about 3% for samples up to 5 mm; subtracting a substrate is valid only if its response is purely diamagnetic. Sec. II.B with Table I: sample size, off-axis position and tilted moments change the reported moment by several per cent. Sec. II.C: the field is taken from the magnet current; trapped flux gives remanent fields up to tens of oersted and apparent or inverted hysteresis; compensation limited to about 99% at high field. Sec. II.D: holder signals. Sec. III: edge contamination, check in two orientations, residual artefacts of a few 10⁻⁷ emu in routine use |
| 2 | M. Buchner, K. Höfler, B. Henne, V. Ney and A. Ney, Tutorial: Basic principles, limits of detection, and pitfalls of highly sensitive SQUID magnetometry for nanomagnetism and spintronics, J. Appl. Phys. 124, 161101 (2018) | doi:10.1063/1.5045299 | full text | Sec. II.A: calibration, point-dipole fit and size limit; scatter from the fit is not the full uncertainty; sample volume must be measured independently. Sec. II.B: units, and the advice to state mass or volume or give the as-measured moment. Sec. II.C: specified sensitivity compared with the accuracy needed when a large background is subtracted. Secs. III.B and IV.A–B: nominal zero field is not zero; a remanent field of about 1.5 mT gives inverted loops and incorrect coercive fields; procedure to quantify it with reference samples. Sec. IV.C: reproducibility over repeated sequences and remounting; forcing zero signal at high field would remove a real contribution |
| 3 | M. A. Garcia, E. Fernandez Pinel, J. de la Venta, A. Quesada, V. Bouzas, J. F. Fernández, J. J. Romero, M. S. Martín González and J. L. Costa-Krämer, Sources of experimental errors in the observation of nanoscale magnetism, J. Appl. Phys. 105, 013925 (2009); read as preprint arXiv:0811.1127 | doi:10.1063/1.3060808 | full text | Secs. 2.1–2.4: adhesive tape with dust, steel tools, deformed straws, inks and silver paint each give spurious signals of about 10⁻⁶ to 10⁻⁴ emu. Sec. 2.5: a localised contaminant gives orientation-dependent signals. Sec. 3: mass-proportional contamination is excluded by chemical analysis, handling-related signals must be judged on the total moment before normalisation, and each laboratory should test its own procedures |
| 4 | L. M. C. Pereira, J. P. Araújo, M. J. Van Bael, K. Temst and A. Vantomme, Practical limits for detection of ferromagnetism using highly sensitive magnetometry techniques, J. Phys. D: Appl. Phys. 44, 215001 (2011) | doi:10.1088/0022-3727/44/21/215001 | abstract | Abstract: magnetic contamination arises from sample processing and handling and can be avoided or removed; with proper procedures extrinsic signals are kept below 5 × 10⁻⁷ emu; most of the findings also apply to vibrating-sample and alternating-gradient magnetometers |
| 5 | A. Zieba and S. Foner, Detection coil, sensitivity function, and sample geometry effects for vibrating sample magnetometers, Rev. Sci. Instrum. 53, 1344–1354 (1982) | doi:10.1063/1.1137182 | abstract | Abstract: the output of a vibrating-sample magnetometer depends on sample position, shape and size through the sensitivity function of the detection coils; corrections are calculated for large samples; field homogeneity, position errors and the sample support also affect the output |
| 6 | R. Prozorov and V. G. Kogan, Effective Demagnetizing Factors of Diamagnetic Samples of Various Shapes, Phys. Rev. Applied 10, 014030 (2018); read as preprint arXiv:1712.06037 | doi:10.1103/PhysRevApplied.10.014030 | full text | Preprint Sec. I: correcting for the field distortion of a finite sample is necessary; the internal field is uniform only in ellipsoids, and the factors sum to one only for ellipsoids. Sec. II, Eqs. (4)–(6): apparent susceptibility χ/(1 + Nχ), which diverges for a perfectly diamagnetic plate in a perpendicular field. Sec. VI.B, Eqs. (22)–(23): approximate factor for cuboids and the resulting error in the moment |
| 7 | S. Mugiraneza and A. M. Hallas, Tutorial: a beginner's guide to interpreting magnetic susceptibility data with the Curie-Weiss law, Commun. Phys. 5, 95 (2022) | doi:10.1038/s42005-022-00853-y | full text | "Magnetism units": unit conversion is error-prone. "Practical considerations", steps 1–7 and Fig. 3: record the mass accurately, state the number of magnetic ions used, watch for non-linear M(H), fit the inverse susceptibility over a justified range, include a temperature-independent term and check that it is physical; the law should not be applied without local moments. Box 2: superconducting screening is measured after zero-field cooling in a small field and deviates from the ideal value through inhomogeneity and demagnetising effects |
| 8 | I. J. Bruvera, P. Mendoza Zélis, M. P. Calatayud, G. F. Goya and F. H. Sánchez, Determination of the blocking temperature of magnetic nanoparticles: The good, the bad, and the ugly, J. Appl. Phys. 118, 184304 (2015); read as preprint arXiv:1508.04413 | doi:10.1063/1.4935484 | full text | Preprint Secs. I, III.A and IV: several definitions of a representative blocking temperature are in use; with a size distribution the peak and the inflection point of the zero-field-cooled curve move away from the mean blocking temperature, by amounts that depend on the width of the distribution and the heating rate |
