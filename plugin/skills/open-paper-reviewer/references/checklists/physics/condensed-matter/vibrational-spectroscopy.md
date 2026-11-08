---
id: T-VIBRATIONAL-SPECTROSCOPY
name: Raman and infrared vibrational spectroscopy
type: technique
field: physics/condensed-matter
applies_when: the paper reports Raman or infrared (FTIR, ATR) spectra, or bases a claim on them about phase or compound identity, phonon modes, crystal symmetry, strain, doping, defect density, temperature, layer number or crystallite size
version: "0.1"
---

# Raman and infrared vibrational spectroscopy

## 1. Heating and other changes caused by the laser

**Question.** Are the excitation wavelength, the power at the sample, the spot size and the acquisition time given, and is it shown that band positions, widths and relative intensities do not change with laser power or exposure?

**Why it matters.** A focused laser can heat a sample strongly enough to serve as the heater in thermal measurements, and Raman band positions and widths depend on temperature, so a shift or broadening can be produced by the measurement itself. Intense or pulsed illumination can also bleach or damage the sample. A temperature read from the ratio of Stokes to anti-Stokes intensities can be wrong under resonant conditions.

**Resolved by.** Power, spot size and exposure stated for each data set; spectra taken at two or more powers, or repeated on the same spot, shown to agree, or the power dependence measured and the reported values taken where it is negligible; a check that no irreversible change occurred during the measurement; any temperature read from the spectra corrected for resonance effects.

**Benchmark.** [1], [2], [3], [4]

## 2. Spectral axis calibration and resolution

**Question.** How was the Raman shift or wavenumber axis calibrated (reference lines or material, form of the calibration function, how often, and how the laser wavelength was checked), what is the spectral resolution, and how do both compare with the shifts or width changes that are claimed?

**Why it matters.** A linear wavelength calibration of a grating spectrograph can leave errors of several wavenumbers, larger than the instrument linewidth, and drift of the laser wavelength moves every Raman band. The same sample measured on different instruments gives different band positions, widths and intensities, and relative intensities depend on the wavelength response of each instrument unless they are corrected. Small differences between spectra taken on different set-ups or days may therefore be instrumental.

**Resolved by.** The calibration lines, function and schedule given; accuracy and repeatability demonstrated on a reference material measured alongside the samples; the spectral resolution stated; claimed shifts larger than the demonstrated accuracy; relative intensities corrected with a certified intensity standard when they are compared across instruments, excitation wavelengths or wide spectral ranges.

**Benchmark.** [1], [2], [5], [6]

## 3. Background subtraction and band fitting

**Question.** How was the fluorescence or other broad background removed (excitation wavelength chosen, baseline method and parameters), which line shape, number of components and constraints were used to fit the bands, and are the band positions, widths and areas on which claims rest stable under reasonable alternative baselines and line shapes?

**Why it matters.** Fluorescence can be far stronger than the Raman signal, and removing it by polynomial or other baseline fits involves choices that can be subjective and that different methods make differently, so weak or broad bands can be created, removed or reshaped. Fitted positions, intensities, areas and widths depend on the profile chosen, weak broad bands carry large errors, and the strong infrared bands of inorganic materials rarely follow a Lorentz profile. Bands of the substrate or support can appear in the spectrum and be mistaken for the sample's.

**Resolved by.** Excitation wavelength chosen, or changed, to reduce fluorescence; the baseline method and its parameters stated; fits shown with residuals; the line shape justified by the nature of the band and the number of components by the expected modes; uncertainties in fitted parameters that include the dependence on baseline and profile; substrate and blank spectra shown so that their bands are not assigned to the sample.

**Benchmark.** [1], [7], [8], [9], [10], [11]

## 4. Band assignment and phase identification

**Question.** Is each band used to identify a phase, compound or vibrational mode assigned by comparison with reference spectra of known materials and with the modes allowed by the crystal structure, and are bands that do not fit (second-order, resonant, defect-activated, substrate or impurity bands) accounted for?

**Why it matters.** The number of Raman-active and IR-active zone-centre modes follows from the space group and the occupied atomic sites, so a set of bands consistent with one structure may be inconsistent with another. Near resonance, second-order and finite-wavevector features appear that are absent away from resonance, and assignments of such features have been revised over time. In nanomaterials, size and shape distribution, defects, strain, coupling and chemical reactions also change the spectrum, so a match of band positions alone can mislead.

**Resolved by.** An assignment table giving each band, its symmetry and the reference spectrum or calculation behind it; the number of observed bands compared with the number of modes expected for the structure; assignments confirmed by polarization or excitation-wavelength dependence; every observed band accounted for, including those left unassigned; for phase identification, the main bands of plausible competing phases and impurities shown to be absent.

**Benchmark.** [11], [12], [13]

## 5. Polarization and selection rules

**Question.** When a mode symmetry, a crystal orientation or an anisotropy is claimed, does the paper give the scattering geometry and the incident and analysed polarizations relative to the crystal axes, and does it show the angular dependence of the intensities rather than a single configuration?

**Why it matters.** The Raman tensor of each mode decides whether it appears with parallel or crossed polarizations; in layered transition metal dichalcogenides measured in backscattering, the out-of-plane A1g mode vanishes with crossed polarizations, so polarization changes the spectrum and is used to separate overlapping bands. In low-symmetry and optically anisotropic crystals the tensor elements are in general complex and depend on laser energy and sample thickness, so a model with real tensor elements, or measurements in only two configurations, may not determine the symmetry.

**Resolved by.** The scattering geometry and polarizations stated in a standard notation, with the crystal orientation determined independently; angle-resolved intensities in parallel and crossed configurations fitted with the tensor for the assumed symmetry; for anisotropic samples, the dependence on excitation energy and thickness taken into account.

**Benchmark.** [11], [14]

## 6. One cause or several for a band change

**Question.** When a change in band position, width, intensity or shape is attributed to one cause (strain, doping, temperature, defects, layer number or crystallite size), does the paper exclude the others or separate them?

**Why it matters.** Strain and charge both shift the same phonon modes, so neither can be read from one band position without knowledge of the other, and temperature, defects, chemical change and size distributions act on the same observables. Layer-number signatures are not unique: a single-component band taken as the mark of a single layer can also come from misoriented multilayers, and empirical relations between band separation and layer number, calibrated on one kind of sample, may not hold for material grown another way or for thicker stacks.

**Resolved by.** Two or more modes analysed together, for example by correlating their shifts; widths and intensities used alongside positions; an independent measurement that fixes one of the variables (thickness, carrier density, temperature); layer number confirmed by interlayer modes or an independent thickness measurement; the alternatives that remain stated.

**Benchmark.** [2], [3], [11], [13]

## 7. Intensity ratios as quantitative measures

**Question.** When a band intensity ratio is used to quantify defect density, crystallite size, layer number or doping, are the excitation wavelength, the substrate and the definition of intensity (height or area) given, and is the relation used valid for those conditions and for that range?

**Why it matters.** At fixed defect density the ratio of a defect-activated band to an allowed band depends strongly on excitation energy and passes through a maximum as disorder increases, so one value can correspond to two defect densities, and some defects give no defect band at all. Interference in layered substrates changes band ratios with substrate and wavelength, near resonance ratios change with excitation energy, and uncorrected instrument response changes ratios between set-ups.

**Resolved by.** The relation used cited with its range of validity and its dependence on excitation energy; band widths used to decide which side of the maximum applies; spectra compared on the same substrate, or interference corrected; intensities corrected for instrument response when compared between set-ups; height or area used consistently.

**Benchmark.** [3], [6], [11], [15]

## 8. Infrared measurement geometry and optical effects

**Question.** For infrared spectra, does the paper state the sampling mode (transmission, reflection, transflection, ATR or diffuse reflectance) and the reference spectrum, and does it account for reflection, interference, scattering and, for ATR, penetration depth and dispersion before interpreting band positions or intensities?

**Why it matters.** Absorbance calculated from transmittance counts reflection losses as absorption. In a film on a substrate, interference changes the field inside the layer, so band intensities, shapes and maxima change with thickness and substrate without any change in the material. In ATR, band maxima shift towards the maxima of the refractive index and the effective path grows at low wavenumber, and particles large enough to scatter strongly distort baselines and band shapes in ways that cannot be removed analytically.

**Resolved by.** The sampling mode and reference stated; samples compared in the same geometry, with similar thickness and substrate; reflection and interference modelled, for example with the complex refractive index, or shown to be negligible; ATR spectra corrected or compared only with ATR spectra; claimed shifts larger than those the optics alone can produce.

**Benchmark.** [10]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | R. R. Jones et al., Raman techniques: Fundamentals and frontiers, Nanoscale Res. Lett. 14, 231 (2019) | doi:10.1186/s11671-019-3039-2 |
| 2 | J. E. Lee et al., Optical separation of mechanical strain from charge doping in graphene, Nat. Commun. 3, 1024 (2012) | doi:10.1038/ncomms2022 |
| 3 | A. C. Ferrari and D. M. Basko, Raman spectroscopy as a versatile tool for studying the properties of graphene, Nat. Nanotechnol. 8, 235 (2013); read as arXiv:1306.5856 | doi:10.1038/nnano.2013.46 |
| 4 | H. Malekpour and A. A. Balandin, Raman-based technique for measuring thermal conductivity of graphene and related materials, J. Raman Spectrosc. 49, 106 (2018); read as preprint arXiv:1710.09749, which carries a different title | doi:10.1002/jrs.5230 |
| 5 | S. Guo et al., et al., Comparability of Raman spectroscopic configurations: A large scale cross-laboratory study, Anal. Chem. 92, 15745 (2020) | doi:10.1021/acs.analchem.0c02696 |
| 6 | S. J. Choquette et al., Relative intensity correction of Raman spectrometers: NIST SRMs 2241 through 2243 for 785 nm, 532 nm, and 488 nm/514.5 nm excitation, Appl. Spectrosc. 61, 117 (2007) | doi:10.1366/000370207779947585 |
| 7 | C. A. Lieber and A. Mahadevan-Jansen, Automated method for subtraction of fluorescence from biological Raman spectra, Appl. Spectrosc. 57, 1363 (2003) | doi:10.1366/000370203322554518 |
| 8 | G. Schulze et al., Investigation of selected baseline removal techniques as candidates for automated implementation, Appl. Spectrosc. 59, 545 (2005) | doi:10.1366/0003702053945985 |
| 9 | X. Yuan and R. A. Mayanovic, An empirical study on Raman peak fitting and its application to Raman quantitative research, Appl. Spectrosc. 71, 2325 (2017) | doi:10.1177/0003702817721527 |
| 10 | T. G. Mayerhöfer et al., The Bouguer-Beer-Lambert law: Shining light on the obscure, ChemPhysChem 21, 2029 (2020) | doi:10.1002/cphc.202000464 |
| 11 | X. Zhang et al., Phonon and Raman scattering of two-dimensional transition metal dichalcogenides from monolayer, multilayer to bulk material, Chem. Soc. Rev. 44, 2757 (2015); read as arXiv:1502.00701 | doi:10.1039/c4cs00282b |
| 12 | Bilbao Crystallographic Server, SAM: Symmetry Adapted Modes, program description page (accessed 2026); program described in E. Kroumova et al., Phase Transitions 76, 155 (2003) | https://www.cryst.ehu.eus/rep/sam.html |
| 13 | G. Gouadec and P. Colomban, Raman spectroscopy of nanostructures and nanosized materials, J. Raman Spectrosc. 38, 598 (2007); arXiv:0706.0775 | doi:10.1002/jrs.1749 |
| 14 | M. A. Pimenta et al., Polarized Raman spectroscopy in low-symmetry 2D materials: angle-resolved experiments and complex number tensor elements, Phys. Chem. Chem. Phys. 23, 27103 (2021) | doi:10.1039/d1cp03626b |
| 15 | L. G. Cançado et al., Quantifying defects in graphene via Raman spectroscopy at different excitation energies, Nano Lett. 11, 3190 (2011); arXiv:1105.0175 | doi:10.1021/nl201432g |
