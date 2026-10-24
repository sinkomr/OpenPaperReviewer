---
id: T-DISTANCE-LADDER
name: Distance ladder and the Hubble constant
type: technique
field: physics/astrophysics
applies_when: the paper measures galaxy distances with Cepheids, the tip of the red giant branch or other stellar standard candles, calibrates Type Ia supernovae or another secondary indicator, derives the Hubble constant, or claims agreement or tension between Hubble constant measurements
version: "0.1"
---

# Distance ladder and the Hubble constant

The distance ladder is used to claim distances to galaxies and a local value of the Hubble constant (H0): geometric distances to nearby anchors calibrate stellar standard candles such as Cepheid variables, through their period-luminosity (Leavitt) law, or the tip of the red giant branch (TRGB); these calibrate a secondary indicator such as Type Ia supernovae (SNe Ia) in host galaxies; and the secondary indicator, measured far out in the smooth expansion (the Hubble flow), gives H0. The same value is often compared with H0 inferred from the cosmic microwave background (CMB) and baryon acoustic oscillations (BAO) within the standard cosmological model (ΛCDM).

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | W. L. Freedman and B. F. Madore, The Hubble constant, Annu. Rev. Astron. Astrophys. 48, 673–710 (2010); read as preprint arXiv:1004.1856 | doi:10.1146/annurev-astro-082708-101829 | full text | Secs. 3.1.4, 3.1.5 and 3.3: Cepheid zero point from Galactic parallaxes, with the LMC and the maser galaxy as independent checks. Secs. 3.0.1 and 3.1.2: extinction biases distances and the Wesenheit magnitude is extinction-free only if the extinction ratio is universal. Sec. 3.1.3: sign and size of the metallicity effect contested. Sec. 3.6: supernova calibration rests on few hosts. Sec. 4 and Table 2: systematic budget with zero point, metallicity, reddening and camera zero-point transformation terms |
| 2 | L. Lindegren, U. Bastian, M. Biermann et al., Gaia Early Data Release 3: parallax bias versus magnitude, colour, and position, Astron. Astrophys. 649, A4 (2021); read as preprint arXiv:2012.01742 | doi:10.1051/0004-6361/202039653 | full text | Abstract and Secs. 2 to 4: parallax zero-point offset of order −20 µas that varies with magnitude, colour and ecliptic latitude; the correction is offered as tentative, for use at the researcher's discretion, valid only within the magnitude and colour range of the calibrating samples, with bright stars resting on extra assumptions |
| 3 | P. Shah, P. Lemos and O. Lahav, A buyer's guide to the Hubble constant, Astron. Astrophys. Rev. 29, 9 (2021); read as preprint arXiv:2109.01161 | doi:10.1007/s00159-021-00137-4 | full text | Secs. 2.4 and 3.4: blending brightens and reddens distant Cepheids, estimated by adding artificial Cepheids to the images; metallicity term in the Leavitt law. Secs. 3.1 to 3.3: parallax zero-point offset and the geometric anchors. Sec. 3.4: calibrating on one anchor alone shifts H0 by about 4 km/s/Mpc, the slope choice matters, and a joint solution is drawn to the data with the lowest error. Sec. 3.6: a TRGB calibration differing through the LMC extinction method. Sec. 3.7: few calibrator supernovae; host-mass step of 0.04 to 0.06 mag, and a bias of up to about 3% from a local star-formation step if calibrators differ from the flow sample. Sec. 1.1: a 10% peculiar-velocity error at 50 Mpc gives about 1% in H0. Sec. 4.1.2: a redshift shift of 0.001 biases H0 by about 3%. Secs. 1.1, 2.2 and 2.5: sigma counting and model dependence of CMB and BAO values. Sec. 5.3: unknown systematics weighed against new physics |
| 4 | A. G. Riess, L. M. Macri, S. L. Hoffmann et al., A 2.4% determination of the local value of the Hubble constant, Astrophys. J. 826, 56 (2016); read as preprint arXiv:1604.01424 | doi:10.3847/0004-637X/826/1/56 | full text | Secs. I, II and III.1: all distant hosts observed with one camera so that zero-point errors cancel, ground-based anchor photometry transformed with a fitted residual offset. Sec. II.1: artificial-star tests near each Cepheid, with a median near-infrared blending bias of about 0.18 mag in hosts. Sec. III: Hubble-flow fit limited to 0.023 < z < 0.15, the lower limit to avoid a coherent local flow, with the deceleration parameter taken from independent data and its uncertainty propagated. Abstract and Sec. III: H0 given for each anchor separately and combined. Sec. IV: analysis variants (outlier rule, colour cut, reddening law, period cuts, metallicity) used as a systematic term |
| 5 | W. L. Freedman, Measurements of the Hubble constant: tensions in perspective, Astrophys. J. 919, 16 (2021); read as preprint arXiv:2106.15656 | doi:10.3847/1538-4357/ac0e95 | full text | Sec. VI.1: TRGB best measured in low-density outer halos where crowding is small. Sec. VI.2, items 3, 5 and 6: Cepheid crowding grows with distance and wavelength; metallicity effect debated in size and sign, usually inferred from H II regions; reddening, metallicity and crowding corrections are covariant, and more distant galaxies reduce only statistical error. Secs. V and VIII: TRGB and Cepheid distances agree within about 7 Mpc and diverge farther out. Sec. II.3: LMC reddening treatment and ground-to-space calibration term |
| 6 | R. L. Beaton, G. Bono, V. F. Braga et al., Old-aged primary distance indicators, Space Sci. Rev. 214, 113 (2018); read as preprint arXiv:1808.09191, which carries a slightly different title | doi:10.1007/s11214-018-0542-1 | full text | Sec. 4.1: tip magnitude nearly constant in the I band for old metal-poor stars, with colour dependence in the near infrared. Sec. 4.2.1: Poisson noise produces false edges and smoothing is needed, at least 100 stars within a magnitude of the tip needed, simulations with an artificial tip to quantify errors. Sec. 4.2.2: colour-based corrections that flatten the tip. Sec. 4.2.3: bright asymptotic giant branch stars mistaken for the tip bias distances; halo fields reduce contamination |
| 7 | A. Carr, T. M. Davis, D. Scolnic et al., The Pantheon+ analysis: improving the redshifts and peculiar velocities of Type Ia supernovae used in cosmological analyses, Publ. Astron. Soc. Aust. 39, e046 (2022); read as preprint arXiv:2112.01471 | doi:10.1017/pasa.2022.41 | full text | Sec. 1: systematic redshift errors matter for large samples. Secs. 6.1 and 6.3: peculiar velocities from a density reconstruction with an assigned uncertainty, and a bulk flow modelled beyond it. Sec. 7.2: effect on H0 of the corrections and of systematic redshift offsets, with H0 fit over 0.0233 < z < 0.15 |
| 8 | H.-Y. Wu and D. Huterer, Sample variance in the local measurements of the Hubble constant, Mon. Not. R. Astron. Soc. 471, 4946–4955 (2017); read as preprint arXiv:1706.09723 | doi:10.1093/mnras/stx1967 | full text | Sec. 3.1, Sec. 4 and Table 1: the supernova redshift distribution, skewed to low redshift, raises the sample variance of local H0 from about 0.13 to about 0.3 km/s/Mpc compared with a uniform sample; sky distribution adds a little more. Sec. 5: the local H0 deviation correlates with the local density contrast |
| 9 | L. Verde, T. Treu and A. G. Riess, Tensions between the early and late Universe, Nat. Astron. 3, 891–895 (2019); read as preprint arXiv:1907.10625, which carries a slightly different title | doi:10.1038/s41550-019-0902-0 | full text | Workshop report. Section on combining late-universe results: ladders sharing supernova calibrators are not independent and cannot be averaged without their covariance; combinations restricted to one ladder at a time; results checked with any one method, team or source left out; a method marginalising over unknown systematics lowers the significance. Discussion of the early-universe value: it rests on a ΛCDM fit |
| 10 | M. Raveri and W. Hu, Concordance and discordance in cosmology, Phys. Rev. D 99, 043506 (2019); read as preprint arXiv:1806.04649 | doi:10.1103/PhysRevD.99.043506 | full text | Sec. II.5: the rule-of-thumb difference of means over combined error ignores priors, assumes Gaussian distributions and does not extend to several parameters. Secs. II.3 and IV.1: priors and the effective number of constrained parameters change the significance. Secs. IV.2 and IV.3 and Appendix C: estimators assume independent data sets, and different estimators give different significances for the same pair, notably with non-Gaussian posteriors. Appendix G: an effective sigma is a Gaussian-equivalent definition |
