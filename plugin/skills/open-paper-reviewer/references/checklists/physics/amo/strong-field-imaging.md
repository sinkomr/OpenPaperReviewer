---
id: T-STRONG-FIELD-IMAGING
name: Strong-field ionization and momentum imaging
type: technique
field: physics/amo
applies_when: the paper reports electron or ion momentum distributions, yields or coincidences from strong-field or multiphoton ionisation, measured by velocity-map imaging, a reaction microscope or another coincidence spectrometer, or bases a claim on laser peak intensity, intensity dependence or correlated fragment momenta
version: "0.1"
---

# Strong-field ionization and momentum imaging

## 1. Peak intensity calibration

**Question.** How was the peak intensity at the target determined, and was it checked in situ against a feature of the measured data, such as the drift momentum of ions or electrons in circularly polarised light, the ponderomotive shift of ATI peaks, or a calibrated ion-yield curve?

**Why it matters.** Intensities calculated from pulse energy, pulse duration and focal spot size commonly differ from in-situ values by tens of percent, scaling measured yields to a tunnelling-rate formula has no unique solution, and features such as cutoff energies read from focal-volume-averaged spectra sit below their peak-intensity values, so they underestimate the intensity. Ionisation rates, cutoff energies and the balance between channels depend steeply on intensity, so an error in the intensity scale changes which mechanism or theory the data appear to support.

**Resolved by.** The calibration method and its uncertainty stated; an in-situ calibration with its conditions met, for example intensities below saturation and a target cold enough that its thermal momentum does not mask the drift momentum; the relation between measured pulse energy or power and peak intensity given; any calibration feature taken from intensity-resolved spectra or with focal averaging included in the model; quoted intensities consistent with intensity-dependent features in the spectra; the intensity uncertainty carried into every comparison with theory.

**Benchmark.** [1], [2], [3], [4]

## 2. Focal-volume averaging and saturation

**Question.** Is each comparison with theory made after averaging the calculation over the spatial and temporal intensity distribution of the focus, does the paper give the focal and target geometry needed to do so, and does it say whether ionisation saturates in the intensity range of the claim?

**Why it matters.** A focus contains every intensity from zero to the peak, so a measured spectrum is a sum weighted by the volume at each intensity, and intensity-dependent features such as cutoffs, resonances and shifted lines are smeared or hidden. Above the saturation intensity the target near the peak of the focus is depleted, the yield grows mainly through the growing volume, and the signal can no longer be attributed to the peak intensity.

**Resolved by.** Beam waist, Rayleigh length, target size and any apertures stated; theory averaged over the same focal volume and pulse envelope before comparison; where intensity-dependent structure is claimed, intensity-resolved data, for example detection from a thin slice of the focus, differences between spectra at closely spaced peak intensities, or deconvolution of an intensity scan; the saturation intensity identified from the yield curve and claims above it qualified.

**Benchmark.** [1], [3], [4]

## 3. Velocity-map calibration and image inversion

**Question.** For velocity-map imaging, how was the conversion from radius on the detector to momentum or energy calibrated across the whole image, and when a three-dimensional distribution is reconstructed by inverse Abel transform, does the experiment have the cylindrical symmetry the inversion needs, with the image centre and the inversion method stated?

**Why it matters.** Velocity mapping relies on lens voltages that map equal initial velocities to the same detector point, and the conversion from radius to energy is set by those voltages, so it must be calibrated against reference lines over the radius range used; features near the detector edge are the least well constrained. The inverse Abel transform assumes a distribution that is cylindrically symmetric about an axis parallel to the detector; elliptical polarisation, a tilted axis or a misplaced centre give reconstructions with artefacts, and inversion methods differ in how they handle noise.

**Resolved by.** Lens voltages stated; calibration against lines of known energy, such as ATI peaks separated by one photon energy, over the radius range used, compared with trajectory simulations; the polarisation axis shown to lie in the detector plane; the centring procedure and inversion method, with any regularisation, named; key features shown to be unchanged with a second inversion method; for distributions without cylindrical symmetry, direct three-dimensional detection or tomography instead of Abel inversion.

**Benchmark.** [3], [5], [6], [7]

## 4. Reaction-microscope fields, zero points and resolution

**Question.** For a reaction microscope, how were the electric and magnetic field strengths, the time of flight of zero-momentum particles and the detector centre determined, and what momentum resolution is stated in each direction?

**Why it matters.** Momenta are computed from positions and flight times through the spectrometer fields, so an error in a field or a zero point shifts or stretches every momentum distribution. Electrons whose flight time equals a whole number of cyclotron periods return to the centre and carry no transverse momentum information. The resolution is limited by the size of the interaction volume, timing resolution, field distortions and the internal temperature of the gas jet, which gives a larger momentum spread for heavier targets.

**Resolved by.** Fields calibrated in situ, for example the magnetic field from the spacing of the cyclotron nodes in electron position against flight time, and the momentum scale checked against reference features of known momentum; zero points taken from a symmetry of the process or from a reference measurement; the resolution stated for each axis together with jet temperature and interaction-volume size; claimed features shown to lie away from the cyclotron nodes; for complete events, the momentum sum of the coincident fragments checked against momentum conservation.

**Benchmark.** [1], [8], [9]

## 5. False coincidences and event rate

**Question.** How many ionisation events occurred per laser shot on average, how were false coincidences or spurious covariances estimated and removed, and does the claimed correlation persist when the event rate is reduced?

**Why it matters.** When one shot ionises more than one atom or molecule and the detection efficiency is below one, particles from different events are paired as if they came from the same event and produce correlations that are not in the physics. Covariance analysis tolerates higher rates, but fluctuations of laser intensity or target density create correlations of their own that grow faster than linearly with the event rate.

**Resolved by.** The mean number of events per shot stated and kept well below one, or the false-coincidence contribution estimated and subtracted; true coincidences selected by momentum conservation where the apparatus measures complete events; for covariance or cumulant analysis, the effect of shot-to-shot fluctuations estimated; the main correlation reproduced at a lower event rate, with any spurious part shown to scale as expected with rate.

**Benchmark.** [10], [11]

## 6. Detection efficiency, dead time and multi-hit losses

**Question.** When yields of channels that need different numbers of detected particles are compared, such as double to single ionisation ratios, branching ratios or coincidence fractions, are the detection efficiencies and the detector dead time stated, and are the regions of momentum space where a second particle cannot be registered identified?

**Why it matters.** Each additional particle a channel needs multiplies its detected yield by a detection efficiency below one, so channels with more fragments are suppressed relative to others. A second hit arriving within the dead time of the detector and electronics, typically 10 to 20 ns, is lost, which removes pairs with similar flight times, such as two electrons emitted with similar momenta, from the measured distribution.

**Resolved by.** Detection efficiencies measured or estimated, with corrections and their uncertainties applied to ratios; the dead time stated and the momentum-space regions it excludes marked on the spectra; theory restricted to, or filtered by, the same detector acceptance before comparison.

**Benchmark.** [8], [9], [11]

## 7. Origin of the signal

**Question.** Does the paper show that the counted ions and electrons come from the intended target in the focus, and not from residual gas, contaminant or undissociated species, clusters in the jet, or a detector driven beyond its charge or count-rate limits?

**Why it matters.** Residual gas, such as water vapour and hydrogen, and warm background gas along the laser path ionise in the same focus and add counts that can overlap the signal; contaminant contributions of a few percent are enough to shift an intensity calibration measurably. Cooling a gas jet can form clusters when heavy gases are used, and high ionisation rates can exceed the charge a detector can deliver, which distorts yields at the highest intensities.

**Resolved by.** Background measured with the target off or with the laser outside the jet and subtracted; species selected by mass and charge; contaminant and residual-gas contributions quantified and their effect on derived quantities stated; target density or ionisation rate reduced at high intensity with yields rescaled and the overlap shown; jet conditions stated where cluster formation is possible.

**Benchmark.** [2], [3], [8], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | A. S. Alnaser et al., Laser-peak-intensity calibration using recoil-ion momentum imaging, Phys. Rev. A 70, 023413 (2004) | doi:10.1103/PhysRevA.70.023413 |
| 2 | W. C. Wallace et al., Satya Sainadh U, J. E. Calvert, D. E. Laban, M. G. Pullen, K. Bartschat, A. N. Grum-Grzhimailo, D. Wells, H. M. Quiney, X. M. Tong, I. V. Litvinyuk, R. T. Sang and D. Kielpinski, Precise and accurate measurements of strong-field photoionization and a transferable laser intensity calibration standard, Phys. Rev. Lett. 117, 053001 (2016); read as arXiv:1601.04379 | doi:10.1103/PhysRevLett.117.053001 |
| 3 | J. Wiese et al., Strong-field photoelectron momentum imaging of OCS at finely resolved incident intensities, New J. Phys. 21, 083011 (2019); read as arXiv:1904.07519 | doi:10.1088/1367-2630/ab34e8 |
| 4 | N. A. Hart et al., Intensity-resolved above-threshold ionization of xenon with short laser pulses, Phys. Rev. A 89, 053414 (2014); read as arXiv:1401.6751 | doi:10.1103/PhysRevA.89.053414 |
| 5 | A. T. J. B. Eppink and D. H. Parker, Velocity map imaging of ions and electrons using electrostatic lenses: application in photoelectron and photofragment ion imaging of molecular oxygen, Rev. Sci. Instrum. 68, 3477 (1997) | doi:10.1063/1.1148310 |
| 6 | M. Davino et al., A plano-convex thick-lens velocity map imaging apparatus for direct, high resolution 3D momentum measurements of photoelectrons with ion time-of-flight coincidence, Rev. Sci. Instrum. 94, 013303 (2023); read as arXiv:2209.11690 | doi:10.1063/5.0129900 |
| 7 | D. D. Hickstein et al., A direct comparison of high-speed methods for the numerical Abel transform, Rev. Sci. Instrum. 90, 065115 (2019); read as arXiv:1902.09007 | doi:10.1063/1.5092635 |
| 8 | J. Ullrich et al., Recoil-ion and electron momentum spectroscopy: reaction-microscopes, Rep. Prog. Phys. 66, 1463 (2003) | doi:10.1088/0034-4885/66/9/203 |
| 9 | R. Dörner et al., Cold target recoil ion momentum spectroscopy: a momentum microscope to view atomic collision dynamics, Phys. Rep. 330, 95 (2000) | doi:10.1016/S0370-1573(99)00109-X |
| 10 | P. Heim et al., Bayesian analysis of femtosecond pump-probe photoelectron-photoion coincidence spectra with fluctuating laser intensities, Entropy 21, 93 (2019); read as arXiv:1901.06933 | doi:10.3390/e21010093 |
| 11 | S. Patchkovskii and J. Mikosch, Statistical theory of cumulant mapping in an imperfect apparatus, Phys. Rev. A 111, 043108 (2025); read as arXiv:2412.18439 | doi:10.1103/PhysRevA.111.043108 |
