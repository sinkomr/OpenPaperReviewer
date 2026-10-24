---
id: T-RADIAL-VELOCITIES
name: Exoplanet radial velocities
type: technique
field: physics/astrophysics
applies_when: the paper measures stellar radial velocities with a spectrograph, analyses a radial-velocity time series with periodograms or Keplerian fits, or bases a claim of a planet, its period, eccentricity, minimum mass or mass on Doppler data
version: "0.1"
---

# Exoplanet radial velocities

Radial-velocity (RV) measurements are used to claim that a star is orbited by one or more planets and to give each planet's period, eccentricity and minimum mass (m sin i, the planet mass times the sine of the orbital inclination). The claim rests on separating a small, strictly periodic Doppler shift from instrumental drifts, sampling effects and velocity signals produced by the star itself.

## 1. Instrumental precision and the error budget

**Question.** What per-measurement uncertainty does the paper quote, which terms does it include (photon noise, wavelength calibration, instrumental drift), how does it compare with the scatter of the velocities about the final model and with the amplitude of the claimed signal, and where velocities come from several spectrographs or from before and after an instrument change, are separate zero-point offsets fitted?

**Why it matters.** The internal uncertainty from photon noise, calibration and drift is a lower bound: stellar jitter and other instrumental effects add to it, and quiet stars alone show jitter of about 1 to 3 m/s. A signal whose amplitude is comparable with the true noise level can be produced by an error budget that leaves terms out. Data sets from different spectrographs, or from one spectrograph before and after an upgrade, have different velocity zero points, which must be fitted as free offsets before the series are combined.

**Resolved by.** The instrument, calibration source and drift correction stated; the components of the per-point uncertainty listed; an additional jitter term fitted or justified; the residual scatter compared with the quoted uncertainties; the semi-amplitude of each claimed signal compared with that scatter; a separate offset, and where needed a separate jitter term, for each instrument or instrument configuration.

**Benchmark.** [1], [2], [6]

## 2. Barycentric correction and telluric lines

**Question.** How were the barycentric correction and its exposure-time weighting computed, and how were absorption lines from the Earth's atmosphere masked or modelled?

**Why it matters.** The correction for the Earth's motion is far larger than a planetary signal: a one-second timing error gives a velocity error of a few cm/s, and a correction computed at a single exposure midpoint, even a flux-weighted one, can be off by tens of cm/s for long exposures. Telluric lines, including shallow micro-telluric lines, move across the stellar spectrum with a yearly period and can bias velocities by about 0.2 to 1 m/s in the optical and by at least a few m/s in the near-infrared.

**Resolved by.** The barycentric code stated, with the correction weighted by the flux recorded through the exposure, for example by an exposure meter; a telluric mask or model described, with the spectral regions used; a check that no claimed signal sits near a period of one year.

**Benchmark.** [1]

## 3. Stellar rotation and its harmonics

**Question.** Does the paper determine the stellar rotation period independently, for example from photometry or activity indicators, and does any claimed planetary period lie near that period or its first harmonics?

**Why it matters.** Spots carried round by rotation produce RV signals at the rotation period and at one-half and one-third of it. A planet can be separated from this signal only if its period is away from these values, the rotation period is well known and the data span more than one rotation. In blind tests, some false detections fell at the rotation period, and a harmonic was sometimes taken for the rotation period itself.

**Resolved by.** A rotation period measured from photometry or activity time series, with its uncertainty; the claimed periods compared with the rotation period and its harmonics; where they are close, additional evidence beyond the RVs that the signal is planetary; a time series that covers more than one rotation, and preferably several.

**Benchmark.** [5], [6], [7]

## 4. Activity indicators and signal coherence

**Question.** Are activity indicators (line bisector span, width of the cross-correlation function, emission in the cores of the calcium H and K lines) shown as time series and periodograms alongside the RVs, and does the paper test that the signal is achromatic and coherent over the whole data set?

**Why it matters.** Stellar activity changes line shapes as well as line positions, and its RV signal varies with wavelength and evolves in amplitude and phase, whereas orbital motion gives the same coherent shift at all wavelengths. The indicators are weak for slowly rotating stars and do not always correlate with velocity, so absence of a correlation alone is limited evidence. A planetary signal should grow steadily in significance as data are added, while an activity signal rises and fades.

**Resolved by.** Periodograms of each indicator shown next to the RV periodogram, with no peak at the claimed period; correlations between indicators and velocities given; velocities from separate wavelength ranges compared; the significance or amplitude of the signal tracked as data accumulate, or across separate seasons, and shown to be stable.

**Benchmark.** [1], [2], [5], [7]

## 5. The noise model and its effect on the result

**Question.** How is correlated stellar noise modelled (a jitter term, regression on activity indicators, or a Gaussian process with stated kernel and priors), is it fitted jointly with the planets, and do the detection and the fitted amplitude survive reasonable alternative noise models?

**Why it matters.** Whether a signal is detected, and the period and amplitude it is given, depend on the noise model. An incomplete noise model can inflate the evidence for a planet, and a Gaussian process given a poor rotation period can absorb a planetary signal or leave activity behind. In blind tests, parameter uncertainties were often underestimated because the stellar noise models were imperfect.

**Resolved by.** The noise model, its hyperparameters and their priors stated; planets and stellar signals fitted together; the detection and the semi-amplitude reported under more than one noise model or prior choice, or a model comparison across them; the uncertainty on the amplitude including the spread between models.

**Benchmark.** [1], [2], [6]

## 6. Aliases and the window function

**Question.** Does the paper show the spectral window function of the observations, and does it show that the adopted period, and not one of its aliases, is the true one?

**Why it matters.** Night-time observing from one site and seasonal gaps put strong peaks in the window function near one solar day, one sidereal day and a year. A true signal then appears at several frequencies, and the highest periodogram peak is not always the true period, because noise can boost an alias. The choice of alias changes the period and so the minimum mass.

**Resolved by.** The window function plotted alongside the periodogram; the alias candidates listed; a test in which a sinusoid at each candidate period, sampled at the actual observation times, is compared with the observed peak heights and phases; the fit quality for the competing periods given; where the data cannot decide, the ambiguity stated.

**Benchmark.** [1], [3], [4]

## 7. Significance of the detection

**Question.** How was the significance of each signal assessed (false alarm probability with a stated method, Bayes factor or false inclusion probability), was the search over the full frequency grid accounted for, and is the semi-amplitude well above the noise level?

**Why it matters.** A false alarm probability states only how often noise alone would give a peak as high, maximised over all frequencies searched; it is not the probability that a planet exists, and it does not exclude activity or window effects. The standard periodogram false alarm probability assumes uncorrelated noise unless the noise model is extended, and Bayes factors depend on priors, on the noise model and on how the evidence was computed. In blind tests, recovery fell sharply and false positives rose for signals whose semi-amplitude was below about 7.5 times the RV scatter (after removing activity-correlated trends) divided by the square root of the number of observations.

**Resolved by.** The frequency grid and its limits stated; the false alarm probability computed by bootstrap or an extreme-value method suited to the sampling, or a Bayes factor with priors and the evidence computation described and checked; injection and recovery tests at the claimed amplitude and period; every candidate signal listed with its significance, not only those labelled planets.

**Benchmark.** [1], [2], [4], [6]

## 8. Orbital shape and planetary mass

**Question.** Is a non-zero eccentricity supported against a circular orbit, has the alternative of two planets near a 2:1 period ratio been tested, and is the reported mass labelled as a minimum mass with the stellar mass and its uncertainty propagated?

**Why it matters.** Because eccentricity cannot be negative, the posterior mean or median for a nearly circular orbit overestimates it, typically by one to two times its uncertainty. An eccentric single-planet fit can be indistinguishable from two planets in a 2:1 resonance, which changes the number of planets and their masses. RV data give only m sin i, and its value scales with the assumed stellar mass, so a true mass needs the inclination from another method.

**Resolved by.** A circular model compared with the eccentric one; for eccentric fits, the two-planet 2:1 alternative tested; eccentricity reported with its full posterior and the summary statistic used, noting the bias near zero; the stellar mass, its source and uncertainty stated and carried into the minimum mass; a true mass given only where the inclination is known, for example from transits or measured planet-planet interactions.

**Benchmark.** [2], [8], [9]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | D. A. Fischer, G. Anglada-Escude, P. Arriagada et al., State of the Field: Extreme Precision Radial Velocities, Publ. Astron. Soc. Pac. 128, 066001 (2016); read as arXiv:1602.07939 | doi:10.1088/1538-3873/128/964/066001 | full text | Sec. II.6: internal uncertainty combines photon noise, calibration and drift and is a lower bound to which stellar and other terms add. Sec. IV.2: jitter of about 1 to 3 m/s for quiet stars, time-correlated, from oscillations, granulation, spots and rotation. Sec. IV.2.1: bisectors, cross-correlation width and Ca II H and K as indicators, hard to measure for slow rotators and not reliable on their own. Sec. IV.1 and IV.1.1: false alarm probability shows only that noise is unlikely and does not exclude activity or window effects; incomplete noise models inflate Bayesian evidence; results sensitive to priors. Sec. IV.4: aliases from daily, sidereal and annual gaps. Sec. IV.5: one second of timing error gives about 3 cm/s, and a single flux-weighted midpoint can err by about 25 cm/s for a 30-minute exposure, so flux should be sampled through the exposure. Sec. IV.6: telluric and micro-telluric lines bias velocities by about 0.2 to 1 m/s in the optical and at least a few m/s in the near-infrared |
| 2 | N. C. Hara and E. B. Ford, Statistical methods for exoplanet detection with radial velocities, Annu. Rev. Stat. Appl. 10, 623–649 (2023); read as arXiv:2308.00701 | doi:10.1146/annurev-statistics-033021-012225 | full text | Sec. 2.2 and Eq. 3: the semi-amplitude depends on planet mass, stellar mass, period and eccentricity; RV gives only m sin i, and inclination comes from transits or planet-planet interactions; each instrument needs its own zero-point offset. Sec. 2.3 and Fig. 3: an instrument upgrade introduces an unknown offset; an extra jitter term is added to the variance. Sec. 4.2: activity signals mimic planets and should be fitted jointly with them; correlated-noise models change periodogram power; the base periodogram assumes uncorrelated noise; false alarm probability defined over the periodogram maximum. Sec. 4.3: Bayes factors depend on the priors and the noise model, and numerical evidence estimates can disagree. Appendix E.1: a loosely constrained noise model can absorb planetary signals. Sec. 6.1: velocities estimated in separate bandwidths separate signals common to all wavelengths from other effects. Sec. 7: run several analyses with different likelihoods and priors; list all candidate signals with a significance measure and use injection-recovery tests |
| 3 | R. I. Dawson and D. C. Fabrycky, Radial velocity planets de-aliased: a new, short period for super-Earth 55 Cnc e, Astrophys. J. 722, 937–953 (2010); read as arXiv:1005.4050 | doi:10.1088/0004-637X/722/1/937 | full text | Sec. II.1 and II.2: sampling gaps put peaks in the window function at one solar and one sidereal day and yearly sidebands, producing aliases. Sec. II.4 to II.6: test each candidate by sampling a sinusoid at the observation times and comparing predicted alias heights and phases with the data; the highest peak is not necessarily the true one. Sec. III and Tables 6 and 7: the alias choice changes the period and minimum mass |
| 4 | J. T. VanderPlas, Understanding the Lomb-Scargle periodogram, Astrophys. J. Suppl. Ser. 236, 16 (2018); read as arXiv:1703.09824 | doi:10.3847/1538-4365/aab766 | full text | Sec. IV.2 and VII.2 to VII.3: the window function shapes the periodogram and the highest peak is often an alias or harmonic. Sec. VII.1: the frequency grid and its limits determine what can be found. Sec. VII.4.2: false alarm probability concerns the maximum over correlated frequencies, compared across the independent-frequency, Baluev and bootstrap methods; it is not the probability that the data are periodic. Sec. VIII.1: check the window function and inject known signals |
| 5 | I. Boisse, F. Bouchy, G. Hébrard, X. Bonfils, N. Santos and S. Vauclair, Disentangling between stellar activity and planetary signals, Astron. Astrophys. 528, A4 (2011); read as arXiv:1012.1452 | doi:10.1051/0004-6361/201014354 | full text | Sec. 2.2: spots give RV signals at the rotation period and its first two harmonics. Sec. 2.6: the RV and bisector anticorrelation is shallow with several spots and needs at least about ten points per rotation. Abstract and Sec. 4: separation needs a planet period away from the rotation period and its harmonics, a well-known rotation period and data covering more than one rotation |
| 6 | X. Dumusque, F. Borsa, M. Damasso et al., Radial-velocity fitting challenge. II. First results of the analysis of the data set, Astron. Astrophys. 598, A133 (2017); read as arXiv:1609.03674 | doi:10.1051/0004-6361/201628671 | full text | Abstract and Sec. 4.2.1: blind analyses of simulated data; recovery drops and false positives rise below K/N of 7.5, where K/N is the semi-amplitude over the RV rms (after removing activity-correlated trends) times the square root of the number of points. Sec. 4.2.1 and 4.2.3: some false positives at the stellar rotation period. Sec. 4.1: a harmonic reported instead of the rotation period in 20 to 45% of cases; Gaussian-process teams need a good rotation-period estimate or the process may model planetary signals. Sec. 4.2.2: uncertainties often underestimated because stellar noise models were imperfect |
| 7 | A. Mortier and A. Collier Cameron, Stacked Bayesian general Lomb-Scargle periodogram: identifying stellar activity signals, Astron. Astrophys. 601, A110 (2017); read as arXiv:1702.03885 | doi:10.1051/0004-6361/201630201 | full text | Abstract, Sec. 2 and 5.3: a stable signal grows in significance, roughly as the square root of the number of points, while an activity signal varies in amplitude and phase and can fade. Sec. 6: long-lived active regions look coherent over short baselines, and periods near the rotation period or its harmonics need indicators, photometry and further analysis |
| 8 | N. L. Zakamska, M. Pan and E. B. Ford, Observational biases in determining extrasolar planet eccentricities in single-planet systems, Mon. Not. R. Astron. Soc. 410, 1895–1910 (2011; published online 2010); read as arXiv:1008.4152 | doi:10.1111/j.1365-2966.2010.17570.x | full text | Sec. I: a measured eccentricity for a circular orbit can only overestimate it. Sec. IV.2 and VI: posterior mean and median for nearly circular orbits exceed the true value by about one to two times the uncertainty, strongly below about 0.05; the mode is the least biased summary. Sec. IV.3: precision and bias improve with effective signal-to-noise |
| 9 | G. Anglada-Escudé, M. López-Morales and J. E. Chambers, How eccentric orbital solutions can hide planetary systems in 2:1 resonant orbits, Astrophys. J. 709, 168–178 (2010) | doi:10.1088/0004-637X/709/1/168 | abstract | Abstract: two planets in a 2:1 resonance can give an RV signal like one eccentric planet; about 35% of published eccentric single-planet fits examined could not be distinguished from such a pair, and about 40% not from a circular orbit |
