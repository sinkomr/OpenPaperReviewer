---
id: T-SUPERNOVA-COSMOLOGY
name: Supernova cosmology
type: technique
field: physics/astrophysics
applies_when: the paper uses type Ia supernovae as distance indicators, fits or standardises their light curves, builds or analyses a supernova Hubble diagram, or bases a claim about distances, the expansion history, dark energy or the Hubble constant on supernova brightnesses
version: "0.1"
---

# Supernova cosmology

Supernova cosmology uses type Ia supernovae (SNe Ia), standardised by the width (stretch) and colour of their light curves, as distance indicators to claim the expansion history of the universe: the matter density, the dark-energy equation of state w and, once the absolute brightness is calibrated, the Hubble constant H0. The claims rest on comparing standardised peak brightnesses across redshift, usually by combining supernovae from several surveys on one Hubble diagram (distance modulus against redshift).

## 1. Light-curve model and its training

**Question.** Which light-curve model was used to fit stretch, colour and peak brightness, on which supernovae and with which photometric calibration was it trained, and does the paper show how the distances change with a different model or training?

**Why it matters.** Fitted distances depend on an empirical spectral model that is least well constrained in the rest-frame ultraviolet, which the observed optical bands sample at high redshift. Different models applied to the same supernovae have given values of w that differ by more than their statistical uncertainty, and training choices such as the assumed intrinsic scatter and the regularisation bias the model. A model trained on light curves with one calibration and applied to recalibrated data is inconsistent.

**Resolved by.** The model and its version named, with its training sample and the rest-frame wavelength range it covers; the model retrained, or its training uncertainty propagated, whenever the calibration changes; rest-frame bands outside the well-trained range excluded or tested; the effect of an alternative model or training on the cosmological result reported as a systematic uncertainty.

**Benchmark.** [1], [2], [3], [13]

## 2. Colour, dust and intrinsic scatter

**Question.** How does the standardisation treat supernova colour (a single linear colour coefficient, or a model that separates intrinsic colour from dust reddening), which model of intrinsic brightness scatter and which populations of stretch and colour were assumed, and how much does the result change under alternatives?

**Why it matters.** An observed colour mixes intrinsic colour with dust reddening along extinction laws that vary between hosts, so one linear coefficient cannot describe both, and the scatter of Hubble residuals depends on colour. The assumed scatter model and parent populations feed directly into the bias corrections; biases for very red or blue supernovae can reach tenths of a magnitude, and changing the colour model has shifted w by more than earlier systematic budgets allowed.

**Resolved by.** The standardisation relation written out with its fitted coefficients; the intrinsic scatter model and the stretch and colour populations stated with their origin; Hubble residuals shown against colour; results given for at least one alternative scatter or dust model, with the difference carried as a systematic uncertainty.

**Benchmark.** [4], [5], [6]

## 3. Host-galaxy correction

**Question.** Is a host-galaxy correction applied to the standardised brightnesses, which host property defines it (global stellar mass, or a local property such as star formation near the supernova), where is any step placed, how were host properties measured and assigned, including for supernovae with no identified host, and is the same correction applied across all redshifts and subsamples?

**Why it matters.** After stretch and colour correction, supernovae in massive hosts or older environments are on average brighter by a few hundredths to about a tenth of a magnitude, and the local environment may account for much of the global mass effect. Because the mix of hosts changes with redshift, an omitted or inconsistent correction biases w. The location of the step and the treatment of supernovae without a host are analysis choices.

**Resolved by.** The host property, step location and host-measurement method stated, with the rule for supernovae without an identified host; the size of the correction fitted or justified, with its uncertainty; the result shown with an alternative step location or host tracer; the host correction modelled consistently with the colour and dust model and with the bias simulations.

**Benchmark.** [4], [7], [8], [9]

## 4. Selection effects and distance bias corrections

**Question.** How were selection effects (detection, spectroscopic follow-up and quality cuts) modelled for each survey, how were the resulting distance biases computed, and does the paper show that its simulation reproduces the observed distributions?

**Why it matters.** Near a survey's limit the brighter supernovae are preferentially found, followed up and kept, so standardised distances are biased, by up to a few hundredths of a magnitude on average in a redshift bin and much more for individual red or blue events. The correction is only as good as the description of the selection and of the intrinsic populations; spectroscopic selection is hard to model from first principles, and nearby samples assembled from targeted galaxy searches have poorly known selection.

**Resolved by.** Bias corrections from simulations of each survey that include its cadence, noise and selection, with the spectroscopic efficiency and how it was derived stated; observed and simulated distributions of redshift, colour, stretch and signal-to-noise compared; alternative selection assumptions, such as a magnitude-limited versus a volume-limited nearby sample, used as systematics; the size of the correction shown against redshift.

**Benchmark.** [5], [6], [9], [10]

## 5. Photometric calibration across surveys

**Question.** How were the photometric systems of the combined surveys tied to a common scale (which reference stars or catalogue and which primary flux standards), how were the filter transmission curves and zero-point uncertainties determined, and how are the calibration uncertainties propagated, including into the light-curve model training?

**Why it matters.** A cosmological fit compares nearby supernovae from one survey with distant supernovae from another, so a zero-point or filter error between surveys mimics a change of distance with redshift. Calibration has been the largest systematic term in several analyses; offsets of tens of millimagnitudes between surveys have been found, and correcting them has moved w by a sizeable fraction of its statistical uncertainty. Errors in the colour calibration of the nearby samples weigh most heavily.

**Resolved by.** All surveys cross-calibrated to a common stellar reference, with the offsets and their covariance given; the primary flux standards and their uncertainty stated; filter curves and any wavelength shifts given; calibration uncertainties propagated jointly through light-curve fitting and model training into a systematic covariance matrix; the Galactic extinction correction and its uncertainty stated; the calibration contribution to the error on each cosmological parameter reported.

**Benchmark.** [3], [9], [11], [12], [13]

## 6. Classification and contamination

**Question.** How were supernovae identified as type Ia (by spectroscopy, or from light curves alone), what contamination by other supernova types is expected, and how is that contamination treated in the cosmological fit?

**Why it matters.** Core-collapse and peculiar supernovae that pass as type Ia lie off the Hubble relation and bias the distances. The expected contamination, and the bias it causes, depend on templates and rates of the other types that are imperfectly known.

**Resolved by.** The classifier, its training set, and its efficiency and contamination on realistic simulations stated; for photometrically classified samples, contamination handled with a probabilistic method that marginalises over the non-Ia population rather than by a hard cut alone; the result shown with alternative classifiers, priors and models of the other types; the contamination systematic quantified.

**Benchmark.** [10], [14], [15]

## 7. Redshifts and peculiar velocities

**Question.** Where does each redshift come from and with what uncertainty, how is it converted to the cosmic microwave background frame, how are peculiar velocities corrected for nearby supernovae, and what minimum redshift is used for the cosmological fit or the Hubble-flow sample?

**Why it matters.** At low redshift the peculiar motion of a host is a significant fraction of its recession velocity, adding scatter and coherent offsets to the nearby supernovae that anchor the Hubble diagram, so errors there pass into H0 and w. Compiled redshift catalogues have contained missing or incorrect heliocentric corrections, coordinates and uncertainties, and a small coherent shift in redshift is a recognised systematic.

**Resolved by.** The source and uncertainty of each redshift stated; the frame conversion described; peculiar velocities corrected with a named flow model and group assignments, with a velocity uncertainty included and an alternative model tested; a stated low-redshift cut, with the result shown for alternative cuts; a coherent redshift shift included as a systematic.

**Benchmark.** [9], [16], [17]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | R. Kessler et al., First-year Sloan Digital Sky Survey-II supernova results: Hubble diagram and cosmological parameters, Astrophys. J. Suppl. 185, 32–84 (2009) | doi:10.1088/0067-0049/185/1/32 | abstract | Abstract: two light-curve fitters applied to the same 288 supernovae give w differing by about 0.2, against statistical errors of about 0.06 to 0.07, traced to the rest-frame ultraviolet model and the colour correction; both show data-model discrepancies in the rest-frame U band |
| 2 | J. Mosher et al., Cosmological parameter uncertainties from SALT-II type Ia supernova light curve models, Astrophys. J. 793, 16 (2014) | doi:10.1088/0004-637X/793/1/16 | abstract | Abstract: simulated training varying the spectral model, intrinsic scatter model and regularisation shows that realistic scatter models bias the trained model in the ultraviolet and bias w by about 0.01 to 0.02 |
| 3 | D. Brout et al., The Pantheon+ analysis: SuperCal-Fragilistic cross calibration, retrained SALT2 light curve model, and calibration systematic uncertainty, Astrophys. J. 938, 111 (2022) | doi:10.3847/1538-4357/ac8bcc | abstract | Abstract: recalibration and model retraining were previously handled separately; here 25 systems and 105 filters are cross-calibrated to Pan-STARRS stars with a covariance matrix, the model is retrained, the offset covariance is propagated through training and fitting, and the calibration term on w is about half the statistical error; a change of about 1.5% in the primary standards is included |
| 4 | D. Brout and D. Scolnic, It's dust: solving the mysteries of the intrinsic scatter and host-galaxy dependence of standardized type Ia supernova brightnesses, Astrophys. J. 909, 26 (2021) | doi:10.3847/1538-4357/abd69b | abstract | Abstract: a model of intrinsic colour plus dust with a wide range of extinction laws reproduces an 11-sigma dependence of Hubble residual scatter on colour; host-dependent dust distributions can account for the mass step; replacing earlier colour models shifts w by up to 0.04, beyond earlier systematic budgets |
| 5 | D. Scolnic and R. Kessler, Measuring type Ia supernova populations of stretch and color and predicting distance biases, Astrophys. J. Lett. 822, L35 (2016) | doi:10.3847/2041-8205/822/2/L35 | abstract | Abstract: simulations including selection, noise and intrinsic scatter show linear standardisation leaves Hubble residual biases with colour (up to 0.3 mag) and stretch; earlier parent populations were too broad and biased w |
| 6 | R. Kessler et al., First cosmology results using type Ia supernova from the Dark Energy Survey: simulations to correct supernova distance biases, Mon. Not. R. Astron. Soc. 485, 1171–1187 (2019) | doi:10.1093/mnras/stz463 | full text | Abstract and Sec. 9: binned distance biases up to about 0.05 mag, up to about 0.4 mag for individual red events, with the difference between two scatter models traced to their colour populations and carried as a systematic. Sec. 7.1: the spectroscopic selection algorithm cannot be simulated, so an empirical efficiency is fitted to the ratio of data to simulation. Sec. 7.2: many nearby searches target lists of galaxies, so magnitude-limited and volume-limited selection are both simulated. Sec. 8: observed and simulated distributions of redshift, signal-to-noise and other quantities compared |
| 7 | M. Sullivan et al., The dependence of type Ia supernovae luminosities on their host galaxies, Mon. Not. R. Astron. Soc. 406, 782–802 (2010) | doi:10.1111/j.1365-2966.2010.16731.x | abstract | Abstract: after shape and colour correction, supernovae in massive hosts are about 0.08 mag brighter; mean host mass changes with redshift, so the effect can bias w at the level of its statistical error; a host-dependent correction is recommended |
| 8 | M. Rigault et al., Strong dependence of type Ia supernova standardization on the local specific star formation rate, Astron. Astrophys. 644, A176 (2020) | doi:10.1051/0004-6361/201730404 | abstract | Abstract: supernovae in younger local environments (within 1 kpc) are about 0.16 mag fainter after standardisation; fitted jointly, the local term remains and the global mass step shrinks; shifting environment ages with redshift can bias w |
| 9 | D. Brout et al., The Pantheon+ analysis: cosmological constraints, Astrophys. J. 938, 110 (2022); read as preprint arXiv:2202.04077 | doi:10.3847/1538-4357/ac8e04 | full text | Secs. II.1, III.3 and IV.5: distance bias corrections from survey simulations, with alternative intrinsic scatter models as systematics. Secs. II.1, III.1.4 and IV.5: host step at a nominal stellar mass with an alternative location as a systematic; hostless supernovae assigned low mass. Secs. III.1.2 and III.1.3: peculiar velocities from a flow model with group velocities and a velocity floor, an alternative flow model and a coherent redshift shift as systematics. Secs. III.2 and IV.5: calibration zero points, filter wavelengths, primary-standard uncertainty and Galactic extinction as systematics in a covariance matrix, with each term's contribution to w listed |
| 10 | R. Kessler and D. Scolnic, Correcting type Ia supernova distances for selection biases and contamination in photometrically identified samples, Astrophys. J. 836, 56 (2017) | doi:10.3847/1538-4357/836/1/56 | abstract | Abstract: a Monte Carlo simulation corrects fitted light-curve parameters for selection effects; core-collapse contamination enters through classification probabilities; the method is tested with three intrinsic scatter models and two core-collapse rates |
| 11 | A. Conley et al., Supernova constraints and systematic uncertainties from the first three years of the Supernova Legacy Survey, Astrophys. J. Suppl. 192, 1 (2011) | doi:10.1088/0067-0049/192/1/1 | abstract | Abstract: the total systematic uncertainty is dominated by calibration terms; systematics are carried in a covariance matrix, propagated into the empirical light-curve models, and a host-mass correction is included |
| 12 | D. Scolnic et al., Supercal: cross-calibration of multiple photometric systems to improve cosmological measurements with type Ia supernovae, Astrophys. J. 815, 117 (2015) | doi:10.1088/0004-637X/815/2/117 | abstract | Abstract: inconsistent calibration between samples is a major systematic; cross-calibration to a common stellar survey finds offsets averaging about 10 mmag and up to 35 mmag; correcting them shifts w by about half its statistical error, depending strongly on the colour calibration of the nearby surveys |
| 13 | M. Betoule et al., Improved cosmological constraints from a joint analysis of the SDSS-II and SNLS supernova samples, Astron. Astrophys. 568, A22 (2014) | doi:10.1051/0004-6361/201423413 | abstract | Abstract: the change from an earlier result is attributed mainly to improved photometric calibration; the recalibration and inter-calibration of the two surveys were done blind to the cosmology analysis, and the full spectroscopically confirmed SDSS-II sample is added to the light-curve model training |
| 14 | D. O. Jones et al., Measuring dark energy properties with photometrically classified Pan-STARRS supernovae. II. Cosmological parameters, Astrophys. J. 857, 51 (2018) | doi:10.3847/1538-4357/aab6b1 | abstract | Abstract: a Bayesian method marginalises over core-collapse contamination in a mostly photometrically classified sample; alternative classification priors and contamination models each change w by at most 2%, and the contamination systematic is quantified |
| 15 | M. Vincenzi et al., The Dark Energy Survey supernova program: cosmological biases from supernova photometric classification, Mon. Not. R. Astron. Soc. 518, 1106–1127 (2022) | doi:10.1093/mnras/stac1404 | abstract | Abstract: core-collapse and peculiar type Ia events mistakenly included can bias cosmology; simulated contamination of 0.8 to 3.5% depends on the non-Ia models assumed; the bias on w is evaluated with a classifier and probabilistic fitting |
| 16 | A. Carr et al., The Pantheon+ analysis: improving the redshifts and peculiar velocities of type Ia supernovae used in cosmological analyses, Publ. Astron. Soc. Aust. 39, e046 (2022) | doi:10.1017/pasa.2022.41 | abstract | Abstract: a review of compiled redshifts found incorrect or missing heliocentric corrections, coordinates, frame redshifts and redshift uncertainties; exact frame conversions and an improved peculiar velocity model are used |
| 17 | E. R. Peterson et al., The Pantheon+ analysis: evaluating peculiar velocity corrections in cosmological analyses with nearby type Ia supernovae, Astrophys. J. 938, 112 (2022) | doi:10.3847/1538-4357/ac4698 | abstract | Abstract: separating expansion from peculiar motion below redshift 0.1 matters for H0 and w; combining group assignments with flow corrections reduces Hubble residual scatter and shifts H0; residual systematic uncertainties are quantified |
