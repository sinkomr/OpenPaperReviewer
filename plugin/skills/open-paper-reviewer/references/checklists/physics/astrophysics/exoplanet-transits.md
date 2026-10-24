---
id: T-EXOPLANET-TRANSITS
name: Exoplanet transits
type: technique
field: physics/astrophysics
applies_when: the paper reports a planet or planet candidate found by transit photometry, validates or confirms a transiting planet, or bases a claim about planet radius, orbit, eccentricity, occurrence rate or false-positive probability on transit light curves
version: "0.1"
---

# Exoplanet transits

Transit photometry is used to claim that a planet passes in front of its host star, and to infer the planet's radius, orbital period, orbital geometry and, in statistical validation, the probability that the signal is a false positive (FPP) rather than a planet. These quantities rest on a small, periodic dip in the combined light of every star in the photometric aperture, interpreted through a model of the star and the transit.

## 1. Detection significance, correlated noise and detrending

**Question.** What detection statistic and threshold were used, was the noise estimated on the timescale of the transit including correlated (red) noise, how was the light curve detrended, how many individual transits contribute to the signal, and was the signal tested against instrumental artefacts and stellar variability?

**Why it matters.** Signal-to-noise ratios computed for uncorrelated noise overstate the significance of a transit when systematics and stellar variability act on timescales close to the transit duration. Detrending filters with too short a window, or that are not robust to the transit points, can reduce the transit depth or remove the signal. Detection efficiency rises gradually above the nominal threshold rather than as a step, so claims about non-detections or occurrence need measured completeness. Periodic systematics, quasi-sinusoidal variability or a single strong event can also produce a detection that is not transit-shaped.

**Resolved by.** The detection statistic, threshold and number of transits stated; a noise estimate that includes correlated noise on the transit timescale, for example the scatter of the light curve binned to the transit duration; the detrending method and window given, with the window long compared with the transit duration or the transits masked when the ephemeris is known; individual transits shown with consistent depths, and the detection not dominated by one event or by a non-transit shape; for completeness or occurrence claims, injection and recovery of simulated transits through the same pipeline.

**Benchmark.** [1], [2], [3], [4]

## 2. Eclipsing binary signatures on the target

**Question.** Does the paper test the light curve for signs that the target itself is an eclipsing binary: different depths of odd and even transits, a secondary eclipse, a V-shaped or grazing transit, or a shape and duration that do not fit a planet around the assumed star?

**Why it matters.** An eclipsing binary seen at half its true period, or a grazing binary eclipse, can give a periodic dip similar to a planetary transit. The presence of a significant secondary eclipse, unequal alternating depths and a transit shape that matches binary scenarios better than a planet are standard diagnostics, and a depth on its own does not decide the question.

**Resolved by.** Odd and even transits fitted separately with their depths and the significance of any difference given; a search for a secondary eclipse at all phases, with an upper limit when none is seen; the transit shape (ingress, egress and flat bottom) shown and compared with planetary and binary models; the duration and shape checked against what the host star's density allows.

**Benchmark.** [4], [5], [6]

## 3. Location of the transit source

**Question.** Does the paper show that the transit occurs on the target star and not on a nearby star blended in the aperture, using difference images, centroid shifts, ephemeris matching against neighbouring stars or higher-resolution photometry?

**Why it matters.** A faint eclipsing binary within the photometric aperture, diluted by the brighter target, can produce a shallow dip that mimics a small planet. Such background false positives are common in crowded, low Galactic latitude fields and with large detector pixels, and centroid methods can be biased by bright neighbours and cannot resolve sources very close to the target.

**Resolved by.** A difference-image or centroid analysis with the measured offset and its uncertainty compared with the positions of known nearby stars; the radius within which a contaminating source cannot be excluded stated; nearby stars bright enough to produce the observed depth listed and either ruled out by photometry at higher resolution or included in the false-positive analysis; a check that the period and epoch do not match a known variable or eclipsing binary nearby.

**Benchmark.** [4], [7], [8]

## 4. Dilution by unresolved companions

**Question.** Has the target been searched for unresolved stellar companions by high-resolution imaging or spectroscopy, and is the transit depth corrected for any light they contribute, with the possibility considered that the planet orbits a companion?

**Why it matters.** Light from an unresolved star adds to the flux and makes the transit shallower, so a radius derived for a single star is too small. If the planet orbits a fainter companion instead of the primary, the true radius can be several times larger than the derived one, which can change a planet into a star or a binary eclipse.

**Resolved by.** High-resolution imaging with contrast curves, and spectra or radial velocities that limit close companions, reported with their detection limits; the flux contribution of known nearby stars in the aperture and of any detected companion removed and propagated into the radius; the radius given for the case that the planet orbits each candidate host, or that case ruled out; residual undetected companions accounted for in the radius uncertainty or the false-positive analysis.

**Benchmark.** [5], [8], [9]

## 5. Host star parameters

**Question.** How were the host star's radius, mass and evolutionary state determined (spectroscopy, parallax, asteroseismology, isochrones), and is the uncertainty in the stellar radius carried into the planet radius?

**Why it matters.** The transit measures the ratio of planet to star radius, so the planet radius is only as accurate as the stellar radius. Stellar radii from photometric catalogues have been revised substantially once parallaxes became available, and stars misclassified as dwarfs when they are subgiants, or unresolved binaries with inflated luminosities, give biased planet radii.

**Resolved by.** The method and data behind each stellar parameter stated, preferably with a parallax-based luminosity or radius; the evolutionary state checked against the position in the colour-magnitude or Hertzsprung-Russell diagram; stellar radius uncertainty propagated into the planet radius; signs of binarity, such as excess luminosity for the spectral type, discussed.

**Benchmark.** [6], [10]

## 6. Limb darkening and the transit fit

**Question.** How was limb darkening treated (which law, coefficients fixed to model atmospheres or fitted, with what priors), and are the fitted radius ratio and impact parameter shown to be robust to that choice?

**Why it matters.** Limb darkening shapes the transit and is degenerate with the radius ratio and the geometry of the transit. Fixing coefficients to one stellar atmosphere model ties the result to that model and hides its uncertainty, while fitting them with unphysical bounds or poor parameterisations gives strong correlations and unrealistic errors. Biases from either choice can reach a few per cent in the radius ratio and more in the orbital geometry, which matters when quoted uncertainties are smaller.

**Resolved by.** The limb darkening law and the source of any fixed or prior values stated; coefficients fitted within physical bounds using a parameterisation that samples them uniformly, or fixed values justified for the data quality and impact parameter; the radius ratio and impact parameter compared between fixed and fitted treatments, or the limb darkening uncertainty included in their errors.

**Benchmark.** [11], [12]

## 7. Integration time, eccentricity and stellar density

**Question.** Does the transit model account for the exposure time of the data, and is the stellar density implied by the light curve compared with the independently determined stellar density?

**Why it matters.** Long exposures smear ingress and egress, which, if the model is not integrated over the exposure, biases the impact parameter upward and the scaled orbital distance and light-curve stellar density downward. The light curve fixes the stellar density only for a circular orbit around the assumed star: a mismatch with the spectroscopic or parallax-based density can reveal an eccentric orbit, a blend or a wrong host star, and fitted eccentricities from light curves depend on that comparison.

**Resolved by.** The cadence stated and the model supersampled or integrated over the exposure for long-cadence data; the light-curve stellar density, or the scaled orbital distance, compared with the independent value; any disagreement interpreted, with eccentricity, dilution and host-star identity considered; eccentricity claims from photometry accompanied by the stellar density prior used and the degeneracy with impact parameter discussed.

**Benchmark.** [6], [13], [14]

## 8. Statistical validation

**Question.** When a planet is called validated rather than confirmed by a mass measurement, which false-positive scenarios were included, which observations constrain them, what priors and population models were assumed, and what false-positive probability threshold was applied?

**Why it matters.** Validation computes the probability of a planet against blended, hierarchical and target eclipsing binaries and planets on other stars, and the result depends on the assumed stellar populations, binary fractions, planet occurrence and the area within which contaminating stars cannot be excluded. Different tools include different scenarios and priors, and results can shift by factors of a few between runs or with changed assumptions. Multiplicity raises the prior that a candidate is a planet, but only under assumptions that can fail for some systems.

**Resolved by.** The tool and version, the scenarios considered and the inputs used (imaging contrast curves, spectroscopic parameters, secondary eclipse limits, centroid exclusion radius) listed; the FPP and, where relevant, the probability that a nearby star is the source given with the threshold adopted; sensitivity to the main priors shown; any multiplicity boost stated separately, with its assumptions; the word confirmed reserved for planets whose mass or planetary nature has been measured independently.

**Benchmark.** [5], [8], [15]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | F. Pont, S. Zucker and D. Queloz, The effect of red noise on planetary transit detection, Mon. Not. R. Astron. Soc. 373, 231–242 (2006); read as arXiv:astro-ph/0608597 | doi:10.1111/j.1365-2966.2006.11012.x | full text | Secs. 2.3 to 2.6 and 2.9: with correlated noise the uncertainty of the in-transit mean stops falling as the square root of the number of points; significance estimated from the variance of means over windows of transit duration, with a red-noise floor. Sec. 3.2: white-noise fit errors underestimate parameter uncertainties |
| 2 | M. Hippke, T. J. David, G. D. Mulders and R. Heller, Wōtan: comprehensive time-series detrending in Python, Astron. J. 158, 143 (2019); read as arXiv:1906.00966 | doi:10.3847/1538-3881/ab3984 | full text | Sec. 1 and Fig. 1: a non-robust filter overfits in-transit points and reduces the depth by about 15%. Secs. 4.1 to 4.3: tests on injected and real shallow planets show recovery rates differ between detrending methods, though for some samples they perform similarly. Sec. 4.6 and Sec. 6: a window of about three transit durations is optimal. Secs. 5.1 and 5.4: mask transits when the ephemeris is known |
| 3 | J. L. Christiansen et al., Measuring transit signal recovery in the Kepler pipeline. III. Completeness of the Q1–Q17 DR24 planet candidate catalogue, with important caveats for occurrence rate calculations, Astrophys. J. 828, 99 (2016); read as arXiv:1605.05729 | doi:10.3847/0004-637X/828/2/99 | full text | Sec. 1: the missed-planet rate is essential to occurrence rates; Sec. 3: measured by injecting simulated transits into calibrated pixels. Sec. 4: detection efficiency is fitted as a smooth function of signal strength that is well below one at the 7.1 sigma threshold, and falls at long periods. Sec. 5: wrong detection efficiencies give large systematic errors in occurrence rates |
| 4 | J. L. Coughlin et al., Planetary candidates observed by Kepler. VII. The first fully uniform catalog based on the entire 48-month data set (Q1–Q17 DR24), Astrophys. J. Suppl. Ser. 224, 12 (2016); read as arXiv:1512.06149 | doi:10.3847/0067-0049/224/1/12 | full text | Sec. 3.2: signals that are not transit-shaped, from quasi-sinusoidal variability or systematics, or dominated by a single event are flagged. Sec. 3.3: depth or inferred radius alone does not reject a candidate; Secs. 3.3.1 to 3.3.3: significant secondary eclipses and odd-even depth differences flag eclipsing binaries, including those detected at half the true period. Sec. 3.4: difference-image centroid offsets flag signals from nearby stars. Sec. 3.5: period and epoch matches to other stars flag contamination |
| 5 | T. D. Morton, An efficient automated validation procedure for exoplanet transit candidates, Astrophys. J. 761, 6 (2012); read as arXiv:1206.1568 | doi:10.1088/0004-637X/761/1/6 | full text | Sec. 2: blended, hierarchical-triple and target eclipsing binary scenarios and blended planets. Sec. 3.2: imaging contrast curves, confusion radius from centroids, spectroscopic parameters and secondary eclipse limits constrain the scenarios. Sec. 3.3: trapezoid shape compared with each scenario. Sec. 3: validated if FPP is well below 1%. Secs. 3.1 and 4.4: results depend on population assumptions, scale with the dominant prior and vary by factors of a few between runs |
| 6 | S. Seager and G. Mallén-Ornelas, A unique solution of planet and star parameters from an extrasolar planet transit light curve, Astrophys. J. 585, 1038–1055 (2003); read as arXiv:astro-ph/0206228 | doi:10.1086/346105 | full text | Secs. 2 and 3.2: depth, durations and period give radius ratio, impact parameter, scaled orbital distance and stellar density, assuming a circular orbit and no blend; planet radius scales with stellar radius. Secs. 6.1 to 6.3: stellar density checks the host's luminosity class; a blend lowers the inferred density, and comparison with the spectral type can reveal it; box-shaped transits are least likely to hide blends |
| 7 | S. T. Bryson et al., Identification of background false positives from Kepler data, Publ. Astron. Soc. Pac. 125, 889–923 (2013); read as arXiv:1303.0052 | doi:10.1086/671767 | full text | Sec. 1: background false positives are a large fraction of signals at low Galactic latitude; a faint eclipsing binary diluted by the target mimics a small planet; sources very close to the target cannot be detected. Secs. 2 and 3: flux-weighted centroid and difference-image methods; Secs. 2.2.1, 2.3.1 and 3.3.1: biases from aperture choice, bright or variable neighbours and PRF model errors |
| 8 | S. Giacalone et al., Vetting of 384 TESS Objects of Interest with TRICERATOPS and statistical validation of 12 planet candidates, Astron. J. 161, 24 (2021, online 2020); read as arXiv:2002.00691 | doi:10.3847/1538-3881/abc6af | full text | Sec. 1: large pixels let several stars contribute flux to one aperture. Sec. 2.1: the flux each nearby star contributes to the aperture is computed. Sec. 2.2 and Table 1: scenarios for unresolved bound and chance-aligned companions and for each nearby star able to produce the depth, including binaries at twice the period. Secs. 2.4 and 4.1: thresholds on FPP and on the nearby false-positive probability. Secs. 2.1, 2.4.1, 2.4.3 and 4.1: caveats on simplified PSF, omitted priors, assumed circular orbits and small calibration sample. Sec. 3.1: adaptive optics imaging lowers the FPP of an example candidate |
| 9 | D. R. Ciardi, C. A. Beichman, E. P. Horch and S. B. Howell, Understanding the effects of stellar multiplicity on the derived planet radii from transit surveys: implications for Kepler, K2, and TESS, Astrophys. J. 805, 16 (2015); read as arXiv:1503.03516 | doi:10.1088/0004-637X/805/1/16 | full text | Sec. 2, Eqs. 1 to 7: companion light dilutes the depth, so single-star radii are too small; if the planet orbits a fainter companion the correction can be several times larger. Sec. 4.2: radial velocity and high-resolution imaging vetting reduce the average correction, and a sizeable fraction of possible companions remain undetected |
| 10 | T. A. Berger, D. Huber, E. Gaidos and J. L. van Saders, Revised radii of Kepler stars and planets using Gaia Data Release 2, Astrophys. J. 866, 99 (2018); read as arXiv:1805.00231 | doi:10.3847/1538-4357/aada83 | full text | Abstract and Secs. 2.2 and 3.2: parallax-based radii are several times more precise than catalogue radii and differ from them by a median of about 12% with large scatter. Secs. 3.1 to 3.3: subgiants previously classed as dwarfs and binary candidates with inflated radii. Sec. 4.2: planet radii recomputed as radius ratio times revised stellar radius |
| 11 | D. M. Kipping, Efficient, uninformative sampling of limb darkening coefficients for two-parameter laws, Mon. Not. R. Astron. Soc. 435, 2152–2160 (2013); read as arXiv:1308.0009 | doi:10.1093/mnras/stt1435 | full text | Sec. 1: fixing coefficients amounts to a delta-function prior and makes results depend on the atmosphere model. Secs. 2.1, 2.3 and 2.5: physical bounds form a triangle sampled uniformly by a reparameterisation. Sec. 3.2: coefficients are degenerate with the geometry and size of the eclipsing body, and the reparameterisation reduces their correlation |
| 12 | N. Espinoza and A. Jordán, Limb darkening and exoplanets: testing stellar model atmospheres and identifying biases in transit parameters, Mon. Not. R. Astron. Soc. 450, 1879–1899 (2015); read as arXiv:1503.07020 | doi:10.1093/mnras/stv744 | full text | Abstract and Secs. 4.3 and 4.4: fitting or fixing quadratic coefficients biases the radius ratio by up to about 1% and 3% respectively, and the scaled orbital distance and inclination by more. Sec. 4.3: which choice is less biased depends on impact parameter and photometric precision. Sec. 6: letting quadratic coefficients float is recommended to minimise bias |
| 13 | D. M. Kipping, Binning is sinning: morphological light-curve distortions due to finite integration time, Mon. Not. R. Astron. Soc. 408, 1758–1769 (2010); read as arXiv:1004.3741 | doi:10.1111/j.1365-2966.2010.17242.x | full text | Sec. 2.1: long integration lengthens apparent ingress and egress, overestimates impact parameter and underestimates scaled orbital distance and light-curve stellar density. Secs. 3.1 to 3.5: integrate or resample the model within each exposure. Sec. 4.4: short- and long-cadence fits agree once this is done |
| 14 | R. I. Dawson and J. A. Johnson, The photoeccentric effect and proto-hot Jupiters. I. Measuring photometric eccentricities of individual transiting planets, Astrophys. J. 756, 122 (2012); read as arXiv:1203.5537 | doi:10.1088/0004-637X/756/2/122 | full text | Sec. 2: a circular-orbit fit to an eccentric transit returns a stellar density scaled by a function of eccentricity and argument of periapse, so comparison with an independent density constrains eccentricity. Sec. 1: impact parameter and eccentricity both change the duration, and resolving ingress and egress separates them. Sec. 2.1: with unresolved ingress and egress, often for small planets, scaled orbital distance is degenerate with impact parameter |
| 15 | J. J. Lissauer et al., Almost all of Kepler's multiple-planet candidates are planets, Astrophys. J. 750, 112 (2012); read as arXiv:1201.5424 | doi:10.1088/0004-637X/750/2/112 | full text | Secs. 2 and 2.1: if false positives are spread randomly over targets, multiple candidates on one star are unlikely to be false positives, giving a multiplicative boost to the planet probability. Secs. 2.2, 2.4 and 3: the assumptions can fail, for example for planets around different stars in a binary, and the authors do not treat all multis as validated |
