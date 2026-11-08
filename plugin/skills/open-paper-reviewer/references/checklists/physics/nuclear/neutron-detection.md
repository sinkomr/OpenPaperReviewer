---
id: T-NEUTRON-DETECTION
name: Neutron detection and spectroscopy
type: technique
field: physics/nuclear
applies_when: the paper counts neutrons or measures their spectrum with scintillators, gas counters, Bonner spheres, activation foils or time-of-flight, or bases a claim about a neutron yield, flux, emission rate, dose or cross section on such data; tokamak and inertial-fusion yields have their own card
version: "0.1"
---

# Neutron detection and spectroscopy

## 1. Discrimination against gamma rays

**Question.** How were gamma-ray events separated from neutron events (by pulse shape discrimination, pulse height or time of flight), how good is the separation at the lowest light output used, and how many gamma events are estimated to remain in the neutron sample at that threshold?

**Why it matters.** In organic scintillators the separation between neutron and gamma pulse shapes worsens as the light output falls, so near threshold a share of events is misidentified, and the neutron energy at which discrimination becomes adequate differs several-fold between scintillators. Counters for thermal neutrons can also respond to gamma rays in a strong gamma field, so their gamma sensitivity needs measurable criteria stated at a given exposure rate.

**Resolved by.** The discrimination parameter plotted against light output with the selection cut drawn; a figure of merit or misidentification fraction given as a function of energy, not only at high energy; the threshold set where the discrimination is adequate; for thermal-neutron counters, the intrinsic gamma efficiency and the gamma rejection measured with a gamma source at a stated exposure rate; the response to the photons that accompany the neutron source checked and corrected if needed.

**Benchmark.** [1], [2], [3]

## 2. Light-output scale and detection threshold

**Question.** How was the light-output scale of a scintillator calibrated (which gamma sources, how the Compton edge was located), which proton light-yield relation converts the threshold and the pulse heights into recoil energy, and was that relation measured with the same pulse integration length as the data?

**Why it matters.** The efficiency near threshold and any simulated response function depend on the threshold expressed as proton recoil energy, which requires the non-linear proton light-yield relation of the particular scintillator. Light-yield relations reported for the same scintillator disagree, largely because they were measured with different pulse integration lengths, and changing from a short to a long window can change the yield by up to about a fifth. The Compton edge in a measured spectrum is smeared by the resolution, so its position has to be found by simulation, and electron response is itself non-linear at low energy.

**Resolved by.** Calibration sources named and the edge located by fitting a simulated energy deposition to the measured distribution; the threshold stated in electron-equivalent energy and in proton or neutron energy; the light-yield relation and its origin stated, measured or chosen for the same scintillator and integration length; the uncertainty of the threshold carried into the efficiency.

**Benchmark.** [1], [4]

## 3. Absolute efficiency and fluence normalisation

**Question.** How was the detection efficiency, or the neutron fluence, determined as a function of energy: by simulation, with a reference source of known emission rate, or relative to a standard cross section, and was any simulated efficiency checked against a measurement?

**Why it matters.** Counts become a flux, a yield, a cross section or a dose only through the efficiency, which depends on neutron energy and is often taken from simulation. Reference fluences rest on cross sections and spectra that are standards only over stated energy ranges, and on source emission rates that need traceability to a primary standard and correction for emission that is rarely isotropic.

**Resolved by.** The efficiency curve shown with its uncertainty; the simulation code, geometry and light-yield input stated and the simulation checked against a reference measurement; normalisation to a standard reaction or reference spectrum, such as the spontaneous fission neutron spectrum of californium-252, used only within the energy range where it is a standard; for sources, a traceable emission rate and the angular emission rate; agreement between independent detectors or reactions where available.

**Benchmark.** [3], [5], [6], [7]

## 4. Time-of-flight energy scale and resolution

**Question.** For time-of-flight data, how were the flight path and the time reference determined, what is the energy resolution at the energies of the claimed features, and could neutrons from earlier pulses appear in the spectrum?

**Why it matters.** The neutron energy follows from the flight path and the flight time, so an error in either shifts the whole energy scale, and at moderated sources the effective flight path includes an energy-dependent moderation length. The resolution function is often non-Gaussian and asymmetric, which both broadens peaks and shifts their apparent position. When the pulse spacing is short, fast neutrons from one pulse overtake slow neutrons from earlier pulses, a frame overlap that mixes energies.

**Resolved by.** The flight path and how it was measured; the time reference and its uncertainty; the energy scale checked against well-known resonances or reactions; the resolution function stated, simulated or measured, at the energies of interest; the pulse spacing compared with the flight time of the slowest neutrons accepted, or frame overlap treated explicitly.

**Benchmark.** [6], [7]

## 5. Spectrum unfolding

**Question.** When a spectrum is unfolded from pulse-height distributions or from few-channel detectors such as Bonner spheres or activation foils, which response matrix, unfolding method and a priori spectrum were used, and how much does the result change when the a priori spectrum or the method is changed?

**Why it matters.** Unfolding is an ill-conditioned inverse problem, and when there are fewer measured channels than energy bins an unlimited number of spectra fit the data, so the result carries information from the a priori spectrum and the response functions. Methods agree when a good a priori spectrum is supplied but can perform poorly with a less accurate one, and the response functions themselves rest on simulations with light-yield input. Spectral shapes from unfolding and from time of flight can differ even when the integrated fluxes agree.

**Resolved by.** The origin of the response matrix and its validation; the method and a priori spectrum stated; results shown for more than one reasonable a priori spectrum or method; uncertainties propagated, for example by varying the inputs within their uncertainties; spectral features claimed only where they persist across these choices; a cross-check against an independent method, such as time of flight, where possible.

**Benchmark.** [4], [7], [8]

## 6. Room return and scattered neutrons

**Question.** What share of the counts comes from neutrons scattered from walls, floor, ceiling, air, supports and shielding, how was it measured, and how does it change over the source-detector distances used?

**Why it matters.** Scattered neutrons have a different energy spectrum from direct ones, so unless the detector response is flat in energy they change the reading by an amount that depends on the detector. In a room the scattered share grows with distance and can exceed the direct contribution at a metre or more, and air attenuation and in-scatter each change the fluence by a few per cent at one metre.

**Resolved by.** Shadow cone measurements at every distance used, with a cone large enough to shadow the detector completely; or another method recognised in ISO 8529-2, or a simulation checked against measurement; corrections for air attenuation and for scatter from supports; the effective centre of the detector determined; the scattered share reported at each position and kept small where the result depends on it.

**Benchmark.** [3], [9]

## 7. Beam-related backgrounds and detector recovery

**Question.** At accelerator and pulsed sources, how were backgrounds from in-beam gamma rays, the prompt gamma flash, secondary neutron sources along the beam line and other beam-related sources measured and subtracted, and how quickly did the detectors recover after the prompt flash?

**Why it matters.** Gamma rays produced in the target and moderator reach the detectors with prompt and delayed components that overlap the neutron signal in time. The prompt flash can saturate a detector and blind it until the baseline recovers, which for different detectors takes from about a hundred nanoseconds to tens of microseconds and limits the highest neutron energy that can be measured. Beam striking objects along the flight tube creates secondary neutron sources.

**Resolved by.** Background counts measured in dedicated runs, for example with a sample that isolates the in-beam gamma rays, and shown with their time or energy dependence alongside the signal; the recovery time after the gamma flash stated and the usable energy range limited accordingly; secondary sources investigated and corrected for.

**Benchmark.** [3], [6]

## 8. Ambient background and spurious counts

**Question.** When the signal is a small excess of counts, how was the background without the neutron source measured, in the same geometry and over periods comparable to the signal runs, and how were spurious pulses such as electronic noise, high-voltage discharges and alpha particles from the detector walls separated from neutron events?

**Why it matters.** The ambient neutron background at the surface comes mostly from cosmic rays, and it can match or exceed a weak signal. Its rate changes with barometric pressure, by roughly 0.7% per hectopascal, and with solar activity, so a background recorded at another time may not be the background under the signal. In gas counters, discharges and wall alphas give pulses that look like neutron captures after pulse shaping, at rates that differ from counter to counter.

**Resolved by.** Source-off or blank runs in the same geometry and shielding, alternated with the signal runs or recorded over the same period, with the barometric pressure logged or corrected for; the background rate stated beside the claimed excess; the pulse-height spectrum shown with the feature expected for neutron capture, such as the 764 keV full-energy peak and wall-effect edges of a helium-3 counter; rise-time or pulse-shape cuts used to reject discharges and alpha events, with the neutron efficiency of those cuts given.

**Benchmark.** [10], [11], [12]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Sénoville et al., Neutron-γ discrimination with organic scintillators: intrinsic pulse shape and light yield contributions, Nucl. Instrum. Methods Phys. Res. A 971, 164080 (2020); read as arXiv:2005.06025 | doi:10.1016/j.nima.2020.164080 |
| 2 | R. T. Kouzes et al., Neutron detection gamma ray sensitivity criteria, Nucl. Instrum. Methods Phys. Res. A 654, 412 (2011) | doi:10.1016/j.nima.2011.07.030 |
| 3 | International Atomic Energy Agency (IAEA), Calibration of Radiation Protection Monitoring Instruments, Safety Reports Series No. 16 (IAEA, Vienna, 2000) | https://www-pub.iaea.org/MTCD/Publications/PDF/P074_scr.pdf |
| 4 | J. A. Brown et al., Proton light yield in organic scintillators using a double time-of-flight technique, J. Appl. Phys. 124, 045101 (2018); read as arXiv:2010.01704 | doi:10.1063/1.5039632 |
| 5 | G. P. A. Nobre et al., ENDF/B-VIII.1: Updated Nuclear Reaction Data Library for Science and Applications, Nucl. Data Sheets 210, 1 (2026); read as arXiv:2511.03564v2 | doi:10.1016/j.nds.2026.04.001 |
| 6 | C. Guerrero et al. (n_TOF Collaboration), Performance of the neutron time-of-flight facility n_TOF at CERN, Eur. Phys. J. A 49, 27 (2013) | doi:10.1140/epja/i2013-13027-6 |
| 7 | K. P. Harrig et al., Neutron spectroscopy for pulsed beams with frame overlap using a double time-of-flight technique, Nucl. Instrum. Methods Phys. Res. A 877, 359 (2018); read as arXiv:2010.02337 | doi:10.1016/j.nima.2017.09.051 |
| 8 | R. Worrall et al., The development, testing and comparison of unfolding methods in SPECTRA-UF for neutron spectrometry, Fusion Eng. Des. 161, 112038 (2020) | doi:10.1016/j.fusengdes.2020.112038 |
| 9 | T. Sarmento Alvarenga et al., Estimation of scattered radiation influence on neutron beams at a calibration laboratory using Monte Carlo simulation of a long counter, Braz. J. Radiat. Sci. 11, 1 (2023) | doi:10.15392/2319-0612.2023.2249 |
| 10 | T. J. Langford et al., Event identification in 3He proportional counters using risetime discrimination, Nucl. Instrum. Methods Phys. Res. A 717, 51 (2013); read as arXiv:1212.4724 | doi:10.1016/j.nima.2013.03.062 |
| 11 | C. R. Heimbach, Cosmic coincidences: investigations for neutron background suppression, J. Res. Natl. Inst. Stand. Technol. 112, 95 (2007) | doi:10.6028/jres.112.007 |
| 12 | P. Davies et al., On the variability of the barometric effect and its relation to cosmic-ray neutron sensing, Sensors 26, 925 (2026) | doi:10.3390/s26030925 |
