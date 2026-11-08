---
id: T-LASER-PLASMA-ACCELERATION
name: Laser-plasma acceleration
type: technique
field: physics/plasma
applies_when: the paper reports electrons accelerated by a laser- or beam-driven plasma wakefield, or ions accelerated by an intense laser, and bases a claim about energy, energy spread, charge, divergence, emittance or stability on spectrometer, scintillator, image plate or track detector data
version: "0.1"
---

# Laser-plasma acceleration

## 1. Spectrometer energy scale and resolution

**Question.** How was the energy scale of the magnetic spectrometer obtained (measured field map or model, particle tracking, entrance angle assumed), what is its energy resolution at the quoted energies, and is a quoted energy spread larger than that resolution?

**Why it matters.** A dipole spectrometer maps position on a screen to energy only for a known field and a known entrance angle. Field models that misrepresent the fringe field can shift the energy scale by tens of percent at low energy, and a beam that enters at an angle that changes from shot to shot is assigned the wrong energy unless the angle is measured. The finite resolution of the spectrometer sets a floor, and a measured spread close to that floor is an upper limit, not a value.

**Resolved by.** The field measured, for example with a Hall probe, and used in the tracking; the entrance angle measured on each shot, for example with a second screen or a screen before the magnet, or limited by an aperture, with its effect on the energy estimated; the resolution given as a function of energy, including divergence; energy spreads near the resolution reported as upper limits.

**Benchmark.** [1], [2], [3]

## 2. Charge calibration of screens and image plates

**Question.** How was the signal on the scintillating screen or image plate converted to charge or particle number: which absolute calibration, for which screen or plate type and particle, how was it transferred to the imaging system used, and were the charge densities within the linear range?

**Why it matters.** Published absolute calibrations of the same screen types differ by about a factor of two, scintillators saturate at high charge density and lose efficiency after large accumulated doses, and the collection efficiency of the camera and optics enters the result directly. Image plate signal fades with the time between exposure and scanning, and the response per particle depends on the particle type and energy, so a calibration for one species or scanner does not carry over to another.

**Resolved by.** The calibration source and screen or plate type named, with its stated uncertainty; the transfer to the experiment made with a reference light source or a cross-calibration on the same shots; peak charge densities shown to be below the onset of saturation; for image plates, the scan delay stated and corrected, and a response function for the particle, energy range and scanner used; for current transformers or Faraday cups, electromagnetic pickup, background radiation and baseline offsets excluded.

**Benchmark.** [4], [5], [6], [13], [14]

## 3. Divergence and emittance

**Question.** How were divergence and emittance measured (screen before the magnet, pepper-pot mask, quadrupole scan, energy-resolved focusing), is the emittance stated as projected or slice and as normalised with or without the energy spread, and is the value above the resolution of the method?

**Why it matters.** Beams from plasma accelerators have percent-level energy spread, which makes the measured emittance depend on how the beam was transported and focused: chromatic effects in quadrupoles enlarge the projected emittance, and a quadrupole scan analysed without them can be biased. The usual conversion from geometric to normalised emittance holds only for small energy spread, and projected emittance exceeds slice emittance when beam properties vary along the bunch. Pepper-pot and screen-based methods have a resolution floor that very small source emittances can reach.

**Resolved by.** The method, the distance from the source and any optics between source and measurement stated; the energy spread at the measurement point given and included in the analysis; emittance stated as projected or slice, with the definition (rms or fitted) and the fraction of charge included; the resolution of the method estimated, and values at that level reported as upper limits; divergence given with its definition and energy dependence; a check for coherent emission where optical transition radiation screens image short bunches.

**Benchmark.** [7], [8], [9], [14]

## 4. Ion species and detector response

**Question.** For ion spectra, how were species and charge states separated, what does each detector respond to, and how were saturation, the energy thresholds of the detector and background from X-rays and electrons handled?

**Why it matters.** A magnetic spectrometer selects by energy only and is adequate only when one species dominates, while a Thomson parabola separates ions by charge-to-mass ratio. RCF stacks give a coarse spectrum through the energy threshold of each layer, CR-39 tracks overlap and saturate at high flux or long etching, and spectrometers sample only the part of the beam that passes their entrance pinhole or slit. Image plates respond to X-rays and scattered particles near the ion trace as well as to the ions.

**Resolved by.** The detector for each species named, with its energy thresholds and calibration; traces of different species or charge states shown to be separated where the claim needs it; CR-39 track densities kept below overlap, or etching checked; background measured beside the trace and subtracted; the solid angle of the spectrometer stated, and any extrapolation to the whole beam justified with an angularly resolved measurement.

**Benchmark.** [6], [10]

## 5. Definition of the quoted energy

**Question.** Is the headline energy a peak, a mean or a maximum (cut-off) energy, how is it defined against the detector noise level, and how many particles or how much charge lie at that energy?

**Why it matters.** For broad, exponential-like spectra the maximum energy depends on the detection method, its sensitivity and the rule used to separate signal from background, so a higher cut-off can reflect a more sensitive detector rather than a better accelerator. A maximum energy or a narrow peak carrying few particles says little about the beam that applications can use.

**Resolved by.** The full absolutely calibrated spectrum shown, in particles or charge per unit energy; the rule defining any cut-off stated, together with the noise level and the number of particles at the cut-off; the charge within any quasi-monoenergetic peak given with the peak width; comparisons with earlier work made on calibrated spectra or conversion efficiency, not on cut-off energies alone; where a gradient is quoted, the energy gain divided by a stated length that includes any coupling or staging optics, and the driver-to-beam efficiency estimated.

**Benchmark.** [11], [15]

## 6. Shot-to-shot variation and which shots are shown

**Question.** Are the energy, charge, divergence and pointing given as distributions over a run of shots under the stated conditions, what fraction of those shots shows the claimed feature, and where does any single shot shown sit within those distributions?

**Why it matters.** Shot-to-shot variation in plasma accelerators is large compared with conventional accelerators, reported as typically a few percent in energy, tens of percent in charge and around a milliradian in pointing, and it arises largely from uncontrolled injection by self-trapping and from small irregularities in the drive laser. A single shot from the best end of the distribution can therefore look very different from the typical beam.

**Resolved by.** The number of shots and the fraction showing the claimed feature stated; mean and spread of energy, charge, divergence and pointing over a run of consecutive shots; spectra shown as averages with their spread alongside any single shot; drive laser parameters recorded on each shot and correlated with the beam parameters.

**Benchmark.** [3], [12]

## 7. Drive laser and target conditions

**Question.** Does the paper give the drive laser parameters on target (energy, pulse duration, focal spot and the fraction of energy in it, temporal contrast and prepulse level) and the target parameters (gas density profile, or foil material, thickness and surface condition), with how each was measured?

**Why it matters.** The energy and number of accelerated particles depend strongly on these parameters. In ion acceleration, prepulse level and duration change the target before the main pulse arrives and strongly influence the maximum proton energy, and experiments that look similar can differ because these conditions are hard to control. In wakefield acceleration, small drifts in laser parameters drive drifts in electron energy.

**Resolved by.** Peak intensity derived from measured energy, duration and focal spot, not from nominal values; contrast measured over the relevant time window and stated; target density or thickness measured, with its uncertainty and, for gas targets, its profile; these parameters reported for the shots shown and their variation over the run.

**Benchmark.** [10], [11], [12]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. V. Ambat et al., Assessment of errors in analytic modeling of permanent magnet electron spectrometers for laser-plasma accelerators, Rev. Sci. Instrum. 96 (2025); read as the OSTI record 3012997 | doi:10.1063/5.0281827 |
| 2 | C. I. Hojbota et al., Accurate single-shot measurement technique for the spectral distribution of GeV electron beams from a laser wakefield accelerator, AIP Adv. 9, 085229 (2019); read as arXiv:1907.02239 | doi:10.1063/1.5117311 |
| 3 | S. M. Hooker, Developments in laser-driven plasma accelerators, Nat. Photon. 7, 775 (2013); read as arXiv:1406.5118 | doi:10.1038/nphoton.2013.234 |
| 4 | A. Buck et al., Absolute charge calibration of scintillating screens for relativistic electron detection, Rev. Sci. Instrum. 81, 033301 (2010) | doi:10.1063/1.3310275 |
| 5 | T. Kurz et al., Calibration and cross-laboratory implementation of scintillating screens for electron bunch charge determination, Rev. Sci. Instrum. 89, 093303 (2018) | doi:10.1063/1.5041755 |
| 6 | D. Doria et al., Calibration of BAS-TR image plate response to GeV gold ions, Rev. Sci. Instrum. 93, 033304 (2022); read as arXiv:2202.10385 | doi:10.1063/5.0079564 |
| 7 | C. A. Lindstrøm and M. Thévenet, Emittance preservation in advanced accelerators, J. Instrum. 17, P05016 (2022); read as arXiv:2201.08876 | doi:10.1088/1748-0221/17/05/P05016 |
| 8 | A. Mostacci et al., Chromatic effects in quadrupole scan emittance measurements, Phys. Rev. ST Accel. Beams 15, 082802 (2012) | doi:10.1103/PhysRevSTAB.15.082802 |
| 9 | G. G. Manahan et al., Characterization of laser-driven single and double electron bunches with a permanent magnet quadrupole triplet and pepper-pot mask, New J. Phys. 16, 103006 (2014) | doi:10.1088/1367-2630/16/10/103006 |
| 10 | A. Macchi et al., Ion acceleration by superintense laser-plasma interaction, Rev. Mod. Phys. 85, 751 (2013); read as arXiv:1302.1775 | doi:10.1103/RevModPhys.85.751 |
| 11 | A. Macchi, A review of laser-plasma ion acceleration, preprint arXiv:1712.06443 (2017) | doi:10.48550/arXiv.1712.06443 |
| 12 | A. R. Maier et al., Decoding sources of energy variability in a laser-plasma accelerator, Phys. Rev. X 10, 031039 (2020) | doi:10.1103/PhysRevX.10.031039 |
| 13 | S. Bohlen et al., Noninvasive cavity-based charge diagnostic for plasma accelerators, J. Phys.: Conf. Ser. 3124, 012020 (2025); read as arXiv:2403.07135 | doi:10.1088/1742-6596/3124/1/012020 |
| 14 | P. Forck, Beam instrumentation and diagnostics, contribution to the CAS–CERN Accelerator School General Introductory Course on Accelerator Physics and Technologies, 2019 and beyond; arXiv:2009.10411 (2020) | doi:10.48550/arXiv.2009.10411 |
| 15 | R. Assmann et al., High-gradient plasma and laser accelerators, in European Strategy for Particle Physics – Accelerator R&D Roadmap, N. Mounet (ed.), CERN Yellow Reports: Monographs CERN-2022-001, p. 91 (2022) | doi:10.23731/CYRM-2022-001.91 |
