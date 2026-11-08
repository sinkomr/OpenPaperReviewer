---
id: T-EXOPLANET-ATMOSPHERES
name: Exoplanet atmospheres
type: technique
field: physics/astrophysics
applies_when: the paper reports a transmission, emission or high-resolution cross-correlation spectrum of an exoplanet, or bases a claim about atmospheric composition, a molecular detection, abundances, metallicity, clouds or temperature structure on such spectra or on an atmospheric retrieval
version: "0.1"
---

# Exoplanet atmospheres

## 1. Light-curve systematics and fitting choices

**Question.** How were instrument systematics modelled in the white-light and spectroscopic light curves, how were limb darkening and the orbital parameters treated in each wavelength bin, and does the paper show that the spectrum does not depend on these choices?

**Why it matters.** The transit or eclipse depth in each bin is fitted together with a model of detector and pointing systematics, and different systematic models that fit the data comparably well can give spectra of different shape and size of uncertainty. Limb-darkening coefficients fixed to stellar-model values or described by an inadequate law can bias the planet-to-star radius ratio by amounts larger than the quoted precision. Molecular inferences from early low-resolution spectra have been revised in later analyses as the systematics became better understood.

**Resolved by.** The systematic model stated and justified, ideally with the spectrum marginalised over a set of plausible models or shown to be stable across them; the limb-darkening law and whether its coefficients were fitted or fixed, with a test of the effect; orbital parameters fixed consistently across bins and their source stated; the raw and detrended white-light curves and residuals shown; agreement between independent reductions of the same data.

**Benchmark.** [1], [2], [3]

## 2. Contamination by the host star

**Question.** Does the paper estimate how unocculted starspots and faculae, and spots crossed by the planet, could change the transit depth with wavelength, and does it test whether stellar contamination alone could produce the claimed features?

**Why it matters.** Spots and faculae make the light passing through the planet's atmosphere differ from the disc-integrated starlight, and this imprints false features on the transmission spectrum, most strongly for small planets around cool, active stars. On cool stars the active regions themselves carry molecular bands that resemble a planetary signal, and the contamination can exceed the expected atmospheric signal by a large factor. Spots crossed by the planet change the transit depth too, and removing the crossings from the light curve does not fully remove their effect. Corrections from rotational variability alone give only a lower limit on the heterogeneity.

**Resolved by.** Stellar activity indicators and variability reported for the epoch of observation; occulted spot crossings identified in the light curves and handled; a retrieval or model comparison that includes stellar heterogeneity as free parameters alongside the planetary atmosphere, with the result for the atmospheric claim reported; repeated transits at different epochs or broad wavelength coverage used to separate stellar from planetary signals.

**Benchmark.** [3], [4], [5]

## 3. Retrieval model, priors and opacities

**Question.** Does the paper state the retrieval's forward model and priors in full (which species, cloud and haze treatment, temperature profile, prior ranges and opacity sources), and does it show how the main conclusions change under reasonable alternative choices?

**Why it matters.** Retrieved abundances depend on what the model includes. Omitting collision-induced absorption can shift a retrieved water abundance by orders of magnitude, a clear-sky assumption narrows constraints without justification, and the treatment of line broadening and the completeness of line lists change the forward spectrum. Different retrieval codes given the same high-precision spectrum can disagree by several standard deviations, and the Bayesian evidence used for model comparison depends on the prior ranges.

**Resolved by.** A table of free parameters with their priors; the opacity sources, line lists and broadening treatment stated; a sensitivity test showing that the headline abundances or detections survive changes to the cloud model, temperature profile, included species and priors; where possible, a comparison with a second retrieval code or a self-consistent model grid; detections shown to survive leaving out individual data points or instruments, for example by leave-one-out cross-validation.

**Benchmark.** [6], [7], [8]

## 4. Degeneracies between clouds, composition and mean molecular weight

**Question.** When the paper infers metallicity, mean molecular weight or an abundance from the size of spectral features, does it show that clouds or hazes, including partial cloud cover at the terminator, cannot produce the same spectrum, does its wavelength coverage break the degeneracy, and is the planet's mass known well enough for the inference?

**Why it matters.** Muted features can arise from a low abundance, a high-altitude cloud deck or a heavy atmosphere with a small scale height. Patchy terminator clouds can reproduce the spectrum of a high mean molecular weight atmosphere almost exactly over a narrow near-infrared band, and a fully cloudy deck makes the abundance of the main absorber degenerate with the cloud-top pressure. Near-infrared data alone often leave these possibilities equally probable. The mass sets the surface gravity and so the scale height, and for most planets other than low-metallicity gas giants a poorly known mass can dominate the uncertainty of the inferred atmospheric properties.

**Resolved by.** Retrievals that allow non-uniform cloud cover and report the competing solutions; posterior distributions shown in full, including correlations between abundance, cloud parameters and reference radius; optical data showing the scattering slope, or longer-wavelength features from other molecules, used to separate the scenarios; the planet's mass and its uncertainty stated and carried into the retrieval; a claim of high metallicity or a cloud-free atmosphere stated only where the alternatives are disfavoured.

**Benchmark.** [3], [6], [9], [11]

## 5. Emission spectra and thermal structure

**Question.** For claims based on emission spectra, does the paper show that its temperature-profile model, including any assumption of a single one-dimensional profile, does not drive the retrieved abundances or the claimed thermal inversion?

**Why it matters.** Emission spectra depend on both temperature structure and composition, and the two trade off against each other unless the data are precise. An emitting hemisphere with strong horizontal temperature contrast, fitted with a single profile, can return abundances that are tightly constrained yet several standard deviations from the truth, and a poor-fitting model can give implausibly small uncertainties. Temperature profiles, including claimed thermal inversions, constrained only by a few broadband photometric points are less secure than those constrained by spectra.

**Resolved by.** The temperature-profile parameterisation stated and its flexibility justified; a comparison with models that include more than one thermal profile where the data support it; abundance and inversion claims shown to survive these alternatives; the wavelength coverage and the bands driving the temperature constraint identified.

**Benchmark.** [3], [10]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | H. R. Wakeford et al., Marginalizing instrument systematics in HST WFC3 transit light curves, Astrophys. J. 819, 10 (2016); read as preprint arXiv:1601.02587 | doi:10.3847/0004-637X/819/1/10 |
| 2 | N. Espinoza and A. Jordán, Limb darkening and exoplanets: testing stellar model atmospheres and identifying biases in transit parameters, Mon. Not. R. Astron. Soc. 450, 1879 (2015); read as preprint arXiv:1503.07020 | doi:10.1093/mnras/stv744 |
| 3 | N. Madhusudhan, Exoplanetary atmospheres: key insights, challenges, and prospects, Annu. Rev. Astron. Astrophys. 57, 617 (2019); read as preprint arXiv:1904.03190 | doi:10.1146/annurev-astro-081817-051846 |
| 4 | B. V. Rackham et al., The transit light source effect: false spectral features and incorrect densities for M-dwarf transiting planets, Astrophys. J. 853, 122 (2018); read as preprint arXiv:1711.05691 | doi:10.3847/1538-4357/aaa08c |
| 5 | B. V. Rackham et al., The effect of stellar contamination on low-resolution transmission spectroscopy: needs identified by NASA's Exoplanet Exploration Program Study Analysis Group 21, RAS Tech. Instrum. 2, 148 (2023) | doi:10.1093/rasti/rzad009 |
| 6 | L. Welbanks and N. Madhusudhan, On degeneracies in retrievals of exoplanetary transmission spectra, Astron. J. 157, 206 (2019); read as preprint arXiv:1904.05356 | doi:10.3847/1538-3881/ab14de |
| 7 | J. K. Barstow et al., A comparison of exoplanet spectroscopic retrieval tools, Mon. Not. R. Astron. Soc. 493, 4884 (2020); read as preprint arXiv:2002.01063 | doi:10.1093/mnras/staa548 |
| 8 | L. Welbanks et al., On the application of Bayesian leave-one-out cross-validation to exoplanet atmospheric analysis, Astron. J. 165, 112 (2023); read as preprint arXiv:2212.03872 | doi:10.3847/1538-3881/acab67 |
| 9 | M. R. Line and V. Parmentier, The influence of nonuniform cloud cover on transit transmission spectra, Astrophys. J. 820, 78 (2016); read as preprint arXiv:1511.09443 | doi:10.3847/0004-637X/820/1/78 |
| 10 | Y. K. Feng et al., The impact of non-uniform thermal structure on the interpretation of exoplanet emission spectra, Astrophys. J. 829, 52 (2016); read as preprint arXiv:1607.03230 | doi:10.3847/0004-637X/829/1/52 |
| 11 | N. E. Batalha et al., The precision of mass measurements required for robust atmospheric characterization of transiting exoplanets, Astrophys. J. Lett. 885, L25 (2019); read as preprint arXiv:1910.00076 | doi:10.3847/2041-8213/ab4909 |
