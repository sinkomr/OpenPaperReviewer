---
id: T-THOMSON-SCATTERING
name: Thomson scattering
type: technique
field: physics/plasma
applies_when: the paper infers electron temperature or density, ion temperature, charge state, flow or an electron distribution from laser light scattered by free electrons in a plasma, by incoherent (non-collective) or collective Thomson scattering, or bases a claim about plasma conditions on such spectra
version: "0.1"
---

# Thomson scattering

Thomson scattering (TS) of a probe laser by free electrons is used to claim local values of electron temperature and density and, from the collective electron plasma wave (EPW) and ion-acoustic wave (IAW) features, ion temperature, charge state, flow and the shape of the electron distribution. These values are inferred by fitting a model spectrum to a very weak signal, about 10^-12 of the probe power, that is calibrated against Rayleigh or Raman scattering from a gas.

## 1. Scattering regime and spectral model

**Question.** Does the paper state the probe wavelength, the scattering angle and the resulting scattering parameter (the ratio of the scattering length to the Debye length, usually written alpha), and is the spectral model it fits appropriate to that regime?

**Why it matters.** Only for alpha well below one does the spectrum map the electron velocity distribution directly, so that its width gives the temperature and its area the density. Near alpha of one, collective features appear and a non-collective width formula gives biased values; at larger alpha the spectrum carries plasma-wave resonances whose positions and widths depend on density, temperature and composition together.

**Resolved by.** Alpha given for the conditions of each measurement; a non-collective model used only where alpha is small; the full collective form factor fitted where alpha approaches or exceeds one; the measured feature (electron, ion-acoustic or both) and the quantity taken from each stated.

**Benchmark.** [1], [5]

## 2. Absolute density calibration

**Question.** How was the density scale calibrated: which gas and pressure, which Rayleigh or Raman cross-sections, with the same optics, alignment and detector settings as the plasma measurement, and how was the Rayleigh signal separated from stray light at the same wavelength?

**Why it matters.** The density follows from the ratio of the Thomson signal to a calibration signal, so any error in the gas density, the cross-section or the collection efficiency passes directly into it. Rayleigh light lies at the laser wavelength with the stray light and is removed by a notch filter, so a Rayleigh calibration needs extra measurements, while a Raman calibration is weak and must be fitted with the instrument function. A calibration taken with a different laser position, or a much brighter calibration signal that pushes the detector out of its linear range, does not carry over to the plasma data.

**Resolved by.** Gas, pressure and cross-sections stated; the Raman or Rayleigh spectrum shown with its fit; calibration signals of similar size to the Thomson signal, or a demonstrated linear detector; calibration done at the laser alignment used for the plasma, or alignment shown to be unchanged; an independent check, such as a second calibration method or agreement with an interferometer.

**Benchmark.** [3], [4], [10]

## 3. Stray light, notch filtering and background

**Question.** How large were stray laser light and plasma emission compared with the scattered signal, how were they removed, which part of the spectrum was blocked by a notch or filter, and how is the blocked part handled in the fit?

**Why it matters.** Stray light at the laser wavelength can exceed the Thomson signal by orders of magnitude, and plasma emission adds a background that varies with the plasma. Subtracting a background removes its mean but not its photon noise. A notch removes the centre of the spectrum, which can hold much of a narrow low-temperature spectrum and, in a spectrometer built for the electron feature, the whole ion-acoustic feature. In molecular gases rotational Raman lines from neutral molecules overlap the Thomson spectrum.

**Resolved by.** Raw spectra with and without plasma, and with and without the laser, so that each background can be seen; interleaved background shots; the blocked wavelength band stated and excluded from the fit; for molecular plasmas, Raman scattering from the neutral gas measured or modelled and separated; the effect of the remaining background on the fitted values estimated.

**Benchmark.** [2], [3], [4], [5]

## 4. Instrument function and spectral calibration

**Question.** Was the instrument function of the spectrometer, or the relative spectral sensitivity of each filter channel, measured and included in the fit, and how stable was it?

**Why it matters.** The temperature comes from the width or the shape of the spectrum. For a spectrometer, a spectrum not much wider than the instrument function, or one affected by its diffraction wings, gives a biased width unless the model is convolved with it. For filter polychromators, the temperature follows from ratios between channels, so their relative sensitivities enter it directly and decide the temperature range the system can measure.

**Resolved by.** An instrument function measured, for example with laser light, and convolved with the model; for polychromators, a relative spectral calibration with a broadband source, its reproducibility stated, and the effect of its uncertainty on the temperature estimated; the temperature range of the filter set stated and the reported values shown to lie within it.

**Benchmark.** [3], [4], [8], [10]

## 5. Relativistic corrections at high temperature

**Question.** Where electron temperatures reach the keV range, or where electron plasma wave features are fitted, does the spectral model include relativistic and finite-velocity corrections, and does the paper state which form it uses?

**Why it matters.** At high temperature the incoherent spectrum is shifted to the blue and the scattered light is partly depolarised, so a non-relativistic Gaussian no longer describes its shape, and the depolarisation interacts with any polarisation-sensitive optics. For collective scattering from electron plasma waves, corrections of first order in electron velocity over the speed of light change the peak intensities, and leaving them out can overestimate the damping and so the fitted temperature.

**Resolved by.** A relativistic spectral form, or a stated velocity correction, used and named; for incoherent scattering at high temperature, the blue shift and depolarisation handled, including the polarisation response of the collection optics; the size of the correction shown for the reported conditions.

**Benchmark.** [7], [8]

## 6. Ion-acoustic fitting and the distribution function

**Question.** For collective spectra, which parameters were free in the fit and which were fixed (charge state, ion species, ion temperature, flow, electron parameters), is a Maxwellian distribution assumed and justified, and are correlations between fitted parameters shown?

**Why it matters.** Where ion Landau damping is weak, the positions of the ion-acoustic peaks give mainly the product of charge state and electron temperature. The ion temperature comes from the peak shape in a mildly collective regime, or from extra modes when a second ion species is present, so it depends on the assumed composition. A distribution that is not Maxwellian, such as a flat-topped super-Gaussian, changes the damping of the plasma waves, and a Maxwellian fit then returns temperatures and densities that can be far from the true values. An error in the electron model also passes into the ion parameters, and different distributions can give nearly the same spectrum.

**Resolved by.** Free and fixed parameters listed, with the source of each fixed value, such as an independent measurement of electron density and temperature from the electron feature; composition and charge state stated and justified; the Maxwellian assumption tested against a non-Maxwellian model or supported by collision times short compared with the measurement; joint uncertainties or posterior distributions shown, not only single-parameter errors; the fitting method checked on synthetic spectra.

**Benchmark.** [1], [5], [9]

## 7. Heating and perturbation by the probe laser

**Question.** Does the paper estimate or measure how far the probe laser heats or otherwise disturbs the plasma it measures, for example by repeating the measurement at several probe energies?

**Why it matters.** Electrons absorb probe light by inverse bremsstrahlung, with neutrals as well as ions in weakly ionised gas, so the temperature can rise during the pulse and the density can change; the measured value is then that of a heated plasma. The ponderomotive force of the probe can push electrons out of the scattering volume in low-density plasmas, and above a critical power the probe can self-focus. Whether the measurement is non-intrusive has to be checked for each plasma, not assumed.

**Resolved by.** Probe energy, duration and focal size stated; temperature and density measured at several probe energies and extrapolated to zero, or shown not to change; an estimate of heating and ponderomotive effects for the actual conditions; probe power below the self-focusing threshold; any correction for heating described and its size given.

**Benchmark.** [1], [2], [5], [6]

## 8. Scattering volume, timing and alignment

**Question.** What are the size of the scattering volume and the duration of the probe pulse and detector gate, how do they compare with the gradient lengths and the time scales of the plasma, and was the overlap between the laser and the collection optics checked during the measurements?

**Why it matters.** A measurement averages over the scattering volume and the gate; gradients within the volume broaden plasma-wave features and mix conditions, and where the probe crosses a small structure the signal is integrated along the beam. The density depends on the overlap between the laser and the imaged collection volume, so a laser that moves between calibration and measurement, or from shot to shot, changes the amplitude and shape of density profiles.

**Resolved by.** Scattering volume dimensions, pulse length and gate stated and compared with the gradient scale lengths and evolution times of the plasma; the effect of gradients on the fitted features estimated; any integration along the beam stated and its assumptions given; laser position monitored, alignment scanned and calibration done at the operating position, with residual position fluctuations included in the uncertainty.

**Benchmark.** [1], [4], [5], [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | S. S. Harilal, M. C. Phillips, D. H. Froula, K. K. Anoop, R. C. Issac and F. N. Beg, Optical diagnostics of laser-produced plasmas, Rev. Mod. Phys. 94, 035002 (2022); read as arXiv:2201.08783 | doi:10.1103/RevModPhys.94.035002 | full text | Sec. IV.4: the scattering parameter sets the regime, with uncorrelated-electron scattering for alpha well below one and collective features near alpha of one; the dynamic structure factor is written for a collisionless plasma; the scattering volume is an aperture imaged into the plasma. Sec. IV.4.2: spectra assume Maxwellian distributions; ion-acoustic peak positions give the product of charge state and electron temperature when that is well above the ion temperature; peak shape gives ion temperature in the mildly collective regime, or a small admixture of a higher-Z species adds modes that give it; density gradients in the volume broaden the plasma-wave peaks. Sec. IV.4.1: the scattered fraction is about 10^-12 of the probe power; ponderomotive self-focusing sets a critical probe power |
| 2 | E. A. D. Carbone and S. Nijdam, Thomson scattering on non-equilibrium low density plasmas: principles, practice and challenges, Plasma Phys. Control. Fusion 57, 014026 (2015) | doi:10.1088/0741-3335/57/1/014026 | abstract | Abstract: stray laser light and plasma emission are the main limits on detection, and Raman scattering from molecules lowers it further; a triple grating spectrometer separates Thomson and Raman signals from Rayleigh and stray light; that the measurement does not disturb the plasma must be verified; molecular plasmas need rotational Raman scattering accounted for |
| 3 | S. Ghazaryan, M. Kaloyan, W. Gekelman, Z. Lucky, S. Vincena, S. K. P. Tripathi, P. Pribyl and C. Niemann, Thomson scattering on the large plasma device, Rev. Sci. Instrum. 93, 083514 (2022); read as arXiv:2204.12616 | doi:10.1063/5.0099172 | full text | Spectrometer and notch description: without the notch, stray light exceeds the Thomson signal by over three orders of magnitude; its photon noise cannot be subtracted. Calibration section: Raman calibration in nitrogen at a pressure chosen so the Raman signal resembles the Thomson signal, limiting detector non-linearity; leakage of Rayleigh light past the notch; a second calibration agreeing within 10%. Instrument function measured with laser light, Gaussian core with Lorentzian wings; background images subtracted |
| 4 | M. Kaloyan, S. Ghazaryan, C. G. Constantin, R. S. Dorst, P. V. Heuer, J. J. Pilgram, D. B. Schaeffer and C. Niemann, Raster Thomson scattering in large-scale laser plasmas produced at high repetition rate, Rev. Sci. Instrum. 92, 093102 (2021); read as arXiv:2105.12666 | doi:10.1063/5.0059244 | full text | Secs. II to IV: Rayleigh light shares the laser wavelength with stray light and needs extra measurements, so calibration uses Raman lines outside the notch; the notch blocks the centre including the ion feature; the model is convolved with the measured instrument function; scattering volume set by beam and fibre image, gate matched to the probe pulse; Raman-calibrated density agrees with the collective fit within 10% |
| 5 | J. Bak, G. Urdaneta, S. Pokharel, R. B. Miles and A. Tropina, Two-dimensional high resolution electron properties of femtosecond laser-induced plasma filament in atmospheric pressure argon, Sci. Rep. 14, 3703 (2024) | doi:10.1038/s41598-024-52868-w | full text | Methods and Results: probe heating by inverse bremsstrahlung, with electron-neutral absorption comparable to electron-ion in weakly ionised gas; temperature measured at four probe energies and extrapolated to zero; density rising with probe energy; heating correction of roughly a quarter to a third of the measured temperature. Stray and Rayleigh light rejected by a Bragg-grating notch; alpha near one used for collective fitting; Maxwellian assumption justified by collision times; signal integrated along the probe path |
| 6 | M. N. Shneider, Ponderomotive perturbations of low density low-temperature plasma under laser Thomson scattering diagnostics, Phys. Plasmas 24, 100701 (2017); read as arXiv:1707.07224 | doi:10.1063/1.4998137 | abstract | Abstract: the ponderomotive force of the probe perturbs a low-density plasma in the interaction region, and the perturbation can lead to large errors in Thomson-scattering electron densities |
| 7 | J. Zheng and C. X. Yu, Thomson scattering from high-temperature high-density plasmas revisited, Plasma Phys. Control. Fusion 51, 095009 (2009); read as arXiv:0901.0346 | doi:10.1088/0741-3335/51/9/095009 | full text | Abstract and Sec. III: the first-order correction in electron velocity over light speed is significant for electron plasma wave spectra and negligible for ion-acoustic ones; without it the electron plasma wave peak intensity is overestimated, and the damping may be too, giving a higher inferred electron temperature. Sec. IV: dielectric correction matters at higher density |
| 8 | E. Parke, V. V. Mirnov and D. J. Den Hartog, A polarization-based Thomson scattering technique for burning plasmas, J. Instrum. 9, C02030 (2014); read as arXiv:1309.4858 | doi:10.1088/1748-0221/9/02/C02030 | full text | Sec. 1: polychromator spectral sensitivity is crucial to the optimal temperature range, and broad high-temperature spectra need many spectral channels. Sec. 2: at fusion temperatures the incoherent spectrum includes a blue shift and a temperature-dependent depolarisation. Sec. 4: the broad spectra exceed the uniform response of detectors and polarisation optics |
| 9 | B. C. Foo, D. B. Schaeffer and P. V. Heuer, Recovering non-Maxwellian particle velocity distribution functions from collective Thomson-scattered spectra, AIP Adv. 13, 115328 (2023); read as arXiv:2308.02488 | doi:10.1063/5.0169393 | full text | Introduction and results: most analyses assume Maxwellian distributions, and a Maxwellian fit to a super-Gaussian electron distribution greatly overestimates temperature; a wrong electron model contaminates ion fits; different ion distributions give similar spectra; joint posteriors and tests on synthetic spectra used to check fits |
| 10 | P. Nelde, G. Fuchert, E. Pasch, M. N. A. Beurskens, S. A. Bozhenkov, K. J. Brunner, U. Höfel, S. Kwak, J. Meineke, E. R. Scott, R. C. Wolf and the W7-X team, Quantification of systematic errors in the electron density and temperature measured with Thomson scattering at W7-X, J. Instrum. 18, P09019 (2023); read as arXiv:2111.03562 | doi:10.1088/1748-0221/18/09/P09019 | full text | Sec. 2: relative calibration of filter channels with a supercontinuum source, about 5% channel deviations tested for their effect on profiles; Raman-calibrated reference channel. Sec. 3: shifts of the laser from its calibrated position change both the amplitude and the shape of density profiles; beam position monitoring, alignment scans and position-resolved calibration recommended |
