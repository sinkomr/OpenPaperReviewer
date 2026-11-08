---
id: T-DETECTOR-EFFICIENCY
name: Detector efficiency and dead time
type: technique
field: physics/methods
applies_when: the paper counts or images photons, electrons, particles or other radiation and bases a claim on absolute or relative count rates, detection efficiency, intensities, coincidence or correlation counts, spectra or arrival times, or on corrections for dead time, pile-up, dark counts or afterpulsing
version: "0.1"
---

# Detector efficiency and dead time

## 1. Which efficiency is quoted

**Question.** Does the paper say which efficiency it quotes or uses (intrinsic to the sensor, or of the whole system including coupling, geometry, threshold and readout), at which reference point it applies, and under which wavelength or energy, polarisation, bias, temperature and count rate?

**Why it matters.** The probability that an absorbed quantum gives a registered event can be much higher than the probability that a quantum arriving at the instrument does, because coupling, absorption and threshold losses multiply in. The same detector also has different efficiencies at different bias, wavelength, count rate and, for imaging detectors, spatial frequency, so a figure without its conditions cannot be compared or used to correct data.

**Resolved by.** The efficiency named and defined, with the losses it includes and the plane at which it is referred, for example the fibre input or the detector window; the wavelength or energy, polarisation, bias or threshold, temperature and count rate at which it was determined; the same definition used throughout the paper and in any comparison with other detectors.

**Benchmark.** [1], [2], [3], [11]

## 2. How the absolute and relative efficiency were established

**Question.** Where a claim depends on absolute efficiency, how was the number of quanta reaching the detector determined independently (a calibrated reference detector, a measured beam current or a calibrated source)? Where it compares intensities at different energies or wavelengths, was the relative efficiency measured across that range? Did the calibration geometry, spectrum and sample match the measurement?

**Why it matters.** An absolute efficiency is only as good as the independent knowledge of the incident flux, and corrections for dark counts, afterpulsing and count rate all enter it. Efficiency also changes with energy or wavelength, sometimes steeply, so a ratio of intensities at two energies needs the efficiency at both. In gamma-ray spectrometry, efficiency calibration depends on correction factors and on how well the sample is characterised, and combined relative standard uncertainties are rarely below one per cent.

**Resolved by.** The reference standard and its traceability stated; the incident flux measured with a stated uncertainty, for example a beam current from a calibrated meter; the corrections applied in the calibration listed; an efficiency or spectral-response curve measured over the energies or wavelengths compared, with its uncertainty; the calibration made in, or transferred with stated corrections to, the geometry, energy and sample of the measurement.

**Benchmark.** [1], [2], [3], [4]

## 3. Dead-time and pile-up corrections

**Question.** Which dead-time or pile-up model was used to correct count rates, how was its parameter measured for the detector and settings in use, and how large is the correction at the highest rate in the data?

**Why it matters.** Dead time and pile-up lose counts in a rate-dependent way and change counting statistics away from Poisson, so corrected rates and their uncertainties depend on the model. Real detectors are often not described by a single dead-time value: it can depend on gain, threshold and the time structure of the source, and can differ between pixels. In time-correlated counting, dead time distorts the arrival-time histogram and so the fitted lifetimes.

**Resolved by.** The model (extending, non-extending or a measured response) and the measured dead time stated for the settings used; the size of the correction at the highest rate shown, with a residual uncertainty; a check that corrected rates agree with a measurement at much lower rate; for pulsed sources, a correction that accounts for the pulse structure; for timing histograms, a stated dead-time correction or evidence that the histogram shape does not change with count rate.

**Benchmark.** [3], [5], [6], [7]

## 4. Linearity and saturation over the range used

**Question.** Does the paper show directly that the detector response is linear, or correctly linearised, over the whole range of rate or intensity in the data, and that no part of the data lies near saturation?

**Why it matters.** Count losses, rate-dependent dead time and shifts in detection delay make the response non-linear at high rates, and an efficiency measured at low rate does not then apply. A ratio of intensities, a fitted peak shape or a photon-statistics measurement taken at different rates inherits the non-linearity as an apparent physical effect.

**Resolved by.** The response measured against a known variation of the input, such as calibrated attenuation or source distance, across the range of the data; the highest local rate, including in the brightest pixel or peak, compared with the rate at which losses become significant; key results repeated at lower flux and shown to be unchanged.

**Benchmark.** [3], [5], [8]

## 5. Dark counts and background

**Question.** Is the dark count or background rate measured under the same conditions as the data (bias, temperature, shielding, light or radiation paths), stated in comparison with the signal rate, and subtracted with its uncertainty?

**Why it matters.** Dark counts arise from thermal and tunnelling processes in the detector, from readout noise and from stray or thermal radiation reaching it, for example through an optical fibre. The rate depends strongly on bias and temperature, and reducing it usually costs efficiency, so a dark rate measured with the input blocked, or at other settings, may not apply to the data.

**Resolved by.** The dark or background rate given for the operating settings, with how it was measured (input blocked, fibre disconnected, source removed); its ratio to the signal rate at the weakest signals that carry a claim; the subtraction and its uncertainty included in the results; for efficiency measurements, dark counts corrected for explicitly.

**Benchmark.** [1], [2]

## 6. Afterpulsing and other correlated false counts

**Question.** Were afterpulsing and other correlated false counts measured for the actual detectors at the settings used, and is their effect on count rates, coincidence counts and correlation functions corrected or shown to be negligible?

**Why it matters.** Afterpulses add counts that are correlated in time with real detections, so they inflate count rates and coincidences and can create structure in correlation and arrival-time data. Detectors of the same make and model can differ widely in afterpulse probability and in its time dependence, and a longer dead time does not reliably reduce it, so values from a data sheet or from another unit are not a substitute.

**Resolved by.** Afterpulse probability and its time distribution measured for each detector at the operating dead time, bias and temperature; the measured correction applied to rates and coincidence counts, or an estimate showing it is small compared with the effect claimed; correlation measurements made with two separate detectors, or the delays where afterpulses fall excluded.

**Benchmark.** [1], [8], [9]

## 7. Resolution and detector artefacts in spectra and timing

**Question.** Are the energy and timing resolution of the detector stated for the conditions of the measurement, including the tails of the response, and are claimed spectral or temporal features distinguished from features the detector itself produces?

**Why it matters.** Detectors produce features that look like signal: escape and coincidence (sum) peaks in energy spectra can be assigned to trace elements, and afterpulse peaks spaced at the dead time can mimic or hide structure in arrival-time data. Timing jitter is usually quoted as a full width at half maximum, but long tails in the response affect lifetime fits and coincidence windows, and dead time skews timing histograms at high rates.

**Resolved by.** The measured response function (energy resolution, or the timing response with its tails) at the rates and settings used; candidate features checked against escape, sum, afterpulse and other detector-generated features at the positions where they are expected; fits that include the measured instrument response; claimed features that do not move or scale as detector artefacts would when rate or settings change.

**Benchmark.** [1], [7], [9], [10]

## 8. Uniformity between channels and stability over time

**Question.** For detectors with several channels or pixels, or measurements over long periods, does the paper show that the efficiency, dead time and dark rate are uniform enough between channels and stable enough over the measurement for the claim, and how was this monitored?

**Why it matters.** Efficiency need not be uniform across the active area of a single detector, which calibrations examine, and dead time and afterpulsing can differ between pixels and between units of the same type. A characterisation made once may not hold for a later measurement, so repeating it over a detector's operating life is advised, and a comparison between channels or between runs can then show a difference that comes from the detector.

**Resolved by.** Per-channel or per-pixel efficiency and dead time measured and applied, or their spread shown to be small compared with the effect; the beam position or illuminated area stated where efficiency is not uniform; efficiency or a reference rate checked before, during and after the measurement, or channels swapped to show that the result follows the sample and not the detector.

**Benchmark.** [2], [5], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | P. Dasika et al., Low-dimensional platforms for single photon detection, arXiv:2604.17452 (2026), review preprint | doi:10.48550/arXiv.2604.17452 |
| 2 | T. Gerrits et al., Calibration of free-space and fiber-coupled single-photon detectors, Metrologia 57, 015002 (2020); read as arXiv:1906.02258 | doi:10.1088/1681-7575/ab4533 |
| 3 | G. McMullan et al., Comparison of optimal performance at 300 keV of three direct electron detectors for use in low dose electron microscopy, Ultramicroscopy 147, 156 (2014); read as arXiv:1406.1389 | doi:10.1016/j.ultramic.2014.08.002 |
| 4 | M. C. Lépy et al., Uncertainties in gamma-ray spectrometry, Metrologia 52, S123–S145 (2015) | doi:10.1088/0026-1394/52/3/S123 |
| 5 | P. Trueb et al., Improved count rate corrections for highest data quality with PILATUS detectors, J. Synchrotron Rad. 19, 347 (2012) | doi:10.1107/S0909049512003950 |
| 6 | S. Pommé et al., Uncertainty of nuclear counting, Metrologia 52, S3–S17 (2015) | doi:10.1088/0026-1394/52/3/S3 |
| 7 | S. Isbaner et al., Dead-time correction of fluorescence lifetime measurements and fluorescence lifetime imaging, Opt. Express 24, 9429 (2016) | doi:10.1364/OE.24.009429 |
| 8 | M. Stipčević et al., Advanced active quenching circuits for single-photon avalanche photodiodes, Proc. SPIE 9858, 98580R (2016) | doi:10.1117/12.2227999 |
| 9 | A. W. Ziarkash et al., Comparative study of afterpulsing behavior and models in single photon counting avalanche photo diode detectors, Sci. Rep. 8, 5076 (2018) | doi:10.1038/s41598-018-23398-z |
| 10 | D. E. Newbury, Mistakes encountered during automatic peak identification of minor and trace constituents in electron-excited energy dispersive X-ray microanalysis, Scanning 31, 91 (2009) | doi:10.1002/sca.20151 |
| 11 | ETSI Industry Specification Group on Quantum Key Distribution, ETSI GS QKD 011 V1.1.1, Quantum Key Distribution (QKD); Component characterization: characterizing optical components for QKD systems (2016) | https://www.etsi.org/deliver/etsi_gs/QKD/001_099/011/01.01.01_60/gs_qkd011v010101p.pdf |
