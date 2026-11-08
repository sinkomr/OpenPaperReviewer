---
id: T-STORAGE-RINGS
name: Ion storage rings and highly charged ions
type: technique
field: physics/amo
applies_when: the paper studies highly charged ions in a heavy-ion storage ring, electron beam ion trap or Penning trap and reports transition energies, line identifications, recombination resonances or rate coefficients, lifetimes, masses, g-factors or comparisons with bound-state quantum electrodynamics
version: "0.1"
---

# Ion storage rings and highly charged ions

## 1. Electron beam energy and charge-state assignment in an EBIT

**Question.** For EBIT data, how was the effective electron energy obtained from the nominal acceleration voltage, what is the energy spread, and how were the charge state of each ion and the assignment of each line established?

**Why it matters.** The beam's own space charge lowers the effective electron energy below the nominal voltage, trapped ions partly offset this, and both terms change with beam current and trap depth. The trap holds a distribution of charge states set by the beam energy relative to the ionisation energies, and ions with several valence electrons have dense spectra, so a line can belong to a neighbouring charge state or be a blend.

**Resolved by.** The space-charge correction measured, for example from radiative recombination peak positions or by varying beam current and trap depth, not only estimated; the beam energy spread stated; charge states assigned from known reference resonances, from the beam energies at which lines appear, or from a modelled charge-state balance; line identifications checked against calculations and along an isoelectronic sequence, with possible blends considered.

**Benchmark.** [1], [2], [3]

## 2. Collision energy scale in merged-beam recombination

**Question.** For recombination measured at a storage-ring electron cooler or electron target, how was the electron-ion collision energy derived from the electron and ion velocities, how was the energy scale checked, and what energy spread enters the resonance shapes?

**Why it matters.** The collision energy is set by the small difference between electron and ion velocities, so the cathode voltage calibration and the space-charge correction carry directly into resonance positions and can leave the energy scale uncertain at the level of a per cent. Where the electron beam is bent in and out of the ion beam, the two cross at changing angles and add signal at shifted energies. The transverse and longitudinal electron temperatures set a resolution that varies with energy and limits what can be said about narrow or very low-energy resonances.

**Resolved by.** The relation used for the collision energy stated, including space charge; the scale checked against independently known energies, such as spectroscopic Rydberg series limits, with any rescaling reported; the contribution of the merging and demerging sections corrected from the geometry; electron temperatures stated and included in fitted resonance shapes; where resonance positions are turned into excitation energies, the calculated Rydberg binding energy and the ion-energy definition given with their uncertainties.

**Benchmark.** [4], [5], [6]

## 3. Detection cutoff, initial-state population and normalisation of rate coefficients

**Question.** Does the paper state which high Rydberg levels of the recombined ions survive to the detector, which long-lived metastable levels are populated in the stored ion beam, how unmeasured resonance strength was handled, and how the absolute rate coefficient was normalised and its background removed?

**Why it matters.** Motional electric fields in the magnets between the interaction region and the detector field-ionise recombined ions in high Rydberg states, so part of the resonance strength is not measured, and a simple sharp cutoff can describe the apparatus poorly. Filling the gap with theory makes a derived plasma rate coefficient partly theoretical. Ions in metastable levels that outlive the storage time before measurement add resonances of their own and change the number of ions in the ground state. The absolute scale rests on the ion and electron currents, the overlap and the detection efficiency, and electron capture on residual gas adds background.

**Resolved by.** The surviving range of Rydberg levels estimated with a model of the fields along the flight path, including radiative decay; any part added from theory shown separately from the measured part; the storage time before measurement stated, resonances from metastable levels identified, and any remaining metastable fraction estimated with its effect on the rate coefficient; plasma rate coefficients given only for temperatures where the experimental resolution does not change them, or with that effect stated; the systematic normalisation uncertainty stated with its main contributions; residual-gas background measured, for example at a reference energy, and subtracted.

**Benchmark.** [4], [7], [9]

## 4. Doppler shifts, ion motion and trap fields

**Question.** How were the ion velocity and the observation or laser angle determined, and how were the Doppler shift, Doppler broadening and any Zeeman structure from the trap's magnetic field included in the fitted line positions and widths?

**Why it matters.** For fast stored ions the photon energy seen in the laboratory depends on the Lorentz factor and on the angle between the ion and the photon, so errors in ion velocity, laser-ion angle or target position shift the result. Ions in an EBIT are hot, which broadens lines and limits resolving power, and the strong field of the trap splits lines into Zeeman components that change their apparent widths and centres.

**Resolved by.** The ion velocity from a calibrated cooler voltage or revolution frequency, with its uncertainty; the laser-ion angle or the position of target and detectors given with uncertainties; a Doppler-reduction scheme where available, such as comparison with a line in the same spectrum that is insensitive to QED and nuclear size; line shapes fitted with Zeeman components at the stated field and a Doppler width taken from a line of negligible natural width.

**Benchmark.** [1], [3], [6], [8]

## 5. Wavelength calibration and polarisation

**Question.** Against which reference lines, measured or calculated, were the spectra calibrated, and were line intensities corrected for the polarisation of the emission and the polarisation sensitivity of the spectrometer?

**Why it matters.** When reference energies are themselves calculated, the result is a measurement relative to theory, which weakens it as a test of that theory; reference-free methods that determine the Bragg angle directly avoid this. Emission excited by a directed electron beam is anisotropic and partly polarised, cascades change the polarisation, and crystal reflectivity differs for the two polarisation directions by an amount that depends on the Bragg angle, so line ratios and cross sections observed at one angle need polarisation-dependent corrections.

**Resolved by.** The reference lines listed with the source and uncertainty of their energies; an absolute or reference-free calibration where the claim is a test of theory; polarisation measured, for example with two spectrometers whose dispersion planes are perpendicular, or calculated including cascades; the relative efficiency of detectors normalised on an unpolarised line; the angular factor used to convert observed intensities into total cross sections stated.

**Benchmark.** [3], [8]

## 6. Lifetimes from decay curves

**Question.** For lifetimes from decay curves recorded in an EBIT, ion trap or storage ring, how were ion loss, repopulation and competing decay channels separated from the radiative decay of the level?

**Why it matters.** The fitted decay constant combines radiative decay with the loss of ions from the trap or ring, mainly through charge exchange and other collisions with residual gas. Recombination of more highly charged ions or cascades from higher levels can add slower components, and fluorescence detection suffers from small solid angles and background photons, which matters most for weak decay channels.

**Resolved by.** The ion loss rate measured independently, for example from the stored ion current or with a reference isotope that lacks the decay channel of interest, and corrected for; production conditions chosen to avoid a recombination tail, or the tail modelled; the choice between single- and multi-exponential fits justified; competing decay channels and the effect of external fields evaluated; the background subtraction described.

**Benchmark.** [1], [5], [9], [10]

## 7. Comparison with bound-state QED and nuclear inputs

**Question.** When a result is presented as a test of QED, does the paper show the size of the QED contribution next to the uncertainties of the nuclear corrections (charge radius and distribution, nuclear polarisation, magnetisation distribution, nuclear magnetic moment) and of uncalculated higher-order terms?

**Why it matters.** In heavy ions the finite nuclear size is a correction comparable in size to the QED terms, and its uncertainty, which depends on the assumed charge distribution as well as the radius, can be large compared with higher-order QED contributions for inner shells. Hyperfine splittings depend on the nuclear magnetisation distribution and magnetic moment, whose uncertainties can be larger than the QED term. Agreement or disagreement then says more about the nuclear inputs than about QED.

**Resolved by.** The theoretical value broken down into contributions with uncertainties and the nuclear inputs named with their sources; the experiment-theory difference compared with the size of the QED term, giving the fraction of QED tested; a specific difference between charge states, or an isotope comparison, where nuclear uncertainty dominates; the dependence of any derived quantity on calculated energies stated.

**Benchmark.** [1], [8], [11]

## 8. Penning-trap frequency ratios

**Question.** For masses or bound-electron g-factors measured in a Penning trap, how was the frequency ratio corrected for trap-specific shifts, and how were the external inputs, such as reference masses, ion masses and electron binding energies, handled?

**Why it matters.** Image charges, magnetic field inhomogeneity, electrostatic anharmonicity, misalignment, relativistic effects and the line-shape model each shift the measured ratio, and for a single highly charged ion the image-charge shift can dominate the budget. Many of these shifts scale with the difference in mass-to-charge ratio between the ion and the reference. Converting an ion mass to an atomic mass, or a g-factor ratio to an electron mass, uses electron binding energies and other masses whose uncertainties pass into the result.

**Resolved by.** A table of systematic shifts with the value and uncertainty of each; a reference ion of similar mass-to-charge ratio, or a measured mass-dependent shift; frequencies extrapolated to zero motional energy where the shifts depend on it; the line-shape model stated; external constants listed with their sources and their uncertainties propagated.

**Benchmark.** [12], [13]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. G. Kozlov et al., Highly charged ions: optical clocks and applications in fundamental physics, Rev. Mod. Phys. 90, 045005 (2018); read as arXiv:1803.06532 | doi:10.1103/RevModPhys.90.045005 |
| 2 | P. Micke et al., The Heidelberg compact electron beam ion traps, Rev. Sci. Instrum. 89, 063109 (2018); read as arXiv:2011.01363 | doi:10.1063/1.5026961 |
| 3 | C. Shah et al., High-resolution laboratory measurements of K-shell X-ray line polarization and excitation cross sections in heliumlike S XV ions, Astrophys. J. 914, 34 (2021); read as arXiv:2106.06493 | doi:10.3847/1538-4357/abf1ea |
| 4 | S. Schippers et al., Storage ring measurement of the C IV recombination rate coefficient, Astrophys. J. 555, 1027 (2001); read as arXiv:astro-ph/0101552 | doi:10.1086/321512 |
| 5 | S. Schippers, Relativistic, QED and nuclear effects in highly charged ions revealed by resonant electron-ion recombination in storage rings, Nucl. Instrum. Methods B 267, 192 (2009); read as arXiv:0805.4381 | doi:10.1016/j.nimb.2008.10.040 |
| 6 | M. Steck and Yu. A. Litvinov, Heavy-ion storage rings and their use in precision experiments with highly charged ions, Prog. Part. Nucl. Phys. 115, 103811 (2020); read as arXiv:2003.05201 | doi:10.1016/j.ppnp.2020.103811 |
| 7 | S. Schippers, Electron-ion merged-beam experiments at heavy-ion storage rings, Nucl. Instrum. Methods B 350, 61 (2015); read as arXiv:1407.6500 | doi:10.1016/j.nimb.2014.12.050 |
| 8 | P. Indelicato, QED tests with highly charged ions, J. Phys. B 52, 232001 (2019); read as arXiv:1909.06274 | doi:10.1088/1361-6455/ab42c9 |
| 9 | S. Schippers, Storage-ring measurements of hyperfine induced transition rates in berylliumlike ions, AIP Conf. Proc. 1545, 7 (2013); read as arXiv:1211.1178 | doi:10.1063/1.4815836 |
| 10 | Lawrence Livermore National Laboratory, EBIT measurements of atomic level lifetimes, web page of the LLNL electron beam ion trap group (undated; accessed 2026) | https://ebit.llnl.gov/research/ebit-measurements-atomic-level-lifetimes |
| 11 | V. M. Shabaev et al., Stringent tests of QED using highly charged ions, Hyperfine Interact. 239, 60 (2018); read as arXiv:1812.00742 | doi:10.1007/s10751-018-1537-8 |
| 12 | F. Köhler et al., The electron mass from g-factor measurements on hydrogen-like carbon 12C5+, J. Phys. B 48, 144032 (2015); read as arXiv:1604.04380 | doi:10.1088/0953-4075/48/14/144032 |
| 13 | M. Brodeur et al., Verifying the accuracy of the TITAN Penning-trap mass spectrometer, Int. J. Mass Spectrom. 310, 20 (2012); read as arXiv:1110.3003 | doi:10.1016/j.ijms.2011.11.002 |
