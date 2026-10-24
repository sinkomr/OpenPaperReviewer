---
id: T-STRONG-FIELD-IMAGING
name: Strong-field ionization and momentum imaging
type: technique
field: physics/amo
applies_when: the paper reports electron or ion momentum distributions, yields or coincidences from strong-field or multiphoton ionisation, measured by velocity-map imaging, a reaction microscope or another coincidence spectrometer, or bases a claim on laser peak intensity, intensity dependence or correlated fragment momenta
version: "0.1"
---

# Strong-field ionization and momentum imaging

Velocity-map imaging (VMI), reaction microscopes based on cold target recoil-ion momentum spectroscopy (COLTRIMS) and other coincidence spectrometers are used to claim ionisation yields and rates, photoelectron and ion momentum distributions, above-threshold ionisation (ATI) structure and cutoffs, and correlations between fragments, usually as functions of laser peak intensity. These claims rest on an intensity scale, a model of the laser focus, a conversion from detector position and time of flight to momentum, and the correct assignment of detected particles to single ionisation events.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | A. S. Alnaser, X. M. Tong, T. Osipov, S. Voss, C. M. Maharjan, B. Shan, Z. Chang and C. L. Cocke, Laser-peak-intensity calibration using recoil-ion momentum imaging, Phys. Rev. A 70, 023413 (2004) | doi:10.1103/PhysRevA.70.023413 | full text | Sec. I: intensities from laser parameters or from normalising yields to tunnelling-rate calculations have large errors; spatial intensity variation hides observables when integrated over the focus. Sec. II: yield written as rate times focal-volume factor, below saturation. Sec. III: a cold target is essential, since thermal momentum of a warm target masks the drift momentum. Sec. IV: in-situ calibration from ion drift momentum in circular polarisation applied below saturation; fitting yields to tunnelling theory has no unique scaling and agrees only within 30%; peak intensity related linearly to measured power. Sec. V: accuracy of about 10% |
| 2 | W. C. Wallace, O. Ghafur, C. Khurmi, Satya Sainadh U, J. E. Calvert, D. E. Laban, M. G. Pullen, K. Bartschat, A. N. Grum-Grzhimailo, D. Wells, H. M. Quiney, X. M. Tong, I. V. Litvinyuk, R. T. Sang and D. Kielpinski, Precise and accurate measurements of strong-field photoionization and a transferable laser intensity calibration standard, Phys. Rev. Lett. 117, 053001 (2016); read as arXiv:1601.04379 | doi:10.1103/PhysRevLett.117.053001 | full text | Text around Eqs. 1–2: focal-volume averaging applied to theory before fitting; intensity estimated from waist, power, duration and repetition rate needed rescaling by a factor of about 0.64, and such estimates can be uncertain by up to about 50%; signals from undissociated hydrogen and background water vapour reached 9.5% of the yield, and leaving them in shifted the calibration by 3.1%. Discussion of Fig. 1: simple tunnelling-rate theory deviates by up to a factor of two at high intensity |
| 3 | J. Wiese, J.-F. Olivieri, A. Trabattoni, S. Trippel and J. Küpper, Strong-field photoelectron momentum imaging of OCS at finely resolved incident intensities, New J. Phys. 21, 083011 (2019); read as arXiv:1904.07519 | doi:10.1088/1367-2630/ab34e8 | full text | Abstract and Sec. II: differences of momentum distributions with respect to peak intensity strongly suppress focal-volume averaging. Sec. III: intensity from beam profile, autocorrelation and pulse energy was 20% low compared with the ponderomotive shift of ATI peaks; the photon-energy spacing of ATI peaks calibrates momentum; above a set intensity the sample density was cut to a third because of the detector's charge-dissipation limit; momenta recovered by inverse Abel transform. Sec. IV A: saturation onset read from the yield against the logarithm of intensity |
| 4 | N. A. Hart, J. Strohaber, G. Kaya, N. Kaya, A. A. Kolomenskii and H. A. Schuessler, Intensity-resolved above-threshold ionization of xenon with short laser pulses, Phys. Rev. A 89, 053414 (2014); read as arXiv:1401.6751 | doi:10.1103/PhysRevA.89.053414 | full text | Sec. I: the focus contains a continuum of intensities, so averaging lowers intensity resolution and masks intensity-dependent features; review of slit, aperture, imaging and deconvolution methods for intensity-resolved data. Abstract and Sec. V: deconvolution of an intensity scan recovers spectra that match the expected 2 Up and 10 Up cutoffs, which the raw averaged data did not; peak intensity cannot be read directly from cutoffs of volume-averaged spectra, and the discrepancy is not removed by rescaling the intensity. Sec. VI: averaging can underestimate the 10 Up cutoff by up to 30% |
| 5 | A. T. J. B. Eppink and D. H. Parker, Velocity map imaging of ions and electrons using electrostatic lenses: application in photoelectron and photofragment ion imaging of molecular oxygen, Rev. Sci. Instrum. 68, 3477–3484 (1997) | doi:10.1063/1.1148310 | abstract | Abstract: electrostatic lenses map all particles with the same initial velocity vector to the same detector point; grid electrodes instead cause trajectory deflections and blurring from the extended source; trajectory simulations support the mapping |
| 6 | M. Davino, E. McManus, N. G. Helming, C. Cheng, G. Moğol, Z. Rodnova, G. Harrison, K. Watson, T. Weinacht, G. N. Gibson, T. Saule and C. Trallero-Herrero, A plano-convex thick-lens velocity map imaging apparatus for direct, high resolution 3D momentum measurements of photoelectrons with ion time-of-flight coincidence, Rev. Sci. Instrum. 94, 013303 (2023); read as arXiv:2209.11690 | doi:10.1063/5.0129900 | full text | Introduction: inverse Abel reconstruction needs cylindrical symmetry and is unsuitable for elliptically polarised light, so direct three-dimensional measurement is preferred. Sec. 3 and Fig. 4: radius calibrated from xenon ATI peaks separated by one photon energy, fitted with a quadratic and compared with trajectory simulations; a peak near the detector edge left out of the calibration |
| 7 | D. D. Hickstein, S. T. Gibson, R. Yurchak, D. D. Das and M. Ryazanov, A direct comparison of high-speed methods for the numerical Abel transform, Rev. Sci. Instrum. 90, 065115 (2019); read as arXiv:1902.09007 | doi:10.1063/1.5092635 | full text | Sec. I: the Abel transform applies to a cylindrically symmetric object with its axis parallel to the detector, and naive numerical inversion is unreliable; methods differ in robustness to noise. Sec. III: an accurate transform requires correct identification of the image centre. Secs. II and IV: Tikhonov regularisation suppresses noise and is set so as to preserve fine features |
| 8 | J. Ullrich, R. Moshammer, A. Dorn, R. Dörner, L. Ph. H. Schmidt and H. Schmidt-Böcking, Recoil-ion and electron momentum spectroscopy: reaction-microscopes, Rep. Prog. Phys. 66, 1463–1545 (2003) | doi:10.1088/0034-4885/66/9/203 | full text | Sec. 3.1.2: electrons with flight times equal to whole cyclotron periods give no transverse momentum information; the node spacing gives the magnetic field; resolution set by detector resolution, target size, timing and field distortions. Sec. 3.2: a cold target is needed because recoil momenta are comparable to thermal spread. Sec. 3.2.1: jet momentum spread grows with target mass; pre-cooling heavy gases can form clusters. Discussion of Fig. 25: a 15 ns dead time prevents registration of the second electron in part of the angular range |
| 9 | R. Dörner, V. Mergel, O. Jagutzki, L. Spielberger, J. Ullrich, R. Moshammer and H. Schmidt-Böcking, Cold target recoil ion momentum spectroscopy: a momentum microscope to view atomic collision dynamics, Phys. Rep. 330, 95–192 (2000) | doi:10.1016/S0370-1573(99)00109-X | full text | Sec. 2.3.1: momentum conservation requires the recoil ion to balance the electron momenta. Sec. 3.4: momentum from flight time and field with a zero point that must be found, calibration against reference data or lines of known momentum, resolution set by interaction-volume size and flight time; Fig. 11 shows a ridge from warm residual gas ionised along the beam. Sec. 3.6: dead time of 10 to 20 ns between hits on delay-line detectors |
| 10 | P. Heim, M. Rumetshofer, S. Ranftl, B. Thaler, W. E. Ernst, M. Koch and W. von der Linden, Bayesian analysis of femtosecond pump-probe photoelectron-photoion coincidence spectra with fluctuating laser intensities, Entropy 21, 93 (2019); read as arXiv:1901.06933 | doi:10.3390/e21010093 | full text | Sec. 1: several ionisation events per shot with detection probabilities below one give false electron-ion pairings; low ionisation rates avoid them at a cost in signal or time; covariance mapping can give systematic deviations outside Poisson statistics; COLTRIMS apparatus can separate true from false coincidences experimentally, at considerable technical cost |
| 11 | S. Patchkovskii and J. Mikosch, Statistical theory of cumulant mapping in an imperfect apparatus, Phys. Rev. A 111, 043108 (2025); read as arXiv:2412.18439 | doi:10.1103/PhysRevA.111.043108 | full text | Abstract and Sec. I: fluctuations of experimental parameters induce spurious correlations in covariance and cumulant mapping, restricting permissible event rate and requiring stability; false contributions grow faster than linearly with event rate, which gives a test. Sec. II: a three-fragment signal falls as the cube of the detection efficiency |
