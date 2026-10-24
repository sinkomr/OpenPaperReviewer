---
id: T-FIRST-PRINCIPLES-EVIDENCE
name: First-principles calculations as supporting evidence
type: technique
field: physics/methods
applies_when: the paper uses density functional theory or other first-principles calculations, such as DFT+U, hybrid functionals or GW, to support an experimental interpretation of a structure, band structure, band gap, magnetic order, topology, defect level or spectral assignment
version: "0.1"
---

# First-principles calculations as supporting evidence

Density functional theory (DFT) and related first-principles methods, including DFT with a Hubbard correction (DFT+U), hybrid functionals and many-body GW calculations, are used alongside experiments to claim that a measured structure, band structure, band gap, magnetic order, topological character, defect level or spectral feature has a particular origin. Each result depends on an approximate exchange-correlation functional, on numerical settings and on a structural and magnetic model chosen by the authors.

## 1. Functional and its known biases

**Question.** Does the paper name the exchange-correlation functional, any dispersion correction and any fitted parameters, and justify the choice for this class of material and for the quantity that carries the claim?

**Why it matters.** The standard local and semi-local functionals have known, systematic errors: they over-delocalise electrons, underestimate band gaps, describe localised d and f electrons poorly and, without a correction, leave out van der Waals binding. Functionals fitted to one class of system can be much worse far from it, and accuracy often rests on cancellation of errors that varies from system to system.

**Resolved by.** The functional, version and any correction stated; a reason for the choice that refers to its known performance for comparable materials and properties; for layered or weakly bound materials, a dispersion treatment and its effect on the structure shown; for a claim that depends on a delicate balance, the key result repeated with a second, different functional.

**Benchmark.** [1], [2], [10]

## 2. Numerical convergence and pseudopotentials

**Question.** Does the paper give the basis set or plane-wave cut-off, the k-point mesh, the smearing, the pseudopotentials or all-electron method with their library and version, and the supercell size, and show that the quantity behind the claim is converged with respect to each?

**Why it matters.** Metals need much denser k-point meshes than insulators, and smearing can change an energy curve enough to change which structure is lowest. Pseudopotential sets disagree with each other far more than all-electron codes do, and those for rare-earth and heavy elements are less tested. Defect and surface calculations in finite supercells carry spurious interactions with their periodic images, which larger cells reduce.

**Resolved by.** A table of numerical settings with the code, version and exact pseudopotential files; convergence tests for the cut-off, k-point mesh and smearing applied to the property that matters (an energy difference, a gap or a band crossing), not only to the total energy; for defects and slabs, results for more than one supercell or slab thickness and the finite-size correction scheme named.

**Benchmark.** [2], [3], [4]

## 3. Structural model and its relaxation

**Question.** Does the structural model used in the calculation correspond to the sample measured (phase, stoichiometry, ordering, defects, surface termination), is it stated whether lattice parameters and atomic positions were relaxed or taken from experiment, and is the model shown to be stable against plausible alternatives?

**Why it matters.** A calculation on an assumed structure that is not the ground state, or that would decompose, can produce properties the real material does not have. Relaxed lattice parameters depend on the functional and its dispersion correction, and the electronic structure of a layered or narrow-gap material can change with small changes in interlayer spacing. Defects can show unexpected bonding, so the search over sites, charge states and configurations decides what is found.

**Resolved by.** The source of the starting structure and the relaxation procedure stated, with relaxed parameters compared with the measured ones; competing structures, orderings or decomposition products computed with the same settings and their energies reported; the sensitivity of the property that carries the claim to the lattice parameters shown, for example by computing it at both relaxed and measured lattice parameters; for defects, the sites, charge states and configurations searched described.

**Benchmark.** [4], [7], [8], [10]

## 4. Treatment of electron correlation

**Question.** For materials with localised d or f electrons or other strong correlation, how is correlation treated (DFT+U, hybrid functional, dynamical mean-field theory or another method), how were the parameters such as U chosen, and does the conclusion hold over a reasonable range of them?

**Why it matters.** Plain semi-local DFT can make a correlated insulator metallic. A Hubbard U fitted to reproduce one measured quantity cannot be relied on for others, and it does not carry over between structures, magnetic orders or basis sets; the gap, magnetic state and structure all move with U, with the choice of local orbitals and with the double-counting form. DFT+U is a static correction and can be qualitatively wrong where dynamical correlation matters.

**Resolved by.** The method, U and J values, their source (computed, for example by linear response, or taken from a cited study) and the orbitals they act on stated; key results shown for a range of U or with a second method; any parameter fitted to experiment identified, and that measurement not then counted as independent agreement; where the claim concerns correlated physics itself, a method that includes dynamical correlation or an argument why a static treatment suffices.

**Benchmark.** [1], [5]

## 5. Spin-orbit coupling and magnetic order

**Question.** Is spin-orbit coupling included where heavy elements, band inversion or magnetic anisotropy make it relevant, and was the magnetic configuration found by comparing several orderings, not assumed?

**Why it matters.** Spin-orbit coupling can open or invert gaps and decide the topology of the bands, so leaving it out can change the result. Many magnetic materials do not order ferromagnetically, and even a systematic search over collinear orderings matches the observed order in only part of known cases. A defect in a non-magnetic host can itself carry a spin, and assuming the wrong spin state is a common error.

**Resolved by.** A statement of whether spin-orbit coupling was included and how (self-consistently or as a perturbation), with results with and without it where the claim depends on it; several magnetic orderings, compatible with the supercell, compared at the same settings and their energies reported; the computed order and moments compared with neutron or magnetometry data where available; the limits of a collinear treatment acknowledged when the claim involves non-collinear order.

**Benchmark.** [4], [8], [9]

## 6. Band gaps and other comparisons with experiment

**Question.** When calculated band gaps, band structures or spectra are compared with measurements, does the paper account for the known gap error of the functional, distinguish the quantity computed from the quantity measured, and report the level of agreement, including disagreements?

**Why it matters.** Kohn-Sham band gaps from local and semi-local functionals are too small, often by up to about half the measured fundamental gap, and a negative calculated gap can produce a band inversion that is not there. The fundamental gap, the difference between ionisation energy and electron affinity, is the unbound limit of the exciton series, so it is not the same quantity as an optical absorption onset. Agreement on one feature, such as the shape of one band, does not show agreement on the feature that carries the claim.

**Resolved by.** The computed quantity named (Kohn-Sham, generalised Kohn-Sham or quasiparticle gap) and matched to what the experiment measures; where the claim depends on a gap or band ordering, a check with a hybrid functional, a gap-corrected potential or GW; the calculated and measured values given side by side with their differences, including features the calculation does not reproduce; any rigid shift or scaling applied to align the calculation with the data stated.

**Benchmark.** [2], [6], [7], [8]

## 7. Testing the interpretation, not only illustrating it

**Question.** Does the calculation make a prediction that could have disagreed with the interpretation, for example by computing the competing explanations with the same settings, or does it only reproduce a feature after the model or parameters were chosen to match it?

**Why it matters.** A calculation set up for one proposed structure, defect or mechanism, with parameters tuned towards the data, will usually show that mechanism and cannot distinguish it from alternatives that were not computed. Adjusting a functional or a parameter to match a measured value removes that value as a test. Wrong structures and wrong Hamiltonians can both give results that look like confirmation.

**Resolved by.** The alternatives named in the paper computed at the same level of theory and compared on the same observables; predictions for quantities not used in setting up the model, compared with data; the conclusion shown to survive changes of functional, U or structural model within their uncertainty; a clear statement in the text of which results are predictions and which were fitted.

**Benchmark.** [1], [3], [5], [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | K. Burke, Perspective on density functional theory, J. Chem. Phys. 136, 150901 (2012); read as preprint arXiv:1201.3679 | doi:10.1063/1.4704546 | full text | Sec. III: standard approximations give Kohn-Sham gaps that are too small and over-delocalise d electrons in transition-metal oxides. Sec. VI: no systematic route to improvement and no simple rule for reliability. Sec. VIII: hundreds of functionals; users advised to keep to standard ones or explain why not; fitted functionals do worse far from their fitting set; adjusting a functional to match a measured value called the worst form of empiricism. Sec. X: standard functionals miss van der Waals interactions |
| 2 | P. J. Hasnip, K. Refson, M. I. J. Probert, J. R. Yates, S. J. Clark and C. J. Pickard, Density functional theory in the solid state, Phil. Trans. R. Soc. A 372, 20130270 (2014); read in PubMed Central (PMC3928868) | doi:10.1098/rsta.2013.0270 | full text | Sec. 2: accuracy improves with the plane-wave cut-off; metals need much denser k-point grids than insulators; generalised gradient functionals improve on the local density approximation but rely on system-dependent error cancellation. Sec. 3: local and semi-local functionals underestimate band gaps; DFT+U, hybrids and screened exchange as remedies, with hybrid parameters fitted to molecular sets. Sec. 10(a): functional performance can only be tested against model systems, experiment or higher-level calculations. Sec. 10(b): dispersion a traditional weakness of DFT |
| 3 | E. Bosoni, L. Beal, M. Bercx, P. Blaha, S. Blügel et al., How to verify the precision of density-functional-theory implementations via reproducible and universal workflows, Nat. Rev. Phys. 6, 45–58 (2024; published online 2023); read as preprint arXiv:2305.17274 | doi:10.1038/s42254-023-00655-3 | full text | Recommendations section and Box 3: k-point spacing and smearing prescribed; smearing can change an equation of state, including which minimum is favoured. Results: spread between pseudopotential approaches much larger than between all-electron codes; rare-earth pseudopotentials often missing or less tested. Box 2: cite exact pseudopotentials with library and version, k-mesh, smearing and cut-offs, as missing information makes simulations non-reproducible; precision (numerics) distinguished from accuracy (functional), and users asked to state a validation argument for their functional |
| 4 | S. Kim et al., Quick-start guide for first-principles modelling of point defects in crystalline materials, J. Phys. Energy 2, 036001 (2020); read as preprint arXiv:2005.01941 | doi:10.1088/2515-7655/aba081 | full text | Practical calculations: the supercell method; a functional suited to the perfect crystal may not describe defects, with semi-local functionals giving spuriously delocalised states; defect chemistry can be unexpected, and interstitial sites and charge states need a wide search. Term 1: a non-magnetic host can need spin-polarised defect calculations, and assuming the wrong spin state is a common mistake. Term 4: interactions with periodic images reduced by larger supercells; charged-defect correction schemes, whose inconsistent choice changes defect densities by orders of magnitude |
| 5 | B. Himmetoglu, A. Floris, S. de Gironcoli and M. Cococcioni, Hubbard-corrected DFT energy functionals: the LDA+U description of correlated systems, Int. J. Quantum Chem. 114, 14–49 (2014); read as preprint arXiv:1309.3355 | doi:10.1002/qua.24521 | full text | Sec. I and II.1: approximate functionals over-delocalise valence electrons, and a Mott insulator can come out metallic. Sec. II.1: gap, localisation and structure depend on U and on how the correction is applied; double counting an open issue. Sec. III.1: tuning U to experiment is conceptually unsatisfactory, U is not portable between structures, magnetic orders and bases, and results depend on the local orbitals. Sec. III.3: U from linear response. Sec. II.4.4: DFT+U is the static limit of DFT plus dynamical mean-field theory and can be qualitatively wrong |
| 6 | J. P. Perdew, W. Yang, K. Burke, Z. Yang, E. K. U. Gross, M. Scheffler, G. E. Scuseria, T. M. Henderson, I. Y. Zhang, A. Ruzsinszky, H. Peng, J. Sun, E. Trushin and A. Görling, Understanding band gaps of solids in generalized Kohn-Sham theory, Proc. Natl. Acad. Sci. USA 114, 2801–2806 (2017); read in PubMed Central (PMC5358356) | doi:10.1073/pnas.1621352114 | full text | Abstract and section on the band-gap problem in Kohn-Sham DFT: even the exact Kohn-Sham gap underestimates the fundamental gap; local and semi-local functionals underestimate both, early local-density gaps often about half the measured value. Abstract and section on generalised Kohn-Sham: hybrid and meta-GGA gaps can be more realistic. Opening section of the main text: the fundamental gap is defined as ionisation energy minus electron affinity and is the unbound limit of the exciton series |
| 7 | J. Vidal, X. Zhang, L. Yu, J.-W. Luo and A. Zunger, False-positive and false-negative assignments of topological insulators in density functional theory and hybrids, Phys. Rev. B 84, 041109(R) (2011); read as preprint arXiv:1101.3734 | doi:10.1103/PhysRevB.84.041109 | full text | Section on false positives due to DFT: systematic gap underestimation produces false-positive band inversions in normal semiconductors. Section asking whether HSE06 is the answer: a fixed-mixing hybrid agrees with self-consistent GW for most compounds but gives false negatives for some. Section on the wrong choice of crystal structure: assumed structures give topological character while the lower-energy ground-state structures are normal, and one assumed structure is unstable to decomposition. Conclusion: prediction needs both the ground-state structure and the correct Hamiltonian |
| 8 | H. Zhang and S.-C. Zhang, Topological insulators from the perspective of first-principles calculations, Phys. Status Solidi RRL 7, 72–81 (2013); read as preprint arXiv:1209.6446 | doi:10.1002/pssr.201206414 | full text | Sec. 2.2: spin-orbit coupling is the key to band topology and should be included. Sec. 3.2: in one compound the band inversion appears only once spin-orbit coupling is switched on. Sec. 2.1: semi-local functionals underestimate gaps and sometimes give a negative gap where the real gap is positive; GW the most effective correction, a gap-corrected potential a cheaper one. Sec. 3.1: local-density DFT with spin-orbit coupling gives the wrong band order in one compound, corrected by the gap-corrected potential; the gap varies with lattice constant (Fig. 2). Sec. 3.2: slab calculations compared with photoemission, which shows a surface state the calculations do not find |
| 9 | M. K. Horton, J. H. Montoya, M. Liu and K. A. Persson, High-throughput prediction of the ground-state collinear magnetic order of inorganic materials using density functional theory, npj Comput. Mater. 5 (2019) | doi:10.1038/s41524-019-0199-7 | abstract | Abstract (read on the Lawrence Berkeley National Laboratory publication page): magnetic orderings enumerated and ranked by symmetry, then relaxed and compared with DFT+U; on 64 known magnetic materials, a non-ferromagnetic ground state predicted for about 95% and the observed ordering matched exactly in just over 60% |
| 10 | T. K. Reid, S. P. Alpay, A. V. Balatsky and S. K. Nayak, First-principles modeling of binary layered topological insulators: structural optimization and exchange-correlation functionals, Phys. Rev. B 101, 085140 (2020); read as preprint arXiv:1907.10544, which carries a slightly different title | doi:10.1103/PhysRevB.101.085140 | full text | Sec. III: the local density approximation gives lattice parameters below experiment and a gradient functional above; without a van der Waals correction the gradient functional overexpands the gap between layers, and dispersion-corrected functionals come close to experiment. Sec. IV: surface-state gaps and band features of slabs depend on which functional was used for relaxation. Sec. V: relaxation advised for non-stoichiometric or doped systems |
