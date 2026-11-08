---
id: T-MACROMOLECULAR-CRYSTALLOGRAPHY
name: Macromolecular crystallography
type: technique
field: physics/biological
applies_when: the paper reports an X-ray or neutron crystal structure of a protein, nucleic acid or complex, or bases a claim about a binding mode, a bound ligand or metal, an active-site chemistry, a protonation state or a conformational change on such a structure
version: "0.1"
---

# Macromolecular crystallography

## 1. Data quality and the resolution cut-off

**Question.** Does the paper report the data statistics overall and in the highest-resolution shell, including completeness, signal-to-noise and the half-dataset correlation (CC1/2), and does it say how the high-resolution cut-off was chosen?

**Why it matters.** The quoted resolution sets how much detail the model can carry, yet it is a choice made during data reduction. Merging R values grow without limit as data weaken and give no sensible cut-off, while a cut-off that is too harsh throws away usable data; anisotropic diffraction makes a single figure misleading. Problems such as twinning, translational non-crystallographic symmetry and outlier intensities also change what the data can support.

**Resolved by.** A data-collection table with overall and outer-shell values for completeness, mean signal-to-noise and CC1/2; the criterion behind the cut-off stated; anisotropy reported, with direction-dependent limits where used; tests for twinning and translational non-crystallographic symmetry reported, and twinned data refined with a twin-aware target.

**Benchmark.** [1], [2]

## 2. Cross-validation with R-free

**Question.** Is R-free reported alongside R-work, how was the test set chosen and kept out of refinement, and does that choice respect any crystallographic, pseudo-crystallographic or twin symmetry?

**Why it matters.** A model can be overfitted and still reach a low conventional R value, so the free R value, computed from reflections withheld from refinement, is the main global check of fit. It is only informative if the withheld reflections are independent of the working set: a test set that ignores higher symmetry, pseudo-symmetry or twinning gives an R-free that is too low.

**Resolved by.** R-work and R-free both reported and compared with structures at similar resolution; the size and selection of the test set stated, with the same set kept out of refinement throughout; the test set chosen so that reflections related by the full lattice symmetry, including any pseudo-symmetry, are not split between the working and test sets, and made twin-law invariant for twinned data.

**Benchmark.** [2], [3]

## 3. Model bias in the maps shown as evidence

**Question.** For each feature on which a claim rests (a ligand, a water network, an alternative conformation, a modified residue), does the paper show a map computed without that feature in the model, such as an omit, polder or difference map, and not only a map computed with it?

**Why it matters.** Routine maps such as 2mFo-DFc use the model's phases, so atoms placed in the model tend to appear in the map whether or not the data support them. Omit maps reduce this bias, but in a standard refinement the bulk-solvent model fills the omitted region and can hide weak density, while leaving the atoms in at zero occupancy still biases the result.

**Resolved by.** Omit or polder maps computed with the feature removed, with the map type and contour level given in each figure caption; for weak density, a comparison of the omit map with maps calculated from models with and without the feature, as a test of whether the density is better explained by the feature or by solvent.

**Benchmark.** [4], [5]

## 4. Ligand identity, pose and occupancy

**Question.** Does the paper show that the electron density supports the ligand and the claimed binding pose, report a real-space fit measure, refined occupancy and B-factors compared with the surrounding protein, and check the ligand geometry against small-molecule standards?

**Why it matters.** Density for a partially bound or mobile ligand is weak, and maps computed with the ligand in the model are biased towards showing it, so a small but significant fraction of deposited ligand models rest only partly on evidence. Ligands with B-factors far above their surroundings or a poor real-space fit may be absent, partly occupied or in a different pose. A weakly binding ligand at the soaking or co-crystallisation concentration used may not reach full occupancy at all.

**Resolved by.** Difference omit density shown for the ligand before it was modelled; a real-space correlation coefficient or real-space R for the ligand, compared with the protein; occupancy refined and B-factors compared with neighbouring atoms; bond lengths, angles and chirality checked against small-molecule data with restraints described; the chemical environment, crystal contacts and tautomer or protonation state considered; the expected occupancy related to the affinity and concentration used.

**Benchmark.** [2], [5]

## 5. Metals and ions

**Question.** How was the identity of each metal or ion established, and does the paper report coordination distances and geometry, B-factors relative to the coordinating atoms and, where possible, an anomalous or spectroscopic signal?

**Why it matters.** Electron density alone often cannot tell a water from a sodium or magnesium ion, or potassium from chloride, such ions have been confused in deposited structures, and a significant fraction of structures with metals contain poorly modelled sites. Default restraints can also hold a metal at distances that do not match its known coordination, which then hides an incorrect assignment.

**Resolved by.** Each assignment supported by coordination number, distances and geometry matching the proposed metal, a bond-valence or similar check, B-factors and occupancy consistent with the environment, and the crystallisation and buffer conditions; where the identity matters to a claim, anomalous difference maps collected near and away from an absorption edge, fluorescence scans or an independent elemental analysis.

**Benchmark.** [2], [6]

## 6. Radiation damage

**Question.** What X-ray dose did the crystal receive, how was it estimated, and does the paper check that the features on which the claim rests, such as metal oxidation states, disulphide bonds or carboxylate groups, are not produced by radiation damage?

**Why it matters.** Even at 100 K, X-rays degrade data and cause specific changes in a reproducible order: disulphide bonds break, glutamate and aspartate lose carboxyl groups, and metal centres are photoreduced, often before the diffraction visibly fades. These changes can be mistaken for chemistry, which matters most for redox states, reaction intermediates and active-site structures.

**Resolved by.** The absorbed dose estimated from the beam, crystal size and composition, and kept below accepted limits, bearing in mind that specific damage starts at doses well below a global limit; damage indicators such as intensity decay and B-factor increase across the data set reported; for sensitive sites, structures or spectra from low-dose or multiple-crystal data, or a dose series, used as controls to show that the feature does not change with dose.

**Benchmark.** [7]

## 7. Validation against geometric and conformational standards

**Question.** Does the paper report standard validation results for the model, such as deviations from ideal bond lengths and angles, Ramachandran and rotamer outliers and all-atom clashes, compared with structures at similar resolution, and does it account for outliers near the region the claim is about?

**Why it matters.** Validation checks catch errors that the fit to the data can miss, such as backbone misfits, flipped side chains and atoms placed too close together. Outliers can be real when the density and interactions support them, but outliers without density support usually signal a misfit, and a model with no outliers at all can indicate overfitting.

**Resolved by.** A wwPDB validation report or equivalent statistics, with percentile ranks against the whole archive and the resolution class; bond and angle deviations relative to standard targets; Ramachandran, rotamer and clash scores; each outlier near the site of interest either corrected or justified by density and interactions; the restraint library and any conformational restraints used in refinement stated.

**Benchmark.** [2], [8]

## 8. Hydrogen and deuterium in neutron models

**Question.** For neutron or joint X-ray and neutron structures used to claim protonation states or hydrogen-bond networks, does the paper report the deuteration of the sample, the completeness and resolution of the neutron data, how hydrogen and deuterium at exchangeable sites were modelled, and the nuclear density for each claimed proton position?

**Why it matters.** Hydrogen has a negative and deuterium a positive neutron scattering length, so partly exchanged sites can cancel and show no density, and hydrogen next to carbon can cancel nearby density. Neutron data are often less complete than X-ray data, and refining hydrogen atoms individually adds many parameters, so the assignment of a proton can rest on limited information. Deposited neutron models have used varied, sometimes inconsistent, ways of modelling exchange and protonation.

**Resolved by.** The deuteration of protein and solvent stated; neutron data statistics, including completeness, given separately from any X-ray data; the treatment of exchangeable sites and the refined H/D occupancies reported; all hydrogen and deuterium atoms used in refinement deposited; the nuclear density shown at each proton position on which a claim rests; neutron-specific X-H bond lengths used in refinement; every data set used in a joint refinement deposited and labelled, with R values that can be reproduced from the deposited data.

**Benchmark.** [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | P. R. Evans and G. N. Murshudov, How good are my data and what is the resolution?, Acta Cryst. D 69, 1204 (2013) | doi:10.1107/S0907444913000061 |
| 2 | R. J. Read et al., A new generation of crystallographic validation tools for the Protein Data Bank, Structure 19, 1395 (2011) | doi:10.1016/j.str.2011.08.006 |
| 3 | A. T. Brünger, Free R value: a novel statistical quantity for assessing the accuracy of crystal structures, Nature 355, 472 (1992) | doi:10.1038/355472a0 |
| 4 | D. Liebschner et al., Polder maps: improving OMIT maps by excluding bulk solvent, Acta Cryst. D 73, 148 (2017) | doi:10.1107/S2059798316018210 |
| 5 | M. C. Deller and B. Rupp, Models of protein–ligand crystal structures: trust, but verify, J. Comput. Aided Mol. Des. 29, 817 (2015) | doi:10.1007/s10822-015-9833-8 |
| 6 | H. Zheng et al., CheckMyMetal: a macromolecular metal-binding validation tool, Acta Cryst. D 73, 223 (2017) | doi:10.1107/S2059798317001061 |
| 7 | E. F. Garman, Radiation damage in macromolecular crystallography: what is it and why should we care?, Acta Cryst. D 66, 339 (2010) | doi:10.1107/S0907444910008656 |
| 8 | C. J. Williams et al., MolProbity: more and better reference data for improved all-atom structure validation, Protein Sci. 27, 293 (2018) | doi:10.1002/pro.3330 |
| 9 | D. Liebschner et al., Evaluation of models determined by neutron diffraction and proposed improvements to their validation and deposition, Acta Cryst. D 74, 800 (2018) | doi:10.1107/S2059798318004588 |
