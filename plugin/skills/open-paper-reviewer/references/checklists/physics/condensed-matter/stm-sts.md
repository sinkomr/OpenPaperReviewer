---
id: T-STM-STS
name: Scanning tunnelling microscopy and spectroscopy
type: technique
field: physics/condensed-matter
applies_when: the paper shows scanning tunnelling microscopy images, tunnelling spectra or conductance maps, or bases a claim about surface structure, local density of states, energy gaps or quasiparticle interference on them
version: "0.1"
---

# Scanning tunnelling microscopy and spectroscopy

## 1. Measured signal or inferred quantity

**Question.** Does the paper state what was recorded (constant-current height, current or differential conductance) and justify reading it as surface geometry or as the local density of states of the sample?

**Why it matters.** A constant-current image follows a contour of constant energy-integrated density of states, so where the electronic structure varies across the surface the image mixes electronic and geometric contrast and depends on the bias. The differential conductance is proportional to the sample density of states only if the tip density of states is featureless and the tunnelling matrix element does not depend on energy, which are approximations.

**Resolved by.** Structural assignments rest on images at more than one bias, including a bias away from the energy range of the spatially varying states. Spectroscopic assignments state the assumptions made, and compare with a calculated or independently measured density of states where the claim depends on it.

**Benchmark.** [1], [2]

## 2. Tip and junction condition

**Question.** Does the paper show that the reported spectra and images do not depend on the particular tip or junction, by describing tip preparation, repeating key measurements with different tips and checking that spectra do not change with tip–sample distance?

**Why it matters.** The tunnelling current is a convolution of the tip and sample densities of states, so structure in the tip states appears in the data. A contaminated junction gives smeared spectral features, a background that rises with energy and apparent spatial variation that is not a property of the sample.

**Resolved by.** The tip material and its conditioning are described, key spectra and maps are reproduced with more than one tip, and spectra normalised to the setpoint coincide over a range of junction resistances. A tunnelling barrier height (apparent work function) of reasonable size is reported as a check of vacuum tunnelling.

**Benchmark.** [1], [4]

## 3. Surface and bulk

**Question.** Is the measured surface identified (preparation, termination, reconstruction, cleanliness), and where the paper draws conclusions about the bulk, does it give evidence that the surface electronic structure represents the bulk?

**Why it matters.** The measurement probes the outermost layer. Even a clean, atomically flat surface may not have the carrier concentration of the bulk and may be reconstructed, structurally or electronically, and contamination of the top layer hides intrinsic properties.

**Resolved by.** The paper states how the surface was prepared, identifies the termination from atomic-resolution images or other surface probes, and connects the surface spectra to bulk behaviour, for example through a spectral feature that follows a bulk transition or agrees with a bulk-sensitive measurement.

**Benchmark.** [1], [2]

## 4. Setpoint effects

**Question.** For every spectrum and conductance map, does the paper give the acquisition mode and the stabilisation bias and current, and show that the features it interprets do not change when these are changed?

**Why it matters.** When the feedback loop sets the tip height at each pixel, the height depends on the density of states integrated up to the stabilisation bias, and this spatial variation is imprinted on the measured conductance. In Fourier-transformed maps this adds features, non-dispersing for spectroscopic grids and dispersing for constant-current maps, that can resemble a property of the sample.

**Resolved by.** The mode and setpoint are reported for each dataset. The interpreted features are shown to persist for different stabilisation biases, in constant-height data or in ratios of conductance at opposite bias, or the stabilisation bias lies outside the energy range of the states under study.

**Benchmark.** [2], [3]

## 5. Energy resolution

**Question.** Are the measurement temperature and the bias modulation amplitude stated, and are the spectral features the paper interprets, such as gaps, peak widths and splittings, resolved at the resulting energy resolution?

**Why it matters.** Spectra are thermally broadened by a few times the thermal energy, counting both tip and sample, and further by the lock-in modulation. Broadening smears sharp features and shifts apparent peak positions.

**Resolved by.** The paper states the temperature and modulation amplitude, keeps the modulation small compared with the features of interest, and includes thermal and instrumental broadening in any fit or comparison with theory.

**Benchmark.** [1], [2]

## 6. Voltage drop in the sample

**Question.** For semiconductors and other samples that do not fully screen the electric field of the tip, does the paper account for the part of the bias that drops inside the sample (tip-induced band bending) before converting voltages to energies, and is the measured current range wide enough to define band edges?

**Why it matters.** The field of the tip bends the bands beneath it, so the voltage at which a feature appears is not its energy relative to the Fermi level, and gaps read directly from the voltage axis are shifted. Band onsets and weak in-gap states are not defined when the current range covers too few orders of magnitude.

**Resolved by.** The paper estimates the band bending, for example by electrostatic modelling with tip radius, separation and contact potential, or from spectral features of known energy. Spectra span several orders of magnitude in current, for example by varying the tip–sample separation with the normalisation stated, and gaps are quoted with an uncertainty.

**Benchmark.** [4]

## 7. Extracting gaps and energies

**Question.** Does the paper state how gap values and other energies were extracted from the spectra (peak positions, onset criteria or a model fit with its broadening terms), show the quality of any fit, and give an uncertainty and the spread over positions?

**Why it matters.** Different procedures give different values from the same spectrum: a fitted gap changes with the broadening parameter, fits can fail to describe the measured line shape, and peak positions shift with thermal broadening. For states that are not localised at the surface, reading onset voltages is not sufficient and a line-shape analysis is needed.

**Resolved by.** The procedure and any normalisation are defined, and fits are shown over the data with all parameters. The result is compared between at least two procedures or shown to be insensitive to the choices, and the number of spectra, where they were taken and the spread of the extracted values are reported.

**Benchmark.** [2], [4]

## 8. Calibration, drift and processing

**Question.** Are the scanner calibration and all processing steps stated (background or line subtraction, drift correction, smoothing, masking, filtering, symmetrisation, averaging), and are the features the paper interprets visible before these steps?

**Why it matters.** Thermal drift and piezo hysteresis and creep distort images, and with them the lengths, angles and wavevectors measured. Processing can add or remove structure: a line-by-line subtraction can introduce artefacts in a Fourier transform, and angular averaging is justified only where the signal is isotropic.

**Resolved by.** Lengths and wavevectors are calibrated against a known lattice or a traceable standard, and the drift or distortion correction is described. Raw images or maps are provided next to processed ones, each processing step is listed with its parameters, and the conclusion is shown not to depend on them.

**Benchmark.** [3], [5], [6]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | Ø. Fischer et al., Scanning tunneling spectroscopy of high-temperature superconductors, Rev. Mod. Phys. 79, 353 (2007); read as preprint arXiv:cond-mat/0610672 | doi:10.1103/RevModPhys.79.353 |
| 2 | J. E. Hoffman, Spectroscopic scanning tunneling microscopy insights into Fe-based superconductors, Rep. Prog. Phys. 74, 124513 (2011); read as preprint arXiv:1201.1380 | doi:10.1088/0034-4885/74/12/124513 |
| 3 | A. J. Macdonald et al., Dispersing artifacts in FT-STS: a comparison of set point effects across acquisition modes, Nanotechnology 27, 414004 (2016); read as preprint arXiv:1606.07402 | doi:10.1088/0957-4484/27/41/414004 |
| 4 | R. M. Feenstra, A prospective: Quantitative scanning tunneling spectroscopy of semiconductor surfaces, Surf. Sci. 603, 2841 (2009); read as the author's preprint, www.cmu.edu/physics/stm/publ/86 | doi:10.1016/j.susc.2009.08.002 |
| 5 | M. P. Yothers et al., Real-space post-processing correction of thermal drift and piezoelectric actuator nonlinearities in scanning tunneling microscope images, Rev. Sci. Instrum. 88, 013708 (2017); abstract read at arXiv:1611.00243 | doi:10.1063/1.4974271 |
| 6 | ISO 11952:2019, Surface chemical analysis — Scanning-probe microscopy — Determination of geometric quantities using SPM: Calibration of measuring systems, edition 2 (International Organization for Standardization, 2019) | https://www.iso.org/standard/67552.html |
