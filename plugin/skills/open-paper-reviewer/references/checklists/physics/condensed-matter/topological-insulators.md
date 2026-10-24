---
id: CL-TOPOLOGICAL-INSULATORS
name: Topological insulators
type: claim
field: physics/condensed-matter
applies_when: the paper claims that a material, film or device is a two- or three-dimensional topological insulator, or reports band inversion, topological surface or edge states, spin-momentum locking, quantum spin Hall or quantum anomalous Hall behaviour, from any measurement or calculation
version: "0.1"
---

# Topological insulators

A topological insulator (TI) claim asserts that a material has an insulating bulk with inverted band ordering and a non-trivial topological invariant, and therefore protected metallic states on its boundary: spin-polarized Dirac surface states in three dimensions, helical edge channels in the quantum spin Hall (QSH) state of a two-dimensional TI, or chiral edge channels in the quantum anomalous Hall (QAH) state of a magnetic TI. The claim joins a statement about the bulk bands to a statement about the boundary, and both must hold for the samples actually measured, whether the evidence comes from angle-resolved photoemission spectroscopy (ARPES), transport, scanning probes or electronic-structure calculations.

## 1. Band inversion and the invariant

**Question.** What establishes that the bulk bands are inverted and the topological invariant is non-trivial, as opposed to a gapless-looking boundary band alone, and if calculations are used, which crystal structure and which level of theory were used, and is the conclusion stable when the method changes?

**Why it matters.** The invariant is a property of the bulk bands, fixed for example by the parities of the occupied states at the time-reversal-invariant momenta, so a boundary band seen in one experiment does not by itself fix it. Standard density-functional calculations underestimate band gaps and can predict an inversion that more accurate methods remove, and a calculation in a crystal structure other than the ground state can give a false positive; hybrid functionals can err the other way.

**Resolved by.** An argument for the invariant from the bulk band structure, such as parity eigenvalues or an observed inversion; for calculations, the structure shown to be the experimental or lowest-energy one, and the inversion checked with a method that corrects the band gap, with the size of the inverted gap compared with the spread between methods; experimental evidence of the bulk gap and its ordering, not only of the boundary state.

**Benchmark.** [1], [2], [3]

## 2. Topological or ordinary boundary states

**Question.** What shows that the claimed surface or edge state is the topological one: does it connect the bulk valence and conduction bands, cross the Fermi level an odd number of times between time-reversal-invariant momenta, and lack dispersion perpendicular to the surface, and how is it told apart from ordinary surface states, quantum-well states or a two-dimensional electron gas on the same surface?

**Why it matters.** Ordinary surface states cross the Fermi level an even number of times and can be pushed out of the gap, while a strong three-dimensional TI has an odd number of Dirac points on its surface. Downward band bending at a surface creates quantized electron-gas states that coexist with the topological state, can look similar in a single cut and also show no out-of-plane dispersion, so neither a Dirac-like band in one spectrum nor photon-energy independence alone shows topological character. In thin films the top and bottom surface states hybridize and open a gap below a material-dependent thickness.

**Resolved by.** Band maps over enough of the surface Brillouin zone to count crossings between the relevant momenta; the state followed from the bulk valence band to the bulk conduction band; photon-energy dependence showing no out-of-plane dispersion; any additional surface bands identified and their origin, such as band bending, discussed; for thin films, the thickness compared with that at which the two surfaces hybridize, and any gap at the Dirac point explained with that in mind; the same assignment confirmed on more than one surface preparation.

**Benchmark.** [1], [2], [4], [11]

## 3. Spin texture

**Question.** If spin-momentum locking is claimed, was the spin measured directly and around the whole constant-energy contour, and does the interpretation account for the dependence of the measured photoelectron spin on the light polarization and geometry?

**Why it matters.** A single non-degenerate, helically spin-polarized Dirac cone is part of what distinguishes a topological surface state from a spin-degenerate trivial band, so a spin texture inferred only from a band shape or from theory leaves the claim open. Rashba-split trivial surface states are also spin-polarized, so spin polarization supports the claim only together with the count of crossings in item 2. In strongly spin-orbit-coupled surfaces the spin of the emitted photoelectron can differ from that of the initial state and can be changed by the light polarization, so a measured spin direction or polarization magnitude is not automatically the intrinsic one.

**Resolved by.** Spin-resolved data for opposite momenta and several points around the contour, showing the reversal expected for a helical texture; the light polarization and experimental geometry stated, with results compared for more than one polarization; claims about the size or out-of-plane component of the spin polarization made only with these effects taken into account.

**Benchmark.** [1], [2], [5]

## 4. Bulk conduction and Fermi level in the measured samples

**Question.** Where is the Fermi level relative to the bulk bands in the samples on which each claim rests, what is the bulk carrier density, and what fraction of the measured conduction or signal is shown to come from the boundary states?

**Why it matters.** Many TI materials are degenerately doped by native defects, so bulk carriers dominate transport, and even the most insulating ones are often weakly insulating bad metals rather than true insulators. A surface contribution of a few per cent can be present yet hidden under bulk conduction, and the Fermi level seen by surface-sensitive spectroscopy on a fresh surface need not be the one in a device.

**Resolved by.** The bulk carrier density and type, and the temperature dependence of the bulk resistivity; the Fermi level placed relative to the bulk band edges for the same kind of sample used in the main measurements; the surface share of the conductance quantified, for example by thickness or size dependence, gating through the Dirac point, or a multi-carrier analysis constrained by independent data.

**Benchmark.** [2], [6]

## 5. Band bending, ageing and surface environment

**Question.** Does the paper report how the surface Fermi level and band bending depend on the time since cleaving or growth, the atmosphere, capping, adsorbates and device processing, and does it exclude a conducting accumulation or inversion layer of ordinary carriers as the source of the surface signal?

**Why it matters.** Surface doping shifts the bands within hours of cleaving, even in vacuum, and the resulting band bending can bind a two-dimensional electron gas next to the topological state. Ordinary accumulation or inversion layers also give surface-dominated conduction and quantum oscillations, so surface-dominated transport alone does not identify topological surface states.

**Resolved by.** Spectra or transport recorded as a function of time after surface preparation, or under the conditions of the device; capping, environment and processing history stated for each sample; evidence that the carriers responsible for the surface signal are the Dirac carriers, such as a density, dispersion or Berry phase consistent with the topological band and not with an ordinary electron gas.

**Benchmark.** [2], [4], [6]

## 6. Transport signatures that are not specific to topology

**Question.** Where transport is used as evidence of topological surface states, does the paper treat weak antilocalization, a Berry phase extracted from quantum oscillations, and two-dimensional angle dependence as consistent with the claim rather than as proof, and is each analysis done in a way that tests the alternatives?

**Why it matters.** Weak antilocalization arises from strong spin-orbit scattering in ordinary metals as well, and its prefactor depends on how many channels are coupled. The phase from a Landau-level fan diagram depends on whether minima of resistivity or conductivity are indexed, and dispersion curvature and Zeeman coupling move the intercept away from the ideal Dirac value, so a straight-line fit can give an apparent π or non-π phase. An elongated bulk Fermi surface can mimic two-dimensional angle dependence over a limited range of angles.

**Resolved by.** The weak-antilocalization prefactor and coherence length interpreted together with gate or thickness dependence, not as a count of topological channels on its own; fan diagrams indexed on conductivity minima unless the Hall conductivity dominates, with the frequency fixed from the Fourier transform and curvature and Zeeman terms considered; oscillation frequencies followed over a wide range of field angles and compared with the surface carrier density from spectroscopy.

**Benchmark.** [2], [6], [7]

## 7. Quantum spin Hall edge transport

**Question.** For a claimed two-dimensional TI, does the paper show that conduction in the gap runs along the edges, that edge resistances take the values helical channels predict in several contact geometries, and that the behaviour is absent in a comparable trivial sample or regime?

**Why it matters.** A resistance near h/2e² is expected only for edges shorter than the length over which backscattering sets in, and longer edges give much larger resistances. Edge conduction also occurs in trivial systems: nonlocal measurements have found it in single InAs quantum wells, with an edge resistivity similar to that in candidate quantum spin Hall bilayers. Such an edge has a resistance that grows with its length, so one device size can give a value near h/2e² without helical transport.

**Resolved by.** Devices of several widths, showing width-independent resistance in the gap; several edge lengths, with the length dependence reported; nonlocal and multi-terminal resistances compared with Landauer-Büttiker values for helical edges, which differ from those of diffusive bulk or ordinary edge conduction; a trivial control, such as a thinner well or a gate-tuned trivial regime, showing no comparable edge conduction; the dependence on perpendicular and in-plane magnetic field reported; edge currents imaged where possible.

**Benchmark.** [8], [9], [10]

## 8. Quantum anomalous Hall quantization

**Question.** For a claimed QAH state, is the Hall resistance quantized at zero applied field with vanishing longitudinal resistance, is the quantization linked to the magnetization, and are the temperature, current and field at which it holds, and its accuracy, stated?

**Why it matters.** The QAH state requires ferromagnetic order and a magnetic gap in the surface states, and disorder in the magnetic dopants and chemical potential usually limits quantization to temperatures far below the Curie temperature and to small currents. Quantization reached only in an applied field may come from field-aligned spins or Landau levels rather than from a zero-field Chern insulator, and a large longitudinal resistance with vanishing Hall resistance is also what an ordinary insulator shows.

**Resolved by.** Hall and longitudinal resistance against field through a full hysteresis loop, with the zero-field values and their deviation from h/e² quoted; the temperature dependence compared with the magnetic ordering temperature; the current dependence and breakdown current reported; magnetization measured on the same sample or film; nonlocal measurements supporting chiral edge transport; samples that do not quantize reported, with the spread between samples.

**Benchmark.** [11]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Z. Hasan and C. L. Kane, Colloquium: Topological insulators, Rev. Mod. Phys. 82, 3045–3067 (2010); read as arXiv:1002.3895 | doi:10.1103/RevModPhys.82.3045 | full text | Sec. II.C and Eq. 12: the Z2 invariant follows from parity eigenvalues of occupied bands at time-reversal-invariant momenta; Sec. II.C with Fig. 3: surface bands crossing the Fermi level an even number of times can be pushed out of the gap, an odd number cannot; Sec. IV.A: a strong TI surface encloses an odd number of Dirac points; Sec. IV.B: photon-energy-modulated photoemission isolates surface states because they do not disperse perpendicular to the surface, and spin-resolved photoemission mapped the spin texture as evidence for the π Berry phase |
| 2 | Y. Ando, Topological insulator materials, J. Phys. Soc. Jpn. 82, 102001 (2013); read as arXiv:1304.5693 | doi:10.7566/JPSJ.82.102001 | full text | Secs. 3.7 to 3.9: a non-trivial invariant forces surface states to cross any Fermi energy in the gap; parity eigenvalues and band inversion at an odd number of momenta. Sec. 5: routes to confirming topological character, including spin-resolved photoemission of a non-degenerate helical Dirac cone and size-dependent conductance; trivial accumulation or inversion layers can also give surface-dominated transport. Sec. 4.2: tetradymite compounds are degenerately doped by native defects so bulk carriers dominate; non-topological Rashba-split surface states are also spin-non-degenerate and add Fermi-level crossings beside the topological one. Sec. 8.3: 2D angle dependence should be checked over a wide angle range, fan diagrams should be indexed on conductivity minima, and the slope fixed from the frequency. Sec. 8.4: a surface share of about 6% of conductance. Sec. 8.5: weak antilocalization also arises from spin-orbit scattering and is not proof of Dirac fermions |
| 3 | J. Vidal, X. Zhang, L. Yu, J.-W. Luo and A. Zunger, False-positive and false-negative assignments of topological insulators in density functional theory and hybrids, Phys. Rev. B 84, 041109(R) (2011); read as arXiv:1101.3734 | doi:10.1103/PhysRevB.84.041109 | full text | Results and Table I: density-functional calculations predict band inversion in several compounds that self-consistent GW finds to be normal insulators; false positives also arise from assuming a crystal structure other than the ground state. Discussion and Table II: a standard hybrid functional gives false negatives in some cases. Conclusion: correct structure and an accurate Hamiltonian are both needed |
| 4 | M. Bianchi, D. Guan, S. Bao, J. Mi, B. B. Iversen, P. D. C. King and P. Hofmann, Coexistence of the topological state and a two-dimensional electron gas on the surface of Bi2Se3, Nat. Commun. 1, 128 (2010); read as arXiv:1009.2879 | doi:10.1038/ncomms1131 | full text | Fig. 1 and text: the band positions shift over a few hours after cleaving in vacuum, attributed to defect-induced downward band bending, and a two-dimensional electron gas appears beside the Dirac cone. Fig. 2 and text: photon-energy-dependent measurements show that neither the topological state nor the electron gas disperses with kz. Fig. 3: model calculations of band-bending-induced quantized states coexisting with the topological state. Discussion: adsorbates could modulate the band bending |
| 5 | C. Jozwiak, C.-H. Park, K. Gotlieb, C. Hwang, D.-H. Lee, S. G. Louie, J. D. Denlinger, C. R. Rotundu, R. J. Birgeneau, Z. Hussain and A. Lanzara, Photoelectron spin-flipping and texture manipulation in a topological insulator, Nat. Phys. 9, 293–298 (2013); read as arXiv:1302.5094 | doi:10.1038/nphys2572 | abstract | Abstract: in spin-resolved photoemission of a topological surface state, the photoelectron spin polarization can be controlled in three dimensions by the light polarization, and the photoelectron spin can differ completely from the initial-state spin |
| 6 | M. Brahlek, N. Koirala, N. Bansal and S. Oh, Transport properties of topological insulators: band bending, bulk metal-to-insulator transition, and weak anti-localization, Solid State Commun. 215, 54–62 (2015); read as arXiv:1408.1614 | doi:10.1016/j.ssc.2014.10.021 | full text | Abstract and Sec. 2: by the Mott and Ioffe-Regel criteria even the best TI materials are weakly insulating bad metals rather than true insulators. Sec. 3: downward band bending gives a surface accumulation region and a non-topological two-dimensional electron gas, and the direction of band bending affects whether surface Shubnikov-de Haas oscillations are seen. Sec. 4: the weak-antilocalization prefactor counts effective channels, and surfaces coupled through a conducting bulk or by tunnelling act as one channel |
| 7 | A. A. Taskin and Y. Ando, Berry phase of nonideal Dirac fermions in topological insulators, Phys. Rev. B 84, 035301 (2011); read as arXiv:1103.3096 | doi:10.1103/PhysRevB.84.035301 | full text | Secs. II, III and V with Figs. 2 and 3: a quadratic term in the surface dispersion and Zeeman coupling shift the Landau-level fan diagram from the ideal Dirac line, most strongly at low Landau index. Sec. VI: a straight-line fan analysis should not be used to determine the Berry phase; fits with fixed frequency and band parameters are used instead |
| 8 | M. König, H. Buhmann, L. W. Molenkamp, T. Hughes, C.-X. Liu, X.-L. Qi and S.-C. Zhang, The quantum spin Hall effect: theory and experiment, J. Phys. Soc. Jpn. 77, 031007 (2008); read as arXiv:0801.0901 | doi:10.1143/JPSJ.77.031007 | full text | Sec. 7 with Fig. 14: 1 μm devices show resistance near h/2e² while 20 μm devices are far higher, attributed to inelastic scattering; devices of different width have the same resistance in the gap, indicating edge transport. Sec. 7 with Fig. 13: wells thinner than the critical thickness are trivial and do not conduct in the gap. Sec. 8 with Fig. 15: perpendicular and in-plane magnetic field suppress the edge conductance at very different rates |
| 9 | A. Roth, C. Brüne, H. Buhmann, L. W. Molenkamp, J. Maciejko, X.-L. Qi and S.-C. Zhang, Nonlocal transport in the quantum spin Hall state, Science 325, 294–297 (2009); read as arXiv:0905.0365 | doi:10.1126/science.1174736 | full text | Discussion of Figs. 1, 3 and 4: Landauer-Büttiker predictions for helical edges give specific local and nonlocal resistances (for example h/4e² in an H-bar) that differ from diffusive estimates and from quantum Hall behaviour, and the measured values match them |
| 10 | S. Mueller, C. Mittag, T. Tschirky, C. Charpentier, W. Wegscheider, K. Ensslin and T. Ihn, Edge transport in InAs and InAs/GaSb quantum wells, Phys. Rev. B 96, 075406 (2017); read as arXiv:1706.00320 | doi:10.1103/PhysRevB.96.075406 | abstract | Abstract: nonlocal measurements beyond bulk pinch-off show edge conduction in single InAs quantum wells, with an edge resistivity of 1–2 kΩ/µm, of the same order as in InAs/GaSb double quantum wells; finger-gate samples probe how the edge resistance depends on length |
| 11 | C.-Z. Chang, C.-X. Liu and A. H. MacDonald, Colloquium: Quantum anomalous Hall effect, Rev. Mod. Phys. 95, 011002 (2023); read as arXiv:2202.13902 | doi:10.1103/RevModPhys.95.011002 | full text | Sec. III.A: in thin films the top and bottom surface states hybridize and open a gap that becomes unobservably small only above a material-dependent thickness of a few quintuple layers. Sec. III.B.1: zero-field Hall resistance at h/e² with a longitudinal dip, hysteresis with magnetization, and a critical temperature an order of magnitude below the Curie temperature owing to fluctuations of chemical potential and exchange gap. Sec. III.C.1: residual bulk and non-chiral channels give non-zero longitudinal resistance with near-quantized Hall resistance; nonlocal tests of chiral edges. Sec. III.C.4: breakdown at tens to hundreds of nanoamperes. Sec. IV.C: in some devices accurate quantization needs a field to align spins, field-induced states can relate to Landau levels, and a large longitudinal with vanishing Hall resistance is also what a trivial insulator shows. Sec. VI.B.2: precision measurements at parts-per-million level |
