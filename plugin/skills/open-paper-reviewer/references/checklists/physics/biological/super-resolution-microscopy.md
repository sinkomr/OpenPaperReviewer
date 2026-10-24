---
id: T-SUPER-RESOLUTION-MICROSCOPY
name: Super-resolution fluorescence microscopy
type: technique
field: physics/biological
applies_when: the paper uses single-molecule localization microscopy (PALM, STORM, DNA-PAINT), STED, structured illumination or expansion microscopy, or bases a claim about nanoscale structure, distances, molecular counts, clustering or resolution on super-resolved fluorescence images
version: "0.1"
---

# Super-resolution fluorescence microscopy

Super-resolution fluorescence microscopy is used to claim the size, shape and arrangement of structures below the diffraction limit of about 250 nm, distances between molecules, molecular counts and clustering. The main families are single-molecule localization microscopy (SMLM, including photoactivated localization microscopy, PALM, stochastic optical reconstruction microscopy, STORM, and DNA points accumulation for imaging in nanoscale topography, DNA-PAINT), stimulated emission depletion (STED) microscopy, structured illumination microscopy (SIM) and expansion microscopy (ExM), each of which produces its image through a different chain of labelling, optics and computation.

## 1. Resolution claimed and how it was measured

**Question.** Is the quoted resolution a measured image resolution, not a localization precision, a best-case instrument figure or a value from a different sample, and how was it measured on the data that carry the claim: Fourier ring correlation on independent halves, separation of features at known distances, or another stated criterion?

**Why it matters.** Localization precision describes how well one emitter is placed; the image resolution also depends on how densely the structure is sampled by localizations and cannot be better than about 2.3 times the precision. Fourier ring correlation depends on a chosen threshold, can be inflated when the same molecule appears in both halves, and gives one number for an image whose resolution varies. Orientation, refractive index variation and aberrations in the actual sample can make the achieved resolution worse than the figure for a test object.

**Resolved by.** The resolution criterion named and applied to the images used for the claim; for SMLM, localization precision and labelling or localization density reported separately, with the density shown to be sufficient for the claimed resolution; Fourier ring correlation computed on statistically independent halves with the threshold stated and repeated localizations accounted for; where possible, a reference structure of known geometry, such as the nuclear pore complex, imaged under the same conditions and resolved at its known spacings.

**Benchmark.** [1], [2], [3], [7]

## 2. Label size, linkage error and labelling efficiency

**Question.** Which labels were used (primary and secondary antibodies, nanobodies, protein tags, fluorescent proteins), how far do they place the fluorophore from the target, what fraction of targets carries a detectable label, and was the fixation shown to immobilize the target, and are measured sizes, distances and counts corrected for or discussed in the light of these?

**Why it matters.** The fluorophore sits some distance from the target: about 10 nm for an antibody and more for indirect labelling, so a structure can appear wider than it is. Incomplete labelling causes missing structure and undercounting, and measured effective labelling efficiencies differ widely between labels, from about 20% to about 75% in one reference system. Fluorescent protein fusions can perturb the target, and incomplete fixation leaves membrane molecules mobile enough for antibody labelling to produce artificial clusters.

**Resolved by.** The labelling strategy and its expected linkage error stated, and taken into account when sizes or distances are quoted; smaller labels used where the claim depends on a few nanometres; labelling efficiency measured, for example on a reference structure, or its effect on the claim discussed; evidence that tagging does not change the target's localization or copy number; a fixation protocol suited to the target, such as aldehyde fixation long enough to immobilize membrane components.

**Benchmark.** [1], [3], [5]

## 3. Drift, channel registration and three-dimensional calibration

**Question.** How was sample drift measured and corrected during acquisition (fiducial markers, cross-correlation of the localizations, active stabilization), in three dimensions where relevant, how large is the residual drift compared with the claimed resolution, how was the axial position calibrated for three-dimensional data, and, where distances or colocalization between colour channels are reported, how were the channels registered?

**Why it matters.** Uncorrected drift over a long acquisition blurs the image by tens of nanometres; correction from the localizations themselves works only for suitable, redundant structures, and high-frequency vibration cannot be removed afterwards. Axial drift degrades even two-dimensional images. A refractive-index mismatch between sample and immersion medium and the resulting aberrations distort axial distances unless the point spread function model is calibrated, and an uncorrected measurement can understate an axial distance by more than 10%. Chromatic aberration shifts one colour channel against another, which biases distances and colocalization between differently coloured labels.

**Resolved by.** The drift correction method stated, with fiducials that remain visible for the whole acquisition or a justification for correction from the data; the residual drift quantified; three-dimensional drift correction where possible; for three-dimensional imaging, an axial calibration with markers at known heights and a check of the refractive-index correction, for example against a structure of known axial spacing; for multicolour data, chromatic aberration measured and corrected with multicolour beads, or avoided, for example by spectral demixing, and the residual registration error stated.

**Benchmark.** [1], [2], [3]

## 4. Emitter density and reconstruction artefacts

**Question.** For SMLM, was the density of active emitters per frame low enough for single-emitter fitting, or was a multi-emitter method used, and are the localization software, its filtering settings and the rendering method stated? For any method, was the super-resolved image compared with a diffraction-limited image of the same field?

**Why it matters.** When point spread functions overlap, two emitters are fitted as one at a wrong position, which blurs or bridges features such as crossing filaments. Strict filtering removes such errors but lowers sampling and makes dense regions look dimmer. Different localization and reconstruction algorithms applied to the same raw data give different errors at the same places, and structures can be missing or misrepresented in ways that are hard to see by eye.

**Resolved by.** Emitter density per frame reported; the software and every setting needed to repeat the reconstruction stated; for dense samples, a method suited to overlapping emitters and an acknowledgement of its lower resolution; the super-resolved image, blurred to diffraction-limited resolution, compared with a widefield or confocal image of the same field, for example as an error map, with disagreements discussed.

**Benchmark.** [1], [9]

## 5. Blinking, molecular counts and cluster analysis

**Question.** When the paper reports molecular counts, oligomeric states or clustering from SMLM data, how were repeated localizations of the same molecule handled, and does it show that the reported clustering exceeds what blinking, multiple labels per target and the chosen analysis parameters would produce from randomly distributed molecules?

**Why it matters.** A fluorophore that blinks, or a target carrying several labels, yields several localizations close together, which inflates counts and creates small clusters even when molecules are randomly distributed. Grouping localizations by a dark-time threshold trades double counting against merging neighbours and missed molecules. The results of cluster methods such as DBSCAN can change markedly with their user-chosen parameters, and Ripley's functions are biased near region edges without correction.

**Resolved by.** The blinking correction stated, such as a dark-time grouping chosen from measured photophysics, kinetic modelling, pair-correlation analysis or calibration with a counting standard; cluster analysis applied to simulated or measured random distributions with the same density, blinking and labelling as the sample, giving a baseline; analysis parameters stated and their effect on the result shown; edge corrections applied; counts calibrated against a structure of known copy number where absolute numbers are claimed.

**Benchmark.** [1], [3], [4], [5]

## 6. Structured illumination raw data and reconstruction

**Question.** For SIM, does the paper report checks on the raw data and on the reconstruction, such as modulation contrast, bleaching and drift between pattern phases, the Fourier spectrum of the reconstruction and a comparison with a widefield image generated from the raw data, and does it state the reconstruction software, the optical transfer function used and the filter settings?

**Why it matters.** SIM resolution gains are about twofold and come from computational reconstruction, which assumes a stable sample and an accurate model of the illumination pattern and optics. Refractive-index mismatch, low stripe contrast from out-of-focus light, bleaching, motion, saturated pixels and reconstruction filter settings produce artefacts such as repeated echoes, intensity dips and noise patterns that can resemble real structure.

**Resolved by.** Quantitative raw-data checks, for example a modulation contrast-to-noise map, intensity profiles over the pattern phases and angles, and a motion check; the reconstructed Fourier spectrum or a resolution estimate from it; the reconstruction compared with a pseudo-widefield image; the immersion medium and optical transfer function matched to the sample and the reconstruction parameters reported.

**Benchmark.** [6], [7], [9]

## 7. Depletion power, bleaching and measured resolution in STED

**Question.** For STED, does the paper report the depletion and excitation powers, pulse and gating settings, and the resolution measured on the sample, for example from line profiles of features of known size, and does it show that photobleaching and the light dose did not alter the structure or the signal used for the claim?

**Why it matters.** STED resolution depends on driving depletion into saturation, so better resolution needs more depletion light, which increases bleaching and the energy load on the sample. Residual depletion light at the centre of the doughnut and time-gated detection both reduce the detected signal. A resolution quoted for test beads or isolated dyes may not hold in a labelled cell.

**Resolved by.** Laser powers, pulse lengths, gating and pixel dwell times stated; resolution measured in the sample, for example as the full width at half maximum of small isolated features, together with signal-to-noise; bleaching across the acquisition quantified; confocal images of the same field shown for comparison; for live samples, evidence that the illumination did not change the structure or the process studied.

**Benchmark.** [7], [8]

## 8. Expansion factor, isotropy and labels in expansion microscopy

**Question.** For ExM, how was the expansion factor measured for the samples that carry the claim, was distortion measured by imaging the same specimen before and after expansion, and does the effective resolution account for the label size and for any loss of label during gelation and digestion?

**Why it matters.** All distances are divided by the expansion factor, so an error in that factor passes directly into every size the paper reports, and the factor depends on gel chemistry. Expansion is designed to be isotropic, but distortions of a few percent are measured in cells and larger ones in tissue. The label is expanded together with the structure, so linkage error limits the effective resolution, and some fluorophores and epitopes are lost during polymerization and digestion.

**Resolved by.** The expansion factor measured for the relevant specimens and stated with its spread; distortion quantified by registering pre- and post-expansion images of the same specimen, or by imaging a structure of known size, reported as a measurement error against length scale; the label size and labelling stage (before or after expansion) stated and considered in the effective resolution; label retention checked; where possible, comparison with another super-resolution method on the same structure.

**Benchmark.** [1], [10], [11]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Lelek, M. T. Gyparaki, G. Beliu, F. Schueder, J. Griffié, S. Manley, R. Jungmann, M. Sauer, M. Lakadamyali and C. Zimmer, Single-molecule localization microscopy, Nat. Rev. Methods Primers 1, 39 (2021); read as the author manuscript in PubMed Central (PMC9160414) | doi:10.1038/s43586-021-00038-x | full text | Box 1: resolution cannot beat about 2.3 times the localization precision, needs sufficient sampling (fivefold oversampling suggested over the Nyquist criterion); Fourier ring correlation needs a user-set threshold and hides spatial variation; resolving structures at known distances is most convincing, with nuclear pores as a reference. "Fluorescent labelling strategies": antibodies add about 10 nm, up to about 20 nm for indirect labelling; fluorescent proteins can perturb the target. "Fixed samples": residual mobility of membrane components lets antibodies form clusters and other artefacts, so aldehyde fixation of sufficient duration is advised. Box 2 and "Co-localization analyses": multicolour imaging suffers chromatic aberration, which must be measured and corrected with multicolour beads or avoided by spectral demixing. "Identifying clusters and counting molecules": blinking creates artefactual clusters and inflated counts; corrections by calibration standards, kinetic modelling, pair correlation, qPAINT. "Limitations and optimizations": drift by fiducials or cautious cross-correlation, 3D drift correction, vibration not correctable; axial distortion from refractive-index mismatch needs calibration with markers at known heights; overlapping emitters fitted as one at a wrong position, filtering lowers sampling and dims dense regions, compare blurred image with widefield; label loss and added linkage error in expansion SMLM. "Reproducibility and data deposition": software and settings to report |
| 2 | R. P. J. Nieuwenhuizen, K. A. Lidke, M. Bates, D. Leyton Puig, D. Grünwald, S. Stallinga and B. Rieger, Measuring image resolution in optical nanoscopy, Nat. Methods 10, 557–562 (2013); read as the author manuscript in PubMed Central (PMC4149789) | doi:10.1038/nmeth.2448 | full text | Introduction and Results: localization precision alone does not set resolution, which also depends on labelling density (density-limited and precision-limited regimes); Fourier ring correlation from two independent halves with a 1/7 threshold; repeated localizations of the same emitter correlate the halves and inflate the resolution, with a correction; drift correction improved the measured resolution from 79 to 54 nm in an example |
| 3 | J. V. Thevathasan, M. Kahnwald, K. Cieśliński, P. Hoess, S. K. Peneti et al., Nuclear pores as versatile reference standards for quantitative superresolution microscopy, Nat. Methods 16, 1045–1053 (2019); read as the author manuscript in PubMed Central (PMC6768092) | doi:10.1038/s41592-019-0574-9 | full text | Results: Nup96 in the nuclear pore (two rings about 49 nm apart, eight corners) as a resolution and 3D calibration standard; astigmatic 3D imaging gave a ring spacing of 42.1 nm instead of 49.3 nm until aberration-induced fitting errors were corrected and the refractive-index factor calibrated; effective labelling efficiencies from about 21% to 74% depending on label; use as a counting reference; incomplete labelling undercounts, reactivation overcounts; C-terminal tagging can change measured copy number |
| 4 | P. Annibale, S. Vanni, M. Scarselli, U. Rothlisberger and A. Radenovic, Quantitative photo activated localization microscopy: unraveling the effects of photoblinking, PLoS ONE 6, e22678 (2011) | doi:10.1371/journal.pone.0022678 | full text | Results and Discussion: blinking makes one molecule appear as several, giving overcounting and small apparent clusters that disappear as the dark-time threshold is raised; a long threshold merges neighbours and misses molecules; off-time behaviour read from how the count changes with the threshold; clustering can be judged only once the same molecule is no longer counted several times |
| 5 | I. M. Khater, I. R. Nabi and G. Hamarneh, A review of super-resolution single-molecule localization microscopy cluster analysis and quantification methods, Patterns 1, 100038 (2020) | doi:10.1016/j.patter.2020.100038 | full text | Sections on multiple blinking, density-based clustering, Ripley's functions and detection efficiency: blinking and multiple probes per target create pseudoclusters; DBSCAN results can change markedly with its parameters; edge effects bias Ripley's K; comparison with complete spatial randomness; displaced labels enlarge apparent clusters; validation with simulations, DNA origami and electron microscopy |
| 6 | G. Ball, J. Demmerle, R. Kaufmann, I. Davis, I. M. Dobbie and L. Schermelleh, SIMcheck: a toolbox for successful super-resolution structured illumination microscopy, Sci. Rep. 5, 15915 (2015) | doi:10.1038/srep15915 | full text | Introduction and Results: artefacts hard to distinguish from real structure arise from refractive-index mismatch (echoes, intensity dips), low modulation contrast, bleaching, motion, illumination variation, saturation and Wiener filter settings; recommended checks include modulation contrast-to-noise maps, reconstructed Fourier plots, pseudo-widefield comparison and intensity histograms |
| 7 | L. Schermelleh, R. Heintzmann and H. Leonhardt, A guide to super-resolution fluorescence microscopy, J. Cell Biol. 190, 165–175 (2010) | doi:10.1083/jcb.201002018 | full text | STED section: resolution relies on saturated depletion, absorption of depletion light can cause severe bleaching, Table I rates the energy load high. SIM section: about twofold gain, reconstruction carries a risk of artefacts, sample must be stable. Localization section: precision scales with inverse square root of photon number and quoted values are not necessarily resolution. Resolution discussion: different criteria, and orientation, refractive index and aberrations in the sample reduce achieved resolution |
| 8 | J. Oracz, V. Westphal, C. Radzewicz, S. J. Sahl and S. W. Hell, Photobleaching in STED nanoscopy and its dependence on the photon flux applied for reversible silencing of the fluorophore, Sci. Rep. 7, 11354 (2017) | doi:10.1038/s41598-017-09902-x | full text | Introduction and Results: higher resolution needs higher depletion pulse energies, and bleaching scales with peak depletion intensity with an effective order above one; residual intensity at the doughnut centre removes much of the fluorescence at high resolution; time gating keeps resolution but cuts signal; resolution defined as full width at half maximum of the fluorescence profile |
| 9 | S. Culley, D. Albrecht, C. Jacobs, P. M. Pereira, C. Leterrier, J. Mercer and R. Henriques, Quantitative mapping and minimization of super-resolution optical imaging artifacts, Nat. Methods 15, 263–266 (2018); read as bioRxiv preprint doi:10.1101/158279 (v2) | doi:10.1038/nmeth.4605 | full text | Introduction and Results: missing or misrepresented structures are found by comparing a super-resolved image, convolved to lower resolution, with a diffraction-limited image of the same field as an error map; errors concentrate at dense filament crossings; different reconstruction algorithms on the same data give different errors at the same place; tested on localization, SIM and STED images |
| 10 | F. Chen, P. W. Tillberg and E. S. Boyden, Expansion microscopy, Science 347, 543–548 (2015); read as the author manuscript in PubMed Central (PMC4312537) | doi:10.1126/science.1260088 | full text | Fig. 2 and text: the same specimen imaged before and after expansion, registered non-rigidly to give a distortion field and measurement error against length; errors about 1% in cells and 2–4% in brain tissue; all post-expansion distances divided by the expansion factor of about 4 to 4.5; effective resolution estimate ignoring the label width |
| 11 | A. T. Wassie, Y. Zhao and E. S. Boyden, Expansion microscopy: principles and uses in biological research, Nat. Methods 16, 33–41 (2019); read as the author manuscript in PubMed Central (PMC6373868) | doi:10.1038/s41592-018-0219-4 | full text | Principles and resolution sections: expansion factor set by gel chemistry, distortions of a few percent, assessed by registration and comparison with other super-resolution images; effective resolution is the diffraction limit divided by the expansion factor but worse in practice because antibody labels are large; some dyes and epitopes are lost during polymerization and digestion |
