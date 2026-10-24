---
id: T-GLASS-TRANSITION
name: Glass transition and dynamic heterogeneity
type: technique
field: physics/soft-matter
applies_when: the paper reports a glass transition temperature or volume fraction, relaxation times of supercooled liquids, colloidal glasses or jammed packings, fragility or a divergence from fits, ageing, dynamic heterogeneity or a dynamic length scale, or confinement or finite-size effects on glassy dynamics
version: "0.1"
---

# Glass transition and dynamic heterogeneity

Experiments on glass-forming liquids, colloidal glasses and jammed packings are used to claim a glass transition temperature (Tg) or volume fraction, how the structural relaxation time (τα) grows on approach to it, a fragility or an underlying divergence, and spatially heterogeneous dynamics measured by quantities such as the four-point susceptibility (χ4) and the dynamic length scale it implies. Because the glass transition is the point where relaxation becomes slower than the experiment, each of these depends on rates, waiting times, definitions and sample size that the paper has to state.

## 1. Definition of the glass transition and its rate dependence

**Question.** Which criterion defines the glass transition in the paper (a calorimetric or dilatometric step, a viscosity near 10^12 Pa s, a relaxation time near 100 s, or the volume fraction at which relaxation exceeds the measurement window), and at what cooling or heating rate, on cooling or on heating, and after what thermal or mechanical history was it taken?

**Why it matters.** The glass transition marks where the liquid falls out of equilibrium on the time scale of the experiment, so its location moves with the cooling rate, the heating rate of the scan and any ageing before it, and calorimetric and viscosity criteria give slightly different values. A value without its criterion and rate cannot be compared with another, and a difference between samples or conditions can come from protocol alone.

**Resolved by.** The criterion stated, with the rate, scan direction and prior history; Tg compared only between data taken by the same criterion and protocol, or the rate dependence measured and shown; for colloids, the volume fraction at the glass transition tied to an explicit relaxation-time criterion and to the duration of the measurement.

**Benchmark.** [1], [2], [3]

## 2. Equilibration, ageing and stationarity

**Question.** Were relaxation times measured in a state that had stopped evolving, and how was this shown: was the waiting time after the quench, shear melting or preparation stated, and were measurements repeated at different waiting times?

**Why it matters.** Near and below the glass transition the sample relaxes towards an equilibrium it may not reach, and its relaxation time grows with the time since preparation, often as a power of the waiting time. A correlation function averaged over a period in which the sample is ageing mixes states of different age, the plateau of a mean-squared displacement lengthens as the sample ages, and apparently stationary subdiffusion can be a transient lasting many decades in time. Treating such data as equilibrium values distorts the temperature or volume fraction dependence of the relaxation time.

**Resolved by.** The starting point of the waiting time defined (end of a quench, of shear rejuvenation or of mixing) and the protocol given; data at two or more waiting times showing that the relaxation time no longer changes, or two-time correlation functions or time-resolved measurements where it still does; equilibrium and ageing data labelled as such and analysed separately; for calorimetry, the annealing history given so that ageing effects on the scan can be identified.

**Benchmark.** [1], [3], [4]

## 3. Amorphous state confirmed

**Question.** Does the paper show that the sample stayed amorphous and homogeneous for the whole measurement, with no crystallisation, demixing or phase separation, and is the size spread or mixture composition chosen to suppress crystallisation stated?

**Why it matters.** Monodisperse hard-sphere colloids eventually crystallise, so glassy colloidal samples need a size spread of several per cent or a mixture of sizes, and walls can nucleate crystals. Crystallites slow the dynamics and change the structure, and can be mistaken for glassy arrest or for a growing static order.

**Resolved by.** The polydispersity or mixture composition reported; structural data, such as the structure factor, pair correlation function, local order analysis or a calorimetric check for melting, taken at the end of the longest measurement and showing no crystalline order; the data taken away from walls that can nucleate crystals, or the absence of crystals near them shown.

**Benchmark.** [3], [9]

## 4. Relaxation time definition and fits

**Question.** How is the relaxation time defined (which correlation function, at which wavevector or probe length, by which threshold or fitted form), over how many decades of relaxation time do the data extend, and does any claimed divergence temperature or volume fraction, or fragility, survive a change of fitting function?

**Why it matters.** The value of τα depends on the observable and on the threshold or stretched exponential used. Vogel-Fulcher-Tammann, mode-coupling, Arrhenius and other forms can all describe a few decades of data, and the data alone usually cannot select between them, so a divergence temperature or volume fraction found by extrapolation reflects the chosen function. Mode-coupling fits in particular hold only over a window of two or three decades, and colloids and simulations cover far fewer decades than molecular liquids, so fits to them constrain behaviour near the glass transition weakly.

**Resolved by.** The correlation function, wavevector and definition of τα stated, with a check that conclusions do not depend on the choice; the dynamic range covered stated; more than one functional form fitted, with parameter uncertainties and the range of each fit; extrapolated divergences presented as properties of a fit unless data reach close to them; fragility given with the method used and the temperature or volume fraction scale it is defined on.

**Benchmark.** [1], [2], [3], [5]

## 5. Measures of dynamic heterogeneity

**Question.** Which measure of dynamic heterogeneity is used (χ4 or the four-point correlation function, a non-Gaussian parameter, a population of mobile particles above a threshold, a bound from the temperature or density derivative of a two-point function), with what probe length, time window, statistical ensemble and number of particles, and how was its statistical uncertainty found?

**Why it matters.** The size of χ4 depends on the probe length and on the time at which it is evaluated: dynamics look homogeneous if the probe length is far below or far above the typical displacement, and the peak sits near the relaxation time. χ4 also depends on whether temperature or density fluctuates in the ensemble measured, and the derivative route gives only a lower bound. χ4 comes from small fluctuations of a sample average, so a small field of view or sample gives a noisy estimate, and in light scattering a non-zero non-Gaussian parameter cannot by itself separate coexisting fast and slow populations from homogeneous non-diffusive motion.

**Resolved by.** The measure defined with its probe length, thresholds and time; results shown as a function of probe length and of time, not at one chosen value; the ensemble stated and, where χ4 is compared between systems or with theory, put on the same footing; the number of particles or independent regions stated with an uncertainty from repeated measurements; heterogeneity confirmed by direct imaging or by more than one measure where the claim depends on it.

**Benchmark.** [2], [4], [6]

## 6. Dynamic length scales, finite size and confinement

**Question.** When the paper extracts a dynamic length scale, or claims that confinement or system size changes the glass transition, is the length compared with the size of the sample, field of view or simulation box, and is the effect separated from interactions with walls, free surfaces or substrates?

**Why it matters.** Dynamic correlation lengths near the glass transition are modest, of order a few to ten particle or molecular diameters, and measuring them requires systems much larger than the length and a reliable tail of the correlation function. In thin films, pores and narrow colloidal cells the free surface speeds up relaxation while attractive or rough walls slow it, so the reported shift depends on surface conditions and on which part of the sample a method weights; different methods can give shifts of different size and sign for nominally the same system.

**Resolved by.** The length scale given with the system or field-of-view size and the range of distances fitted; results shown to be unchanged in a larger sample or box; for confined samples, the surface treatment, wall roughness and substrate interaction stated, the thickness or pore size varied, and the Tg or relaxation measure identified with the part of the sample it reflects; where possible, a direct measurement of the gradient in mobility across the sample.

**Benchmark.** [2], [3], [6], [7]

## 7. Jamming and its distinction from the glass transition

**Question.** For claims about jamming of grains, foams, emulsions or soft colloids, does the paper say whether thermal motion is relevant, how the packing was prepared, how the jamming point was located, how rattlers and contacts were identified, and how the distance to jamming was measured?

**Why it matters.** Jamming is defined for packings at zero temperature and zero shear, whereas the glass transition is set by relaxation of thermal motion; in hard-sphere-like systems the colloidal glass transition, near a volume fraction of 0.58, lies below random close packing, near 0.64, and the two are easily conflated. The jamming packing fraction is not unique: it depends on preparation history and friction, and scatters between packings in a way that narrows with system size. Rattlers carry no force and spoil contact counts if they are included, and single packings scatter so much that scaling laws appear only after averaging over many.

**Resolved by.** The system identified as thermal or athermal, with its softness, friction and any driving stated; the preparation protocol given and the jamming point located for the same protocol; rattlers defined and excluded from contact numbers; distance to jamming measured by excess packing fraction, pressure or particle overlap over a range that supports any scaling claim; averaging over several packings, with system size stated.

**Benchmark.** [2], [3], [8]

## 8. Volume fraction scale in colloidal and soft-particle glasses

**Question.** For colloidal, emulsion or microgel samples, how was the absolute volume fraction determined (weighing, mapping to the hard-sphere freezing and melting points, particle counting, sedimentation, or a generalised volume fraction for soft particles), which particle radius was used, and how large is the systematic uncertainty on that scale?

**Why it matters.** Viscosity and relaxation time change steeply with volume fraction near the glass transition, yet the absolute volume fraction of colloids carries systematic errors of a few per cent from particle size, polydispersity, swelling, softness and charge. A shift of this size moves an apparent divergence or glass volume fraction, and can make data sets from different studies appear to disagree when they are consistent, or to agree when they are not.

**Resolved by.** The method used to set the volume fraction stated, with the radius definition, polydispersity and any correction for softness or charge; the systematic uncertainty on the absolute scale given separately from the much smaller uncertainty between samples of one batch; comparisons with other experiments, simulations or theory made with that uncertainty in view, or on a scale fixed by a shared reference point such as the freezing volume fraction.

**Benchmark.** [3], [9]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Micoulaut, Relaxation and physical aging in network glasses: a review, Rep. Prog. Phys. 79, 066504 (2016); read as preprint arXiv:1605.07403 | doi:10.1088/0034-4885/79/6/066504 | full text | Secs. 1 and 2.1: glass transition defined by a viscosity of 10^12 Pa s, relaxation times of roughly 100 to 1000 s, calorimetric Tg slightly different. Sec. 2.5.1: Tg cannot be uniquely defined; faster cooling freezes in a higher fictive temperature; Tg rises with heating rate; ageing below Tg gives a heat-capacity overshoot on reheating that grows with annealing time. Secs. 2.1 to 2.4: fragility defined from the slope at Tg; VFT diverges at finite temperature while other forms do not; stretched exponential fits and their link to fragility (read up to Sec. 4.2) |
| 2 | L. Berthier and G. Biroli, Theoretical perspective on the glass transition and amorphous materials, Rev. Mod. Phys. 83, 587 (2011); read as preprint arXiv:1011.2578 | doi:10.1103/RevModPhys.83.587 | full text | Sec. II.1.1: Tg set by a viscosity of 10^12 Pa s and depends on the cooling rate and the time scale of observation. Sec. II.1.2: data cannot unambiguously select the functional form of the relaxation time; claims of a singularity, or of none, need caution. Sec. II.2.1: hard spheres jam near 0.57 to 0.59, as ill-defined as Tg; grains are athermal. Sec. III.1: dynamic lengths near Tg about 10 molecular diameters. Sec. III.2.2: dynamics look homogeneous if the coarse-graining length is too small or too large; the variance of a sample average scales inversely with volume; very large systems are needed to determine the dynamic length. Secs. III.2.4 and III.3: χ4 depends on the statistical ensemble; the temperature-derivative route gives a lower bound. Secs. IV.2.2 and IV.2.4: mode-coupling fits hold over 2 to 3 decades and judging them is subjective |
| 3 | G. L. Hunter and E. R. Weeks, The physics of the colloidal glass transition, Rep. Prog. Phys. 75, 066501 (2012); read as preprint arXiv:1106.3581 | doi:10.1088/0034-4885/75/6/066501 | full text | Sec. 1.4 and Fig. 1: monodisperse samples always eventually crystallise, glassy samples need about 8 per cent polydispersity; wall nucleation may affect crystallisation. Sec. 2.6: layering near walls likely changes dynamics. Sec. 3.1: small volume fraction changes give large changes in viscosity, and an accurately known volume fraction is hard to achieve; the colloidal glass transition near 0.58 lies below random close packing near 0.64; Doolittle fits diverge near random close packing while mode-coupling fits diverge elsewhere. Sec. 3.2 and Fig. 11: glass transition referenced to a 100 s relaxation-time criterion. Sec. 3.4: confinement raises or lowers Tg depending on boundary conditions; rough walls slow colloids further. Sec. 4.2: ageing samples are shear-rejuvenated and waiting time starts when stirring stops; mean-squared displacement depends on waiting time |
| 4 | L. Cipelletti and L. Ramos, Slow dynamics in glassy soft matter, J. Phys.: Condens. Matter 17, R253 (2005); read as preprint arXiv:cond-mat/0502024 | doi:10.1088/0953-8984/17/6/R01 | full text | Sec. 3.1: subdiffusive transients up to about 10^7 Brownian times in hard-sphere glasses. Sec. 3.2: age defined from the quench or end of shear; relaxation time grows as a power of waiting time; no age dependence below the glass volume fraction, clear slowing above it; behaviour depends on system and initialisation. Sec. 5.2: time-resolved correlation as an analogue of two-time correlation functions for evolving samples; in light scattering a non-zero non-Gaussian parameter cannot distinguish coexisting fast and slow populations from homogeneous non-diffusive motion |
| 5 | T. Hecksher, A. I. Nielsen, N. B. Olsen and J. C. Dyre, Little evidence for dynamic divergences in ultraviscous molecular liquids, Nat. Phys. 4, 737–741 (2008) | doi:10.1038/nphys1033 | abstract | Abstract (Roskilde University research portal): dielectric relaxation data for 42 organic liquids near the glass transition give no compelling support for the finite-temperature divergence predicted by the Vogel-Fulcher-Tammann law |
| 6 | L. Berthier, Dynamic heterogeneity in amorphous materials, Physics 4, 42 (2011); read as preprint arXiv:1106.1739 | doi:10.1103/Physics.4.42 | full text | Sections on four-point functions: χ4 defined from a mobility with a probe length of order the particle size; it peaks near the relaxation time. Section on measurements: the fluctuations are small, direct measurement is possible in colloids and grains, molecular liquids need the derivative bound. Section on length scales: lengths stay modest, nanometres in molecular liquids; simulations limited by system size and need the tail of the correlation function; colloids, grains and simulations span at most 5 to 6 decades of relaxation time against up to 14 for molecular liquids |
| 7 | W. Zhang, J. F. Douglas and F. W. Starr, Why we need to look beyond the glass transition temperature to characterize the dynamics of thin supported polymer films, Proc. Natl. Acad. Sci. USA 115, 5641–5646 (2018); read on PubMed Central (PMC5984511) | doi:10.1073/pnas.1722024115 | full text | Introduction: reported Tg shifts in thin films differ in size and sign for nominally identical systems. Results: the free surface is mobile, a strongly attractive substrate forms a slow layer; thermodynamic and dynamic Tg measures weight these regions differently and can give opposite trends. Conclusions: no single Tg measure characterises the film; combine thermodynamic and dynamic measures and measure the mobility gradient directly. A simulation study of supported polymer films |
| 8 | M. van Hecke, Jamming of soft particles: geometry, mechanics, scaling and isostaticity, J. Phys.: Condens. Matter 22, 033101 (2010); read as preprint arXiv:0911.1384 | doi:10.1088/0953-8984/22/3/033101 | full text | Secs. I and III.1: jamming treated at zero temperature and zero shear. Sec. III.2: the jamming density varies between packings, with a spread that shrinks with system size and a large-system value near 0.64 in three dimensions; random close packing is a contested concept; distance to jamming measured by excess density, pressure or average overlap. Sec. III.3: rattlers, up to about 5 per cent at low pressure, excluded from contact numbers. Secs. III.4 and III.5: individual packings scatter, so scaling is seen after averaging over many packings. Sec. IV.1: friction and preparation history change the jamming density and contact number |
| 9 | W. C. K. Poon, E. R. Weeks and C. P. Royall, On measuring colloidal volume fractions, Soft Matter 8, 21–30 (2012); read as preprint arXiv:1106.2566 | doi:10.1039/C1SM06083J | full text | Abstract and Sec. V.8: relative volume fractions can be precise but systematic errors of 3 to 6 per cent in the absolute value are probably unavoidable; viscosity and nucleation rates change steeply with volume fraction. Sec. III: several radius definitions, each sizing method with its own caveats. Sec. IV: polydispersity shifts freezing and melting; crystallisation fails above roughly 7 per cent. Secs. V.1 to V.7: weighing, mapping to freezing and melting, sedimentation and particle counting each carry systematic errors; swelling and sedimentation change the volume fraction. Sec. VI: rescaling volume fractions by a few per cent reconciles two data sets near 0.58. Sec. VII: papers should state how the volume fraction was found and its likely systematic error |
