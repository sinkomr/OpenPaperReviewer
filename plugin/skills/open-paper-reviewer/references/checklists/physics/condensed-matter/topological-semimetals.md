---
id: CL-TOPOLOGICAL-SEMIMETALS
name: Topological semimetals
type: claim
field: physics/condensed-matter
applies_when: the paper claims a Weyl, Dirac or nodal-line semimetal, or reports Fermi arcs, a chiral anomaly or negative longitudinal magnetoresistance, a non-trivial Berry phase from quantum oscillations, or an anomalous or nonlinear Hall effect attributed to band topology
version: "0.1"
---

# Topological semimetals

A claim of a topological semimetal asserts that bulk bands cross at isolated points (Weyl or Dirac nodes) or along lines (nodal lines) close to the Fermi level, protected by symmetry or topology, and that these crossings produce observable signatures: surface Fermi arcs, the chiral anomaly (charge pumped between nodes of opposite chirality by parallel electric and magnetic fields, seen as negative longitudinal magnetoresistance), a Berry phase of π in quantum oscillations, and anomalous or nonlinear Hall effects from Berry curvature. A careful demonstration ties each signature to the claimed nodes in the measured samples and excludes ordinary band, surface and transport effects that produce the same signal.

## 1. Nodes at the Fermi level and what protects them

**Question.** Does the paper state which symmetry protects each claimed crossing, including the effect of spin-orbit coupling, and show where the nodes lie relative to the Fermi level of the samples actually measured, together with any trivial pockets that also cross the Fermi level?

**Why it matters.** Weyl signatures appear only in a narrow energy window: once the Fermi level is far from the nodes, Fermi surfaces merge and can enclose nodes of opposite chirality with no net Berry flux, and trivial pockets can carry much of the response. Line nodes protected only by inversion and time reversal do not survive spin-orbit coupling unless a further crystal symmetry, such as a glide or screw, protects them. Signatures attributed to the nodes, such as the chiral anomaly, are expected to weaken as the Fermi level moves away from them.

**Resolved by.** The protecting symmetry and the role of spin-orbit coupling stated; node energies relative to the Fermi level given from calculation and from measurement on the same samples, for example by spectroscopy, Hall density or oscillation frequencies; the Fermi surfaces listed, with those that enclose a single node distinguished from trivial ones; where possible, the signature shown to change as the Fermi level is moved towards or away from the nodes across several samples.

**Benchmark.** [1], [2]

## 2. Bulk nodes and Fermi arcs

**Question.** Where spectroscopy supports the claim, does the paper locate the bulk crossing in all three momentum directions, and does it show that claimed Fermi arcs are open contours ending at the projected nodes, or give a non-zero chirality count around a closed loop, instead of closed trivial surface states?

**Why it matters.** Surface-sensitive spectroscopy sees bulk and surface states together, so a bulk node must also be located in out-of-plane momentum. Trivial surface states can resemble arcs, the way arcs connect the projected nodes depends on the surface termination, and closely spaced nodes can lie below the momentum resolution. Real arcs are more complex than simple models, so their identification rests on a careful comparison with calculations.

**Resolved by.** Bulk dispersions mapped through the node as a function of out-of-plane momentum, for example by varying photon energy; constant-energy contours that stay open and end at the projected node positions over a range of energies; the crossings and their velocity signs counted along a closed loop, giving a non-zero net chirality; the momentum resolution compared with the node separation; the surface termination identified and the arcs compared with surface calculations for that termination.

**Benchmark.** [1], [3]

## 3. Current distribution in longitudinal magnetoresistance

**Question.** When negative longitudinal magnetoresistance is offered as evidence of the chiral anomaly, does the paper show that the current flows uniformly between the voltage contacts over the field range of the effect?

**Why it matters.** In high-mobility semimetals a field along the current focuses the current into a narrow jet, and voltage contacts away from the jet read a falling voltage that mimics negative magnetoresistance. Such signals can vanish when the field is turned by a few degrees or when the contacts span the sample. Whether an intrinsic signal can be seen depends on whether mobility times field becomes large before the quantum limit is reached.

**Resolved by.** Voltages measured at several positions, on the line joining the current contacts and at the edge, falling together with field; contacts that span the sample cross-section, with the sample shape and contact layout stated; the field at which mobility times field reaches about five compared with the field range of the claimed effect.

**Benchmark.** [1], [2]

## 4. Other explanations of negative magnetoresistance

**Question.** Beyond current jetting, does the paper exclude other origins of negative longitudinal magnetoresistance, and does the effect show the dependences expected of the chiral anomaly on field, on the angle between field and current, and on the Fermi level relative to the nodes?

**Why it matters.** In the quantum limit a generic three-dimensional metal can show longitudinal magnetoresistance of either sign, depending on band structure and impurity type, so a negative sign alone does not identify Weyl nodes. Spatial fluctuations of mobility, spin-orbit-related magnetoresistance in magnetic compounds and weak antilocalization are other proposed origins. A sharp angular dependence is not decisive, because current jetting also produces one.

**Resolved by.** The magnetoconductance compared with the quadratic low-field form and its dependence on the angle between field and current; magnetic order and magnetisation considered for magnetic compounds; any weak-antilocalization term separated with its parameters stated; the effect shown to grow as the Fermi level approaches the nodes across samples; support from a probe that does not rely on a uniform current between contacts.

**Benchmark.** [1], [2], [4]

## 5. Berry phase from quantum oscillations

**Question.** Where a Berry phase of π is offered as evidence of topology, is the phase determined well enough to tell π from zero once the three-dimensional correction, Zeeman coupling, departures from a linear dispersion and the choice of resistivity extrema are taken into account, and is it assigned to a pocket that encloses a node?

**Why it matters.** The measured phase offset combines the Berry phase with a correction of plus or minus one eighth for a three-dimensional Fermi surface, and Zeeman coupling and band curvature shift the intercept of a fan diagram, most strongly at low Landau index, so a straight-line fit can mislead. In materials with several pockets a phase says nothing about the nodes unless its pocket is identified, and a pocket enclosing two nodes of opposite chirality carries no net Berry flux.

**Resolved by.** The phase quoted with its uncertainty and with each correction stated; an analysis that includes Zeeman coupling and band curvature, or a fit to the oscillation waveform, instead of a straight-line intercept alone; the pocket identified from its frequency and angle dependence and matched to calculation; the topological claim supported by more than the phase.

**Benchmark.** [1], [5]

## 6. Anomalous Hall effect from Berry curvature

**Question.** When an anomalous Hall effect is attributed to Weyl nodes or Berry curvature, how is it separated from the ordinary Hall signal, and is the intrinsic mechanism distinguished from skew scattering by the scaling of the anomalous Hall conductivity with longitudinal conductivity and by comparison with the value calculated for the band structure?

**Why it matters.** The ordinary Hall signal of a high-mobility semimetal can be large and non-linear in field, and can hide or imitate an anomalous term. Skew scattering grows with conductivity and dominates in very clean samples, while side-jump scattering has the same scaling as the intrinsic term and cannot be separated from it by dc transport alone. In a Weyl semimetal the intrinsic value is set by the node separation and changes little with Fermi level until Fermi surfaces merge, which gives a quantitative test.

**Resolved by.** Hall resistivity against field shown together with magnetisation on the same sample; the subtraction of the ordinary term described; the anomalous Hall conductivity plotted against longitudinal conductivity across temperatures or samples; its size compared with the calculated Berry-curvature value at the measured Fermi level, with a possible side-jump contribution acknowledged.

**Benchmark.** [1], [6]

## 7. Nonlinear Hall effect

**Question.** For a nonlinear Hall effect attributed to a Berry curvature dipole, does the paper show that the transverse second-harmonic voltage is quadratic in current and independent of drive frequency, follows the dependence on current direction allowed by the crystal symmetry, and is separated from disorder-induced contributions?

**Why it matters.** The effect requires broken inversion symmetry, and the point group fixes which response components can be non-zero and how the signal varies with current direction relative to the crystal axes. Side-jump and skew scattering also produce a nonlinear Hall response, disorder matters more here than in the linear Hall effect, and measured signals have been found to contain contributions beyond the Berry curvature dipole.

**Resolved by.** Second-harmonic transverse voltage plotted against current, showing a quadratic dependence at more than one frequency; the dependence on current direction measured, for example in a device with several current orientations, and compared with the allowed symmetry; a scaling analysis against longitudinal conductivity or temperature that separates the contributions; comparison with a calculated Berry curvature dipole.

**Benchmark.** [7]

## 8. Large transverse magnetoresistance

**Question.** Where a very large, non-saturating or linear transverse magnetoresistance is offered in support of topological bands, does the paper weigh it against ordinary semimetal explanations such as electron-hole compensation, and rest the topological claim on measurements specific to the nodes?

**Why it matters.** The classical two-carrier magnetoresistance of a compensated semimetal does not saturate, several mechanisms give a strong transverse magnetoresistance in any low-density material, and spatial fluctuations of mobility can make it linear in field. Such magnetoresistance is therefore common to semimetals with and without topological nodes.

**Resolved by.** Densities and mobilities of each carrier type from a joint fit of Hall and longitudinal data, with the degree of compensation stated; the transverse magnetoresistance treated as characterisation of the samples, not as evidence of nodes; the topological claim supported by signatures tied to the nodes.

**Benchmark.** [1]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | N. P. Armitage, E. J. Mele and A. Vishwanath, Weyl and Dirac semimetals in three-dimensional solids, Rev. Mod. Phys. 90, 015001 (2018); read as preprint arXiv:1705.01111 | doi:10.1103/RevModPhys.90.015001 | full text | Sec. II.2.1: Fermi surfaces merge at a Lifshitz energy beyond which the phase is no longer a Weyl metal. Sec. II.3.2: anomaly magnetoconductivity quadratic in field and largest with field along current. Sec. II.3.3: intrinsic anomalous Hall conductivity set by node separation, nearly unchanged with chemical potential until Fermi surfaces merge. Sec. IV.1.1: Weyl physics confined to a narrow energy range; a Fermi surface enclosing a pair of nodes has zero net Chern number; ARPES may lack the resolution to settle Fermi-surface chirality. Sec. V.1: bulk nodes located by tuning photon energy; chirality count of surface-state velocities around a loop; arcs of highly non-trivial shape, needing careful comparison with calculations; how arcs connect the projected nodes depends on the termination; some arc-like features trivial; pockets enclosing two nodes give zero net chirality. Sec. V.3.1: phase offset includes a plus or minus one-eighth term for 3D Fermi surfaces, band curvature and choice of extrema matter; a trivial pocket alongside non-trivial ones. Sec. V.3.2: total Berry flux through a Fermi surface can be zero; current jetting in high-mobility semimetals mimics negative magnetoresistance, which vanished on small rotations or with contacts spanning the sample; mobility fluctuations, generic 3D metals, weak antilocalization and spin-orbit-related directional magnetoresistance in a magnetic compound as other origins; non-contact and homogeneous-current probes recommended; several mechanisms give strong transverse magnetoresistance, all enhanced at low carrier density, and large transverse magnetoresistance in compensated semimetals, and classical transverse magnetoresistance that does not saturate under exact compensation; spatial mobility fluctuations predicted to give linear magnetoresistance. Sec. VI.1: with spin-orbit coupling, line nodes need a glide or screw symmetry |
| 2 | N. P. Ong and S. Liang, Experimental signatures of the chiral anomaly in Dirac–Weyl semimetals, Nat. Rev. Phys. 3, 394–404 (2021); read as preprint arXiv:2010.08564, which carries a different title | doi:10.1038/s42254-021-00310-9 | full text | Sec. IV: current jetting in high-mobility samples; rule of thumb comparing the field where mobility times field is about 5 with the field for the lowest Landau level; spine and edge voltages compared to separate artefacts from intrinsic magnetoresistance. Sec. V.2: negative magnetoresistance largest with the Fermi level near the node and suppressed as it moves away, across many samples. Sec. V.3: negative magnetoresistance vanishing for a tilt of one to two degrees in one material |
| 3 | I. Belopolski et al., Criteria for directly detecting topological Fermi arcs in Weyl semimetals, Phys. Rev. Lett. 116, 066802 (2016); read as preprint arXiv:1509.07465, which carries a different title | doi:10.1103/PhysRevLett.116.066802 | full text | Introduction and text with Fig. 2 (the preprint has no numbered sections): an arc appears as an open constant-energy contour; net chirality of edge modes along a closed loop as a criterion; closed hole-like pockets argued to be trivial surface states. Text with the calculations and Fig. 4: calculated node separations below the ARPES linewidth, so the nodes cannot be resolved; Fermi level position prevents a loop count; a criterion based on how contours evolve with binding energy |
| 4 | P. Goswami, J. H. Pixley and S. Das Sarma, Axial anomaly and longitudinal magnetoresistance of a generic three dimensional metal, Phys. Rev. B 92, 075205 (2015) | doi:10.1103/PhysRevB.92.075205 | abstract | Abstract: the axial anomaly is generic to 3D metals; it does not by itself guarantee negative longitudinal magnetoresistance; in the quantum limit ionic impurities give a large positive magnetoconductivity, so negative magnetoresistance, in any 3D metal, and short-range impurities give either sign depending on band structure |
| 5 | A. A. Taskin and Y. Ando, Berry phase of nonideal Dirac fermions in topological insulators, Phys. Rev. B 84, 035301 (2011); read as preprint arXiv:1103.3096 | doi:10.1103/PhysRevB.84.035301 | full text | Sec. V: a finite effective mass shifts and curves the fan-diagram lines; Zeeman coupling grows with field and distorts the diagram near the quantum limit. Sec. VI: a simple straight-line fan-diagram analysis should not be used to determine the Berry phase |
| 6 | N. Nagaosa, J. Sinova, S. Onoda, A. H. MacDonald and N. P. Ong, Anomalous Hall effect, Rev. Mod. Phys. 82, 1539–1592 (2010); read as preprint arXiv:0904.4154 | doi:10.1103/RevModPhys.82.1539 | full text | Sec. I.2: intrinsic term independent of scattering, skew scattering proportional to the transport lifetime, side jump with the same scaling as the intrinsic term and not separable by dc measurement. Secs. II.1.1 and II.1.2: ordinary term proportional to field and anomalous term following magnetisation; scaling regimes of anomalous Hall conductivity against longitudinal conductivity; in clean samples the ordinary term grows faster, becomes non-linear in field and can hide the anomalous term |
| 7 | Z. Z. Du, H.-Z. Lu and X. C. Xie, Nonlinear Hall effects, Nat. Rev. Phys. 3, 744–752 (2021); read as preprint arXiv:2105.10940 | doi:10.1038/s42254-021-00359-6 | full text | Sec. I: second-harmonic transverse voltage measured by lock-in; quadratic dependence on current independent of drive frequency; dependence on current direction relative to crystal axes. Secs. II.1 and II.4: broken inversion symmetry required; point group fixes allowed components. Secs. II.2 and II.3: side-jump and skew-scattering contributions, disorder more important than in the linear case; scaling with longitudinal conductivity and temperature used to separate contributions; experiments indicating contributions beyond the Berry curvature dipole |
