---
id: T-LEVITATED-OPTOMECHANICS
name: Optical tweezers and levitated optomechanics
type: technique
field: physics/amo
applies_when: the paper traps a particle in an optical tweezer in gas or vacuum, or in liquid other than as a handle for single-molecule, motor or microrheology measurements, and reports a trap stiffness, calibrated force, motional temperature or occupation, heating rate, or force or acceleration sensitivity
version: "0.1"
---

# Optical tweezers and levitated optomechanics

## 1. Displacement calibration and its conditions

**Question.** How was the detector signal converted to displacement, under which conditions (pressure, laser power, feedback on or off) was the conversion factor obtained, and does the paper show that the factor still holds under the conditions of the headline measurement?

**Why it matters.** The usual calibration assumes that the particle is in thermal equilibrium with gas at a known temperature and that the trap is harmonic, and it needs the particle mass. At low pressure, absorption can raise the effective bath temperature, and the conversion factor can change between the calibration pressure and the operating pressure, so a factor taken at one pressure and applied at another biases every energy, occupation and force derived from it.

**Resolved by.** The calibration method named with its assumptions; the bath temperature and pressure at calibration stated; a second, independent calibration, such as a known driving force on a charged particle or a sideband ratio that needs no absolute calibration, compared with the first; the factor checked, or its drift bounded, at the operating conditions.

**Benchmark.** [1], [2], [9]

## 2. Trap stiffness in liquid

**Question.** For tweezers in liquid, which method gave the trap stiffness (equipartition, power spectrum, autocorrelation, or an applied flow or oscillation), which inputs did it need (temperature, viscosity, particle radius, distance from the nearest surface), and over what frequency range and with what detector model was any spectrum fitted?

**Why it matters.** Stiffness methods differ in what they assume: methods based on the drag coefficient need the viscosity and radius and hold only far from walls, and equipartition is biased by position noise and by filtering. A simple Lorentzian fit ignores hydrodynamic corrections to Brownian motion and the low-pass filtering of silicon photodiodes at near-infrared wavelengths, and strong traps can give spectra that a Lorentzian does not fit.

**Resolved by.** The method and every input stated with its value and source; the height above the surface given where drag enters; the fitted model including hydrodynamic and detector-filtering terms, or a demonstration that they are negligible in the fitted range; the fit range and residuals shown; agreement between two methods on the same data.

**Benchmark.** [2], [3], [4]

## 3. Nonlinearity, mode coupling and linewidth

**Question.** Does the paper show that the motion stays in the harmonic regime of the trap for the amplitudes used in calibration and measurement, and, in vacuum, how was the damping rate obtained: from the spectral linewidth, a ringdown, or a gas model?

**Why it matters.** A Gaussian focus gives an anharmonic potential, and at low pressure thermal motion alone can reach the nonlinear regime, so the frequency of each mode depends on the amplitudes of all modes. The spectral peak then becomes asymmetric and much broader than the damping rate implies, so a linewidth read as damping overstates it, and equipartition of potential energy no longer holds.

**Resolved by.** Amplitudes compared with the beam waist, or the nonlinear coefficients measured; damping rates from ringdown or from a stated gas-kinetic model rather than from a linewidth at low pressure; energies taken from kinetic energy or from a model that includes the nonlinearity where amplitudes are large; correlations between mode energies and frequencies checked.

**Benchmark.** [1], [5]

## 4. Particle mass and size

**Question.** How were the particle's mass and radius determined (manufacturer specification, inference from gas damping, or a direct measurement), with what uncertainty, and how does that uncertainty enter the quoted force, temperature or occupation?

**Why it matters.** Converting a displacement into a force or an energy needs the mass. Nominal sizes have a spread of a few per cent, the density of amorphous silica can vary by up to about a fifth, and mass inferred from gas damping also depends on the density and the gas pressure, so mass estimates are often uncertain by tens of per cent and the force error follows.

**Resolved by.** The method for the mass stated with its inputs and uncertainty; where a force or acceleration is a headline, a direct mass measurement, for example by driving a particle of known charge with a known field, with its systematic uncertainty itemised; consistency between the methods used.

**Benchmark.** [1], [6]

## 5. Occupation inferred under feedback

**Question.** When the motion is cooled by feedback, is the temperature or occupation read from an out-of-loop detector, and does the analysis include the measurement imprecision fed back into the motion?

**Why it matters.** At high feedback gain the in-loop signal contains measurement noise correlated with the motion, and its spectrum can fall below the detection noise floor. Reading the occupation from the in-loop signal then underestimates the true energy. The imprecision fed back also heats the particle and sets a floor on the occupation that depends on detection efficiency.

**Resolved by.** An independent out-of-loop measurement used for thermometry, or an in-loop estimate validated against one; the in-loop and out-of-loop spectra shown; the occupation compared with a model whose parameters (feedback gain, imprecision noise, heating rate) were measured separately, with the number of free parameters stated.

**Benchmark.** [7], [8]

## 6. Ground-state and quantum claims

**Question.** When the paper claims an occupation near or below one, does it rest on a measurement that needs no absolute calibration, such as motional sideband asymmetry, and does the paper exclude classical laser noise and detector imbalance as sources of the asymmetry?

**Why it matters.** The ratio of Stokes and anti-Stokes sidebands gives the occupation without a displacement calibration, but classical laser phase noise heats the motion and squashes or anti-squashes the detected sidebands, which biases the inferred occupation and can mask the quantum asymmetry, and the two sidebands can see different detector responses. A claimed occupation should also be consistent with the measured detection efficiency, which bounds the occupation that feedback cooling can reach.

**Resolved by.** Sideband spectra with background subtraction described, and the sidebands swapped (for example by changing the sign of the heterodyne offset) to remove response imbalance; laser noise measured at the mechanical frequency or shown not to change the result; the asymmetry compared with a calibrated classical estimate; the detection efficiency and the ratio of measurement rate to decoherence rate reported and consistent with the occupation.

**Benchmark.** [8], [9], [10], [11], [13]

## 7. Heating budget from gas and photon recoil

**Question.** Does the paper measure the heating rate directly, for example by switching off cooling and following the reheating, and compare it with the contributions expected from residual gas, photon recoil and laser noise at the stated pressure and power?

**Why it matters.** Heating from gas collisions scales with pressure and particle size, while photon recoil heating scales with scattered power, depends on the axis relative to the polarisation and dominates at very low pressure. A heating rate that is not measured, or an occupation not set against the measured heating, leaves the claimed cooling performance unsupported. Absorption also raises the particle's internal temperature, which adds emission and can lead to particle loss at low pressure.

**Resolved by.** Reheating curves with the time window short compared with the damping time; heating measured at several pressures and powers and separated into gas and recoil parts; laser intensity noise and feedback heating estimated and shown small or included; the internal temperature of the particle considered where absorption is significant.

**Benchmark.** [7], [8], [12], [13]

## 8. Force and acceleration sensitivity

**Question.** Is a quoted sensitivity a measured noise spectral density calibrated with a known force, is it distinguished from the smallest force resolved in a stated integration time, and does the paper address the background forces that can mimic a signal?

**Why it matters.** The thermal limit to force sensitivity depends on temperature, mass and damping, so it inherits the mass and calibration uncertainties above. Averaging improves resolution only until drifts in laser pointing, power or polarisation take over. Near surfaces, residual charge, permanent dipoles, patch potentials, Casimir forces, vibrations and electrical pickup can produce forces at the signal frequency.

**Resolved by.** A force spectrum calibrated by a known applied force and compared with the expected thermal and measurement noise; the integration time and an Allan-type analysis of drifts reported; charge state controlled and stated; each relevant background modelled, measured or bounded at the signal frequency.

**Benchmark.** [1], [6], [14]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | E. Hebestreit et al., Calibration and energy measurement of optically levitated nanoparticle sensors, Rev. Sci. Instrum. 89, 033111 (2018); read as preprint arXiv:1711.09049, which carries a different title | doi:10.1063/1.5017119 |
| 2 | J. Gieseler et al., Optical tweezers — from calibration to applications: a tutorial, Adv. Opt. Photon. 13, 74 (2021); read as preprint arXiv:2004.05246, which carries a different title | doi:10.1364/AOP.394888 |
| 3 | K. Berg-Sørensen and H. Flyvbjerg, Power spectrum analysis for optical tweezers, Rev. Sci. Instrum. 75, 594 (2004) | doi:10.1063/1.1645654 |
| 4 | K. Berg-Sørensen et al., Power spectrum analysis for optical tweezers. II: Laser wavelength dependence of parasitic filtering, and how to achieve high bandwidth, Rev. Sci. Instrum. 77, 063106 (2006); read as arXiv:physics/0603073 | doi:10.1063/1.2204589 |
| 5 | J. Gieseler et al., Thermal nonlinearities in a nanomechanical oscillator, Nat. Phys. 9, 806 (2013); read as preprint arXiv:1307.4684 | doi:10.1038/nphys2798 |
| 6 | F. Ricci et al., Accurate mass measurement of a levitated nanomechanical resonator for precision force-sensing, Nano Lett. 19, 6711 (2019); read as preprint arXiv:1812.11645 | doi:10.1021/acs.nanolett.9b00082 |
| 7 | F. Tebbenjohanns et al., Cold damping of an optically levitated nanoparticle to microkelvin temperatures, Phys. Rev. Lett. 122, 223601 (2019); read as preprint arXiv:1812.09875 | doi:10.1103/PhysRevLett.122.223601 |
| 8 | L. Magrini et al., Real-time optimal quantum control of mechanical motion at room temperature, Nature 595, 373 (2021); read as preprint arXiv:2012.15188 | doi:10.1038/s41586-021-03602-3 |
| 9 | F. Tebbenjohanns et al., Motional sideband asymmetry of a nanoparticle optically levitated in free space, Phys. Rev. Lett. 124, 013603 (2020); read as preprint arXiv:1908.05079 | doi:10.1103/PhysRevLett.124.013603 |
| 10 | A. H. Safavi-Naeini et al., Laser noise in cavity-optomechanical cooling and thermometry, New J. Phys. 15, 035007 (2013); read as preprint arXiv:1210.2671 | doi:10.1088/1367-2630/15/3/035007 |
| 11 | F. Tebbenjohanns et al., Optimal position detection of a dipolar scatterer in a focused field, Phys. Rev. A 100, 043821 (2019); read as preprint arXiv:1907.12838 | doi:10.1103/PhysRevA.100.043821 |
| 12 | V. Jain et al., Direct measurement of photon recoil from a levitated nanoparticle, Phys. Rev. Lett. 116, 243601 (2016); read as preprint arXiv:1603.03420 | doi:10.1103/PhysRevLett.116.243601 |
| 13 | C. Gonzalez-Ballestero et al., Levitodynamics: levitation and control of microscopic objects in vacuum, Science 374, eabg3027 (2021); read as preprint arXiv:2111.05215 | doi:10.1126/science.abg3027 |
| 14 | D. C. Moore and A. A. Geraci, Searching for new physics using optically levitated sensors, Quantum Sci. Technol. 6, 014008 (2021); read as preprint arXiv:2008.13197 | doi:10.1088/2058-9565/abcf8a |
