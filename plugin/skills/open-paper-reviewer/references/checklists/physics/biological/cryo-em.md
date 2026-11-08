---
id: T-CRYO-EM
name: Cryo-electron microscopy
type: technique
field: physics/biological
applies_when: the paper reports a three-dimensional map from single-particle cryo-electron microscopy, cryo-electron tomography or subtomogram averaging, quotes a resolution from a Fourier shell correlation, or builds an atomic model into such a map
version: "0.1"
---

# Cryo-electron microscopy

## 1. Resolution from the Fourier shell correlation, and overfitting

**Question.** Is the quoted resolution taken from the FSC between two half-maps refined independently from the start, with the threshold stated, full curves shown for masked and unmasked maps, and a test, such as high-resolution noise substitution, showing that neither noise built into the map nor the mask inflates it?

**Why it matters.** The FSC measures agreement between two maps, so it reports resolution only if the two maps were built without shared information, and the value read from it depends on the threshold. At high resolution the images contain far more noise than signal, and orientations refined against a map made from the same images can lock that noise into the map, which raises the FSC and gives a false impression of resolution. A tight or sharp-edged mask adds correlation of its own at high resolution, and a mask shared by both half-maps can make them look more similar than the data justify. Streaks and features finer than the claimed resolution are typical of overfitted noise.

**Resolved by.** A statement that the particles were split into two half-sets before any refinement, with any shared step named, or that orientation search was restricted to a lower resolution than the one claimed; the threshold stated and justified; FSC curves out to the Nyquist frequency for masked and unmasked half-maps; a soft mask whose shape and fall-off are given; an FSC corrected for the mask by phase randomisation or noise substitution beyond a stated resolution, with the uncorrected and noise-substituted curves shown; the unmasked map from the last refinement cycle deposited alongside the masked map.

**Benchmark.** [1], [2], [3], [4], [6]

## 2. Particle picking and reference bias

**Question.** How were particles picked and how were the initial references obtained, and does the paper show that the particles are visible in the micrographs and that the structure did not inherit its features from a template?

**Why it matters.** Aligning images of pure noise to a template and averaging them reproduces the template, so a map can look convincing while most of the data contain no particles. The risk is greatest for small, low-contrast particles and when particles are picked by matching to a template or an existing structure and then classified. The same bias arises in tomography when a known structure is used as a template or a starting reference.

**Resolved by.** Representative micrographs in which the particles can be seen, with picked positions marked; initial picking by hand or without a template, especially for small particles; no classification of template-picked particles without a test for reference bias; templates and starting references taken from existing structures heavily low-pass filtered; for small particles, the particle size and imaging conditions shown to give enough contrast to determine orientations.

**Benchmark.** [3], [8]

## 3. Particle selection, classification and heterogeneity

**Question.** Does the paper report how many particles were picked and how many were kept at each classification step, how the number of classes and the classes kept were chosen, and, where a distinct state is claimed, that it is supported by more than one classification run or setting?

**Why it matters.** Classification can separate conformations or assemblies that biochemistry could not, but its accuracy varies, especially for minor or sub-stoichiometric populations, and the number of classes and what counts as a real difference are choices left to the user. Discarding particles until the map looks best can remove real variability, and flexible or partly occupied regions end up at lower resolution or missing. In tomography, classifying small or rare particles in cells remains hard.

**Resolved by.** A processing flowchart with particle numbers and class choices at every step; the fraction of particles assigned to each state; a claimed state shown to persist when the number of classes, the mask or the starting reference is changed; flexible regions treated by focused classification or multi-body or continuous-heterogeneity methods, with the method named.

**Benchmark.** [4], [8]

## 4. Preferred orientation and anisotropic resolution

**Question.** Does the paper show the distribution of particle orientations and a measure of directional resolution, such as a three-dimensional FSC, and are the parts of the map a claim relies on unaffected by any anisotropy?

**Why it matters.** Particles that adsorb to the air-water interface or to a support film tend to lie in a few views, leaving some directions in Fourier space under-sampled. The map is then stretched along the poorly sampled direction, can show artefactual density and can report a high global resolution while being largely incorrect. A global FSC does not reveal this.

**Resolved by.** An angular distribution plot; a three-dimensional FSC or directional resolution analysis with a sphericity or similar measure; where orientation is strongly preferred, tilted data collection or other remedies, with the effect on directional resolution shown; a map-to-model FSC that agrees with the half-map FSC.

**Benchmark.** [4], [5]

## 5. Local resolution, sharpening and interpretation

**Question.** Does the paper report local resolution across the map, state how the map was sharpened, filtered and thresholded for display, and are the features it interprets consistent with the local resolution where they appear?

**Why it matters.** Resolution varies within a map, usually with a well-ordered core and less ordered periphery or flexible domains, and a single global value overstates the resolution of the weaker regions, which are often where the biological interest lies. Sharpening, filtering and the chosen contour level have no single standard and change what density appears, so interpretation of side chains, ligands or secondary structure must match what the local resolution supports.

**Resolved by.** A local resolution map, with the method and its parameters given; the masking, sharpening, filtering and display threshold stated; features interpreted only where the local resolution allows them, for example helical pitch and strand separation at resolutions better than about 4.5 Å; densities for ligands or small changes shown at several thresholds and in the half-maps.

**Benchmark.** [1], [4], [6]

## 6. Validation of atomic models built into the map

**Question.** Does the paper report how well the model fits the map, both globally and residue by residue, and its geometry, using measures that were not restrained during refinement?

**Why it matters.** Models built into maps at typical resolutions often contain peptide geometry errors, misoriented peptides, local sequence misalignment and missing ligands or ions. Different fit-to-map measures depend in different ways on resolution, background noise and threshold, and measures used as restraints during refinement, such as Ramachandran statistics, no longer test the model. A model refined against the full map can also be overfitted to its noise.

**Resolved by.** A map-to-model FSC compared with the half-map FSC; several complementary fit and geometry measures, such as a per-residue fit score, a side-chain measure, backbone conformation checks and clash scores; refinement against one half-map with the fit tested against the other; regions of poor fit or low local resolution identified in the model.

**Benchmark.** [1], [4], [7]

## 7. Tomography and subtomogram averaging

**Question.** For cryo-electron tomography, does the paper state the tilt range and scheme, how tilt series were aligned and corrected for the contrast transfer function, and how the missing wedge was handled in alignment and in interpreting the tomograms and averages?

**Why it matters.** Tilting is limited to about ±60°, so a wedge of views is missing; tomograms are smeared and their resolution is anisotropic, and this can hide particles in some orientations during picking and bias alignment. Tilt-series alignment errors and the defocus gradient across a tilted, thick specimen further limit resolution. Subtomogram averages need the same half-set separation and FSC reporting as single-particle maps.

**Resolved by.** The tilt range, increment, dose and alignment method stated; contrast transfer function correction described, including per-particle or three-dimensional correction where used; the missing wedge modelled in alignment and averaging; particles in many orientations averaged, or the remaining anisotropy shown; subtomogram averages refined from independent half-sets, with FSC and local resolution reported; features in raw tomograms interpreted with the anisotropy in mind.

**Benchmark.** [6], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | R. Henderson et al., Outcome of the first electron microscopy validation task force meeting, Structure 20, 205 (2012) | doi:10.1016/j.str.2011.12.014 |
| 2 | S. Chen et al., High-resolution noise substitution to measure overfitting and validate resolution in 3D structure determination by single particle electron cryomicroscopy, Ultramicroscopy 135, 24 (2013) | doi:10.1016/j.ultramic.2013.06.004 |
| 3 | R. Henderson, Avoiding the pitfalls of single particle cryo-electron microscopy: Einstein from noise, Proc. Natl. Acad. Sci. USA 110, 18037 (2013) | doi:10.1073/pnas.1314449110 |
| 4 | D. Lyumkis, Challenges and opportunities in cryo-EM single-particle analysis, J. Biol. Chem. 294, 5181 (2019) | doi:10.1074/jbc.REV118.005602 |
| 5 | Y. Z. Tan et al., Addressing preferred specimen orientation in single-particle cryo-EM through tilting, Nat. Methods 14, 793 (2017) | doi:10.1038/nmeth.4347 |
| 6 | A. Kucukelbir et al., Quantifying the local resolution of cryo-EM density maps, Nat. Methods 11, 63 (2014) | doi:10.1038/nmeth.2727 |
| 7 | C. L. Lawson et al., Cryo-EM model validation recommendations based on outcomes of the 2019 EMDataResource challenge, Nat. Methods 18, 156 (2021) | doi:10.1038/s41592-020-01051-w |
| 8 | E. Pyle and G. Zanetti, Current data processing strategies for cryo-electron tomography and subtomogram averaging, Biochem. J. 478, 1827 (2021) | doi:10.1042/BCJ20200715 |
