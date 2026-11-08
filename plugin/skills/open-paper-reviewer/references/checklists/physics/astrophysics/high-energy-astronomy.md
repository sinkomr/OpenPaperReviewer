---
id: T-HIGH-ENERGY-ASTRONOMY
name: X-ray and gamma-ray astronomy
type: technique
field: physics/astrophysics
applies_when: the paper analyses photon-counting data from an X-ray or gamma-ray telescope, or a ground-based Cherenkov telescope, and bases a claim on a source detection, flux, spectrum, spectral line, extension or upper limit derived from event counts and instrument responses
version: "0.1"
---

# X-ray and gamma-ray astronomy

## 1. Background estimation and screening

**Question.** How was the background estimated (from which regions, observations or model), are the background regions free of source emission and matched to the source region in detector response, and were periods of high or flaring background found and removed?

**Why it matters.** Space-borne X-ray detectors record a particle-induced background, with fluorescence lines from detector materials whose strength varies across the detector, and flares of soft protons that vary rapidly, differ between cameras and raise the background inside the field of view. Cherenkov telescopes see gamma rays against a far larger background of cosmic-ray showers, normalised by an acceptance that depends on position in the field, zenith angle and energy. A background region that contains extended emission or a nearby source, or whose acceptance differs from that of the source region, over- or under-subtracts.

**Resolved by.** Source and background regions shown on the image, with their sizes and offsets and the normalisation factor between them; background taken at a comparable detector position, or modelled, so that instrumental lines and gradients cancel; known sources and extended emission excluded from the background regions; background light curves shown with the screening threshold and the exposure removed; for Cherenkov telescopes, the background method named and the result compared with a second method whose systematics differ; the background spectrum shown alongside the source spectrum.

**Benchmark.** [1], [2], [3]

## 2. Effective area, energy scale and point-spread function

**Question.** Which calibration version and response files were used, how large are their stated systematic uncertainties in effective area, energy scale and PSF, and were these uncertainties carried into the fluxes, spectral parameters and source sizes on which the claims rest?

**Why it matters.** Response functions come from simulations and ground calibration corrected with flight data, and residual uncertainties remain in the effective area, in the PSF containment radii and in the absolute energy scale, which for one widely used gamma-ray instrument carries an uncertainty of a few per cent. Different observatories disagree in flux normalisation by up to 10 to 15 per cent in some bands, and in spectral slope, so a joint fit with a fixed cross-normalisation can bias the result. Ignoring calibration uncertainty understates error bars and can bias fitted parameters.

**Resolved by.** The calibration database version and response files named; the effective-area and energy-scale uncertainties propagated, for example by repeating the analysis with bracketing responses or by sampling plausible calibration files; in fits that combine instruments, cross-normalisation constants left free and compared with published values; a claimed extension compared with the PSF measured on calibration sources at the same energy and detector position.

**Benchmark.** [3], [4], [5], [6], [19]

## 3. Source confusion and diffuse emission

**Question.** Could neighbouring sources within the PSF, unresolved sources or an imperfect model of diffuse emission contribute to the counts attributed to the source, and does the paper show how the result changes when the diffuse model or the list of nearby sources is changed?

**Why it matters.** The PSF of X-ray mirrors broadens with off-axis angle and with energy, and the PSF of gamma-ray instruments is about a degree or more wide at low energies, so sources closer than the PSF width blend. Faint gamma-ray sources near the Galactic plane sit on bright diffuse emission whose model is built from gas tracers that miss part of the gas. Underestimating the gas in a cloud tends to create spurious sources on top of it, and errors in the diffuse model shift the positions, fluxes and spectra of real sources.

**Resolved by.** Nearby sources included in the model with their positions and spectra; the PSF used stated for the source's energy and off-axis angle; residual or test-statistic maps shown after the fit; the detection, position and flux shown to hold with an alternative diffuse model or analysis method, especially for sources near the Galactic plane or on gas clumps.

**Benchmark.** [3], [7], [8]

## 4. Pile-up and high count rates

**Question.** For bright sources, does the paper give the count rate per detector frame and the expected pile-up fraction, and how was pile-up avoided, corrected or modelled?

**Why it matters.** When two or more photons land in the same detector region within one frame, they are recorded as a single event at roughly the sum of their energies. Pile-up hardens the spectrum, lowers the count rate, suppresses the core of the PSF more than the wings and moves events out of the standard event grades, so standard calibrations underestimate the flux. A pile-up fraction above about 10 per cent is likely to affect the result.

**Resolved by.** The count rate per frame and the estimated pile-up fraction stated; an observing mode chosen to limit pile-up, such as a subarray, continuous clocking or a grating; where pile-up remains, a pile-up model included in the forward-folded spectral fit; the radial profile of the source compared with the expected PSF.

**Benchmark.** [3], [9]

## 5. Fit statistic with few counts

**Question.** Which fit statistic was used for spectra or images with few counts per bin, how was the background included in that statistic, how were the data grouped, and how was goodness of fit assessed?

**Why it matters.** Chi-squared with variances estimated from the data biases the best-fit model low when bins hold few counts, and common approximations to chi-squared can stay biased even at high counts unless the bins are few. A Poisson likelihood avoids this, but a background spectrum cannot simply be subtracted from Poisson counts: it has to be modelled or profiled, and the profiled form can fail with very few counts. For statistics other than chi-squared, the distribution of the statistic for a good fit has to be found by simulation.

**Resolved by.** The fit statistic named; with a Poisson likelihood, source and background fitted together or a profile likelihood used, with the grouping stated; a grouping scheme fixed in advance rather than tuned to the data; goodness of fit from simulated data sets, not from a reduced chi-squared applied to a Poisson statistic; key parameters shown to be stable when the statistic or grouping is changed.

**Benchmark.** [10], [11], [12]

## 6. Spectral model and forward folding

**Question.** Is the spectral model stated in full (every component, absorption model, abundance table and fixed parameter), was it fitted by folding through the instrument response, and were physically plausible alternative models tested against the same data?

**Why it matters.** Observed counts in instrument channels relate to the source spectrum through the response, and inverting that relation is generally not unique and unstable to small changes in the counts. The spectrum is therefore inferred by folding a parametric model through the response, and with few counts several different models may fit acceptably. Simple or unphysical models are often adopted, while comparison of physically motivated models can favour a different description.

**Resolved by.** Every model component and fixed parameter listed with the responses used; the counts spectrum shown with the folded model and residuals; alternative plausible models compared with a stated criterion; parameter degeneracies shown, for example as confidence contours; physical quantities derived from the model, such as a column density or a luminosity, quoted together with the model they depend on.

**Benchmark.** [10], [13]

## 7. Significance of a detection, line or added component

**Question.** How was the significance of a source, an excess, a spectral line or an extra spectral component computed, does the reference distribution used hold for that test, and does the quoted significance account for the number of positions, energies or time intervals searched?

**Why it matters.** With an on and an off measurement, the significance depends on the formula used and on the normalisation between the two; formulas checked by simulation are available. In likelihood analyses, the test statistic is converted to a significance with a number of degrees of freedom that should match the free parameters of the added source. The likelihood ratio and F tests do not follow their nominal distributions when the tested parameter sits on a boundary, as for a line whose amplitude can be zero. Searching many positions or energies makes a local excess look more significant than it is.

**Resolved by.** The significance formula or test named, with the background normalisation and the degrees of freedom stated; for lines and added components, the reference distribution calibrated by simulation under the null model; both local and global significance given, with the trials factor or the search range stated; the residual image or spectrum shown at the position or energy of the claimed signal.

**Benchmark.** [1], [7], [14], [15], [16], [17]

## 8. Non-detections and upper limits

**Question.** When a source is not detected, does the paper state how the upper limit was computed (detection threshold, confidence level, background, exposure and assumed spectrum), and does it distinguish an upper limit from a confidence interval on the flux of a particular source?

**Why it matters.** An upper limit in the strict sense describes the detection procedure: the intensity a source would need to be detected, with a stated probability, above the chosen threshold. A confidence bound instead gives a range of plausible intensities for one source. The two answer different questions, and confusing them, or omitting the threshold and the assumed spectrum used for conversion to flux, makes a non-detection hard to compare with predictions or other data.

**Resolved by.** The detection threshold and its false-positive rate stated; the method and confidence level of the upper limit named; the background and exposure at the source position given; the spectral shape assumed for the conversion to flux stated; both the upper limit and the confidence bound reported where both are relevant.

**Benchmark.** [18]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | D. Berge et al., Background modelling in very-high-energy γ-ray astronomy, Astron. Astrophys. 466, 1219 (2007); read as preprint arXiv:astro-ph/0610959 | doi:10.1051/0004-6361:20066674 |
| 2 | XMM-Newton Community Support Team, European Space Agency, XMM-Newton Users Handbook, issue 2.24 (27 July 2026), Sec. 3.3.7 EPIC background; read on the HEASARC mirror | https://heasarc.gsfc.nasa.gov/docs/xmm/uhb/epicbkgd.html |
| 3 | Chandra X-ray Center, The Chandra Proposers' Observatory Guide, version 28.0 (December 2025) | https://cxc.harvard.edu/proposer/POG/html/index.html |
| 4 | Fermi-LAT Collaboration (M. Ackermann et al.), The Fermi Large Area Telescope on orbit: event classification, instrument response functions, and calibration, Astrophys. J. Suppl. 203, 4 (2012); read as preprint arXiv:1206.1896 | doi:10.1088/0067-0049/203/1/4 |
| 5 | H. Lee et al., Accounting for calibration uncertainties in X-ray analysis: effective areas in spectral fitting, Astrophys. J. 731, 126 (2011); read on arXiv:1102.4610 | doi:10.1088/0004-637X/731/2/126 |
| 6 | K. K. Madsen et al., IACHEC cross-calibration of Chandra, NuSTAR, Swift, Suzaku, XMM-Newton with 3C 273 and PKS 2155-304, Astron. J. 153, 2 (2017); read as arXiv:1609.09032 | doi:10.3847/1538-3881/153/1/2 |
| 7 | Fermi-LAT Collaboration (S. Abdollahi et al.), Fermi Large Area Telescope Fourth Source Catalog, Astrophys. J. Suppl. 247, 33 (2020); read as preprint arXiv:1902.10045 | doi:10.3847/1538-4365/ab6bcb |
| 8 | F. Acero et al. (Fermi-LAT Collaboration), Development of the model of Galactic interstellar emission for standard point-source analysis of Fermi Large Area Telescope data, Astrophys. J. Suppl. 223, 26 (2016); read as preprint arXiv:1602.07246 | doi:10.3847/0067-0049/223/2/26 |
| 9 | J. E. Davis, Event pileup in charge-coupled devices, Astrophys. J. 562, 575 (2001) | doi:10.1086/323488 |
| 10 | K. Arnaud et al., XSPEC: An X-Ray Spectral Fitting Package, users' guide for version 13.0.1 (HEASARC, NASA/GSFC, August 2026) | https://heasarc.gsfc.nasa.gov/xanadu/xspec/manual/XspecManual.html |
| 11 | W. Cash, Parameter estimation in astronomy through application of the likelihood ratio, Astrophys. J. 228, 939 (1979) | doi:10.1086/156922 |
| 12 | P. J. Humphrey et al., χ² and Poissonian data: biases even in the high-count regime and how to avoid them, Astrophys. J. 693, 822 (2009); read on arXiv:0811.2796 | doi:10.1088/0004-637X/693/1/822 |
| 13 | J. Buchner et al., X-ray spectral modelling of the AGN obscuring region in the CDFS: Bayesian model selection and catalogue, Astron. Astrophys. 564, A125 (2014); read on arXiv:1402.0004 | doi:10.1051/0004-6361/201322971 |
| 14 | T.-P. Li and Y.-Q. Ma, Analysis methods for results in gamma-ray astronomy, Astrophys. J. 272, 317 (1983) | doi:10.1086/161295 |
| 15 | J. R. Mattox et al., The likelihood analysis of EGRET data, Astrophys. J. 461, 396 (1996) | doi:10.1086/177068 |
| 16 | R. Protassov et al., Statistics, handle with care: detecting multiple model components with the likelihood ratio test, Astrophys. J. 571, 545 (2002); read on arXiv:astro-ph/0201547 | doi:10.1086/339856 |
| 17 | E. Gross and O. Vitells, Trial factors for the look elsewhere effect in high energy physics, Eur. Phys. J. C 70, 525 (2010); read on arXiv:1005.1891 | doi:10.1140/epjc/s10052-010-1470-8 |
| 18 | V. L. Kashyap et al., On computing upper limits to source intensities, Astrophys. J. 719, 900 (2010); read on arXiv:1006.4334 | doi:10.1088/0004-637X/719/1/900 |
| 19 | Fermi Science Support Center, NASA/GSFC, Caveats about analyzing LAT Pass 8 (P8R3_V3) data, web page last updated 29 August 2025 (2025) | https://fermi.gsfc.nasa.gov/ssc/data/analysis/LAT_caveats.html |
