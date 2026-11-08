---
id: T-ASTRONOMICAL-SPECTROSCOPY
name: Astronomical spectroscopy and redshifts
type: technique
field: physics/astrophysics
applies_when: the paper measures redshifts, velocities, line identifications or line fluxes from ultraviolet, optical or infrared spectra of galaxies, quasars, stars or transients, or claims spectroscopic confirmation of a high-redshift or photometrically selected candidate; precise stellar radial velocities and exoplanet spectra have their own cards
version: "0.1"
---

# Astronomical spectroscopy and redshifts

## 1. Wavelength scale and velocity frame

**Question.** How was the wavelength scale calibrated and checked (arc lamps taken when, sky lines, residuals of the fit), are wavelengths stated as air or vacuum, and to which velocity frame are the redshifts or velocities referred?

**Why it matters.** Flexure of the instrument shifts the wavelength scale between the calibration and the science exposure, and a fit of too high an order adds structure of its own. Air and vacuum wavelengths differ by about 0.03 per cent, comparable to a velocity of about 90 km/s, and the correction from the observatory to the barycentre of the solar system is up to about 30 km/s; mixing conventions between the data and the rest wavelengths gives a systematic offset.

**Resolved by.** Calibration frames taken close in time and telescope position to the science exposures, or a correction for flexure; the residuals of the wavelength solution stated as a fraction of a resolution element and checked against night-sky lines in the science frames; the air or vacuum convention of both the data and the rest wavelengths stated; the velocity frame named and the barycentric or heliocentric correction applied.

**Benchmark.** [1], [2]

## 2. Sky subtraction and residuals

**Question.** How was the sky background subtracted (nodding along the slit, separate sky frames, modelling of the unrectified two-dimensional spectrum), and does the paper show the residuals at the wavelengths of bright sky lines near the features its claims rest on?

**Why it matters.** Near-infrared airglow lines can be more than a thousand times brighter than the sky between them and vary within minutes, with different lines varying differently, so a sky frame taken at another time leaves residuals. Small wavelength shifts between frames and the resampling of two-dimensional spectra leave sharp residuals at the edges of sky lines, which can be larger than a faint line from the source.

**Resolved by.** The sky-subtraction method stated; the two-dimensional spectrum shown around each claimed feature with the positions of sky lines marked; the noise near sky lines estimated from the data and not assumed to be the noise between them; features that coincide with strong sky lines treated with caution or confirmed in data with a different redshift or setup.

**Benchmark.** [1], [3], [4]

## 3. Telluric absorption

**Question.** For ground-based spectra, how was absorption by the Earth's atmosphere corrected (which standard stars, at what airmass and time relative to the target, how their own spectral lines were removed), and do any claimed features fall in telluric bands?

**Why it matters.** Atmospheric absorption is strong and varies with airmass, water vapour and time, and it does not scale simply with airmass. Dividing by a standard star observed at a different airmass or time, or one whose own absorption lines were not removed, leaves residuals or creates features that are not in the source.

**Resolved by.** The telluric standards named, observed close in airmass and time to the target, with their intrinsic lines modelled or removed; the correction aligned in wavelength with the target spectrum; the telluric bands marked on the spectra, and any claimed feature inside them shown to survive a change of standard or method.

**Benchmark.** [1], [5]

## 4. Flux calibration and slit losses

**Question.** How was the flux scale set (which spectrophotometric standards, through what slit width, at what slit angle), how were slit losses corrected, and are fluxes or ratios of lines widely separated in wavelength checked against photometry?

**Why it matters.** A narrow slit loses light by an amount that depends on seeing and, through atmospheric differential refraction, on wavelength unless the slit lies along the parallactic angle or a dispersion corrector is used. Standard-star flux scales themselves carry uncertainties of about a per cent at best and larger for older catalogues, and multi-slit data have a different response for each slit.

**Resolved by.** The standards and their flux scale named; a wide slit for the standards, or slit losses matched or corrected between standards and target; the slit angle or use of a dispersion corrector stated; the absolute scale and the continuum shape compared with broadband photometry of the source; ratios of lines far apart in wavelength reported with the calibration uncertainty included.

**Benchmark.** [1], [5], [6]

## 5. Identification of a single line

**Question.** When a redshift rests on one emission line, what excludes other identifications of that line, such as Lyα against the [O II] 3727 doublet, [O III] or Hα, and does the spectrum cover the wavelengths where the other lines of each alternative would appear?

**Why it matters.** A line at a given observed wavelength can come from different transitions at very different redshifts, and line flux alone does not tell them apart. The [O II] doublet is split by only about 2.5 Å in the rest frame and is unresolved at low resolution, and equivalent-width cuts used to separate the populations are neither complete nor free of contamination.

**Resolved by.** The alternative identifications listed with the wavelengths of their companion lines, and those lines shown to be absent where they would be detectable; the [O II] doublet resolved where resolution allows; the line profile shown, such as the asymmetry expected of Lyα; for Lyα, no continuum detected blueward of the line; the redshift checked against photometry that brackets the line.

**Benchmark.** [7], [8]

## 6. Redshift measurement and confidence

**Question.** How was each redshift measured (template fitting or cross-correlation, which templates, over what redshift range), how is its reliability graded, and has the rate of wrong redshifts been measured for the sample?

**Why it matters.** A template fit can find a minimum at a wrong redshift when the signal is weak or the templates do not match the source, and the formal uncertainty from the fit says nothing about such errors. Formal redshift errors can also be underestimated when tested against repeat observations.

**Resolved by.** The method, templates and redshift range stated; a quantitative confidence criterion, such as the difference in goodness of fit between the best and the next-best solution well separated in redshift; the definition of each quality grade given; the rate of wrong redshifts and the size of redshift errors checked by repeat observations or independent inspection.

**Benchmark.** [1], [9]

## 7. Systemic redshift and line offsets

**Question.** Which features define the redshift that is quoted, and is the redshift from Lyα or from interstellar absorption lines corrected for their usual offset from the systemic redshift given by nebular lines or stars?

**Why it matters.** Outflowing gas shifts Lyα emission to longer wavelengths and interstellar absorption lines to shorter ones, each by typically a few hundred km/s relative to the nebular lines. A redshift taken directly from these features is biased and adds scatter, which matters for velocity offsets, pair and environment studies and the modelling of absorption near the Lyα break.

**Resolved by.** The features behind each redshift stated; nebular emission lines or stellar features used for the systemic redshift where they are available; otherwise, a stated calibration of the Lyα or absorption-line offset applied with its scatter included in the uncertainty.

**Benchmark.** [10], [11]

## 8. Spectroscopic confirmation of high-redshift candidates

**Question.** When a candidate selected from imaging is reported as confirmed, which features confirm it (a continuum break, one or more lines), how significant is each in the two-dimensional data, and are lower-redshift solutions, such as a Balmer break or a dusty galaxy, and absorption that shifts the apparent break, excluded?

**Why it matters.** Galaxies at lower redshift with a Balmer break, heavy dust or strong emission lines, and cool dwarf stars can mimic the colours of a high-redshift galaxy. Rare noise peaks can look like a line in one data set, and Lyα becomes weak at the highest redshifts. A redshift from the break alone depends on the column of neutral hydrogen near the galaxy, and ignoring dense absorbers biases it.

**Resolved by.** The two-dimensional and one-dimensional spectra shown with the noise, and the line present in independent subsets of the exposures; at least two features, or a break with no flux blueward of it together with a line; the best lower-redshift solutions fitted and shown to be worse; break redshifts fitted with damped absorption allowed, and preferably anchored by nebular lines; the spectroscopic redshift compared with the photometric redshift.

**Benchmark.** [8], [11], [12], [13]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | P. Massey and M. M. Hanson, Astronomical Spectroscopy, in Planets, Stars and Stellar Systems, pp. 35–98, Springer (2013); read as arXiv:1010.5270 | doi:10.1007/978-94-007-5618-2_2 |
| 2 | E. W. Greisen et al., Representations of spectral coordinates in FITS, Astron. Astrophys. 446, 747 (2006); read as arXiv:astro-ph/0507293 | doi:10.1051/0004-6361:20053818 |
| 3 | D. D. Kelson, Optimal techniques in two-dimensional spectroscopy: background subtraction for the 21st century, Publ. Astron. Soc. Pac. 115, 688 (2003); read as arXiv:astro-ph/0303507 | doi:10.1086/375502 |
| 4 | R. I. Davies, A method to remove residual OH emission from near-infrared spectra, Mon. Not. R. Astron. Soc. 375, 1099 (2007); read as arXiv:astro-ph/0612257 | doi:10.1111/j.1365-2966.2006.11383.x |
| 5 | W. D. Vacca et al., A method of correcting near-infrared spectra for telluric absorption, Publ. Astron. Soc. Pac. 115, 389 (2003); read as arXiv:astro-ph/0211255 | doi:10.1086/346193 |
| 6 | R. C. Bohlin et al., Techniques and review of absolute flux calibration from the ultraviolet to the mid-infrared, Publ. Astron. Soc. Pac. 126 (2014); read as arXiv:1406.1707 | doi:10.1086/677655 |
| 7 | A. S. Leung et al., Bayesian redshift classification of emission-line galaxies with photometric equivalent widths, Astrophys. J. 843, 130 (2017); read as arXiv:1510.07043 | doi:10.3847/1538-4357/aa71af |
| 8 | J. S. Dunlop, Observing the first galaxies, in The First Galaxies, Astrophysics and Space Science Library 396, pp. 223–292, Springer (2013); read as arXiv:1205.1543 | doi:10.1007/978-3-642-32362-1_5 |
| 9 | A. S. Bolton et al., Spectral classification and redshift measurement for the SDSS-III Baryon Oscillation Spectroscopic Survey, Astron. J. 144, 144 (2012); read as arXiv:1207.7326 | doi:10.1088/0004-6256/144/5/144 |
| 10 | C. C. Steidel et al., The structure and kinematics of the circumgalactic medium from far-ultraviolet spectra of z ≈ 2–3 galaxies, Astrophys. J. 717, 289 (2010); read as arXiv:1003.0679 | doi:10.1088/0004-637X/717/1/289 |
| 11 | C. L. Pollock et al., Characterising Lyα damping wings at the onset of reionisation, arXiv:2602.11783 (2026) | doi:10.48550/arXiv.2602.11783 |
| 12 | K. E. Heintz et al., JWST spectroscopy of galaxies at z>10: damped Lyα absorbers reveal efficient star formation and hidden redshift biases, arXiv:2606.30787 (2026) | doi:10.48550/arXiv.2606.30787 |
| 13 | P. Arrabal Haro et al., Confirmation and refutation of very luminous galaxies in the early Universe, Nature 622, 707 (2023); read as arXiv:2303.15431 | doi:10.1038/s41586-023-06521-7 |
