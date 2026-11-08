---
id: T-ELECTRON-MICROSCOPY
name: Electron microscopy imaging and diffraction
type: technique
field: physics/condensed-matter
applies_when: the paper bases a claim about crystal structure, phase, atomic arrangement, defects, interfaces, strain, particle size or morphology on transmission or scanning electron microscopy images, scanning transmission images, or selected-area or convergent-beam electron diffraction patterns
version: "0.1"
---

# Electron microscopy imaging and diffraction

## 1. Specimen preparation

**Question.** Does the paper describe how the specimen was prepared (focused ion beam lift-out, ion milling, polishing, dispersion on a grid, protective or conductive layers), including the final thinning conditions, and does it show that the features claimed were not introduced by that preparation?

**Why it matters.** Focused ion beam milling can leave amorphous surface layers, implanted gallium, redeposited material and local mixing at interfaces, and these can look like structural or chemical features of the sample. Thinning a lamella can bend it, relax strain and open or close cracks, and protective caps can hide or alter the surface being studied.

**Resolved by.** The preparation route and its conditions stated, including the ion energy of the final thinning steps, any low-energy cleaning, the protective layer and the final thickness; claims about surface or interfacial layers, light-atom positions, strain or defect density checked against a second preparation route or against regions where preparation damage can be judged; the preparation history taken into account when a feature could have more than one origin.

**Benchmark.** [2], [3]

## 2. Electron dose and beam-induced change

**Question.** Does the paper report the electron dose (fluence, in electrons per unit area) and dose rate used for the images and patterns on which the claims rest, and does it show that the structure did not change during exposure?

**Why it matters.** The beam displaces atoms by knock-on collisions and breaks bonds by radiolysis, and for many materials the damage cannot be switched off, only kept within a dose budget. The dose at which a feature changes differs by many orders of magnitude between material classes, and damage shows up as fading diffraction spots, mass loss and changes in composition. Exposure during survey imaging, focusing and mapping can also produce new phases or morphologies that resemble the effect being claimed.

**Resolved by.** The accelerating voltage, fluence and flux stated for each data set, including the exposure used to find and focus the region; the first and later frames of a series, or a dose series, compared to show that the claimed features are stable; a critical dose measured or cited for the material and the recorded dose kept below it; low-dose or cryogenic methods used for sensitive materials.

**Benchmark.** [1], [3]

## 3. Interpreting image contrast

**Question.** Where a claim rests on what atomic columns, lattice fringes or intensity differences show (an atom type, a vacancy, a dopant site, an interface termination, a number of atoms), does the paper give the imaging conditions (defocus, aberrations, convergence and detector angles, thickness, orientation) and compare the images with simulations of the proposed structure and of the alternatives?

**Why it matters.** TEM and STEM images are two-dimensional projections of three-dimensional objects. HAADF intensity rises roughly as the square of the atomic number, but the dependence changes with the detector angles, peak intensities also depend on defocus, aberrations and small mistilt, and visual reading cannot separate columns that differ little in atomic number or are recorded at low signal-to-noise. Phase-contrast and ABF images depend further on the imaging conditions, specimen thickness and any amorphous surface layer.

**Resolved by.** The imaging parameters stated for each image; experimental images compared with simulations for the candidate structures over a range of thickness and defocus; intensities normalised to the incident beam, with the detector response characterised, where intensities are compared with simulation quantitatively; positions and compositions obtained by fitting a model to the image, with their precision stated, rather than by visual reading of peaks.

**Benchmark.** [3], [4], [5], [6]

## 4. Electron diffraction patterns

**Question.** Where phase, symmetry, superstructure or ordering is claimed from SAED or CBED patterns, does the paper state the area that contributed to each pattern and its orientation, and does it account for multiple scattering when it interprets reflection intensities or weak reflections?

**Why it matters.** Electron diffraction intensities are very sensitive to crystal symmetry and specimen thickness, and multiple (dynamical) scattering means they cannot in general be read as kinematic intensities; it is strongest in low-index zone-axis patterns, where it can level out or reorder intensities, and such patterns record few reflections. In SAED the aperture sits in an image plane, so the illuminated area is larger than the area selected.

**Resolved by.** The size of the selected or illuminated area given and compared with the grain, particle or feature of interest; patterns indexed at more than one orientation, or a tilt series reconstructed in three dimensions; for claims that rest on intensities (ordering, superstructure, site occupancy), precession or off-zone data and dynamical calculations rather than a kinematic reading; a phase assigned from cell parameters together with an independent measure of composition, not from one spacing; CBED used where point or space group symmetry is claimed.

**Benchmark.** [8], [9]

## 5. How much of the sample was examined

**Question.** For claims about size distributions, morphology, defect density or uniformity, how many particles, grains or regions were measured, from how many specimens or grid areas and image frames, how were the regions chosen, and what rules decided which objects were counted?

**Why it matters.** Electron microscopy examines a very small part of a sample, and a few high-magnification images may not stand for the rest. The number of particles needed for a reliable mean depends on the spread of the distribution, and rules for overlapping, touching, irregular or frame-cut particles change the result; overlapping particles also reduce the projected area. A small lamella suits atomic-scale work at a chosen site but may not represent the microstructure at larger scales.

**Resolved by.** The number of objects, frames and specimens stated, with the counting rules; several hundred particles measured where a size distribution is claimed, as in interlaboratory protocols; low-magnification overviews showing where the high-magnification images were taken; the fitted distribution and its spread reported, not only a mean; a larger cross-section or further sites examined where a claim concerns representative microstructure.

**Benchmark.** [3], [7]

## 6. SEM imaging: charging, coating and signal

**Question.** For SEM images used to claim morphology or dimensions, does the paper state the accelerating voltage, the detected signal (secondary or backscattered electrons), any conductive coating and its thickness, and show that charging did not distort the images?

**Why it matters.** Charging of poorly conducting samples brightens regions, distorts the image geometry and deflects the beam, which leads to measurement error. A conductive coating reduces charging, but the signal then comes partly from the coating, which can crack or change surface detail and adds its thickness to the size of every feature. Measured widths also depend on the signal and the edge criterion: with the same threshold, features appear larger in secondary-electron images than in backscattered-electron images.

**Resolved by.** Accelerating voltage, detector, coating material and coating thickness stated for each image; low landing energy, variable pressure or another charge-reduction method used for insulating samples, and the absence of charging distortion shown; coating thickness accounted for in quoted sizes; dimensions measured with a stated signal and edge criterion and, where accuracy matters, compared between signals or with modelling of the signal profile.

**Benchmark.** [10], [11]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Ilett et al., Analysis of complex, beam-sensitive materials by transmission electron microscopy and associated techniques, Phil. Trans. R. Soc. A 378, 20190601 (2020) | doi:10.1098/rsta.2019.0601 |
| 2 | J. Mayer et al., TEM sample preparation and FIB-induced damage, MRS Bull. 32, 400 (2007) | doi:10.1557/mrs2007.63 |
| 3 | C. Chen et al., Focused-ion-beam artifacts and evidence reliability in advanced microscopy of energy materials, Molecules 31, 2148 (2026) | doi:10.3390/molecules31122148 |
| 4 | S. Van Aert et al., Advanced electron crystallography through model-based imaging, IUCrJ 3, 71 (2016) | doi:10.1107/S2052252515019727 |
| 5 | J. M. LeBeau et al., Quantitative atomic resolution scanning transmission electron microscopy, Phys. Rev. Lett. 100, 206101 (2008) | doi:10.1103/PhysRevLett.100.206101 |
| 6 | J. M. LeBeau and S. Stemmer, Experimental quantification of annular dark-field images in scanning transmission electron microscopy, Ultramicroscopy 108, 1653 (2008) | doi:10.1016/j.ultramic.2008.07.001 |
| 7 | S. B. Rice et al., Particle size distributions by transmission electron microscopy: an interlaboratory comparison case study, Metrologia 50, 663 (2013) | doi:10.1088/0026-1394/50/6/663 |
| 8 | M. Gemmi et al., 3D electron diffraction: the nanocrystallography revolution, ACS Cent. Sci. 5, 1315 (2019) | doi:10.1021/acscentsci.9b00394 |
| 9 | P. A. Midgley and A. S. Eggeman, Precession electron diffraction – a topical review, IUCrJ 2, 126 (2015) | doi:10.1107/S2052252514022283 |
| 10 | M. T. Postek and A. E. Vladár, Does your SEM really tell the truth? How would you know? Part 4: Charging and its mitigation, Proc. SPIE 9636, 963605 (2015); read as the NIST author manuscript in PubMed Central | doi:10.1117/12.2195344 |
| 11 | M. T. Postek et al., Comparison of electron imaging modes for dimensional measurements in the scanning electron microscope, Microsc. Microanal. 22, 768 (2016) | doi:10.1017/S1431927616011430 |
