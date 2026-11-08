---
id: T-CMB-MEASUREMENTS
name: Cosmic microwave background measurements
type: technique
field: physics/astrophysics
applies_when: the paper measures cosmic microwave background temperature or polarization maps or power spectra, separates Galactic foregrounds from them, or bases a claim about B-mode polarization, the tensor-to-scalar ratio, cosmic birefringence or polarized foregrounds on such data
version: "0.1"
---

# Cosmic microwave background measurements

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

| # | Reference | Identifier |
|---|---|---|
| 1 | Planck Collaboration (Y. Akrami et al.), Planck 2018 results. IV. Diffuse component separation, Astron. Astrophys. 641, A4 (2020); read as preprint arXiv:1807.06208 | doi:10.1051/0004-6361/201833881 |
| 2 | M. Remazeilles et al., Sensitivity and foreground modelling for large-scale CMB B-mode polarization satellite missions, Mon. Not. R. Astron. Soc. 458, 2032 (2016) | doi:10.1093/mnras/stw441 |
| 3 | Planck Collaboration (Y. Akrami et al.), Planck 2018 results. XI. Polarized dust foregrounds, Astron. Astrophys. 641, A11 (2020) | doi:10.1051/0004-6361/201832618 |
| 4 | M. Kamionkowski and E. D. Kovetz, The quest for B modes from inflationary gravitational waves, Annu. Rev. Astron. Astrophys. 54, 227 (2016); read as preprint arXiv:1510.06042 | doi:10.1146/annurev-astro-081915-023433 |
| 5 | W. Hu et al., Benchmark parameters for CMB polarization experiments, Phys. Rev. D 67, 043004 (2003); read as preprint arXiv:astro-ph/0210096 | doi:10.1103/PhysRevD.67.043004 |
| 6 | BICEP2 and Keck Array Collaborations (P. A. R. Ade et al.), BICEP2/Keck Array XI: beam characterization and temperature-to-polarization leakage in the BK15 dataset, Astrophys. J. 884, 114 (2019); read as preprint arXiv:1904.01640 | doi:10.3847/1538-4357/ab391d |
| 7 | B. G. Keating et al., Self-calibration of cosmic microwave background polarization experiments, Astrophys. J. Lett. 762, L23 (2013); read as preprint arXiv:1211.5734 | doi:10.1088/2041-8205/762/2/L23 |
| 8 | J. Aumont et al., Absolute calibration of the polarisation angle for future CMB B-mode experiments from current and future measurements of the Crab nebula, Astron. Astrophys. 634, A100 (2020); read as preprint arXiv:1805.10475 | doi:10.1051/0004-6361/201833504 |
| 9 | Planck Collaboration (N. Aghanim et al.), Planck 2018 results. III. High Frequency Instrument data processing and frequency maps, Astron. Astrophys. 641, A3 (2020) | doi:10.1051/0004-6361/201832909 |
| 10 | QUIET Collaboration (C. Bischoff et al.), First season QUIET observations: measurements of cosmic microwave background polarization power spectra at 43 GHz in the multipole range 25 ≤ ℓ ≤ 475, Astrophys. J. 741, 111 (2011); read as preprint arXiv:1012.3191 | doi:10.1088/0004-637X/741/2/111 |
| 11 | K. M. Smith and M. Zaldarriaga, General solution to the E-B mixing problem, Phys. Rev. D 76, 043001 (2007); read as preprint arXiv:astro-ph/0610059 | doi:10.1103/PhysRevD.76.043001 |
| 12 | E. Hivon et al., MASTER of the cosmic microwave background anisotropy power spectrum: a fast method for statistical analysis of large and complex cosmic microwave background data sets, Astrophys. J. 567, 2 (2002); read as preprint arXiv:astro-ph/0105302 | doi:10.1086/338126 |
