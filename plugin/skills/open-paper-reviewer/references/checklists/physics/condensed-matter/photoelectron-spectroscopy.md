---
id: T-PHOTOELECTRON-SPECTROSCOPY
name: Photoelectron spectroscopy
type: technique
field: physics/condensed-matter
applies_when: the paper reports X-ray or ultraviolet photoelectron spectra (XPS, UPS, HAXPES), or bases a claim about surface composition, oxidation or chemical state, bonding, core-level binding-energy shifts, work function or energy-level alignment on them; angle-resolved photoemission has its own card
version: "0.1"
---

# Photoelectron spectroscopy

## 1. Charging and charge compensation

**Question.** For samples that are insulating, semiconducting or not in good electrical contact with the spectrometer, does the paper say how surface charging was controlled (flood gun or other neutraliser, mounting, grounding or isolation) and show that the peak positions and shapes used for the claims are free of differential charging?

**Why it matters.** Emission of photoelectrons leaves positive charge that shifts all peaks to higher apparent binding energy, by anything from a few tenths of an electronvolt, which can pass unnoticed, to hundreds of electronvolts. When the charge is not uniform across the sample or through a layered structure, it broadens and distorts peaks and can add features that look like an extra chemical state.

**Resolved by.** The charge-control method and its settings stated; peak shapes and positions shown to be unchanged when the neutraliser settings or the X-ray flux are varied, or when a different spot is measured; peak widths compared with those from a test sample measured under the same conditions; for samples with a Fermi edge, the edge shown at zero binding energy as evidence of electrical contact.

**Benchmark.** [2], [3]

## 2. Energy scale calibration and binding-energy referencing

**Question.** How was the spectrometer energy scale calibrated, and, separately, how were binding energies corrected for charging: which reference peak and value were used, are the reference spectra shown, and was the result checked by an independent route?

**Why it matters.** Calibration against clean reference metals is distinct from charge referencing, and the two are often confused. The most common charge reference, the C 1s peak of adventitious carbon, is set at values spread over more than 1 eV in the literature, and on conducting samples its measured binding energy varies by more than 2 eV with the substrate and its work function, so referencing to it can produce chemical-state assignments that are wrong or physically impossible. Gold deposits and substrate peaks have their own known limitations as references, and no single method gives absolute binding energies for insulators.

**Resolved by.** The energy-scale calibration stated, for example against Au 4f7/2, Ag 3d5/2 and Cu 2p3/2 peaks of sputter-cleaned metals as in ISO 15472, and repeated regularly; the charge-referencing method, the peak and the value used stated and the reference spectrum shown; the referencing checked against an internal reference of known chemistry, against peak separations within the sample, or against another method; conclusions drawn from relative shifts within one sample where absolute binding energies are uncertain.

**Benchmark.** [2], [3], [4]

## 3. Peak fitting

**Question.** Is each peak fit physically constrained, with a background suited to the material, component widths held within a range set by the instrument and reference spectra, spin-orbit doublets with fixed separation and area ratio and line shapes suited to the material, and is each fit shown over the measured data with the background, the components and the envelope?

**Why it matters.** The choice of background and its end points changes component areas more than any other fitting choice. Extra components almost always improve a fit without having chemical meaning, and fits with widely varying widths, wrong or missing spin-orbit constraints, data too noisy or too poorly resolved to separate components, or narrow windows that cut off the background or one doublet partner are among the errors most often found in published XPS analyses, alongside fit parameters that are not reported.

**Resolved by.** A background chosen for the material and justified, shown with the unaltered data; component widths constrained within a narrow range justified by the instrument resolution or by reference spectra; spin-orbit doublets with fixed separation and area ratio; asymmetric line shapes where the material requires them, such as metals; only as many components as the chemistry supports, each confirmed where possible by a related peak of the same sample, such as O 1s for an oxidized carbon component; a test, such as a uniqueness plot, showing that the result does not hinge on one width or constraint; the fit parameters and software reported.

**Benchmark.** [1], [4], [5]

## 4. Assignment of chemical states

**Question.** On what basis is each component assigned to a chemical state: reference compounds measured on the same instrument, database values, or the accompanying spectral features such as satellites, multiplet structure and Auger lines?

**Why it matters.** Binding energies tabulated for the same compound by different laboratories spread by about 1 eV even for metals and by more for oxides, nitrides and other compounds, which is comparable to typical chemical shifts. Shake-up satellites and spin-orbit partners are often mislabelled as separate chemical states, plasmon losses and multiplet splitting add further structure that has to be accounted for, and a shift can come from charging, electrical contact or the local electrostatic environment instead of a change in chemistry.

**Resolved by.** Reference materials of known chemistry measured under the same conditions, or database values with their spread acknowledged; every spectral feature, including satellites and loss structure, accounted for; assignments consistent across all elements in the survey and narrow scans; peak separations within the sample compared, since a shift shared by every core level suggests an electrostatic rather than chemical origin; where suitable Auger lines are present, the Auger parameter, which does not depend on charging, used as a cross-check; support from another technique for assignments that carry the claim.

**Benchmark.** [2], [3], [4]

## 5. Quantification of composition

**Question.** How were atomic fractions or ratios obtained from peak areas: which sensitivity factors and from what source, which background, whether they suit the instrument's transmission function, and whether the sample meets the assumption of a homogeneous composition within the sampling depth?

**Why it matters.** Sensitivity factors measured on one instrument or operating mode apply only to instruments with the same energy-dependent transmission, and using the wrong set can change a ratio by about a quarter. Atomic percentages assume a single homogeneous phase within the sampling depth, which few real samples satisfy, and sensitivity varies by about a factor of 100 between elements, so a nominal detection limit does not apply to every element.

**Resolved by.** The source of the sensitivity factors and the background method stated; the procedure checked on a reference material of known stoichiometry with a clean surface; results described as equivalent homogeneous composition, or a layer or phase model used, when the sample is not uniform; detection limits estimated for the element and matrix in question.

**Benchmark.** [1], [5]

## 6. Surface sensitivity, depth and sputtering

**Question.** Does the paper relate the information depth of the measurement to the claim, and where a bulk property, a buried layer or a depth profile is claimed, does it show that the result is not an artefact of the surface or of ion sputtering?

**Why it matters.** With laboratory X-ray sources most of the signal comes from the top 1 to 10 nm, whose composition generally differs from the bulk because species segregate to or are depleted from the surface. Ion sputtering used to clean or profile a sample can cause preferential removal of some elements, implantation, disorder and chemical reduction, and the modified layer can be comparable to the sampling depth, so that a large share of the signal after sputtering comes from altered material.

**Resolved by.** The information depth stated for the relevant peaks; claims about the bulk or buried interfaces supported by more bulk-sensitive or depth-resolved data, such as higher photon energies or varied emission angle; ion species, energy and angle stated for any sputtering, with evidence that the chemistry of interest survives it, for example comparison with unsputtered or gently sputtered surfaces; overlayer thicknesses derived with a stated model and attenuation lengths.

**Benchmark.** [1], [3], [5]

## 7. Sample history, contamination and beam damage

**Question.** Does the paper describe how the sample was prepared, stored, exposed to air and transferred before measurement, show a survey spectrum with every detected element identified, and show that the X-rays, flood electrons or ions did not change the sample during data collection?

**Why it matters.** Because the measurement samples only the outermost layers, air exposure of minutes can grow oxide on reactive materials, solvents can remove or alter surface species, and adventitious carbon and other contamination can obscure the surface of interest. Some materials, notably high oxidation states of some transition metals, are reduced by X-ray exposure or by the charge-neutralization beam during the time needed to collect data, which creates the lower oxidation states that might then be reported.

**Resolved by.** Preparation, storage time, environment and transfer conditions stated, with inert transfer, in-situ preparation or a capping layer where the surface is reactive; a survey spectrum with all elements identified; spectra repeated over the exposure time, or a fresh spot used, showing no change in the chemical states of interest; any degradation observed during analysis reported.

**Benchmark.** [1], [2], [3], [5]

## 8. Work function and valence-band measurements

**Question.** For work functions and energy levels from UPS or the secondary-electron cutoff, does the paper give the photon energy, the sample bias, how the Fermi level was referenced, and how the cutoff was located, and does it show that the cutoff is a single, bias-independent onset from a sample that is not charging?

**Why it matters.** The sample is biased to measure the slowest electrons, and both the applied field and fields at the surface distort electron paths, so the result depends on geometry and bias range. Contaminated or inhomogeneous surfaces can show extra intensity or several onsets below the true cutoff, air exposure itself shifts the work function, and charging of poorly conducting samples moves the whole spectrum.

**Resolved by.** The Fermi edge of a grounded clean metal used to set the energy scale and the work function of a clean reference metal reported; the cutoff region shown with the fit used to locate it; the cutoff measured at several bias values within a range shown to be linear for a reference metal, giving the same work function after correction; analyser acceptance angle and pass energy stated; surface preparation and the absence of charging documented for the measured sample.

**Benchmark.** [3], [6], [7]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | D. R. Baer et al., Practical guides for x-ray photoelectron spectroscopy: First steps in planning, conducting, and reporting XPS measurements, J. Vac. Sci. Technol. A 37, 031401 (2019); read as the published PDF hosted by the Caltech Molecular Materials Research Center | doi:10.1116/1.5065501 |
| 2 | D. R. Baer et al., XPS guide: Charge neutralization and binding energy referencing for insulating samples, J. Vac. Sci. Technol. A 38, 031204 (2020); read as the published PDF hosted by the Caltech Molecular Materials Research Center | doi:10.1116/6.0000057 |
| 3 | G. Greczynski and L. Hultman, X-ray photoelectron spectroscopy: Towards reliable binding energy referencing, Prog. Mater. Sci. 107, 100591 (2020); read as the copy in the Linköping University repository (DiVA) | doi:10.1016/j.pmatsci.2019.100591 |
| 4 | G. H. Major et al., Practical guide for curve fitting in x-ray photoelectron spectroscopy, J. Vac. Sci. Technol. A 38, 061203 (2020); read as the published PDF hosted by the Caltech Molecular Materials Research Center | doi:10.1116/6.0000377 |
| 5 | A. G. Shard, Practical guides for x-ray photoelectron spectroscopy: Quantitative XPS, J. Vac. Sci. Technol. A 38, 041201 (2020); read as the published PDF hosted by the Caltech Molecular Materials Research Center | doi:10.1116/1.5141395 |
| 6 | A. P. Baddorf, Identifying the secondary electron cutoff in ultraviolet photoemission spectra for work function measurements of non-ideal surfaces, Sci. Rep. 13, 13452 (2023) | doi:10.1038/s41598-023-40187-5 |
| 7 | J. E. Whitten, Ultraviolet photoelectron spectroscopy: Practical aspects and best practices, Appl. Surf. Sci. Adv. 13, 100384 (2023) | doi:10.1016/j.apsadv.2023.100384 |
