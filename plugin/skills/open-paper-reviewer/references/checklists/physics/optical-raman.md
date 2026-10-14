---
id: T-OPTICAL-RAMAN
name: Optical and Raman spectroscopy of solids and nanomaterials
type: technique
field: physics
applies_when: the paper bases a claim on optical absorption or reflectance, photoluminescence or Raman spectra of a solid, thin film or nanomaterial, for example a band gap, a quantum yield, the assignment of an emission band, or a layer number, strain, doping level or defect density read from Raman bands
version: "0.1"
---

# Optical and Raman spectroscopy of solids and nanomaterials

Absorption, photoluminescence and Raman spectra are used to claim band gaps, emission efficiencies and the nature of emitting states, and to infer layer number, strain, doping, defect density, composition or temperature from the positions, widths and intensities of spectral bands. Each of these is an inference from light collected through a particular instrument, from a particular sample geometry, under illumination that can itself change the sample.

## 1. Absorbance versus absorption

**Question.** Does the paper state how the absorption spectrum was obtained (transmission alone, transmission with reflection, or diffuse reflectance with a stated transform) and how reflection, scattering and thin-film interference were dealt with?

**Why it matters.** Absorbance calculated from transmitted intensity counts reflection and scattering losses as absorption. In a film on a substrate, interference changes the field inside the layer, so band intensities, shapes and apparent positions can change with thickness, substrate or measurement geometry without any change in the material.

**Resolved by.** The measurement geometry and the reference are given, reflection and scattering are measured or modelled rather than folded into the absorbance, interference in films is treated with an optical model or shown to be negligible, and for powders the reflectance transform, its assumptions and the formula used for the absorption coefficient are stated.

**Benchmark.** [1], [2], [3]

## 2. Band gap from the absorption edge

**Question.** Is the procedure used to extract a band gap (type of plot, exponent, fitted energy range, baseline) stated and justified for the material, and is the fit shown?

**Why it matters.** The exponent in a Tauc-type plot presupposes the kind of transition, and the construction was devised for amorphous semiconductors. Absorption below the gap from defects, dopants, surface species or a second component distorts the plot so that a direct extrapolation gives a gap that is too small, which can be read as band-gap narrowing; the value also moves with the energy range chosen for the linear fit.

**Resolved by.** The plot and the fitted range are shown, the exponent is supported by independent knowledge of the transition type, sub-gap absorption is handled with a baseline or by separating the spectral components, and the quoted uncertainty covers the dependence on fitting range and on how the absorption coefficient was computed.

**Benchmark.** [2], [3]

## 3. Emission spectra and quantum yields

**Question.** Were emission spectra corrected for the wavelength-dependent response of the detection system and checked for spurious peaks, and is any quantum yield given with its method (relative to a named standard, or absolute), the sample absorbance and an uncertainty?

**Why it matters.** Detection responsivity varies strongly with wavelength, so the shape, peak position and intensity ratios of an uncorrected spectrum are specific to the instrument, and second-order diffraction of the excitation light or Raman scattering from a solvent or matrix can appear as emission peaks. In optically dense samples the excitation is attenuated and the emission reabsorbed, which changes intensity and spectral shape; a relative quantum yield also carries the uncertainty of its standard, and few standards are well established.

**Resolved by.** The correction method and its reference (calibrated lamp or certified standard) are stated, blank or substrate spectra are shown, the absorbance at the excitation wavelength is given and kept low or reabsorption is corrected, and the quantum yield is reported with its method, its standard and an uncertainty in line with what such methods achieve.

**Benchmark.** [4], [5], [6]

## 4. Origin of an emission band

**Question.** Is the assignment of an emission band (band edge, free or bound exciton, defect level) supported by its dependence on excitation power, over a stated range and at a stated temperature, rather than by its energy alone?

**Why it matters.** Excitonic and defect-related transitions follow different power laws in excitation intensity, and this is the usual way of telling them apart. The exponent is not a constant, however: it changes when defect levels saturate and depends on the excitation wavelength, so a slope taken over a narrow range, or a single spectrum, can support more than one assignment.

**Resolved by.** Emission intensity against excitation power is shown over several orders of magnitude with the fitted exponents and any crossover, the excitation wavelength and temperature are given, and the assignment is consistent with the model used to interpret the exponent.

**Benchmark.** [7], [8]

## 5. Changes caused by the excitation light

**Question.** Are the excitation wavelength, the power at the sample, the spot size and the exposure time given, and is it shown that the spectra do not change with power or exposure?

**Why it matters.** A focused laser can heat, bleach or damage a sample. Raman peak positions and widths depend on temperature, and emission intensity, sometimes even spectral shape, changes with exposure and temperature, so a shift or an intensity change can be produced by the measurement itself.

**Resolved by.** Power density and exposure are reported, spectra taken at several powers or repeated on the same spot are shown to agree, or the dependence is measured and the reported values are taken where it is negligible.

**Benchmark.** [4], [9], [10], [11], [12]

## 6. Raman shift calibration and resolution

**Question.** How was the Raman shift axis calibrated (reference lines or standards, order of the calibration function, how often), what is the spectral resolution, and how do both compare with the shifts or width changes that are claimed?

**Why it matters.** A linear wavelength calibration of a single-grating spectrograph can leave errors of several wavenumbers, more than the instrument linewidth, and drift of the laser wavelength moves every peak. The same sample measured on different instruments gives different peak positions, widths and intensities, so small differences between spectra taken on different setups or on different days may be instrumental.

**Resolved by.** The calibration lines and procedure are given, accuracy and repeatability are demonstrated on a reference material, the spectral resolution is stated, and the claimed shifts exceed the demonstrated accuracy.

**Benchmark.** [11], [12], [13]

## 7. One cause or several for a Raman shift

**Question.** When a change in peak position, width or shape is attributed to one cause (strain, doping, temperature, disorder, layer number, particle size), does the paper exclude the others or separate them?

**Why it matters.** Strain and charge both shift the same phonon modes, so neither can be read from one peak position without knowledge of the other; temperature, defects, chemical change and distributions of size or shape act on the same observables. A single spectral signature is seldom unique: a line shape taken as the mark of a single layer, for instance, can also arise from decoupled or misoriented multilayers.

**Resolved by.** Two or more modes are analysed together (for example by correlating their shifts), widths and intensities are used alongside positions, an independent measurement fixes one of the variables (thickness, carrier density, temperature), and the alternatives that remain are stated.

**Benchmark.** [9], [11], [14]

## 8. Raman intensity ratios as quantitative measures

**Question.** When an intensity ratio is used to quantify defect density, crystallite size, layer number or doping, are the excitation wavelength, the substrate and the definition of intensity (peak height or area) given, and is the calibration relation valid for those conditions and for that range?

**Why it matters.** For a given defect density the ratio of a defect-activated band to an allowed band depends strongly on the excitation energy, and with increasing disorder it passes through a maximum, so one value can correspond to two different defect densities; relations for point defects and for crystallite size differ, and some defects give no signal at all. Interference in the substrate changes relative band intensities with substrate and wavelength even for the same sample.

**Resolved by.** The relation used is cited with its range of validity and includes the excitation energy, peak widths are used to decide which side of the maximum applies, the spectra compared were taken on the same substrate or interference is corrected, and height or area is used consistently.

**Benchmark.** [9], [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | T. G. Mayerhöfer, S. Pahlow and J. Popp, The Bouguer-Beer-Lambert law: Shining light on the obscure, ChemPhysChem 21, 2029–2046 (2020) | doi:10.1002/cphc.202000464 | full text | Abstract and Secs. 2, 2.1 and 2.2: band shifts and intensity changes can arise purely from the measurement method, the substrate and the form of the sample; absorbance from transmittance includes reflection losses; interference in a layer on a substrate alters band intensities, shapes and positions with thickness; scattering is a further cause of deviation that cannot be removed analytically. |
| 2 | P. Makuła, M. Pacia and W. Macyk, How to correctly determine the band gap energy of modified semiconductor photocatalysts based on UV–Vis spectra, J. Phys. Chem. Lett. 9, 6814–6817 (2018) | doi:10.1021/acs.jpclett.8b02892 | full text | Whole Viewpoint (Eqs. 1 to 3, Figs. 1 to 4): the Tauc exponent depends on the type of transition; diffuse reflectance is converted with the Kubelka-Munk function, defined for an infinitely thick specimen; sub-gap absorption introduced by defects, dopants or surface modification makes a direct extrapolation underestimate the gap; a baseline or a separation of components corrects this. |
| 3 | A. R. Zanatta, Revisiting the optical bandgap of semiconductors and the proposal of a unified methodology to its determination, Sci. Rep. 9, 11225 (2019) | doi:10.1038/s41598-019-47670-y | full text | Introduction, subsection "Optical absorption and optical bandgap": the Tauc construction was formulated for amorphous semiconductors yet is routinely applied to crystalline or heavily doped ones; gap values depend on how the absorption coefficient was obtained (measurement details, thickness, formula) and differ by many meV with the range chosen for the linear fit. |
| 4 | P. C. DeRose, Recommendations and guidelines for standardization of fluorescence spectroscopy, NISTIR 7457, National Institute of Standards and Technology (2007) | doi:10.6028/NIST.IR.7457 | full text | Sec. 3.1: wavelength-dependent responsivity changes the shape of a measured emission spectrum, and a grating passes second-order light. Sec. 3.2: inner-filter effects and reabsorption in optically dense samples; photobleaching limits the reproducibility of intensity and sometimes of spectral shape; intensity depends on temperature; Raman peaks of the solvent or matrix appear in emission spectra. Sec. 5.5: spectral correction, by calibrated source or certified reference material, is needed for true band shape, peak position and intensity ratios. |
| 5 | A. M. Brouwer, Standards for photoluminescence quantum yield measurements in solution (IUPAC Technical Report), Pure Appl. Chem. 83, 2213–2228 (2011) | doi:10.1351/PAC-REP-10-09-31 | abstract | Abstract: only three quantum-yield standards are regarded as well established and six more have been examined by several independent groups; many others in common use are of less certain validity, and standards for the ultraviolet, the near infrared and for low yields are lacking. |
| 6 | C. Würth, M. Grabolle, J. Pauli, M. Spieles and U. Resch-Genger, Relative and absolute determination of fluorescence quantum yields of transparent samples, Nat. Protoc. 8, 1535–1550 (2013) | doi:10.1038/nprot.2013.087 | abstract | Abstract: relative determination uses a conventional spectrometer and a standard, absolute determination a calibrated integrating sphere; the protocol addresses the typical sources of uncertainty, and with assessed standards uncertainties of 5 to 10 per cent are achievable for transparent solutions. |
| 7 | T. Schmidt, K. Lischka and W. Zulehner, Excitation-power dependence of the near-band-edge photoluminescence of semiconductors, Phys. Rev. B 45, 8989–8994 (1992) | doi:10.1103/PhysRevB.45.8989 | abstract | Abstract: near-band-edge emission intensity follows a power law in excitation power, with an exponent between 1 and 2 for excitonic lines and with model relations linking the exponents of free-exciton, bound-exciton and free-to-bound transitions; the law fails when the power is varied over more than two decades, and the exponent changes with excitation wavelength. |
| 8 | C. Spindler, T. Galvani, L. Wirtz, G. Rey and S. Siebentritt, Excitation-intensity dependence of shallow and deep-level photoluminescence transitions in semiconductors, J. Appl. Phys. 126, 175703 (2019) | doi:10.1063/1.5095235 | abstract | Abstract: the dependence on excitation intensity at low temperature is the usual means of distinguishing excitonic from defect-related transitions; the exponent takes multiples of one half according to the recombination channels available, and saturation of defect levels produces crossovers from one power law to another. |
| 9 | A. C. Ferrari and D. M. Basko, Raman spectroscopy as a versatile tool for studying the properties of graphene, Nat. Nanotechnol. 8, 235–246 (2013); arXiv:1306.5856 | doi:10.1038/nnano.2013.46 | full text | Read in the arXiv version, which includes the supplementary notes; sections cited by title. "Number and relative orientation of layers": a single-component 2D line is not proof of a single layer. "Defects and disorder": the D to G ratio depends on excitation energy, is non-monotonic in disorder, and some defects are Raman-silent. "Effect of perturbations" with the supplementary notes on temperature and on interference-enhanced scattering: strain, doping, field and temperature all change positions and widths, and substrate interference changes band ratios with substrate and wavelength. |
| 10 | L. G. Cançado, A. Jorio, E. H. Martins Ferreira, F. Stavale, C. A. Achete, R. B. Capaz, M. V. O. Moutinho, A. Lombardo, T. S. Kulmala and A. C. Ferrari, Quantifying defects in graphene via Raman spectroscopy at different excitation energies, Nano Lett. 11, 3190–3196 (2011); arXiv:1105.0175 | doi:10.1021/nl201432g | full text | Abstract, Introduction and Figs. 4 and 5: the D to G intensity ratio at fixed defect density depends strongly on laser energy and peaks near 3 nm defect spacing, so one value fits two densities unless the G width is used; ratios of height and of area are distinguished, as are point defects and crystallite size. Experimental paragraph of the results section: laser power and spot size are stated, with the power kept low to avoid heating. |
| 11 | J. E. Lee, G. Ahn, J. Shim, Y. S. Lee and S. Ryu, Optical separation of mechanical strain from charge doping in graphene, Nat. Commun. 3, 1024 (2012) | doi:10.1038/ncomms2022 | full text | Introduction: strain and charge both shift the G and 2D modes, so neither can be determined without the other unless the two modes are correlated. Methods, "Spectral accuracy of the Raman measurements": a linear calibration left errors of several wavenumbers, exceeding the instrument linewidth, with a caution about comparing frequencies between spectrographs; accuracy was checked on graphite. Methods, "Raman spectroscopy": power and spot size given, and no irreversible photoinduced change observed. |
| 12 | R. R. Jones, D. C. Hooper, L. Zhang, D. Wolverson and V. K. Valev, Raman techniques: Fundamentals and frontiers, Nanoscale Res. Lett. 14, 231 (2019) | doi:10.1186/s11671-019-3039-2 | full text | Section "Experimental considerations", subsection "Instrumentation": drift of the laser wavelength shifts the Raman peaks and hinders comparison between measurements; spectral resolution is set by slit width, focal length, grating and detector; high laser power can bleach or damage the sample. |
| 13 | S. Guo, C. Beleites, U. Neugebauer, et al., Comparability of Raman spectroscopic configurations: A large scale cross-laboratory study, Anal. Chem. 92, 15745–15756 (2020) | doi:10.1021/acs.analchem.0c02696 | abstract | Abstract: the same samples measured on 35 instruments in 15 institutes gave spectra that differed in peak position, intensity, peak width and noise level. |
| 14 | G. Gouadec and P. Colomban, Raman spectroscopy of nanostructures and nanosized materials, J. Raman Spectrosc. 38, 598–603 (2007); arXiv:0706.0775 | doi:10.1002/jrs.1749 | abstract | Abstract: chemical reactions, size or shape distribution, defects, strain and coupling effects can all contribute, alongside nanoscale dimension, to the Raman signature of a nanomaterial. |
