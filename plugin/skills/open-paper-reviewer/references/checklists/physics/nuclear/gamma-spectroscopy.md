---
id: T-GAMMA-SPECTROSCOPY
name: Gamma-ray spectroscopy
type: technique
field: physics/nuclear
applies_when: the paper measures gamma-ray spectra with germanium or scintillation detectors, or bases a claim about radionuclide identity or activity, gamma-ray energies or emission probabilities, decay data, or the presence or absence of a gamma line on them
version: "0.1"
---

# Gamma-ray spectroscopy

Gamma-ray spectroscopy with high-purity germanium (HPGe) detectors or scintillation detectors such as thallium-doped sodium iodide (NaI(Tl)) is used to claim which radionuclides or nuclear transitions are present, their activities or emission rates, and gamma-ray energies and emission probabilities. Each of these claims rests on assigning full-energy peaks to lines and converting net peak areas into emission rates through a full-energy-peak (FEP) efficiency, a live time and a set of corrections.

## 1. Energy calibration and line identification

**Question.** Do the energy-calibration lines bracket the energies used, is the calibration shown to have held during the measurement, and is each radionuclide or transition identified by more than one line, or by checking that its other expected lines are present in the expected ratios?

**Why it matters.** Peak positions move with changes in room temperature, supply voltage and count rate, and scintillation spectrometers are especially sensitive to temperature, so a drifted calibration can assign a peak to the wrong line. A single peak can also coincide, within the detector resolution, with a line from another nuclide in the sample or the background, or be an escape or sum peak rather than an emitted line, and a nuclide library chosen for the wrong kind of sample leaves peaks unidentified or misidentified.

**Resolved by.** Calibration lines with recommended energies that bracket the energies used, with residuals of the fit; the centroid and width of a reference or background peak tracked over the run; identification confirmed by secondary lines whose efficiency-corrected intensities agree with the emission probabilities; known interfering lines within about one to two full widths at half maximum (FWHM), and escape and sum peaks of strong lines, named and dealt with.

**Benchmark.** [2], [3], [5]

## 2. Full-energy-peak efficiency for the sample as measured

**Question.** How was the FEP efficiency obtained for the actual sample, and does the paper show that the calibration source matched the sample in container, fill height, source-to-detector distance, density and composition, or that corrections for the differences (self-attenuation, efficiency transfer, Monte Carlo simulation) were applied and validated?

**Why it matters.** The efficiency depends strongly on the source-to-detector geometry and on attenuation and scattering in the sample, most of all close to the detector and at low energies, so a curve measured with a point source or a different matrix does not carry over without correction. Efficiency-transfer and Monte Carlo codes applied to the same cases have agreed with measured efficiencies only to within about 10% in most cases, and have differed markedly from each other.

**Resolved by.** Calibration with traceable sources in the same geometry and a similar matrix; otherwise a detector model validated against measured efficiencies, with the transfer uncertainty stated; sample density and composition reported, with the method used for self-attenuation at low energies; the efficiency uncertainty carried into the result.

**Benchmark.** [1], [2], [3], [6], [8], [9]

## 3. True-coincidence summing

**Question.** For nuclides that emit gamma rays in cascade, or X-rays in coincidence with them, measured close to the detector or in a well, does the paper state whether true-coincidence summing corrections were applied, how they were obtained and how large they were, and whether the calibration nuclides were themselves affected?

**Why it matters.** Summing removes counts from the peaks of cascade gamma rays and adds counts at their sum energies. It grows as the source approaches the detector, with detector volume and with thin entrance windows that see X-rays, and it does not depend on count rate, so weak samples are not exempt. Calibrating a close geometry with multi-gamma sources biases the efficiency curve, and codes that compute the corrections have disagreed for high-efficiency geometries with n-type detectors and X-ray emitters.

**Resolved by.** The correction for each line used, with the method (calculation with a stated detector model, or calibration with the same nuclide in the same geometry); single-gamma nuclides, or corrected values, used to build close-geometry efficiency curves; a consistency check such as agreement between activities from several lines of one nuclide, or between measurements at two distances.

**Benchmark.** [1], [3], [10]

## 4. Dead time, pile-up and changing count rates

**Question.** What were the dead time and total input rate for the sample, background and calibration measurements, how were counting losses and pile-up corrected, and is the correction valid if the rate changed during the count, as for short-lived nuclides?

**Why it matters.** Counting losses depend on the whole processing chain, and the idealised dead-time models are often applied without checking that they fit the system and its operating conditions. Pile-up, or random summing, is a separate effect that grows with the square of the rate, moves counts out of peaks and distorts peak shapes. Pile-up rejection and loss-correction schemes change the counting statistics, and a calibration taken at high rate without correction gives an efficiency that is too low.

**Resolved by.** Dead time and input rate stated for each spectrum; the loss-correction method (live-time clock, pulser, loss-free counting) named and shown to suit the rate history; pile-up checked, for example with a pulser peak or by repeating at a larger distance; decay during counting corrected using clock time; uncertainties of corrected counts that match the correction method.

**Benchmark.** [1], [2], [3], [11], [12]

## 5. Background and its subtraction

**Question.** How was the background measured (duration, timing relative to the sample, shield and radon-purge conditions), which background lines fall at or near the analyte energies, and does the subtraction account for the effect of the sample itself on the background?

**Why it matters.** The background comes from natural radionuclides in buildings, shields and detector parts, from radon progeny in the air inside the shield and from cosmic rays, and it varies with time. A background peak at the analyte energy must be subtracted as well as the continuum. A dense sample shields the detector from external background, so subtracting a background taken without it can bias net rates and detection limits, at low levels even to significantly negative values.

**Resolved by.** Background spectra of comparable duration, close in time, with the same shield and purge conditions; background peak rates at the analyte energies reported; for low-level results, the background level stated, its stability shown across repeated measurements, and the shielding effect of the sample estimated or bounded; an empty container or blank measured where relevant.

**Benchmark.** [2], [3], [13], [14]

## 6. Net peak areas and multiplets

**Question.** How were net peak areas obtained (peak-search settings, peak shape including tailing, baseline under the peak, region limits), and for peaks within about one to two FWHM of another line, how were the components separated and checked?

**Why it matters.** Analysis programs agree well on isolated peaks, but doublets closer than about 1.2 FWHM have often been fitted as single peaks with position uncertainties much too small, and default settings have given worse results than settings chosen by the user. Peak-acceptance thresholds set too low report nuclides that are not there; set too high, they miss small peaks, and small, poorly defined peaks barely above the continuum are the hardest to find and fit.

**Resolved by.** The fit function and baseline model stated; the fitted spectrum with residuals shown for the peaks on which the claims rest; multiplets resolved with energies and widths constrained from the calibration, by subtracting an interferer using its other lines, or by using an interference-free line instead; the fitting and unfolding uncertainty included in the peak-area uncertainty.

**Benchmark.** [1], [3], [7]

## 7. Decision threshold and detection limit

**Question.** For a claim that a line or nuclide is detected, or absent, does the paper define a decision threshold from the background and blank, quote the detection limit separately, and give the expressions and error probabilities used?

**Why it matters.** The minimum detectable activity is a performance characteristic of the measurement, and comparing a measured result with it to decide detection is a recognised error. Poisson-based expressions hold only when the blank behaves like a Poisson count, and radioanalytical guidance asks for each result to be reported as a value with its uncertainty, not only as below a detection limit.

**Resolved by.** The decision threshold and detection limit expressions cited to a stated framework, with the error probabilities; the blank or background used for them justified; each result reported with its uncertainty even when it is below the threshold or negative; any upper limit stated with the method used to obtain it.

**Benchmark.** [4], [14]

## 8. Decay data and decay corrections

**Question.** Which half-lives, emission probabilities and energies were used, from which evaluated source and version, for both the calibration nuclides and the analytes, and were the decay corrections (to a reference time and during counting) and the uncertainties of these data included?

**Why it matters.** Different evaluations recommend slightly different values for the same quantity, and small differences in the data for calibration nuclides propagate into every efficiency and activity derived from them. The emission probability enters each activity directly, and calibrating with a different nuclide from the analyte requires a correction for the difference in decay schemes. Some inputs are correlated, which affects fits and uncertainties.

**Resolved by.** The decay-data source named with its version; emission probability and half-life uncertainties propagated, with correlations considered where the same data enter calibration and analysis; reference dates for the calibration source and the sample stated; the decay correction during counting applied with clock time when the counting time is not short compared with the half-life.

**Benchmark.** [2], [3], [5], [6]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | International Electrotechnical Commission, IEC 61452:2021, Nuclear instrumentation – Measurement of activity or emission rate of gamma-ray emitting radionuclides – Calibration and use of germanium-based spectrometers, edition 2.0 (2021); read as the publisher's preview of the foreword, introduction, scope and contents | https://www.vde-verlag.de/iec-normen/preview-pdf/info_iec61452%7Bed2.0%7Den.pdf | abstract | Introduction: emission rate from net FEP area, live time and FEP efficiency for the geometry used, with corrections for decay, attenuation and solid angle not covered by the calibration, true-coincidence summing and pile-up. Scope: performance tests of algorithms for single and multiplet peaks; methods to measure and correct pile-up; a test of the size of true-coincidence summing. Contents: sections on pile-up, cascade summing and Monte Carlo efficiency uncertainties |
| 2 | U.S. Environmental Protection Agency and others, Multi-Agency Radiological Laboratory Analytical Protocols Manual (MARLAP), NUREG-1576, EPA 402-B-04-001B, Volume II, Chapter 15, Quantification of Radionuclides (2004) | https://www.epa.gov/sites/default/files/2015-05/documents/402-b-04-001b-15-final.pdf | full text | Sec. 15.2.2: calibration sources should match test sources in geometry, self-absorption and density; decay-scheme corrections when another nuclide is used. Sec. 15.2.5: dead-time losses and random summing during calibration bias efficiency low. Sec. 15.6.2: NaI(Tl) resolution, background sources, temperature-driven spectral shifts and misidentification. Sec. 15.6.3: HPGe background from natural radionuclides in shield materials and from cosmic rays (511 keV peak), changing under unusual conditions; calibration per geometry with density corrections; calibration decay data from an evaluated database; random sum rate grows with the square of the count rate, pile-up affects peak shape, and peaks shift at high rates and with supply-voltage changes; cascade summing falls with distance; random and cascade sum peaks and escape peaks; doublets within about one to two FWHM, alternative interference-free lines and checks of secondary-line ratios |
| 3 | U.S. Environmental Protection Agency and others, MARLAP, NUREG-1576, EPA 402-B-04-001B, Volume II, Chapter 16, Data Acquisition, Reduction, and Reporting for Nuclear-Counting Instrumentation (2004) | https://www.epa.gov/sites/default/files/2015-05/documents/402-b-04-001b-16-final.pdf | full text | Sec. 16.2.2: decay during counting with clock time; high dead time affects peak shape. Sec. 16.3.1.1: library choice and interfering lines; acceptance thresholds too low or too high give false or missed peaks; secondary lines to confirm identity. Secs. 16.3.1.2 to 16.3.1.5: multiplet deconvolution, interference-free lines, energy calibration with lines across the range, tailing and baseline under the peak. Sec. 16.3.1.7: efficiency curve for each geometry. Sec. 16.3.1.8: true-coincidence summing grows close to the detector, with volume and thin windows, is independent of count rate; single-gamma nuclides for close-geometry calibration. Sec. 16.3.1.9: uncertainty terms for peak area, background peak, unfolding, summing correction, branching ratio and decay constant |
| 4 | U.S. Environmental Protection Agency and others, MARLAP, NUREG-1576, EPA 402-B-04-001C, Volume III, Chapter 20, Detection and Quantification Capabilities Overview (2004) | https://www.epa.gov/sites/default/files/2015-05/documents/402-b-04-001c-20_final.pdf | full text | Secs. 20.2.2 to 20.2.4: detection decided by comparing the signal with a critical value; comparing a result with the minimum detectable concentration to decide detection is incorrect. Sec. 20.3: check the Poisson approximation before using Poisson-based critical values, otherwise use replicated blanks; minimum detectable value only as a performance characteristic; report each result with its uncertainty even if negative, never as less than the detection limit |
| 5 | International Atomic Energy Agency, Update of X Ray and Gamma Ray Decay Data Standards for Detector Calibration and Other Applications, Volume 1: Recommended Decay Data, High Energy Gamma Ray Standards and Angular Correlation Coefficients, STI/PUB/1287 (2007) | https://www-pub.iaea.org/MTCD/publications/PDF/Pub1287_Vol1_web.pdf | full text | Foreword: evaluators recommend slightly different values, and small deviations in decay data for calibration nuclides propagate into efficiency calibrations and later measurements. Secs. 1 to 3: recommended half-lives, gamma-ray energies and emission probabilities with standard uncertainties for calibration nuclides, and high-energy gamma-ray standards |
| 6 | M.-C. Lépy, A. Pearce and O. Sima, Uncertainties in gamma-ray spectrometry, Metrologia 52, S123–S145 (2015) | doi:10.1088/0026-1394/52/3/S123 | abstract | Abstract: the combined uncertainty depends on the main inputs and on correction factors; the sample's physical parameters must be well characterised; the focus is on efficiency calibration, peak area and corrections; some inputs are correlated, which matters for fits and uncertainties; relative combined uncertainties are rarely below 1% |
| 7 | International Atomic Energy Agency, Intercomparison of gamma ray analysis software packages, IAEA-TECDOC-1011 (1998) | https://www-pub.iaea.org/MTCD/Publications/PDF/te_1011_prn.pdf | full text | Chapter 9 (Conclusions): programmes agree on singlet peak areas to about 1%; doublets separated by less than 1.2 FWHM are often taken as singlets with much too small position uncertainties; user-defined settings usually do better than defaults; residual plots help users judge fit quality |
| 8 | M.-C. Lépy and others, Intercomparison of efficiency transfer software for gamma-ray spectrometry, Appl. Radiat. Isot. 55, 493–503 (2001) | doi:10.1016/S0969-8043(01)00101-4 | abstract | Abstract: efficiency transfer from a reference point source to other distances and to cylindrical sources with three matrices; deviations between computed and measured efficiencies mostly within 10%; quality uneven, so codes are not for direct metrological use |
| 9 | T. Vidmar and others, An intercomparison of Monte Carlo codes used in gamma-ray spectrometry, Appl. Radiat. Isot. 66, 764–768 (2008) | doi:10.1016/j.apradiso.2008.02.015 | abstract | Abstract: commonly used Monte Carlo codes applied to the same full-energy-peak and total efficiency calculations showed surprising differences between codes |
| 10 | T. Vidmar and others, Equivalence of computer codes for calculation of coincidence summing correction factors, Appl. Radiat. Isot. 87, 336–341 (2014) | doi:10.1016/j.apradiso.2013.11.045 | abstract | Abstract: codes agreed for a p-type detector model, but results scattered for high-efficiency geometries with an n-type detector and a nuclide emitting abundant X-rays |
| 11 | S. Usman and A. Patil, Radiation detector deadtime and pile up: a review of the status of science, Nucl. Eng. Technol. 50, 1006–1016 (2018) | doi:10.1016/j.net.2018.06.014 | abstract | Abstract: paralysable and non-paralysable models are used without regard to operating conditions; no general agreement on which model fits a given detector; pile-up is often confused with dead time |
| 12 | S. Pommé, Dead time, pile-up, and counting statistics, in Applied Modeling and Computations in Nuclear Science, ACS Symposium Series 945, 218–233 (2007; online 2006) | doi:10.1021/bk-2007-0945.ch016 | abstract | Abstract: non-random count loss causes deviations from Poisson statistics; misconceptions include confusing pile-up with extending dead time and neglecting the effect of pile-up rejection on fixed live-time and loss-free counting; statistics of loss-free and zero-dead-time spectra and uncertainty formulas for different count-loss types |
| 13 | M. Hult, Low-level gamma-ray spectrometry using Ge-detectors, Metrologia 44, S87–S94 (2007) | doi:10.1088/0026-1394/44/4/S12 | abstract | Abstract: identifying and reducing the background components of HPGe systems is one of the two main developments that lowered detection limits |
| 14 | M. Thiesse, P. Scovell and L. Thompson, Background shielding by dense samples in low-level gamma spectrometry, Appl. Radiat. Isot. 188, 110384 (2022); read as arXiv:2204.06792 | doi:10.1016/j.apradiso.2022.110384 | full text | Sec. 1: external background sources include cosmogenic radiation, building materials, the shield and airborne radon inside the shield, which is reduced by purging. Abstract and Secs. 2 to 3: a dense sample attenuates external background more than the low-density standard, biasing activities and detection limits if ignored in background subtraction, most for large-solid-angle geometries. Sec. 5, Table 2: uncorrected net rates significantly negative for several lines. Secs. 4 to 6: report conservative limits when background source locations are unknown |
