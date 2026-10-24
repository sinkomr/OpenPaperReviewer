---
id: T-NEUTRON-DETECTION
name: Neutron detection and spectroscopy
type: technique
field: physics/nuclear
applies_when: the paper counts neutrons or measures their energy spectrum with scintillators, gas counters, Bonner spheres, activation foils or time of flight, or bases a claim about a neutron yield, flux, emission rate, dose or cross section on such data
version: "0.1"
---

# Neutron detection and spectroscopy

Neutron counters and spectrometers are used to claim neutron yields, fluxes and emission rates, energy spectra, doses and reaction cross sections. Neutrons are seen only through the charged particles or light they produce, so every result depends on separating neutrons from gamma rays and from background, on the detection efficiency, and on either the time of flight (TOF) or the unfolding of a measured response into a spectrum.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Sénoville, F. Delaunay, M. Pârlog, N. L. Achouri and N. A. Orr, Neutron-γ discrimination with organic scintillators: intrinsic pulse shape and light yield contributions, Nucl. Instrum. Methods Phys. Res. A 971, 164080 (2020); read as arXiv:2005.06025 | doi:10.1016/j.nima.2020.164080 | full text | Secs. 3.3 to 3.6: figure of merit defined from the separation and widths of the neutron and gamma peaks; it falls at low energy mainly through the total light; a figure of merit of 1 taken as roughly 1% misidentified events; threshold neutron energies range from about 0.5 MeV to about 3 MeV across seven scintillators. Secs. 2.3 and 3.5: light calibrated in electron-equivalent energy from gamma sources with Compton-edge positions from simulation; non-linear electron response below about 100 keVee; thresholds converted with proton light-output functions |
| 2 | R. T. Kouzes, J. H. Ely, A. T. Lintereur, E. K. Mace, D. L. Stephens and M. L. Woodring, Neutron detection gamma ray sensitivity criteria, Nucl. Instrum. Methods Phys. Res. A 654, 412–416 (2011) | doi:10.1016/j.nima.2011.07.030 | abstract | Abstract (OSTI record 1030457): a neutron detector must meet an efficiency requirement while staying insensitive to gamma rays; measurable criteria are set for intrinsic gamma detection efficiency and gamma absolute rejection, with a defined rejection ratio, GARRn, required to lie between 0.9 and 1.1 at a 10 mR/h exposure rate |
| 3 | International Atomic Energy Agency (IAEA), Calibration of Radiation Protection Monitoring Instruments, Safety Reports Series No. 16 (IAEA, Vienna, 2000) | https://www-pub.iaea.org/MTCD/Publications/PDF/P074_scr.pdf | full text | Sec. 6.5.1: source emission rate traceable to a primary standard, angular emission rate needed as emission is rarely isotropic, photon emission from the source checked. Sec. 6.5.2: secondary neutron sources from beam striking objects along the flight tube. Sec. 6.5.4: room and air scatter have a different spectrum and affect each detector differently, air attenuation about 1 to 3% and in-scatter about 2 to 7% at 100 cm, scatter from supports, shadow cone measurement at each distance with the cone shadowing the detector, effective centre of the detector. Sec. 6.6: photon discrimination of survey meters tested |
| 4 | J. A. Brown, B. L. Goldblum, T. A. Laplace, K. P. Harrig, L. A. Bernstein, D. L. Bleuel, W. Younes, D. Reyna, E. Brubaker and P. Marleau, Proton light yield in organic scintillators using a double time-of-flight technique, J. Appl. Phys. 124, 045101 (2018); read as arXiv:2010.01704 | doi:10.1063/1.5039632 | full text | Sec. I: the light-yield relation is an input to Monte Carlo response simulations, which in turn feed pulse-height unfolding. Sec. II.3: edge positions are smeared by resolution and distorted by multiple scattering and non-linearity, so edge methods can be biased. Secs. V and VI: gamma calibration by fitting simulated energy deposition; light yield differs by about 6 to 22% between 30 ns and 300 ns integration lengths, and literature discrepancies are largely explained by integration length |
| 5 | G. P. A. Nobre et al., ENDF/B-VIII.1: Updated Nuclear Reaction Data Library for Science and Applications, Nucl. Data Sheets 210, 1–224 (2026); read as arXiv:2511.03564v2 | doi:10.1016/j.nds.2026.04.001 | full text | Sec. XI and Table XLV: the energy ranges over which each cross-section standard and reference quantity applies, including H(n,n), 6Li(n,t), 10B(n,α) and 235U(n,f), and the californium-252 spontaneous fission prompt neutron spectrum; the ENDF/B-VIII.0 standards sublibrary holds data inside and outside these ranges, and non-standard reactions, without marking them, so the table gives the ranges to use |
| 6 | C. Guerrero et al. (n_TOF Collaboration), Performance of the neutron time-of-flight facility n_TOF at CERN, Eur. Phys. J. A 49, 27 (2013) | doi:10.1140/epja/i2013-13027-6 | full text | Sec. 1: energy from flight path and time, resolution set by the relative time spread. Sec. 4: flux measured with several detectors based on reactions with standard cross sections, each used only in the energy range where the cross section is standard, normalised and averaged. Sec. 6: effective flight path includes an energy-dependent moderation length; the resolution function is non-Gaussian and asymmetric, shifts observed resonance positions and is validated with well-known resonances. Sec. 7.1: in-beam gamma background with prompt and delayed components, measured with a lead sample that scatters gamma rays and absorbs few neutrons. Sec. 7.2: the gamma flash blinds detectors until the baseline recovers, from about 100 ns to about 40 μs depending on the detector, limiting the usable energy range |
| 7 | K. P. Harrig, B. L. Goldblum, J. A. Brown, D. L. Bleuel, L. A. Bernstein, J. Bevins, M. Harasty, T. A. Laplace and E. F. Matthews, Neutron spectroscopy for pulsed beams with frame overlap using a double time-of-flight technique, Nucl. Instrum. Methods Phys. Res. A 877, 359–366 (2018); read as arXiv:2010.02337 | doi:10.1016/j.nima.2017.09.051 | full text | Sec. 1: frame overlap at pulsed sources, where fast neutrons from one pulse have the same flight time as slower neutrons from earlier pulses. Secs. 3.2 and 3.3: scintillator efficiency simulated with two codes that disagree above 2 MeV; spectrum normalised by foil activation. Sec. 4: spectra unfolded with two codes differ in shape from the time-of-flight spectrum while integrated fluxes agree within two standard deviations |
| 8 | R. Worrall, B. Colling, M. R. Gilbert, E. Litherland-Smith, C. R. Nobs, L. W. Packer, C. Wilson and A. Žohar, The development, testing and comparison of unfolding methods in SPECTRA-UF for neutron spectrometry, Fusion Eng. Des. 161, 112038 (2020) | doi:10.1016/j.fusengdes.2020.112038 | full text | Abstract and Sec. 1: with fewer reaction channels than energy channels the problem is ill-conditioned and under-determined with infinitely many solutions; methods agree with a good a priori spectrum but perform poorly with a less accurate one, one method relying more on the a priori spectrum. Sec. 3: uncertainty propagated by Monte Carlo variation of the inputs |
| 9 | T. Sarmento Alvarenga, S. S. Fernandes, W. W. Pereira, M. R. Mayhugh and L. V. E. Caldas, Estimation of scattered radiation influence on neutron beams at a calibration laboratory using Monte Carlo simulation of a long counter, Braz. J. Radiat. Sci. 11, 1–12 (2023) | doi:10.15392/2319-0612.2023.2249 | full text | Sec. 1: scatter from walls, floor and ceiling changes the spectrum and causes systematic calibration errors; ISO 8529-2 lists shadow cone, semi-empirical, generalised fit and reduced fitting methods. Sec. 3, Table 1: in the room studied the simulated scattered fluence rate (with shadow cone) exceeded the direct fluence rate at both 100 cm and 150 cm, and the scattered share grew with distance; ISO 8529-2 recommends a scattered share of at most 40% at the calibration point |
| 10 | T. J. Langford, C. D. Bass, E. J. Beise, H. Breuer, D. K. Erwin, C. R. Heimbach and J. S. Nico, Event identification in 3He proportional counters using risetime discrimination, Nucl. Instrum. Methods Phys. Res. A 717, 51–57 (2013); read as arXiv:1212.4724 | doi:10.1016/j.nima.2013.03.062 | full text | Secs. 2.1 and 3: neutron capture gives a 764 keV full-energy peak with wall-effect edges near 200 and 600 keV. Sec. 4.1: alpha particles from wall contamination overlap the neutron region, at rates varying widely among counters of one make. Sec. 4.2: microdischarges look like particle events after shaping and are separable only by rise time. Sec. 5: rise-time and pulse-height cuts reject about 99% of alpha events at a stated loss of neutron efficiency |
| 11 | C. R. Heimbach, Cosmic coincidences: investigations for neutron background suppression, J. Res. Natl. Inst. Stand. Technol. 112, 95–105 (2007) | doi:10.6028/jres.112.007 | full text | Sec. 1: the ambient neutron background, about 0.015 neutrons per cm² per second and mostly from cosmic-ray interactions with the atmosphere and ground, can be comparable to or dominate a weak neutron signal |
| 12 | P. Davies, R. Baatz, P. Schattan, E. Quansah, L. K. Amekudzi and H. R. Bogena, On the variability of the barometric effect and its relation to cosmic-ray neutron sensing, Sensors 26, 925 (2026) | doi:10.3390/s26030925 | full text | Abstract and Sec. 3.1, Table 1: cosmic-ray neutron count rates fall with barometric pressure, with coefficients of about 0.63 to 0.82% per hPa across neutron monitors and soil-moisture sensors. Secs. 1 and 2.1: count rates also vary with solar modulation of the incoming cosmic-ray flux and are corrected for it |
