---
id: T-HIGH-CONTRAST-IMAGING
name: High-contrast and direct imaging
type: technique
field: physics/astrophysics
applies_when: the paper detects, characterises or rules out faint companions, planets or circumstellar disc structure near a bright star using coronagraphy, adaptive optics or point-spread-function subtraction, or reports contrast curves, companion astrometry or model-based companion masses from such images
version: "0.1"
---

# High-contrast and direct imaging

High-contrast imaging is used to claim the detection of planets, brown dwarfs and disc structures close to a bright star, their positions, brightnesses and spectra, and, from non-detections, limits on companions of a given mass. The claims rest on suppressing the star's light with adaptive optics (AO), a coronagraph and point-spread-function (PSF) subtraction such as angular, spectral or reference differential imaging (ADI, SDI, RDI), after which the remaining signal is a small fraction of the starlight and is easily confused with residual speckles, processed disc light or unrelated stars.

## 1. Signal loss in PSF subtraction

**Question.** Which PSF-subtraction method and parameters were used (reference selection, exclusion criterion in field rotation or wavelength, number of components or size of optimisation regions), how was the loss and distortion of the companion's signal measured and corrected before its flux, position or spectrum was quoted, and against what measurement of the star's own flux were contrasts computed?

**Why it matters.** PSF subtraction removes part of a companion's own light, through self-subtraction when the companion is present in the reference images, which leaves a dimmed source flanked by negative lobes, and through over-subtraction when the fit to the starlight absorbs part of the companion. The fraction removed depends on separation and on the reduction parameters, so uncorrected photometry, astrometry and spectra are biased, most strongly close to the star and for aggressive reductions. Because the star itself is masked or saturated, any error in its reference flux carries into every contrast and companion magnitude.

**Resolved by.** The algorithm and its parameters stated; the field rotation or wavelength range available at the companion's separation compared with the exclusion criterion; throughput measured by injecting artificial point sources at the same separation, by fitting a negative copy of the companion, or by forward modelling of the processed signal; the star's flux taken from a stated reference, such as unsaturated images or satellite spots of known relative brightness; the corrected flux, position and spectrum quoted with uncertainties that include this step.

**Benchmark.** [1], [2], [3], [4], [5]

## 2. A source, or a residual speckle

**Question.** How was the detection significance of each candidate computed (how the noise was estimated, at what separation, with what correction for the small number of independent resolution elements), and does the candidate persist across reduction parameters, wavelengths, epochs or instruments?

**Why it matters.** Quasi-static speckles look like point sources and their intensity statistics have a long tail, so the usual Gaussian relation between a signal-to-noise ratio and a false-alarm probability does not hold. Close to the star there are only a few independent resolution elements in each annulus, so a five-standard-deviation signal there carries a much higher false-positive probability than the same signal far from the star.

**Resolved by.** Noise measured in an annulus at the candidate's separation with the candidate and its subtraction lobes masked; a small-sample correction such as the Student t-distribution, with the corresponding false-positive probability stated; the candidate shown to survive a range of reduction aggressiveness and to appear at the same position in independent data sets, such as different wavelengths, nights or instruments.

**Benchmark.** [4], [5], [6]

## 3. Contrast curves and detection limits

**Question.** How was each contrast curve or detection limit defined: what noise estimate and threshold, what false-positive and completeness levels, whether the curve was corrected for algorithmic throughput and coronagraph transmission, and how the small-sample effect at small separations was handled?

**Why it matters.** Contrast curves are computed in different ways by different authors, so two curves labelled five standard deviations can correspond to very different false-positive rates and completeness. A curve without throughput correction measures how well the starlight was removed, not which companions could have been detected, and a curve that ignores small-sample statistics overstates the sensitivity close to the star.

**Resolved by.** The threshold given as a false-positive probability or expected number of false positives, together with the completeness the curve corresponds to; throughput measured with injected sources and applied; the small-sample correction stated; for limits on companion populations, completeness or sensitivity maps built from injected or simulated companions rather than a single curve.

**Benchmark.** [4], [6], [7], [8]

## 4. Point sources and disc structure

**Question.** Where a candidate lies on or within circumstellar disc emission, does the paper show that it is a compact source and not a part of the disc reshaped by processing, for example by forward modelling the disc through the same reduction?

**Why it matters.** PSF subtraction filters extended emission unevenly, and narrow or asymmetric disc features such as rings, spirals and arcs can become compact, point-like residuals after processing. Scattered light from dust can also resemble the colours or spectrum expected of a young planet, so a point-like signal in a disc is not by itself evidence of a planet.

**Resolved by.** Forward modelling of a disc model through the same reduction, showing that the disc alone does not produce the candidate; the candidate recovered in reductions that preserve extended emission, such as reference differential imaging or polarimetric imaging; orbital motion over several epochs consistent with a bound object rather than a static or co-rotating disc feature; independent evidence such as accretion signatures, where available.

**Benchmark.** [4], [5]

## 5. Star position and astrometric calibration

**Question.** How was the position of the star behind the coronagraph determined, and which plate scale, orientation of north, distortion solution and their uncertainties were applied to convert detector positions into separations and position angles?

**Why it matters.** Companion astrometry is measured relative to a star whose image is blocked by the coronagraph, so the star's position must be inferred, for example from satellite spots. Plate scale, north offset and distortion vary between instruments, filters and set-ups and can drift with time; uncorrected, they produce apparent motion at the milliarcsecond level and above that can be mistaken for, or can hide, orbital or common proper motion.

**Resolved by.** The method for locating the star stated, with its uncertainty; plate scale, north offset and distortion taken from a stated calibration close in time to the observations, ideally with astrometric reference fields; each calibration uncertainty propagated into the separation and position angle; for multi-epoch comparisons across instruments, the calibrations used for each epoch given.

**Benchmark.** [4], [9]

## 6. Background stars and common proper motion

**Question.** How does the paper establish that a candidate is bound to the star and not a background or foreground object: does it show multi-epoch relative astrometry against the track expected for a stationary background object, including parallax, and does it consider background stars that have their own proper motion?

**Why it matters.** Unrelated stars are common in deep images, especially near the Galactic plane, and distant red giants can share the colours of young companions, so photometry in one or two bands rarely settles companionship. A second epoch showing shared motion is the usual test, but a background star with its own proper motion can move in a way that resembles co-motion, and a short time baseline may not separate the two tracks.

**Resolved by.** Relative astrometry at two or more epochs plotted against the predicted track of a stationary background object, with the separation between the tracks large compared with the uncertainties; where the tracks are close, the case of a background star with its own proper motion considered explicitly; the Galactic latitude of the field taken into account when judging the chance of an unrelated star; a spectrum, where available, showing features of a young, low-gravity companion rather than a background star.

**Benchmark.** [4], [5], [8]

## 7. Masses from evolutionary models

**Question.** When a companion's mass, or a mass limit from a contrast curve, is inferred from luminosity, which evolutionary models and initial conditions were used, what age was adopted and on what grounds, and does the quoted uncertainty include the uncertainty in age and the spread between models?

**Why it matters.** Without a dynamical measurement, a directly imaged companion's mass, and the mass corresponding to a detection limit, comes from cooling models that convert luminosity and age into mass. The result depends strongly on the adopted age, which is often poorly known for isolated stars, and on assumed initial conditions: hot-start, warm-start and cold-start models can give masses that differ by several times for the same young object.

**Resolved by.** The models, their initial conditions and the age with its uncertainty and basis (for example membership of a young moving group) stated, for detections and for mass limits alike; the mass range shown for the plausible ages and model families, not a single value; classification as a planet or brown dwarf qualified when the range spans the boundary; a dynamical mass from orbital motion, host-star astrometry or radial velocities used where available to test the model-based value.

**Benchmark.** [4], [5], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | C. Marois, D. Lafrenière, R. Doyon, B. Macintosh and D. Nadeau, Angular differential imaging: a powerful high-contrast imaging technique, Astrophys. J. 641, 556–564 (2006); read as preprint arXiv:astro-ph/0512335 | doi:10.1086/500401 | full text | Sec. III: a companion is rejected from the reference only if field rotation moves it by a minimum number of FWHM, which sets a minimum separation and time interval; Sec. VI.3: detection limits computed from simulated companions and noise in annuli one FWHM wide |
| 2 | D. Lafrenière, C. Marois, R. Doyon, D. Nadeau and É. Artigau, A new algorithm for point-spread function subtraction in high-contrast imaging: a demonstration with angular differential imaging, Astrophys. J. 660, 770–780 (2007); read as preprint arXiv:astro-ph/0702697 | doi:10.1086/513180 | full text | Sec. II: smaller optimisation regions attenuate noise better but subtract more companion signal, so partial subtraction must be characterised; Secs. IV.2 and IV.3: partial subtraction measured with artificial point sources as a function of separation and parameters, and used to correct photometry; Sec. IV.4: detection limits corrected for partial subtraction |
| 3 | R. Soummer, L. Pueyo and J. Larkin, Detection and characterization of exoplanets and disks using projections on Karhunen-Loève eigenimages, Astrophys. J. Lett. 755, L28 (2012) | doi:10.1088/2041-8205/755/2/L28 | abstract | Abstract: principal-component PSF subtraction allows forward modelling of astrophysical sources, reducing the astrometric and photometric biases that earlier subtraction algorithms introduce for faint sources |
| 4 | K. B. Follette, An introduction to high contrast differential imaging of exoplanets and disks, Publ. Astron. Soc. Pac. 135, 093001 (2023); read as preprint arXiv:2308.01354 | doi:10.1088/1538-3873/aceb31 | full text | Secs. IV.3, IV.4 and V.2: self-subtraction in ADI and SDI leaves negative lobes and is limited by excluding nearby frames. Secs. VII.1 to VII.4: throughput correction by false-planet injection, forward modelling and negative planets; noise measured in annuli with lobes masked and a small-sample correction near the star; contrast at a chosen multiple of the noise needs throughput correction. Sec. VIII.2: narrow, asymmetric disc structures can look point-like after subtraction; candidates checked across reduction parameters, epochs, wavelengths and instruments. Sec. III: satellite spots as proxies for the star's position and brightness. Sec. VIII.1: chance alignments are more common near the Galactic plane, background red giants share companions' colours, and a second epoch showing common proper motion is the usual test. Sec. I.2: masses from evolutionary models depend on age and formation pathway (hot or cold start) |
| 5 | T. Currie, B. Biller, A.-M. Lagrange, C. Marois, O. Guyon, E. Nielsen, M. Bonnefoy and R. De Rosa, Direct imaging and spectroscopy of extrasolar planets, in Protostars and Planets VII, Astron. Soc. Pac. Conf. Ser. 534, 799–837 (2023); read as preprint arXiv:2205.05696 | doi:10.26624/uctd5384 | full text | Sec. 2.3: PSF subtraction attenuates and distorts planet signals, biases measured by injected or negative planets and by forward modelling; speckle statistics have a long positive tail that produces false positives. Sec. 3.4.1: background stars are common near the Galactic plane, confirming companionship often needs multi-year observations, and background stars with their own proper motion are more easily confused with planets. Sec. 3.4.3: forward modelling needed to show a claimed planet is not a partly subtracted piece of a disc; dust can resemble protoplanet spectra. Sec. 3.4.2: masses from luminosity evolution models depend on the adopted age and on hot- or cold-start assumptions; revised ages can change masses substantially. Sec. 3.5: model-independent masses from host-star astrometry and radial velocities |
| 6 | D. Mawet, J. Milli, Z. Wahhaj, D. Pelat, O. Absil, C. Delacroix, A. Boccaletti, M. Kasper, M. Kenworthy, C. Marois, B. Mennesson and L. Pueyo, Fundamental limitations of high contrast imaging set by small sample statistics, Astrophys. J. 792, 97 (2014); read as preprint arXiv:1407.2247 | doi:10.1088/0004-637X/792/2/97 | full text | Sec. I.1: raw speckle noise is non-Gaussian. Sec. II.2: only about 2πr independent resolution elements at radius r (in units of λ/D), so the small-sample regime applies close to the star. Sec. III: Student t-test and corrected signal-to-noise ratio. Sec. IV.1.1: a fixed five-sigma threshold at 1 λ/D gives a false-positive fraction orders of magnitude higher than the Gaussian value. Secs. II, IV.2 and V: five-sigma contrasts at different separations are not equivalent, and completeness (true-positive fraction) matters as well as the false-positive fraction |
| 7 | R. Jensen-Clem, D. Mawet, C. A. Gomez Gonzalez, O. Absil, R. Belikov, T. Currie, M. A. Kenworthy, C. Marois, J. Mazoyer, G. Ruane and A. Tanner, A new standard for assessing the performance of high contrast imaging systems, Astron. J. 155, 19 (2018); read as preprint arXiv:1711.01215 | doi:10.3847/1538-3881/aa97e4 | full text | Secs. I and III.3: authors treat throughput, small-sample correction and non-Gaussian noise differently, so contrast curves are not comparable. Sec. III.2: a contrast curve fixes completeness at 50% and hides the false-positive rate; standard-deviation thresholds assume Gaussian noise and many samples, which fail near the star. Sec. III.4: raw contrast is not a detection limit. Secs. IV and V: performance maps of true-positive fraction against flux ratio and separation at a fixed false-positive rate |
| 8 | B. P. Bowler, Imaging extrasolar giant planets, Publ. Astron. Soc. Pac. 128, 102001 (2016); read as preprint arXiv:1605.02731 | doi:10.1088/1538-3873/128/968/102001 | full text | Sec. IV.5: survey sensitivity maps built by Monte Carlo simulation of artificial planets compared with contrast curves, converting mass to brightness with hot-start models and stellar ages; most survey candidates rejected as background objects at a second epoch. Sec. III.1: hot-start models give the lowest masses, cold-start models much lower luminosities, with model-dependent masses differing by several times for one object; stellar age often dominates the error budget. Sec. III.2: no imaged planet then had a measured mass, and dynamical masses would test cooling models |
| 9 | A.-L. Maire, M. Langlois, K. Dohlen, A.-M. Lagrange, R. Gratton, G. Chauvin, S. Desidera, J. H. Girard, J. Milli, A. Vigan and others, SPHERE IRDIS and IFS astrometric strategy and calibration, Proc. SPIE 9908, 990834 (2016); read as preprint arXiv:1609.06681 | doi:10.1117/12.2233013 | full text | Sec. 1: astrometry confirms companionship and constrains orbits; the star centre behind the coronagraph is found from faint replicas of the star made with the deformable mirror. Sec. 2.1: pixel scale, north offset and pupil zeropoint must be calibrated, and pixel scale depends on filter and coronagraph. Sec. 3.1: uncorrected distortion amounts to several milliarcseconds at one arcsecond. Sec. 3.3.2: the north offset was found to vary by more than a degree over a few months before correction |
