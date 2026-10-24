---
id: T-ACCELERATOR-PHYSICS
name: Accelerator and beam physics
type: technique
field: physics/particle
applies_when: the paper reports measured beam emittance, energy spread, bunch charge or beam size, a luminosity computed from beam parameters, calibration of beam instrumentation, or the energy gain, gradient or beam quality of a new acceleration scheme such as plasma or dielectric acceleration
version: "0.1"
---

# Accelerator and beam physics

Beam measurements are used to claim the transverse emittance (the area a beam occupies in position and angle, a measure of how well it can be focused), the energy and energy spread, the bunch charge, and the luminosity (the collision rate per unit cross section) of a collider. New acceleration schemes, such as laser- or beam-driven plasma wakefield acceleration (LWFA, PWFA) and dielectric laser acceleration (DLA), are claimed through the energy gain, accelerating gradient and quality of the beams they produce. All of these rest on beam instruments and on models of how the beam is transported to them.

## 1. Definition of the emittance

**Question.** Which emittance is quoted: an rms value or one enclosing a stated fraction of the beam, geometric or normalised, trace-space (position and angle) or phase-space (position and momentum), projected or slice; and, where it is normalised, how was the energy spread taken into account?

**Why it matters.** Optics-based measurements describe the beam by an ellipse, which applies to rms values of a general distribution but not to widths such as the full width at half maximum, and conventions for the enclosed fraction differ between communities. Multiplying a geometric emittance by the mean relativistic factor gives the normalised emittance only when the energy spread is small; with a large energy spread and divergence, as in beams from plasma sources, the normalised emittance changes in a drift and differs from the trace-space value, so the two are not interchangeable.

**Resolved by.** The definition and the formula used stated; rms values computed from the measured distribution, with any cut or core fraction stated; the energy spread at the measurement point given and used in the conversion to normalised emittance, or shown to be small enough that the simple scaling holds; projected and slice values kept distinct.

**Benchmark.** [1], [2], [3]

## 2. Emittance measurement method and its assumptions

**Question.** For the method used (quadrupole or solenoid scan, multi-screen, slit or pepper-pot mask, single-shot scan using the energy spread), does the paper state the transport model and the scan range, and show that chromatic effects, space charge and sampling of phase space do not bias the result?

**Why it matters.** Envelope methods fit beam sizes to a linear transport model. With a percent-level energy spread and a large beam at the first quadrupole, chromatic effects bias the fitted emittance, usually upward, and a scan that undersamples the region of the waist can shift the result even without energy spread. Space charge must be included in the model or shown to be negligible. Masks need beamlets much larger than the holes and enough holes across the beam, and for strongly divergent beams such as those from plasma sources undersampling dominates the reconstruction.

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

**Why it matters.** A peak or axial field can be well above the average gradient the beam actually experiences, and an accelerator built from many stages must also preserve beam quality between them and include the length of the optics that couple them. Parameters reached separately in different shots or set-ups do not show that they can be reached together. Plasma-accelerated beams fluctuate more in energy and position from shot to shot than conventional beams, so a best shot does not describe typical performance.

**Resolved by.** The gradient defined and computed from the measured energy gain and stated length; energy gain, charge, energy spread and emittance reported for the same data set; the energy transfer efficiency from driver to beam estimated; the shot-to-shot spread of each parameter given alongside any single shot shown.

**Benchmark.** [2], [10], [11]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | K. Floettmann, Some basic features of the beam emittance, Phys. Rev. ST Accel. Beams 6, 034202 (2003) | doi:10.1103/PhysRevSTAB.6.034202 | full text | Sec. II: ellipse-based optics concepts apply only to rms values of irregular distributions, not to widths such as the FWHM. Secs. III and IV: trace-space and phase-space emittance differ when a correlated divergence meets a significant energy spread, and the normalised emittance is not constant in a drift unless the energy spread is small. Sec. VII: sources with large divergence and energy spread, such as plasma sources, are sensitive to this, and a measurement should check which emittance it determines |
| 2 | B. Marchetti, Particle beam diagnostics, lecture notes, arXiv:2008.05896 (2020) | doi:10.48550/arXiv.2008.05896 | full text | Sec. 2.1: normalised emittance is conserved only for small energy spread, which plasma beams usually violate. Sec. 2.2: plasma beams are less stable in energy and position than conventional beams, so single-shot measurements are preferred. Sec. 3.1.4: undersampling dominates trace-space reconstruction of plasma beams with masks. Sec. 3.2.1: space charge must be included or negligible in quadrupole scans, and a large energy spread dilutes the emittance through chromatic effects. Sec. 4.1: dipole spectrometer resolution set by the betatron beam size relative to the dispersion. Sec. 4.2.1: slice emittance measured with a transverse deflecting structure |
| 3 | G. Kube, Transverse emittance and emittance measurements, contribution to the CAS–CERN Accelerator School on Beam Instrumentation, Split, 2025; arXiv:2606.23013 (2026) | doi:10.48550/arXiv.2606.23013 | full text | Sec. 0.2: rms emittance from the beam matrix; electron beams quoted at one rms width while proton machines often use a boundary enclosing about 87% of a Gaussian beam; trace space versus canonical phase space; normalised emittance. Sec. 0.4.1: pepper-pot holes must be spaced finely enough to sample the beam and beamlets must be much larger than the holes. Sec. 0.4.2: very small beam sizes in quadrupole scans are affected by space-charge broadening and resolution effects. Sec. 0.4.4: slice emittance and why projected values can hide variation along the bunch |
| 4 | A. Mostacci, M. Bellaveglia, E. Chiadroni, A. Cianchi, M. Ferrario, D. Filippetto, G. Gatti and C. Ronsivalle, Chromatic effects in quadrupole scan emittance measurements, Phys. Rev. ST Accel. Beams 15, 082802 (2012) | doi:10.1103/PhysRevSTAB.15.082802 | full text | Sec. I: with large beam size, divergence and energy spread the measurement itself can change the emittance, typically giving an overestimate; wakefield-accelerated beams have percent-level or larger energy spread. Sec. IV B: the error grows with energy spread and with beam size at the quadrupole, and the region around the spot-size minimum must not be undersampled. Sec. VI C and Sec. VIII: undersampling of the gradient scan biases the result even without energy spread |
| 5 | P. Forck, Beam instrumentation and diagnostics, contribution to the CAS–CERN Accelerator School General Introductory Course on Accelerator Physics and Technologies, 2019 and beyond; arXiv:2009.10411 (2020) | doi:10.48550/arXiv.2009.10411 | full text | Sec. 2.2: offset drift of dc current transformers and its zero compensation without beam. Secs. 3.2 and 3.3: BPM position sensitivity depends on beam position and frequency, and button BPMs are non-linear at large displacement. Sec. 4.1: saturation of scintillating screens deforms the recorded profile. Sec. 4.2: coherent OTR from short, intense bunches gives images that do not represent the transverse distribution |
| 6 | S. Bohlen, O. Kononenko, J.-P. Schwinkendorf, F. Grüner, D. Lipka, M. Meisel, C. Palmer, T. Staufer, K. Põder and J. Osterhoff, Noninvasive cavity-based charge diagnostic for plasma accelerators, J. Phys.: Conf. Ser. 3124, 012020 (2025); read as arXiv:2403.07135 | doi:10.1088/1742-6596/3124/1/012020 | full text | Sec. 1: integrating current transformers have overestimated charge in plasma accelerators by up to an order of magnitude because of electromagnetic pulses, so calibrated screens or Faraday cups have been used instead. Sec. 3: electrons below a few MeV deposit more energy in a scintillating screen than energetic ones. Sec. 4.3: background radiation and low-energy electrons can raise screen readings, and calibration differences between diagnostics |
| 7 | The ATLAS Collaboration (G. Aad et al.), Luminosity determination in pp collisions at √s = 7 TeV using the ATLAS detector at the LHC, Eur. Phys. J. C 71, 1630 (2011); read as arXiv:1101.2185 | doi:10.1140/epjc/s10052-011-1630-5 | full text | Sec. 4.1: luminosity from beam parameters as the product of bunch populations and the beam overlap integral, assuming negligible transverse coupling. Sec. 4.5: an error in absolute bunch charge passes directly into the luminosity; slow baseline drifts of the dc current transformers dominate the bunch-charge uncertainty; emittance growth and beam-separation length scale add further uncertainty |
| 8 | R. Faccini et al., Multi-GeV electron spectrometer, Nucl. Instrum. Methods Phys. Res. A 623, 704 (2010); read as arXiv:1002.3497 | doi:10.1016/j.nima.2010.02.095 | full text | Sec. 1: the resolution of a spectrometer for laser-plasma electrons is dominated by the angular divergence of the beam at the source. Sec. 2.1: trajectories of a given momentum converge, whatever their initial angle, only on a locus of foci, where a detector is placed to reduce the angular error |
| 9 | J. Bauche et al., A magnetic spectrometer to measure electron bunches accelerated at AWAKE, Nucl. Instrum. Methods Phys. Res. A 940, 103 (2019); read as arXiv:1902.05752 | doi:10.1016/j.nima.2019.05.067 | full text | Sec. 2.1: position-to-energy conversion uses measured field maps, surveyed spectrometer geometry and particle tracking, with the field-map uncertainty as the main magnetic term. Secs. 2.2 to 3.1: the optical resolution of the screen imaging limits the energy resolution at the high-energy end. Secs. 3.1 and 3.2: calibration of the optical system and of the scintillator charge response |
| 10 | V. Shiltsev and F. Zimmermann, Accelerator physics of colliders, revised July 2023, in S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110, 030001 (2024) | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-accel-phys-colliders.pdf | full text | Sec. 31.1: luminosity formula for Gaussian bunches with a factor for crossing angle, bunch length and dynamic effects. Sec. 31.2.3: hourglass and crossing-angle (Piwinski angle) reduction factors; beam-beam parameter as a common limit. Sec. 31.5.2: pinch enhancement of luminosity, typically between 1 and 2, in linear colliders. Sec. 31.5.4: plasma acceleration needs staging and phase locking, and power efficiency is a critical issue |
| 11 | R. Assmann, E. Gschwendtner, K. Cassou, S. Corde, L. Corner, B. Cros, M. Ferrario, S. Hooker, R. Ischebeck, A. Latina, O. Lundh, P. Muggli, P. Nghiem, J. Osterhoff, T. Raubenheimer, A. Specka, J. Vieira and M. Wing, High-gradient plasma and laser accelerators, in European Strategy for Particle Physics – Accelerator R&D Roadmap, N. Mounet (ed.), CERN Yellow Reports: Monographs CERN-2022-001, p. 91 (2022) | doi:10.23731/CYRM-2022-001.91 | full text | Sec. 4.1: staging of multiple structures with all optical elements, including tolerances, length and cost scaling, remains to be demonstrated. Sec. 4.2: parameters achieved individually (gradient, energy gain, charge, energy spread, emittance) must now be achieved together and preserved from stage to stage. Sec. 4.5: an accelerator needs more than a demonstrated gradient and energy gain, namely sufficient efficiency and preserved energy spread and emittance; an example of an axial field of 1.8 GV/m with an average gradient of 0.85 GeV/m; energy spread, reproducibility, reliability and energy efficiency as figures of merit. Sec. 4.5.2: strong focusing between stages keeps the average gradient of a staged accelerator high |
