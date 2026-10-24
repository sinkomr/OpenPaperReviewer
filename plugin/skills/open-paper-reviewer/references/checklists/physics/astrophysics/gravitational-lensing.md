---
id: T-GRAVITATIONAL-LENSING
name: Gravitational lensing
type: technique
field: physics/astrophysics
applies_when: the paper measures weak-lensing shear, cosmic shear or galaxy-galaxy or cluster lensing, models a strongly lensed system, infers masses, magnifications, time delays, the Hubble constant or dark matter substructure from lensing, or interprets a microlensing event
version: "0.1"
---

# Gravitational lensing

Gravitational lensing is used to claim the mass and its distribution in galaxies and clusters, cosmological parameters from cosmic shear, the Hubble constant from strong-lens time delays, dark matter substructure, and the masses of stars and planets from microlensing events. Weak lensing infers a statistical shear from the shapes of many faint galaxies with photometric redshifts (photo-z); strong lensing infers a mass model from multiple images; microlensing infers the lens from the light curve of a temporarily magnified star.

## 1. Shear calibration

**Question.** How was the multiplicative and additive bias of the shear estimator determined, are the calibration values and their uncertainties given for each sample or redshift bin, and do the image simulations used for calibration match the data in depth, seeing, galaxy population and blending?

**Why it matters.** Galaxy shapes measured at finite signal-to-noise with an imperfect model are biased, so the shear must be calibrated, usually with image simulations, and a calibration error scales the lensing signal directly. Blending of overlapping galaxies is a main source of multiplicative bias in deep data and makes the bias depend on redshift, so a calibration from simulations that leave out nearby objects can be wrong by more than the statistical error.

**Resolved by.** The shear method named and its calibration stated per bin with an uncertainty that enters the error budget; simulations shown to reproduce the observed distributions of size, flux, noise and neighbour density; blending included and its redshift dependence treated jointly with the redshift calibration; the required calibration accuracy compared with the statistical error of the measurement.

**Benchmark.** [1], [2], [5]

## 2. Point-spread function and additive systematics

**Question.** How was the point-spread function (PSF) modelled and interpolated to the galaxy positions, and does the paper show null tests that would reveal residual PSF leakage: correlations of PSF model residuals, star-galaxy shape cross-correlations, B-mode power and cross-correlation of the shear with maps of observing conditions?

**Why it matters.** An error in the PSF size produces a multiplicative bias and an error in the PSF shape produces an additive shear that adds coherent power to the signal. B-mode power flags some systematics, but many systematics produce none, so the absence of B modes does not by itself show that the measurement is clean.

**Resolved by.** PSF residual correlation functions measured on stars not used to build the model, and their contribution to the shear signal shown to be small compared with the statistical error; star-galaxy cross-correlations and mean shear in detector coordinates consistent with zero; B modes and cross-correlations with maps of stellar density, PSF size and PSF shape reported; any null test checked to be truly null under the analysis assumptions.

**Benchmark.** [1]

## 3. Source redshifts and source-sample purity

**Question.** How were the redshift distributions of the lensed (source) galaxies determined for each bin, how representative is the spectroscopic or other calibration sample of the sources, and how are the uncertainties in the mean and width of each distribution, and any contamination by foreground or cluster galaxies, carried into the result?

**Why it matters.** The lensing signal depends on the redshifts of the sources, so an error in the mean redshift of a bin shifts the inferred amplitude and mass. Spectroscopic samples are incomplete at the depths of lensing surveys and can fail for particular galaxy types, which biases methods trained on them. In cluster and galaxy-galaxy lensing, unlensed cluster members or foreground galaxies in the source sample dilute the signal most at small radii and bias the mass and concentration low.

**Resolved by.** The calibration method stated, with the incompleteness of the calibration sample addressed, for example by reweighting in colour space or by a second, independent method; the uncertainty in each bin's mean redshift, and in the width where it matters, marginalised over in the inference; outlier fractions characterised; for cluster lensing, the background selection described and the residual contamination measured as a function of radius.

**Benchmark.** [1], [3], [5]

## 4. Intrinsic alignments and small-scale modelling

**Question.** Does the cosmological or mass inference model the intrinsic alignment of galaxy shapes and the effect of baryons on the matter distribution at small scales, and does it show which scales were used and how the result changes when these models or the scale cuts change?

**Why it matters.** Galaxy shapes can be aligned by the same tidal fields that produce lensing, which adds or removes correlated shape signal; ignoring this can bias dark-energy and clustering-amplitude parameters by tens of per cent. Feedback from galaxy formation changes the matter power spectrum at small scales, and the scales where the chosen model holds set how much of the data can be used.

**Resolved by.** An intrinsic-alignment model with free parameters marginalised over, and its dependence on galaxy colour or type considered; baryonic effects modelled or removed by scale cuts justified with hydrodynamic simulations; results shown for alternative alignment models and scale cuts, with the parameter shifts compared with the statistical error.

**Benchmark.** [1], [4]

## 5. Strong-lens mass-model degeneracies

**Question.** Does the strong-lens analysis state which mass-model families were used, and does it address the mass-sheet and radial-profile degeneracies and the line-of-sight (external) convergence for quantities that depend on them, such as time delays, the Hubble constant, enclosed mass profiles and magnifications?

**Why it matters.** Image positions are unchanged under a mass-sheet transformation and related transformations, but predicted time delays and magnifications change, so a model that fits the images well can still give a biased distance or magnification. Simple parametric profiles hide this freedom and give errors smaller than the true uncertainty; independent model families applied to the same cluster can differ substantially in magnification, most of all near the critical curves.

**Resolved by.** The degeneracies named and broken with independent data, such as stellar kinematics and an external-convergence estimate from line-of-sight galaxy counts or weak lensing; results shown for more than one mass-model family, with the spread included in the uncertainty; magnifications quoted with uncertainties that grow with magnification; for time delays, microlensing and data gaps in the light curves treated in the delay measurement.

**Benchmark.** [6], [7], [8]

## 6. Substructure and flux-ratio anomalies

**Question.** When anomalous image flux ratios or localised image distortions are attributed to dark matter substructure, does the paper exclude other causes: microlensing by stars, dust extinction, source variability combined with time delays, lens light, and angular structure of the main lens not included in the macro-model?

**Why it matters.** Small source regions are microlensed by stars in the lens galaxy, dust and source variability alter flux ratios, and discs, multipoles and departures from elliptical symmetry in the main lens can mimic a subhalo. Detections made with too simple a lens or source model can therefore be spurious, and analytic source models can bias dark matter constraints.

**Resolved by.** Fluxes measured at wavelengths emitted by a region extended enough to avoid stellar microlensing, or averaged over time with the delays corrected; the macro-model given enough angular freedom, with multipoles or a disc tested; the detection significance shown to survive changes to the lens-light and source models; line-of-sight haloes included in the interpretation.

**Benchmark.** [9]

## 7. Microlensing lens mass, distance and blending

**Question.** How are the lens mass and distance obtained from a microlensing event: from measured parallax and finite-source effects, from lens flux in high-resolution imaging, or only from a Galactic model given the event timescale? Is the blended light from unrelated stars and from the lens fitted and constrained?

**Why it matters.** The Einstein crossing time combines the lens mass, the lens and source distances and their relative motion, so on its own it does not fix the mass or distance. Blended light from stars in the same seeing disc lowers the apparent magnification and shortens the apparent timescale, and the lens itself may contribute part of that light.

**Resolved by.** The physical parameters stated with the measurements that determine them; parallax and finite-source parameters, with the source angular size estimated from its stellar type, where these are claimed; where neither is measured, masses presented as probabilistic estimates with the Galactic model stated; blend flux fitted for each data set and, where possible, constrained or resolved by later high-resolution imaging.

**Benchmark.** [10], [11]

## 8. Competing models for microlensing anomalies

**Question.** For an event interpreted as a planet or binary lens, does the paper search the parameter space for all models that fit the light curve, including close and wide lens separations, a binary source, finite-source effects and parallax with lens orbital motion, and report how much better the adopted model fits?

**Why it matters.** Short deviations from a single-lens light curve can be produced by planets at more than one separation, by a faint companion to the source star, or by finite-source effects that mimic a larger mass ratio, and parallax and orbital motion are partly degenerate. Gaps in coverage, especially during caustic crossings, allow several solutions.

**Resolved by.** All competing solutions listed with their fit statistics and parameters; the coverage of the anomaly shown; colour information, dense sampling or astrometry used to separate binary-source and planetary models; conclusions stated for each surviving solution, or limited to what the solutions have in common.

**Benchmark.** [10], [11], [12]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | R. Mandelbaum, Weak lensing for precision cosmology, Annu. Rev. Astron. Astrophys. 56, 393–433 (2018); read as arXiv:1710.03235 | doi:10.1146/annurev-astro-081817-051928 | full text | Sec. 2.1: PSF size errors give multiplicative and PSF shape errors additive bias; residual correlation statistics and reserved stars as tests. Secs. 2.3 and 2.7: blends are common and calibration simulations need realistic nearby structure. Sec. 2.7: noise and model bias, calibration by image simulations, Stage IV need of about 2×10⁻³. Sec. 2.8: unrepresentative spectroscopic samples limit photo-z calibration. Secs. 3.4 and 3.5: ignoring intrinsic alignments gives unacceptable bias; baryonic modelling sets usable scales. Sec. 4: many systematics produce no B modes; star-galaxy shape cross-correlations; mean shear in CCD coordinates; cross-correlation with maps of stellar density, PSF size and PSF shape; null tests can be defeated by faulty assumptions |
| 2 | N. MacCrann et al., DES Y3 results: blending shear and redshift biases in image simulations, Mon. Not. R. Astron. Soc. 509, 3371–3394 (2021); read as arXiv:2012.08567 | doi:10.1093/mnras/stab2870 | abstract | Abstract: deeper surveys need realistic image simulations because blending grows; blending is the main source of the mean multiplicative shear bias of about −2%; simulations with redshift-dependent shear calibrate shear and redshift biases together |
| 3 | J. A. Newman and D. Gruen, Photometric redshifts for next-generation surveys, Annu. Rev. Astron. Astrophys. 60, 363–414 (2022); read as arXiv:2206.13633 | doi:10.1146/annurev-astro-032122-014611 | full text | Sec. 1.2.2: lensing needs each bin's full redshift distribution, with the mean known to about 0.001(1+z) for future surveys and the tails characterised. Sec. 1.2.1: outlier rates known or marginalised. Secs. 2.2 and 3.1: spectroscopic samples incomplete at lensing depths and failures for some object types bias trained methods. Sec. 3.3: reweighting by colour cells |
| 4 | M. A. Troxel and M. Ishak, The intrinsic alignment of galaxies and its impact on weak gravitational lensing in an era of precision cosmology, Phys. Rep. 558, 1–59 (2015); read as arXiv:1407.6990 | doi:10.1016/j.physrep.2014.11.001 | full text | Abstract and Sec. 1: intrinsic alignment is a main physical systematic that correlates with the lensing signal; ignoring it can bias the dark-energy equation of state by 50% or more and the amplitude of matter fluctuations by up to 30%. Sec. 6: mitigation by marginalising over alignment models, tomography, nulling and self-calibration |
| 5 | K. Umetsu, Cluster–galaxy weak lensing, Astron. Astrophys. Rev. 28, 7 (2020); read as arXiv:2007.00506 | doi:10.1007/s00159-020-00129-w | full text | Sec. 3.4.2: PSF and noise biases parametrised as multiplicative and additive, calibrated against image simulations to about 2% in clusters. Secs. 3.6.2 and 3.6.3: source redshift distribution and mean inverse critical density. Sec. 4.1: photo-z outliers and representativeness of calibration samples; cluster members and foreground galaxies dilute the signal most at small radii, biasing concentration and mass low |
| 6 | T. Treu and P. J. Marshall, Time delay cosmography, Astron. Astrophys. Rev. 24, 11 (2016); read as arXiv:1605.05333 | doi:10.1007/s00159-016-0096-8 | full text | Sec. 3: mass-sheet and source-position transformations keep image positions but change predicted delays; profile slope is degenerate with the delay; stellar kinematics break the degeneracy. Sec. 4.3: external convergence from galaxy counts or mass reconstructions. Secs. 2 and 4.2.2: simple parametric models gave errors much smaller than the true uncertainty. Secs. 2 and 4.1: data gaps and microlensing in optical light curves gave conflicting delays; explicit microlensing modelling avoids catastrophic delay errors |
| 7 | P. Schneider and D. Sluse, Mass-sheet degeneracy, power-law models and external convergence: impact on the determination of the Hubble constant from gravitational lensing, Astron. Astrophys. 559, A37 (2013) | doi:10.1051/0004-6361/201321882 | abstract | Abstract: the formal precision of lensing H0 values rests on assuming a power-law profile; mass-sheet-like transformations leave freedom even with Einstein rings; a composite lens fitted by a power law gives an H0 about 20% different; model degeneracies have been underestimated |
| 8 | M. Meneghetti et al., The Frontier Fields lens modelling comparison project, Mon. Not. R. Astron. Soc. 472, 3177–3216 (2017); read as arXiv:1606.04548 | doi:10.1093/mnras/stx2064 | full text | Sec. 4.5: the largest magnification errors are near critical lines and scatter grows with magnification, reaching about 30% at a magnification of 10 for the best model; other models show biases up to about 40 to 50%. Sec. 7: parametric and free-form methods perform differently, and groups using the same code and data obtain different reconstructions |
| 9 | S. Vegetti et al., Strong gravitational lensing as a probe of dark matter, Space Sci. Rev. 220, 58 (2024); read as arXiv:2306.11781 | doi:10.1007/s11214-024-01087-w | full text | Sec. 3: flux-ratio anomalies can come from stellar microlensing, dust and source variability; useful only at wavelengths where the source is larger than the microlens scale; line-of-sight haloes also leave an imprint. Sec. 5.1: discs, multipoles and unmodelled angular structure mimic substructure, and too simple lens models gave false detections. Sec. 5.2: microlensing of small emitting regions, avoided at wavelengths from extended regions; variability with delays; source and potential degeneracies; analytic source models bias dark matter constraints. Sec. 5.3: lens light can cause false positives |
| 10 | S. Mao, Astrophysical applications of gravitational microlensing, Res. Astron. Astrophys. 12, 947–972 (2012); read as arXiv:1207.3720 | doi:10.1088/1674-4527/12/8/005 | full text | Sec. 2.5.1: the timescale combines mass, distances and velocity, so mass and distance are only statistically estimated with a Galactic model; blending lowers the observed magnification. Sec. 2.6: parallax and finite-source effects together give the mass. Sec. 3.7: close and wide binary solutions, and planetary and binary lens light curves can mimic each other |
| 11 | Y. Tsapras, Microlensing searches for exoplanets, Geosciences 8, 365 (2018); read as arXiv:1810.02691 | doi:10.3390/geosciences8100365 | full text | Secs. 2.1.6 and 2.2.1 to 2.2.3: timescale alone does not give mass or distance; parallax with Einstein radius gives both; source angular size from its stellar type; blending makes events look less magnified and shorter; high-resolution imaging measures lens flux. Secs. 2.2.4, 2.6 and 2.7: binary sources mimic planets, finite-source effects mimic larger mass ratios, close and wide ambiguities, coverage gaps allow several solutions, parallax and orbital motion partly degenerate |
| 12 | B. S. Gaudi, Planetary microlensing perturbations: true planets or binary sources?, Astrophys. J. 506, 533–539 (1998); read as arXiv:astro-ph/9706268 | doi:10.1086/306256 | abstract | Abstract: binary-source events with a faint companion passing close to the lens reproduce planetary perturbations and could contaminate planet samples; dense sampling, optical and infrared photometry or spectroscopy break the degeneracy |
