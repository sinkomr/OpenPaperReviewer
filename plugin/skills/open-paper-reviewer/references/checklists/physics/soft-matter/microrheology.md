---
id: T-MICRORHEOLOGY
name: Particle tracking and microrheology
type: technique
field: physics/soft-matter
applies_when: the paper tracks tracer particles by video microscopy, reports mean-squared displacements, diffusion coefficients or anomalous exponents, or infers viscosity, viscoelastic moduli or heterogeneity of a soft or biological material from passive or active microrheology, including optical or magnetic tweezers
version: "0.1"
---

# Particle tracking and microrheology

Video particle tracking (VPT) follows embedded tracer particles and is used to claim diffusion coefficients, anomalous or confined motion, and, through the generalized Stokes-Einstein relation (GSER), local viscosity and viscoelastic moduli. Passive microrheology infers these from thermal motion alone; active microrheology drives the probe with optical or magnetic tweezers and measures its response. Both rest on mean-squared displacements (MSDs) or response functions built from noisy, finite trajectories.

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

**Resolved by.** Trajectory number and length given; the fitted lag range stated and limited to a fraction of the trajectory length, or chosen by a stated rule; uncertainties that account for correlations between MSD points; both time-averaged and ensemble-averaged MSDs shown when an anomalous exponent is claimed, with the scatter between trajectories; further tests, such as displacement distributions or ergodicity-breaking measures, before a mechanism is assigned.

**Benchmark.** [2], [9], [10]

## 8. Active microrheology: force calibration and linear response

**Question.** For optical or magnetic tweezer measurements, how was the force or trap stiffness calibrated, and does the paper show that the response was measured in the linear regime and, where passive and active data are compared, with the same probe and location?

**Why it matters.** The modulus from an active measurement is only as good as the force calibration, which usually uses a probe of known size in a fluid of known viscosity and holds in the sample only if the probe and optical conditions are the same. Large forces drive the medium out of linear response and give a strain-dependent result, and comparing passive and active data from different probes or regions confounds sample variation with a breakdown of the fluctuation-dissipation relation.

**Resolved by.** The calibration method, reference fluid and probe size stated, with any in-situ check of the calibration; the response shown to be independent of force or displacement amplitude over the range used; for comparisons of passive and active data, both measured on the same probe and location, with the frequency at which they diverge reported.

**Benchmark.** [3], [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | T. Savin and P. S. Doyle, Static and dynamic errors in particle tracking microrheology, Biophys. J. 88, 623–638 (2005) | doi:10.1529/biophysj.104.042457 | abstract | Abstract: localization error in the MSD has two parts, a static error seen in the positions of immobilized particles and a dynamic error from motion during the finite exposure; the static part can be corrected using static measurements made at a similar noise-to-signal ratio |
| 2 | X. Michalet, Mean square displacement analysis of single-particle trajectories with localization error: Brownian motion in an isotropic medium, Phys. Rev. E 82, 041914 (2010); read as the author manuscript in PubMed Central (PMC3055791) | doi:10.1103/PhysRevE.82.041914 | full text | Sec. 2: localization error adds a positive MSD offset and finite exposure can make it negative; forcing the intercept to be positive biases the diffusion coefficient. Secs. 3 and 4: long-lag MSD points rest on fewer displacements and are noisier. Sec. 5: MSD points are correlated and there is an optimal number of points to fit, set by the reduced localization error. Sec. 6: localization uncertainty estimated from immobilized probes recorded under the same conditions as the diffusing ones |
| 3 | Y. Mao, P. Nielsen and J. Ali, Passive and active microrheology for biomedical systems, Front. Bioeng. Biotechnol. 10, 916354 (2022) | doi:10.3389/fbioe.2022.916354 | full text | Passive Microrheology: GSER assumes a homogeneous, isotropic, incompressible continuum, equilibrium, linear response, negligible inertia and no slip; static error measured with fixed beads and dynamic error from the camera exposure. General Considerations: probes smaller than the mesh report the interstitial fluid; check against bulk rheology and with several probe sizes and surface chemistries; carboxylated particles adsorb protein; two-point analysis reduces collective motion and vibration, and pair motion reveals drift; non-Gaussian displacements and van Hove analysis indicate heterogeneity. Active Microrheology: trap stiffness or magnetic force calibrated with a probe of known size in a fluid of known viscosity; passive methods suit equilibrium, linear systems |
| 4 | J. W. R. Mellnik, M. Lysy, P. A. Vasquez, N. S. Pillai, D. B. Hill, J. Cribb, S. A. McKinley and M. G. Forest, Maximum likelihood estimation for single particle, passive microrheology data with drift, J. Rheol. 60, 379 (2016); read as arXiv:1509.03261 | doi:10.1122/1.4943988 | abstract | Abstract: drift is non-diffusive and, when large compared with diffusive mobility, distorts MSD statistics; the standard practice estimates and subtracts drift before computing MSDs, and the paper proposes fitting drift and diffusion together instead |
| 5 | M. T. Valentine, Z. E. Perlman, M. L. Gardel, J. H. Shin, P. Matsudaira, T. J. Mitchison and D. A. Weitz, Colloid surface chemistry critically affects multiple particle tracking measurements of biomaterials, Biophys. J. 86, 4004–4014 (2004) | doi:10.1529/biophysj.103.037812 | full text | Introduction and Fig. 1: probes larger than the mesh report bulk viscoelasticity, smaller probes sample local microenvironments. Results: tracers with different surface chemistry adsorb different amounts of protein and report different mobilities and moduli in the same networks; two-particle analysis removes most of the difference (Fig. 7). Summary: effects of particle size and surface chemistry need to be studied for each new material |
| 6 | J. C. Crocker, M. T. Valentine, E. R. Weeks, T. Gisler, P. D. Kaplan, A. G. Yodh and D. A. Weitz, Two-point microrheology of inhomogeneous soft materials, Phys. Rev. Lett. 85, 888 (2000) | doi:10.1103/PhysRevLett.85.888 | abstract | Abstract: cross-correlating the motion of tracer pairs gives moduli independent of the exact coupling between tracer and medium and accurate for inhomogeneous materials; conventional one-particle microrheology may not reflect bulk behaviour |
| 7 | F. S. Gnesotto, F. Mura, J. Gladrow and C. P. Broedersz, Broken detailed balance and non-equilibrium dynamics in living systems: a review, Rep. Prog. Phys. 81, 066601 (2018); read as preprint arXiv:1710.03456 | doi:10.1088/1361-6633/aab3ed | full text | Sec. II: the fluctuation-dissipation theorem links fluctuations and response at equilibrium, and driven systems generally violate it. Sec. II.1: passive microrheology assumes it and the GSER and cannot by itself give the mechanics of non-equilibrium systems; active microrheology applies a force to the probe and, in the linear regime, obtains the response from displacement over force. Sec. II.2: in active gels fluctuations exceed the prediction at low frequency; non-Gaussian statistics are not a reliable marker of activity. Sec. II.3: same probe and location used for passive and active data; results depending on probe size |
| 8 | M. T. Valentine, P. D. Kaplan, D. Thota, J. C. Crocker, T. Gisler, R. K. Prud'homme, M. Beck and D. A. Weitz, Investigating the microenvironments of inhomogeneous soft materials with multiple particle tracking, Phys. Rev. E 64, 061506 (2001) | doi:10.1103/PhysRevE.64.061506 | abstract | Abstract: because imaging volume and time are limited, statistical methods based on the distribution of particle displacements are needed to compare individual particles and characterize differences between microenvironments |
| 9 | T. Savin and P. S. Doyle, Statistical and sampling issues when using multiple particle tracking, Phys. Rev. E 76, 021501 (2007) | doi:10.1103/PhysRevE.76.021501 | abstract | Abstract: the finite observation volume makes sampling in heterogeneous systems unusual; estimators for the mean and variance of probe dynamics are derived; heterogeneity can be quantified only as far as the probes sample the material; careful assessment of statistics is needed for unbiased results |
| 10 | R. Metzler, J.-H. Jeon, A. G. Cherstvy and E. Barkai, Anomalous diffusion models and their properties: non-stationarity, non-ergodicity, and ageing at the centenary of single particle tracking, Phys. Chem. Chem. Phys. 16, 24128–24164 (2014) | doi:10.1039/C4CP03465A | abstract | Abstract: in several anomalous-diffusion models the time-averaged MSD differs from the ensemble-averaged MSD, so time averages cannot be read with ensemble results; the scatter of time-averaged MSD amplitudes and ergodicity-breaking parameters are compared between processes |
| 11 | Y. Ling, M. Lysy, I. Seim, J. M. Newby, D. B. Hill, J. Cribb and M. G. Forest, Measurement error correction in particle tracking microrheology, Ann. Appl. Stat. 16, 1747–1773 (2022); read as preprint arXiv:1911.06451 | doi:10.1214/21-AOAS1565 | full text | Abstract and Sec. 1: high-frequency instrumental noise biases the power-law MSD parameters that give viscous and elastic properties, and inadequate correction can severely bias them. Sec. 2.3: static noise raises and longer exposure lowers the MSD at the shortest lags. Sec. 2.1: subtracting the mean displacement to remove drift biases the empirical MSD towards zero at long lags |
