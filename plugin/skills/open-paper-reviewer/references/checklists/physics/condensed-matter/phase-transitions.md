---
id: CL-PHASE-TRANSITIONS
name: Claims of a phase transition
type: claim
field: physics/condensed-matter
applies_when: the paper claims that a phase transition or ordered phase sets in, assigns a transition temperature or critical point, states the order of a transition, reports critical exponents or a scaling collapse, or claims quantum critical or non-Fermi-liquid behaviour near a quantum critical point
version: "0.1"
---

# Claims of a phase transition

A claim of a phase transition asserts that a material changes state at a sharp value of temperature, pressure, field, composition or another tuning parameter, usually with a change of symmetry described by an order parameter. Related claims concern the order of the transition (first order, with a discontinuity, or continuous), its critical exponents, and quantum critical behaviour near a continuous transition at zero temperature, a quantum critical point (QCP).

## 1. Order parameter and broken symmetry

**Question.** Does the paper name the order parameter or the symmetry that changes at the claimed transition, and show a measurement that couples to it and becomes non-zero at the transition, rather than only a kink or step in a property that does not?

**Why it matters.** An order parameter is zero in one phase and non-zero in the other, and this is what separates two phases from a single phase whose properties change gradually. A kink or step in one property can have other origins, so on its own it does not show which order, if any, sets in.

**Resolved by.** The proposed order parameter and broken symmetry stated; a probe that couples to it directly, such as superlattice or magnetic Bragg intensity, a static internal field seen by a local probe, or a spontaneous polarisation, followed through the transition and shown to vanish on the disordered side; the onset in that probe at the same temperature or tuning parameter as the anomalies in other quantities.

**Benchmark.** [1], [2], [10]

## 2. Transition or crossover

**Question.** Is the feature shown to be a sharp transition and not a smooth crossover, given the dimensionality and size of the system and any applied field that couples to the claimed order parameter?

**Why it matters.** A sharp transition exists only in the limit of a large system; in a finite system a transition is rounded and shifted. In two dimensions, with short-range interactions, a continuous symmetry cannot be broken at finite temperature, and a field that couples to the order parameter replaces the transition by a crossover whose susceptibility peak marks only a pseudo-critical line. A broad maximum in any of these cases can be read as a transition.

**Resolved by.** The width of the feature compared with the temperature or field steps and the measurement resolution; for films, two-dimensional systems, nanostructures and simulations, an argument from dimensionality, symmetry and size, and in simulations a comparison of several system sizes; the role of any applied field that couples to the order parameter discussed before a feature measured in that field is called a transition.

**Benchmark.** [1], [2], [7]

## 3. Bulk thermodynamic signature and volume fraction

**Question.** Is the transition seen in a bulk thermodynamic quantity, and is the size of that anomaly, or the ordered volume fraction from a local probe, consistent with the whole sample taking part?

**Why it matters.** A transition of the bulk is a singularity of the free energy, so it leaves a mark in thermodynamic quantities such as specific heat, thermal expansion or magnetisation. A probe that responds to part of the sample can register order in a minority phase or in isolated regions that the rest of the sample does not share. Near a QCP, a divergent Grüneisen ratio (thermal expansion divided by specific heat) is a thermodynamic signature of a continuous quantum transition that does not occur at a finite-temperature transition.

**Resolved by.** A thermodynamic anomaly at the same temperature or tuning parameter as the other signatures, with its size or the entropy released compared with what full participation of the sample would give; for local probes such as muon spin rotation, the ordered volume fraction stated with its uncertainty; near a claimed QCP, the Grüneisen ratio or the magnetocaloric effect measured where possible.

**Benchmark.** [2], [3], [4], [5], [10]

## 4. Order of the transition

**Question.** What evidence fixes the order of the transition: a jump in the order parameter, volume or entropy, a latent heat, coexistence of the two phases, or hysteresis; and was any hysteresis shown to belong to the sample and not to the way the measurement was made?

**Why it matters.** At a first-order transition the order parameter jumps and the two phases coexist, while at a continuous transition the order parameter vanishes continuously and the correlation length diverges. A weakly first-order transition can look continuous, and quenched disorder can round a first-order transition, so a smooth curve does not by itself prove a continuous transition. Some dynamic methods do not capture a latent heat, and a finite thermal link between sample and thermometer, or a sweep that does not cross the whole transition, distorts the hysteresis that is recorded.

**Resolved by.** The quantity that jumps measured with a method able to resolve it, such as long heat pulses that cross the transition or a structural probe showing the two phases together; heating and cooling, or up and down sweeps, compared, with the thermal coupling and sweep conditions stated; any latent heat reported separately from the continuous background; in simulations, the dependence of the specific-heat peak or energy distribution on system size compared with the forms expected for first-order and continuous transitions.

**Benchmark.** [1], [3], [4], [6], [7], [8]

## 5. Critical exponents and scaling analysis

**Question.** For quoted critical exponents or a scaling collapse, does the paper state the range of reduced temperature or tuning parameter fitted, how the critical point was fixed, whether correction-to-scaling and background terms were included, and how much the exponents change with these choices?

**Why it matters.** Power laws hold only asymptotically close to the critical point; further away, corrections to scaling and analytic background terms change the apparent exponent, and leaving out the leading correction can bias an exponent well beyond its statistical error. Fits over a narrow range, or with a free critical point or background, return exponents that depend on those choices, and a data collapse judged by eye is subjective.

**Resolved by.** Fits over more than a decade in the scaling variable, with the exponents shown to change little as the fit limits and the critical point are varied; correction and background terms included or shown to be small; a quantitative measure of the quality of a collapse, with uncertainties on the exponents; exponents checked against the scaling relations and compared with the expected universality class, or a reason given for departing from it.

**Benchmark.** [2], [3], [9]

## 6. Quantum critical behaviour

**Question.** For a claim of quantum criticality, is the transition followed towards zero temperature as a function of a stated tuning parameter, does the claimed critical behaviour hold over a wide enough range of temperature, and are disorder and a first-order transition considered as alternatives?

**Why it matters.** Universal quantum critical behaviour is expected only in a region close to the QCP, bounded at high temperature by microscopic energy scales and at the sides by crossovers, so a power law over a narrow window is weak evidence. Disorder can change the critical behaviour, give power laws with non-universal exponents over a whole region of the phase diagram through rare-region (Griffiths) effects, or smear the transition. A transition can also become first order at low temperature instead of ending at a QCP.

**Resolved by.** The phase boundary traced to the lowest temperatures reached, with the tuning parameter stated; power laws or scaling over more than a decade, and the return of conventional low-temperature behaviour away from the critical point; the dependence on sample quality, such as residual resistivity, examined; thermodynamic tests such as the Grüneisen ratio; evidence that the transition stays continuous at the lowest temperatures.

**Benchmark.** [1], [3], [4], [5]

## 7. Inhomogeneity and broadened transitions

**Question.** How broad is the transition, and does the paper show whether the width is intrinsic or comes from a spread of transition temperatures across the sample caused by composition gradients, strain or disorder?

**Why it matters.** Different parts of an inhomogeneous sample order at different values of the tuning parameter, so the measured transition is a superposition of local transitions. This rounding can be mistaken for critical behaviour, and in its tail ordered islands can coexist with a disordered bulk, so a measured onset may mark a small part of the sample.

**Resolved by.** The transition width given by a stated criterion and compared between samples, or between pieces of one sample; composition and homogeneity characterised on the piece measured; local or spatially resolved probes used to look for coexisting regions; critical or scaling analysis restricted to the range outside the rounded region, or modelled with a distribution of transition temperatures.

**Benchmark.** [3], [4], [6], [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Vojta, Quantum phase transitions, Rep. Prog. Phys. 66, 2069–2110 (2003); read as preprint arXiv:cond-mat/0309604 | doi:10.1088/0034-4885/66/12/R01 | full text | Sec. 2.1: the order parameter is zero in the disordered phase and non-zero in the other; at a first-order transition the phases coexist, at a continuous one the order vanishes continuously and the correlation length diverges. Sec. 2.2: quantum critical region bounded by crossover lines and cut off when temperature exceeds microscopic energy scales; universal behaviour only close to the QCP; no finite-temperature order in two-dimensional magnets with continuous symmetry. Sec. 2.4: a sharp transition needs the thermodynamic limit, and finite size rounds a transition into a crossover. Sec. 2.5.1: a first-order transition has a jump in the order parameter; continuum theories apply only to weakly first-order cases |
| 2 | A. Pelissetto and E. Vicari, Critical phenomena and renormalization-group theory, Phys. Rep. 368, 549–727 (2002); read as preprint arXiv:cond-mat/0012164 | doi:10.1016/S0370-1573(02)00219-3 | full text | Secs. 1.1 and 1.3: order parameter and its power-law vanishing; scaling forms valid only asymptotically close to the critical point, with corrections controlled by an irrelevant exponent; an analytic background must be included in the specific heat when its exponent is negative; scaling and hyperscaling relations between exponents; in a field the susceptibility peak defines a pseudo-critical crossover line. Sec. 1.5.7: correction and background terms enter all quantities. Sec. 2.2.1: omitting the leading correction term gives large systematic errors |
| 3 | H. v. Löhneysen, A. Rosch, M. Vojta and P. Wölfle, Fermi-liquid instabilities at magnetic quantum phase transitions, Rev. Mod. Phys. 79, 1015–1075 (2007); read as preprint arXiv:cond-mat/0606317 | doi:10.1103/RevModPhys.79.1015 | full text | Sec. I.3: power laws are meaningful only over a broad range; a fit is reliable if the exponent depends only weakly on the fit limits and spans more than a decade; effective exponents are biased by the choice of residual resistivity; scaling collapse used to extract exponents. Secs. I.4 and II.7: a broad distribution of Kondo temperatures and Griffiths phases give non-Fermi-liquid behaviour over a whole region. Sec. III.2: a divergent Grüneisen ratio is a unique signature of a continuous quantum transition. Sec. III.6: small amounts of disorder change the predicted behaviour, and many samples fitted to critical power laws are dirty. Sec. III.8.1: a ferromagnetic transition can become weakly first order at low temperature, with a tricritical point. Sec. III.10: disorder can give a new critical point, an infinite-disorder point or a smeared transition, and power laws with non-universal exponents |
| 4 | T. Vojta, Rare region effects at classical, quantum and non-equilibrium phase transitions, J. Phys. A 39, R143–R205 (2006); read as preprint arXiv:cond-mat/0602312 | doi:10.1088/0305-4470/39/22/R01 | full text | Abstract and Secs. 3.2 and 3.3: rare regions can destroy a sharp transition, different parts of the system order at different values of the control parameter, and the tail of a smeared transition has ordered islands in a disordered bulk; Griffiths regions with non-universal power laws away from the critical point. Sec. 7.2.2: non-Fermi-liquid behaviour in disordered heavy-fermion metals has been attributed to Griffiths effects. Sec. 7.3: disorder weakens first-order transitions, and in two or fewer dimensions weak disorder makes them continuous |
| 5 | L. Zhu, M. Garst, A. Rosch and Q. Si, Universally diverging Grüneisen parameter and the magnetocaloric effect close to quantum critical points, Phys. Rev. Lett. 91, 066404 (2003); read as preprint arXiv:cond-mat/0212335 | doi:10.1103/PhysRevLett.91.066404 | full text | Introduction and section on the divergence at QCPs: the Grüneisen ratio diverges at any QCP but stays finite near a classical transition; its temperature exponent gives the product of critical exponents; the ratio and the magnetocaloric effect proposed as a check that a QCP exists at all |
| 6 | Y. Imry and M. Wortis, Influence of quenched impurities on first-order phase transitions, Phys. Rev. B 19, 3580 (1979) | doi:10.1103/PhysRevB.19.3580 | abstract | Abstract: quenched impurities may round a first-order transition through local fluctuations of phase, and the resulting inhomogeneity can form domains much larger than the correlation length |
| 7 | M. S. S. Challa, D. P. Landau and K. Binder, Finite-size effects at temperature-driven first-order transitions, Phys. Rev. B 34, 1841 (1986) | doi:10.1103/PhysRevB.34.1841 | abstract | Abstract: in finite systems the singularities of a first-order transition are rounded and the specific-heat peak is shifted; a two-Gaussian energy distribution gives a scaling form for the specific heat and the features that distinguish first-order from second-order transitions, tested by simulation |
| 8 | A. Scheie, LongHCPulse: Long pulse heat capacity on a Quantum Design PPMS, J. Low Temp. Phys. 193, 60–73 (2018); read as preprint arXiv:1705.07129 | doi:10.1007/s10909-018-2042-9 | full text | Secs. I and II.2: the standard relaxation method assumes constant heat capacity over a pulse and is unsuited to first-order transitions; hysteresis between heating and cooling is recorded only if a pulse crosses the whole transition. Sec. III.2: thermal equilibration between sample and platform is not instantaneous. Sec. IV.3: residual hysteresis from pulses that do not cross the transition |
| 9 | S. M. Bhattacharjee and F. Seno, A measure of data collapse for scaling, J. Phys. A 34, 6375–6380 (2001); read as preprint arXiv:cond-mat/0102515 | doi:10.1088/0305-4470/34/33/302 | full text | Opening paragraphs: data collapse is a standard way to show scaling and extract exponents, but should not be judged by eye; a quantitative measure of collapse is proposed and minimised to find the exponents. Text after Eq. (4): error bars from the width of the minimum |
| 10 | S. J. Blundell, Spin-polarized muons in condensed matter physics, Contemp. Phys. 40, 175–192 (1999); read as preprint arXiv:cond-mat/0207699 | doi:10.1080/001075199181521 | full text | Sec. 4: oscillations from a static internal field vanish above the ordering temperature. Sec. 6: each signal's amplitude is proportional to the volume fraction it comes from, so a local probe can detect order in part of a sample and reveal phase separation |
