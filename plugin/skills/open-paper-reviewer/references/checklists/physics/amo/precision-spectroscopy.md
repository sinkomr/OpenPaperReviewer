---
id: T-PRECISION-SPECTROSCOPY
name: Precision spectroscopy and frequency combs
type: technique
field: physics/amo
applies_when: the paper reports an absolute transition frequency, line centre, isotope or fine-structure interval measured by laser or microwave spectroscopy, often referenced to an optical frequency comb, or derives a fundamental constant, nuclear charge radius or test of theory from such frequencies
version: "0.1"
---

# Precision spectroscopy and frequency combs

Precision spectroscopy is used to claim the absolute frequency of an atomic or molecular transition, the size of an interval between levels, and, by comparison with theory, a value for a fundamental constant such as the Rydberg constant or for a nuclear charge radius. The frequency is read against an optical frequency comb (a mode-locked laser whose modes sit at known multiples of a radio-frequency reference), and the result is only as good as the line-centre determination and the corrections for systematic shifts (AC Stark or light shifts, collisional shifts, Doppler and field shifts) that move the observed line away from the unperturbed transition.

## 1. Line-shape model and line centre

**Question.** Which line-shape model was fitted to obtain the line centre, are the fit residuals shown, and does the quoted centre change when a different physically reasonable model is used?

**Why it matters.** A symmetric profile such as a Lorentzian or Voigt fitted to a line that is in fact narrowed or asymmetric leaves structured residuals and biases the fitted parameters. Speed-dependent collisional effects and correlations between collisions can make a real line slightly asymmetric, so the peak of a symmetric fit is not the same as the transition frequency.

**Resolved by.** The fitted function stated with its free and fixed parameters; residuals plotted at the full signal-to-noise; the centre compared across profiles that include or exclude narrowing and asymmetry, with the spread entered in the uncertainty budget; any fixed parameters, such as unresolved component ratios or splittings, justified.

**Benchmark.** [1], [3]

## 2. Quantum interference with neighbouring lines

**Question.** Are there other transitions within a few linewidths of the one measured, and if so does the analysis include quantum interference between them, for example by modelling the cross terms or by using a detection geometry in which they vanish?

**Why it matters.** When two excitation paths lead to the same final state, the signal is not a sum of independent line profiles. The cross terms distort and shift each line by an amount that depends on laser polarisation and detection direction, and the shift falls off only slowly with separation, so even a distant neighbour can matter at high precision. Fits that ignore them give centres that change with polarisation.

**Resolved by.** The neighbouring transitions and their separations stated; a line-shape model that includes the interference terms, or detection at the angle where they cancel, with the finite collection solid angle accounted for; line centres shown to agree across polarisations or geometries; the interference correction and its uncertainty listed separately.

**Benchmark.** [2], [3], [7]

## 3. Light shifts from probe and trapping fields

**Question.** How were AC Stark (light) shifts from the probe laser, any trapping or cooling light and any other optical field evaluated: was the line centre measured at several intensities and extrapolated to zero, and is the intensity dependence shown to follow the assumed form?

**Why it matters.** Every optical field at the atoms shifts the levels, and the probe itself shifts the transition it measures. Optical pumping at higher intensity can also move the apparent centre. An extrapolation that assumes a linear dependence, when higher-order terms are present, leaves a residual shift.

**Resolved by.** The line centre plotted against probe and trap intensity, with the extrapolation model and its uncertainty given; for trapped samples, measurements at several trap depths and the operating wavelength relative to the wavelength where the shift cancels; higher-order intensity terms tested or bounded; the result in the budget as a separate line.

**Benchmark.** [3], [4], [7]

## 4. Collisional and pressure shifts

**Question.** Was the line centre measured at several gas pressures or sample densities, and is the result extrapolated to zero pressure or density with the dependence shown?

**Why it matters.** Collisions with the background gas or between the atoms themselves shift and broaden the line. These shifts usually cannot be calculated well enough and must be measured. In the binary-collision regime the fitted width and shift should vary linearly with pressure, and fitted parameters that depart from this point to an inadequate line-shape model.

**Resolved by.** Line centre and width plotted against pressure or density over a range wide enough to fix the slope; the extrapolated zero-pressure value and the slope with uncertainties; the pressure or density measurement and its calibration described; the same line-shape model used at every pressure.

**Benchmark.** [1], [4]

## 5. Doppler, motional and field shifts

**Question.** How were the first-order Doppler shift, the second-order Doppler (time-dilation) shift and the shifts from static magnetic and electric fields and blackbody radiation removed or evaluated, and on what measured velocity distribution, field or temperature does each correction rest?

**Why it matters.** A residual first-order Doppler shift remains whenever counter-propagating beams are imperfectly aligned or the atom-laser distance drifts, and it can dominate for single-photon transitions. The second-order Doppler shift depends on the velocity distribution and can be the largest correction for fast atoms or ions with excess motion. Zeeman and blackbody shifts depend on fields and temperatures at the atoms that are often inferred, not measured.

**Resolved by.** The method of cancelling the first-order Doppler shift stated and its residual bounded by a measurement, not only by an alignment estimate; the velocity distribution measured, not assumed, where it sets the second-order correction; the magnetic field at the atoms calibrated, with first-order Zeeman shifts averaged out by measuring opposite sublevels where possible; the thermal environment characterised for the blackbody correction.

**Benchmark.** [4], [7]

## 6. Comb referencing and traceability

**Question.** Does the paper say what reference the comb's repetition rate and offset frequency were locked to, how that reference is linked to the SI second and with what uncertainty, and how the comb mode number and the signs of the offset and beat frequencies were determined?

**Why it matters.** The comb transfers the accuracy of its radio-frequency reference to the optical frequency, and any error in the reference adds directly to the measured optical frequency. The optical frequency follows from the mode number, the repetition rate, the offset frequency and a beat note, so an incorrectly identified mode number or a wrong sign shifts the result by a multiple of the repetition rate or by twice an offset or beat frequency.

**Resolved by.** The reference named (for example a hydrogen maser, a caesium standard or a satellite-disciplined oscillator) with its link to the SI second and its fractional uncertainty over the averaging time; the mode number fixed by a wavemeter whose resolution is shown to be well below the mode spacing, or by repeating the measurement at two or more repetition rates; the signs of the offset and beat frequencies fixed by a stated test, such as changing the offset lock point or tuning the laser; the reference uncertainty listed in the budget.

**Benchmark.** [5], [9]

## 7. Frequency-counting statistics and drift

**Question.** How was the statistical uncertainty of the averaged frequency obtained: is an Allan deviation against averaging time shown, is the type of frequency counter stated, and does the averaging continue to reduce the scatter over the full data set?

**Why it matters.** Frequency data are not always limited by white noise. The Allan deviation shows how the scatter falls with averaging time, and one that stops falling points to drift or a drifting systematic effect, which a standard error of the mean would hide. Counters that weight their readings differently return different variances from the same signal, so stability figures are misread if the counter type is not known.

**Resolved by.** An Allan deviation (or overlapping variant) of the frequency data against averaging time, with the noise type identified and the averaging time of the final value marked; the counter type and gate time stated, and the variance computed in a way consistent with it; day-to-day scatter compared with the statistical uncertainty of each day.

**Benchmark.** [4], [6]

## 8. Constants and radii derived from spectroscopy

**Question.** When a fundamental constant or a nuclear charge radius is derived from measured frequencies, does the paper state the theoretical expression and its uncertainty, which other constants were fixed and at what values, and how correlated quantities were separated?

**Why it matters.** Spectroscopy gives a frequency, and a constant or radius follows only through a theoretical expression whose uncalculated higher-order terms carry their own uncertainty. Quantities such as the Rydberg constant and a nuclear radius enter the same expressions and are strongly correlated, so at least two transitions, or an external value for one of them, are needed to separate them. Recommended values themselves combine data sets that do not all agree.

**Resolved by.** The theory used, with its version, references and uncertainty, kept separate from the experimental uncertainty; the input constants and their source stated; two or more transitions, or a stated external input, used to separate correlated quantities, with the correlation given; for charge-radius differences from isotope shifts, the calculated point-nucleus isotope shift and field-shift coefficient stated with their source and uncertainty; the result compared with the current recommended values and with independent determinations, the size of any difference stated in combined uncertainties.

**Benchmark.** [3], [7], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | J. Tennyson, P. F. Bernath, A. Campargue, A. G. Császár, L. Daumont, R. R. Gamache, J. T. Hodges, D. Lisak, O. V. Naumenko, L. S. Rothman, H. Tran et al., Recommended isolated-line profile for representing high-resolution spectroscopic transitions (IUPAC Technical Report), Pure Appl. Chem. 86, 1931–1943 (2014); read as arXiv:1409.7782 | doi:10.1515/pac-2014-0208 | full text | Sec. I: the Voigt profile is not fully accurate; Voigt fits of high-precision spectra leave W-shaped residuals and underestimate intensities. Secs. I and III: speed dependence and velocity-changing (Dicke) collisions narrow lines; in the binary-collision regime fitted parameters vary linearly with pressure. Sec. IV: the recommended Hartmann–Tran profile is generally slightly asymmetric because of correlation and the speed dependence of the shift |
| 2 | M. Horbatsch and E. A. Hessels, Shifts from a distant neighboring resonance, Phys. Rev. A 82, 052519 (2010) | doi:10.1103/PhysRevA.82.052519 | abstract | Abstract: quantum interference with a neighbouring resonance shifts a line centre; the effect is easily overlooked; an analytic treatment for a three-level atom finds shifts large enough to matter in precision measurements |
| 3 | R. C. Brown, S. Wu, J. V. Porto, C. J. Sansonetti, C. E. Simien, S. M. Brewer, J. N. Tan and J. D. Gillaspy, Quantum interference and light polarization effects in unresolvable atomic lines: application to a precise measurement of the 6,7Li D2 lines, Phys. Rev. A 87, 032504 (2013); read as arXiv:1212.2220 | doi:10.1103/PhysRevA.87.032504 | full text | Secs. I–II.1: interference between levels about a linewidth apart makes the line shape differ from a sum of Lorentzians; cross terms depend on polarisation and detection direction and vanish at a particular angle. Sec. II.2: far from the neighbour the centre shift is about the width squared over four times the separation. Sec. III.2: centres fitted without cross terms vary with polarisation, fits with them agree. Sec. III.1: unresolved component ratios and splittings fixed in the fit. Sec. III.3: intensity-dependent shifts from optical pumping and light shifts. Sec. IV: radius difference from the measured isotope shift, a calculated point-nucleus isotope shift and a field-shift coefficient, compared with other determinations. Appendix C: finite collection angle shifts the centre |
| 4 | A. D. Ludlow, M. M. Boyd, J. Ye, E. Peik and P. O. Schmidt, Optical atomic clocks, Rev. Mod. Phys. 87, 637–701 (2015); read as arXiv:1407.3493 | doi:10.1103/RevModPhys.87.637 | full text | Sec. I.2: Allan deviation defined, with the overlapping form, and drifting systematic effects make it level off. Sec. II.3.1: collisional shifts usually have to be calibrated experimentally; blackbody shift scales with the fourth power of temperature; first-order Zeeman shift averaged by alternating opposite sublevels. Sec. II.3.2: first-order Doppler shifts can dominate single-photon transitions and need control of the atom-laser distance; second-order Doppler shifts from ion motion can be the largest uncertainty. Secs. VI.4.2 and VI.5.1: lattice light shifts evaluated from measurements across trap depths and wavelengths about the magic wavelength, with the uncertainty of the higher-order (hyperpolarizability) term determined experimentally. Secs. IV.1 and VI.5.5: light shift from the probe or interrogation laser |
| 5 | T. Fortier and E. Baumann, 20 years of developments in optical frequency comb technology and applications, Commun. Phys. 2, 153 (2019); read as arXiv:1909.05384 | doi:10.1038/s42005-019-0249-y | full text | Sec. 2.1: each comb mode is fixed by the repetition rate and offset frequency, both stabilised by feedback. Sec. 2.2: the difference from the nearest mode is read as a beat note. Sec. 4.2.1: an unknown optical frequency follows from the mode number, the comb parameters and the beat note; the mode number comes from a wavemeter, and repetition rates well above the wavemeter resolution are used to avoid ambiguity; absolute optical measurements are limited by the microwave reference, whose errors add directly to the optical frequency |
| 6 | E. Rubiola, On the measurement of frequency and of its sample variance with high-resolution counters, Rev. Sci. Instrum. 76, 054703 (2005); read as arXiv:physics/0411227 | doi:10.1063/1.1898203 | full text | Secs. 2.1–2.4: counters with rectangular and triangular weighting give different variances for the same noise; how to tell the type from the specification. Sec. 3.2: raw readings from a triangular-weighting counter fed into the Allan formula give the modified Allan variance, not the Allan variance. Abstract and Sec. 2.3: results are easily misread unless the counter's internal processing is understood |
| 7 | P. J. Mohr, D. B. Newell, B. N. Taylor and E. Tiesinga, CODATA recommended values of the fundamental physical constants: 2022, Rev. Mod. Phys. 97, 025002 (2025); read as arXiv:2409.03787 | doi:10.1103/RevModPhys.97.025002 | full text | Secs. III.1–III.2: hydrogen and deuterium levels depend on the Rydberg constant, the fine-structure constant and the nuclear radii, with uncalculated higher-order QED terms assigned uncertainties and additive theory corrections given with their correlations. Sec. III.3.2: an experiment corrected for second-order Doppler shift from a fitted velocity distribution, for light and pressure shifts and for quantum interference. Secs. I.2.3 and IV.2: the hydrogen and deuterium input frequencies are mutually inconsistent, so their uncertainties are expanded by a common factor |
| 8 | S. G. Karshenboim, Precision physics of simple atoms: QED tests, nuclear structure and fundamental constants, Phys. Rep. 422, 1–63 (2005); read as arXiv:hep-ph/0509010 | doi:10.1016/j.physrep.2005.08.008 | full text | Sec. 3: measured frequencies of two or more transitions combined with QED theory give both the Rydberg constant and the Lamb shift, which are strongly correlated. Sec. 4: the lack of an accurate proton charge radius is the main problem in Lamb-shift theory; independent determinations compared as a test for systematic effects. Sec. 1: the aim of checking consistency between results from different fields |
| 9 | A. L. Wolf, S. A. van den Berg, C. Gohle, E. J. Salumbides, W. Ubachs and K. S. E. Eikema, Frequency metrology on the 4s 2S1/2 - 4p 2P1/2 transition in the calcium ion for a comparison with quasar data, Phys. Rev. A 78, 032511 (2008); read as arXiv:0804.4130 | doi:10.1103/PhysRevA.78.032511 | full text | Sec. II.3: the sign of the beat note found from the scan direction and the sign of the comb offset frequency from a repeat with a different offset lock point; the mode number fixed by repeating the measurement at two repetition rates, which agree only for the correct mode number |
