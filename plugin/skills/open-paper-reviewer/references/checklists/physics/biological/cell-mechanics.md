---
id: T-CELL-MECHANICS
name: Cell mechanics
type: technique
field: physics/biological
applies_when: the paper reports a Young's modulus, stiffness, viscoelastic parameter, cortical tension or traction force of cells or soft tissue from atomic force microscope indentation, micropipette aspiration, traction force microscopy or a similar method, or compares cells by such values
version: "0.1"
---

# Cell mechanics

Atomic force microscope (AFM) indentation, micropipette aspiration and traction force microscopy (TFM) are used to claim the elastic modulus, viscoelastic parameters or cortical tension of cells and tissues, the forces that cells exert on their surroundings, and differences in these quantities between cell types, treatments or disease states. None of these quantities is measured directly: each comes from a measured deflection, aspirated length or bead displacement through a mechanical model of the probe, the cell and the substrate.

## 1. Cantilever and probe calibration

**Question.** For AFM measurements, how were the deflection sensitivity and the spring constant of the cantilever determined, and was the shape and size of the probe measured rather than taken from the manufacturer's nominal value?

**Why it matters.** The force and the indentation are both computed from the cantilever deflection, so an error in the deflection sensitivity passes into the spring constant and then into the modulus. In a comparison between laboratories measuring the same gels and cells, these two calibrations were the largest sources of error, and conventionally obtained sensitivities were nearly always off. The contact models also need the probe radius or cone angle, and an error in the probe geometry is a further systematic error.

**Resolved by.** The method for the deflection sensitivity (for example on a stiff, clean surface in the same liquid) and for the spring constant stated, with values and uncertainties; a cross-check of the two against each other or against a reference sample of known modulus; the probe geometry and radius stated, with how they were determined.

**Benchmark.** [1]

## 2. Contact model and indentation range

**Question.** Which contact model was used to convert force-indentation curves into a modulus, does it match the probe geometry, how was the contact point found, over what indentation range was the fit made, and what Poisson's ratio was assumed?

**Why it matters.** The Hertz and Sneddon models assume a linear, homogeneous, isotropic and very thick sample and an indentation small compared with the probe radius, and cells meet none of these conditions strictly. Applying a paraboloid or cone formula outside its range, or choosing a different fit range or contact point, changes the modulus, so values from different models or fitting choices are not directly comparable. Sharp tips can also strain soft samples beyond the linear range.

**Resolved by.** The model named with the probe geometry it assumes; the maximum indentation given relative to the probe radius and the sample height; the contact-point method and the fit range stated; example force curves with the fit overlaid; the assumed Poisson's ratio stated; the result described as an apparent modulus where the model's assumptions are not met.

**Benchmark.** [1], [2], [3]

## 3. Substrate effect and local cell height

**Question.** When cells or thin layers on a rigid support are indented, does the paper give the indentation and contact radius relative to the local sample height, and does it correct for the support or show that its influence is small?

**Why it matters.** Adherent cells are only a few micrometres thick, and their height varies several-fold between the edge and the nucleus. Models for an infinitely thick sample then overestimate the modulus, by an amount that grows with the ratio of contact radius to thickness and that is largest for large spherical probes. A cell that is thinner, or a measurement made nearer the edge, can therefore appear stiffer without any change in the material.

**Resolved by.** The local height measured at each indentation point, for example from the AFM topography; indentations kept to a small fraction of the height, or a finite-thickness (bottom-effect) correction applied with the probe geometry and the boundary condition stated; comparisons made at matched positions on the cell, such as above the nucleus.

**Benchmark.** [2], [3], [4]

## 4. Loading rate and viscoelasticity

**Question.** What indentation speed, loading rate or hold time was used, is it reported for every data set, and does the paper show how the result depends on it or fit a viscoelastic model when the material is clearly not elastic?

**Why it matters.** Cells are viscoelastic, so an elastic modulus from a single force curve is an apparent value that lies between the short-time and long-time moduli and depends on how fast the probe moved. Two cell types can have the same short-time modulus yet different apparent moduli because they relax differently. Hysteresis between approach and retraction shows that the elastic model leaves something out, and at high speeds the drag on the cantilever adds a further force.

**Resolved by.** The speed, ramp size and any dwell time stated; the same speed used for all groups that are compared; approach and retraction curves shown; either measurements at more than one rate, or a viscoelastic model (such as power-law or standard linear solid) fitted and its parameters reported; a hydrodynamic drag correction where speeds are high.

**Benchmark.** [2], [5], [6]

## 5. Model and geometry for micropipette aspiration

**Question.** For micropipette aspiration, which model links the aspirated length to a modulus, tension or viscosity, and are the pipette radius, the cell radius, the pressure and the range of aspirated length used in the fit stated and within that model's assumptions?

**Why it matters.** The widely used half-space elastic model ignores the finite size of the cell, so a difference in cell size relative to the pipette can be read as a difference in stiffness. Liquid-drop models describe some suspended cells but no longer apply once the cell flows into the pipette, and time-dependent creep needs a viscoelastic model. Adhesion of the membrane to the glass can raise the apparent stiffness.

**Resolved by.** The model named, with the ratio of cell to pipette radius and the fitted range of aspirated length relative to the pipette radius; a finite-size model where cells are small relative to the pipette; the pressure and how it was set; aspirated length against time shown, with a creep or viscoelastic analysis where the length keeps changing; steps taken to prevent adhesion to the pipette.

**Benchmark.** [7]

## 6. Substrate properties and reference state in traction force microscopy

**Question.** For TFM, were the Young's modulus, Poisson's ratio and thickness of the substrate measured for the gels actually used, how close to the surface are the tracked beads, and how was the force-free reference image obtained?

**Why it matters.** Tractions are computed from displacements through a model of the substrate, so they scale with the modulus that is assumed, and an error in Poisson's ratio or thickness changes the result further. Moduli taken from published recipes may not match the gels made in a given laboratory. Linear reconstructions also assume small strains and a purely elastic substrate, and beads that are not at the surface do not report the surface displacement.

**Resolved by.** The substrate modulus measured, for example by indentation, with its uncertainty; Poisson's ratio and thickness stated, with a finite-thickness model where the gel is thin; bead depth controlled or tracked; a reference image taken after the cell was removed or its contraction stopped; strains shown to stay in the linear regime, or a non-linear method used.

**Benchmark.** [8], [9]

## 7. Regularisation and resolution of traction reconstructions

**Question.** Which reconstruction method and regularisation were used, how was the regularisation parameter chosen, was it the same for all cells and conditions that are compared, and what are the spatial resolution and the noise floor of the traction maps?

**Why it matters.** Recovering tractions from noisy displacements is an ill-posed inverse problem, and the regularisation parameter strongly affects the result. Too little regularisation fits noise with large, scattered tractions; too much spreads small tractions over a wide area, and peak stresses can differ by orders of magnitude between the two. When the parameter is chosen by hand, differences between conditions can arise from that choice and not from the cells. Bead density and optical resolution limit how finely tractions can be resolved.

**Resolved by.** The method and regularisation named; the parameter value and the rule used to choose it, such as an L-curve or Bayesian criterion, stated, with whether it was fixed or set per image; tractions outside the cell boundary shown to be at the noise level; the bead density and the resulting resolution given; the method tested on simulated displacement fields with added noise.

**Benchmark.** [8], [9], [10]

## 8. Cell state, measurement location and comparability

**Question.** Does the paper state where on each cell the measurement was made and the conditions that change cell mechanics (substrate stiffness and other culture conditions), say how values from several positions or force curves were combined into one value per cell, show the spread between cells, and compare absolute values only with data taken by the same method and protocol?

**Why it matters.** Moduli of the same cell line measured by different methods can differ by about a thousandfold, because the applied stress, deformation rate, probe geometry, location in the cell and environment differ. Within one method, cells vary intrinsically, cell height and stiffness change across a cell, and the substrate changes cell spreading and force. A difference between groups can therefore come from where or under what conditions the cells were measured.

**Resolved by.** The measurement position and the culture and measurement conditions stated and matched between groups; distributions shown for all cells measured, not only means; comparisons with literature values framed as relative, or made with the same method and settings; for traction data, quantities such as total force or strain energy reported together with cell spread area and substrate stiffness.

**Benchmark.** [1], [4], [6], [9]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | H. Schillers et al., Standardized nanomechanical atomic force microscopy procedure (SNAP) for measuring soft and biological samples, Sci. Rep. 7, 5117 (2017) | doi:10.1038/s41598-017-05383-0 | full text | Abstract and Results: deflection sensitivity and the resulting spring constant are the main error sources between laboratories; nearly all conventionally obtained sensitivities needed correction; Discussion: with the corrected procedure, gel modulus errors fell from about 30% to 1%, and Results: consistency for cells improved about twofold. Introduction: tip geometry, tip velocity, sample position and choice of model as further error sources, and intrinsic inhomogeneity within a sample. Discussion: the Hertz model needs a linear response of an isotropic, homogeneous sample, and these assumptions do not strictly hold for cells |
| 2 | S. V. Kontomaris and A. Malamou, Hertz model or Oliver & Pharr analysis? Tutorial regarding AFM nanoindentation experiments on biological samples, Mater. Res. Express 7, 033001 (2020) | doi:10.1088/2053-1591/ab79ce | full text | Sec. 2.1.2: the Hertz model assumes indentation much smaller than the tip radius, a homogeneous, isotropic, linear-elastic half-space, and depth below about 5 to 10% of sample thickness; biological samples often do not meet these. Secs. 2.1.3 and 2.2: errors from the paraboloid approximation at larger depth relative to radius, and models giving systematically different moduli. Later sections: loading-unloading hysteresis from viscoelasticity changes the extracted stiffness, so ramp rate matters |
| 3 | E. K. Dimitriadis, F. Horkay, J. Maresca, B. Kachar and R. S. Chadwick, Determination of elastic moduli of thin layers of soft material using the atomic force microscope, Biophys. J. 82, 2798–2810 (2002) | doi:10.1016/S0006-3495(02)75620-8 | abstract | Abstract: sharp tips strain soft samples beyond the linear range, so spherical probes are proposed; the Hertz model gives significant errors for thin samples, with corrections for samples bonded and not bonded to a rigid substrate; error from uncertainty in the contact point estimated |
| 4 | P. D. Garcia and R. Garcia, Determination of the elastic moduli of a single cell cultured on a rigid support by force microscopy, Biophys. J. 114, 2923–2932 (2018) | doi:10.1016/j.bpj.2018.05.012 | full text | Abstract and Introduction: cell softness and thickness of 2 to 15 micrometres make infinite-thickness models unsuitable; Results and Discussion: Sneddon and Hertz models overestimate the modulus, by an amount set by the ratio of contact radius to cell thickness and growing with indentation for cones and spheres; cell thickness varies from about 2.5 micrometres at the edge to 10 above the nucleus; sharp high-aspect-ratio tips reduce the effect, while large colloidal probes make a correction necessary |
| 5 | Y. M. Efremov, W.-H. Wang, S. D. Hardy, R. L. Geahlen and A. Raman, Measuring nanoscale viscoelastic parameters of cells directly from AFM force-displacement curves, Sci. Rep. 7, 1541 (2017) | doi:10.1038/s41598-017-01784-3 | full text | Introduction: viscoelasticity shows as approach-retraction hysteresis and as speed dependence of the Hertz modulus. Discussion: the Hertz value is an apparent modulus between the instantaneous and long-term moduli and depends on indentation rate. Results: two cell lines with similar instantaneous moduli had Hertz moduli differing twofold because their power-law exponents differed. Methods: power-law and standard linear solid fits to approach and retraction together, data at several indentation times to tell models apart, and a hydrodynamic drag correction above 2 micrometres per second |
| 6 | P.-H. Wu, D. R.-B. Aroush, A. Asnacios, W.-C. Chen, M. E. Dokukin et al., A comparison of methods to assess cell mechanical properties, Nat. Methods 15, 491–498 (2018) | doi:10.1038/s41592-018-0015-1 | abstract | Abstract: six methods applied to the same breast cancer cell line gave elastic and viscous moduli spanning about 1,000-fold and 100-fold; the differences are attributed to applied stress and deformation rate, probe geometry, location probed in the cell and the extracellular environment |
| 7 | B. González-Bermúdez, G. V. Guinea and G. R. Plaza, Advances in micropipette aspiration: applications in cell biomechanics, models, and extended studies, Biophys. J. 116, 587–594 (2019) | doi:10.1016/j.bpj.2019.01.004 | full text | Section on continuum models: the half-space model is applied to nearly spherical cells, where finite cell size can be mistaken for a difference in rigidity; finite-size models and fitting ranges of aspirated length relative to pipette radius; creep functions for viscoelastic analysis. Section on subcellular models: the liquid-drop model fails once the cell flows freely into the pipette. Membrane adhesion to glass can inflate estimates; heterogeneity and cortex remodelling as sources of cell-to-cell variation |
| 8 | U. S. Schwarz and J. R. D. Soiné, Traction force microscopy on soft elastic substrates: a guide to recent computational advances, Biochim. Biophys. Acta Mol. Cell Res. 1853, 3095–3104 (2015); read as preprint arXiv:1506.02394 | doi:10.1016/j.bbamcr.2015.05.028 | full text | Sec. I: linear methods rely on the small-strain approximation. Sec. II: the inverse problem is ill-posed, small changes in displacement give large changes in force; substrate modulus, Poisson's ratio near 0.5 and thickness. Sec. III: Tikhonov regularisation and choice of its parameter by Bayesian or L-curve methods; resolution mainly set by bead density; the depth of the imaged beads must be tracked. Sec. IV: validation with simulated data with added noise. Sec. VI: substrate rigidity measured, reference image after cell removal, viscous components avoided, finite-thickness solutions needed for very thin substrates |
| 9 | A. K. Denisin, H. Kim, I. H. Riedel-Kruse and B. L. Pruitt, Field guide to traction force microscopy, Cell. Mol. Bioeng. 17, 87–106 (2024) | doi:10.1007/s12195-024-00801-6 | full text | Sections on data processing and choosing parameters: the regularisation parameter strongly influences traction magnitude, under- and over-regularisation give scattered or smeared tractions and peak stresses differing by orders of magnitude; many papers give a value without saying how it was chosen; state whether one value or per-image optimisation was used. Section on substrate properties: wrong modulus or Poisson's ratio enters the Green's function, so measure the gels directly; stiffness changes cell spreading and force. Section on representing data: total traction and strain energy as reported quantities |
| 10 | Y. Huang, C. Schell, T. B. Huber, A. N. Şimşek, N. Hersch, R. Merkel, G. Gompper and B. Sabass, Traction force microscopy with optimized regularization and automated Bayesian parameter selection for comparing cells, Sci. Rep. 9, 539 (2019) | doi:10.1038/s41598-018-36896-x | abstract | Abstract: traction reconstruction is poorly conditioned because of undersampling and noise; manually chosen regularisation parameters make results subjective and can cause systematic errors when comparing cells across conditions; automated Bayesian parameter selection reduces this |
