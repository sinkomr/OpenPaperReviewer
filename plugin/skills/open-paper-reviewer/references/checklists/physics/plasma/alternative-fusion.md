---
id: CL-ALTERNATIVE-FUSION
name: Claims for alternative fusion concepts
type: claim
field: physics/plasma
applies_when: the paper claims fusion yield, thermonuclear conditions, confinement, breakeven or a route to energy gain for a pinch, field-reversed configuration, spheromak, magnetized target, inertial electrostatic, beam-target, aneutronic-fuel or other concept outside mainstream tokamaks and laser-driven inertial fusion
version: "0.1"
---

# Claims for alternative fusion concepts

## 1. Plasma conditions measured, not inferred from the yield

**Question.** Are the ion and electron temperatures, densities, plasma size and confinement time that support the claim measured directly, at the time and place of the fusion emission, or are they inferred from the yield itself or assumed (for example equal ion and electron temperatures, or peak values from averages)?

**Why it matters.** A temperature inferred from the yield assumes a thermal origin and so cannot confirm it. In compact and pulsed devices access is limited, and confinement time, ion temperature or ion density are often estimated from other quantities or taken from different times, which can overstate a triple product or Lawson parameter.

**Resolved by.** Independent measurements of temperature, density and magnetic field, with rough profiles and time histories, taken during the emission; each inferred quantity and its assumptions labelled as such; confinement time defined and its bounds stated; all parameters taken from the same shot or from well-reproduced shots, not peak values from different shots.

**Benchmark.** [1], [2], [4]

## 2. Timing of the emission against the plasma history

**Question.** When during the discharge or pulse do the fusion products appear, how long does the emission last, and is that timing compared with the phases of the plasma, such as formation, compression, a quiescent stable period, or the onset of instabilities and disruption?

**Why it matters.** In pinches, beam-target emission tends to come in short bursts tied to instabilities, lasting tens to hundreds of nanoseconds, while emission from a confined thermal plasma should follow the period of good confinement. The share of non-thermal emission can also change during a single pulse, so a yield integrated over the whole pulse can mix both.

**Resolved by.** Time-resolved fusion-product signals plotted on the same time axis as current, magnetic, density and temperature diagnostics; the emission duration compared with instability growth times and the confinement period; any time-resolved test of origin, for example isotropy measured in separate time windows.

**Benchmark.** [3], [4]

## 3. Neutron signals in a pulsed environment

**Question.** How does the paper show that the detector signal comes from fusion neutrons and not from x-rays, electrical noise or pile-up, and how was the calibration corrected for the spectrum and pulse shape of the burst?

**Why it matters.** Pulsed-power devices produce hard x-rays and electromagnetic interference at the moment of emission, and a burst of neutrons arrives faster than counting detectors can resolve. An isotopic calibration source has a different spectrum and time structure from the plasma, so the conversion from signal to yield needs explicit corrections.

**Resolved by.** Shots with a non-fusing fill, such as hydrogen only, showing no signal; shielding against x-rays and a measured noise background; the calibration corrected for the difference in spectrum and pulse shape between the calibration source and the burst; a second detector type used to check the gamma-ray background; the uncertainty from counting, pile-up and noise stated across the range of yields reported.

**Benchmark.** [3], [4], [5]

## 4. Where the reactions take place

**Question.** Does the paper show that the reactions occur in the confined plasma, and not on electrodes, grids or walls loaded with fuel, or between fast ions or neutrals and background gas?

**Why it matters.** In electrostatic and beam-driven devices a large share of the reactions can occur on cathode and anode surfaces, on the chamber wall or in the background gas. Such reactions add to the yield but do not show the confinement or convergence the concept depends on, and they scale differently with device size.

**Resolved by.** A spatially resolved measurement of the reaction distribution, for example collimated detection of charged fusion products or neutron imaging; the shares from volume, surfaces and background gas estimated; the dependence of yield on gas pressure and on electrode material or loading reported.

**Benchmark.** [6]

## 5. Identification of charged fusion products

**Question.** For claims based on charged fusion products, such as alpha particles from proton-boron reactions, does the paper show that the detected particles are fusion products and not other ions from the plasma or the driver, and how was the detector calibrated for each species and energy?

**Why it matters.** Laser- and beam-driven plasmas accelerate protons, carbon, boron and other ions in large numbers. On track detectors a track of a given size can come from different ions or energies, and on magnetic spectrometers several species share the same charge-to-mass ratio, so a small alpha signal can be confused with a much larger background of other ions.

**Resolved by.** Species identification by two or more independent means, for example a spectrometer with charge-to-mass separation together with track detectors behind filters chosen to stop heavier ions; track-size calibrations for each relevant species against etching time; the number of fusion products estimated with the background from other ions subtracted and its uncertainty stated.

**Benchmark.** [9]

## 6. Which energy is counted against the fusion output

**Question.** When the paper quotes a gain or breakeven, which input energy is the denominator (energy absorbed by the fuel, energy delivered to the plasma or target, energy stored in the capacitor bank or driver, or electrical energy from the grid), and does it count the energy spent forming, heating, compressing and sustaining the plasma, including any power recirculated to keep it out of equilibrium?

**Why it matters.** Fuel gain, scientific gain and engineering or wall-plug gain can differ by orders of magnitude for pulsed and magneto-inertial concepts, whose drivers deliver only a fraction of their stored energy to the fuel. Concepts that rely on non-thermal ion distributions also need recirculating power to maintain them, and for most such schemes that power can exceed the fusion power.

**Resolved by.** The gain named and defined, with each energy in the denominator measured and stated; the coupling efficiencies from stored to delivered to absorbed energy given; for non-equilibrium concepts, the power needed to maintain the distribution estimated and included.

**Benchmark.** [1], [2], [8]

## 7. Extrapolation from the device to gain

**Question.** When the paper projects energy gain or a reactor from present results, does it state the scaling it assumes, show that the reactions on which the projection rests are of a kind that scales, and estimate the losses that grow at the projected conditions, such as bremsstrahlung, collisional relaxation of non-thermal ions and electron losses?

**Why it matters.** Beam-target yields, and ion distributions that collisions relax faster than the ions fuse, set limits that do not apply to a thermal plasma, and several electrostatic and non-equilibrium schemes face loss channels that exceed the fusion power. Advanced fuels such as deuterium-helium-3 and proton-boron need much higher triple products than deuterium-tritium, and at the temperatures they need, bremsstrahlung can approach or exceed the fusion power.

**Resolved by.** The scaling law and its basis stated, with the measured range it rests on and the factor of extrapolation; a power balance at the projected conditions that includes radiation, transport and the energy to maintain non-thermal populations; for advanced fuels, the electron temperature assumed and the bremsstrahlung it implies; the projection presented as a projection, separate from what was measured.

**Benchmark.** [1], [2], [7], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | S. E. Wurzel and S. C. Hsu, Progress toward fusion energy breakeven and gain as measured against the Lawson criterion, Phys. Plasmas 29, 062103 (2022); read as arXiv:2105.10954 | doi:10.1063/5.0083990 |
| 2 | S. C. Hsu et al., Retrospective of the ARPA-E BETHE-GAMOW-era fusion programs and project cohorts, J. Fusion Energy 44, 38 (2025); read as arXiv:2505.01784 | doi:10.1007/s10894-025-00504-4 |
| 3 | R. A. Ryan et al., Time-resolved measurement of neutron energy isotropy in a sheared-flow-stabilized Z pinch, arXiv:2408.05171 (2024) | doi:10.48550/arXiv.2408.05171 |
| 4 | Y. Zhang et al., Sustained neutron production from a sheared-flow stabilized Z pinch, Phys. Rev. Lett. 122, 135001 (2019); read as arXiv:1806.05894 | doi:10.1103/PhysRevLett.122.135001 |
| 5 | A. Tarifeño-Saldivia et al., Methodology for the use of proportional counters in pulsed fast neutron yield measurements, arXiv:1110.2500 (2011) | doi:10.48550/arXiv.1110.2500 |
| 6 | K. Masuda et al., Diagnostic system development for D-D and D-3He reaction distributions in an inertial-electrostatic confinement device by collimated proton measurements, Fusion Sci. Technol. 56, 528 (2009); abstract read on the American Nuclear Society page | doi:10.13182/FST09-A8957 |
| 7 | T. H. Rider, A general critique of inertial-electrostatic confinement fusion systems, Phys. Plasmas 2, 1853 (1995); abstract read from the Crossref record | doi:10.1063/1.871273 |
| 8 | T. H. Rider, Fundamental limitations on plasma fusion systems not in thermodynamic equilibrium, Phys. Plasmas 4, 1039 (1997); abstract read from the Crossref record | doi:10.1063/1.872556 |
| 9 | V. Kantarelou et al., A methodology for the discrimination of alpha particles from other ions in laser-driven proton-boron reactions using CR-39 detectors coupled in a Thomson parabola spectrometer, Laser Part. Beams 2023, e10 (2023) | doi:10.1155/2023/3125787 |
