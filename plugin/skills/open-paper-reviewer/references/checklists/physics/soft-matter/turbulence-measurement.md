---
id: T-TURBULENCE-MEASUREMENT
name: Turbulence measurement
type: technique
field: physics/soft-matter
applies_when: the paper measures a turbulent flow with particle image velocimetry, particle tracking, laser Doppler or hot-wire anemometry, or reports turbulence spectra, structure functions, dissipation rates, scaling exponents, acceleration statistics or a turbulence Reynolds number from such data
version: "0.1"
---

# Turbulence measurement

Particle image velocimetry (PIV), particle tracking velocimetry (PTV, also Lagrangian particle tracking), laser Doppler anemometry (LDA) and hot-wire anemometry (HWA) are used to claim velocity statistics, spectra, structure functions, accelerations, dissipation rates and scaling laws of turbulent flows, often as functions of a Reynolds number. Each instrument averages over a finite volume and time, samples the flow through tracers or a sensor, and records a finite stretch of a random signal, and each of these limits the small-scale and high-order quantities on which such claims rest.

## 1. Spatial resolution against the smallest scales

**Question.** Does the paper give the size of the measuring volume (hot-wire sensing length, PIV interrogation window and vector spacing, laser Doppler probe volume) in units of the Kolmogorov length, or of the viscous length in wall-bounded flows, and does it account for the attenuation this causes in the quantities it reports?

**Why it matters.** A probe averages over its measuring volume, so motions smaller than it are attenuated: high-wavenumber spectra, velocity gradients, vorticity and dissipation come out too low. Because the Kolmogorov length shrinks as the Reynolds number grows, a fixed sensor resolves less at higher Reynolds number, and a change caused by resolution can be read as a Reynolds-number trend.

**Resolved by.** Sensor length, window size, overlap and vector spacing stated in Kolmogorov or viscous units for every condition; comparisons across Reynolds number made at matched resolution or with a stated correction; where the small scales are not resolved, the correction or subgrid model named and checked against an independent estimate.

**Benchmark.** [1], [2], [3]

## 2. Temporal resolution and the frozen-turbulence approximation

**Question.** Are the sampling rate and frequency response (anemometer bandwidth, camera frame rate, laser Doppler data rate) stated relative to the Kolmogorov time or the highest frequency in the flow, and, where time series are turned into spatial statistics with Taylor's frozen-turbulence hypothesis, does the paper say which convection velocity was used and why the approximation holds?

**Why it matters.** A signal sampled or filtered too slowly loses the small-scale content, and particle accelerations need several samples per Kolmogorov time. Taylor's hypothesis with a single convection velocity misplaces scales that travel at other speeds, which shifts spectral content in wavenumber and can create spurious spectral peaks, more so near walls and at high Reynolds number.

**Resolved by.** Frame rate or bandwidth given in units of the Kolmogorov time or compared with a stated maximum flow frequency; the convection velocity and the turbulence intensity reported; where the conversion is doubtful, a comparison with directly measured spatial statistics or a correction for scale-dependent convection.

**Benchmark.** [1], [4], [5], [6]

## 3. Tracer fidelity and seeding

**Question.** For PIV, PTV and LDA, does the paper give the tracer size and density as measured, and the Stokes number (particle response time over Kolmogorov time) and the ratio of particle size to Kolmogorov length for each flow condition, and does it describe the seeding?

**Why it matters.** Tracers follow the flow only if they respond faster than the smallest flow time scale and are smaller than the smallest eddies; larger particles show smaller accelerations than fluid particles, and particles that are heavier or lighter than the fluid sample it unevenly. The Stokes number of a given particle grows with the Reynolds number, so a tracer that is adequate at one condition may not be at the highest one. Inertial particles also concentrate preferentially in parts of the flow, and dense seeding raises the rate of tracking errors.

**Resolved by.** Particle diameter and density measured, not only quoted from a supplier; Stokes number and size ratio stated for every condition and small throughout; settling, buoyancy and particle charge considered; seeding density stated; where possible, a check that results do not change with tracer size.

**Benchmark.** [4], [6], [7]

## 4. Noise, filtering and differentiation of particle data

**Question.** How were particle positions or PIV displacements filtered and differentiated to obtain velocities, gradients or accelerations, does the paper show that the reported statistics do not depend on the filter length and that the contribution of measurement noise was estimated and removed, and, for PIV, was bias of displacements towards whole pixels (peak locking) checked?

**Why it matters.** Differentiation amplifies position noise, so at short filter lengths the variance and flatness of accelerations or gradients mostly reflect the noise, while long filters remove real signal. Filters that discard samples near the ends of tracks drop short tracks, which tend to carry intense events, and bias the variance low; tracking errors produce spurious large values. In PIV, peak locking leaves the mean velocity little changed but distorts fluctuating quantities such as the rms velocity.

**Resolved by.** Filter type and length stated in Kolmogorov units; the statistic plotted against filter length, with any extrapolation to zero filter length described; the noise estimated independently, for example from separate cameras, and its contribution subtracted; the handling of track ends, gaps and outliers described; for PIV, the peak-locking error assessed, for example by repeating the measurement with different pulse separations, and corrected or shown to be small.

**Benchmark.** [4], [7], [15]

## 5. Laser Doppler sampling bias

**Question.** For laser Doppler data, does the paper say how it corrected averages and moments for the bias that arises because particle arrivals are correlated with the velocity, and does it give the probe-volume size and data rate against the flow scales?

**Why it matters.** More particles cross the probe volume when the flow is fast than when it is slow, so a plain average of individual realisations is weighted towards high speeds. The finite probe volume, the particle transit time and velocity gradients across the volume broaden the Doppler signal and limit the spatial and temporal resolution.

**Resolved by.** The weighting scheme (for example inverse-velocity or transit-time weighting) stated and its effect on the reported statistics shown; the data rate compared with the flow time scales; probe-volume dimensions compared with the Kolmogorov and integral scales.

**Benchmark.** [3], [8]

## 6. Convergence of turbulence statistics

**Question.** Does the paper give, for each statistic, the record length in integral time scales or the number of statistically independent samples or fields, and does it show that higher moments, probability density tails and high-order structure functions are converged?

**Why it matters.** The random error of a turbulence statistic falls with the square root of the effective number of independent samples, which can be far smaller than the number of samples when these are correlated in time or space. Higher moments depend on rare, intense events, and even modest intermittency makes inertial-range structure functions unreliable from typical records at orders as low as five or six.

**Resolved by.** The integral time or length scale and the resulting number of independent samples stated; uncertainties of means and Reynolds stresses based on that number; convergence shown for higher moments, for example through the integrand of the moment plotted against amplitude or the moment against record length; the highest order reported limited to what the record supports.

**Benchmark.** [9], [10]

## 7. Dissipation rate and the definition of the Reynolds number

**Question.** Which method gave the dissipation rate (direct velocity gradients, a fit to a structure function or spectrum with an assumed constant, a subgrid model, or a scaling with velocity cubed over an integral length), which assumptions does it need, and does the paper define its Reynolds number (velocity, length scale and formula, for example for the Taylor-microscale Reynolds number) together with the dissipation estimate it uses?

**Why it matters.** Dissipation methods disagree with each other and depend on the resolution, on isotropy, on the extent of an inertial range and on the constants assumed. The dissipation rate scaled by the integral length and velocity is not a universal constant: it depends on the forcing and large-scale structure, and it varies in non-equilibrium flows even where the spectrum shows the expected power law. Reynolds numbers, Kolmogorov scales and normalised results computed from the dissipation inherit these errors, and formulas for the Taylor-microscale Reynolds number based on the dissipation or on an integral length agree only if that scaling holds.

**Resolved by.** The method, constants and corrections for resolution and low Reynolds number stated; two or more methods compared, or the estimate checked against an independent global value such as the measured power input or torque; definitions of the Reynolds number, Kolmogorov length and time given with the dissipation value they use, so that results can be compared with other flows.

**Benchmark.** [2], [4], [11], [12], [13]

## 8. Scaling ranges and exponents

**Question.** When the paper claims a scaling exponent or a Kolmogorov-type law, does it show the range of scales used for the fit, justify that range as an inertial or other scaling range at the stated Reynolds number, and report how the exponent changes with the fit range?

**Why it matters.** At laboratory Reynolds numbers the scaling range is short, and finite Reynolds number, decay and inhomogeneity distort it, so laws such as the four-fifths law are approached at different rates in different flows. Limited spatial resolution and the frozen-turbulence approximation also bend measured spectra, and exponents of high-order moments are limited by statistical convergence.

**Resolved by.** Compensated plots showing the plateau the exponent rests on; the fit range given in units of the Kolmogorov and integral scales; exponents with uncertainties that include their sensitivity to the fit range; trends checked across Reynolds number; high-order exponents limited to orders the data support.

**Benchmark.** [1], [5], [10], [14]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | N. Hutchins, T. B. Nickels, I. Marusic and M. S. Chong, Hot-wire spatial resolution issues in wall-bounded turbulence, J. Fluid Mech. 635, 103–136 (2009) | doi:10.1017/S0022112009007721 | abstract | Abstract: scatter in the near-wall intensity peak comes from Reynolds number and viscous-scaled wire length together, which led earlier studies to wrong conclusions about Reynolds-number dependence; an apparent outer peak is an artefact of long wires; a maximum flow frequency criterion for time response; wire length erodes part of the spectrum and Kolmogorov-scaled spectra are significantly affected by spatial resolution |
| 2 | S. Tokgoz, G. E. Elsinga, R. Delfos and J. Westerweel, Spatial resolution and dissipation rate estimation in Taylor–Couette flow for tomographic PIV, Exp. Fluids 53, 561–583 (2012) | doi:10.1007/s00348-012-1311-7 | abstract | Abstract (TU Delft research portal): resolution is set by the interrogation volume size; dissipation from PIV checked against a torque-based value; at the highest Reynolds number only a small part of the dissipation is resolved and a subgrid model is needed; overlap ratio changes the dissipation estimate |
| 3 | W. K. George and J. L. Lumley, The laser-Doppler velocimeter and its application to the measurement of turbulence, J. Fluid Mech. 60, 321–362 (1973) | doi:10.1017/S0022112073000194 | abstract | Abstract: Doppler ambiguity arises from finite transit time, turbulence across the measuring volume, mean gradients and noise; the sampling volume limits spatial and temporal resolution |
| 4 | G. A. Voth, A. La Porta, A. M. Crawford, J. Alexander and E. Bodenschatz, Measurement of particle accelerations in fully developed turbulence, J. Fluid Mech. 469, 121–160 (2002); read as preprint arXiv:physics/0110027 | doi:10.1017/S0022112002001842 | full text | Sec. 1: the Kolmogorov time must be resolved to measure accelerations, and relatively large particles have smaller accelerations than fluid particles. Sec. 2.3: tracers must be small and closely density matched to avoid sampling bias. Sec. 3.3: definition of the Taylor-microscale Reynolds number via dissipation, with an alternative form using an integral length; dissipation from a structure-function fit with an assumed constant. Sec. 4.2: acceleration variance depends strongly on the fit window, overestimated by short fits through noise and underestimated by long ones, with extrapolation to zero window |
| 5 | J. C. del Álamo and J. Jiménez, Estimation of turbulent convection velocities and corrections to Taylor's approximation, J. Fluid Mech. 640, 5–26 (2009) | doi:10.1017/S0022112009991029 | abstract | Abstract: small and large scales convect at different speeds; Taylor's approximation shifts near-wall large scales to apparently shorter wavelengths and can create spurious spectral peaks, more so at higher Reynolds number; a correction for experimental spectra is given |
| 6 | C. Küchler, A. Ibanez Landeta, J. Moláček and E. Bodenschatz, Lagrangian particle tracking at large Reynolds numbers, Rev. Sci. Instrum. 95, 105110 (2024); read as preprint arXiv:2404.04215 | doi:10.1063/5.0211508 | full text | Sec. I: imaging needs more than about ten frames per Kolmogorov time. Sec. III and Fig. 1: Stokes number defined as particle response time over Kolmogorov time, particle size compared with the Kolmogorov length, density measured and found well below the bulk material value, Stokes number rising with Reynolds number so that tracers stay suitable only up to a limit; particle charge assessed |
| 7 | J. M. Lawson, E. Bodenschatz, C. C. Lalescu and M. Wilczek, Bias in particle tracking acceleration measurement, Exp. Fluids 59, 172 (2018); read as preprint arXiv:1805.12440 | doi:10.1007/s00348-018-2622-0 | full text | Sec. 1 and 4.1: acceleration is very sensitive to position noise, which dominates variance and flatness at short filter scales, while long filters remove signal; convolution filters drop samples near track ends and under-represent short tracks with large accelerations; tracking errors give spurious large values, reduced by lower seeding density or a higher frame rate; small density-matched tracers are recommended against preferential concentration and finite-size effects. Secs. 2.1 and 6: noise estimated from independent camera measurements and removed; filter scales chosen so they do not affect results |
| 8 | D. K. McLaughlin and W. G. Tiederman, Biasing correction for individual realization of laser anemometer measurements in turbulent flows, Phys. Fluids 16, 2082–2088 (1973) | doi:10.1063/1.1694269 | abstract | Abstract: more scattering particles cross the probe volume during fast periods than slow ones, biasing individual-realisation statistics; weighting by the inverse of the instantaneous velocity corrects it |
| 9 | A. Sciacchitano and B. Wieneke, PIV uncertainty propagation, Meas. Sci. Technol. 27, 084006 (2016) | doi:10.1088/0957-0233/27/8/084006 | abstract | Abstract: the uncertainty of mean values and Reynolds stresses is often dominated by finite sample size and falls with the square root of the effective number of independent samples |
| 10 | T. Dudok de Wit, Can high-order moments be meaningfully estimated from experimental turbulence measurements?, Phys. Rev. E 70, 055302 (2004) | doi:10.1103/PhysRevE.70.055302 | abstract | Abstract: moments of finite samples become unreliable above some order; an empirical criterion for that order; even with modest intermittency, inertial-range structure functions cannot be meaningfully assessed at orders as low as 5 or 6 |
| 11 | J. de Jong, L. Cao, S. H. Woodward, J. P. L. C. Salazar, L. R. Collins and H. Meng, Dissipation rate estimation from PIV in zero-mean isotropic turbulence, Exp. Fluids 46, 499–515 (2009) | doi:10.1007/s00348-008-0576-3 | abstract | Abstract (University at Buffalo research portal): no consensus on the best PIV method for dissipation; five methods compared and their dependence on interrogation cell size examined; corrections for measurement uncertainty, finite resolution and low Reynolds number evaluated |
| 12 | K. R. Sreenivasan, An update on the energy dissipation rate in isotropic turbulence, Phys. Fluids 10, 528–529 (1998) | doi:10.1063/1.869575 | abstract | Abstract: the dissipation rate scaled by integral length and rms velocity tends to a constant of order one at high Reynolds number, but its value depends on the large-scale forcing or flow structure |
| 13 | J. C. Vassilicos, Dissipation in turbulent flows, Annu. Rev. Fluid Mech. 47, 95–114 (2015) | doi:10.1146/annurev-fluid-010814-014637 | abstract | Abstract: many flows have a non-equilibrium region where the spectrum follows the -5/3 law over a wide range yet the dissipation coefficient is not constant, varying with global and local Reynolds numbers |
| 14 | R. A. Antonia and P. Burattini, Approach to the 4/5 law in homogeneous isotropic turbulence, J. Fluid Mech. 550, 175–184 (2006) | doi:10.1017/S0022112005008438 | abstract | Abstract: in laboratory flows finite Reynolds number and large-scale non-stationarity or inhomogeneity affect inertial-range behaviour; the 4/5 value is approached much faster in forced than in decaying turbulence |
| 15 | J. Nogueira, M. Legrand, R. Jiménez and F. De Gregorio, Peak-locking full characterization: PIV error assessment and velocity ensemble measurement correction, Meas. Sci. Technol. 32, 114005 (2021) | doi:10.1088/1361-6501/ac092a | abstract | Abstract (UC3M research portal): peak-locking error in PIV is calibrated by measuring the same flow with subsets of different time separations, and the local mean and rms velocities are corrected, the rms error almost completely |
