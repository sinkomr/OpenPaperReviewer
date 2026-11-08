---
id: T-PHOTOMETRY
name: Photometry and light curves
type: technique
field: physics/astrophysics
applies_when: the paper measures the brightness of astronomical sources in images, builds light curves by aperture, point-spread-function or differential photometry, or bases a claim about magnitudes, fluxes, colours, variability, periods, transits, eclipses or event timing on them
version: "0.1"
---

# Photometry and light curves

## 1. Photometric system and flux calibration

**Question.** In which passband and magnitude system are the brightnesses reported, how was the zero point set (which standard stars or reference spectra), and how were colour terms and atmospheric extinction handled when converting instrumental counts to magnitudes or fluxes?

**Why it matters.** A magnitude or flux is defined only for a stated passband and zero point, and converting counts to flux needs the system throughput. Colour terms that map an instrumental system onto a standard one depend on the spectrum of the source, so terms derived from ordinary stars can be wrong at the percent level or worse for sources with different spectra. Atmospheric extinction includes molecular absorption that does not scale simply with airmass.

**Resolved by.** The filter, detector and magnitude system named, with the standards or reference spectra behind the zero point and their own uncertainty; the transformation equations, colour terms and extinction coefficients given with the colour range over which they were fitted; a statement of whether the targets lie within that colour range; absolute values quoted only where the calibration supports them, and relative photometry labelled as relative.

**Benchmark.** [1], [2]

## 2. Comparison stars

**Question.** Which comparison stars were used for differential photometry, how were they chosen and weighted, how were variable comparison stars found and removed, and does a separate check star show the precision reached?

**Why it matters.** Differential photometry removes transparency changes only to the extent that the comparison stars share them and are themselves constant. A variable comparison star puts its own signal, inverted, into the target light curve. When the target's colour differs from that of the comparison stars, changes in atmospheric absorption, such as water vapour, affect them differently and can produce slow trends or transit-like dips in the differential light curve.

**Resolved by.** The comparison stars identified, with their brightness, colour and distance from the target; the weighting scheme and the rule for rejecting variable stars stated; the light curves of the comparison stars, or of a check star not used in the ensemble, shown to be flat at the level of the claimed signal; where the target and comparison stars differ in colour, an estimate or correction of colour-dependent extinction.

**Benchmark.** [3], [4], [5]

## 3. Aperture, point-spread function and contamination

**Question.** How were the aperture size or PSF model chosen, was the choice fixed or varied with seeing, and does the paper show that the signal comes from the target and not from a neighbouring source inside the aperture?

**Why it matters.** Too small an aperture adds correlated noise as the image width and airmass change; too large an aperture adds sky noise and light from neighbours, and an aperture chosen to minimise scatter can also suppress real variability. Flux from nearby stars dilutes a signal on the target, and a faint eclipsing or variable star in the aperture can produce a small dip that mimics a signal on the target.

**Resolved by.** The aperture radius or PSF model stated with the rule used to choose it, and the result shown to hold for other reasonable apertures; the fraction of flux in the aperture from known neighbours estimated and the depth or amplitude corrected for it; for small signals, a test of where the signal originates, such as centroid shifts during the event, difference images, or photometry in smaller apertures.

**Benchmark.** [4], [5], [6]

## 4. Detrending of instrumental systematics

**Question.** What detrending was applied to remove instrumental trends (the method, its free parameters, any window length, and which data were masked), and does the paper show that the method preserves signals of the kind and time-scale it claims?

**Why it matters.** Pointing drift, focus and temperature changes and similar effects put trends into light curves that are often larger than the signal. A detrending fit can absorb part of an astrophysical signal, reduce a transit depth, distort intrinsic stellar variability, or add noise; a filter with too short a window fits out the signal, and some methods can create transit-like features that were not in the data.

**Resolved by.** The method and its parameters stated, with the window length compared with the time-scale of the claimed signal; the signal masked during the fit or the trend and signal fitted together; light curves shown before and after detrending; injection and recovery of synthetic signals of the claimed size and time-scale showing how much the detrending retains.

**Benchmark.** [7], [8]

## 5. Noise model and correlated noise

**Question.** Does the paper give a noise budget that includes photon, sky, detector and, for bright stars observed from the ground, scintillation noise, and does it measure how much of the remaining noise is correlated in time?

**Why it matters.** The significance of a dip or bump depends on the noise on the time-scale of the event. Correlated noise from airmass, seeing, tracking and flat-field errors does not average down as the square root of the number of points, so a white-noise estimate can overstate significance by a large factor. Scintillation can dominate for bright stars and is underestimated by the commonly used approximation.

**Resolved by.** Expected and measured scatter compared, with the scintillation estimate and its basis stated; the scatter of binned data plotted against bin size, or an equivalent measure of correlated noise; significances and uncertainties computed with the correlated noise included, on the time-scale of the claimed signal.

**Benchmark.** [9], [10]

## 6. Evidence for variability

**Question.** How is a source judged to be variable: which variability index or test was used, against what distribution for constant stars of similar brightness in the same data, and how were image artefacts and blends excluded?

**Why it matters.** Photometric scatter grows with faintness and differs between fields and nights, so an index is meaningful only relative to that of constant stars measured the same way. Cosmetic detector defects, diffraction spikes, cosmic rays, blending and night-to-night zero-point shifts can each make a constant star look variable, and different indices respond differently to outliers and to variability on short and long time-scales.

**Resolved by.** The index and threshold stated, with the source's value shown against the distribution for stars of similar magnitude in the same data; an index suited to the time-scale of the claimed variability; candidate light curves inspected for artefacts, and checked against nearby bright variables and independent data; the fraction of constant stars that pass the same threshold reported.

**Benchmark.** [3], [5], [11]

## 7. Periods and sampling

**Question.** When a period is claimed, does the paper show the periodogram with its window function, consider aliases and harmonics of the strongest peak, and state how the false-alarm probability was computed and what noise it assumes?

**Why it matters.** Uneven sampling, especially daily gaps from the ground, produces aliases, and the highest peak is often not the true period. A false-alarm probability gives the chance that noise alone yields such a peak, not the probability that the period is right; its analytic estimates assume Gaussian noise, and simple bootstrap estimates do not account for correlated noise.

**Resolved by.** The periodogram shown over a stated frequency grid with the window function; light curves folded at the main peak and at its likely aliases and harmonics; a false-alarm probability from a stated method, such as bootstrap or an analytic bound, with its noise assumptions; injection tests where detection efficiency matters to the claim.

**Benchmark.** [12]

## 8. Time stamps

**Question.** For claims that rest on the timing of events, such as transit times, eclipse times or period changes, does the paper state the time system of its time stamps and how they were converted, for example to Barycentric Julian Date in Barycentric Dynamical Time?

**Why it matters.** Time systems in common use differ by up to about a minute, and heliocentric dates differ from barycentric ones by up to about 8 s. Combining data with mixed or unstated time systems can create apparent timing variations or period changes, and instrument clocks and header times may themselves be off by seconds.

**Resolved by.** The time system stated for every data set, including literature times used in the analysis; the conversion method and the target coordinates used; the observatory arrival times reported alongside the barycentric times; the accuracy of the instrument clock or exposure time stamps stated and compared with the size of the claimed timing effect.

**Benchmark.** [13]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | C. W. Stubbs and J. L. Tonry, Toward 1% photometry: end-to-end calibration of astronomical telescopes and detectors, Astrophys. J. 646, 1436 (2006); read as preprint arXiv:astro-ph/0604285 | doi:10.1086/505138 |
| 2 | R. C. Bohlin et al., Techniques and review of absolute flux calibration from the ultraviolet to the mid-infrared, Publ. Astron. Soc. Pac. 126, 711 (2014); read as preprint arXiv:1406.1707 | doi:10.1086/677655 |
| 3 | A. Y. Burdanov et al., Astrokit: an efficient program for high-precision differential CCD photometry and search for variable stars, Astrophys. Bull. 69, 368 (2014); read as preprint arXiv:1408.0664 | doi:10.1134/S1990341314030122 |
| 4 | C. A. Murray et al., Photometry and performance of SPECULOOS-South, Mon. Not. R. Astron. Soc. 495, 2446 (2020); read as preprint arXiv:2005.02423 | doi:10.1093/mnras/staa1283 |
| 5 | J. L. Tonry et al., A search for variable stars and planetary occultations in NGC 2301. I. Techniques, Publ. Astron. Soc. Pac. 117, 281 (2005); read as preprint arXiv:astro-ph/0501052 | doi:10.1086/428596 |
| 6 | S. T. Bryson et al., Identification of background false positives from Kepler data, Publ. Astron. Soc. Pac. 125, 889 (2013); read as preprint arXiv:1303.0052 | doi:10.1086/671767 |
| 7 | M. Hippke et al., Wotan: comprehensive time-series detrending in Python, Astron. J. 158, 143 (2019); read as preprint arXiv:1906.00966 | doi:10.3847/1538-3881/ab3984 |
| 8 | J. C. Smith et al., Kepler presearch data conditioning II: a Bayesian approach to systematic error correction, Publ. Astron. Soc. Pac. 124, 1000 (2012); read as preprint arXiv:1203.1383 | doi:10.1086/667697 |
| 9 | F. Pont et al., The effect of red noise on planetary transit detection, Mon. Not. R. Astron. Soc. 373, 231 (2006); read as preprint arXiv:astro-ph/0608597 | doi:10.1111/j.1365-2966.2006.11012.x |
| 10 | J. Osborn et al., Atmospheric scintillation in astronomical photometry, Mon. Not. R. Astron. Soc. 452, 1707 (2015); read as preprint arXiv:1506.06921 | doi:10.1093/mnras/stv1400 |
| 11 | K. V. Sokolovsky et al., Comparative performance of selected variability detection techniques in photometric time series data, Mon. Not. R. Astron. Soc. 464, 274 (2017); read as preprint arXiv:1609.01716 | doi:10.1093/mnras/stw2262 |
| 12 | J. T. VanderPlas, Understanding the Lomb–Scargle periodogram, Astrophys. J. Suppl. Ser. 236, 16 (2018); read as preprint arXiv:1703.09824 | doi:10.3847/1538-4365/aab766 |
| 13 | J. Eastman et al., Achieving better than 1 minute accuracy in the heliocentric and barycentric Julian dates, Publ. Astron. Soc. Pac. 122, 935 (2010); read as preprint arXiv:1005.4415 | doi:10.1086/655938 |
