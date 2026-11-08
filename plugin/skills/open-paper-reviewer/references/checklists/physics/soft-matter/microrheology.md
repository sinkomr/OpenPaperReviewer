---
id: T-MICRORHEOLOGY
name: Particle tracking and microrheology
type: technique
field: physics/soft-matter
applies_when: the paper tracks tracer particles by video microscopy, reports mean-squared displacements, diffusion coefficients or anomalous exponents, or infers viscosity, viscoelastic moduli or heterogeneity of a soft or biological material from passive or active microrheology, including optical or magnetic tweezers
version: "0.1"
---

# Particle tracking and microrheology

## 1. Localization error and the short-lag floor

**Question.** Does the paper state the localization error of the tracking, measured under the same imaging conditions as the experiments, and show that the MSD at the shortest lag times lies well above the floor it sets?

**Why it matters.** Noise in each position adds a constant offset to the MSD. In a stiff or slow sample this offset can be mistaken for a plateau, an elastic modulus or subdiffusion, and it biases fitted diffusion coefficients when the fit forces the intercept.

**Resolved by.** MSDs of particles fixed to a surface, recorded at the same signal-to-noise ratio, exposure and magnification as the experiment; the resulting noise floor drawn on the MSD plots; the static contribution corrected or the lag range restricted to where the signal clearly exceeds it; fits that leave the intercept free.

**Benchmark.** [1], [2], [3]

## 2. Exposure time and motion blur

**Question.** Are the camera exposure time and frame interval stated, and is the effect of motion during the exposure on the short-lag MSD considered?

**Why it matters.** Each frame records the average position over the exposure, which lowers the apparent MSD at lags comparable to the exposure time. Blur and localization noise shift the MSD in opposite directions, so together they can bend its slope at short lags and bias the anomalous exponents, and the high-frequency moduli obtained from them with the GSER.

**Resolved by.** Exposure time, frame rate and number of frames per trajectory reported; exposures short compared with the shortest lag analysed, or a correction for blur applied; a test in a Newtonian fluid of known viscosity showing that the analysis returns a linear MSD and the expected diffusion coefficient over the lag range used.

**Benchmark.** [1], [2], [11]

## 3. Drift and collective motion

**Question.** How was drift of the stage, sample or flow detected and removed, and does the paper show that the correction neither left directed motion in the data nor removed motion that belongs to the sample?

**Why it matters.** Drift adds a directed displacement that grows with lag time, so it distorts the MSD most at long lags, where it can mimic superdiffusion or hide a plateau. Subtracting the mean motion of all particles removes only the part of the drift that they share, and it also removes any real collective motion of the sample. Subtracting each trajectory's own mean displacement pulls its MSD towards zero at long lags.

**Resolved by.** The drift correction described, with the drift itself plotted; evidence that the drift was uniform over the field of view before an ensemble mean was subtracted; results shown with and without correction; where available, two-point microrheology, which is insensitive to motion common to both tracers, used as a cross-check.

**Benchmark.** [3], [4], [11]

## 4. Probe size and interactions between tracer and medium

**Question.** Does the paper give the probe size relative to the structural length scales of the medium, such as mesh or pore size, and the probe surface chemistry, and does it test whether the result changes with either?

**Why it matters.** Probes smaller than the mesh move through the solvent between the strands and report a local, not a bulk, property, while probes that adsorb polymer or protein, or are excluded from a depletion layer around them, couple to the medium in an unknown way. In such cases one-particle microrheology need not reflect the bulk material, and the same medium can appear stiffer or softer depending on the tracer.

**Resolved by.** Probe radius compared with the mesh size or other structural scale; surface treatment stated and chosen to limit adsorption, for example a polymer coating that resists protein binding; results repeated with more than one probe size or surface chemistry; agreement with two-point microrheology, which does not depend on the exact coupling between tracer and medium.

**Benchmark.** [3], [5], [6]

## 5. Generalized Stokes-Einstein relation and its assumptions

**Question.** When moduli or viscosities are obtained from MSDs, does the paper state which form of the GSER was used and check its assumptions for this sample: thermal equilibrium, linear response, a homogeneous, isotropic and incompressible continuum on the probe scale, a no-slip probe surface and negligible inertia?

**Why it matters.** The GSER converts thermal motion into moduli only when these assumptions hold. In a medium driven by internal activity, such as motor proteins in living cells, the fluctuations exceed the thermal prediction and passive data alone cannot give the mechanical properties. Errors in the short-lag MSD also pass through the conversion, for example as apparent elasticity at high frequency.

**Resolved by.** The conversion method and frequency range stated; moduli reported only over lags where the MSD is free of localization, blur and drift artefacts; agreement with bulk rheology in an overlapping frequency range, or with several probe sizes; for active or non-equilibrium systems, an independent active measurement of the response instead of inference from fluctuations alone.

**Benchmark.** [3], [7], [11]

## 6. Heterogeneity and the distribution of probes

**Question.** Does the paper show the distribution of single-particle MSDs or displacements, and not only an ensemble average, and does it state how many probes and locations were sampled before claiming that the material is or is not heterogeneous?

**Why it matters.** An ensemble-averaged MSD from a heterogeneous sample mixes probes in different environments and can look like anomalous diffusion of a single kind. Because the imaging volume and time are finite, the probes sample the material unevenly, which limits how far heterogeneity can be quantified. Non-Gaussian displacements point to heterogeneity in a passive sample, but they can also arise in other ways, so they are not proof on their own.

**Resolved by.** Histograms of individual MSDs or displacement distributions (van Hove functions) compared with those for a homogeneous control fluid with the same tracers; the number of probes, fields of view and samples stated; estimators of heterogeneity that account for the sampling; consistency with two-point measurements, which are insensitive to local heterogeneity.

**Benchmark.** [3], [6], [7], [8], [9]

## 7. Statistics of the mean-squared displacement

**Question.** How many trajectories, of what length, enter each MSD, over what range of lag times is it fitted, and are the error bars and fitted exponents computed in a way that accounts for overlapping displacements and for the difference between time and ensemble averages?

**Why it matters.** MSD points at long lags rest on few, overlapping and correlated displacements, so their uncertainty grows; fitting too many lag points, or quoting error bars that ignore the correlations, misstates the uncertainty of the fitted coefficient or exponent. In several anomalous-diffusion processes the time-averaged MSD of single trajectories differs from the ensemble average and scatters between trajectories, so an exponent from the MSD alone does not identify the process.

**Resolved by.** Trajectory number and length given; the fitted lag range stated and limited to a fraction of the trajectory length, or chosen by a stated rule; uncertainties that account for correlations between MSD points; both time-averaged and ensemble-averaged MSDs shown when an anomalous exponent is claimed, with the scatter between trajectories; further tests, such as displacement distributions or ergodicity-breaking measures, before a mechanism is assigned; tracks classed as confined or directed only against thresholds set from simulated Brownian tracks of the same length and noise, with the fraction of tracks in each class and its sensitivity to the threshold reported.

**Benchmark.** [2], [9], [10], [12]

## 8. Active microrheology: force calibration and linear response

**Question.** For optical or magnetic tweezer measurements, how was the force or trap stiffness calibrated, and does the paper show that the response was measured in the linear regime and, where passive and active data are compared, with the same probe and location?

**Why it matters.** The modulus from an active measurement is only as good as the force calibration, which usually uses a probe of known size in a fluid of known viscosity and holds in the sample only if the probe and optical conditions are the same. Large forces drive the medium out of linear response and give a strain-dependent result, and comparing passive and active data from different probes or regions confounds sample variation with a breakdown of the fluctuation-dissipation relation.

**Resolved by.** The calibration method, reference fluid and probe size stated, with any in-situ check of the calibration; the response shown to be independent of force or displacement amplitude over the range used; for comparisons of passive and active data, both measured on the same probe and location, with the frequency at which they diverge reported.

**Benchmark.** [3], [7]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | T. Savin and P. S. Doyle, Static and dynamic errors in particle tracking microrheology, Biophys. J. 88, 623 (2005) | doi:10.1529/biophysj.104.042457 |
| 2 | X. Michalet, Mean square displacement analysis of single-particle trajectories with localization error: Brownian motion in an isotropic medium, Phys. Rev. E 82, 041914 (2010); read as the author manuscript in PubMed Central (PMC3055791) | doi:10.1103/PhysRevE.82.041914 |
| 3 | Y. Mao et al., Passive and active microrheology for biomedical systems, Front. Bioeng. Biotechnol. 10, 916354 (2022) | doi:10.3389/fbioe.2022.916354 |
| 4 | J. W. R. Mellnik et al., Maximum likelihood estimation for single particle, passive microrheology data with drift, J. Rheol. 60, 379 (2016); read as arXiv:1509.03261 | doi:10.1122/1.4943988 |
| 5 | M. T. Valentine et al., Colloid surface chemistry critically affects multiple particle tracking measurements of biomaterials, Biophys. J. 86, 4004 (2004) | doi:10.1529/biophysj.103.037812 |
| 6 | J. C. Crocker et al., Two-point microrheology of inhomogeneous soft materials, Phys. Rev. Lett. 85, 888 (2000) | doi:10.1103/PhysRevLett.85.888 |
| 7 | F. S. Gnesotto et al., Broken detailed balance and non-equilibrium dynamics in living systems: a review, Rep. Prog. Phys. 81, 066601 (2018); read as preprint arXiv:1710.03456 | doi:10.1088/1361-6633/aab3ed |
| 8 | M. T. Valentine et al., Investigating the microenvironments of inhomogeneous soft materials with multiple particle tracking, Phys. Rev. E 64, 061506 (2001) | doi:10.1103/PhysRevE.64.061506 |
| 9 | T. Savin and P. S. Doyle, Statistical and sampling issues when using multiple particle tracking, Phys. Rev. E 76, 021501 (2007) | doi:10.1103/PhysRevE.76.021501 |
| 10 | R. Metzler et al., Anomalous diffusion models and their properties: non-stationarity, non-ergodicity, and ageing at the centenary of single particle tracking, Phys. Chem. Chem. Phys. 16, 24128 (2014) | doi:10.1039/C4CP03465A |
| 11 | Y. Ling et al., Measurement error correction in particle tracking microrheology, Ann. Appl. Stat. 16, 1747 (2022); read as preprint arXiv:1911.06451 | doi:10.1214/21-AOAS1565 |
| 12 | M. J. Saxton, Lateral diffusion in an archipelago: single-particle diffusion, Biophys. J. 64, 1766 (1993) | doi:10.1016/S0006-3495(93)81548-0 |
