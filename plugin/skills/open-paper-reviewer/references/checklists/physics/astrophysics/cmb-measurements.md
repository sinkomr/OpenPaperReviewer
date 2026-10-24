---
id: T-CMB-MEASUREMENTS
name: Cosmic microwave background measurements
type: technique
field: physics/astrophysics
applies_when: the paper measures cosmic microwave background temperature or polarization maps or power spectra, separates Galactic foregrounds from them, or bases a claim about B-mode polarization, the tensor-to-scalar ratio, cosmic birefringence or polarized foregrounds on such data
version: "0.1"
---

# Cosmic microwave background measurements

Cosmic microwave background (CMB) measurements are used to claim maps and angular power spectra of the temperature and polarization of the CMB, and the cosmological parameters derived from them. The most demanding claims concern B-mode (curl-type) polarization, whose amplitude sets the tensor-to-scalar ratio r of primordial gravitational waves; it is far fainter than the E-mode (curl-free) polarization, the temperature signal and the polarized Galactic foregrounds from dust and synchrotron emission.

## 1. Foreground model and component separation

**Question.** How were Galactic and extragalactic foregrounds separated from the CMB (which method, which frequency channels, which spectral model for dust and synchrotron), and does the paper show that the result holds when the method or the foreground model is changed?

**Why it matters.** Polarized foregrounds are brighter than the primordial B-mode signal over most of the sky, and their spectra and angular power vary from region to region. A parametric fit with too simple a model, such as one dust component where the sky needs two, or no curvature in the synchrotron spectrum, can bias the tensor-to-scalar ratio by several standard deviations for a sensitive experiment. Different separation methods make different assumptions, so agreement between them is a test of the result.

**Resolved by.** The frequency channels and the foreground model stated, with the priors on spectral parameters; residual foregrounds estimated from simulations or from comparison of maps; the main result repeated with a second separation method or with an extended foreground model (extra dust component, curved synchrotron spectrum, frequency decorrelation) and shown not to move by more than its uncertainty; the sky mask and its dependence on foreground level stated.

**Benchmark.** [1], [2], [3]

## 2. Primordial B modes against lensing and dust

**Question.** For a claim of primordial B-mode polarization or a limit on r, how does the paper account for B modes produced by gravitational lensing of E modes and by polarized dust in the observed field, and does it use enough frequencies to tell a CMB spectrum from a foreground spectrum?

**Why it matters.** Lensing converts E modes into B modes whose power rises relative to the primordial signal toward smaller angular scales, and it limits the sensitivity to r more as the r sought gets smaller. No region of the sky is free enough of foregrounds to detect primordial B modes without subtracting them, and dust measured at one frequency can be mistaken for a CMB signal. A signal seen at a single frequency cannot by itself be shown to have the CMB spectrum.

**Resolved by.** The lensing contribution modelled, or removed by delensing with a stated residual; data at several frequencies, including at least one dominated by dust and, at low frequency, by synchrotron, analysed jointly or cross-correlated; the dust amplitude in the observed field measured, not assumed; the angular scale of the signal compared with the recombination and reionization features expected from gravitational waves; the result reported as a detection only when the foreground and lensing models leave it significant.

**Benchmark.** [3], [4]

## 3. Beam mismatch and temperature-to-polarization leakage

**Question.** How were the beams measured, and how does the paper show that differences between the beams of the detectors that are combined to measure polarization (differential gain, pointing, width and ellipticity) do not leak temperature into polarization at the level of the claimed signal?

**Why it matters.** Polarization is often measured by differencing two orthogonal detectors, so any difference in their beams or gains turns the much larger temperature signal into false polarization, and pointing and calibration errors also mix E modes into B modes. Leakage of the kind produced by differential beam width is most harmful near the first acoustic peak, close to the angular scales where primordial B modes peak. Removing the leading beam-mismatch terms by filtering or template regression leaves higher-order residuals that need their own estimate.

**Resolved by.** Measured beam maps for each detector or detector pair, with the differential parameters reported; the method that removes or subtracts leakage stated (template regression, deprojection, subtraction from beam measurements); the remaining leakage estimated by passing measured beams and a temperature-only sky through the full pipeline; that residual expressed as an equivalent bias on r or on the B-mode bandpowers and shown to be small compared with the statistical uncertainty.

**Benchmark.** [5], [6]

## 4. Polarization angle calibration

**Question.** How was the absolute polarization angle of the detectors calibrated (artificial source, astrophysical source such as the Crab nebula, or the CMB itself), with what uncertainty, and how does that uncertainty enter the B-mode result and any EB or TB correlation the paper reports?

**Why it matters.** An error in the polarization angle rotates the large E-mode signal into B modes and produces EB and TB correlations that standard cosmology predicts to be zero. Setting the angle by forcing EB and TB to vanish removes this, but it cannot then distinguish an angle error from a real rotation such as cosmic birefringence, and foregrounds or other systematics can also produce EB and TB. Hardware and astrophysical calibrators have often been limited to roughly a degree, coarser than small values of r require.

**Resolved by.** The calibration method and the angle uncertainty stated; the effect of that uncertainty on the B-mode spectrum or on r computed; if the angle is set from EB and TB, a statement that this assumes no parity-violating signal, and no claim of cosmic birefringence or similar physics from the same correlations without an independent angle calibration; agreement between angles from different calibrators or frequencies shown.

**Benchmark.** [5], [7], [8]

## 5. Gain, bandpass and polarization efficiency calibration

**Question.** How were the absolute gain, the relative gains of detectors that are differenced, their bandpasses and their polarization efficiencies calibrated, and does the paper estimate the false polarization that mismatches between detectors produce?

**Why it matters.** The absolute gain sets the amplitude of every spectrum and of any r derived from it, and the polarized signal scales also with the polarization efficiency. A mismatch in gain or bandpass between detectors that are differenced turns temperature and foreground intensity into false polarization, and bandpass mismatch makes this leakage depend on the spectrum of the source.

**Resolved by.** The absolute calibrator named (for example the CMB dipole, a planet or a polarized source) with its uncertainty; relative gains measured and their time variation tracked; bandpasses measured and any bandpass-mismatch leakage fitted or corrected; polarization efficiencies measured or marginalized over; residual calibration effects estimated from simulations and propagated into the spectra.

**Benchmark.** [1], [9], [10]

## 6. Filtering, partial sky and E-to-B mixing

**Question.** How were the effects of time-stream filtering, the sky mask and incomplete sky coverage on the power spectra corrected, and how was the leakage of E-mode power into B modes estimated and removed?

**Why it matters.** Filtering removes part of the signal, mostly at large scales, and a mask couples different multipoles. On an incomplete sky some modes cannot be assigned uniquely to E or B; because E is much larger than B, these ambiguous modes leak E power into the B-mode estimate and can dominate its variance. Subtracting the mean leakage removes the bias but not the added variance.

**Resolved by.** A transfer function for filtering estimated from signal-only simulations passed through the same pipeline; the mode-coupling from the mask corrected; an estimator designed to suppress E-to-B mixing, such as a pure pseudo-spectrum, or an explicit estimate of the leaked power; the full pipeline validated on simulations with known input spectra, recovering them without bias; noise bias estimated from simulations or removed with cross-spectra.

**Benchmark.** [11], [12]

## 7. Null tests and data splits

**Question.** Which null tests were made (how the data were split, how many tests, which statistic), what is the distribution of their probabilities to exceed, and were the data selection and the null tests fixed before the signal spectra were examined?

**Why it matters.** Differencing maps from two halves of the data cancels the sky signal and leaves noise and any systematic that differs between the halves, such as pickup tied to scan direction, ground or Sun position, detector subset or season. A set of null tests passes only if its probabilities to exceed are consistent with a uniform distribution once correlations between tests are allowed for. Data selection is often adjusted until the tests pass; keeping the signal spectra hidden while this is done stops those choices being tuned to the result.

**Resolved by.** The list of splits chosen to target the expected systematics (scan direction, boresight angle, detector type, time, environmental conditions, ground and Sun proximity); null spectra compared with noise simulations through the same pipeline; the distribution of probabilities to exceed shown, with the expected number of failures for the number of tests; any failures and the changes they prompted reported; the analysis blind to the signal spectra until selection and calibration were final.

**Benchmark.** [1], [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | Planck Collaboration (Y. Akrami et al.), Planck 2018 results. IV. Diffuse component separation, Astron. Astrophys. 641, A4 (2020); read as preprint arXiv:1807.06208 | doi:10.1051/0004-6361/201833881 | full text | Secs. 1 and 2: four CMB separation methods of different classes (blind and non-blind, pixel and harmonic) applied to the same data, with the advice to use all four to test robustness to algorithmic choices. Sec. 3.2: half-mission and odd-even splits as tracers of instrumental systematics and noise; polarization efficiencies noted as a significant uncertainty. Secs. 3.5 and 4.4: simulations through each pipeline as the basis for goodness-of-fit tests. Sec. 5.3: polarization-efficiency corrections shift the fitted dust spectral index, and the difference is reported as a known systematic |
| 2 | M. Remazeilles, C. Dickinson, H. K. K. Eriksen and I. K. Wehus, Sensitivity and foreground modelling for large-scale CMB B-mode polarization satellite missions, Mon. Not. R. Astron. Soc. 458, 2032–2050 (2016) | doi:10.1093/mnras/stw441 | abstract | Abstract: fitting one modified blackbody when the sky has two dust components biases r by more than 5 sigma for the most sensitive experiments; ignoring synchrotron spectral curvature can bias r by more than 1 sigma; modelling errors matter more as sensitivity rises |
| 3 | Planck Collaboration (Y. Akrami et al.), Planck 2018 results. XI. Polarized dust foregrounds, Astron. Astrophys. 641, A11 (2020) | doi:10.1051/0004-6361/201832618 | abstract | Abstract: dust EE and BB power-law exponents vary between sky regions and differ between EE and BB; foreground amplitudes and spectra estimated per region with Planck and WMAP; component separation for the reionization and recombination features will be difficult; no decorrelation detected across frequencies |
| 4 | M. Kamionkowski and E. D. Kovetz, The quest for B modes from inflationary gravitational waves, Annu. Rev. Astron. Astrophys. 54, 227–269 (2016); read as preprint arXiv:1510.06042 | doi:10.1146/annurev-astro-081915-023433 | full text | Sec. 5: gravitational-wave B modes show a recombination peak near multipole 100 and a reionization bump at low multipoles. Sec. 6: lensing turns a curl-free polarization pattern into one with B modes. Secs. 8.2.1, 8.3.1 and 8.3.5: lensing B modes limit the sensitivity to r, rise relative to the gravitational-wave signal with multipole, and matter more as r gets smaller; delensing reduces them. Sec. 7.1: no sky region found clean enough for detection without foreground subtraction; correlation with a high-frequency map used to attribute a single-frequency signal to dust. Secs. 7 and 8.3.4: multi-frequency measurements over the same field used to separate components |
| 5 | W. Hu, M. M. Hedman and M. Zaldarriaga, Benchmark parameters for CMB polarization experiments, Phys. Rev. D 67, 043004 (2003); read as preprint arXiv:astro-ph/0210096 | doi:10.1103/PhysRevD.67.043004 | full text | Secs. I and II: differential gain, differential pointing, beam width and ellipticity leak temperature into polarization; cross-coupling acts as a rotation of the polarization angle. Sec. III.2: calibration, rotation and pointing errors mix E into B. Sec. III.3: monopole leakage, which includes differential beam width, is most harmful near the first acoustic peak, close to the multipoles of gravitational-wave B modes. Abstract: temperature leakage must be controlled to about 1e-4 to 1e-3 |
| 6 | BICEP2 and Keck Array Collaborations (P. A. R. Ade et al.), BICEP2/Keck Array XI: beam characterization and temperature-to-polarization leakage in the BK15 dataset, Astrophys. J. 884, 114 (2019); read as preprint arXiv:1904.01640 | doi:10.3847/1538-4357/ab391d | full text | Secs. III.2 and III.3: differential beam parameters from fits to measured far-field beams; deprojection regresses pair-difference data against temperature templates, leaving higher-order residuals. Sec. V.1: measured per-detector beam maps convolved with a temperature-only sky and run through the pipeline to estimate leakage. Sec. VI.2: the residual leakage expressed as a bias on r and compared with the statistical error on r |
| 7 | B. G. Keating, M. Shimon and A. P. S. Yadav, Self-calibration of cosmic microwave background polarization experiments, Astrophys. J. Lett. 762, L23 (2013); read as preprint arXiv:1211.5734 | doi:10.1088/2041-8205/762/2/L23 | full text | Introduction: hardware and astrophysical calibrators do no better than about 1 degree; miscalibration creates EB and TB correlations, which vanish in standard cosmology; angle uncertainty of a few arcminutes needed to keep the bias on r = 0.01 small. Polarization map making and miscalibration: an angle error mixes E and B. Discussion: angle error and cosmic birefringence are degenerate, so self-calibration cannot separate them |
| 8 | J. Aumont, J. F. Macías-Pérez, A. Ritacco, N. Ponthieu and A. Mangilli, Absolute calibration of the polarisation angle for future CMB B-mode experiments from current and future measurements of the Crab nebula, Astron. Astrophys. 634, A100 (2020); read as preprint arXiv:1805.10475 | doi:10.1051/0004-6361/201833504 | full text | Sec. 1: setting the angle by minimizing EB and TB is limited by foregrounds, systematics and possible birefringence. Secs. 2 and 3: Crab angle measurements combined across frequencies and experiments, with the combined error depending on assumptions. Sec. 4: the E-to-B leakage does not depend on scan pattern and cannot be mitigated by it. Secs. 4 and 5: bias on r grows roughly as the square of the angle error |
| 9 | Planck Collaboration (N. Aghanim et al.), Planck 2018 results. III. High Frequency Instrument data processing and frequency maps, Astron. Astrophys. 641, A3 (2020) | doi:10.1051/0004-6361/201832909 | abstract | Abstract: dipole-based calibration reduces intensity-to-polarization leakage from calibration mismatch; bandpass leakage reduced by fitting per-detector bandpass-mismatch coefficients in mapmaking; simulations used to correct a small calibration bias and measure residual systematics; polarization data improved over the previous release |
| 10 | QUIET Collaboration (C. Bischoff et al.), First season QUIET observations: measurements of cosmic microwave background polarization power spectra at 43 GHz in the multipole range 25 ≤ ℓ ≤ 475, Astrophys. J. 741, 111 (2011); read as preprint arXiv:1012.3191 | doi:10.1088/0004-637X/741/2/111 | full text | Secs. IV.1, IV.3 and IV.5: absolute responsivity from a polarized astrophysical source with cross-checks, polarization angles from the Moon with Tau A as a cross-check, and leakage from intensity to polarization assigned a systematic error. Sec. VI: calibration and data selection finalized before the power spectra were examined; 42 null tests from splits by detector, pointing, Sun and Moon proximity and environment; null statistics compared with Monte Carlo simulations of the full suite and their probabilities to exceed checked for uniformity |
| 11 | K. M. Smith and M. Zaldarriaga, General solution to the E-B mixing problem, Phys. Rev. D 76, 043001 (2007); read as preprint arXiv:astro-ph/0610059 | doi:10.1103/PhysRevD.76.043001 | full text | Secs. I and II.3: on an incomplete sky some modes are ambiguous between E and B and are dominated by E power; subtracting the mean leakage removes the bias but not the extra variance, which can dominate the B-mode error. Secs. III and IV: pure pseudo-spectrum estimators suppress the mixing. Sec. VIII: large gains over ordinary pseudo-spectra at low multipoles |
| 12 | E. Hivon, K. M. Górski, C. B. Netterfield, B. P. Crill, S. Prunet and F. Hansen, MASTER of the cosmic microwave background anisotropy power spectrum: a fast method for statistical analysis of large and complex cosmic microwave background data sets, Astrophys. J. 567, 2–17 (2002); read as preprint arXiv:astro-ph/0105302 | doi:10.1086/338126 | full text | Secs. II.2 and III: the cut-sky pseudo-spectrum mixes multipoles through a kernel set by the mask. Sec. III.2: a transfer function for time-stream filtering estimated from signal-only simulations through the same pipeline. Sec. III.3: noise bias from noise-only simulations. Sec. IV: the method validated by recovering known input spectra from simulated data |
