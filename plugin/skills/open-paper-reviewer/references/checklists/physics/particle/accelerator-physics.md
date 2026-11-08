---
id: T-ACCELERATOR-PHYSICS
name: Accelerator and beam physics
type: technique
field: physics/particle
applies_when: the paper reports emittance, energy spread, bunch charge or beam size measured on a radio-frequency, dielectric or other non-plasma accelerator, a luminosity computed from beam parameters, calibration of beam instrumentation, or the gradient or energy gain of a new non-plasma acceleration scheme
version: "0.1"
---

# Accelerator and beam physics

## 1. Definition of the emittance

**Question.** Which emittance is quoted: an rms value or one enclosing a stated fraction of the beam, geometric or normalised, trace-space (position and angle) or phase-space (position and momentum), projected or slice; and, where it is normalised, how was the energy spread taken into account?

**Why it matters.** Optics-based measurements describe the beam by an ellipse, which applies to rms values of a general distribution but not to widths such as the full width at half maximum, and conventions for the enclosed fraction differ between communities. Multiplying a geometric emittance by the mean relativistic factor gives the normalised emittance only when the energy spread is small; with a large energy spread and divergence, the normalised emittance changes in a drift and differs from the trace-space value, so the two are not interchangeable.

**Resolved by.** The definition and the formula used stated; rms values computed from the measured distribution, with any cut or core fraction stated; the energy spread at the measurement point given and used in the conversion to normalised emittance, or shown to be small enough that the simple scaling holds; projected and slice values kept distinct.

**Benchmark.** [1], [2], [3]

## 2. Emittance measurement method and its assumptions

**Question.** For the method used (quadrupole or solenoid scan, multi-screen, slit or pepper-pot mask, single-shot scan using the energy spread), does the paper state the transport model and the scan range, and show that chromatic effects, space charge and sampling of phase space do not bias the result?

**Why it matters.** Envelope methods fit beam sizes to a linear transport model. With a percent-level energy spread and a large beam at the first quadrupole, chromatic effects bias the fitted emittance, usually upward, and a scan that undersamples the region of the waist can shift the result even without energy spread. Space charge must be included in the model or shown to be negligible. Masks need beamlets much larger than the holes and enough holes across the beam.

**Resolved by.** The optics model, quadrupole strengths and number of points, with the measured beam sizes and fit shown; the scan spanning and sampling the waist; an estimate of the chromatic and space-charge contributions for the actual energy spread, charge and beam size at the first magnet; for masks, slit or hole size, spacing and drift length with the resulting resolution; results reported as limits where the method cannot resolve the emittance.

**Benchmark.** [2], [3], [4]

## 3. Profile and position monitors

**Question.** What spatial resolution, linearity and dynamic range do the screens, wire scanners or beam position monitors (BPMs) have under the conditions of the measurement, and how were they calibrated?

**Why it matters.** Beam sizes near the resolution of the monitor are overestimated unless the resolution is removed. Scintillating screens can saturate at high charge density, which distorts the recorded profile. For short, intense electron bunches, coherent optical transition radiation (OTR) can produce images that do not represent the transverse distribution. The position sensitivity of a BPM can depend on the beam position and on frequency, giving non-linear readings at large displacement.

**Resolved by.** The point-spread or resolution of each imaging system measured and stated, and subtracted in quadrature where significant; evidence that the screen response is linear at the charge density used, or a saturation correction; a check for coherent emission where OTR screens are used with short bunches; the linear range of each BPM stated, with displacements kept within it or corrected with a position map.

**Benchmark.** [3], [5]

## 4. Bunch charge and beam intensity

**Question.** How was the bunch charge or beam intensity measured, and how were electromagnetic pickup, background radiation, baseline offsets and particles outside the energy range of interest excluded?

**Why it matters.** Integrating current transformers near plasma accelerators pick up electromagnetic pulses and have overestimated the charge by up to an order of magnitude. Scintillating screens need absolute calibration, respond more strongly to low-energy electrons than to energetic ones, record background radiation, and saturate at high charge density. In storage rings, slow baseline drifts of the current transformers can dominate the uncertainty on bunch intensity.

**Resolved by.** Shielding against electromagnetic pulses and background described, or the charge cross-checked against a second, independently calibrated detector; the screen response checked for the energy range and charge density of the beam; the charge quoted for a stated energy range, such as the main peak, separately from the total; baselines measured without beam and their drift included in the uncertainty.

**Benchmark.** [5], [6], [7]

## 5. Energy and energy spread

**Question.** How was the spectrometer calibrated (field map, geometry, trajectory model), what is its energy resolution for the beam's size and divergence, and how is the quoted energy spread defined?

**Why it matters.** The measured width in a dipole spectrometer includes the betatron beam size at the detector as well as the dispersion, which sets a resolution limit. Where the beam diverges or points off axis, particles of one energy land at different places unless the detector lies where trajectories of that energy converge, so divergence and pointing can dominate the resolution and shift the energy reading. An energy spread quoted as the width of a peak, without the charge in that peak and in the low-energy tail, does not describe the whole beam.

**Resolved by.** The magnetic field map, spectrometer geometry and trajectory calculation stated; the resolution computed from the beam size, divergence and dispersion and compared with the quoted spread; pointing measured or the beam collimated, with the effect of pointing on the energy reading estimated; the definition of the energy spread given (rms or full width at half maximum, of which part of the spectrum) together with the charge it contains and the full spectrum shown.

**Benchmark.** [2], [8], [9]

## 6. Luminosity from beam parameters

**Question.** When a luminosity is computed or projected from beam parameters, does the paper list the bunch populations, number of bunches, collision frequency and beam sizes at the interaction point, state whether the beam sizes were measured or inferred from emittance and optics, and include the geometric and dynamic factors that change the overlap?

**Why it matters.** The basic formula assumes Gaussian bunches colliding head on. A crossing angle combined with long bunches, and the hourglass effect when the bunch length is comparable to the focusing function at the collision point, reduce the luminosity, while the mutual focusing of the beams can increase it. The result scales directly with the product of the bunch populations, so a calibration error in the current measurement passes straight into the luminosity, and beam sizes inferred from optics carry the errors of the optics model.

**Resolved by.** A table of all parameters entering the formula, with their source and uncertainty; the reduction factors for crossing angle and bunch length and any beam-beam enhancement computed and stated; the beam-size inputs measured or their inference described; for a projected luminosity, a check that the assumed intensities and beam sizes respect the beam-beam limits; peak and integrated luminosity distinguished; where available, comparison with a luminosity measured by the experiments.

**Benchmark.** [7], [10]

## 7. Gradient, energy gain and beam quality for new acceleration schemes

**Question.** For a new acceleration scheme, how is the gradient defined (peak field, average over the active length, or including the length needed for coupling and staging), and are the energy gain, charge, energy spread, emittance, efficiency and stability reported for the same shots and the same beam?

**Why it matters.** A peak or axial field can be well above the average gradient the beam actually experiences, and an accelerator built from many stages must also preserve beam quality between them and include the length of the optics that couple them. Parameters reached separately in different shots or set-ups do not show that they can be reached together.

**Resolved by.** The gradient defined and computed from the measured energy gain and stated length; energy gain, charge, energy spread and emittance reported for the same data set; the energy transfer efficiency from driver to beam estimated; the shot-to-shot spread of each parameter given alongside any single shot shown.

**Benchmark.** [2], [10], [11]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | K. Floettmann, Some basic features of the beam emittance, Phys. Rev. ST Accel. Beams 6, 034202 (2003) | doi:10.1103/PhysRevSTAB.6.034202 |
| 2 | B. Marchetti, Particle beam diagnostics, lecture notes, arXiv:2008.05896 (2020) | doi:10.48550/arXiv.2008.05896 |
| 3 | G. Kube, Transverse emittance and emittance measurements, contribution to the CAS–CERN Accelerator School on Beam Instrumentation, Split, 2025; arXiv:2606.23013 (2026) | doi:10.48550/arXiv.2606.23013 |
| 4 | A. Mostacci et al., Chromatic effects in quadrupole scan emittance measurements, Phys. Rev. ST Accel. Beams 15, 082802 (2012) | doi:10.1103/PhysRevSTAB.15.082802 |
| 5 | P. Forck, Beam instrumentation and diagnostics, contribution to the CAS–CERN Accelerator School General Introductory Course on Accelerator Physics and Technologies, 2019 and beyond; arXiv:2009.10411 (2020) | doi:10.48550/arXiv.2009.10411 |
| 6 | S. Bohlen et al., Noninvasive cavity-based charge diagnostic for plasma accelerators, J. Phys.: Conf. Ser. 3124, 012020 (2025); read as arXiv:2403.07135 | doi:10.1088/1742-6596/3124/1/012020 |
| 7 | The ATLAS Collaboration (G. Aad et al.), Luminosity determination in pp collisions at √s = 7 TeV using the ATLAS detector at the LHC, Eur. Phys. J. C 71, 1630 (2011); read as arXiv:1101.2185 | doi:10.1140/epjc/s10052-011-1630-5 |
| 8 | R. Faccini et al., Multi-GeV electron spectrometer, Nucl. Instrum. Methods Phys. Res. A 623, 704 (2010); read as arXiv:1002.3497 | doi:10.1016/j.nima.2010.02.095 |
| 9 | J. Bauche et al., A magnetic spectrometer to measure electron bunches accelerated at AWAKE, Nucl. Instrum. Methods Phys. Res. A 940, 103 (2019); read as arXiv:1902.05752 | doi:10.1016/j.nima.2019.05.067 |
| 10 | V. Shiltsev and F. Zimmermann, Accelerator physics of colliders, revised July 2023, in S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110, 030001 (2024) | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-accel-phys-colliders.pdf |
| 11 | R. Assmann et al., High-gradient plasma and laser accelerators, in European Strategy for Particle Physics – Accelerator R&D Roadmap, N. Mounet (ed.), CERN Yellow Reports: Monographs CERN-2022-001, p. 91 (2022) | doi:10.23731/CYRM-2022-001.91 |
