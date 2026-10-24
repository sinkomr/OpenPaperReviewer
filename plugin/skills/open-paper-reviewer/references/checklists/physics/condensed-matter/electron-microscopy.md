---
id: T-ELECTRON-MICROSCOPY
name: Electron microscopy imaging and diffraction
type: technique
field: physics/condensed-matter
applies_when: the paper bases a claim about crystal structure, phase, atomic arrangement, defects, interfaces, strain, particle size or morphology on transmission or scanning electron microscopy images, scanning transmission images, or selected-area or convergent-beam electron diffraction patterns
version: "0.1"
---

# Electron microscopy imaging and diffraction

Transmission electron microscopy (TEM), including high-resolution TEM (HRTEM), scanning TEM (STEM) with high-angle annular dark-field (HAADF) or annular bright-field (ABF) detectors, scanning electron microscopy (SEM), and selected-area (SAED) and convergent-beam (CBED) electron diffraction are used to claim crystal structure and phase, atomic arrangements at defects and interfaces, lattice spacings and strain, and particle size and morphology. Each of these claims is drawn from a small, thinned or coated region of the sample, recorded with an electron beam that can itself change that region.

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

## 4. Length calibration and scan distortion

**Question.** Where lattice spacings, strain, interface widths or particle sizes are measured from images, was the image scale calibrated against a standard under the same optical conditions, and for scanned images were drift and scan distortion measured and corrected?

**Why it matters.** The actual magnification at a given setting can differ from the indicated value by up to 10%. In scanned images, drift of the sample relative to the probe produces linear and non-linear distortions that change apparent spacings and angles, so a small strain or lattice change can be an artefact of the scan.

**Resolved by.** The calibration standard named and measured close in time to the data, at the same settings; the pixel size given and small compared with the feature measured; drift and scan distortion corrected, for example with image pairs recorded with orthogonal scan directions or a series with rotated scan directions, and the residual distortion checked from lattice angles.

**Benchmark.** [7], [8], [9]

## 5. Electron diffraction patterns

**Question.** Where phase, symmetry, superstructure or ordering is claimed from SAED or CBED patterns, does the paper state the area that contributed to each pattern and its orientation, and does it account for multiple scattering when it interprets reflection intensities or weak reflections?

**Why it matters.** Electron diffraction intensities are very sensitive to crystal symmetry and specimen thickness, and multiple (dynamical) scattering means they cannot in general be read as kinematic intensities; it is strongest in low-index zone-axis patterns, where it can level out or reorder intensities, and such patterns record few reflections. In SAED the aperture sits in an image plane, so the illuminated area is larger than the area selected.

**Resolved by.** The size of the selected or illuminated area given and compared with the grain, particle or feature of interest; patterns indexed at more than one orientation, or a tilt series reconstructed in three dimensions; for claims that rest on intensities (ordering, superstructure, site occupancy), precession or off-zone data and dynamical calculations rather than a kinematic reading; a phase assigned from cell parameters together with an independent measure of composition, not from one spacing; CBED used where point or space group symmetry is claimed.

**Benchmark.** [10], [11]

## 6. How much of the sample was examined

**Question.** For claims about size distributions, morphology, defect density or uniformity, how many particles, grains or regions were measured, from how many specimens or grid areas and image frames, how were the regions chosen, and what rules decided which objects were counted?

**Why it matters.** Electron microscopy examines a very small part of a sample, and a few high-magnification images may not stand for the rest. The number of particles needed for a reliable mean depends on the spread of the distribution, and rules for overlapping, touching, irregular or frame-cut particles change the result; overlapping particles also reduce the projected area. A small lamella suits atomic-scale work at a chosen site but may not represent the microstructure at larger scales.

**Resolved by.** The number of objects, frames and specimens stated, with the counting rules; several hundred particles measured where a size distribution is claimed, as in interlaboratory protocols; low-magnification overviews showing where the high-magnification images were taken; the fitted distribution and its spread reported, not only a mean; a larger cross-section or further sites examined where a claim concerns representative microstructure.

**Benchmark.** [3], [7]

## 7. SEM imaging: charging, coating and signal

**Question.** For SEM images used to claim morphology or dimensions, does the paper state the accelerating voltage, the detected signal (secondary or backscattered electrons), any conductive coating and its thickness, and show that charging did not distort the images?

**Why it matters.** Charging of poorly conducting samples brightens regions, distorts the image geometry and deflects the beam, which leads to measurement error. A conductive coating reduces charging, but the signal then comes partly from the coating, which can crack or change surface detail and adds its thickness to the size of every feature. Measured widths also depend on the signal and the edge criterion: with the same threshold, features appear larger in secondary-electron images than in backscattered-electron images.

**Resolved by.** Accelerating voltage, detector, coating material and coating thickness stated for each image; low landing energy, variable pressure or another charge-reduction method used for insulating samples, and the absence of charging distortion shown; coating thickness accounted for in quoted sizes; dimensions measured with a stated signal and edge criterion and, where accuracy matters, compared between signals or with modelling of the signal profile.

**Benchmark.** [12], [13]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Ilett, M. S'ari, H. Freeman, Z. Aslam, N. Koniuch, M. Afzali, J. Cattle, R. Hooley, T. Roncal-Herrero, S. M. Collins, N. Hondow, A. Brown and R. Brydson, Analysis of complex, beam-sensitive materials by transmission electron microscopy and associated techniques, Phil. Trans. R. Soc. A 378, 20190601 (2020) | doi:10.1098/rsta.2019.0601 | full text | Sec. 2: knock-on displacement and radiolysis as the main damage mechanisms; radiolysis shows as fading of diffraction spots, mass loss and composition change; critical fluence defined from the decay of a feature and about 1 to 15 e/Å² for biological material and down to about 0.2 e/Å² for some organic crystals, against above 10^7 e/Å² for transition metal oxides. Sec. 4: the fluence budget includes locating, aligning and focusing as well as recording. Sec. 11: radiolytic damage cannot be switched off, so work must fit a dose budget |
| 2 | J. Mayer, L. A. Giannuzzi, T. Kamino and J. Michael, TEM sample preparation and FIB-induced damage, MRS Bull. 32, 400–407 (2007) | doi:10.1557/mrs2007.63 | abstract | Abstract: reviews focused ion beam preparation of TEM specimens and names FIB-induced damage and gallium contamination among the problems of the method |
| 3 | C. Chen, L. Gao, J. Jia and Z. Ding, Focused-ion-beam artifacts and evidence reliability in advanced microscopy of energy materials, Molecules 31, 2148 (2026) | doi:10.3390/molecules31122148 | full text | Sec. 2: gallium FIB can produce amorphous layers, gallium implantation, redeposition and local mixing that may look meaningful; final thinning can bend lamellae, relax strain and open cracks; caps can mask surface features; SEM and ion beams can induce morphologies resembling the claimed feature; a phase seen after STEM may be dose-dependent. Sec. 5: ABF and phase-contrast assignment of light atoms is more sensitive to amorphisation, thickness and contamination than HAADF; small lamellae versus larger cross-sections for representative volumes |
| 4 | S. Van Aert, A. De Backer, G. T. Martinez, A. J. den Dekker, D. Van Dyck, S. Bals and G. Van Tendeloo, Advanced electron crystallography through model-based imaging, IUCrJ 3, 71–83 (2016) | doi:10.1107/S2052252515019727 | full text | Sec. 1: TEM and STEM give two-dimensional projections of three-dimensional objects; the dependence of contrast on atomic number varies with detector collection range. Sec. 3: a reconstructed exit wave is ideally free of imaging artefacts present in single images; statistical parameter estimation gives column positions with stated precision. Sec. 4: HAADF signal scales roughly with the square of atomic number; scattering cross-sections are robust to defocus, aberrations and small mistilt where peak intensities are not; model fitting separates columns that visual reading cannot |
| 5 | J. M. LeBeau, S. D. Findlay, L. J. Allen and S. Stemmer, Quantitative atomic resolution scanning transmission electron microscopy, Phys. Rev. Lett. 100, 206101 (2008) | doi:10.1103/PhysRevLett.100.206101 | abstract | Abstract: HAADF intensities placed on an absolute scale by normalising to the incident beam and compared directly with simulations for specimens up to about 120 nm thick, with close agreement once spatial incoherence is included |
| 6 | J. M. LeBeau and S. Stemmer, Experimental quantification of annular dark-field images in scanning transmission electron microscopy, Ultramicroscopy 108, 1653–1658 (2008) | doi:10.1016/j.ultramic.2008.07.001 | abstract | Abstract: method for normalising HAADF images to the incident beam; characterising detector linearity, saturation, uniformity, size and shape, which are needed as input for image simulations |
| 7 | S. B. Rice, C. Chan, S. C. Brown, P. Eschbach, L. Han, D. S. Ensor, A. B. Stefaniak, J. Bonevich, A. E. Vladár, A. R. Hight Walker, J. Zheng, C. Starnes, A. Stromberg, J. Ye and E. A. Grulke, Particle size distributions by transmission electron microscopy: an interlaboratory comparison case study, Metrologia 50, 663–678 (2013) | doi:10.1088/0026-1394/50/6/663 | full text | Sec. 2.3 (Calibration): actual magnification may differ from indicated by up to 10%; calibrate to a known length under similar optical conditions, with standards run near the time of the study. Sec. 1.2: the number of particles needed depends on the spread of the distribution. Sec. 2.4: at least 500 particles per laboratory in frames spread across the sample, pixel size specified, irregular particles not excluded, touching and frame-cut particles not reported, overlapping particles reduce projected area |
| 8 | C. Ophus, J. Ciston and C. T. Nelson, Correcting nonlinear drift distortion of scanning probe and scanning transmission electron microscopies from image pairs with orthogonal scan directions, Ultramicroscopy 162, 1–9 (2016) | doi:10.1016/j.ultramic.2015.12.002 | abstract | Abstract: unwanted motion of the probe relative to the sample causes linear and non-linear artefacts in STEM images; correction from orthogonal scan pairs |
| 9 | X. Sang and J. M. LeBeau, Revolving scanning transmission electron microscopy: correcting sample drift distortion without prior knowledge, Ultramicroscopy 138, 28–35 (2014) | doi:10.1016/j.ultramic.2013.12.004 | abstract | Abstract: sample drift distorts atomic-resolution images; a series with rotated scan directions measures drift from lattice vector angles and corrects the distortion without prior knowledge of the structure, giving picometre-level precision |
| 10 | M. Gemmi, E. Mugnaioli, T. E. Gorelik, U. Kolb, L. Palatinus, P. Boullay, S. Hovmöller and J. P. Abrahams, 3D electron diffraction: the nanocrystallography revolution, ACS Cent. Sci. 5, 1315–1329 (2019) | doi:10.1021/acscentsci.9b00394 | full text | Sec. 1: multiple scattering changes Bragg intensities, levelling them or scrambling their ranking, and is maximised in low-index zone-axis patterns; zone-axis data record few reflections; off-zone tilt series reconstructed in three dimensions. Sec. 2: in SAED the aperture is in an image plane, so the illuminated area is larger than the area selected. Sec. 3: dynamical refinement improves the accuracy of structure parameters over kinematic refinement. Sec. 4: phases in nanocrystalline mixtures identified from cell parameters combined with compositional analysis |
| 11 | P. A. Midgley and A. S. Eggeman, Precession electron diffraction – a topical review, IUCrJ 2, 126–136 (2015) | doi:10.1107/S2052252514022283 | full text | Sec. 1: electron diffraction intensities are very sensitive to crystal symmetry and thickness, and multiple scattering means they cannot in general be read kinematically; precession gives more kinematic-like intensities. Sec. 2: individual reflections can deviate strongly from kinematic values. Sec. 3.1: zone-axis patterns, especially combined with CBED, identify point and space groups |
| 12 | M. T. Postek and A. E. Vladár, Does your SEM really tell the truth? How would you know? Part 4: Charging and its mitigation, Proc. SPIE 9636, 963605 (2015); read as the NIST author manuscript in PubMed Central | doi:10.1117/12.2195344 | full text | Sec. 2.2.2.1: negative charging brightens the image, distorts its geometry and deflects the beam. Sec. 3.1: low landing energy reduces charging. Sec. 3.2: with a coating, the signal comes mainly from the coating, which can crack, change surface detail and enlarge features by its thickness. Secs. 3.3.1 to 3.3.5: variable pressure and other mitigation. Sec. 2.2.2.1 and Sec. 5: charging deflection leads to dimensional measurement error |
| 13 | M. T. Postek, A. E. Vladár, J. S. Villarrubia and A. Muto, Comparison of electron imaging modes for dimensional measurements in the scanning electron microscope, Microsc. Microanal. 22, 768–777 (2016) | doi:10.1017/S1431927616011430 | full text | Abstract and Discussion: with a 50% threshold criterion, lines appear consistently larger in secondary-electron images than in backscattered or low-loss images recorded at the same time; modelling attributes the differences to beam size and sidewall angle, so measured widths depend on the signal and edge criterion |
