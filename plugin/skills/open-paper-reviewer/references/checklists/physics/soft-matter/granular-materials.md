---
id: T-GRANULAR-MATERIALS
name: Granular materials
type: technique
field: physics/soft-matter
applies_when: the paper reports experiments on packings or flows of macroscopic grains, such as beads, disks or sand, that are tapped, vibrated, sheared or compressed, or bases a claim on packing fraction, photoelastic forces, a granular or effective temperature, or discrete-element simulations
version: "0.1"
---

# Granular materials

## 1. Preparation protocol and packing fraction

**Question.** How was each packing prepared (pouring, tapping, vibration, fluidisation, compression, and with what amplitude, number of cycles and history), how was the packing fraction measured, and is it stated with its uncertainty and with the region over which it was averaged?

**Why it matters.** The packing fraction of nominally identical grains depends on the preparation protocol, on interparticle friction and on polydispersity, and a tapped packing first follows an irreversible branch that keeps a memory of its history before reaching a reproducible state. Labels such as random close packing do not name a unique density, so a value quoted only by name, or a packing compared with another prepared differently, may not describe the same state.

**Resolved by.** The full preparation sequence stated, including how long the system was driven before data were taken; evidence that the state was reproducible or had reached a steady branch, for example repeated runs from a fresh start giving the same packing fraction; the measurement method (total volume, tomography, imaging, or local cell volumes) and averaging region stated, with wall regions identified; grain friction and size distribution reported, since they shift the accessible range of packing fractions.

**Benchmark.** [1], [2]

## 2. Walls, container size and boundary conditions

**Question.** What are the container dimensions compared with the grain size, what are the walls made of and how rough are they, and does the paper show that the reported stress, velocity profile or packing fraction is not set by the walls?

**Why it matters.** Friction at side walls carries part of the weight of a granular column, so the pressure at the base stops growing with filling height in a way that depends on the container width and the wall friction. In flows, side-wall friction changes velocity profiles and pile angles in narrow channels, wall roughness changes the thickness of boundary layers and the width of shear zones, a slip velocity can appear at the boundaries even when the walls are rough, and grains form ordered layers next to walls, which alters the local packing fraction and the shear over the first few grain diameters.

**Resolved by.** Container size, wall material and roughness stated relative to the grain diameter; results shown for more than one container width or gap, or an estimate of the wall contribution, such as a ratio of layer height to channel width; the wall roughness stated, for example glued grains, and any slip velocity at the walls measured and reported; averages taken away from the first few layers next to a wall, or the wall region reported separately.

**Benchmark.** [3], [4], [5]

## 3. Humidity, cohesion and interstitial gas

**Question.** Were the relative humidity and temperature controlled or at least recorded, how long did the sample rest before each measurement, and does the paper show that cohesion from liquid bridges or other surface forces, and drag from the interstitial gas, do not affect the result?

**Why it matters.** Even humid air condenses into liquid bridges at grain contacts, and the cohesion they create raises the angle of repose and the maximum stability angle, which can grow with resting time at intermediate humidity; small grains are the most affected, and cohesion stabilises looser packings than dry grains can hold. In vibrated beds the interstitial air can drive effects such as heaping that disappear in vacuum or for larger grains, so a result attributed to grain collisions may depend on the surrounding gas.

**Resolved by.** Humidity and temperature reported for each data set, with humidity controlled where cohesion could matter; waiting times stated and a check that results do not drift with resting time; grain size and surface condition reported, with an estimate of cohesive forces compared with grain weight; for vibrated or rapidly flowing beds, a comparison at reduced gas pressure, or an argument comparing the grain settling velocity with the drive velocity.

**Benchmark.** [6], [7], [8]

## 4. Photoelastic calibration and the stress proxy

**Question.** For photoelastic particles, how was the material calibrated (fringe or stress-optic constant from a known diametric load), what optical arrangement and light source were used, and over what range of forces, particle sizes and image resolutions is any image-based stress proxy, such as the squared intensity gradient, shown to be proportional to force?

**Why it matters.** Converting fringe patterns into forces needs a calibration made with the same material, thickness, wavelength and lighting as the experiment, a circular polariscope and close to monochromatic light. The squared intensity gradient tracks the summed contact force only while fringes are resolved; it saturates at higher forces, and its constant depends on particle radius, thickness, lighting, camera resolution and material, so comparisons across these require separate calibration. Residual stress left in particles by cutting or printing adds a signal that is not caused by contact forces.

**Resolved by.** A calibration of each particle material and size in the same optical set-up, with the force range covered; uniform, monochromatic illumination and a circular polariscope described; the proxy shown to be linear over the forces in the experiment, or a nonlinear calibration applied; particles checked for residual stress under no load, and annealed or selected if needed.

**Benchmark.** [9], [10]

## 5. Vector contact forces from photoelastic images

**Question.** When individual contact forces are obtained by fitting photoelastic images, how were particle centres and contacts identified, what image resolution per particle was used, how were starting guesses chosen, and what check on the fitted forces is reported?

**Why it matters.** The fit inverts a nonlinear relation that has no unique inverse, so the optimiser can settle on a wrong local solution, especially at large forces or many contacts per particle. A contact list based only on distance includes false contacts and misses real ones, weak contacts give dim signals near the particle edge, and fringes become unresolved at large forces. The method is well specified for circular disks confined to a plane, and force balance cannot be used as a constraint when particles accelerate.

**Resolved by.** Centre location accuracy and the contact detection rule stated, with contacts confirmed by the local photoelastic signal; the resolution and number of fringes per particle given; an error estimate from calibration loads with known forces; the agreement of the two estimates of each contact force from the neighbouring particles reported as a consistency check; the force range below which forces are not resolved stated; particles kept in one plane and the method used only for shapes it covers.

**Benchmark.** [9], [10]

## 6. How the system is driven

**Question.** Is the driving fully specified and measured where it acts on the grains: for vibration both the frequency and the amplitude (and hence the peak acceleration relative to gravity), for shear the rate or stress and the geometry, for fluidisation the flow rate, and is the energy input uniform across the sample?

**Why it matters.** Granular states depend on more than one drive parameter: in vibrated layers the pattern formed depends on both the dimensionless acceleration and the frequency, as well as on layer depth and grain size, so quoting the acceleration alone does not fix the state. Energy enters through boundaries and is dissipated in collisions, so the agitation is strongest near the driving surface and a colder, denser region can form away from it; a measurement in one region need not represent another.

**Resolved by.** All drive parameters stated, with the motion of the container or driving surface measured rather than taken from the controller setting; layer depth in grain diameters and grain size given; results shown against the drive parameters that matter, not one combination only; profiles of density or agitation with distance from the driving boundary, or the measurement location stated.

**Benchmark.** [8]

## 7. Definition of an effective temperature

**Question.** When the paper uses a granular temperature, a compactivity, an angoricity or a temperature from a fluctuation-dissipation relation, which definition is used, how was it measured, and is it shown to be the same in different regions, directions, grain species or by different measurement routes?

**Why it matters.** A driven granular system is not in thermal equilibrium, so a temperature-like quantity is useful only if it behaves like one. Different grain species in one vibrated mixture can reach different kinetic temperatures, effective temperatures from probe fluctuations and response have been found to depend on direction and position, and different methods of measuring compactivity do not always agree. Edwards-type descriptions also assume that the system explores its states ergodically, which can fail under weak driving.

**Resolved by.** The definition and measurement route stated; the temperature compared between subregions, directions or species, and between at least two independent routes where it is used as a thermodynamic variable; tests that different runs of the same protocol reach the same stationary distribution; claims of equilibrium-like behaviour limited to the conditions in which these checks were made.

**Benchmark.** [1], [11], [12]

## 8. Comparison with discrete-element simulations

**Question.** When experiments are compared with DEM simulations, does the paper state the contact model and its parameters (friction coefficient, restitution, stiffness, rolling resistance), grain shape and size distribution, dimensionality, boundaries and system size, and say which parameters were measured, which were calibrated against which bulk test, and whether the agreement was checked on a different test?

**Why it matters.** DEM results depend on input parameters that are often not measured directly. Interparticle friction strongly changes packing fraction and, especially between frictionless and frictional grains, the effective friction; contact stiffness must be high enough to reach the rigid-grain limit or it alters coordination and shear localisation; and polydispersity and wall construction change the structure. Without calibration and validation, simulated results can be imprecise or unphysical; calibration to a single test can be satisfied by several parameter sets, for example trading sliding against rolling friction, so agreement on the quantity used for calibration does not test the model; two-dimensional simulations and experiments can also differ in quantities such as flowing-layer depth.

**Resolved by.** All contact parameters and the time step listed, with measured values used where possible; calibration against one set of bulk measurements and validation against another; the sensitivity of the compared quantity to friction, stiffness and restitution shown; matching dimensionality, size distribution, boundaries and drive between simulation and experiment, or the differences stated and their effect estimated.

**Benchmark.** [4], [5], [13], [14]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | A. Baule et al., Edwards statistical mechanics for jammed granular matter, Rev. Mod. Phys. 90, 015006 (2018); read as preprint arXiv:1602.04369 | doi:10.1103/RevModPhys.90.015006 |
| 2 | S. Torquato et al., Is random close packing of spheres well defined?, Phys. Rev. Lett. 84, 2064 (2000); read as preprint arXiv:cond-mat/0003416 | doi:10.1103/PhysRevLett.84.2064 |
| 3 | M. Sperl, Experiments on corn pressure in silo cells: translation and comment of Janssen's paper from 1895, Granular Matter 8, 59 (2006); read as preprint arXiv:cond-mat/0511618 | doi:10.1007/s10035-005-0224-z |
| 4 | GDR MiDi, On dense granular flows, Eur. Phys. J. E 14, 341 (2004); read as preprint arXiv:cond-mat/0312502 | doi:10.1140/epje/i2003-10153-0 |
| 5 | F. da Cruz et al., Rheophysics of dense granular materials: discrete simulation of plane shear flows, Phys. Rev. E 72, 021309 (2005); read as preprint arXiv:cond-mat/0503682 | doi:10.1103/PhysRevE.72.021309 |
| 6 | L. Bocquet et al., Moisture-induced ageing in granular media and the kinetics of capillary condensation, Nature 396, 735 (1998); read as preprint arXiv:cond-mat/9801218 | doi:10.1038/25492 |
| 7 | N. Mitarai and F. Nori, Wet granular materials, Adv. Phys. 55, 1 (2006); read as preprint arXiv:cond-mat/0601660 | doi:10.1080/00018730600626065 |
| 8 | I. S. Aranson and L. S. Tsimring, Patterns and collective behavior in granular media: theoretical concepts, Rev. Mod. Phys. 78, 641 (2006); read as preprint arXiv:cond-mat/0507419 | doi:10.1103/RevModPhys.78.641 |
| 9 | K. E. Daniels et al., Photoelastic force measurements in granular materials, Rev. Sci. Instrum. 88, 051808 (2017); read as preprint arXiv:1612.03525 | doi:10.1063/1.4983049 |
| 10 | A. Abed Zadeh et al., Enlightening force chains: a review of photoelasticimetry in granular matter, Granular Matter 21, 83 (2019); read as preprint arXiv:1902.11213 | doi:10.1007/s10035-019-0942-2 |
| 11 | K. Feitosa and N. Menon, Breakdown of energy equipartition in a 2D binary vibrated granular gas, Phys. Rev. Lett. 88, 198301 (2002); read as preprint arXiv:cond-mat/0111391 | doi:10.1103/PhysRevLett.88.198301 |
| 12 | G. D'Anna et al., Observing Brownian motion in vibration-fluidized granular matter, Nature 424, 909 (2003); read as preprint arXiv:cond-mat/0310040 | doi:10.1038/nature01867 |
| 13 | C. Windows-Yule and A. Neveu, Calibration of DEM simulations for dynamic particulate systems, Pap. Phys. 14, 140010 (2022) | doi:10.4279/pip.140010 |
| 14 | A.-L. Nicusan et al., ACCES: Non-Invasive Simulation Calibration via Optimisation using Evolutionary Algorithms and Metaprogramming, preprint (2025) | https://arxiv.org/abs/2505.02967 |
