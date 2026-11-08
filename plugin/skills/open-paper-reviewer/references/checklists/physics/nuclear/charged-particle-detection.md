---
id: T-CHARGED-PARTICLE-DETECTION
name: Charged-particle detection and identification
type: technique
field: physics/nuclear
applies_when: the paper detects charged particles from nuclear reactions or decays with silicon detectors, energy-loss telescopes, time of flight or a magnetic spectrometer, and bases a claim on particle identification, measured energies or excitation energies, yields, cross sections or angular distributions
version: "0.1"
---

# Charged-particle detection and identification

## 1. Identification of each species

**Question.** Does the paper show the identification maps (ΔE-E, ToF-E or rigidity-based) with the gates used, quantify how well neighbouring charges and masses are separated over the energy range of the claim, and state the energy range, from the lower threshold to the punch-through energy, over which each species is identified?

**Why it matters.** The loci of neighbouring isotopes are separated only when their width, set by straggling, noise, non-uniform ΔE thickness and channelling along crystal axes in silicon, is small compared with their spacing; otherwise species mix within a gate. Particles that stop in the first layer are not identified by ΔE-E at all, particles near the energy at which they punch through the stopping detector mix with other event types, and particles that react in a thick stopping detector fall off the loci.

**Resolved by.** Identification maps shown with gates drawn, for each detector type used; a separation measure such as a figure of merit for adjacent peaks, with the contamination of each gate by its neighbours estimated; identification thresholds and punch-through energies stated per species, with events near punch-through excluded or treated; the ΔE thickness and its uniformity, the crystal orientation or other measures against channelling, and, where pulse-shape identification is used, the doping uniformity, stated.

**Benchmark.** [1], [2]

## 2. Energy calibration across species and energies

**Question.** Which reference points calibrate the energy scale (alpha sources, elastic scattering, known states), do they cover the particle species and energies on which the claims rest, and are the entrance dead layer and the pulse-height defect included?

**Why it matters.** A silicon detector does not give a signal strictly proportional to deposited energy: energy lost in the entrance window and dead layer, energy given to nuclear displacements and charge recombination in dense heavy-ion tracks all reduce the pulse. A gain fitted with light ions and applied to heavy ions without these corrections misplaces energies, and ignoring the defect can make the apparent gain vary by several per cent across one data set.

**Resolved by.** The calibration points and the fit listed, with species and energies that bracket those of the claim; the dead layer and pulse-height defect corrections stated with the formula or measurement used for each species; a check that one gain describes all calibration points once the corrections are applied; known peaks reproduced at their expected energies as a test.

**Benchmark.** [3], [4]

## 3. Energy-loss corrections and stopping powers

**Question.** Which stopping-power tables or codes were used to correct for energy lost in the target, backing, windows and dead layers, and to convert ΔE signals or thicknesses, and is the uncertainty of those values carried into the result?

**Why it matters.** Reconstructed reaction energies, excitation energies and ΔE thicknesses all depend on tabulated stopping powers. For many ion and material combinations only one data set or none exists, measurements for slow heavy ions are scarce, and a widely used semi-empirical code differs on average by about ten per cent from measurements published after it was fitted.

**Resolved by.** The tables or code and version named; an uncertainty assigned to the stopping powers that is appropriate for the ion, material and energy range, not taken as exact; the size of each energy-loss correction compared with the effect being claimed; where the correction is large, a check against a measured energy loss or a known peak.

**Benchmark.** [3], [5]

## 4. Solid angle and absolute normalisation

**Question.** How were the solid angle and angular acceptance of each detector determined (measured geometry, a calibrated source, simulation, or normalisation to a known cross section), and how were the beam dose and target thickness measured for absolute yields?

**Why it matters.** An absolute yield scales directly with the product of collected beam charge and solid angle, which is hard to determine to high accuracy and is often fixed relative to a standard. In a large-acceptance device the effective solid angle changes across the acceptance, so a single nominal value misstates angular distributions.

**Resolved by.** The method for the solid angle stated with its uncertainty; for extended or large-acceptance devices, a differential solid angle for each angular bin from a simulation that includes apertures and detector edges, validated against a known cross section such as Rutherford scattering; beam-charge integration and target thickness described with their uncertainties.

**Benchmark.** [3], [6]

## 5. Efficiency, losses and rate effects

**Question.** Does the paper correct for particles lost or misrecorded: nuclear reactions and out-scattering in thick stopping detectors, edges and dead regions, discriminator thresholds, acquisition dead time and pile-up?

**Why it matters.** Light ions crossing a thick scintillator can be lost to nuclear reactions and out-scattering at levels reported up to tens of per cent, and these events leave the identification loci. Dead time removes a fraction of triggers that can be large, and pile-up produces events at summed energies that can be taken for real signals or push particles off their loci.

**Resolved by.** Reaction-loss and out-scattering corrections stated as a function of energy or range, with their source, and edge events gated out or corrected; the thresholds and dead regions folded into the efficiency; the dead-time fraction measured and applied; pile-up modelled or shown to be negligible at the count rates used.

**Benchmark.** [2], [3], [6]

## 6. Time-of-flight calibration

**Question.** Where velocity, mass or energy is derived from time of flight, how were the flight path, the time offset and the amplitude-dependent time walk calibrated, and for heavy ions stopped in silicon, is the plasma delay corrected?

**Why it matters.** The velocity is the flight path divided by the flight time, so an error in either, or a time offset, shifts every derived mass and energy. Leading-edge timing drifts with signal amplitude and can depend on the hit position; heavy ions in silicon form a dense charge cloud that delays the signal, by up to more than a nanosecond, and also reduces its amplitude, and a start detector near the target degrades resolution and has limited efficiency.

**Resolved by.** Flight path and time offset stated and fixed by a reference (a known particle, elastic peak or beam bunch); a walk correction, position-dependent where needed, with the resulting time resolution shown; plasma delay and pulse-height defect corrected together for heavy ions; the start detector's efficiency and its effect on resolution stated; the mass resolution achieved compared with the mass separation needed.

**Benchmark.** [4], [6], [7]

## 7. Magnetic spectrometer calibration and charge states

**Question.** For spectrometer data, how were the rigidity scale and focal-plane positions calibrated, are high-order optical aberrations corrected, and, when yields come from a single transmitted charge state, how was the fraction of ions in that charge state determined?

**Why it matters.** Mass over charge follows from the rigidity and kinetic energy, but with aberrations the focal-plane position is no longer a unique function of the bending radius, and a linear calibration can leave a residual non-linearity in momentum. Ions leave the target in a distribution of charge states, only those within the rigidity limits reach the detector, and charge-state fractions taken from models can carry systematic errors too large for an absolute cross section.

**Resolved by.** The field measurement and the calibration reactions or known states used for the momentum scale, with the residual non-linearity stated; trajectory reconstruction of adequate order, tested on known lines; the charge state selected and its fraction measured under the experiment's conditions, or a model value with an uncertainty that reflects its reliability for that ion, energy and stripper.

**Benchmark.** [6], [8]

## 8. Assigning peaks to the intended reaction

**Question.** Are the peaks that carry the claim shown to come from the intended target nucleus and reaction channel, for example by following their kinematic shift with angle, rather than from target contaminants, backings or scattered beam?

**Why it matters.** Light-element contaminants such as carbon and oxygen, and target backings, give peaks from elastic and inelastic scattering or transfer whose energies move with angle differently from those of the intended reaction, and at some angles they fall in the region of interest. A peak seen at one angle only can be a contaminant line.

**Resolved by.** Spectra at several angles with each peak following the kinematics of the intended reaction; calculated contaminant loci overlaid on the spectra; measurements on a backing or contaminant target where overlap is possible; target composition and purity stated.

**Benchmark.** [6]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | G. Poggi for the FAZIA Collaboration, FAZIA: A Versatile Detection System for EoS Studies, Acta Phys. Pol. B 48, 377 (2017) | doi:10.5506/APhysPolB.48.377 |
| 2 | S. Sweany et al., Reaction losses of charged particles in CsI(Tl) crystals, Nucl. Instrum. Methods A 1018, 165798 (2021); read as preprint arXiv:2107.13531 | doi:10.1016/j.nima.2021.165798 |
| 3 | C. Jeynes et al., Accurate determination of quantity of material in thin films by Rutherford backscattering spectrometry, Anal. Chem. 84, 6061 (2012); read as the submitted manuscript hosted by the University of Surrey | doi:10.1021/ac300904c |
| 4 | J. Velkovska and R. L. McGrath, Fission fragment mass reconstruction from Si surface barrier detector measurement, Nucl. Instrum. Methods A 430, 507 (1999); read as preprint arXiv:nucl-ex/9807008 | doi:10.1016/S0168-9002(99)00225-9 |
| 5 | C. C. Montanari et al., The IAEA electronic stopping power database: modernization, review, and analysis of the existing experimental data, Nucl. Instrum. Methods B 551, 165336 (2024); read as preprint arXiv:2402.03080 | doi:10.1016/j.nimb.2024.165336 |
| 6 | F. Cappuzzello et al., The MAGNEX spectrometer: results and perspectives, Eur. Phys. J. A 52, 167 (2016); read as preprint arXiv:1606.06731 | doi:10.1140/epja/i2016-16167-1 |
| 7 | G. Kornakov et al., Performance study and calibration strategy of the HADES scintillator TOF Wall with fast digital readout, arXiv:2103.07416 (2021) | doi:10.48550/arXiv.2103.07416 |
| 8 | C. Marshall et al., Measurement of charge state distributions using a scintillation screen, Nucl. Instrum. Methods A 1056, 168661 (2023); read as preprint arXiv:2309.02991 | doi:10.1016/j.nima.2023.168661 |
