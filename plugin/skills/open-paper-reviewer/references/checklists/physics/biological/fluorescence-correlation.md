---
id: T-FLUORESCENCE-CORRELATION
name: Fluorescence correlation spectroscopy and diffusion
type: technique
field: physics/biological
applies_when: the paper reports diffusion coefficients, mobilities, concentrations or binding from fluorescence correlation or cross-correlation spectroscopy, fluorescence recovery after photobleaching or single-particle tracking, or claims anomalous diffusion, confinement, binding or crowding from such data
version: "0.1"
---

# Fluorescence correlation spectroscopy and diffusion

Fluorescence correlation spectroscopy (FCS), fluorescence cross-correlation spectroscopy (FCCS), fluorescence recovery after photobleaching (FRAP) and single-particle tracking (SPT) are used to claim diffusion coefficients, concentrations, bound fractions and residence times, and modes of motion such as anomalous diffusion, confinement or crowding. Each infers these from a model fitted to a correlation curve, a recovery curve or a set of trajectories, so the result depends on calibration, photophysics and the model chosen.

## 1. Calibration of the observation volume

**Question.** How were the size and shape of the observation volume determined (reference dye and the diffusion coefficient and temperature assumed for it, bead scans, or a calibration-free method), and were the calibration and the sample measured under the same optical conditions: coverslip, refractive index of the medium, depth, pinhole and alignment?

**Why it matters.** Single-focus FCS returns a diffusion time, and converting it to a diffusion coefficient or a concentration needs the size of the observation volume, so most measurements are relative to a reference. The volume often departs from the assumed three-dimensional Gaussian and changes with coverslip thickness, refractive-index mismatch, pinhole size, aberrations and saturation, which shifts diffusion times and can add apparent components. A calibration in water does not automatically carry over to a cell or a gel.

**Resolved by.** The reference dye, the literature value of its diffusion coefficient and the temperature stated; the beam waist and structure parameter reported; the calibration repeated on the day under matching conditions (same coverslip, correction collar and depth); where absolute values matter, a check by an independent route such as a dilution series, bead scans, dual-focus or scanning FCS.

**Benchmark.** [1], [2], [3], [4], [5], [6]

## 2. Excitation power, saturation, photobleaching and background

**Question.** Does the paper give the excitation power at the sample and show that the diffusion time, the number of molecules and the molecular brightness do not change with power over the range used, does it check for photobleaching during the measurement, and does it correct the correlation amplitude for uncorrelated background before deriving concentrations?

**Why it matters.** Optical saturation changes the effective observation volume and the amplitude and shape of the correlation curve, so FCS results depend on excitation power and accurate diffusion coefficients become hard to obtain. Photobleaching distorts the intensity trace and the correlation amplitude, and in a small compartment it depletes the pool of fluorophores. Uncorrelated background such as autofluorescence lowers the correlation amplitude and so inflates the apparent number of molecules.

**Resolved by.** The power at the sample stated for calibration and sample alike; a power series showing that diffusion time and molecule number are independent of power at the level used, or a saturation correction calibrated from count rate against power; intensity traces shown stable over each measurement; bleaching corrected or shown to be negligible; background measured on unlabelled samples and corrected for in concentrations and brightness.

**Benchmark.** [3], [6], [7], [8], [9]

## 3. Photophysics in the correlation curve

**Question.** Which terms besides translational diffusion does the fit model contain (triplet, blinking, protonation), how were their amplitudes and relaxation times constrained, and are they shown to be separated in time from the diffusion component?

**Why it matters.** Triplet transitions and other dark states make fluorophores blink and add fast relaxation terms to the correlation curve; in fluorescent proteins, protonation of the chromophore adds pH-dependent blinking on tens to hundreds of microseconds with a large dark fraction at low pH. Left out of the model, or absorbed into a free anomalous exponent or an extra diffusion component, these terms bias the diffusion time and the concentration.

**Resolved by.** The full fit function written out; blinking terms included, with their relaxation times compared with the diffusion time; their dependence on excitation power or pH checked; residuals shown across the full range of lag times.

**Benchmark.** [8], [10], [11]

## 4. Normal, anomalous or multi-component models in FCS

**Question.** When a correlation curve is fitted with an anomalous exponent or with several diffusing components, does the paper compare the alternative models, show that the lag-time range is wide enough to tell them apart, and test the choice independently, for example by varying the size of the observation volume?

**Why it matters.** An apparent exponent below one can also come from a mixture of species with different diffusion coefficients, from an observation volume that is not Gaussian, or from drift and other artefacts, and different models can fit the same curve about equally well while giving very different parameters. Slow anomalous transport can be measured reliably only from data that span several decades of time.

**Resolved by.** Fits and residuals for normal, two-component and anomalous models shown side by side; the lag-time range stated; measurements at several beam waists giving a diffusion law (diffusion time against the area of the observation volume) consistent with the claimed mode of motion; the exponent not used to absorb drift or photophysics.

**Benchmark.** [1], [11], [12], [13]

## 5. Localisation error, motion blur and fitting in single-particle tracking

**Question.** For diffusion coefficients and exponents from trajectories, does the paper give the localisation precision, the exposure time and frame interval, the distribution of trajectory lengths and the range of lag times fitted, and does the estimator account for localisation error and motion blur?

**Why it matters.** Localisation noise adds an offset to the mean squared displacement and blur during the exposure distorts it, so a mean squared displacement fitted without them gives biased diffusion coefficients and exponents, typically underestimating the exponent. The result depends strongly on how many lag times are fitted, and short or noisy trajectories give unreliable estimates.

**Resolved by.** Localisation precision measured, for example on immobilised particles; the fitting range chosen by a stated rule and reported; an estimator that includes localisation error and blur, or the offset subtracted with a measured precision; simulations with matched noise and trajectory length showing that the analysis recovers known values.

**Benchmark.** [14], [15], [16], [17]

## 6. From an exponent or a track shape to a mechanism

**Question.** When the paper concludes that motion is confined, directed or follows a particular anomalous-diffusion mechanism, what evidence beyond the exponent of the mean squared displacement supports it, and how likely are the observed track shapes for ordinary Brownian motion?

**Why it matters.** Different mechanisms, such as continuous-time random walks, fractional Brownian motion and obstructed diffusion, can give the same exponent and differ instead in ergodicity and in their displacement distributions. Unobstructed random walks can look confined or directed by chance, so classifying individual tracks by eye or by a threshold needs a statistical test.

**Resolved by.** Time-averaged and ensemble-averaged mean squared displacements compared; displacement distributions or other statistics that separate the candidate models shown; classification thresholds derived from simulated Brownian tracks of the same length and noise; the fraction of tracks in each class reported along with its sensitivity to the threshold.

**Benchmark.** [11], [17], [18]

## 7. Bleach geometry, timing and the recovery model in FRAP

**Question.** For diffusion or binding parameters from FRAP, does the paper report the bleach region and its measured profile, the bleach and imaging durations, the correction for bleaching during acquisition and the model fitted, and does it show that the system is in the regime the model assumes?

**Why it matters.** Finite bleach and scan times let molecules move during the bleach, and analyses that ignore this can substantially underestimate diffusion coefficients. FRAP models rest on different assumptions: diffusion contributes to many recoveries and can hide binding kinetics, and an incomplete recovery is easily confused with slow anomalous recovery unless the measurement runs long enough.

**Resolved by.** Bleach region size and shape with the measured post-bleach profile; normalisation and acquisition-bleaching corrections described; recovery followed to a plateau; the dependence on bleach-spot size tested to separate diffusion from binding; the model's assumptions stated and checked for self-consistency.

**Benchmark.** [11], [13], [19], [20], [21]

## 8. Binding and crowding as explanations for slow diffusion

**Question.** When slower or anomalous diffusion is attributed to binding, complex formation or crowding, does the paper measure a matched inert tracer or a binding-deficient variant, and are bound fractions and residence times checked with another technique or kinetic model?

**Why it matters.** Different kinetic models can fit the same FRAP or FCS data equally well while giving residence times that differ by an order of magnitude or more, and estimates for the same protein have differed between studies for technical reasons. Anomalous diffusion is not found everywhere in cells, and where it is attributed to crowding its degree depends on the tracer size and the protein concentration; in cross-correlation binding assays, spectral cross-talk, incomplete labelling and background change the apparent bound fraction.

**Resolved by.** Inert tracers of several sizes or a binding-deficient variant measured in the same cells; the kinetic model supported by independent data such as single-molecule residence times; bound fraction and residence time compared across techniques; for cross-correlation, cross-talk, degree of labelling and background measured and corrected.

**Benchmark.** [9], [13], [22], [23], [24]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | S. T. Hess and W. W. Webb, Focal volume optics and experimental artifacts in confocal fluorescence correlation spectroscopy, Biophys. J. 83, 2300–2317 (2002) | doi:10.1016/S0006-3495(02)73990-8 | abstract | Abstract: the usual three-dimensional Gaussian observation volume often fails under typical conditions; the resulting artefacts can mimic additional kinetics, shift diffusion times and distort axial ratios, and depend on detector aperture and illumination |
| 2 | J. Enderlein, I. Gregor, D. Patra, T. Dertinger and U. B. Kaupp, Performance of fluorescence correlation spectroscopy for measuring diffusion and concentration, ChemPhysChem 6, 2324–2336 (2005) | doi:10.1002/cphc.200500414 | abstract | Abstract: interpretation of FCS data depends strongly on the setup; wave-optical calculations of the effect of cover-slide thickness, sample refractive index, beam geometry, optical saturation and pinhole adjustment on the correlation function |
| 3 | S. Rüttinger, V. Buschmann, B. Krämer, R. Erdmann, R. Macdonald and F. Koberling, Comparison and accuracy of methods to determine the confocal volume for quantitative fluorescence correlation spectroscopy, J. Microsc. 232, 343–352 (2008) | doi:10.1111/j.1365-2818.2008.02105.x | abstract | Abstract: misalignment, aberrations, saturation and refractive-index variations in biological samples make the volume hard to determine in situ, usually restricting FCS to relative measurements; compares FCS fits, dilution series and bead scans |
| 4 | T. Dertinger, V. Pacheco, I. von der Hocht, R. Hartmann, I. Gregor and J. Enderlein, Two-focus fluorescence correlation spectroscopy: a new tool for accurate and absolute diffusion measurements, ChemPhysChem 8, 433–443 (2007) | doi:10.1002/cphc.200600638 | abstract | Abstract: two foci at a known separation give an internal length scale that is robust against the optical and photophysical artefacts of standard FCS; dye diffusion coefficient at a stated temperature agrees with pulsed-field-gradient NMR |
| 5 | Z. Petrášek and P. Schwille, Precise measurement of diffusion coefficients using scanning fluorescence correlation spectroscopy, Biophys. J. 94, 1437–1448 (2008) | doi:10.1529/biophysj.107.108811 | abstract | Abstract: fixed-volume FCS is mostly limited to relative measurements against a standard because the volume size is hard to determine; a calibrated scan radius supplies the length scale without a reference standard |
| 6 | L. Yu, Y. Lei, Y. Ma, M. Liu, J. Zheng, D. Dan and P. Gao, A comprehensive review of fluorescence correlation spectroscopy, Front. Phys. 9, 644450 (2021) | doi:10.3389/fphy.2021.644450 | full text | "Dual/Multi-Focus FCS": single-focus FCS needs a pre-calibrated focus size for quantitative analysis. "Summary": the observation volume changes with cover-slip thickness and index mismatch, and photobleaching at high excitation must be compensated in the trace and amplitude. "Dual-Color FCCS": autofluorescence background lowers correlation amplitudes |
| 7 | I. Gregor, D. Patra and J. Enderlein, Optical saturation in fluorescence correlation spectroscopy under continuous-wave and pulsed excitation, ChemPhysChem 6, 164–170 (2005) | doi:10.1002/cphc.200400319 | abstract | Abstract: FCS results depend on excitation power through optical saturation, which makes accurate diffusion coefficients difficult to obtain; the behaviour differs between continuous-wave and pulsed excitation |
| 8 | L. M. Davis and G. Shen, Accounting for triplet and saturation effects in FCS measurements, Curr. Pharm. Biotechnol. 7, 287–301 (2006) | doi:10.2174/138920106777950843 | abstract | Abstract: triplet transitions cause fast blinking, usually fitted with an exponential term; saturation also changes the amplitude and shape of the rest of the curve; a correction calibrated from count rate against laser power improves concentration and diffusion estimates |
| 9 | J. Ries, Z. Petrášek, A. J. García-Sáez and P. Schwille, A comprehensive framework for fluorescence cross-correlation spectroscopy, New J. Phys. 12, 113009 (2010) | doi:10.1088/1367-2630/12/11/113009 | abstract | Abstract: correlation curves analysed in the presence of spectral cross-talk, incomplete labelling, multiple binding sites, fluorescent background and depletion by photobleaching; dual-focus variant avoids chromatic-aberration and saturation artefacts and volume calibration |
| 10 | U. Haupts, S. Maiti, P. Schwille and W. W. Webb, Dynamics of fluorescence fluctuations in green fluorescent protein observed by fluorescence correlation spectroscopy, Proc. Natl. Acad. Sci. USA 95, 13573–13578 (1998) | doi:10.1073/pnas.95.23.13573 | abstract | Abstract: the autocorrelation of green fluorescent protein variants contains chemical relaxation terms besides diffusion; a protonation-linked term speeds from about 300 to 45 microseconds as pH falls, with the dark fraction rising to about 80 percent |
| 11 | F. Höfling and T. Franosch, Anomalous transport in the crowded world of biological cells, Rep. Prog. Phys. 76, 046602 (2013); read as arXiv:1301.6990 | doi:10.1088/0034-4885/76/4/046602 | full text | Abstract and Sec. II.2.2: models with identical mean squared displacements differ in their propagators. Preface: apparent subdiffusion can come from several species. Sec. IV.1: time and ensemble averages compared to test ergodicity. Sec. IV.2: the anomalous exponent should not absorb artefacts such as drift; the Gaussian assumption tested by varying the beam waist; slow transport needs several decades in time. Sec. IV.3: long FRAP measurements needed to separate stretched recovery from incomplete recovery |
| 12 | L. Wawrezinieck, H. Rigneault, D. Marguet and P.-F. Lenne, Fluorescence correlation spectroscopy diffusion laws to probe the submicron cell membrane organization, Biophys. J. 89, 4029–4042 (2005) | doi:10.1529/biophysj.105.067959 | abstract | Abstract: diffusion time plotted against the transverse area of the observation volume (the FCS diffusion law) distinguishes models of submicron confinement such as isolated domains and meshworks |
| 13 | D. Mazza, A. Abernathy, N. Golob, T. Morisaki and J. G. McNally, A benchmark for chromatin binding measurements in live cells, Nucleic Acids Res. 40, e119 (2012) | doi:10.1093/nar/gks701 | full text | Results and Fig. 1 legend: three kinetic models fitted FRAP and FCS data equally well but gave residence times from 0.4 to 6.3 s (FRAP) and 0.02 to 3.2 s (FCS); tracking thresholds changed bound fractions from 10 to 40 percent; choosing the model from single-molecule data brought bound fractions into agreement and residence times to within about a factor of two; a smaller FRAP spot lowered the residence time |
| 14 | X. Michalet, Mean square displacement analysis of single-particle trajectories with localization error: Brownian motion in an isotropic medium, Phys. Rev. E 82, 041914 (2010) | doi:10.1103/PhysRevE.82.041914 | abstract | Abstract: with localisation uncertainty, an unweighted least-squares fit of the mean squared displacement gives the best diffusion coefficient only if an appropriate number of points is fitted |
| 15 | A. J. Berglund, Statistics of camera-based single-particle tracking, Phys. Rev. E 82, 011917 (2010) | doi:10.1103/PhysRevE.82.011917 | abstract | Abstract: localisation noise and motion blur during the camera exposure introduce artefacts that standard mean-squared-displacement analyses do not fully handle; a maximum-likelihood estimator for diffusion coefficient and noise with a motion blur coefficient |
| 16 | E. Kepten, A. Weron, G. Sikora, K. Burnecki and Y. Garini, Guidelines for the fitting of anomalous diffusion mean square displacement graphs from single particle tracking experiments, PLoS ONE 10, e0117722 (2015) | doi:10.1371/journal.pone.0117722 | full text | Introduction: localisation error adds an offset to the time-averaged mean squared displacement, and small and large fitting ranges both bias the exponent. Results and Discussion: short trajectories and large errors give poor precision and negative bias. Conclusions: choose the fitting range by estimator efficiency and report the error and the selection method |
| 17 | G. Muñoz-Gil, G. Volpe, M. A. Garcia-March et al., Objective comparison of methods to decode anomalous diffusion, Nat. Commun. 12, 6253 (2021) | doi:10.1038/s41467-021-26320-w | full text | Introduction: different models give curves with the same scaling exponent, so the mean squared displacement alone says little about the mechanism; non-ergodic models make time and ensemble averages differ. Results: the mean-squared-displacement baseline underestimates the exponent because of localisation error, and accuracy falls for short, noisy tracks |
| 18 | M. J. Saxton, Lateral diffusion in an archipelago: single-particle diffusion, Biophys. J. 64, 1766–1780 (1993) | doi:10.1016/S0006-3495(93)81548-0 | abstract | Abstract: random walks in unobstructed systems show structure that could be read as obstructed, directed or confined motion, so interpretation must weigh the probability of each trajectory; probabilities of such apparent behaviour estimated |
| 19 | M. Weiss, Challenges and artifacts in quantitative photobleaching experiments, Traffic 5, 662–671 (2004) | doi:10.1111/j.1600-0854.2004.00215.x | abstract | Abstract: finite bleach and scan durations can make confocal FRAP substantially underestimate diffusion coefficients; diffusion, including diffusion-limited binding, can distort or mask binding kinetics; simulations recommended alongside experiments |
| 20 | B. L. Sprague, R. L. Pego, D. A. Stavreva and J. G. McNally, Analysis of binding reactions by fluorescence recovery after photobleaching, Biophys. J. 86, 3473–3495 (2004) | doi:10.1529/biophysj.103.026765 | abstract | Abstract: full reaction-diffusion solution for FRAP; diffusion should play a key role in many recoveries; limits on what can be estimated from FRAP data, with self-consistency checks and tests of the diffusion contribution |
| 21 | N. Lorén, J. Hagman, J. K. Jonasson, H. Deschout, D. Bernin et al., Fluorescence recovery after photobleaching in material and life sciences: putting theory into practice, Q. Rev. Biophys. 48, 323–387 (2015) | doi:10.1017/S0033583515000013 | abstract | Abstract: the many FRAP models rest on different assumptions, which makes the choice of model difficult; the review covers the theory and practical details needed for accurate measurements |
| 22 | F. Mueller, D. Mazza, T. J. Stasevich and J. G. McNally, FRAP and kinetic modeling in the analysis of nuclear protein dynamics: what do we really know?, Curr. Opin. Cell Biol. 22, 403–411 (2010) | doi:10.1016/j.ceb.2010.03.002 | abstract | Abstract: studies using different models reach very different binding estimates for the same or similar proteins, partly for technical reasons; reliable in vivo binding values need cross-validation with several experimental and modelling approaches |
| 23 | J. A. Dix and A. S. Verkman, Crowding effects on diffusion in solutions and cells, Annu. Rev. Biophys. 37, 247–263 (2008) | doi:10.1146/annurev.biophys.37.032807.125824 | abstract | Abstract: simulations predict anomalous diffusion with obstacles, but experiments in solutions and cell water compartments mostly show Brownian diffusion; crowding does not universally produce anomalous diffusion in cells, and the slowing is smaller than often assumed |
| 24 | M. Weiss, M. Elsner, F. Kartberg and T. Nilsson, Anomalous subdiffusion is a measure for cytoplasmic crowding in living cells, Biophys. J. 87, 3518–3524 (2004) | doi:10.1529/biophysj.104.044263 | abstract | Abstract: FCS and simulations relate cytoplasmic subdiffusion to crowding; the degree of anomaly depends on the size and conformation of the tracer and on the total protein concentration |
