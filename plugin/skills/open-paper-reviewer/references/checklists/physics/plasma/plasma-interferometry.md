---
id: T-PLASMA-INTERFEROMETRY
name: Interferometry and reflectometry
type: technique
field: physics/plasma
applies_when: the paper measures plasma electron density or its fluctuations with microwave, far-infrared or laser interferometry, Faraday or Cotton-Mouton polarimetry, or profile, fluctuation or Doppler reflectometry, or bases a claim on density profiles, line densities or turbulence data from them
version: "0.1"
---

# Interferometry and reflectometry

## 1. Phase tracking and fringe jumps

**Question.** How was the phase followed through multiples of 2π, does the paper say whether fringe jumps occurred in the data it uses (for example during fast density rises, pellet injection, edge-localised modes or disruptions), and how were they detected and corrected?

**Why it matters.** An interferometer measures phase only within one fringe and counts fringes to follow larger changes, so a brief loss of signal or a phase step of more than one fringe leaves a permanent offset of a whole number of fringes in the density. Such jumps are most frequent in exactly the fast events that papers often study, and some remain after automatic correction.

**Resolved by.** The phase detection and fringe-counting method stated; raw phase or signal amplitude shown for the events the claim rests on; the correction method named and checked, for example by a second wavelength, a polarimeter, a geometrically similar chord or a return of the density to its expected value after the plasma ends; any intervals with signal loss marked or excluded.

**Benchmark.** [1], [2], [3], [4]

## 2. Vibration and optical path drifts

**Question.** How were changes in optical path length from vibration and thermal drift of the optics separated from the plasma phase shift, and what residual phase noise, expressed as a line density, remains after compensation?

**Why it matters.** Movement of the optics changes the path length, and for short-wavelength interferometers it can amount to hundreds of fringes over a discharge, so it must be tracked alongside the plasma phase. A second interferometer or a second wavelength removes most of this, but compensation leaves a residual noise that is most important at low and middle densities, where a small density change can be confused with mechanical motion.

**Resolved by.** The compensation scheme described (second wavelength, second interferometer, dispersion interferometer or mechanical isolation); the vibration phase shown alongside the plasma phase for a representative discharge; a residual noise level measured without plasma and quoted as a line density; the smallest claimed density change compared with that residual.

**Benchmark.** [5], [6], [7]

## 3. Refraction and choice of wavelength

**Question.** Does the paper consider refraction of the beam by density gradients in the conditions of the claim, and does it show that the detected signal stays strong enough at the highest densities and steepest gradients used?

**Why it matters.** Density gradients bend the probing beam and can reduce the detected signal or interrupt it for a short time, which produces fringe jumps. The problem grows with density and is worse for longer wavelengths, so a wavelength that suits low-density discharges can fail in the high-density or pellet-fuelled conditions where a claim is made.

**Resolved by.** The wavelength justified against the density range; signal amplitude recorded and shown not to fall below a stated threshold during the events used; where refraction is significant, a comparison with a shorter-wavelength system or an estimate of the beam deflection.

**Benchmark.** [1], [2], [6]

## 4. Line integration and profile reconstruction

**Question.** When a local density or a profile is derived from line-integrated chords, how many chords were used, which inversion method and which symmetry or flux-surface mapping did it assume, and how sensitive is the claimed profile shape to those assumptions?

**Why it matters.** Each chord gives only an integral of density along its path, so a profile is inferred, not measured, and the inversion is ill-posed: Abel inversion assumes axial or flux-surface symmetry, amplifies noise near the axis and can give misleading profiles when the symmetry is not met. In magnetically confined plasmas the result also depends on the magnetic equilibrium used to map the chords onto flux surfaces, and with few chords the profile shape rests largely on the assumed form and the smoothness imposed.

**Resolved by.** The chord geometry shown; the inversion method, regularisation or prior, and equilibrium reconstruction stated; the reconstructed profile tested by recomputing the measured line integrals and by changes in the symmetry assumption, regularisation strength or equilibrium; uncertainty bands that include these choices; features such as hollow profiles or steep gradients checked against an independent profile diagnostic.

**Benchmark.** [1], [4], [7], [8]

## 5. Polarimetry and the plasma model

**Question.** When a density or magnetic quantity is derived from Faraday rotation or the Cotton-Mouton effect, or from interferometric phase in a very hot plasma, which plasma model links the measured polarisation or phase to that quantity, and does the analysis account for coupling between the two polarimetric effects and for finite electron temperature where it matters?

**Why it matters.** Polarimetry gives a line density that does not depend on the measurement history, which makes it a check on fringe counting, but it is less precise than interferometry. Faraday rotation and the Cotton-Mouton effect act together on the beam, and the size of their coupling depends on both effects and on the wavelength. At burning-plasma temperatures relativistic and other finite-temperature corrections to the refractive index affect both interferometry and polarimetry, so a cold-plasma formula can bias the result.

**Resolved by.** The model stated, from the simple linear formulas to a full Stokes or Jones calculation, with the conditions under which the simple form holds; the magnitude of the cross-coupling and of temperature corrections estimated for the plasma parameters of the claim; polarimetric and interferometric line densities compared on the same discharges with the level of agreement stated.

**Benchmark.** [5], [9], [10], [11]

## 6. Reflectometry profile reconstruction

**Question.** For density profiles from reflectometry, how was the group delay calibrated for the transmission line, how was the profile below the first measured cut-off initialised, and what geometry and plasma model did the inversion assume?

**Why it matters.** Reflectometry locates each cut-off layer from the round-trip group delay of a swept frequency, so the whole profile depends on an assumed starting position for the lowest frequency and on removing the delay of the waveguides and antennas. The inversion treats the plasma as a cold slab that varies only along the beam, and density fluctuations and edge-localised modes disturb individual sweeps, so profiles can be precise and still offset from the true position.

**Resolved by.** The waveguide and antenna delay measured and subtracted; the initialisation method stated, with the effect of plausible alternatives on the profile shown; the probing polarisation stated relative to the magnetic field direction; the averaging or rejection of disturbed sweeps described; the profile position compared with an independent diagnostic or the magnetic reconstruction, with any offset quoted.

**Benchmark.** [12], [13]

## 7. Turbulence and flow from fluctuation and Doppler reflectometry

**Question.** When a turbulence amplitude, correlation length or wavenumber spectrum is derived from fluctuation or Doppler reflectometry, or a perpendicular flow velocity or radial electric field from the Doppler shift, does the paper show that the measurement is in the regime where its interpretation holds, state where in the plasma and at which wavenumbers the signal originates and how they were obtained, account for beam alignment, and, for flows, state what it assumes about the phase velocity of the turbulence?

**Why it matters.** The simple one-dimensional link between reflected phase fluctuations and local density fluctuations holds only for small fluctuations and favourable geometry; at larger turbulence levels the response becomes nonlinear, and parts of the signal come from turbulence away from the cut-off. In Doppler reflectometry the spatial and wavenumber resolution depend on the density profile and the beam, and misalignment of the beam with the magnetic field reduces the backscattered power, which affects any amplitude inferred from it. The Doppler shift gives a velocity only after division by the probed perpendicular wavenumber, which is calculated from the beam path and so depends on the density profile and the magnetic equilibrium. The measured velocity is the sum of the E×B drift and the phase velocity of the turbulence, so reading it as a radial electric field assumes the phase velocity is small, which need not hold in steep-gradient regions such as the edge pedestal.

**Resolved by.** The fluctuation level compared with the range where the linear model applies, or a full-wave or beam-tracing synthetic diagnostic used to interpret the data; the location and wavenumber of the measurement calculated by ray or beam tracing in the measured profile, beam geometry and equilibrium, with their resolution and spread, and the velocity uncertainty that follows from uncertainty in the profile; the beam alignment with the field estimated and its effect on the signal power assessed; relative and absolute amplitudes distinguished; the assumption about the turbulence phase velocity stated and supported, for example by comparing different probed wavenumbers or an independent measurement of the radial electric field such as charge-exchange spectroscopy.

**Benchmark.** [14], [15], [16], [17], [18]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | A. Murari et al., Real-time recovery of the electron density from interferometric measurements affected by fringe jumps, Rev. Sci. Instrum. 77, 073505 (2006) | doi:10.1063/1.2219731 |
| 2 | C. Gil et al., Fringe jump analysis and electronic corrections for the Tore Supra far infrared interferometer, Rev. Sci. Instrum. 79, 10E710 (2008) | doi:10.1063/1.2956824 |
| 3 | C. Gil et al., Analysis and improvements of fringe jump corrections by electronics on the JET tokamak far infrared interferometer, Rev. Sci. Instrum. 81, 10D536 (2010) | doi:10.1063/1.3502317 |
| 4 | R. Fischer et al., Integrated Data Analysis and Validation, preprint arXiv:2411.09270 (2024) | doi:10.48550/arXiv.2411.09270 |
| 5 | T. N. Carlstrom and R. T. Snider, Prototype tests of a combined CO2 laser interferometer/polarimeter for ITER (abstract), Rev. Sci. Instrum. 70, 694 (1999) | doi:10.1063/1.1149526 |
| 6 | K. Tanaka et al., Improvements of CO2 laser heterodyne imaging interferometer for electron density profile measurements on LHD, Plasma Fusion Res. 2, S1033 (2007) | doi:10.1585/pfr.2.S1033 |
| 7 | T. Kinoshita et al., Development of two-color laser imaging interferometer using CO2 laser and quantum cascade laser in the Large Helical Device, Plasma Fusion Res. 17, 1402107 (2022) | doi:10.1585/pfr.17.1402107 |
| 8 | P. Tomassini and A. Giulietti, A generalization of Abel inversion to non-axisymmetric density distribution, Opt. Commun. 199, 143 (2001); read as preprint arXiv:physics/0111139 | doi:10.1016/S0030-4018(01)01575-9 |
| 9 | J. Chen et al., Impact of the Cotton–Mouton effect on Faraday polarimetry measurements using circular polarization, Plasma Phys. Control. Fusion 60, 085001 (2018) | doi:10.1088/1361-6587/aac708 |
| 10 | M. Brombin et al., Real-time electron density measurements from Cotton–Mouton effect in JET machine, Rev. Sci. Instrum. 79, 10E718 (2008) | doi:10.1063/1.2956831 |
| 11 | V. V. Mirnov et al., Finite electron temperature effects on interferometric and polarimetric measurements in fusion plasmas, Phys. Plasmas 14, 102105 (2007) | doi:10.1063/1.2790886 |
| 12 | B. Gonçalves et al., Advances, challenges, and future perspectives of microwave reflectometry for plasma position and shape control on future nuclear fusion devices, Sensors 23, 3926 (2023) | doi:10.3390/s23083926 |
| 13 | C. Laviron et al., Reflectometry techniques for density profile measurements on fusion plasmas, Plasma Phys. Control. Fusion 38, 905 (1996) | doi:10.1088/0741-3335/38/7/002 |
| 14 | R. Nazikian et al., A tutorial on the basic principles of microwave reflectometry applied to fluctuation measurements in fusion plasmas, Phys. Plasmas 8, 1840 (2001) | doi:10.1063/1.1362534 |
| 15 | G. Leclert et al., Full-wave test of the radial correlation reflectometry analytical theory in linear and nonlinear regimes, Plasma Phys. Control. Fusion 48, 1389 (2006) | doi:10.1088/0741-3335/48/9/008 |
| 16 | E. Z. Gusakov and A. V. Surkov, Spatial and wavenumber resolution of Doppler reflectometry, Plasma Phys. Control. Fusion 46, 1143 (2004); read as preprint arXiv:physics/0410107 | doi:10.1088/0741-3335/46/7/012 |
| 17 | V. H. Hall-Chen et al., Effect of mismatch on Doppler backscattering in MAST and MAST-U plasmas, preprint arXiv:2211.17141 (2022) | doi:10.48550/arXiv.2211.17141 |
| 18 | G. D. Conway et al., Plasma rotation profile measurements using Doppler reflectometry, Plasma Phys. Control. Fusion 46, 951 (2004) | doi:10.1088/0741-3335/46/6/003 |
