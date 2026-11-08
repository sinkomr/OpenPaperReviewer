---
id: T-PRECISION-SPECTROSCOPY
name: Precision spectroscopy and frequency combs
type: technique
field: physics/amo
applies_when: the paper reports an absolute transition frequency, line centre or isotope or fine-structure interval from laser or microwave spectroscopy, other than an atomic clock's own frequency, or derives a fundamental constant, nuclear charge radius or test of theory from such frequencies
version: "0.1"
---

# Precision spectroscopy and frequency combs

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

| # | Reference | Identifier |
|---|---|---|
| 1 | J. Tennyson et al., Recommended isolated-line profile for representing high-resolution spectroscopic transitions (IUPAC Technical Report), Pure Appl. Chem. 86, 1931 (2014); read as arXiv:1409.7782 | doi:10.1515/pac-2014-0208 |
| 2 | M. Horbatsch and E. A. Hessels, Shifts from a distant neighboring resonance, Phys. Rev. A 82, 052519 (2010) | doi:10.1103/PhysRevA.82.052519 |
| 3 | R. C. Brown et al., Quantum interference and light polarization effects in unresolvable atomic lines: application to a precise measurement of the 6,7Li D2 lines, Phys. Rev. A 87, 032504 (2013); read as arXiv:1212.2220 | doi:10.1103/PhysRevA.87.032504 |
| 4 | A. D. Ludlow et al., Optical atomic clocks, Rev. Mod. Phys. 87, 637 (2015); read as arXiv:1407.3493 | doi:10.1103/RevModPhys.87.637 |
| 5 | T. Fortier and E. Baumann, 20 years of developments in optical frequency comb technology and applications, Commun. Phys. 2, 153 (2019); read as arXiv:1909.05384 | doi:10.1038/s42005-019-0249-y |
| 6 | E. Rubiola, On the measurement of frequency and of its sample variance with high-resolution counters, Rev. Sci. Instrum. 76, 054703 (2005); read as arXiv:physics/0411227 | doi:10.1063/1.1898203 |
| 7 | P. J. Mohr et al., CODATA recommended values of the fundamental physical constants: 2022, Rev. Mod. Phys. 97, 025002 (2025); read as arXiv:2409.03787 | doi:10.1103/RevModPhys.97.025002 |
| 8 | S. G. Karshenboim, Precision physics of simple atoms: QED tests, nuclear structure and fundamental constants, Phys. Rep. 422, 1 (2005); read as arXiv:hep-ph/0509010 | doi:10.1016/j.physrep.2005.08.008 |
| 9 | A. L. Wolf et al., Frequency metrology on the 4s 2S1/2 - 4p 2P1/2 transition in the calcium ion for a comparison with quasar data, Phys. Rev. A 78, 032511 (2008); read as arXiv:0804.4130 | doi:10.1103/PhysRevA.78.032511 |
