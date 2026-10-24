---
id: T-ASTRONOMICAL-SPECTROSCOPY
name: Astronomical spectroscopy and redshifts
type: technique
field: physics/astrophysics
applies_when: the paper reports ultraviolet, optical or infrared spectra of astronomical sources, measures redshifts, radial velocities, line identifications or line fluxes from them, or claims spectroscopic confirmation of a high-redshift or photometrically selected candidate
version: "0.1"
---

# Astronomical spectroscopy and redshifts

Astronomical spectra are used to claim a source's redshift or radial velocity, the identity and strength of its emission and absorption lines, and, for candidates selected from imaging, that the source really lies at the proposed distance. Each of these rests on a wavelength scale, a removed sky background, a correction for absorption in the Earth's atmosphere (telluric absorption), a flux calibration and the identification of at least one spectral feature; the Lyman-alpha (Lyα) line and the break it leaves in the continuum carry most claims at the highest redshifts.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | P. Massey and M. M. Hanson, Astronomical Spectroscopy, in Planets, Stars and Stellar Systems, pp. 35–98, Springer (2013); read as arXiv:1010.5270 | doi:10.1007/978-94-007-5618-2_2 | full text | Sec. II.1 and II.6: slit width set against seeing, slit losses. Sec. III.1.1: flux calibration of multi-slit data difficult, each slit having its own response and wavelength coverage. Sec. III.1.2: wavelength-scale uncertainty below a tenth of a resolution element with a fit of low order, OH sky lines as a near-infrared reference; OH residuals left because the sky varies in time; telluric standards near the target's airmass with their intrinsic lines removed, absorption not scaling simply with airmass. Sec. III.2.1: differential refraction gives wavelength-dependent slit losses, avoided at the parallactic angle or with a dispersion corrector. Sec. III.2.7: arcs before and after integrations to remove flexure; velocities by cross-correlation with standards of similar type; heliocentric correction up to about 30 km/s. Sec. III.3.1: slit kept wide, or a wider slit added, to preserve the continuum shape |
| 2 | E. W. Greisen, M. R. Calabretta, F. G. Valdes and S. L. Allen, Representations of spectral coordinates in FITS, Astron. Astrophys. 446, 747–771 (2006); read as arXiv:astro-ph/0507293 | doi:10.1051/0004-6361:20053818 | full text | Sec. 2: definitions of redshift and velocity conventions. Sec. 4: air and vacuum wavelengths differ by 0.028 to 0.032 per cent, with the conversion formula. Sec. 7 and Table 12: spectral reference frames (topocentric, geocentric, barycentric, local standard of rest and others) with offsets of up to hundreds of km/s; heliocentric often misused as an alias for barycentric; the date and observatory position are needed to convert between frames, and keywords are reserved for them |
| 3 | D. D. Kelson, Optimal techniques in two-dimensional spectroscopy: background subtraction for the 21st century, Publ. Astron. Soc. Pac. 115, 688–699 (2003); read as arXiv:astro-ph/0303507 | doi:10.1086/375502 | full text | Secs. I and II: rectifying two-dimensional spectra before sky subtraction adds correlated noise and leaves sharp residuals at the edges of strong sky lines. Secs. III.2 and III.3: periodic artefacts at night-sky lines in rebinned near-infrared and echelle data. Sec. III.1 and Sec. IV: modelling the sky before rectification leaves no systematic residuals, only the expected noise |
| 4 | R. I. Davies, A method to remove residual OH emission from near-infrared spectra, Mon. Not. R. Astron. Soc. 375, 1099–1105 (2007); read as arXiv:astro-ph/0612257 | doi:10.1111/j.1365-2966.2006.11383.x | full text | Sec. 1: OH line fluxes vary within minutes and the background on a line can exceed that between lines by over three orders of magnitude, so sky frames from other times leave residuals. Sec. 2: different vibrational bands vary differently. Sec. 3: small wavelength shifts from flexure give P-Cygni-shaped residuals that are hard to correct afterwards |
| 5 | W. D. Vacca, M. C. Cushing and J. T. Rayner, A method of correcting near-infrared spectra for telluric absorption, Publ. Astron. Soc. Pac. 115, 389–409 (2003); read as arXiv:astro-ph/0211255 | doi:10.1086/346193 | full text | Sec. I: telluric absorption is strong and variable; the hydrogen lines of A-type standards, if interpolated over, can create false features. Secs. II and III: standards must be close in airmass and time; changing humidity limits accuracy. Sec. IV: flexure misaligns telluric features unless the correction is shifted. Secs. II to IV: the method also sets an approximate flux scale if slit losses are similar for standard and target |
| 6 | R. C. Bohlin, K. D. Gordon and P.-E. Tremblay, Techniques and review of absolute flux calibration from the ultraviolet to the mid-infrared, Publ. Astron. Soc. Pac. 126 (2014); read as arXiv:1406.1707 | doi:10.1086/677655 | full text | Abstract and Sec. IV: primary standards accurate to about 1 per cent in relative flux from the visible to 2.5 µm. Secs. III.1 and V.3: older calibrations differ by several to tens of per cent. Sec. II.1: the calibrated flux is the standard's flux times a ratio of signals, so errors in standard-star fluxes pass into every spectrum calibrated with them |
| 7 | A. S. Leung, V. Acquaviva, E. Gawiser and others, Bayesian redshift classification of emission-line galaxies with photometric equivalent widths, Astrophys. J. 843, 130 (2017); read as arXiv:1510.07043 | doi:10.3847/1538-4357/aa71af | full text | Sec. I: high-redshift Lyα and low-redshift [O II] fall at the same observed wavelength with similar fluxes; the [O II] doublet is about 2.5 Å apart and unresolved at the survey resolution. Secs. III.3 and IV.5: other lines such as [Ne III], Hβ and [O III] help where they fall in range. Sec. III.2 and Table 3: the usual equivalent-width cut is incomplete and still contaminated |
| 8 | J. S. Dunlop, Observing the first galaxies, in The First Galaxies, Astrophysics and Space Science Library 396, pp. 223–292, Springer (2013); read as arXiv:1205.1543 | doi:10.1007/978-3-642-32362-1_5 | full text | Sec. 3.1.3: Balmer-break galaxies, dusty galaxies and cool dwarf stars contaminate high-redshift colour selections. Sec. 3.2.1: an asymmetric Lyα profile supports a single-line identification. Sec. 3.2.2: lower-redshift [O II], [O III] and Hα emitters mimic Lyα emitters; no flux blueward of Lyα; rare noise peaks in a single data set look like lines and need repeat observations. Sec. 4.3: Lyα detection rates fall at the highest redshifts and confirmation becomes difficult |
| 9 | A. S. Bolton, D. J. Schlegel, É. Aubourg and others, Spectral classification and redshift measurement for the SDSS-III Baryon Oscillation Spectroscopic Survey, Astron. J. 144, 144 (2012); read as arXiv:1207.7326 | doi:10.1088/0004-6256/144/5/144 | full text | Sec. III.1: redshifts from template fits over a redshift grid, with low confidence flagged when the best fit is not clearly better than the next-best fit more than 1000 km/s away. Sec. V.1: rate of wrong redshifts measured against visual inspection. Sec. V.2: galaxy redshift errors tested with repeat observations and found underestimated by factors of about 1.2 to 1.3; abstract: by about 2 for quasars |
| 10 | C. C. Steidel, D. K. Erb, A. E. Shapley and others, The structure and kinematics of the circumgalactic medium from far-ultraviolet spectra of z ≈ 2–3 galaxies, Astrophys. J. 717, 289–322 (2010); read as arXiv:1003.0679 | doi:10.1088/0004-637X/717/1/289 | full text | Sec. II.3: relative to Hα nebular redshifts, Lyα emission is offset by about +445 km/s and interstellar absorption by about −164 km/s on average; systemic redshifts recalibrated from the ultraviolet features, with Lyα adding scatter |
| 11 | C. L. Pollock, K. E. Heintz, J. Witstok and others, Characterising Lyα damping wings at the onset of reionisation, arXiv:2602.11783 (2026) | doi:10.48550/arXiv.2602.11783 | full text | Sec. 2: nebular lines fix the systemic redshift, which is essential for modelling the Lyα break and damping wings; risks of redshifts from the break alone noted. Sec. 3.2: the break position is degenerate with the neutral hydrogen column, so redshifts without lines can be ambiguous |
| 12 | K. E. Heintz, C. L. Pollock, J. Witstok and others, JWST spectroscopy of galaxies at z>10: damped Lyα absorbers reveal efficient star formation and hidden redshift biases, arXiv:2606.30787 (2026) | doi:10.48550/arXiv.2606.30787 | abstract | Abstract: ignoring damped Lyα absorption biases both photometric and Lyα-break redshifts of galaxies at z ≥ 10, by about 0.39 and 0.14 on average |
| 13 | P. Arrabal Haro, M. Dickinson, S. L. Finkelstein and others, Confirmation and refutation of very luminous galaxies in the early Universe, Nature 622, 707–711 (2023); read as arXiv:2303.15431 | doi:10.1038/s41586-023-06521-7 | abstract | Abstract: photometric redshifts of the earliest galaxies can be degenerate or badly wrong; a candidate at a photometric z of about 16 lay at z = 4.9, where nebular line emission with dust reddening mimicked the colours of a much more distant galaxy; spectroscopy is needed to confirm such candidates |
