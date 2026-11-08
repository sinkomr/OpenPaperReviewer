---
id: T-RADIO-INTERFEROMETRY
name: Radio astronomy and interferometry
type: technique
field: physics/astrophysics
applies_when: the paper reports images, flux densities, spectra or detections from a radio or millimetre interferometer (aperture-synthesis array), or bases a claim about compact or extended structure, a spectral line, a faint source or a non-detection on interferometric visibilities or images
version: "0.1"
---

# Radio astronomy and interferometry

## 1. Flux scale and calibrator choice

**Question.** Which sources set the flux-density scale, the bandpass and the time-variable gains, how far from the target and how often was the gain calibrator observed, and what uncertainty in the absolute flux scale is carried into flux densities, spectral indices and comparisons between epochs or instruments?

**Why it matters.** The absolute scale rests on a few standard sources, some of which vary by up to about 20 per cent over a few years or are resolved on long baselines and need a model, and the scale itself is uncertain by a few per cent. Gains transferred from a calibrator are never exact: the errors grow with the angular separation and the time between calibrator scans, and they limit the dynamic range that can be reached without self-calibration.

**Resolved by.** The flux, bandpass and gain calibrators named, with the flux model or catalogue used; a flux calibrator that is stable and suited to the array's resolution, or a model for its structure; the calibrator separation and cycle time stated; a flux-scale uncertainty of a few per cent or more included in quoted flux densities and in any comparison between epochs, bands or instruments.

**Benchmark.** [1], [2]

## 2. Self-calibration

**Question.** Was self-calibration applied, and if so with what starting model, solution interval, signal-to-noise ratio per solution and mode (phase only, or amplitude as well), and does the paper show how the peak flux, integrated flux, noise and source positions changed?

**Why it matters.** Self-calibrating weak data against a point-source model can create a source at the model position out of noise, and a model that contains artefacts can reinforce them. Amplitude self-calibration with an incomplete model can remove flux from extended emission while the noise appears to improve, and a point-source starting model discards the absolute position.

**Resolved by.** Enough signal before self-calibration was attempted, with the signal-to-noise ratio per antenna and solution interval stated; conservative early models; peak flux, integrated flux and noise tracked through the iterations; positions compared before and after; amplitude gains checked for large departures from unity; weak features tested by leaving them out of the model and showing that they persist.

**Benchmark.** [2]

## 3. uv coverage and the largest recoverable scale

**Question.** What range of baselines, in wavelengths, and what uv coverage underlie each image, what is the largest angular scale the data can recover, and does any claim about extended emission, total flux or the absence of extended structure stay within that scale?

**Why it matters.** An interferometer records only spatial frequencies between its shortest and longest baselines, so structure larger than the scale set by the shortest baseline is missing: total flux is underestimated and emission is surrounded by negative bowls. Because the measurements do not determine the image uniquely, deconvolution fills in the unmeasured spatial frequencies, and the result depends on how it does so.

**Resolved by.** The uv coverage or baseline range shown; the largest recoverable scale stated and compared with the size of the source; the interferometric flux compared with a single-dish or lower-resolution total flux; short spacings added from a single dish or a compact array where extended emission matters; data from different arrays compared over a matched range of spatial frequencies.

**Benchmark.** [3], [4]

## 4. Weighting, deconvolution and the restored image

**Question.** Which weighting, taper, deconvolution algorithm, masks and stopping threshold were used, are the synthesised beam and the residual image shown, and how were the deconvolved model and the residuals combined in the image from which fluxes are measured?

**Why it matters.** Weighting trades sensitivity against resolution and sidelobe level, and pixel-based CLEAN represents extended emission poorly, as many point components. The residuals are in units per dirty beam and the model per restoring beam; when the dirty beam has a broad low-level shelf, adding them unscaled can change the flux of faint, extended emission by tens of per cent.

**Resolved by.** The weighting scheme and its parameters, the taper, the restoring beam, the algorithm (scale-sensitive for extended emission), the masks and the threshold stated; residual images that look like noise; the ratio of restoring-beam to dirty-beam volume stated or the residuals rescaled, with the units of quoted fluxes and noise made explicit.

**Benchmark.** [4], [5]

## 5. Wide-field and direction-dependent effects

**Question.** For emission away from the pointing centre, in mosaics or over a wide band, does the paper say where in the primary beam the claimed emission lies and how the primary beam, non-coplanar baselines and the change of beam and source spectrum with frequency were handled?

**Why it matters.** The primary beam differs between antennas and changes with time, frequency and pointing errors, so flux densities and spectral indices far from the centre depend on the beam model, and the noise rises towards the edge of the image. Imaging with a two-dimensional Fourier transform distorts sources far from the phase centre when the baselines are not coplanar, and imaging a wide band as if spectra were flat leaves errors around sources whose spectra vary.

**Resolved by.** The position of the emission relative to the beam stated; the primary-beam model named and a noise map or noise at the source position given; wide-field imaging that corrects for non-coplanar baselines where the field and wavelength require it; a wide-band method that models spectral structure; spectral indices away from the centre checked against the frequency dependence of the beam.

**Benchmark.** [4], [6], [7]

## 6. Radio-frequency interference

**Question.** How was RFI identified and removed (automatic flagging, thresholds, inspection, subtraction), which times and channels were flagged, and are the claimed features clear of interference and of the effects of its removal?

**Why it matters.** Interference can be narrow in time or frequency or drift across the band, and weak, persistent interference spread over the band is hard to detect; left in the data it produces image artefacts and spectral features. Thresholds also flag genuine data, which can bias flux densities, flaggers that smooth across frequency can remove strong spectral lines, and subtracting interference instead of flagging it can leave artefacts of unknown form.

**Resolved by.** The flagging method and its thresholds stated, with the flagged channels and times shown or summarised; the flagging checked by inspection; spectral lines protected from flaggers that would remove them; any claimed line or transient shown not to coincide with flagged or contaminated channels and times, and not to be produced by the mitigation itself.

**Benchmark.** [8]

## 7. Significance of detections in images and cubes

**Question.** How was the noise measured at the position of each detection, how many independent beams and channels were searched, and how was the rate of false detections estimated, for example from the same search run on the negative of the data?

**Why it matters.** Noise varies across an interferometric image and rises near bright sources, where imaging artefacts produce spurious faint sources, and pixels within a beam are not independent, so the number of chances for a noise peak is set by beams and channels searched. In a blind search of a cube many peaks reach a few times the noise by chance, more often for narrow features than broad ones after spectral smoothing, and fitted fluxes of faint sources can be biased.

**Resolved by.** Noise estimated locally or from a noise map, not a single global value; the reliability of each candidate estimated from negative peaks, which noise produces as often as positive ones; completeness and reliability given as a function of signal-to-noise ratio; detections near bright sources treated with caution; candidates confirmed by an independent counterpart or redshift where available.

**Benchmark.** [7], [9], [10]

## 8. Spectral-line calibration, smoothing and continuum subtraction

**Question.** For a claimed spectral line, how was the bandpass calibrated and with what signal-to-noise ratio, what spectral resolution and smoothing apply to the plotted spectrum, how was the continuum subtracted (which line-free channels, what order of fit, in the visibilities or the image), and is the line identification supported independently of the line itself?

**Why it matters.** Noise and errors in the bandpass solution pass directly into the line spectrum, and the finite correlation range gives a sinc-shaped channel response with ringing that smoothing suppresses at the cost of resolution and of correlations between channels. Continuum subtraction by a low-order fit in frequency assumes a smooth continuum within a limited field, and residuals near bright continuum sources can be taken for spectral features; a single line can also be assigned to the wrong transition.

**Resolved by.** The bandpass calibrator and the signal-to-noise ratio of its solution stated; the channel width, effective resolution and any smoothing given; the line-free channels and fit order of the continuum subtraction stated, with residuals checked near bright continuum sources; line width compared with the resolution; the identification supported by other lines or by an independent redshift.

**Benchmark.** [9], [10], [11]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | R. A. Perley and B. J. Butler, An accurate flux density scale from 50 MHz to 50 GHz, Astrophys. J. Suppl. Ser. 230, 7 (2017); read as preprint arXiv:1609.05940 | doi:10.3847/1538-4365/aa6df9 |
| 2 | C. L. Brogan et al., Advanced gain calibration techniques in radio interferometry, lecture for the 2014 Synthesis Imaging Workshop (2018), arXiv:1805.05266 | doi:10.48550/arXiv.1805.05266 |
| 3 | S. Stanimirović, Short-spacings correction from the single-dish perspective, in Single-Dish Radio Astronomy: Techniques and Applications, ASP Conf. Ser. 278 (2002), arXiv:astro-ph/0205329 | doi:10.48550/arXiv.astro-ph/0205329 |
| 4 | U. Rau et al., Advances in calibration and imaging techniques in radio interferometry, Proc. IEEE 97, 1472 (2009); read as preprint arXiv:0902.0817 | doi:10.1109/JPROC.2009.2014853 |
| 5 | I. Czekala et al., Molecules with ALMA at Planet-forming Scales (MAPS). II. CLEAN strategies for synthesizing images of molecular line emission in protoplanetary disks, Astrophys. J. Suppl. Ser. 257, 2 (2021); read as preprint arXiv:2109.06188 | doi:10.3847/1538-4365/ac1430 |
| 6 | T. J. Cornwell et al., The noncoplanar baselines effect in radio interferometry: the W-projection algorithm, IEEE J. Sel. Top. Signal Process. 2, 647 (2008); read as preprint arXiv:0807.4161 | doi:10.1109/JSTSP.2008.2005290 |
| 7 | A. M. Hopkins et al., The ASKAP/EMU source finding data challenge, Publ. Astron. Soc. Aust. 32, e037 (2015); read as preprint arXiv:1509.03931 | doi:10.1017/pasa.2015.37 |
| 8 | A. R. Offringa et al., Post-correlation radio frequency interference classification methods, Mon. Not. R. Astron. Soc. 405, 155 (2010); read as preprint arXiv:1002.1957 | doi:10.1111/j.1365-2966.2010.16471.x |
| 9 | P. Serra et al., SoFiA: a flexible source finder for 3D spectral line data, Mon. Not. R. Astron. Soc. 448, 1922 (2015); read as preprint arXiv:1501.03906 | doi:10.1093/mnras/stv079 |
| 10 | J. González-López et al., The Atacama Large Millimeter/submillimeter Array Spectroscopic Survey in the Hubble Ultra Deep Field: CO emission lines and 3 mm continuum sources, Astrophys. J. 882, 139 (2019); read as preprint arXiv:1903.09161 | doi:10.3847/1538-4357/ab3105 |
| 11 | J. N. Chengalur, Y. Gupta and K. S. Dwarakanath (eds.), Low Frequency Radio Astrophysics, notes from the 1999 NCRA-TIFR school, chapter 13 Spectral Line Observations, sections Bandshape Calibration, Smoothing and Continuum Subtraction, web edition (2003) | https://www.gmrt.ncra.tifr.res.in/doc/WEBLF/LFRA/node116.html |
