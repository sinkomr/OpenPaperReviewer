---
id: T-EXOPLANET-TRANSITS
name: Exoplanet transits
type: technique
field: physics/astrophysics
applies_when: the paper reports a planet or planet candidate found by transit photometry, validates or confirms a transiting planet, or bases a claim about planet radius, orbit, eccentricity, occurrence rate or false-positive probability on transit light curves
version: "0.1"
---

# Exoplanet transits

## 1. Detection statistic and individual transits

**Question.** What detection statistic and threshold were used, how many individual transits contribute to the signal, and was the signal tested against instrumental artefacts and stellar variability?

**Why it matters.** Detection efficiency rises gradually above the nominal threshold rather than as a step, so claims about non-detections or occurrence need measured completeness. Periodic systematics, quasi-sinusoidal variability or a single strong event can produce a detection that is not transit-shaped.

**Resolved by.** The detection statistic, threshold and number of transits stated; individual transits shown with consistent depths, and the detection not dominated by one event or by a non-transit shape; for completeness or occurrence claims, injection and recovery of simulated transits through the same pipeline.

**Benchmark.** [1], [2]

## 2. Eclipsing binary signatures on the target

**Question.** Does the paper test the light curve for signs that the target itself is an eclipsing binary: different depths of odd and even transits, a secondary eclipse, a V-shaped or grazing transit, or a shape and duration that do not fit a planet around the assumed star?

**Why it matters.** An eclipsing binary seen at half its true period, or a grazing binary eclipse, can give a periodic dip similar to a planetary transit. The presence of a significant secondary eclipse, unequal alternating depths and a transit shape that matches binary scenarios better than a planet are standard diagnostics, and a depth on its own does not decide the question.

**Resolved by.** Odd and even transits fitted separately with their depths and the significance of any difference given; a search for a secondary eclipse at all phases, with an upper limit when none is seen; the transit shape (ingress, egress and flat bottom) shown and compared with planetary and binary models; the duration and shape checked against what the host star's density allows.

**Benchmark.** [2], [3], [4]

## 3. Location of the transit source

**Question.** Does the paper show that the transit occurs on the target star and not on a nearby star blended in the aperture, using difference images, centroid shifts, ephemeris matching against neighbouring stars or higher-resolution photometry?

**Why it matters.** A faint eclipsing binary within the photometric aperture, diluted by the brighter target, can produce a shallow dip that mimics a small planet. Such background false positives are common in crowded, low Galactic latitude fields and with large detector pixels, and centroid methods can be biased by bright neighbours and cannot resolve sources very close to the target.

**Resolved by.** A difference-image or centroid analysis with the measured offset and its uncertainty compared with the positions of known nearby stars; the radius within which a contaminating source cannot be excluded stated; nearby stars bright enough to produce the observed depth listed and either ruled out by photometry at higher resolution or included in the false-positive analysis; a check that the period and epoch do not match a known variable or eclipsing binary nearby.

**Benchmark.** [2], [5], [6]

## 4. Dilution by unresolved companions

**Question.** Has the target been searched for unresolved stellar companions by high-resolution imaging or spectroscopy, and is the transit depth corrected for any light they contribute, with the possibility considered that the planet orbits a companion?

**Why it matters.** Light from an unresolved star adds to the flux and makes the transit shallower, so a radius derived for a single star is too small. If the planet orbits a fainter companion instead of the primary, the true radius can be several times larger than the derived one, which can change a planet into a star or a binary eclipse.

**Resolved by.** High-resolution imaging with contrast curves, and spectra or radial velocities that limit close companions, reported with their detection limits; the flux contribution of known nearby stars in the aperture and of any detected companion removed and propagated into the radius; the radius given for the case that the planet orbits each candidate host, or that case ruled out; residual undetected companions accounted for in the radius uncertainty or the false-positive analysis.

**Benchmark.** [3], [6], [7]

## 5. Host star parameters

**Question.** How were the host star's radius, mass and evolutionary state determined (spectroscopy, parallax, asteroseismology, isochrones), and is the uncertainty in the stellar radius carried into the planet radius?

**Why it matters.** The transit measures the ratio of planet to star radius, so the planet radius is only as accurate as the stellar radius. Stellar radii from photometric catalogues have been revised substantially once parallaxes became available, and stars misclassified as dwarfs when they are subgiants, or unresolved binaries with inflated luminosities, give biased planet radii.

**Resolved by.** The method and data behind each stellar parameter stated, preferably with a parallax-based luminosity or radius; the evolutionary state checked against the position in the colour-magnitude or Hertzsprung-Russell diagram; stellar radius uncertainty propagated into the planet radius; signs of binarity, such as excess luminosity for the spectral type, discussed.

**Benchmark.** [4], [8]

## 6. Limb darkening and the transit fit

**Question.** How was limb darkening treated (which law, coefficients fixed to model atmospheres or fitted, with what priors), and are the fitted radius ratio and impact parameter shown to be robust to that choice?

**Why it matters.** Limb darkening shapes the transit and is degenerate with the radius ratio and the geometry of the transit. Fixing coefficients to one stellar atmosphere model ties the result to that model and hides its uncertainty, while fitting them with unphysical bounds or poor parameterisations gives strong correlations and unrealistic errors. Biases from either choice can reach a few per cent in the radius ratio and more in the orbital geometry, which matters when quoted uncertainties are smaller.

**Resolved by.** The limb darkening law and the source of any fixed or prior values stated; coefficients fitted within physical bounds using a parameterisation that samples them uniformly, or fixed values justified for the data quality and impact parameter; the radius ratio and impact parameter compared between fixed and fitted treatments, or the limb darkening uncertainty included in their errors.

**Benchmark.** [9], [10]

## 7. Integration time, eccentricity and stellar density

**Question.** Does the transit model account for the exposure time of the data, and is the stellar density implied by the light curve compared with the independently determined stellar density?

**Why it matters.** Long exposures smear ingress and egress, which, if the model is not integrated over the exposure, biases the impact parameter upward and the scaled orbital distance and light-curve stellar density downward. The light curve fixes the stellar density only for a circular orbit around the assumed star: a mismatch with the spectroscopic or parallax-based density can reveal an eccentric orbit, a blend or a wrong host star, and fitted eccentricities from light curves depend on that comparison.

**Resolved by.** The cadence stated and the model supersampled or integrated over the exposure for long-cadence data; the light-curve stellar density, or the scaled orbital distance, compared with the independent value; any disagreement interpreted, with eccentricity, dilution and host-star identity considered; eccentricity claims from photometry accompanied by the stellar density prior used and the degeneracy with impact parameter discussed.

**Benchmark.** [4], [11], [12]

## 8. Statistical validation

**Question.** When a planet is called validated rather than confirmed by a mass measurement, which false-positive scenarios were included, which observations constrain them, what priors and population models were assumed, and what false-positive probability threshold was applied?

**Why it matters.** Validation computes the probability of a planet against blended, hierarchical and target eclipsing binaries and planets on other stars, and the result depends on the assumed stellar populations, binary fractions, planet occurrence and the area within which contaminating stars cannot be excluded. Different tools include different scenarios and priors, and results can shift by factors of a few between runs or with changed assumptions. Multiplicity raises the prior that a candidate is a planet, but only under assumptions that can fail for some systems.

**Resolved by.** The tool and version, the scenarios considered and the inputs used (imaging contrast curves, spectroscopic parameters, secondary eclipse limits, centroid exclusion radius) listed; the FPP and, where relevant, the probability that a nearby star is the source given with the threshold adopted; sensitivity to the main priors shown; any multiplicity boost stated separately, with its assumptions; the word confirmed reserved for planets whose mass or planetary nature has been measured independently.

**Benchmark.** [3], [6], [13]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | J. L. Christiansen et al., Measuring transit signal recovery in the Kepler pipeline. III. Completeness of the Q1–Q17 DR24 planet candidate catalogue, with important caveats for occurrence rate calculations, Astrophys. J. 828, 99 (2016); read as arXiv:1605.05729 | doi:10.3847/0004-637X/828/2/99 |
| 2 | J. L. Coughlin et al., Planetary candidates observed by Kepler. VII. The first fully uniform catalog based on the entire 48-month data set (Q1–Q17 DR24), Astrophys. J. Suppl. Ser. 224, 12 (2016); read as arXiv:1512.06149 | doi:10.3847/0067-0049/224/1/12 |
| 3 | T. D. Morton, An efficient automated validation procedure for exoplanet transit candidates, Astrophys. J. 761, 6 (2012); read as arXiv:1206.1568 | doi:10.1088/0004-637X/761/1/6 |
| 4 | S. Seager and G. Mallén-Ornelas, A unique solution of planet and star parameters from an extrasolar planet transit light curve, Astrophys. J. 585, 1038 (2003); read as arXiv:astro-ph/0206228 | doi:10.1086/346105 |
| 5 | S. T. Bryson et al., Identification of background false positives from Kepler data, Publ. Astron. Soc. Pac. 125, 889 (2013); read as arXiv:1303.0052 | doi:10.1086/671767 |
| 6 | S. Giacalone et al., Vetting of 384 TESS Objects of Interest with TRICERATOPS and statistical validation of 12 planet candidates, Astron. J. 161, 24 (2021, online 2020); read as arXiv:2002.00691 | doi:10.3847/1538-3881/abc6af |
| 7 | D. R. Ciardi et al., Understanding the effects of stellar multiplicity on the derived planet radii from transit surveys: implications for Kepler, K2, and TESS, Astrophys. J. 805, 16 (2015); read as arXiv:1503.03516 | doi:10.1088/0004-637X/805/1/16 |
| 8 | T. A. Berger et al., Revised radii of Kepler stars and planets using Gaia Data Release 2, Astrophys. J. 866, 99 (2018); read as arXiv:1805.00231 | doi:10.3847/1538-4357/aada83 |
| 9 | D. M. Kipping, Efficient, uninformative sampling of limb darkening coefficients for two-parameter laws, Mon. Not. R. Astron. Soc. 435, 2152 (2013); read as arXiv:1308.0009 | doi:10.1093/mnras/stt1435 |
| 10 | N. Espinoza and A. Jordán, Limb darkening and exoplanets: testing stellar model atmospheres and identifying biases in transit parameters, Mon. Not. R. Astron. Soc. 450, 1879 (2015); read as arXiv:1503.07020 | doi:10.1093/mnras/stv744 |
| 11 | D. M. Kipping, Binning is sinning: morphological light-curve distortions due to finite integration time, Mon. Not. R. Astron. Soc. 408, 1758 (2010); read as arXiv:1004.3741 | doi:10.1111/j.1365-2966.2010.17242.x |
| 12 | R. I. Dawson and J. A. Johnson, The photoeccentric effect and proto-hot Jupiters. I. Measuring photometric eccentricities of individual transiting planets, Astrophys. J. 756, 122 (2012); read as arXiv:1203.5537 | doi:10.1088/0004-637X/756/2/122 |
| 13 | J. J. Lissauer et al., Almost all of Kepler's multiple-planet candidates are planets, Astrophys. J. 750, 112 (2012); read as arXiv:1201.5424 | doi:10.1088/0004-637X/750/2/112 |
