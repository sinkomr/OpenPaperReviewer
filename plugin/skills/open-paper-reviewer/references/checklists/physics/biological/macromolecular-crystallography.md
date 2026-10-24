---
id: T-MACROMOLECULAR-CRYSTALLOGRAPHY
name: Macromolecular crystallography
type: technique
field: physics/biological
applies_when: the paper reports an X-ray or neutron crystal structure of a protein, nucleic acid or complex, or bases a claim about a binding mode, a bound ligand or metal, an active-site chemistry, a protonation state or a conformational change on such a structure
version: "0.1"
---

# Macromolecular crystallography

Macromolecular crystallography (MX) with X-rays or neutrons is used to claim the atomic structure of proteins, nucleic acids and their complexes, and from it the presence and pose of bound ligands, the identity of metals and ions, protonation states and mechanisms. The structure is a model refined against diffraction data, and the map that is shown as evidence is computed partly from that model.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | P. R. Evans and G. N. Murshudov, How good are my data and what is the resolution?, Acta Cryst. D 69, 1204–1214 (2013) | doi:10.1107/S0907444913000061 | full text | Sec. 3.2.1: mean signal-to-noise as a cut-off criterion depends on how well sigma is estimated; Sec. 3.2.2: merging R values tend to infinity as data weaken, and CC1/2 from random half-data sets is preferred; Sec. 3.2.3: most data sets are anisotropic, analysed by direction. Sec. 4.2: adding weak high-resolution data seemed to do no harm; Sec. 5: a harsh cut-off at data reduction is advised against, since data can be excluded later |
| 2 | R. J. Read, P. D. Adams, W. B. Arendall III et al., A new generation of crystallographic validation tools for the Protein Data Bank, Structure 19, 1395–1412 (2011) | doi:10.1016/j.str.2011.08.006 | full text | Data-validation sections: checks for Wilson outliers, anisotropy, twinning, missed symmetry and translational non-crystallographic symmetry. "Agreement of the model with the diffraction data": R-free as the most useful global measure of fit, ranked by resolution; "Missed Symmetries" and "Twinning": a test set not compatible with real or pseudo-crystallographic symmetry, or not invariant under the twin law, lowers R-free artificially; real-space R preferred for local fit. Geometry sections: Engh and Huber targets, Ramachandran, rotamer and clash criteria, scores as percentiles by resolution class. "Ligands": Mogul geometry checks and ligands with real-space R over twice the protein average flagged. "Ions": metal identity hard to establish from density, anomalous scattering and coordination help, and some ions are misidentified |
| 3 | A. T. Brünger, Free R value: a novel statistical quantity for assessing the accuracy of crystal structures, Nature 355, 472–475 (1992) | doi:10.1038/355472a0 | abstract | Abstract: an incorrect model can be refined to a fairly good conventional R value; the free R value, computed from a test set of reflections left out of modelling and refinement, is proposed as a cross-validated measure and correlates with the accuracy of the model phases |
| 4 | D. Liebschner, P. V. Afonine, N. W. Moriarty, B. K. Poon, O. V. Sobolev, T. C. Terwilliger and P. D. Adams, Polder maps: improving OMIT maps by excluding bulk solvent, Acta Cryst. D 73, 148–157 (2017) | doi:10.1107/S2059798316018210 | full text | Abstract: maps used in structure solution are almost always model-biased; Sec. 1: omit maps test ligands, waters and weak regions, but the flat bulk-solvent model fills the omitted region and keeping atoms at zero occupancy biases the residual density. Sec. 5, "Validation of polder maps": comparing the polder map with maps calculated with and without the atoms tests whether the density is better explained by the atoms or by solvent |
| 5 | M. C. Deller and B. Rupp, Models of protein–ligand crystal structures: trust, but verify, J. Comput. Aided Mol. Des. 29, 817–836 (2015) | doi:10.1007/s10822-015-9833-8 | full text | "Electron density-based validation of protein–ligand models": maps computed with the ligand are biased towards its presence, so difference omit maps calculated without the ligand are the stronger evidence; real-space correlation above 0.9 for well-defined ligands and below 0.8 for poorly modelled ones. "Disorder and mobility" and the environment section: ligand B-factors well above the local average and low occupancy call for caution; stereochemistry, crystal contacts and chemistry checked. "Ligand binding is rarely complete": weak binders at practical concentrations cannot reach full occupancy. Same section: a small but significant fraction of ligand models are only partly based on evidence |
| 6 | H. Zheng, D. R. Cooper, P. J. Porebski, I. G. Shabalin, K. B. Handing and W. Minor, CheckMyMetal: a macromolecular metal-binding validation tool, Acta Cryst. D 73, 223–233 (2017) | doi:10.1107/S2059798317001061 | full text | Introduction: metals are modelled in about 40% of PDB entries and a significant fraction of sites are poorly modelled. Validation parameters: coordinating ligands, bond valence, geometry, occupancy and B-factor relative to the environment; anomalous data and spectroscopy as independent evidence. Examples of sodium, magnesium, calcium, potassium, chloride and water confused; default restraints for magnesium and zinc that differ from ideal distances; B-factor or density alone not sufficient |
| 7 | E. F. Garman, Radiation damage in macromolecular crystallography: what is it and why should we care?, Acta Cryst. D 66, 339–351 (2010) | doi:10.1107/S0907444910008656 | full text | Abstract and introduction: damage remains a concern at 100 K and produces artefacts that affect biological interpretation. Global damage sections: intensity loss and B-factor increase as indicators. Sec. 2: global indicators such as intensity decay and relative B-factor; specific damage to disulphides and glutamate and aspartate in a reproducible order, often well before the diffraction visibly degrades, with sequential data sets showing it; Sec. 3: metal centres reduced swiftly, monitored by on-line spectroscopy; dose estimated from beam, crystal size and composition with RADDOSE. Sec. 4: data merged from several crystals, and control experiments needed to separate damage from mechanism. Sec. 5: recommended limit of 30 MGy |
| 8 | C. J. Williams, J. J. Headd, N. W. Moriarty et al., MolProbity: more and better reference data for improved all-atom structure validation, Protein Sci. 27, 293–315 (2018) | doi:10.1002/pro.3330 | full text | "MolProbity Workflow and New Validations": all-atom clashscore, Ramachandran, rotamer, C-beta deviation, cis-nonproline and CaBLAM checks, with percentiles against structures of similar resolution. "Understanding Local Quality and Making Local Corrections": check each outlier against the density, correct those without support and keep those supported by density and interactions; except for small high-resolution structures, zero outliers usually means overfitting |
| 9 | D. Liebschner, P. V. Afonine, N. W. Moriarty, P. Langan and P. D. Adams, Evaluation of models determined by neutron diffraction and proposed improvements to their validation and deposition, Acta Cryst. D 74, 800–813 (2018) | doi:10.1107/S2059798318004588 | full text | Sec. 1: hydrogen's negative scattering length cancels density next to positively scattering atoms such as in CH2 groups, partly exchanged H/D sites near 0.6:0.4 cancel, deuteration reduces incoherent background, individual hydrogen refinement adds many parameters, and neutron data are typically less complete than X-ray data, about 80% on average. Sec. 3: exchanged sites, H/D occupancies and protonation states modelled inconsistently; X-ray X-H bond lengths used in over 40 models; reported R values often not reproducible. Sec. 4: deposit all H and D atoms, deposit and label all data of joint models, standardise exchange modelling, develop neutron-specific validation |
