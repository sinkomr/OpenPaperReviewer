---
id: T-DUSTY-PLASMAS
name: Dusty and complex plasmas
type: technique
field: physics/plasma
applies_when: the paper reports experiments with charged microparticles in a plasma, infers particle charge, mass or forces such as ion drag and thermophoresis from particle motion, tracks particles in video images, or claims crystalline order, melting or waves in a dusty or complex plasma
version: "0.1"
---

# Dusty and complex plasmas

Experiments on dusty or complex plasmas, in which charged microparticles are suspended in a weakly ionized gas, are used to claim particle charges, the forces on particles (electric, ion drag, neutral gas drag and thermophoretic), and the structure and dynamics of the particle ensemble, including crystalline order, melting and waves. Most of these quantities are inferred from video images of particles lit by a laser sheet, through a force balance or a model of the interaction between particles.

## 1. Particle size and mass in the plasma

**Question.** Does the paper state the material, nominal size and size spread of the particles and how long they were exposed to the plasma, and does it show that their size and mass did not change over the experiment, or measure them in situ?

**Why it matters.** Particle mass and radius enter every force balance, charge estimate and drag coefficient. Polymer microspheres held in a discharge can gain mass from deposited sputtered material and lose it by outgassing and degradation in the discharge, and over tens of minutes they can shrink to a fraction of their initial size, so the supplier's value may not hold for the whole experiment.

**Resolved by.** Material, density, nominal diameter and spread stated; time in the plasma reported for each data set; mass or size followed in situ, for example through the vertical resonance frequency, or particles recovered and measured afterwards; results shown not to drift with the time the particles have spent in the plasma.

**Benchmark.** [1], [2]

## 2. Particle charge

**Question.** Was the particle charge measured, and by which method, or calculated from a charging theory, and does the paper show that the assumptions of that method or theory hold at its gas pressure and at the position of the particles (sheath or plasma bulk)?

**Why it matters.** Charges calculated from the collisionless orbital-motion-limited theory can be several times larger than measured charges at the gas pressures of many discharge experiments, because collisions between ions and gas atoms reduce the charge. Measured charges come from the response of particles to a perturbation or from waves, interpreted through a model of the confinement or of the interaction and through the particle mass, so they inherit the limits of that model.

**Resolved by.** The charge measured by a named method suited to where the particles are, with the model, mass and other inputs stated; any theoretical estimate including ion-neutral collisions and compared with a measurement; where two methods are available, their agreement shown.

**Benchmark.** [3], [4], [5], [22]

## 3. Forces in the balance

**Question.** When a force, charge or field is inferred from particle positions or velocities, which forces does the paper include (electric, gravity, neutral gas drag, ion drag, thermophoresis, radiation pressure from the illuminating or manipulating laser), which model and coefficients are used for each, and does the conclusion hold under alternative ion drag models?

**Why it matters.** A force balance is only as good as the models for the forces it keeps or omits. Ion drag estimates differ from each other by up to about a factor of two depending on the ion velocity distribution, the collisionality and the shielding length assumed, and the standard Coulomb scattering treatment fails under typical conditions. A gas temperature gradient, such as one from a heated or cooled electrode, moves particles by thermophoresis with forces that can balance gravity, and measured neutral drag and radiation pressure coefficients differ from their idealized values.

**Resolved by.** Every force listed with its formula, coefficients and their source; electrode and wall temperatures stated, or the gas temperature gradient estimated and the thermophoretic force compared with the others; the neutral drag coefficient given with its source; ion drag evaluated with more than one model or measured, with the spread shown not to change the conclusion; radiation pressure from any laser estimated.

**Benchmark.** [6], [7], [8], [9], [10]

## 4. Imaging and particle tracking

**Question.** Does the paper report the pixel scale, frame rate, particle image size and position-finding method, check for pixel locking, and show that velocities and kinetic temperatures do not depend on the time interval between the frames used?

**Why it matters.** Sub-pixel positions from intensity moments tend to cluster at preferred places relative to pixel edges (pixel locking), with errors set by the threshold, spot size, baseline and noise. A two-frame velocity combines a position error that grows at high frame rates with an acceleration error that grows at low ones, so a kinetic temperature from particle tracking has no unique value and depends on the interval chosen; velocity distributions can show spurious peaks and short-time displacements are exaggerated.

**Resolved by.** Pixel scale, frame rate, spot size in pixels, threshold and baseline stated; sub-pixel maps or tests on simulated images showing that pixel locking is small; the quantity of interest plotted against sampling interval and taken from a range where it is flat; multi-frame or smoothed velocities for correlation functions; the position uncertainty and its contribution to the kinetic temperature estimated.

**Benchmark.** [11], [12]

## 5. Gravity, sheath levitation and microgravity

**Question.** Where in the discharge were the particles held, and does the paper account for what that implies: in ground experiments, the strong field and ion flow of the sheath that balance gravity; in microgravity, the residual accelerations of the platform and the region kept free of particles?

**Why it matters.** Under gravity, particles levitate in the sheath or form thin layers and compressed three-dimensional clouds, and streaming ions form positive space charge below each particle; this aligns particles vertically, makes forces between layers attractive and can drive oscillations below a threshold gas density. Microgravity removes the compression but not the ion flow, which can push particles out of a central void, and aircraft parabolic flights give about 20 s per parabola with residual accelerations of order 10^-2 g and larger transients at entry.

**Resolved by.** The particle position relative to the sheath edge, and the plasma parameters there, reported; vertical structure such as alignment and layer spacing examined before the system is treated as isotropic or three-dimensional; for microgravity, the platform, duration and measured residual acceleration during the data used, and the void size and position, reported; data restricted to periods of stable low gravity.

**Benchmark.** [6], [13], [14], [15]

## 6. Crystalline order, melting and coupling strength

**Question.** How does the paper establish crystalline order or a phase transition (which structural measures, over how many particles), how are the coupling and screening parameters obtained, and does it consider plasma-driven heating and non-reciprocal interactions before comparing with an equilibrium phase diagram?

**Why it matters.** The equilibrium phase boundaries of particles with a screened Coulomb (Yukawa) interaction depend on both the coupling and the screening parameters, which rest on the charge, the screening length and the kinetic temperature. A particle ensemble in a plasma is driven: flowing ions make interactions non-reciprocal, so that the force of one particle on another is not matched by the reverse force and different species can have different kinetic temperatures, and two-dimensional crystals can melt through a plasma-driven mode-coupling instability instead of by thermal fluctuations.

**Resolved by.** Pair correlation, bond-orientational order or defect statistics computed over a stated field of view containing many lattice spacings; the coupling and screening parameters given with the charge, screening length and temperature behind them; kinetic temperatures reported for each direction and each species; the kinetic energy followed through the transition, and lattice-mode spectra checked for coupled or hybrid modes, before melting is interpreted as thermal; equilibrium and driven regimes distinguished.

**Benchmark.** [16], [17], [18], [19], [20]

## 7. Waves and parameters from dispersion relations

**Question.** When waves are used to infer charge, screening length or damping, does the paper state how they were excited and in which direction relative to the lattice, which wave model was fitted, which parameters were free, and how well the fit constrains each one?

**Why it matters.** Charge, screening parameter and damping rate are often obtained together by fitting measured dispersion relations to a model, and the dispersion depends on the screening, the damping and the direction of propagation. Different wave models describe the same data differently, so the values returned depend on the model chosen, and spectra from random particle motion are taken from a system that is not in thermal equilibrium.

**Resolved by.** The excitation method and amplitude stated and the response shown to be linear; the direction of propagation relative to the lattice given; real and imaginary parts fitted with damping included, or the friction coefficient fixed from an independent estimate; the charge fixed from an independent measurement where possible, or the correlation between fitted charge and screening parameter reported; the chosen model compared with alternatives.

**Benchmark.** [8], [21], [22], [23]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | J. Carstensen, H. Jung, F. Greiner and A. Piel, Mass changes of microparticles in a plasma observed by a phase-resolved resonance method, Phys. Plasmas 18, 033701 (2011); abstract read from the Crossref record | doi:10.1063/1.3556677 | abstract | Abstract: precise measurements of the vertical confinement frequency show that the plasma changes the mass of melamine formaldehyde particles, with a gain from deposited sputtered material and a loss from water outgassing |
| 2 | E. S. Dzlieva, A. P. Gorbenko, M. S. Golubev, M. A. Ermolenko, L. A. Novikov, S. I. Pavlov, V. A. Polishchuk and V. Yu. Karasev, Modification and mass loss of melamine formaldehyde particles in dusty plasma formed in heavy noble gas, Plasma Phys. Rep. 49, 136–141 (2023); abstract read on the Springer journal page | doi:10.1134/S1063780X22601791 | abstract | Abstract: particles held in an argon glow discharge trap shrink from about 7.3 to 3.5 µm in 30 min, losing most of their mass in stages; the rate depends on the gas; recommendations for long experiments |
| 3 | S. Ratynskaia, S. Khrapak, A. Zobnin, M. H. Thoma, M. Kretschmer, A. Usachev, V. Yaroshenko, R. A. Quinn, G. E. Morfill, O. Petrov and V. Fortov, Experimental determination of dust-particle charge in a discharge plasma at elevated pressures, Phys. Rev. Lett. 93, 085001 (2004); abstract read on the APS journal page | doi:10.1103/PhysRevLett.93.085001 | abstract | Abstract: charges measured at 20 to 100 Pa by two independent methods agree with simulations and are several times lower than the collisionless theory predicts, pointing to ion-neutral collisions |
| 4 | S. A. Khrapak, S. V. Ratynskaia, A. V. Zobnin, A. D. Usachev, V. V. Yaroshenko, M. H. Thoma, M. Kretschmer, H. Höfner, G. E. Morfill, O. F. Petrov and V. E. Fortov, Particle charge in the bulk of gas discharges, Phys. Rev. E 72, 016406 (2005); abstract read on the APS journal page | doi:10.1103/PhysRevE.72.016406 | abstract | Abstract: measured charges are well below orbital-motion-limited values; comparison with simulations, other measurements and a collisional model shows that ion-neutral collisions substantially reduce the charge under typical discharge conditions |
| 5 | H. Jung, F. Greiner, O. H. Asnaz, J. Carstensen and A. Piel, Resonance methods for the characterization of dust particles in plasmas, J. Plasma Phys. 82, 615820301 (2016); abstract read on the Cambridge journal page | doi:10.1017/S0022377816000441 | abstract | Abstract: resonance methods infer particle mass, charge and the interaction between particles from the dynamic response of particles in the sheath to small external perturbations |
| 6 | S. A. Khrapak, A. V. Ivlev, G. E. Morfill and H. M. Thomas, Ion drag force in complex plasmas, Phys. Rev. E 66, 046414 (2002); abstract read on the APS journal page | doi:10.1103/PhysRevE.66.046414 | abstract | Abstract: standard Coulomb scattering theory usually fails for ion-dust collisions; an extended theory gives a substantially larger ion drag, which typically exceeds the electric force in weak fields and is the likely cause of the central void in microgravity experiments |
| 7 | I. H. Hutchinson and C. B. Haakonsen, Collisional effects on nonlinear ion drag force for small grains, Phys. Plasmas 20, 083701 (2013); read as preprint arXiv:1305.6944 | doi:10.1063/1.4818144 | full text | Secs. I and II: reliable drag values in collisional plasmas were not known; Coulomb-logarithm and linearized-shielding treatments do not apply to typical grains. Sec. VI: a drift distribution changes the drag by up to a factor of two against a shifted Maxwellian; moderate collisionality raises the drag by up to about two; the nonlinear shielding length is needed |
| 8 | B. Liu, J. Goree, V. Nosenko and L. Boufendi, Radiation pressure and gas drag forces on a melamine-formaldehyde microsphere in a dusty plasma, Phys. Plasmas 10, 9–20 (2003); abstract read from the Crossref record | doi:10.1063/1.1526701 | abstract | Abstract: radiation pressure coefficient measured as 0.94; Epstein drag coefficient in argon measured as 1.26 or 1.44 by two methods, against unity for specular reflection |
| 9 | G. M. Jellum, J. E. Daugherty and D. B. Graves, Particle thermophoresis in low pressure glow discharges, J. Appl. Phys. 69, 6923–6934 (1991); abstract read from the Crossref record | doi:10.1063/1.347630 | abstract | Abstract: changing the temperature of the water cooling the electrodes moved suspended particles away from the heated electrode toward the cooled one |
| 10 | H. Rothermel, T. Hagl, G. E. Morfill, M. H. Thoma and H. M. Thomas, Gravity compensation in complex plasmas by application of a temperature gradient, Phys. Rev. Lett. 89, 175001 (2002); abstract read on the APS journal page | doi:10.1103/PhysRevLett.89.175001 | abstract | Abstract: a gas temperature gradient produces a thermophoretic force that can levitate micron-sized particles against gravity |
| 11 | Y. Feng, J. Goree and B. Liu, Accurate particle position measurement from images, Rev. Sci. Instrum. 78, 053704 (2007); read as arXiv:1104.3776 | doi:10.1063/1.2735920 | full text | Sec. II: pixel locking defined and shown in dusty plasma images with sub-pixel maps. Secs. V and VI: error depends on threshold, spot size, baseline and noise, with recommended choices. Appendix: spurious peaks in velocity distributions, exaggerated short-time mean-square displacement, and sensitive structural measures such as defect maps expected to be affected |
| 12 | Y. Feng, J. Goree and B. Liu, Errors in particle tracking velocimetry with high-speed cameras, Rev. Sci. Instrum. 82, 053707 (2011); read as arXiv:1104.3540 | doi:10.1063/1.3589267 | full text | Sec. II: two-frame velocity error from position uncertainty grows as the interval shrinks, acceleration error grows as it lengthens; analyse at several intervals and look for a flat region. Sec. III: kinetic temperature has no unique value and depends on the sampling interval; multi-frame tracking or smoothing for correlation functions |
| 13 | M. H. Thoma, H. M. Thomas, C. A. Knapek, A. Melzer and U. Konopka, Complex plasma research under microgravity conditions, npj Microgravity 9, 13 (2023); read on PubMed Central (PMC9905515) | doi:10.1038/s41526-023-00261-8 | full text | Introduction: gravity restricts ground experiments to two-dimensional, quasi-two-dimensional or compressed, stressed three-dimensional clouds. Fig. 2 caption: under microgravity the cloud fills the chamber apart from a central void. PK-4 section: under gravity particles sit near the bottom of the tube, where the sheath field prevents the string formation seen in microgravity |
| 14 | V. A. Schweigert, I. V. Schweigert, A. Melzer, A. Homann and A. Piel, Alignment and instability of dust crystals in plasmas, Phys. Rev. E 54, 4155 (1996); abstract read on the APS journal page | doi:10.1103/PhysRevE.54.4155 | abstract | Abstract: particles in layered sheath crystals align vertically and oscillate below a threshold gas density; positive ion clouds below each particle give attractive forces that differ between layers |
| 15 | V. Pletser, Aircraft parabolic flights: a gateway to orbital microgravity and extra-terrestrial planetary gravities, in Preparation of Space Experiments, ed. V. Pletser, IntechOpen (2020) | doi:10.5772/intechopen.93464 | full text | Abstract and Sec. 3: about 20 s of microgravity per parabola; residual accelerations at floor-mounted set-ups typically of order 10^-2 g; a transitory phase of a few seconds at the start of the low-gravity period with variations of about 10^-1 g |
| 16 | S. Hamaguchi, R. T. Farouki and D. H. E. Dubin, Triple point of Yukawa systems, Phys. Rev. E 56, 4671 (1997); abstract read on the APS journal page | doi:10.1103/PhysRevE.56.4671 | abstract | Abstract: fluid-solid and solid-solid transition temperatures of Yukawa systems mapped as a function of the screening parameter, giving a phase diagram in coupling and screening parameters |
| 17 | V. Nosenko, S. K. Zhdanov, A. V. Ivlev, C. A. Knapek and G. E. Morfill, 2D melting of plasma crystals: equilibrium and nonequilibrium regimes, Phys. Rev. Lett. 103, 015001 (2009); abstract read on the APS journal page | doi:10.1103/PhysRevLett.103.015001 | abstract | Abstract: melting studied through defect density against kinetic temperature, with different behaviour under steady and time-varying heating, and evidence that melting starts at grain boundaries |
| 18 | L. Couëdel, V. Nosenko, A. V. Ivlev, S. K. Zhdanov, H. M. Thomas and G. E. Morfill, Direct observation of mode-coupling instability in two-dimensional plasma crystals, Phys. Rev. Lett. 104, 195001 (2010); abstract read on the APS journal page | doi:10.1103/PhysRevLett.104.195001 | abstract | Abstract: melting of two-dimensional plasma crystals is accompanied by a sudden rise in kinetic energy and is caused by resonant coupling of lattice modes, with a hybrid branch, as mode-coupling theory predicts |
| 19 | A. V. Ivlev, J. Bartnick, M. Heinen, C.-R. Du, V. Nosenko and H. Löwen, Statistical mechanics where Newton's third law is broken, Phys. Rev. X 5, 011035 (2015); abstract and popular summary read on the APS journal page | doi:10.1103/PhysRevX.5.011035 | abstract | Abstract and popular summary: action-reaction symmetry can break when interactions are mediated by a flowing environment such as a plasma; distinct species then acquire distinct kinetic temperatures; tested in two-dimensional binary complex plasmas |
| 20 | A. Melzer, V. A. Schweigert and A. Piel, Transition from attractive to repulsive forces between dust molecules in a plasma sheath, Phys. Rev. Lett. 83, 3194 (1999); abstract read on the APS journal page | doi:10.1103/PhysRevLett.83.3194 | abstract | Abstract: in a sheath with flowing ions, the attraction between two particles acts on only one of them, shown by laser manipulation |
| 21 | A. Homann, A. Melzer, S. Peters and A. Piel, Determination of the dust screening length by laser-excited lattice waves, Phys. Rev. E 56, 7138 (1997); abstract read on the APS journal page | doi:10.1103/PhysRevE.56.7138 | abstract | Abstract: the screening length is obtained by comparing a laser-excited dispersion relation with a one-dimensional lattice wave model; a dust acoustic wave model does not fit the same data |
| 22 | S. Nunomura, J. Goree, S. Hu, X. Wang and A. Bhattacharjee, Dispersion relations of longitudinal and transverse waves in two-dimensional screened Coulomb crystals, Phys. Rev. E 65, 066402 (2002); abstract read on the APS journal page | doi:10.1103/PhysRevE.65.066402 | abstract | Abstract: dispersion of laser-excited waves measured against screening parameter, damping rate and propagation direction; comparison with a model gives the screening parameter and particle charge |
| 23 | S. Nunomura, J. Goree, S. Hu, X. Wang, A. Bhattacharjee and K. Avinash, Phonon spectrum in a plasma crystal, Phys. Rev. Lett. 89, 035001 (2002); abstract read on the APS journal page | doi:10.1103/PhysRevLett.89.035001 | abstract | Abstract: spectra of waves from random particle motion in a two-dimensional crystal agree with a Yukawa dispersion relation; the crystal is not in thermal equilibrium, although phonon energy is spread almost evenly over wave numbers |
