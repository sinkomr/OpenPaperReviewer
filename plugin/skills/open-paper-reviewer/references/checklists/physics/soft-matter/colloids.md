---
id: T-COLLOIDS
name: Colloidal systems
type: technique
field: physics/soft-matter
applies_when: the paper uses model colloidal particles, such as PMMA, polystyrene, silica or microgel spheres, and bases a claim on their volume fraction, interactions, phase behaviour, structure or dynamics, or on particle coordinates from confocal or video microscopy
version: "0.1"
---

# Colloidal systems

Experiments with model colloids, such as poly(methyl methacrylate) (PMMA), polystyrene, silica or microgel spheres, are used to claim phase behaviour, structure and dynamics that are compared with hard spheres or another model system, often from particle coordinates obtained by confocal microscopy. These claims depend on a particle size, a volume fraction and an interaction potential that are not measured directly and that each carry systematic uncertainty.

## 1. Particle size, polydispersity and swelling

**Question.** Which radius is quoted (hydrodynamic, core, core plus stabilising layer, or effective hard-sphere), by which method and in which solvent, and how was the polydispersity measured and reported?

**Why it matters.** Light scattering, electron microscopy and microscopy in the sample solvent give different radii for the same particles, because of the stabilising layer, drying and solvent uptake; particles can swell by several per cent or more over weeks in some solvent mixtures. Polydispersity raises the freezing and melting volume fractions, and a polydispersity of more than roughly 5 to 10 per cent strongly suppresses crystallisation, so the reference phase behaviour depends on it.

**Resolved by.** The sizing method and solvent stated, with the radius used for each derived quantity named; sizes measured in the solvent and at the time of the experiment, or a check that swelling had finished; polydispersity given as the standard deviation of the size distribution divided by the mean, with the distribution shown where it may be broad or bimodal; any comparison with theory or simulation made at the measured polydispersity.

**Benchmark.** [1], [3]

## 2. Volume fraction

**Question.** How was the volume fraction determined (from mass and density, from the fluid-crystal coexistence region, from a sediment assumed to be at random close packing, by counting particles in images, or by another route), and what systematic uncertainty does the paper attach to it?

**Why it matters.** Relative volume fractions within one stock can be very precise, but absolute values usually carry systematic errors of a few per cent, and each route rests on assumptions: dry and wet particles being equivalent, the reference volume fractions of a monodisperse system, the packing of a sediment, or a radius that enters the result cubed. Because the properties of dense suspensions change steeply with volume fraction, an error of this size can shift a result by a large factor.

**Resolved by.** The route described step by step with the reference values and radius it uses; a systematic uncertainty stated alongside the statistical one; where possible, two independent routes that agree; dilution series made from one calibrated stock, with its age and any swelling or evaporation addressed; claims phrased in terms that hold within the stated uncertainty.

**Benchmark.** [1], [3]

## 3. Interactions: charge, softness and attraction

**Question.** What is known about the interaction potential in the solvent used: the likely particle charge and screening (Debye) length, the softness of any stabilising layer, and any attraction from imperfect refractive-index matching or solvent uptake, and how was it checked?

**Why it matters.** Particles that are not perfectly hard need an effective diameter and volume fraction, and different mapping methods need not agree. The low-polarity solvent mixtures used to match density and refractive index for confocal microscopy often leave micron-sized particles strongly charged with long screening lengths; added salt shortens the screening length only so far, and some solvents swell the particles or cause attraction. Microgels and similar soft particles have an effective volume fraction that can itself depend on concentration.

**Resolved by.** The solvent, any added salt and an estimate of charge and screening length stated, with how they were obtained; the effective diameter and the mapping used to get it; a test of the interactions, such as the pair correlation function of a dilute sample, the positions of the freezing and melting points, or the crystal structure formed, compared with what a hard-sphere or other assumed potential predicts; for soft particles, the definition of volume fraction made explicit.

**Benchmark.** [2], [3]

## 4. Sedimentation and the gravitational length

**Question.** How large is the gravitational length (thermal energy divided by buoyant weight) compared with the particle size and the sample height, was the density matched and how closely, and how long was the sample left before measurement, at what height?

**Why it matters.** When the gravitational length is not large compared with the particle size, particles settle on the time scale of the experiment and the local volume fraction varies with height and time. Crystals then form first in layers at the bottom, and settling from an uneven start can make a single fluid look phase-separated, so a structure seen at one height or one time may not represent the nominal volume fraction. Density matching for larger particles usually requires solvents that bring in charge or swelling.

**Resolved by.** The particle and solvent densities and the resulting gravitational length or Péclet number given; the measurement height and time after mixing or shear melting stated; where settling is possible, the local volume fraction measured at the position imaged or a density profile shown; any calibration from crystal fraction corrected for compression of the sediment.

**Benchmark.** [1], [2], [3]

## 5. Particle location from confocal images

**Question.** How were particle coordinates obtained from the images, what are the location errors along and across the optical axis, what fraction of particles is missed or spurious, and how were these estimated?

**Why it matters.** Resolution is poorer along the optical axis than across it, and images of neighbouring particles overlap in dense samples, which pulls apparent positions together and adds spurious features below contact in the pair correlation function. Pixel bias, refractive-index mismatch and imaging deep in the sample worsen location further, and a small error in radius or a few per cent of missed particles changes a volume fraction found by counting. Static location error and particle motion during the exposure both bias the measured mean-squared displacement.

**Resolved by.** The locating algorithm, its parameters and the pixel size calibration stated; location errors estimated separately in the axial and lateral directions, for example from immobilised particles imaged under the same conditions or from the onset of the pair correlation function; checks for pixel bias and for missed or doubled particles; imaging depth, refractive-index matching and exposure time reported; dynamics corrected for static and dynamic error, or shown to be larger than them.

**Benchmark.** [1], [3], [4], [5]

## 6. Walls, equilibration and sample history

**Question.** How far from the cell walls were the data taken, how long was the sample equilibrated or aged after preparation or shear melting, and does the result depend on position or waiting time?

**Why it matters.** A flat wall orders the suspension next to it and can form crystalline layers below the bulk freezing volume fraction, and hydrodynamic interactions slow diffusion near a wall. Dense colloidal fluids and glasses age: relaxation slows with waiting time, the time to reach a stationary state grows with volume fraction, and the density reached by jamming depends on the preparation protocol. Data taken close to the coverslip or at one waiting time may therefore reflect the cell or the history, not the bulk state.

**Resolved by.** The distance from the walls stated, with data far enough from them or compared at several distances; wall coatings or roughness described where they matter; the preparation, shear-melting and waiting protocol given; measurements repeated at more than one waiting time, or a stationary state shown before the claimed property is measured.

**Benchmark.** [3]

## 7. Comparison with hard-sphere or other model behaviour

**Question.** When the paper compares its observations with hard-sphere or another model's phase behaviour, structure or dynamics, does it propagate the uncertainty in volume fraction, polydispersity and interactions into the comparison, and would the conclusion survive a shift of the volume fraction within that uncertainty?

**Why it matters.** Agreement or disagreement with a model is only as good as the mapping of the experiment onto it. Fixing the volume fraction from the freezing point and then claiming agreement near freezing is circular, polydispersity and softness both shift and narrow the coexistence region, and a change of about one per cent in volume fraction is enough to account for large apparent discrepancies between experiment and simulation in quantities that vary steeply with it. For dynamics, the comparison also depends on the time unit used to scale experiment onto simulation and on whether hydrodynamic interactions, omitted from many simulations, matter for the quantity compared.

**Resolved by.** The mapping, and which observations were used to calibrate it, kept separate from the observations used to test it; theory or simulation run at the measured polydispersity and with the estimated interaction, or the sensitivity to them shown; results plotted with the volume fraction uncertainty visible, or relative to a reference point such as freezing where that reduces the dependence on absolute values; for dynamics, the time unit stated (for example the free diffusion time from the measured size and solvent viscosity) and the role of hydrodynamics addressed; any departure from the model weighed against these sources before it is attributed to new physics.

**Benchmark.** [1], [2], [3]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | W. C. K. Poon, E. R. Weeks and C. P. Royall, On measuring colloidal volume fractions, Soft Matter 8, 21–30 (2012); read as preprint arXiv:1106.2566 | doi:10.1039/C1SM06083J | full text | Secs. III.1 to III.4: hydrodynamic, core, core-shell and effective radii differ; light scattering measures different radii from dried-particle electron microscopy; in a case study confocal radii exceeded light-scattering ones by about 10 nm or more. Secs. II and V.7: solvent swelling of up to 10 per cent or more over several weeks; a radius error of x per cent gives about 3x per cent or more in volume fraction. Secs. IV and V.2: polydispersity raises freezing and melting volume fractions; crystallisation fails above about 7 per cent. Secs. V.1 to V.4: mass and density (dry and wet particles assumed equivalent), coexistence (crystal sediment compression must be allowed for), centrifugation to an assumed random close packing, and confocal counting (edge and missed particles), each with its assumptions. Sec. V.8: relative values can be very precise but absolute ones carry systematic errors of about 3 to 6 per cent; a 1 per cent change can alter nucleation rates by orders of magnitude. Sec. VII: authors should report exactly how each volume fraction was obtained |
| 2 | C. P. Royall, W. C. K. Poon and E. R. Weeks, In search of colloidal hard spheres, Soft Matter 9, 17–27 (2013); read as preprint arXiv:1205.6665 | doi:10.1039/C2SM26245B | full text | Introduction and Sec. II: real colloids are never perfectly hard, so an effective diameter and volume fraction are needed; Sec. II.2: the dilute-limit pair correlation function gives the potential. Introduction: PMMA particles below about 400 nm sediment at most about a millimetre a day, larger ones need density-matching solvents that bring in charging. Sec. III.2: microgel swelling, and so effective volume fraction, can depend on conditions including concentration; softness and polydispersity both narrow the coexistence gap. Sec. IV.3: density-matching solvents leave micron particles with large charges and micron Debye lengths; added salt limits screening to about 100 nm; some solvents swell PMMA and cause attraction; charge shows as freezing near 0.4 and bcc crystals. Secs. V and VI: mappings to hard spheres are system- and approach-specific and none is entirely satisfactory |
| 3 | C. P. Royall, P. Charbonneau, M. Dijkstra, J. Russo, F. Smallenburg, T. Speck and C. Valeriani, Colloidal hard spheres: triumphs, challenges and mysteries, Rev. Mod. Phys. 96, 045003 (2024); read as preprint arXiv:2305.02452 | doi:10.1103/RevModPhys.96.045003 | full text | Sec. III.1: polydispersity defined as standard deviation over mean diameter, distributions can be bimodal. Secs. III.3 to III.5: charging always present, salt gives about 100 nm screening and notable softness, solvent uptake causes attraction; different mapping methods need not agree; volume fraction accuracy limited by softness, polydispersity and solvent age, about 1 per cent absolute achievable with care. Sec. IV.2: good data have position errors near 0.05 diameters and a few per cent missing or spurious particles. Sec. V.4: many simulations omit hydrodynamics, which can affect dynamics. Sec. VII.2: larger polydispersity strongly suppresses crystallisation, with a terminal value of about 5 to 12 per cent depending on the distribution. Sec. VII.4: dynamics compared after scaling by the free diffusion coefficient; hydrodynamic interactions lower short-time diffusion with volume fraction. Sec. VIII.1: walls promote crystal layers below bulk freezing, gravity freezes bottom layers first, diffusion slowed near walls. Sec. XI.1: gravitational length and Péclet number defined, settling profiles. Secs. XII.8 and XII.9: jammed densities depend on protocol, ageing. Sec. XIII.4: a shift of about 0.01 in volume fraction would largely remove the nucleation rate discrepancy with simulation |
| 4 | M. C. Jenkins and S. U. Egelhaaf, Confocal microscopy of colloidal particles: towards reliable, optimum coordinates, Adv. Colloid Interface Sci. 136, 65–92 (2008); read as preprint arXiv:0709.4052 | doi:10.1016/j.cis.2007.07.006 | full text | Secs. 2.3 and 3.1: axial resolution poorer than lateral. Secs. 3.1 and 3.3: index mismatch, concentration and depth reduce location reliability; pixel size calibration. Sec. 5: checks by brightness statistics, histogram of sub-pixel positions for pixel bias, pair-correlation onset, Voronoi volumes for missed particles. Sec. 6.3: overlapping particle images make apparent separations too small and add spurious pair correlations below contact |
| 5 | T. Savin and P. S. Doyle, Static and dynamic errors in particle tracking microrheology, Biophys. J. 88, 623–638 (2005) | doi:10.1529/biophysj.104.042457 | abstract | Abstract: location error splits into a static part, measured on immobilised particles, and a dynamic part from motion during the exposure; both propagate into the mean-squared displacement, and the static part can be corrected using static measurements at a similar signal-to-noise ratio |
