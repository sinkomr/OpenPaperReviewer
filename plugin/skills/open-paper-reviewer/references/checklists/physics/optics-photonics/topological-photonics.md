---
id: CL-TOPOLOGICAL-PHOTONICS
name: Topological photonics
type: claim
field: physics/optics-photonics
applies_when: the paper claims topological edge, interface or corner modes in a photonic, polariton or other classical-wave structure, attributes robust or backscattering-free light transport to topology, reports a photonic topological invariant, or claims topological lasing
version: "0.1"
---

# Topological photonics

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

| # | Reference | Identifier |
|---|---|---|
| 1 | T. Ozawa et al., Topological photonics, Rev. Mod. Phys. 91, 015006 (2019); read as preprint arXiv:1802.04173 | doi:10.1103/RevModPhys.91.015006 |
| 2 | M. Proctor et al., Robustness of topological corner modes in photonic crystals, Phys. Rev. Research 2, 042038 (2020); read as preprint arXiv:2007.10624 | doi:10.1103/PhysRevResearch.2.042038 |
| 3 | Y. Ota et al., Active topological photonics, Nanophotonics 9, 547 (2020); read as preprint arXiv:1912.05126 | doi:10.1515/nanoph-2019-0376 |
| 4 | M. Jalali Mehrabad et al., Topological photonics: Fundamental concepts, recent developments, and future directions, Phys. Rev. A 108, 040101 (2023); read as preprint arXiv:2305.16528 | doi:10.1103/PhysRevA.108.040101 |
| 5 | G. Arregui et al., Quantifying the robustness of topological slow light, Phys. Rev. Lett. 126, 027403 (2021); read as preprint arXiv:2007.15606 | doi:10.1103/PhysRevLett.126.027403 |
| 6 | C. A. Rosiek et al., Observation of strong backscattering in valley-Hall photonic topological interface modes, Nat. Photonics 17, 386 (2023); read as preprint arXiv:2206.11741 | doi:10.1038/s41566-023-01189-x |
