---
id: T-LASER-COOLING
name: Laser cooling and trapping of neutral atoms
type: technique
field: physics/amo
applies_when: the paper reports atom numbers, temperatures, densities, phase-space densities, trap frequencies, trap depths or lifetimes of laser-cooled or evaporatively cooled neutral atoms in a magneto-optical trap, optical molasses or optical dipole trap, or bases a claim on fluorescence, absorption, time-of-flight or release-and-recapture measurements
version: "0.1"
---

# Laser cooling and trapping of neutral atoms

## 1. Atom number from fluorescence

**Question.** When atom number is inferred from fluorescence, which photon scattering rate per atom was assumed, how were the intensity, detuning and collection efficiency that enter it determined, and was the number checked by an independent method?

**Why it matters.** The scattering rate in a MOT depends on the intensity of several beams at the atoms, the detuning, the population of magnetic sublevels and the multilevel structure of the transition. A multilevel transition has a higher effective saturation intensity and a lower maximum scattering rate than a two-level atom, so a two-level formula with the free-space saturation intensity can misstate the atom number. Fluorescence imaging collects only a small fraction of the scattered light, set by the geometry of the optics, and in a dipole trap the light shift of the transition changes the effective detuning.

**Resolved by.** The scattering-rate model and effective saturation intensity stated, with the intensity and detuning at the atoms; the collection solid angle, the transmission of the optics and the detector calibration given; a cross-check against absorption or against a measured scattering rate; for atoms in a dipole trap, the light shift taken into account; the resulting uncertainty in atom number stated.

**Benchmark.** [2], [4], [5], [6]

## 2. Atom number and density from absorption imaging

**Question.** When atom number or density comes from absorption imaging, what absorption cross-section and probe saturation were assumed, what was the peak optical density, and are the probe intensity, detuning and duration given?

**Why it matters.** The cross-section depends on the probe polarisation and the sublevel populations, and at high probe intensity the Beer–Lambert law needs a saturation term with an effective saturation intensity that must be calibrated; neglecting it can underestimate the optical depth by about a factor of two. Measured optical densities above about three or four are limited by camera noise and dynamic range, so the centre of a dense cloud is undercounted, while detuning the probe to reduce absorption makes the cloud act as a lens and distorts the image. Each absorbed photon pushes and heats the atoms, which blurs the image during a long probe pulse.

**Resolved by.** The cross-section and any correction factor stated and calibrated, for example by varying the probe intensity; the peak optical density kept within the range the imaging system can measure, or a method designed for dense clouds used; magnification and resolution measured; the number of photons scattered per atom during the probe estimated; densities and phase-space densities quoted with the effect of the atom-number uncertainty on them.

**Benchmark.** [2], [3]

## 3. Temperature from time of flight

**Question.** When a temperature comes from time of flight, over what range of expansion times was the cloud size measured, was the initial size included in the fit, and were all trapping light and magnetic fields off during the expansion?

**Why it matters.** The temperature follows from the growth of the cloud size only for free, ballistic expansion of a thermal distribution: at short times the initial size dominates, and residual magnetic fields, slowly decaying coil currents or collisions during the expansion change the expansion and bias the result. A cloud with a cold and a hot component, or a non-Gaussian profile, gives a temperature that depends on which part of the profile is fitted. Temperatures from the size of a cloud held in the trap depend instead on knowing the trap frequencies.

**Resolved by.** Cloud size against time over several expansion times that are long compared with the initial size divided by the thermal velocity; a fit that includes the initial size; switch-off times of beams and coils stated, with a check that no residual force acts, such as the absence of centre-of-mass motion; each axis reported; imaging magnification calibrated; non-thermal components treated explicitly; for in-trap thermometry, measured trap frequencies.

**Benchmark.** [1], [2], [7]

## 4. Temperature from release and recapture

**Question.** When a temperature is extracted from release and recapture, what model of the trap, the capture region and the atomic motion converts recapture probability into temperature, and how were the model's parameters measured?

**Why it matters.** The recapture fraction carries information on temperature only through a model of which atoms are still within the capture region after the release time. The result depends on the assumed waist, depth and shape of the potential, on gravity and on the recapture efficiency at zero release time. A thermal distribution in a harmonic potential is a fair starting point only when the trap depth is much larger than the thermal energy.

**Resolved by.** The recapture probability plotted against release time, including the efficiency at zero release time; the model stated, for example a Monte Carlo simulation of classical trajectories, with measured waist and depth and with gravity included; the temperature uncertainty including that of the model parameters; the ratio of trap depth to thermal energy given; where possible, a cross-check by a second method such as adiabatic lowering of the trap or time of flight.

**Benchmark.** [1], [4]

## 5. Temperature against the cooling mechanism

**Question.** When a temperature is compared with the Doppler limit or offered as evidence for a cooling mechanism, does the paper report how it varies with intensity, detuning, magnetic field and atom number or density?

**Why it matters.** The Doppler limit depends on the linewidth and the detuning; sub-Doppler temperatures scale roughly with intensity divided by detuning, need the magnetic field at the atoms to be close to zero, and sudden changes of the cooling light can leave a bimodal velocity distribution. At high density, light scattered by one atom and reabsorbed by another heats the cloud and limits the density. A temperature at one setting cannot separate mechanisms and may not hold at another atom number.

**Resolved by.** Temperature plotted against intensity and detuning, with the Doppler temperature of the transition stated; the compensation of stray magnetic fields described and the residual field estimated; the temperature reported at the atom number and density of the main result; the dependence on density shown.

**Benchmark.** [6], [7], [8], [9]

## 6. Depth and frequencies of an optical dipole trap

**Question.** Were the trap depth and trap frequencies measured, for example by parametric excitation or by oscillation of the cloud, or only calculated from laser power, beam waist and polarisability, and is the harmonic approximation valid at the temperature of the atoms?

**Why it matters.** The depth scales with intensity over detuning and the frequencies with the square root of depth divided by the waist or the Rayleigh length, so errors in the waist at the atoms or in the delivered power pass into every derived quantity. Circular or mixed polarisation makes the potential depend on the magnetic sublevel, the effective depth of a crossed-beam trap is only half its peak depth at the crossing, because more energetic atoms escape along one beam, and gravity lowers the barrier of a shallow trap. A Gaussian beam gives a harmonic potential only for atoms whose thermal energy is well below the depth.

**Resolved by.** Trap frequencies measured, for example by parametric excitation at twice the trap frequency or by cloud oscillations, and compared with values calculated from the measured waist and power; the depth stated together with its ratio to the thermal energy; the trap polarisation stated; gravity included for shallow traps; measured rather than calculated frequencies used for densities, phase-space densities and in-trap temperatures.

**Benchmark.** [1], [4]

## 7. Lifetime, loss and heating

**Question.** How was the trap lifetime measured and modelled: was the decay fitted with separate one-body and density-dependent terms, were heating and loss told apart, and were near-resonant light and laser noise excluded as causes?

**Why it matters.** Atoms are lost through collisions with background gas (one-body), through light-assisted and hyperfine-changing collisions between trapped atoms (two-body) and through three-body collisions, and they are heated out of the trap by photon scattering and by laser intensity and pointing noise. A single exponential fitted to a decay that contains density-dependent loss or heating gives a time constant that is not the background-limited lifetime. Collisions that heat atoms without ejecting them make the loss rate depend on trap depth, so converting a lifetime to a pressure depends on depth and gas species and, without calibration, is accurate only to about a factor of two.

**Resolved by.** Atom number and temperature against hold time, fitted with stated one-body and two-body terms and a measured density; the lifetime compared at different densities or with near-resonant light off; the laser intensity noise or the heating rate measured and compared with the heating expected from photon scattering; the trap depth and the assumed loss coefficient stated when a pressure is inferred.

**Benchmark.** [1], [10], [11], [12], [13]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | R. Grimm et al., Optical dipole traps for neutral atoms, Adv. At. Mol. Opt. Phys. 42, 95 (2000); read as arXiv:physics/9902072 | doi:10.1016/S1049-250X(08)60186-X |
| 2 | W. Ketterle et al., Making, probing and understanding Bose-Einstein condensates, contribution to the proceedings of the 1998 Enrico Fermi summer school, arXiv:cond-mat/9904034 (1999) | doi:10.48550/arXiv.cond-mat/9904034 |
| 3 | G. Reinaudi et al., Strong saturation absorption imaging of dense clouds of ultracold atoms, Opt. Lett. 32, 3143 (2007); read as arXiv:0707.2930 | doi:10.1364/OL.32.003143 |
| 4 | C. Tuchendler et al., Energy distribution and cooling of a single atom in an optical tweezer, Phys. Rev. A 78, 033425 (2008); read as arXiv:0805.3510 | doi:10.1103/PhysRevA.78.033425 |
| 5 | K. Jooya et al., Photon-scattering-rate measurement of atoms in a magneto-optical trap, Phys. Rev. A 88, 063401 (2013) | doi:10.1103/PhysRevA.88.063401 |
| 6 | N. J. Fitch and M. R. Tarbutt, Laser-cooled molecules, Adv. At. Mol. Opt. Phys. 70, 157 (2021); read as arXiv:2103.00968 | doi:10.1016/bs.aamop.2021.04.003 |
| 7 | M. Landini et al., Sub-Doppler laser cooling of potassium atoms, Phys. Rev. A 84, 043432 (2011); read as arXiv:1107.2337 | doi:10.1103/PhysRevA.84.043432 |
| 8 | P. D. Lett et al., Optical molasses, J. Opt. Soc. Am. B 6, 2084 (1989) | doi:10.1364/JOSAB.6.002084 |
| 9 | C. G. Townsend et al., Phase-space density in the magneto-optical trap, Phys. Rev. A 52, 1423 (1995) | doi:10.1103/PhysRevA.52.1423 |
| 10 | T. Arpornthip et al., Vacuum-pressure measurement using a magneto-optical trap, Phys. Rev. A 85, 033420 (2012); read as arXiv:1203.0189 | doi:10.1103/PhysRevA.85.033420 |
| 11 | T. A. Savard et al., Laser-noise-induced heating in far-off resonance optical traps, Phys. Rev. A 56, R1095–R1098 (1997) | doi:10.1103/PhysRevA.56.R1095 |
| 12 | S. P. Eckel et al., Effect of glancing collisions in the cold-atom vacuum standard, Phys. Rev. A 111, 023317 (2025); read as arXiv:2409.11226 | doi:10.1103/PhysRevA.111.023317 |
| 13 | C. W. Gardiner et al., Evaluation of heating effects on atoms trapped in an optical trap, Phys. Rev. A 61, 045801 (2000); read as arXiv:quant-ph/9910056 | doi:10.1103/PhysRevA.61.045801 |
