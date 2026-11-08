---
id: CL-TOPOLOGICAL-INSULATORS
name: Topological insulators
type: claim
field: physics/condensed-matter
applies_when: the paper claims that a material, film or device is a two- or three-dimensional topological insulator, or reports band inversion, topological surface or edge states, spin-momentum locking, quantum spin Hall or quantum anomalous Hall behaviour, from any measurement or calculation
version: "0.1"
---

# Topological insulators

## 1. Band inversion and the invariant

**Question.** What establishes that the bulk bands are inverted and the topological invariant is non-trivial, as opposed to a gapless-looking boundary band alone, and if calculations are used, which crystal structure and which level of theory were used, and is the conclusion stable when the method changes?

**Why it matters.** The invariant is a property of the bulk bands, fixed for example by the parities of the occupied states at the time-reversal-invariant momenta, so a boundary band seen in one experiment does not by itself fix it. Standard density-functional calculations underestimate band gaps and can predict an inversion that more accurate methods remove, and a calculation in a crystal structure other than the ground state can give a false positive; hybrid functionals can err the other way.

**Resolved by.** An argument for the invariant from the bulk band structure, such as parity eigenvalues or an observed inversion; for calculations, the structure shown to be the experimental or lowest-energy one, and the inversion checked with a method that corrects the band gap, with the size of the inverted gap compared with the spread between methods; experimental evidence of the bulk gap and its ordering, not only of the boundary state.

**Benchmark.** [1], [2], [3]

## 2. Topological or ordinary boundary states

**Question.** What shows that the claimed surface or edge state is the topological one: does it connect the bulk valence and conduction bands, cross the Fermi level an odd number of times between time-reversal-invariant momenta, and lack dispersion perpendicular to the surface, and how is it told apart from ordinary surface states, quantum-well states or a two-dimensional electron gas on the same surface?

**Why it matters.** Ordinary surface states cross the Fermi level an even number of times and can be pushed out of the gap, while a strong three-dimensional TI has an odd number of Dirac points on its surface. Downward band bending at a surface creates quantized electron-gas states that coexist with the topological state, can look similar in a single cut and also show no out-of-plane dispersion, so neither a Dirac-like band in one spectrum nor photon-energy independence alone shows topological character. In thin films the top and bottom surface states hybridize and open a gap below a material-dependent thickness.

**Resolved by.** Band maps over enough of the surface Brillouin zone to count crossings between the relevant momenta; the state followed from the bulk valence band to the bulk conduction band; photon-energy dependence showing no out-of-plane dispersion; any additional surface bands identified and their origin, such as band bending, discussed; for thin films, the thickness compared with that at which the two surfaces hybridize, and any gap at the Dirac point explained with that in mind; the same assignment confirmed on more than one surface preparation.

**Benchmark.** [1], [2], [4], [10]

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

**Question.** Where weak antilocalization, a Berry phase from quantum oscillations or two-dimensional angle dependence is offered as evidence of topological surface states, does the paper treat it as consistent with the claim rather than as proof, and test the ordinary explanations?

**Why it matters.** Each also arises without topological states: weak antilocalization from spin-orbit scattering in ordinary metals, with a prefactor that counts coupled channels, an apparent π phase from how a fan diagram is indexed, and two-dimensional angle dependence from an elongated bulk Fermi surface over a limited range of angles.

**Resolved by.** Each signature followed with gate voltage or thickness and compared with the surface carrier density from spectroscopy; the topological claim resting on more than these signatures.

**Benchmark.** [2], [6]

## 7. Quantum spin Hall edge transport

**Question.** For a claimed two-dimensional TI, does the paper show that conduction in the gap runs along the edges, that edge resistances take the values helical channels predict in several contact geometries, and that the behaviour is absent in a comparable trivial sample or regime?

**Why it matters.** A resistance near h/2e² is expected only for edges shorter than the length over which backscattering sets in, and longer edges give much larger resistances. Edge conduction also occurs in trivial systems: nonlocal measurements have found it in single InAs quantum wells, with an edge resistivity similar to that in candidate quantum spin Hall bilayers. Such an edge has a resistance that grows with its length, so one device size can give a value near h/2e² without helical transport.

**Resolved by.** Devices of several widths, showing width-independent resistance in the gap; several edge lengths, with the length dependence reported; nonlocal and multi-terminal resistances compared with Landauer-Büttiker values for helical edges, which differ from those of diffusive bulk or ordinary edge conduction; a trivial control, such as a thinner well or a gate-tuned trivial regime, showing no comparable edge conduction; the dependence on perpendicular and in-plane magnetic field reported; edge currents imaged where possible.

**Benchmark.** [7], [8], [9]

## 8. Quantum anomalous Hall quantization

**Question.** For a claimed QAH state, is the Hall resistance quantized at zero applied field with vanishing longitudinal resistance, is the quantization linked to the magnetization, and are the temperature, current and field at which it holds, and its accuracy, stated?

**Why it matters.** The QAH state requires ferromagnetic order and a magnetic gap in the surface states, and disorder in the magnetic dopants and chemical potential usually limits quantization to temperatures far below the Curie temperature and to small currents. Quantization reached only in an applied field may come from field-aligned spins or Landau levels rather than from a zero-field Chern insulator, and a large longitudinal resistance with vanishing Hall resistance is also what an ordinary insulator shows.

**Resolved by.** Hall and longitudinal resistance against field through a full hysteresis loop, with the zero-field values and their deviation from h/e² quoted; the temperature dependence compared with the magnetic ordering temperature; the current dependence and breakdown current reported; magnetization measured on the same sample or film; nonlocal measurements supporting chiral edge transport; samples that do not quantize reported, with the spread between samples.

**Benchmark.** [10]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Z. Hasan and C. L. Kane, Colloquium: Topological insulators, Rev. Mod. Phys. 82, 3045 (2010); read as arXiv:1002.3895 | doi:10.1103/RevModPhys.82.3045 |
| 2 | Y. Ando, Topological insulator materials, J. Phys. Soc. Jpn. 82, 102001 (2013); read as arXiv:1304.5693 | doi:10.7566/JPSJ.82.102001 |
| 3 | J. Vidal et al., False-positive and false-negative assignments of topological insulators in density functional theory and hybrids, Phys. Rev. B 84, 041109(R) (2011); read as arXiv:1101.3734 | doi:10.1103/PhysRevB.84.041109 |
| 4 | M. Bianchi et al., Coexistence of the topological state and a two-dimensional electron gas on the surface of Bi2Se3, Nat. Commun. 1, 128 (2010); read as arXiv:1009.2879 | doi:10.1038/ncomms1131 |
| 5 | C. Jozwiak et al., Photoelectron spin-flipping and texture manipulation in a topological insulator, Nat. Phys. 9, 293 (2013); read as arXiv:1302.5094 | doi:10.1038/nphys2572 |
| 6 | M. Brahlek et al., Transport properties of topological insulators: band bending, bulk metal-to-insulator transition, and weak anti-localization, Solid State Commun. 215, 54 (2015); read as arXiv:1408.1614 | doi:10.1016/j.ssc.2014.10.021 |
| 7 | M. König et al., The quantum spin Hall effect: theory and experiment, J. Phys. Soc. Jpn. 77, 031007 (2008); read as arXiv:0801.0901 | doi:10.1143/JPSJ.77.031007 |
| 8 | A. Roth et al., Nonlocal transport in the quantum spin Hall state, Science 325, 294 (2009); read as arXiv:0905.0365 | doi:10.1126/science.1174736 |
| 9 | S. Mueller et al., Edge transport in InAs and InAs/GaSb quantum wells, Phys. Rev. B 96, 075406 (2017); read as arXiv:1706.00320 | doi:10.1103/PhysRevB.96.075406 |
| 10 | C.-Z. Chang et al., Colloquium: Quantum anomalous Hall effect, Rev. Mod. Phys. 95, 011002 (2023); read as arXiv:2202.13902 | doi:10.1103/RevModPhys.95.011002 |
