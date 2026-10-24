---
id: T-ASTEROSEISMOLOGY
name: Asteroseismology and stellar parameters
type: technique
field: physics/astrophysics
applies_when: the paper detects stellar oscillations or uses their frequencies to infer stellar properties, measures a large frequency separation, frequency of maximum power, period spacings or individual mode frequencies, or derives stellar masses, radii, ages or evolutionary states from asteroseismic scaling relations or seismic modelling
version: "0.1"
---

# Asteroseismology and stellar parameters

Asteroseismology uses the frequencies of a star's oscillation modes to claim its mean density, surface gravity, radius, mass, evolutionary state, internal rotation and age. For solar-like oscillators the claims rest on two global quantities, the large frequency separation (Δν) and the frequency of maximum oscillation power (νmax), combined in scaling relations, or on individual mode frequencies matched to stellar models; for stars with gravity (g) modes they rest on period spacings.

## 1. Detection of the oscillations

**Question.** How was the presence of oscillations established: what test, threshold and false-alarm level were used, and does the paper show that the detected excess power and spacing are not instrumental or sampling artefacts?

**Why it matters.** A power excess or a spacing can be found in noise when many trial values are searched, and a weak detection at a loose significance level carries a sizeable chance that no signal is present. Artefacts such as the orbital frequency of the spacecraft, the diurnal frequency and its harmonics, twice the true spacing, and signals above the Nyquist frequency folded back into the spectrum can all mimic oscillation features.

**Resolved by.** The power spectrum shown with the background level and the oscillation envelope; a detection statistic with its threshold and false-alarm probability, accounting for the range of spacings searched; known instrumental and window-function frequencies identified and excluded; a check, where the sampling allows, that the signal is not a super-Nyquist alias.

**Benchmark.** [1], [2]

## 2. Global seismic parameters

**Question.** How were Δν and νmax measured: which method or pipeline, which background model, over which frequency range, and do the quoted uncertainties include the scatter between methods and the noise from the stochastic excitation of the modes?

**Why it matters.** Δν and νmax are defined operationally, and different definitions, background models and frequency ranges give values that differ by a few percent, which is comparable to the precision claimed for derived masses and radii. Δν changes with frequency, so its value depends on the range used. The random excitation and damping of the modes adds an uncertainty that does not shrink with better photometry alone and is easily left out.

**Resolved by.** The method named and described, with the background components and the frequency range used for Δν; results compared with a second, independent method or pipeline, or the method-to-method spread taken from published comparisons and added to the uncertainty; the uncertainty from the stochastic nature of the signal included, for example from simulations or repeated realisations.

**Benchmark.** [2], [3], [4]

## 3. Mode identification

**Question.** How were angular degree, radial order and azimuthal order assigned to the observed frequencies, is the échelle diagram or period-spacing pattern shown, and were alternative identifications tested?

**Why it matters.** Every inference from individual frequencies assumes the identification is right. In hotter stars broad modes blur the pairs of radial and quadrupole modes, so the two possible identifications, which differ by about half a large separation, are hard to tell apart. In red giants and subgiants, mixed modes depart from the regular pattern, and for high-order g modes rotation tilts the period-spacing pattern and the radial order can be off by one or more.

**Resolved by.** An échelle diagram or period-spacing diagram with the identification marked; for ambiguous cases, both identifications fitted and compared, or an independent discriminant such as the offset ε against effective temperature or linewidth; rotational multiplets identified with the splittings and their assumed geometry stated; frequencies with uncertain identification flagged and the sensitivity of the results to them shown.

**Benchmark.** [2], [5], [6], [7]

## 4. Scaling relations and their calibration

**Question.** When masses and radii come from scaling relations, which form of the relations, which solar reference values and which corrections to the Δν relation were used, and is the accuracy of the relations for this type of star supported by independent tests?

**Why it matters.** The relations scale Δν and νmax from solar values and are approximate; mass depends on the cube of νmax and the inverse fourth power of Δν, so small offsets in either become large errors in mass. Comparisons with eclipsing binaries and parallaxes show systematic departures of several percent in radius and larger in mass for some classes of star, for example red giants and subgiants, and an overestimated mass gives an underestimated age.

**Resolved by.** The relations, solar reference values and any Δν correction stated, with the corrections matched to the star's evolutionary state and metallicity; the derived mass and radius compared with an independent determination, such as a parallax radius, interferometric diameter or binary dynamical mass, for the same star or for calibrators of the same type; a systematic uncertainty for the relations included alongside the measurement uncertainty.

**Benchmark.** [5], [8], [9]

## 5. Evolutionary state of red giants

**Question.** For red giants, how was the evolutionary state (hydrogen-shell burning on the red-giant branch or core helium burning in the red clump) determined, and was it used consistently in the scaling-relation corrections and the model grid?

**Why it matters.** Red-giant-branch and red-clump stars can have similar surface temperatures and luminosities but different interiors. The Δν scaling differs between them, so applying the wrong correction can shift clump masses by about ten percent, and the state also selects the model tracks from which an age is read. Classifications from different methods do not always agree.

**Resolved by.** The state determined from seismic diagnostics such as the dipole period spacing or mixed-mode pattern, with the method named; agreement with a second classification method, or stars without a consistent classification flagged; corrections and model tracks chosen to match the state; results shown not to depend on stars with an uncertain state.

**Benchmark.** [4], [5], [10]

## 6. Individual frequencies and the surface effect

**Question.** When individual mode frequencies are fitted with stellar models, how was the offset between model and observed frequencies caused by the poorly modelled near-surface layers treated, and does the result depend on that choice?

**Why it matters.** Standard stellar models usually predict mode frequencies that are too high, by an amount that grows with frequency, because convection and non-adiabatic effects near the surface are poorly described. Different empirical corrections fit the data with different success, and a correction calibrated on the Sun needs adjustment for mixed modes and evolved stars, so the choice can move the inferred mass, radius and age.

**Resolved by.** The surface correction named and its free parameters fitted together with the stellar parameters; results compared for at least two corrections, or, for main-sequence stars, frequency separation ratios that are largely insensitive to the surface layers used as a cross-check; the fit residuals shown as a function of frequency.

**Benchmark.** [4], [5], [11]

## 7. Model dependence of masses and ages

**Question.** Which stellar evolution codes, grids and input physics (mixing length, convective overshoot, diffusion, initial helium, opacities) were used to derive mass and age, and is the spread between different grids or modelling choices included in the quoted uncertainty?

**Why it matters.** Radius and density follow closely from the seismic data, but mass and especially age depend on composition, diffusion, core overshoot and other mixing processes that are not well calibrated. More overshoot, for example, supplies more fuel to the core and lengthens its burning lifetime. Comparisons of widely used grids give spreads of about 5% in mass and 20% in age for main-sequence and subgiant stars, a term that the statistical uncertainty of a single fit with fixed physics does not include.

**Resolved by.** The codes, grids and input physics listed, with which parameters were free and which fixed; results from several grids or modelling pipelines compared and the scatter between them added to the uncertainty; ages quoted with an uncertainty that includes this model term; claims that rest on precise ages, such as age ordering of stars or populations, checked against the size of the model systematics.

**Benchmark.** [5], [7], [12], [13]

## 8. Non-seismic inputs

**Question.** Which effective temperature, metallicity and, where used, luminosity enter the analysis, on what scale were they measured, and how do changes within their systematic uncertainties change the derived mass, radius and age?

**Why it matters.** Scaling-relation masses and radii depend on effective temperature, and grid-based masses and ages depend strongly on the adopted metallicity. Effective temperatures on different scales, for example spectroscopic or infrared-flux, differ systematically, and the absolute temperature scale itself is uncertain at about the two percent level, so the choice of scale can change agreement with independent radii.

**Resolved by.** The source and scale of each non-seismic input stated, with uncertainties that include a systematic term; the derived parameters recomputed for a plausible change of temperature scale and metallicity, or the corresponding uncertainty propagated.

**Benchmark.** [5], [9], [13]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | B. Mosser and T. Appourchaux, On detecting the large separation in the autocorrelation of stellar oscillation times series, Astron. Astrophys. 508, 877–887 (2009); read as arXiv:0909.0782 | doi:10.1051/0004-6361/200912944 | full text | Secs. 4.1 and 4.7 with Table 3: a white-noise null hypothesis test, with detection thresholds set from the number of independent bins tested; Sec. 5.1: a 10% significance level is weak and leaves a large posterior probability of no signal; Sec. 5.2: in red giants many apparent detections were artefacts at twice the spacing, the diurnal frequency and harmonics, and the orbital frequency |
| 2 | R. A. García and J. Ballot, Asteroseismology of solar-type stars, Living Rev. Sol. Phys. 16, 4 (2019); read as arXiv:1906.12262 | doi:10.1007/s41116-019-0020-1 | full text | Sec. 3: signals above the Nyquist frequency alias to lower frequencies, and some claimed detections were marginal or disputed; Sec. 4.1.1: peaks above the acoustic cut-off are interference, not modes; Secs. 5.2.1 and 5.7: background modelled with Harvey-type components, νmax from a fitted envelope and Δν from autocorrelation or a Fourier transform of the spectrum; Sec. 5.6: in F stars broad modes make the ridge identification ambiguous, tested by comparing identifications and using ε against temperature |
| 3 | S. Hekker et al., Solar-like oscillations in red giants observed with Kepler: comparison of global oscillation parameters from different methods, Astron. Astrophys. 525, A131 (2011) | doi:10.1051/0004-6361/201015185 | abstract | Abstract: several groups measured νmax and Δν for over a thousand red giants with different methods; values agree within a few percent; the stochastic nature of the oscillations adds an uncertainty that is not negligible and should be included in modelling |
| 4 | S. Hekker and J. Christensen-Dalsgaard, Giant star seismology, Astron. Astrophys. Rev. 25, 1 (2017); read as arXiv:1609.07487 | doi:10.1007/s00159-017-0101-x | full text | Secs. 3.3.1 and 3.3.3: νmax definitions agree within a few percent, and Δν curves with frequency so its value depends on the range used; Secs. 3.3.6 and 3.3.7: small dipole separations and period spacings separate red-giant-branch from core-helium-burning stars; Sec. 3.4.3: a solar-calibrated power-law surface correction needs adjustment for mixed modes, a two-term correction works better across evolutionary stages, and frequency separation ratios suppress the surface effect in main-sequence stars but are of limited use in red giants |
| 5 | W. J. Chaplin and A. Miglio, Asteroseismology of solar-type and red-giant stars, Annu. Rev. Astron. Astrophys. 51, 353–392 (2013); read as arXiv:1303.1957 | doi:10.1146/annurev-astro-082812-140938 | full text | Sec. 3: broad peaks in F stars made odd and even ridges hard to tag; Sec. 4: effective temperature and strong metallicity priors are needed for mass and age; Sec. 4.1: scaling relations with M proportional to νmax cubed over Δν to the fourth, masses less certain than radii, red-clump and red-giant-branch Δν scaling differing, clump masses off by about 10% if this is ignored, and masses and ages depending on composition, diffusion and overshoot, so several grids should be used with their scatter in the uncertainty; Sec. 5.1: models overestimate frequencies by an amount growing with frequency, and frequency separation ratios are largely insensitive to the surface; Sec. 5.2: period spacings separate clump and branch stars |
| 6 | T. R. White et al., Solving the mode identification problem in asteroseismology of F stars observed with Kepler, Astrophys. J. Lett. 751, L36 (2012); read as arXiv:1205.0544 | doi:10.1088/2041-8205/751/2/L36 | full text | Secs. 1 and 2: large linewidths in hot stars blur the radial and quadrupole pairs; the two candidate identifications give ε values differing by about 0.5; abstract and Sec. 4: ε against effective temperature, with linewidth, used to choose between them |
| 7 | C. Aerts, Probing the interior physics of stars through asteroseismology, Rev. Mod. Phys. 93, 015001 (2021); read as arXiv:1912.12300 | doi:10.1103/RevModPhys.93.015001 | full text | Sec. III and III.B: modes must be labelled (n, l, m) before interpretation, with uncertain labels treated in the prior; Sec. III.B.2: rotational multiplets reveal l and m; Sec. III.B.3: the slope of g-mode period-spacing patterns is set by rotation; Sec. II.B.2: assignment of g-mode radial order uncertain by at least one; Sec. II.A.1: convective boundary mixing is uncalibrated, and more of it brings more fuel to the core, changing core mass and age; Sec. II.A.6: the fit repeated for other choices of input physics |
| 8 | P. Gaulme et al., Testing the asteroseismic scaling relations for red giants with eclipsing binaries observed by Kepler, Astrophys. J. 832, 121 (2016) | doi:10.3847/0004-637X/832/2/121 | abstract | Abstract: for ten red giants in eclipsing binaries, scaling relations overestimate radii by about 5% and masses by about 15% on average; an overestimated mass leads to an underestimated age |
| 9 | D. Huber et al., Asteroseismology and Gaia: testing scaling relations using 2200 Kepler stars with TGAS parallaxes, Astrophys. J. 844, 102 (2017) | doi:10.3847/1538-4357/aa75ca | abstract | Abstract: seismic radii accurate to about 5% or better between about 0.8 and 8 solar radii, but subgiants underestimated by about 5%; the differences are partly removed by a hotter, infrared-flux temperature scale instead of spectroscopic temperatures; tentative evidence that corrections to the Δν relation improve agreement for red-giant-branch stars |
| 10 | Y. Elsworth et al., Insights from the APOKASC determination of the evolutionary state of red-giant stars by consolidation of different methods, Mon. Not. R. Astron. Soc. 489, 4641–4657 (2019) | doi:10.1093/mnras/stz2356 | abstract | Abstract: the evolutionary state of red giants determined by comparing several seismic methods; stars without a consensus are flagged; the consensus states are inputs to methods that derive masses and ages |
| 11 | W. H. Ball and L. Gizon, A new correction of stellar oscillation frequencies for near-surface effects, Astron. Astrophys. 568, A123 (2014) | doi:10.1051/0004-6361/201424325 | abstract | Abstract: inaccurate near-surface layers bias the comparison of model and observed frequencies; surface terms fitted together with stellar parameters; the scaled power-law correction gives a significantly worse fit than the proposed inertia-based terms |
| 12 | V. Silva Aguirre et al., Standing on the shoulders of dwarfs: the Kepler asteroseismic LEGACY sample II – radii, masses, and ages, Astrophys. J. 835, 173 (2017) | doi:10.3847/1538-4357/835/2/173 | abstract | Abstract: the same frequencies of 66 stars modelled by seven teams with different codes, input physics and methods; average uncertainties of about 2% in radius, 4% in mass and 10% in age; accuracy tested against the Sun, interferometry, parallaxes and binaries |
| 13 | J. Tayar, Z. R. Claytor, D. Huber and J. van Saders, A guide to realistic uncertainties on the fundamental properties of solar-type exoplanet host stars, Astrophys. J. 927, 31 (2022); read as arXiv:2012.07957 | doi:10.3847/1538-4357/ac4bbc | abstract | Abstract: systematic floors of about 2% in effective temperature and 4% in radius from the fundamental measurement scale, and about 5% in mass and 20% in age from comparing widely used model grids for main-sequence and subgiant stars |
