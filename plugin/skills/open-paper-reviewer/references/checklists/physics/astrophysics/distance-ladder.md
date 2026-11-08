---
id: T-DISTANCE-LADDER
name: Distance ladder and the Hubble constant
type: technique
field: physics/astrophysics
applies_when: the paper measures galaxy distances with Cepheids, the tip of the red giant branch or other stellar standard candles, calibrates Type Ia supernovae or another secondary indicator, derives the Hubble constant, or claims agreement or tension between Hubble constant measurements
version: "0.1"
---

# Distance ladder and the Hubble constant

## 1. Geometric anchors and the photometric link to them

**Question.** Which geometric anchors set the absolute scale (trigonometric parallaxes, detached eclipsing binaries, water masers), how were their distances and uncertainties used, how was any parallax zero-point offset treated, and were the anchors and the distant hosts measured on the same photometric system?

**Why it matters.** Every distance on the ladder scales with the anchor zero point, which rests on a handful of objects, and calibrating on one anchor rather than another can move H0 by several per cent. Space-based parallaxes carry a zero-point offset that depends on magnitude, colour and sky position, and published corrections are tentative and valid only where they were calibrated, which excludes some bright stars. Any offset between the photometric systems of the nearby anchors and the distant hosts passes straight into the distances.

**Resolved by.** Each anchor named with its distance and uncertainty; H0 reported for each anchor alone as well as combined; the parallax offset correction stated, with a check that the calibrators fall within its range or a residual offset fitted; anchors and hosts observed with the same instrument and filters, or the transformation between systems stated and its uncertainty carried into the result.

**Benchmark.** [1], [2], [3], [4], [5]

## 2. Crowding and blending of calibrator stars

**Question.** How was the bias from unresolved neighbouring stars in the photometry of calibrator stars in distant hosts measured, how large is the correction compared with the claimed precision, and how does it differ between the nearby anchors and the distant hosts?

**Why it matters.** Light from unresolved neighbours brightens and reddens a star, so its distance comes out too short. The effect grows with distance and with wavelength, as resolution worsens, and for Cepheids in supernova hosts it has been measured at about two tenths of a magnitude in the near infrared; because the anchors are near and less crowded, it does not cancel along the ladder. For the TRGB, crowded disc fields add young stars and bright asymptotic giant branch stars that can be mistaken for the tip.

**Resolved by.** Artificial stars injected near each calibrator in the same images and recovered with the same pipeline, with the mean offset applied and its uncertainty propagated; the correction shown as a function of local surface brightness or host distance; independent tests such as colour cuts, light-curve amplitudes or higher-resolution imaging; for the TRGB, fields in the low-density outer halo, with the selection rule stated.

**Benchmark.** [3], [4], [5], [6]

## 3. Extinction and metallicity corrections

**Question.** How were dust extinction and the difference in metallicity between anchors and hosts corrected (the reddening law, the reddening-free magnitude used, the metallicity term and where the abundances came from), and how much does H0 change under other reasonable choices?

**Why it matters.** A reddening-free (Wesenheit) magnitude removes extinction only if the assumed ratio of total to selective extinction holds everywhere. The metallicity dependence of the Leavitt law is still uncertain in size and even sign, the abundances are usually taken from nearby H II regions rather than the stars, and anchors and hosts differ in metallicity, so the correction does not cancel. Reddening, metallicity and crowding corrections are covariant, and different extinction treatments for the same anchor have given different TRGB zero points.

**Resolved by.** The reddening law and colour coefficients stated, with H0 shown for alternative laws; the metallicity term given with its source and constrained within the sample where possible, and its effect on H0 quantified; data in several bands, including the near or mid infrared where extinction is small; for the TRGB, the colour or metallicity dependence of the tip and the extinction adopted for the calibrating field stated.

**Benchmark.** [1], [3], [4], [5], [6]

## 4. Measuring the indicator in each galaxy

**Question.** How was the indicator measured in each galaxy (for Cepheids, the period range, light-curve coverage and whether the period-luminosity slope is shared between galaxies; for the TRGB, the edge-detection method, smoothing, number of stars near the tip and treatment of contaminating populations), and was the same procedure applied to anchors and distant hosts?

**Why it matters.** A TRGB distance depends on locating an edge in a noisy luminosity function: Poisson noise produces false edges in sparse samples, and results move with smoothing and binning. For Cepheids, period cuts, breaks in the period-luminosity relation and slopes that differ between hosts change the inferred distances. A procedure that differs between the nearby and distant ends of the ladder gives a systematic offset rather than random scatter.

**Resolved by.** The detection method and its parameters stated, with the number of stars near the tip, and artificial-tip or injection tests showing the bias and uncertainty; for Cepheids, the period range, slope treatment and outlier rule stated, with H0 shown for alternatives such as a fixed slope or a different period cut; the same method applied at every rung.

**Benchmark.** [3], [4], [6]

## 5. Calibrator and Hubble-flow supernovae

**Question.** Are the calibrator supernovae and the Hubble-flow supernovae observed, standardised and selected in the same way, and does the paper test whether their host-galaxy properties differ and whether that changes H0?

**Why it matters.** Few supernovae have hosts close enough for stellar distances, so the calibration rests on small numbers. Standardised SN Ia brightness shifts by a few hundredths of a magnitude with host stellar mass or with star formation near the supernova, and if the calibrator hosts differ in these properties from the Hubble-flow hosts, H0 can be biased by up to a few per cent. Survey selection and cross-calibration between surveys can also differ between the two samples.

**Resolved by.** The number of calibrators and their scatter stated; the same light-curve fitter, standardisation parameters and photometric calibration used for both samples; host properties of the two samples compared and an environmental correction tested; H0 shown for subsets, for example restricted to similar hosts or to the calibrators with the best distances.

**Benchmark.** [1], [3]

## 6. Redshifts, peculiar velocities and the local volume

**Question.** Over what redshift range is H0 measured, how were redshifts and peculiar velocities corrected, what is assumed for the expansion history in the fit, and is the variance from local large-scale structure included in the uncertainty?

**Why it matters.** Close by, coherent flows and peculiar velocities form a large part of the measured redshift; a 10% error on a typical peculiar velocity at 50 Mpc already gives about 1% in H0, and small systematic redshift offsets bias it too. A sample concentrated at low redshift and unevenly spread on the sky samples local density fluctuations, which adds variance to the local value.

**Resolved by.** A lower redshift limit chosen to avoid coherent local flows, with H0 shown to be stable when it is changed; peculiar-velocity corrections from a stated flow model with an assigned uncertainty; the deceleration parameter or expansion history taken from independent data and its effect stated; a sample-variance term in the error budget.

**Benchmark.** [3], [4], [7], [8]

## 7. Covariant systematics and independent cross-checks

**Question.** Does the systematic error budget list the terms at each rung and their correlations, show how H0 changes across the plausible variants of each analysis choice, and compare distances from independent indicators to the same galaxies?

**Why it matters.** The rungs share calibrations and corrections, so their systematic errors are correlated and do not average down; adding more distant galaxies reduces only the statistical error. A joint fit is pulled towards the data set with the smallest quoted error, which need not have the smallest systematic error. Independent indicators that agree for nearby galaxies but diverge farther out can point to a distance-dependent systematic in at least one of them.

**Resolved by.** A table of systematic terms per rung with their size in H0 and any correlations; results for analysis variants (anchors, reddening law, metallicity term, outlier rule, period or colour cuts), with their spread included in the quoted uncertainty; distances to galaxies measured with two or more independent indicators compared as a function of distance.

**Benchmark.** [1], [3], [4], [5]

## 8. Claims of tension between measurements

**Question.** When the paper claims agreement or tension between H0 values, how is the significance computed, are the compared or combined measurements independent of one another, is the model dependence of each value stated, and does the conclusion hold when single methods, anchors or data sets are left out?

**Why it matters.** Ladders that share calibrators or anchors are correlated and cannot be averaged as if independent. The difference of two means over their combined error ignores priors, assumes Gaussian posteriors and can miss a tension shared between correlated parameters, and different tension statistics give different significances for the same data. An H0 inferred from the CMB or BAO depends on the cosmological model assumed, so a tension is between a direct measurement and a model-dependent inference.

**Resolved by.** The statistic used to quantify tension named, with its assumptions; covariances between combined measurements included, or each combination restricted to independent ladders; the model behind each inferred value stated; the significance shown when each method, anchor or data set is dropped in turn; the possibility of unidentified systematics weighed alongside new physics.

**Benchmark.** [3], [9], [10]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | W. L. Freedman and B. F. Madore, The Hubble constant, Annu. Rev. Astron. Astrophys. 48, 673 (2010); read as preprint arXiv:1004.1856 | doi:10.1146/annurev-astro-082708-101829 |
| 2 | L. Lindegren et al., Gaia Early Data Release 3: parallax bias versus magnitude, colour, and position, Astron. Astrophys. 649, A4 (2021); read as preprint arXiv:2012.01742 | doi:10.1051/0004-6361/202039653 |
| 3 | P. Shah et al., A buyer's guide to the Hubble constant, Astron. Astrophys. Rev. 29, 9 (2021); read as preprint arXiv:2109.01161 | doi:10.1007/s00159-021-00137-4 |
| 4 | A. G. Riess et al., A 2.4% determination of the local value of the Hubble constant, Astrophys. J. 826, 56 (2016); read as preprint arXiv:1604.01424 | doi:10.3847/0004-637X/826/1/56 |
| 5 | W. L. Freedman, Measurements of the Hubble constant: tensions in perspective, Astrophys. J. 919, 16 (2021); read as preprint arXiv:2106.15656 | doi:10.3847/1538-4357/ac0e95 |
| 6 | R. L. Beaton et al., Old-aged primary distance indicators, Space Sci. Rev. 214, 113 (2018); read as preprint arXiv:1808.09191, which carries a slightly different title | doi:10.1007/s11214-018-0542-1 |
| 7 | A. Carr et al., The Pantheon+ analysis: improving the redshifts and peculiar velocities of Type Ia supernovae used in cosmological analyses, Publ. Astron. Soc. Aust. 39, e046 (2022); read as preprint arXiv:2112.01471 | doi:10.1017/pasa.2022.41 |
| 8 | H.-Y. Wu and D. Huterer, Sample variance in the local measurements of the Hubble constant, Mon. Not. R. Astron. Soc. 471, 4946 (2017); read as preprint arXiv:1706.09723 | doi:10.1093/mnras/stx1967 |
| 9 | L. Verde et al., Tensions between the early and late Universe, Nat. Astron. 3, 891 (2019); read as preprint arXiv:1907.10625, which carries a slightly different title | doi:10.1038/s41550-019-0902-0 |
| 10 | M. Raveri and W. Hu, Concordance and discordance in cosmology, Phys. Rev. D 99, 043506 (2019); read as preprint arXiv:1806.04649 | doi:10.1103/PhysRevD.99.043506 |
