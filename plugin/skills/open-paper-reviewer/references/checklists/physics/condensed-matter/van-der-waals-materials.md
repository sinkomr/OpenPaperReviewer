---
id: T-VAN-DER-WAALS
name: Two-dimensional materials and van der Waals heterostructures
type: technique
field: physics/condensed-matter
applies_when: the paper studies exfoliated or grown atomically thin layers or stacks of them, such as graphene, hBN, transition metal dichalcogenides or twisted moiré bilayers, and bases a claim on layer number, twist angle, stacking, strain, encapsulation or devices made from them
version: "0.1"
---

# Two-dimensional materials and van der Waals heterostructures

Two-dimensional (2D) materials are crystals one or a few atomic layers thick, such as graphene, hexagonal boron nitride (hBN) and the transition metal dichalcogenides (TMDs), used alone or stacked into van der Waals heterostructures, including twisted (moiré) bilayers. Papers use them to claim properties of a given layer number, stacking or twist angle, and to attribute what they measure to the material itself and not to the sample, its surroundings or its fabrication.

## 1. Layer number and coverage

**Question.** How was the number of layers in each measured flake or film determined, with which method and calibration, and where the claim depends on it, is the assignment confirmed by a second, independent method?

**Why it matters.** Optical contrast depends on the oxide thickness of the substrate, the wavelength and the refractive index of the layer, which is unknown for many newer materials. Atomic force microscope (AFM) step heights are changed by the tip interacting differently with flake and substrate, by the imaging set-point and by residue under the flake. Raman and photoluminescence indicators also respond to strain, doping, defects and stacking, and some are calibrated only for the first few layers.

**Resolved by.** The method and its calibration stated for the material and the range of layer numbers in question, for example low-frequency interlayer Raman modes or optical contrast with the substrate specified; AFM heights interpreted with residue and set-point in mind; an independent cross-check, such as Raman with AFM or electron microscopy, for the samples on which claims rest; for grown films, maps showing the fraction of monolayer, multilayer and uncovered area, and the location of the measured region within them.

**Benchmark.** [1], [2]

## 2. Twist angle, stacking order and alignment in the finished device

**Question.** How were the twist angle between layers, the stacking order, and the alignment of each layer with neighbouring crystals, including the encapsulating hBN, determined in the finished device, and does the paper distinguish what was set during stacking from what was measured afterwards?

**Why it matters.** The angle reached during stacking often differs from the one set on the rotation stage, because of strain in the polymer and the flake, stage precision and backlash, and relaxation or snap-in on assembly. Later heating, as in resist baking or annealing, can rotate layers towards alignment, so the final angle tends to be smaller than the target, and metastable stackings, such as rhombohedral graphene multilayers, can convert to the lower-energy stacking. In transition metal dichalcogenide bilayers, stacks near 0° and near 60° form different superlattices, and a layer close to alignment with hBN forms its own moiré superlattice, which changes the electronic structure.

**Resolved by.** The twist angle inferred from a quantity measured on the device itself, such as the carrier density at full filling of the moiré band from transport, or local imaging, with its uncertainty; the stacking order, and for dichalcogenides the distinction between near-0° and near-60° stacking, checked on the completed stack, for example by Raman, near-field infrared or second-harmonic imaging; the fabrication steps after stacking listed with their temperatures; the alignment of hBN and other neighbouring layers measured or stated, with its possible effect on the claim considered.

**Benchmark.** [3]

## 3. Homogeneity of twist angle and strain

**Question.** Does the paper show how the twist angle and the strain vary across the region that produced the data, for example by comparing several contact pairs or by local imaging, and is each claimed feature tied to a region of known angle?

**Why it matters.** Angle variations of about 0.1° and differential strain between the layers of a few tenths of a per cent are typical across micrometre-sized samples, and strain in the moiré pattern is much larger than the strain between the layers that causes it. At a fixed carrier density the moiré filling changes with the square of the angle, so a spread of angles mixes phases. A device can show a global transport signature while parts of it behave differently, and percolating patches can mimic effects attributed to the whole sample.

**Resolved by.** The full-filling density, or another angle-sensitive quantity, compared between several contact pairs or regions; local maps of angle or strain where available; claimed features tied to a stated region and angle; results reproduced in more than one device or region with the spread reported.

**Benchmark.** [3], [4]

## 4. Interfaces, bubbles and wrinkles

**Question.** Does the paper show images of the finished stack, such as optical, dark-field or AFM images, that locate bubbles, wrinkles and folds, and does it show that the device channel or the probed spot lies in a clean region?

**Why it matters.** Hydrocarbons, water and air trapped during stacking gather into bubbles from nanometres to micrometres across, often spaced 1 to 10 µm apart. The interface between bubbles is clean, but a channel or a laser spot that overlaps bubbles or folds samples local strain, doping and disorder that are not properties of the material.

**Resolved by.** Images of the stack with the device outline or measurement spots marked; the stacking method and its temperature stated; spatial maps, for example Raman maps, showing that the measured region is uniform; data from regions with bubbles or folds identified and treated separately.

**Benchmark.** [5], [6]

## 5. Separating strain from doping

**Question.** When a spectral shift, a change of band gap or a change of electronic properties is attributed to strain or to doping, how does the paper separate the two, and does it consider strain varying on scales smaller than the probe?

**Why it matters.** In graphene the Raman G and 2D peak positions both respond to strain and to charge, so a shift of one peak cannot be assigned without knowing the other. Correlation analysis of the two peaks separates them only under stated assumptions and for the excitation wavelength its reference values were taken at, and strain, hole doping and electron doping cannot all be separated unless one of them is known or assumed. A Raman map averages over a spot of about half a micrometre and misses strain variations on the nanometre scale, which limit carrier mobility.

**Resolved by.** A correlation analysis of two or more spectral features with its assumptions and reference values stated, or doping measured independently, for example with a gate; strain given with its uncertainty and its spatial variation; peak widths used as an indicator of strain variation below the spot size; the effect of thermal treatments on strain and doping recorded.

**Benchmark.** [5], [6], [7]

## 6. Contacts to atomically thin layers

**Question.** What contact metal and geometry (top or edge contact) were used, and when a Schottky barrier height or a property of the channel is quoted, does the analysis separate the contact from the channel?

**Why it matters.** Metal contacts to 2D semiconductors usually form Schottky barriers, often with the Fermi level pinned by reactions at the interface, so device characteristics can reflect the contacts more than the layer. The activation energy from temperature-dependent data equals the barrier height only at the flat-band condition, the channel resistance contributes to the temperature dependence, and barrier lowering at finite bias makes the extracted height too small.

**Resolved by.** Contact metal, deposition conditions and geometry stated; the barrier height extracted where the activation energy stops depending linearly on gate voltage, with the gate dependence shown and the result extrapolated to zero bias; contact resistance measured separately from the channel; conclusions about the layer drawn from data where the contacts do not dominate.

**Benchmark.** [8]

## 7. Processing history and exposure to air

**Question.** Does the paper state the processing history of the measured sample (polymers and solvents in contact with the layers, annealing temperatures and times, lithography and metal deposition, and the time and atmosphere of exposure before and during measurement), and does it show that the property claimed is stable over the measurement period?

**Why it matters.** Polymer residues and adsorbates from air dope the layers and lower mobility, and annealing changes strain and doping and can rotate layers. Air-sensitive materials change within minutes to hours and can degrade within days, shifting threshold voltages and thinning or destroying the layer. Small, unreported differences in such steps change outcomes between laboratories.

**Resolved by.** Process steps listed with their parameters, including polymer type, temperatures and times; the atmosphere and the time spent in air recorded, with inert handling or full encapsulation for air-sensitive materials; characterisation, such as Raman or AFM, repeated after device fabrication and not only before; key measurements repeated over time or after thermal cycling to show stability.

**Benchmark.** [3], [5], [7], [9], [10]

## 8. Encapsulation and dielectric environment

**Question.** Is the dielectric environment of the layer stated for each data set (substrate, encapsulating layers and their thickness, gate electrodes), and when properties are compared with other work or with theory, is the comparison made for the same environment?

**Why it matters.** Screening in a 2D layer is weak, so the surrounding materials change the band gap and the exciton binding energy, by hundreds of milli-electronvolts in some cases. The band gap and the exciton binding energy can shift by similar amounts in the same direction, so an almost unchanged optical transition energy does not show that the environment has no effect. Rough or charged substrates broaden optical lines to tens of milli-electronvolts, while encapsulation in hBN can narrow them to a few. A value measured in one environment is not an intrinsic property of the layer.

**Resolved by.** The environment specified for every data set; comparisons with other samples, literature values or calculations made for matching environments or corrected for the difference; spatial changes in the environment, such as partial encapsulation or a nearby gate, considered where they could produce the claimed effect; linewidths reported alongside energies.

**Benchmark.** [11], [12]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | A. J. Pollard, K. R. Paton, C. A. Clifford, E. Legge, A. Oikonomou, S. Haigh, C. Casiraghi, L. Nguyen and D. Kelly, Characterisation of the structure of graphene, National Physical Laboratory Measurement Good Practice Guide No. 145 (2017) | https://eprintspublications.npl.co.uk/8654/1/mgpg145.pdf | full text | Sec. 2.2: single-layer contrast is sufficient for identification only for certain oxide thicknesses, and turbostratic multilayers give varying contrast. Sec. 2.2.2: coverage reported as uncovered, monolayer and multilayer fractions. Sec. 2.3.2: monolayer criteria from the 2D peak shape and width; turbostratic few-layer graphene can also show a single narrow 2D peak, and the 2D to G ratio is lowered by disorder and doping, so electron microscopy is needed to confirm layer number. Sec. 3.3.3: lowering the AFM set-point changes the measured step height, and residue between flake and substrate must be allowed for in flakes of about 3 nm or less |
| 2 | X. Zhang, X.-F. Qiao, W. Shi, J.-B. Wu, D.-S. Jiang and P.-H. Tan, Phonon and Raman scattering of two-dimensional transition metal dichalcogenides from monolayer, multilayer to bulk material, Chem. Soc. Rev. 44, 2757–2785 (2015); read as arXiv:1502.00701 | doi:10.1039/c4cs00282b | full text | Sec. IV.A: the separation of the two main Raman peaks of MoS2 identifies layer number only up to about five layers. Sec. VII.A: optical contrast needs the refractive index, monolayer thickness and oxide thickness (often uncertain by 5%), unknown for many new materials; AFM heights suffer from different tip interactions with flake and substrate and from roughness and surface cleanliness; photoluminescence depends on temperature, defects and doping; interlayer shear and breathing modes give a substrate-free identification |
| 3 | C. N. Lau, M. W. Bockrath, K. F. Mak and F. Zhang, Reproducibility in the fabrication and physics of moiré materials, Nature 602, 41–50 (2022); read as the accepted manuscript in the NSF Public Access Repository (record 10326322) | doi:10.1038/s41586-021-04173-z | full text | Section on fabrication: the achieved twist angle often differs from the target because of polymer and flake strain, stage precision and relaxation or snap-in; annealing at 200–400 °C rotates graphene towards alignment with hBN below 12°, and resist baking at 180 °C suggests final angles below target; graphene aligned with hBN forms its own superlattice; rhombohedral trilayer domains not isolated from Bernal domains tend to convert to the lower-energy stacking, identified by near-field infrared or Raman imaging; TMD bilayers near 0° and 60° form distinct superlattices, distinguished by second-harmonic generation, which is repeated on the completed stack. "Angular and strain disorders": angle disorder appears as different full-filling densities across a device; local probes show about ±0.1° and heterostrain of 0.1–0.7%; moiré strain amplified by about 1/θ; filling scales with θ² at fixed density; heterostrain introduced by tearing, pick-up and metal deposition. Fig. 1 and Outlook: single-device studies; percolating patches in inhomogeneous devices; polymer residue and bubbles |
| 4 | A. Uri, S. Grover, Y. Cao, J. A. Crosse, K. Bagani, D. Rodan-Legrain, Y. Myasoedov, K. Watanabe, T. Taniguchi, P. Moon, M. Koshino, P. Jarillo-Herrero and E. Zeldov, Mapping the twist-angle disorder and Landau levels in magic-angle graphene, Nature 581, 47–52 (2020); abstract read on arXiv:1908.04595, which carries a different title | doi:10.1038/s41586-020-2255-3 | abstract | Abstract: local imaging of encapsulated twisted bilayer devices shows twist-angle variations spanning close to 0.1° even in high-quality devices, and regions without local magic-angle behaviour in devices whose global transport shows magic-angle features |
| 5 | D. G. Purdie, N. M. Pugno, T. Taniguchi, K. Watanabe, A. C. Ferrari and A. Lombardo, Cleaning interfaces in layered materials heterostructures, Nat. Commun. 9, 5387 (2018) | doi:10.1038/s41467-018-07558-3 | full text | Introduction: encapsulation isolates graphene from lithographic polymers, solvents and air, which lower mobility and increase doping; hydrocarbons, air and water trapped during stacking gather into blisters from nanometres to micrometres across; the interface between blisters is clean, and device size is limited by blister spacing of 1–10 µm. Results, Raman spectroscopy: the G peak position responds to both doping and strain, separated by correlating peak parameters; a narrower 2D peak after encapsulation indicates smaller nanometre-scale strain variation |
| 6 | C. Neumann, S. Reichardt, P. Venezuela, M. Drögeler, L. Banszerus, M. Schmitz, K. Watanabe, T. Taniguchi, F. Mauri, B. Beschoten, S. V. Rotkin and C. Stampfer, Raman spectroscopy as probe of nanometre-scale strain variations in graphene, Nat. Commun. 6, 8429 (2015) | doi:10.1038/ncomms9429 | full text | Abstract and introduction: Raman maps resolve about the laser spot size (about 500 nm) and average over it; the 2D line width measures strain variations on the nanometre scale, which limit carrier mobility in high-quality devices. Results: G line width measured at 8 T is increased where the flake has bubbles and folds, identified by scanning force microscopy |
| 7 | J. E. Lee, G. Ahn, J. Shim, Y. S. Lee and S. Ryu, Optical separation of mechanical strain from charge doping in graphene, Nat. Commun. 3, 1024 (2012) | doi:10.1038/ncomms2022 | full text | Abstract and introduction: G and 2D modes are both sensitive to strain and charge, which complicates determining either alone; correlation analysis separates them; thermal treatment produces compression and hole doping. Discussion: decomposition into strain, p-type and n-type doping is not unambiguous unless one component is known or assumed, and the analysis is tied to the excitation wavelength used |
| 8 | A. Allain, J. Kang, K. Banerjee and A. Kis, Electrical contacts to two-dimensional semiconductors, Nat. Mater. 14, 1195–1205 (2015); read as the open-access copy in the EPFL Infoscience repository | doi:10.1038/nmat4452 | full text | "Interface geometry": top and edge contacts perform differently; Fermi-level pinning from metal–MoS2 alloying and gap states limits tuning of the barrier by choice of metal. "Extraction of the Schottky barrier height" and Fig. 4: activation energy equals the barrier height only at flat band, identified where it stops depending linearly on gate voltage; channel resistance contributes to the temperature dependence; image-force lowering at finite bias underestimates the barrier, reduced by extrapolating to zero bias; barrier inhomogeneity gives apparent temperature dependences |
| 9 | J. O. Island, G. A. Steele, H. S. J. van der Zant and A. Castellanos-Gomez, Environmental instability of few-layer black phosphorus, 2D Mater. 2, 011002 (2015); read as arXiv:1410.2608 | doi:10.1088/2053-1583/2/1/011002 | full text | Abstract and results: in air, flakes take up water within hours and are etched layer by layer; transistor threshold voltage shifts within minutes from adsorbed oxygen and nitrogen, strong p-type doping follows over hours from water, and channels degrade within days; top-side hBN encapsulation alone did not prevent degradation |
| 10 | P. Bøggild, T. J. Booth, B. S. Jessen, A. Shivayogimath, N. Lassaline, S. Hofmann, O. Burton, K. Daasbjerg, A. Smith, K. Nørgaard, A. Zurutuza, T. Barkan and A. J. Pollard, Recommendations and tools to enable reproducibility in 2D materials research, arXiv:2409.18994 (2024) | doi:10.48550/arXiv.2409.18994 | full text | Introduction: atomic thinness makes 2D materials sensitive to ambient conditions, surface contamination and minor processing variations, and factors such as tape type, substrate roughness or humidity can change outcomes. "Reporting results": omitting polymer type, annealing temperature, ambient conditions or process timing prevents comparable outcomes; reviewers are asked to check that key parameters, sample sizes and process variability are reported |
| 11 | A. Raja, A. Chaves, J. Yu, G. Arefe, H. M. Hill, A. F. Rigosi, T. C. Berkelbach, P. Nagler, C. Schüller, T. Korn, C. Nuckolls, J. Hone, L. E. Brus, T. F. Heinz, D. R. Reichman and A. Chernikov, Coulomb engineering of the bandgap and excitons in two-dimensional materials, Nat. Commun. 8, 15251 (2017) | doi:10.1038/ncomms15251 | full text | Abstract and introduction: beyond a few nanometres the screening in a monolayer is set by its surroundings; changing the dielectric environment shifts the band gap and exciton binding energy of WS2 and WSe2 monolayers by hundreds of meV; a spatially varying environment produces a lateral band-gap profile with wells above 100 meV |
| 12 | F. Cadiz, E. Courtade, C. Robert, G. Wang, Y. Shen, H. Cai, T. Taniguchi, K. Watanabe, H. Carrere, D. Lagarde, M. Manca, T. Amand, P. Renucci, S. Tongay, X. Marie and B. Urbaszek, Excitonic linewidth approaching the homogeneous limit in MoS2-based van der Waals heterostructures, Phys. Rev. X 7, 021026 (2017) | doi:10.1103/PhysRevX.7.021026 | full text | Abstract: low-temperature optical linewidths of MoS2 are typically tens of meV, with inhomogeneous contributions; hBN encapsulation suppresses the inhomogeneous part, giving widths down to 2 meV; surface protection and substrate flatness are named as key to sample quality. Sec. II.A: hBN protects the layer from charge transfer, field fluctuations and roughness of the substrate; encapsulation lowers both the free-carrier gap and the exciton binding energy, so the emission energy shifts only slightly |
