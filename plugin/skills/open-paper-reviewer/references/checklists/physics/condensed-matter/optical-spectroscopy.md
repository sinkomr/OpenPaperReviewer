---
id: T-OPTICAL-SPECTROSCOPY
name: Optical absorption, reflectivity and ellipsometry
type: technique
field: physics/condensed-matter
applies_when: the paper reports optical absorption, transmission or diffuse reflectance, a band gap from an absorption edge or Tauc plot, reflectivity with Kramers-Kronig analysis, spectroscopic ellipsometry, optical conductivity or terahertz spectra, or bases a claim about optical constants, carrier response or spectral weight on them
version: "0.1"
---

# Optical absorption, reflectivity and ellipsometry

## 1. Absorbance versus absorption coefficient

**Question.** Does the paper state how the absorption spectrum was obtained (transmission alone, transmission with reflection, or diffuse reflectance with a stated transform) and how reflection, scattering, substrate and thin-film interference were dealt with in computing the absorption coefficient?

**Why it matters.** Absorbance calculated from transmitted intensity counts reflection and scattering losses as absorption. In a film on a substrate, interference changes the field inside the layer, so band intensities, shapes and apparent positions can change with thickness, substrate or geometry without any change in the material. For powders, scattering cannot be neglected, and the usual diffuse-reflectance transform assumes an optically thick layer measured against a white standard.

**Resolved by.** The measurement geometry and the reference are given; reflection and scattering are measured or modelled rather than folded into the absorbance; the film thickness is measured and interference treated with an optical model or shown to be negligible; for powders, the reflectance standard, the layer thickness and the transform used are stated.

**Benchmark.** [1], [2]

## 2. Band gap from the absorption edge

**Question.** Is the procedure used to extract a band gap (type of plot, exponent, fitted energy range, baseline) stated and justified for the material, is the fit shown, and does the paper consider whether excitons, band tails, defect absorption, a second phase, quantum confinement or heavy doping shape the edge?

**Why it matters.** The Tauc construction was devised for amorphous semiconductors and its crystalline variants assume a single transition between parabolic bands, with an exponent fixed by the transition type. Excitonic absorption, Urbach tails, defect bands, overlapping direct and indirect transitions, confinement and band filling all change the edge, so the plot can return a value with no clear meaning. Sub-gap absorption from another phase makes extrapolation to the energy axis underestimate the gap, and the value moves with the energy range chosen for the linear fit.

**Resolved by.** The plot and the fitted range are shown; the exponent is supported by independent knowledge of the transition type; sub-gap absorption is handled with a baseline or by separating components; excitonic or band-filling contributions are discussed where the material makes them likely, and where the edge is not a single band-to-band transition an optical gap is defined by a stated procedure and compared only with gaps defined the same way; the quoted uncertainty covers the dependence on fitting range and on how the absorption coefficient was computed.

**Benchmark.** [2], [3], [4]

## 3. Absolute reflectance

**Question.** How was the reflectance put on an absolute scale (reference mirror, in situ metal coating of the sample, or another method), and what does the paper do about sample size, surface quality and differences in position between sample and reference?

**Why it matters.** Reflectance is measured relative to a reference, and a small, irregular or rough sample scatters light out of the detected beam, so the measured ratio is lower than the specular reflectance by an amount that depends on frequency. Errors in absolute level pass directly into the optical constants derived from the reflectance.

**Resolved by.** The reference and the procedure for exchanging sample and reference are described; geometric and scattering losses are corrected, for example by coating the sample in situ with gold or aluminium and remeasuring; the sample size is compared with the beam and the effect of diffraction at long wavelengths is estimated.

**Benchmark.** [5]

## 4. Kramers-Kronig analysis and extrapolations

**Question.** For optical constants obtained by KK analysis of reflectance or transmission, does the paper state the measured range, the low- and high-frequency extrapolations and their parameters, and show how the results that carry a claim change when the extrapolations are varied?

**Why it matters.** The KK integral runs from zero to infinite frequency, while data cover a finite range, so the result depends on the extrapolations. The high-frequency extension in particular is often a power law with an arbitrary exponent, and changing it can alter the conductivity over the whole measured range by a large factor and change partial sum rules. The standard phase relation also holds only for normal-incidence reflection from a thick sample, not for thin films or oblique incidence.

**Resolved by.** The extrapolations are given with their parameters; the low-frequency extension is tied to an independent measurement such as the dc resistivity; the high-frequency extension uses ellipsometry over an overlapping range or calculated atomic scattering functions instead of a free power law; the sensitivity of the claimed features to these choices is shown; for films or multilayers, a method that models the full structure is used.

**Benchmark.** [6], [7], [8]

## 5. Ellipsometry model and fit

**Question.** For spectroscopic ellipsometry, does the paper give the layer model (substrate, layers, roughness or overlayers, interfaces), the dispersion model for each layer, the figure of merit of the fit, and the uncertainties and correlations of the fitted parameters?

**Why it matters.** Ellipsometry measures ratios of reflection coefficients, not thickness or optical constants, which are obtained only by fitting a model of the near-surface region. Without a statistical measure of fit it is not known whether the model fits, and fitted parameters can be correlated, so some are not determined by the data. A rough surface layer and an oxide overlayer can be confused unless spectroscopic data separate them, and a dispersion model that is not KK-consistent, or that is too restrictive, can distort the optical constants.

**Resolved by.** The full model is stated, with which parameters were fitted and which fixed; the measured and calculated spectra are shown with a statistical figure of merit; confidence limits and correlation coefficients are reported; the dispersion model obeys KK consistency and the physical limits of the material; thickness or roughness is checked against an independent measurement or constrained by several angles, samples or techniques.

**Benchmark.** [7], [9]

## 6. Polarisation and anisotropy

**Question.** For a material that is not optically isotropic, does the paper state the polarisation of the light relative to the crystal axes and the plane of incidence, and treat the response as a tensor rather than as a single isotropic function?

**Why it matters.** In anisotropic materials the optical constants are tensors, and an applied magnetic field adds off-diagonal components. Data taken with unknown or mixed polarisation, or analysed with an isotropic model, combine different components; an anisotropic sample needs a 4×4 matrix treatment, as in generalised ellipsometry, and simple linear-dichroism models are inadequate for strongly absorbing solids.

**Resolved by.** Sample orientation and polarisation are stated for each spectrum; separate spectra along the principal axes, or generalised or Mueller-matrix ellipsometry, determine the components; the analysis uses an anisotropic layer model where needed.

**Benchmark.** [1], [8]

## 7. Terahertz transmission and its extraction

**Question.** For THz-TDS, does the paper describe the reference (bare substrate or open aperture), the sample and substrate thicknesses, how echoes from multiple reflections were handled, the formula used to extract the conductivity or refractive index and the conditions under which it holds, and the frequency range in which the signal is well above the noise?

**Why it matters.** The conductivity is extracted from the ratio of sample and reference transmission through a model of the layers, so differences between the reference and sample substrates, errors in thickness, and echoes in thin layers or substrates enter the result directly. The thin-film approximation holds only for a layer that is optically thin, much thinner than the wavelength in the material, and a composite of nanostructures and voids needs an effective-medium treatment. The largest absorption that can be measured is set by the dynamic range in transmission, and by scan-to-scan reproducibility in reflection.

**Resolved by.** The reference measurement and the extraction formula are stated with their assumptions checked; thicknesses are measured; echoes are windowed or included in the model; for composite samples the filling factor and effective-medium model are given; the usable bandwidth and dynamic range are shown, and claims rest only on the part of the spectrum within them.

**Benchmark.** [10], [11]

## 8. Conductivity models and spectral weight

**Question.** When carrier density, scattering rate, mobility, localisation or a change of spectral weight is inferred from an optical or THz conductivity, does the paper state the model and the frequency range of each fit, consider alternative models, and give the integration cut-off for any spectral weight and how the result depends on it?

**Why it matters.** Drude-Lorentz fits restrict the conductivity to an assumed form, and phenomenological extensions such as the Drude-Smith model fit many non-Drude spectra but have parameters whose physical meaning is uncertain; a plasmon model can give the same spectra. Spectral-weight changes can come from the choice of cut-off, because intraband and interband contributions often overlap, and not only from a change in the electronic state.

**Resolved by.** Both real and imaginary parts are fitted over a stated range; the number of free parameters is stated and their uncertainties given; alternative models (Drude, Drude-Smith, plasmon, effective-medium) are compared and the choice justified physically; spectral weight is shown as a function of cut-off frequency, and conclusions hold across reasonable choices.

**Benchmark.** [7], [8], [10], [12]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | T. G. Mayerhöfer et al., The Bouguer-Beer-Lambert law: Shining light on the obscure, ChemPhysChem 21, 2029 (2020) | doi:10.1002/cphc.202000464 |
| 2 | A. Escobedo-Morales et al., Automated method for the determination of the band gap energy of pure and mixed powder samples using diffuse reflectance spectroscopy, Heliyon 5, e01505 (2019) | doi:10.1016/j.heliyon.2019.e01505 |
| 3 | A. R. Zanatta, Revisiting the optical bandgap of semiconductors and the proposal of a unified methodology to its determination, Sci. Rep. 9, 11225 (2019) | doi:10.1038/s41598-019-47670-y |
| 4 | J. Klein et al., Limitations of the Tauc plot method, Adv. Funct. Mater. 33, 2304523 (2023) | doi:10.1002/adfm.202304523 |
| 5 | C. C. Homes et al., Technique for measuring the reflectance of irregular, submillimeter-sized samples, Appl. Opt. 32, 2976 (1993) | doi:10.1364/AO.32.002976 |
| 6 | D. B. Tanner, Use of x-ray scattering functions in Kramers-Kronig analysis of reflectance, Phys. Rev. B 91, 035123 (2015); read as preprint arXiv:1411.2061 | doi:10.1103/PhysRevB.91.035123 |
| 7 | A. B. Kuzmenko, Kramers-Kronig constrained variational analysis of optical spectra, Rev. Sci. Instrum. 76, 083108 (2005); read as preprint arXiv:cond-mat/0503565 | doi:10.1063/1.1979470 |
| 8 | D. N. Basov et al., Electrodynamics of correlated electron materials, Rev. Mod. Phys. 83, 471 (2011); read as preprint arXiv:1106.2309 | doi:10.1103/RevModPhys.83.471 |
| 9 | D. E. Aspnes et al., Investigation of effective-medium models of microscopic surface roughness by spectroscopic ellipsometry, Phys. Rev. B 20, 3292 (1979) | doi:10.1103/PhysRevB.20.3292 |
| 10 | H. J. Joyce et al., A review of the electrical properties of semiconductor nanowires: insights gained from terahertz conductivity spectroscopy, Semicond. Sci. Technol. 31, 103003 (2016) | doi:10.1088/0268-1242/31/10/103003 |
| 11 | P. U. Jepsen and B. M. Fischer, Dynamic range in terahertz time-domain transmission and reflection spectroscopy, Opt. Lett. 30, 29 (2005) | doi:10.1364/OL.30.000029 |
| 12 | T. L. Cocker et al., Microscopic origin of the Drude-Smith model, Phys. Rev. B 96, 205439 (2017); read as preprint arXiv:1705.10350 | doi:10.1103/PhysRevB.96.205439 |
