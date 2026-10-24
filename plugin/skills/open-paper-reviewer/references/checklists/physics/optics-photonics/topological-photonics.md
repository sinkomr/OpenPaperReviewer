---
id: CL-TOPOLOGICAL-PHOTONICS
name: Topological photonics
type: claim
field: physics/optics-photonics
applies_when: the paper claims topological edge, interface or corner modes in a photonic, polariton or other classical-wave structure, attributes robust or backscattering-free light transport to topology, reports a photonic topological invariant, or claims topological lasing
version: "0.1"
---

# Topological photonics

A claim in topological photonics asserts that a structured optical medium has a non-trivial bulk band topology, described by an invariant such as a Chern number, a winding number, a Zak phase (the Berry phase across the Brillouin zone) or a valley Chern number, and that modes at its edges, interfaces or corners inherit properties from it: they lie inside a bulk band gap, resist or avoid backscattering, or, in a topological laser, lase in a single edge mode that persists under disorder. Common models include the Su-Schrieffer-Heeger (SSH) chain and photonic analogues of the quantum Hall, quantum spin Hall (QSH) and valley Hall (VH) effects.

## 1. Bulk topology established for the structures on both sides

**Question.** Does the paper establish the topological invariant of the bulk on each side of the boundary, for the geometry actually built, and say how it was obtained (calculation method, measurement, or both), instead of inferring topology from the presence of a localised boundary mode?

**Why it matters.** The bulk-edge correspondence guarantees in-gap boundary modes where two bulks with different invariants meet; it does not make every localised boundary mode topological, since defect and interface modes also occur in trivial structures. Some widely used photonic lattices that host edge modes have a trivial invariant of the claimed kind and are better described by another classification, so the name given to the phase matters for what protection can be claimed.

**Resolved by.** The invariant computed for both bulks with the method named (for example Berry curvature integration, Wilson loops or symmetry indicators) and the classification stated; where possible, a measurement of a bulk quantity, such as Berry curvature reconstructed from wavepacket motion or a winding number from mean chiral displacement; a reference boundary between two bulks with the same invariant, showing that the claimed mode is absent or different there.

**Benchmark.** [1], [2]

## 2. The mode is in the measured bulk gap and at the boundary

**Question.** Is the reported mode shown, on the fabricated device, to lie inside the measured bulk band gap and to be localised at the boundary, and do the number and propagation direction of the measured edge modes match the difference in invariants?

**Why it matters.** Fabricated structures differ from their designs, so a bulk gap and an edge dispersion taken from simulation may not match the device. A localised mode that does not lie inside the bulk gap of the device itself cannot be the edge state that the invariant predicts. For chiral edge modes the number and direction in each gap are set by the Chern numbers, which gives a check that a measurement can pass or fail.

**Resolved by.** Bulk transmission or band measurements on the same sample showing the gap; the edge-mode frequency, and where possible its measured dispersion, placed inside that gap; field or emission maps showing confinement at the boundary; for chiral modes, the propagation direction measured and shown to reverse when the symmetry-breaking bias is reversed, with no edge signal when the bias is removed.

**Benchmark.** [1], [3], [6]

## 3. The protecting symmetry is present in the device

**Question.** Which symmetry does the claimed protection rely on (time-reversal breaking, chiral or sublattice symmetry, pseudospin conservation, valley separation, a crystalline symmetry), and does the paper show that the real device, its couplings and its disorder respect that symmetry?

**Why it matters.** Photons are bosons, so photonic QSH analogues are protected only while the two pseudospins stay uncoupled, and perturbations that mix them can open a gap in the edge spectrum. A valley Chern number is well defined only for certain interface orientations and small enough gaps. In SSH-type lattices chiral symmetry pins the edge mode at mid-gap, but on-site disorder and the coupling beyond nearest neighbours that is generally present in photonic lattices break it, so mid-gap pinning and degeneracies then cease to be guaranteed.

**Resolved by.** The protecting symmetry named for each claim; a model that includes long-range couplings and the measured on-site detuning, showing what survives when they are included; for pseudospin or valley systems, the interface type stated and the pseudospin- or valley-mixing rate estimated against the relevant bandwidth or coupling rate; robustness claims limited to perturbations that preserve the named symmetry.

**Benchmark.** [1], [2], [3], [4]

## 4. Robustness tested against the disorder that matters

**Question.** Is robustness tested against disorder of the kind present in fabricated devices, quantified over many disorder realisations, devices or waveguide lengths, and not only against a few designed defects or sharp bends that preserve the protecting symmetry?

**Why it matters.** Transmission through a designed bend or around a chosen defect shows protection against that perturbation only. In systems that keep time-reversal symmetry, a counter-propagating partner mode always exists, and whether random fabrication disorder backscatters into it depends on whether that disorder preserves the pseudospin. Low reflection at a few local defects says little about propagation losses from distributed disorder, which need a quantitative measure such as a backscattering mean free path or a loss per unit length.

**Resolved by.** Propagation loss or backscattering mean free path measured over several lengths or many devices, with uncertainties; transmission statistics over disorder realisations in simulation, with the disorder amplitude stated and tied to the measured fabrication tolerances; robustness stated as a quantity with its conditions (frequency, group index, disorder type), not as a qualitative label.

**Benchmark.** [4], [5], [6]

## 5. A matched trivial comparison

**Question.** Is the topological device compared with a conventional or topologically trivial counterpart made on the same platform, with equivalent disorder, at the same group index and frequency range, and measured with the same figure of merit?

**Why it matters.** Backscattering in any waveguide grows as light slows down, so a topological waveguide at low group index can look more robust than a conventional one at high group index for that reason alone. Without both the robustness measure and the group index, a claim that topological transport outperforms conventional transport is not justified. The same applies to lasers, where a trivial lattice under a different pump profile is not a fair reference.

**Resolved by.** A trivial reference fabricated on the same chip or in the same run, so that disorder statistics are equivalent; comparison at matched group index, or the full dependence on group index shown for both; the same pump geometry, coupling scheme and figure of merit for both devices; any advantage stated with the conditions under which it holds.

**Benchmark.** [3], [5], [6]

## 6. Loss channels separated

**Question.** Does the paper separate backscattering from out-of-plane radiation, absorption and coupling losses, and state whether the edge mode lies below the light line of the structure?

**Why it matters.** Topology can at most suppress backscattering into a partner mode; it does not remove radiation into free space, material absorption or loss at couplers. Edge modes above the light line radiate, which limits propagation length and quality factor whatever the topology, and transmission alone cannot tell scattering out of the plane from reflection back along the edge.

**Resolved by.** The position of the edge dispersion relative to the light line; coupling efficiency measured separately from propagation loss, for example by cut-back over several lengths; reflection or backscattered power measured, or out-of-plane scattering imaged, to attribute the loss; absorption of the materials stated where they enter the loss budget.

**Benchmark.** [4], [6]

## 7. Topological lasing

**Question.** For a claim of topological lasing, does the paper show that the lasing mode is the topological edge mode (in the gap, extended along the edge, with the expected direction or symmetry), compare it with a trivial lattice pumped in the same way, and establish that the emission is lasing?

**Why it matters.** Pumping only the edge favours edge modes in any lattice, so lasing at the boundary does not by itself show that the mode is topological. In trivial lattices disorder localises modes and lasing tends to fragment into several spectral lines, which is the behaviour the topological case should be shown to avoid. A topological gap that is narrow compared with the laser linewidth or with fabrication spread leaves the mode identification open.

**Resolved by.** Spatially and spectrally resolved emission showing a single lasing mode inside the bulk gap and extended along the boundary; for unidirectional lasers, the output direction reversed with the bias; a trivial lattice with the same gain and pump profile compared for threshold, slope efficiency, spectrum and response to disorder; the evidence for lasing itself (threshold, linewidth narrowing, coherence) given to the standard of the laser characterization card; the gap width compared with the linewidth.

**Benchmark.** [1], [3]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | T. Ozawa, H. M. Price, A. Amo, N. Goldman, M. Hafezi, L. Lu, M. C. Rechtsman, D. Schuster, J. Simon, O. Zilberberg and I. Carusotto, Topological photonics, Rev. Mod. Phys. 91, 015006 (2019); read as preprint arXiv:1802.04173 | doi:10.1103/RevModPhys.91.015006 | full text | Sec. I: bulk-edge correspondence, edge states required at the interface of materials with different invariants, at energies in the bulk gap. Sec. II.A.2: photons are bosons, so photonic QSH analogues need uncoupled pseudospins and are not robust to terms that couple them. Sec. III.A.1: the number and direction of chiral edge states in each gap are set by the Chern numbers, and backscattering is suppressed for any defect. Sec. III.B.2, Fig. 18: a non-topological edge state in the same lattice is backscattered by disorder. Sec. III.B.6: where the crystal is truncated at an edge the two pseudospins couple and a small gap opens in the edge bands. Sec. III.D: valley Chern numbers well defined only for zigzag interfaces and small gaps; VH edge states not robust to arbitrary interface disorder. Sec. VIII.B: topological lasers pumped selectively on the edge and benchmarked against a trivial device. Sec. VIII.C: measurement of Berry curvature, Chern number and winding from bulk observables |
| 2 | M. Proctor, P. Arroyo Huidobro, B. Bradlyn, M. Blanco de Paz, M. G. Vergniory, D. Bercioux and A. García-Etxarri, Robustness of topological corner modes in photonic crystals, Phys. Rev. Research 2, 042038 (2020); read as preprint arXiv:2007.10624 | doi:10.1103/PhysRevResearch.2.042038 | full text | Photonic crystal section: a widely used breathing honeycomb crystal hosting edge states has a trivial Z2 invariant and is an obstructed atomic limit, shown by symmetry analysis and Wilson loops. Following sections: long-range photonic interactions break chiral symmetry, so corner modes are no longer pinned to a fixed frequency; protection then rests on lattice symmetries, and removing a site next to a corner, which breaks them, removes a corner mode |
| 3 | Y. Ota, K. Takata, T. Ozawa, A. Amo, Z. Jia, B. Kante, M. Notomi, Y. Arakawa and S. Iwamoto, Active topological photonics, Nanophotonics 9, 547–567 (2020); read as preprint arXiv:1912.05126 | doi:10.1515/nanoph-2019-0376 | full text | Sec. 2: SSH chiral symmetry protects the edge-mode energy against hopping disorder but not against on-site disorder. Sec. 3: in 1D photonic crystals without chiral symmetry the in-gap mode is not pinned, and its robustness to disorder is unclear. Sec. 4: edge lasing imaged, absent without magnetic bias, and its direction checked by reversing the field. Sec. 5: photonic QSH lasers protected only while pseudospin is conserved; gain placed on the perimeter favours edge modes; comparison with a trivial lattice pumped the same way, where lasing fragments; topological gap comparable to the laser linewidth |
| 4 | M. Jalali Mehrabad, S. Mittal and M. Hafezi, Topological photonics: Fundamental concepts, recent developments, and future directions, Phys. Rev. A 108, 040101 (2023); read as preprint arXiv:2305.16528 | doi:10.1103/PhysRevA.108.040101 | full text | Sec. II.D: in coupled-ring lattices each pseudospin sees an opposite effective field only while clockwise and counter-clockwise modes do not mix; backscattering can be neglected only when it is slower than the hopping rate. Sec. V.A: spin-Hall photonic-crystal edge states above the light cone are radiative, which limits propagation length and quality factor; further studies are needed to confirm and quantify any protection of VH waveguides against real-world defects |
| 5 | G. Arregui, J. Gomis-Bresco, C. M. Sotomayor-Torres and P. D. Garcia, Quantifying the robustness of topological slow light, Phys. Rev. Lett. 126, 027403 (2021); read as preprint arXiv:2007.15606 | doi:10.1103/PhysRevLett.126.027403 | full text | Abstract and introduction: the backscattering mean free path and the group index must both be given when comparing topological and conventional slow-light waveguides, otherwise a claim of better performance is not justified; robustness shown with chosen local defects still needs systematic quantification against disorder. Introduction: in time-reversal-invariant QSH and VH systems a counter-propagating partner exists, and whether backscattering is reduced depends on whether the disorder preserves the pseudospin. Fig. 2: field intensities averaged over about twenty disorder configurations of stated amplitude |
| 6 | C. A. Rosiek, G. Arregui, A. Vladimirova, M. Albrechtsen, B. Vosoughi Lahijani, R. E. Christiansen and S. Stobbe, Observation of strong backscattering in valley-Hall photonic topological interface modes, Nat. Photonics 17, 386–392 (2023); read as preprint arXiv:2206.11741 | doi:10.1038/s41566-023-01189-x | full text | Introduction: deviations from the designed structure are inherent to any fabrication method; QSH interface states above the light line are intrinsically lossy. Section on disorder length scales: transmission through sharp bends gives no evidence of protection against fabrication imperfections; assessing protection needs propagation losses extracted and modelled so that out-of-plane radiation is separated from backscattering, and compared with conventional waveguides under equivalent disorder at matched group index. Section on characterisation of propagation losses and Supplementary Secs. 2.2, 2.3: conventional waveguides on the same chip as the reference, coupling loss measured with separate circuits, loss fitted over waveguides of several lengths |
