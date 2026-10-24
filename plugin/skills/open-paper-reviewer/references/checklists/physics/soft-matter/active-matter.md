---
id: T-ACTIVE-MATTER
name: Active matter
type: technique
field: physics/soft-matter
applies_when: the paper studies self-propelled particles, swimming bacteria or cells, catalytic or light-driven active colloids, or motor-driven active gels and nematics, and bases a claim on propulsion speed or mechanism, wall accumulation, clustering, density or order parameters, or a collective phase
version: "0.1"
---

# Active matter

Experiments on active matter, such as self-propelled (active) colloids, swimming bacteria and other cells, and active gels of cytoskeletal filaments driven by motor proteins, are used to claim a propulsion speed and mechanism, interactions with walls, and collective states such as clusters, motility-induced phase separation (MIPS), flocks and active turbulence. These claims rest on separating motion driven by consumed fuel from Brownian motion, flows, gravity and ordinary attractive interactions.

## 1. Propulsion mechanism

**Question.** When the paper names a propulsion mechanism, such as self-diffusiophoresis, self-electrophoresis, self-thermophoresis or bubble release, which measurements test it against the alternatives: the dependence of speed on fuel concentration, added salt, ionic surfactants, coating thickness or illumination, and the direction of motion relative to the catalytic face?

**Why it matters.** For catalytic swimmers the strength and even the direction of propulsion can depend strongly on added salt and ionic surfactants, and a mechanism that is often assumed can fail quantitative tests against measured speeds and reaction rates. A mechanism stated without such tests is a hypothesis, and claims built on it, such as scaling with fuel or interactions between swimmers, inherit its uncertainty.

**Resolved by.** The mechanism presented as tested or as assumed; speed measured against fuel concentration and against the ionic composition of the solution, with conductivity or salt concentration reported; the direction of motion relative to the coated or active face determined; measured reaction or fuel consumption rates compared with what the proposed mechanism needs; untested alternatives named.

**Benchmark.** [1], [2]

## 2. Speed and persistence from trajectories

**Question.** How were propulsion speed and persistence obtained from the trajectories, at what frame rate compared with the rotational diffusion time, and does the paper show the mean-squared displacement over lag times from well below to well above that time, fitted with a model that includes translational diffusion?

**Why it matters.** For an active Brownian particle the mean-squared displacement is diffusive at the shortest times, grows faster than linearly near the rotational diffusion time and becomes diffusive again at long times with an enhanced coefficient. The rotational diffusion time scales as the cube of the particle radius, so for small particles the directed regime is short and is easily missed at low frame rates. An enhanced long-time diffusivity alone does not separate propulsion from other processes, and a speed taken from frame-to-frame displacements includes Brownian steps.

**Resolved by.** The frame rate and exposure stated and compared with the rotational diffusion time; mean-squared displacements shown on logarithmic axes over the full range of lag times, for active and fuel-free particles in the same cell; speed, rotational diffusion time and translational diffusivity fitted together, with the fitted rotational time compared with the value expected from particle size and viscosity; whether motion is tracked in two or three dimensions stated; the number of trajectories and their length given.

**Benchmark.** [1], [3]

## 3. Drift, flows, sedimentation and contamination

**Question.** How does the paper exclude apparent propulsion from drift, convection, sedimentation, bubbles, thermal gradients under illumination or contamination by bacteria, and are passive particles or fuel-free samples imaged under the same conditions as a reference?

**Why it matters.** Convection, sedimentation, Brownian motion and bacteria attached to particles can all make small particles appear self-propelled, and attached bacteria cannot be told apart by tracking alone. Loading a sample chamber creates transient flows that can take a long time to decay.

**Resolved by.** Drift subtracted using passive tracers or the mean motion of the ensemble, with the subtraction stated; fuel-free and passive-particle controls imaged in the same chamber, at the same height and time after loading; sealing, temperature control and illumination intensity reported; the time after loading at which measurements start stated and justified; checks for contamination, such as sterile handling or imaging at magnifications that would reveal attached cells.

**Benchmark.** [3], [5]

## 4. Walls, gravity and confinement

**Question.** Where were the particles relative to the walls of the sample cell during the measurement, how close to a wall were they, and does the paper show that a reported speed, accumulation, circular motion or collective state is a property of the bulk, or does it state that it is specific to motion along a surface?

**Why it matters.** Active particles accumulate at walls even when the walls are purely repulsive, and hydrodynamic interactions with a surface change their orientation and path; flagellated bacteria swim in circles near solid surfaces. Dense catalytic particles settle onto a surface within minutes and move along it, often oriented by gravity, so most experiments on synthetic swimmers are effectively two-dimensional. Results obtained at a wall may not carry over to the bulk.

**Resolved by.** Cell dimensions, imaging height and the time after loading stated; densities of particles and fluid, or the sedimentation length, reported; measurements repeated at more than one height, or in the bulk, where a bulk property is claimed; surface treatment of the walls described, with sticking excluded; the role of the wall, and of gravity, discussed when the claim concerns accumulation, rectification or collective behaviour.

**Benchmark.** [1], [2], [4], [5]

## 5. Activity level and its stability over time

**Question.** Does the paper show that the activity, such as swimming speed or motor-driven flow speed, stayed constant over the duration of each measurement, and how were the fuel, oxygen and nutrient supply controlled?

**Why it matters.** Activity is sustained only while fuel lasts: motor-driven gels keep flowing only while there is enough ATP (adenosine triphosphate), and bacteria in a sealed chamber slow steadily and then stop abruptly when oxygen runs out, sooner at higher cell density. A collective state compared across densities or times can then reflect falling activity instead of the variable that was intended. Growth stage, washing and handling also change bacterial speed and the fraction of cells that swim.

**Resolved by.** Speed or flow speed measured repeatedly over the duration of the experiment, with the window of acceptable activity stated; fuel, ATP or oxygen supply and any regeneration system or energy source described; for bacteria, the strain, growth medium and stage, washing method, buffer and sealing reported; measurements at different densities made at matched times after preparation, or with activity measured for each.

**Benchmark.** [5], [7]

## 6. Concentration and the motile fraction

**Question.** How was the concentration or area fraction of swimmers measured, and does the paper report the fraction that is non-motile and the distribution of speeds, not only a mean speed?

**Why it matters.** Cell concentrations from optical density depend on wavelength and on a calibration that changes with growth stage, and appendages such as flagella make the effective volume fraction much larger than the body volume fraction. Populations contain non-motile cells, which sediment and change the measured motile fraction with time and height. A mean speed over all particles mixes these populations and can hide a broad speed distribution.

**Resolved by.** The method for concentration stated, with the calibration and wavelength for optical density; the effective volume or area fraction defined; the non-motile fraction and speed distribution measured, for example by tracking or differential dynamic microscopy, at the time and height of the main measurement; collective results presented against a density measured in the field of view.

**Benchmark.** [5]

## 7. Clustering and phase separation

**Question.** When clusters or phase separation are attributed to motility alone, how does the paper exclude attraction from phoretic or chemical gradients, depletion, adhesion to the wall or between particles, or secreted polymers, and does it show whether the clusters coarsen or remain finite?

**Why it matters.** Motility-induced phase separation arises from self-trapping when speed falls steeply enough with density, but phoretic attraction from overlapping reagent and product gradients and polymer-induced attraction in bacteria can also produce clusters. Clusters alone therefore do not establish MIPS. Synthetic swimmers often form clusters that stop growing, and it is not settled whether these are motility-driven separation arrested by attraction or attraction-driven separation arrested by activity.

**Resolved by.** Pair interactions or approach velocities between particles measured directly, in particular for catalytic swimmers; the same system shown not to cluster without fuel at the same density; speed measured as a function of local density; cluster size distributions and their evolution in time shown, over times long compared with the time a particle takes to cross a cluster; the description stated as clustering where coarsening or a density-dependent speed is not shown.

**Benchmark.** [1], [4]

## 8. Order parameters, fluctuations, defects and system size

**Question.** How are the order parameter, number fluctuations or defect density defined and computed, over what range of length scales compared with the field of view and the system size, and how do the reported values depend on confinement, substrate friction and the surrounding fluid?

**Why it matters.** Giant number fluctuations are measured from the scaling of the variance of particle number with the mean number in subregions, and an exponent fitted over a narrow range of sizes is weakly constrained; the largest usable scale is set by the system size. Structures such as travelling bands appear only when the system is larger than their width, and whether momentum is damped by a substrate or carried by the fluid changes the expected behaviour. In active nematics the number of defects depends on the viscosity of the adjacent fluid, the friction with the substrate and the confinement, and the activity and elastic constants needed to compare with theory are hard to measure.

**Resolved by.** Definitions of every order parameter and fluctuation measure, with the box sizes and fitting range given and as wide as the field of view allows; the equilibrium scaling shown for comparison, for example with passive particles at the same density; field of view and system size compared with the correlation length, band width or active length; the boundary conditions, friction and surrounding fluid described; the parameters used in any comparison with theory measured independently, or the uncertainty in them stated.

**Benchmark.** [6], [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | C. Bechinger, R. Di Leonardo, H. Löwen, C. Reichhardt, G. Volpe and G. Volpe, Active particles in complex and crowded environments, Rev. Mod. Phys. 88, 045006 (2016); read as preprint arXiv:1602.00081 | doi:10.1103/RevModPhys.88.045006 | full text | Sec. II.3: mean-squared displacement of an active Brownian particle, diffusive at short times, superdiffusive near the rotational time, diffusive with an enhanced coefficient at long times. Sec. II.1: rotational diffusion coefficient scales as the inverse cube of the radius. Sec. II.5.1: propulsion strength and direction of catalytic swimmers depend strongly on added salt and ionic surfactants. Sec. III.3: hydrodynamic attraction and alignment of pushers at walls, bacteria swimming in circles above solid surfaces. Sec. V.1: large accumulation at a wall even when it is purely repulsive. Sec. IV.2.1: clusters and living crystals in experiments, with directly measured diffusiophoretic attraction in one system and self-trapping as the explanation in others |
| 2 | A. Brown and W. Poon, Ionic effects in self-propelled Pt-coated Janus swimmers, Soft Matter 10, 4016–4027 (2014); read as preprint arXiv:1312.4130 | doi:10.1039/C4SM00340C | full text | Abstract and Results: neutral salts slow the swimmers and an ionic surfactant reverses their direction. Secs. 4.1.4 to 4.2: neutral self-diffusiophoresis is inconsistent with the salt dependence and measured reaction rates, and ionic self-diffusiophoresis is argued against; Sec. 5: the favoured self-electrophoresis mechanism is stated as unproven by the data. Methods: particles reach the capillary surface within minutes and move parallel to it, the heavier coated side facing down; bulk observations confirm the behaviour away from the surface |
| 3 | G. Dunderdale, S. Ebbens, P. Fairclough and J. Howse, Importance of particle tracking and calculating the mean-squared displacement in distinguishing nanopropulsion from other processes, Langmuir 28, 10997–11006 (2012) | doi:10.1021/la301370y | abstract | Abstract: Brownian motion, convection, sedimentation and bacterial contamination can mimic propulsion of small particles; tracking with mean-squared displacement at short and long times is needed; bacteria attached to particles cannot be distinguished by tracking alone, so control experiments are essential; a test protocol is proposed |
| 4 | M. E. Cates and J. Tailleur, Motility-induced phase separation, Annu. Rev. Condens. Matter Phys. 6, 219–244 (2015); read as preprint arXiv:1406.3533 | doi:10.1146/annurev-conmatphys-031214-014710 | full text | Sec. 6.2: synthetic swimmer experiments are mostly quasi-two-dimensional because swimmers accumulate at walls; some evidence for MIPS in synthetic colloids, more needed; attractions from reagent and product gradients, and polymer-induced attractions in bacteria, can also cause clustering; widespread finite clusters are an unsolved puzzle. Sec. 8: unclear whether these are MIPS arrested by attraction or attraction-driven separation arrested by activity. Introduction (Eq. 3) and Sec. 4.1: speed falling steeply enough with density as the instability criterion |
| 5 | J. Schwarz-Linek, J. Arlt, A. Jepson, A. Dawson, T. Vissers, D. Miroli, T. Pilizota, V. A. Martinez and W. C. K. Poon, Escherichia coli as a model active colloid: a practical introduction, Colloids Surf. B 137, 2–16 (2016); read as preprint arXiv:1506.04562 | doi:10.1016/j.colsurfb.2015.07.048 | full text | Sec. 3.4: optical density calibration depends on wavelength and growth stage; flagella make the effective volume fraction far larger than the body fraction. Sec. 4 introduction: differential dynamic microscopy gives mean speed and non-motile fraction. Secs. 3.2 and 4.2: non-motile cells sediment, so the measured non-motile fraction changes with time; near walls swimming becomes two-dimensional with circling; loading causes drift that decays over time; measurements at three heights. Secs. 5.1 and 5.2: growth medium and washing change speed. Sec. 7.1: in sealed samples speed falls and then crashes when oxygen runs out, sooner at higher density. Sec. 8.1: with glucose, speed stays roughly constant |
| 6 | M. C. Marchetti, J. F. Joanny, S. Ramaswamy, T. B. Liverpool, J. Prost, M. Rao and R. A. Simha, Hydrodynamics of soft active matter, Rev. Mod. Phys. 85, 1143–1189 (2013); read as preprint arXiv:1207.2929, titled Soft active matter | doi:10.1103/RevModPhys.85.1143 | full text | Sec. I: dry systems, where substrate friction damps momentum, versus wet systems where it is conserved. Sec. II.1.3: giant number fluctuations defined from the variance of particle number against mean number in subregions, with the equilibrium square-root scaling for comparison and the smallest wavevector set by system size; experimental reports measured over a limited dynamical range. Fig. 10 caption: bands appear only when the system is larger than their width |
| 7 | A. Doostmohammadi, J. Ignés-Mullol, J. M. Yeomans and F. Sagués, Active nematics, Nat. Commun. 9, 3246 (2018) | doi:10.1038/s41467-018-05666-8 | full text | Box 2 and Active systems: in microtubule-kinesin mixtures ATP concentration is a main control of activity, and active turbulence persists only while there is enough ATP. Viscous control and Substrate friction: more defects with higher oil viscosity and, in simulations, with higher friction. Two- and three-dimensional confinement: confinement changes the flow states. Perspectives: how to measure activity and orientational elasticity in experiments is an open question |
