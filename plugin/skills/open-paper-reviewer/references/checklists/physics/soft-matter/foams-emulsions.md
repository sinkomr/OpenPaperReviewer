---
id: T-FOAMS-EMULSIONS
name: Foams and emulsions
type: technique
field: physics/soft-matter
applies_when: the paper reports experiments on liquid foams or emulsions and bases a claim on bubble or droplet sizes, coarsening, coalescence, drainage, liquid or dispersed-phase fraction, the role of a surfactant or stabiliser, rheology near jamming, or three-dimensional images of foam structure
version: "0.1"
---

# Foams and emulsions

## 1. Where and how sizes were measured

**Question.** How were bubble or droplet sizes obtained (images through a container wall, a dilute monolayer, tomography of the bulk, or a bulk optical signal), which average and which measure of polydispersity are reported, and does the paper show that the measured population represents the bulk?

**Why it matters.** Bubbles seen through a wall are only the first layer: small bubbles can collect there, the wall flattens them, coarsening near the wall can differ, and refraction hides the contacts between bubbles so that outlines look smaller than the bubbles are, so surface and bulk size distributions need not agree. Sizes from diffuse light transmission rest on a proportionality between the transport mean free path and a size moment whose prefactor changes with liquid fraction and cell geometry. For a polydisperse sample, the mean radius and the Sauter radius (third over second moment) differ, so a size means little unless the average is named.

**Resolved by.** The method named with its resolution limit; the average and the polydispersity defined; surface images checked against a bulk measurement, a dilute monolayer of the same sample or a second method; for optical methods, a calibration against images for the same cell and liquid fraction; a stated rule for bubbles that touch the walls or lie near the resolution limit.

**Benchmark.** [1], [2]

## 2. Liquid or dispersed-phase fraction

**Question.** How was the liquid fraction of the foam, or the dispersed-phase fraction of the emulsion, measured and calibrated, and does the paper show how it varied with height and time during each measurement?

**Why it matters.** Conductivity gives the liquid fraction only through an empirical relation between relative conductivity and liquid fraction, normalised by the conductivity of the foaming solution, and earlier relations underestimate the conductivity at intermediate liquid fractions. Under gravity liquid drains, so a foam column carries a vertical gradient in liquid fraction, and the value set at preparation can differ from the value in the measured region. Fractions from images depend on the grey-level threshold used to separate liquid from gas.

**Resolved by.** The method and relation used, with its range of validity and the normalisation stated; the fraction measured where and when each data set was taken, with a profile in height, several electrode pairs or a fluorescence or image map showing uniformity or the gradient; for tomography, the threshold and its effect on the fraction stated.

**Benchmark.** [2], [3], [4], [5]

## 3. Coarsening rate and growth law

**Question.** When a coarsening rate or growth exponent is reported, does the paper show that the sample had reached a self-similar state, that drainage and coalescence were suppressed or accounted for, and that the exponent is interpreted in the light of the liquid fraction?

**Why it matters.** Gas transfer through thin films in dry foams makes the mean radius grow as the square root of time, whereas diffusion through the liquid in very wet foams and bubbly liquids makes it grow as the cube root, with a transition at a liquid fraction of roughly 25 to 30 per cent, so an exponent reflects the liquid fraction as well as the mechanism. Early size distributions have not yet reached the scaling state. On the ground, wet foams drain within minutes, and the coarsening rate itself depends on the stabiliser through surface tension, film permeability and gas loss outside the films, varying nearly tenfold between stabilisers.

**Resolved by.** Size distributions at several ages, rescaled by the mean to show that their shape no longer changes before a growth law is fitted; the fitted time range stated; the liquid fraction followed during coarsening, or drainage suppressed; a check that bubbles are not lost by coalescence; the measured rate compared with one estimated from the separately measured surface tension and film permeability.

**Benchmark.** [1], [4], [6]

## 4. Drainage and the mobility of interfaces

**Question.** For a drainage claim, which experiment was done (free, forced or pulsed drainage), how was the liquid fraction followed in space and time, and does the interpretation state whether the interfaces are taken as mobile or rigid and how bubble size enters?

**Why it matters.** Measured drainage velocities follow power laws that models with Poiseuille flow in the liquid channels (Plateau borders) cannot explain, and whether dissipation is dominated by the channels or by the junctions where they meet depends on how mobile the interfaces are. Interface mobility depends on the surfactant or protein used, while bubble size and liquid fraction set how much it matters; surface properties and bubble size combine into a single mobility parameter, so changing bubble size alone can move a foam from one drainage regime to the other.

**Resolved by.** The type of experiment and its boundary conditions stated; liquid-fraction profiles shown against height and time; the drainage law tested over a range of flow rates and bubble sizes; the regime identified from measured interfacial properties and bubble size, not inferred from an exponent alone.

**Benchmark.** [5], [7], [8]

## 5. Stabiliser and interfacial properties

**Question.** Does the paper characterise the surfactant, protein or other stabiliser under the conditions used (concentration relative to the critical micelle concentration, surface tension, interfacial viscoelasticity), and are claims about its role supported by those measurements and not only by the behaviour of the foam or emulsion?

**Why it matters.** Foaming, emulsification and the stability of foams and emulsions depend strongly on the compression elasticity and viscosity of the adsorbed layer, which an equilibrium surface tension does not capture. Micelles in the continuous phase can speed up Ostwald ripening by factors of 2 to 50 in a way that equilibrium solubilisation does not explain. Stabiliser chemistry also shifts drainage regimes and changes coarsening rates nearly tenfold, so a difference between formulations can come from any of these routes.

**Resolved by.** Stabiliser identity, concentration and critical micelle concentration stated; surface tension and interfacial rheology measured on the same solutions; thin-film observations where film stability is claimed; comparisons between stabilisers made at the same bubble or droplet size and liquid fraction.

**Benchmark.** [6], [8], [9], [10]

## 6. Separating ripening from coalescence and flocculation in emulsions

**Question.** When droplet growth in an emulsion is attributed to Ostwald ripening or to coalescence, what evidence separates the two from each other and from flocculation?

**Why it matters.** The Lifshitz-Slyozov-Wagner (LSW) theory of ripening predicts that the cube of the mean radius grows linearly in time and that the size distribution takes a particular skewed shape. Flocculation and coalescence can also give a linear growth of the cubed radius over a transient period, so a straight line on that plot does not identify ripening by itself. Micelles of excess surfactant change the ripening rate, which makes a measured rate hard to interpret without the composition of the continuous phase.

**Resolved by.** Full size distributions at several times compared with the predicted shape, not only a mean radius; the ripening rate compared with a value estimated from the solubility and diffusivity of the dispersed phase; surfactant concentration relative to the critical micelle concentration and ionic strength stated and varied; the early transient separated from the later regime.

**Benchmark.** [10], [11]

## 7. Volume fraction and ageing in rheology near jamming

**Question.** How was the gas or dispersed-phase volume fraction of each rheological sample determined and corrected, how close is it to the jamming fraction, and did the sample change by drainage or coarsening during the measurement?

**Why it matters.** The shear modulus of foams and emulsions vanishes and the yield stress falls by many orders of magnitude as the volume fraction approaches about 0.635, close to random close packing, so a small error in volume fraction near jamming produces a large change in the quantities measured. For small droplets, the effective volume fraction includes the thickness of a repulsive interfacial layer, and the jamming fraction adopted in analyses varies between about 0.62 and 0.64, so where data sit relative to jamming depends on these choices. In a coarsening foam the slow relaxation times lengthen as the foam ages, so the low-frequency response depends on sample age.

**Resolved by.** The volume fraction measured on the loaded sample, with any correction for interfacial layers stated; data plotted against the distance from the jamming fraction with its uncertainty; bubble or droplet size and liquid fraction checked before and after each test; the age of the sample stated and the time scale of the test compared with the coarsening time.

**Benchmark.** [12], [13], [14]

## 8. Three-dimensional imaging and segmentation

**Question.** For claims based on X-ray tomography or other three-dimensional imaging, does the paper state the voxel size and the scan time relative to film thickness and to the rate at which bubbles move or coarsen, and does it describe and check how bubbles were segmented?

**Why it matters.** Films between bubbles are too thin to appear in the images, so individual bubbles exist only after a segmentation step that reconstructs the films; its errors create spurious bubbles or merge real ones and change counts of neighbours and faces, which are also ambiguous in wet foams. Bubbles must not move much during a scan, bubbles near the resolution limit vanish from one image to the next, and bubbles cut by the walls or the field of view bias size and topology statistics.

**Resolved by.** Voxel size, scan time and the rate of change of the sample stated; the segmentation method and parameters given, with a check such as filtering of spurious bubbles or agreement with an independent measurement; bubbles at walls or field-of-view edges excluded by a stated rule; volume uncertainty from the voxel size propagated; the neighbour criterion defined.

**Benchmark.** [2], [15]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Pasquet et al., Aqueous foams in microgravity, measuring bubble sizes, C. R. Mécanique 351 (S2), 139 (2023); read as preprint arXiv:2209.03464 | doi:10.5802/crmeca.153 |
| 2 | J. Lambert et al., Experimental growth law for bubbles in a moderately "wet" 3D liquid foam, Phys. Rev. Lett. 99, 058304 (2007); read as preprint arXiv:cond-mat/0702685, which carries a slightly shorter title | doi:10.1103/PhysRevLett.99.058304 |
| 3 | K. Feitosa et al., Electrical conductivity of dispersions: from dry foams to dilute suspensions, J. Phys.: Condens. Matter 17, 6301 (2005); read as preprint arXiv:cond-mat/0507381 | doi:10.1088/0953-8984/17/41/001 |
| 4 | N. Isert et al., Coarsening dynamics of three-dimensional levitated foams: from wet to dry, Eur. Phys. J. E 36, 116 (2013); read as preprint arXiv:1211.0473 | doi:10.1140/epje/i2013-13116-x |
| 5 | S. A. Koehler et al., A generalized view of foam drainage: experiment and theory, Langmuir 16, 6327 (2000) | doi:10.1021/la9913147 |
| 6 | A. Requier et al., Wet foam coarsening: More than film permeability, J. Colloid Interface Sci. 696, 137825 (2025) | doi:10.1016/j.jcis.2025.137825 |
| 7 | S. A. Koehler et al., Drainage of single Plateau borders: direct observation of rigid and mobile interfaces, Phys. Rev. E 66, 040601 (2002) | doi:10.1103/PhysRevE.66.040601 |
| 8 | A. Saint-Jalmes et al., Quantitative description of foam drainage: transitions with surface mobility, Eur. Phys. J. E 15, 53 (2004) | doi:10.1140/epje/i2004-10036-x |
| 9 | D. Langevin, Influence of interfacial rheology on foam and emulsion properties, Adv. Colloid Interface Sci. 88, 209 (2000) | doi:10.1016/S0001-8686(00)00045-2 |
| 10 | S. Ariyaprakai and S. R. Dungan, Influence of surfactant structure on the contribution of micelles to Ostwald ripening in oil-in-water emulsions, J. Colloid Interface Sci. 343, 102 (2010) | doi:10.1016/j.jcis.2009.11.034 |
| 11 | G. Urbina-Villalba et al., Influence of flocculation and coalescence on the evolution of the average radius of an O/W emulsion. Is a linear slope of R3 vs. t an unmistakable signature of Ostwald ripening?, Phys. Chem. Chem. Phys. 11, 11184 (2009) | doi:10.1039/b915470a |
| 12 | A. Saint-Jalmes and D. J. Durian, Vanishing elasticity for wet foams: equivalence with emulsions and role of polydispersity, J. Rheol. 43, 1411 (1999) | doi:10.1122/1.551052 |
| 13 | F. Scheffold et al., Linear and nonlinear rheology of dense emulsions across the glass and the jamming regimes, J. Phys.: Condens. Matter 25, 502101 (2013); read as preprint arXiv:1305.5182, which carries a slightly different title | doi:10.1088/0953-8984/25/50/502101 |
| 14 | S. Cohen-Addad et al., Viscoelastic response of a coarsening foam, Phys. Rev. E 57, 6897 (1998) | doi:10.1103/PhysRevE.57.6897 |
| 15 | F. Schott et al., Multiscale stress dynamics in sheared liquid foams revealed by tomo-rheoscopy, Nat. Commun. 16, 9210 (2025); read as preprint arXiv:2411.10338 | doi:10.1038/s41467-025-64412-z |
