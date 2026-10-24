---
id: T-BIOMOLECULAR-NMR
name: Biomolecular NMR
type: technique
field: physics/biological
applies_when: the paper uses solution or solid-state NMR of proteins or nucleic acids to report resonance assignments, a structure calculated from NMR restraints, relaxation or exchange dynamics, or binding sites and affinities from chemical-shift perturbation
version: "0.1"
---

# Biomolecular NMR

Biomolecular nuclear magnetic resonance (NMR) spectroscopy, in solution or in the solid state with magic-angle spinning (MAS), is used to claim resonance assignments, three-dimensional structures calculated from restraints such as nuclear Overhauser effect (NOE) distances and dihedral angles, internal motions from spin relaxation and relaxation dispersion, and binding sites and dissociation constants (Kd) from chemical-shift perturbation (CSP). All of these rest on chemical shifts and peak intensities that are only as good as the referencing, the assignment and the state of the sample.

## 1. Chemical-shift referencing and assignment

**Question.** Does the paper state how chemical shifts were referenced (for example to DSS, with indirect referencing of carbon and nitrogen), how complete the assignment is for the construct studied, how the assignments were obtained and checked, and are the shifts deposited?

**Why it matters.** A referencing offset shifts every value and biases anything derived from shifts, such as secondary structure, torsion-angle restraints or comparisons with other studies. Audits of deposited data have found that a substantial fraction of entries were mis-referenced and that many contain at least one assignment error, and an incomplete or wrong assignment passes directly into the restraints and into any per-residue interpretation.

**Resolved by.** The reference compound and the referencing method stated; assignment completeness given against the full construct, with the experiments used to make the assignments listed; a check of the shifts against database statistics or shifts predicted from the structure, with outliers explained; the assigned shifts deposited in the Biological Magnetic Resonance Data Bank (BMRB).

**Benchmark.** [1], [2], [3]

## 2. Restraints and their agreement with the model

**Question.** Does the paper report how many restraints of each kind were used, grouped by sequence separation (intra-residue, sequential, medium and long range), how ambiguous restraints were treated, how intermolecular restraints were told apart from intramolecular ones in an oligomer or complex, and the number and size of restraint violations across the ensemble, and are the restraints deposited?

**Why it matters.** The fold is defined mainly by long-range restraints, so a total count can hide how little constrains the tertiary structure. Ambiguous and stereospecifically unassigned restraints must be averaged correctly, and restraints that were violated in early rounds are often removed, so a model can show few violations because the inconvenient data were discarded. In a symmetric oligomer an intersubunit NOE gives the same cross-peak as an intrasubunit one, so the interface is undetermined unless the two are separated experimentally. Without the deposited restraints a reader cannot check the agreement at all.

**Resolved by.** A table of restraints by type and sequence separation, including inter-chain restraints; the treatment of ambiguous restraints stated; for oligomers or complexes, intermolecular restraints identified by isotope-filtered experiments on mixed-labelled samples or by other stated means; violations binned by size with the largest named, per model and for the ensemble, and mapped onto residues; any restraints removed during calculation listed with the reason; restraints deposited in a standard format such as NEF or NMR-STAR together with the coordinates.

**Benchmark.** [1], [4], [6], [13]

## 3. Ensemble precision is not accuracy

**Question.** Does the paper treat the root-mean-square deviation (RMSD) of its ensemble as a measure of precision only, define the well-defined regions over which it is quoted, and avoid reading the spread of the ensemble as a measure of accuracy or of motion?

**Why it matters.** An NMR ensemble shows how consistently the restraints were satisfied by the calculation, not how close the model is to the true structure, and it is not a statistically sound estimate of coordinate uncertainty or of dynamics. Ensemble RMSD and the number of restraints per residue correlate poorly with accuracy, and loops with few restraints can look flexible or well defined for reasons unrelated to their motion.

**Resolved by.** RMSD quoted over stated well-defined residues, with the method used to choose them; the ensemble described as precision, with separate evidence for accuracy (item 4); claims about flexibility supported by relaxation or other dynamics data, not by ensemble spread alone; coordinates supplied for all assigned residues, including poorly defined ones.

**Benchmark.** [1], [5], [6]

## 4. Geometry and agreement with the data

**Question.** Is the structure validated both by knowledge-based checks (backbone torsion angles, steric clashes, packing) reported against reference distributions, and by a measure of agreement with data, such as NOESY peak lists, residual dipolar couplings or backbone chemical shifts, that does not depend only on the restraints used in the calculation?

**Why it matters.** Refinement can give good stereochemistry to a structure that is wrong, and a structure with a significantly wrong fold can still score well on geometric quality measures. Agreement with the restraints alone is circular, because the restraints were fitted, and restraint violations are a weak guide to accuracy.

**Resolved by.** Ramachandran and clash statistics for the well-defined regions, given as scores or percentiles against the archive; at least one model-versus-data score, such as agreement with the NOESY peak list or with residual dipolar couplings, or a comparison of rigidity predicted from the structure with that inferred from backbone shifts; where a structure was calculated automatically, the input peak lists and the data-agreement score reported.

**Benchmark.** [1], [5], [6]

## 5. Relaxation analysis and the model-free approach

**Question.** For order parameters and internal correlation times from longitudinal (R1) and transverse (R2) relaxation rates and heteronuclear NOE, does the paper state the rotational diffusion model and how it was chosen, the number of magnetic fields, how the motional models were selected, and whether chemical exchange was separated from R2?

**Why it matters.** The model-free analysis assumes that internal motion is independent of, and faster than, overall tumbling, and its parameters depend on the diffusion tensor. Fitting an isotropic tensor to a molecule that tumbles anisotropically, or choosing too simple a motional model, can create apparent nanosecond motions or apparent exchange that are artefacts of the fit. R2 includes any microsecond-to-millisecond exchange contribution, so a high R2 alone does not show exchange or rigidity.

**Resolved by.** Relaxation data at two or more magnetic fields; the diffusion tensor tested among isotropic, axially symmetric and fully anisotropic forms, with the choice justified; model selection by a stated statistical criterion, such as the Akaike information criterion, with the selected model given per residue; exchange contributions identified and, where they matter to the claim, confirmed by relaxation dispersion.

**Benchmark.** [7], [8]

## 6. Chemical exchange and relaxation dispersion

**Question.** When rates, populations or chemical-shift differences of a minor state are claimed from relaxation dispersion, does the paper state the exchange model and the equation used, the number of fields, and how strongly the fitted parameters are correlated?

**Why it matters.** Dispersion curves are usually fitted with a two-state model, and many combinations of rate, population and shift difference can fit a curve equally well, particularly in fast exchange, where these parameters combine into one. Pulse imperfections can also produce spurious dispersions. A more complex model always fits at least as well, so the extra parameters need statistical justification.

**Resolved by.** The exchange model and fitting equation stated together with its regime of validity; data at more than one magnetic field, or of more than one kind of magnetisation; residues fitted globally only when a shared process is justified; a statistical comparison of competing models; correlations between the fitted parameters reported; the pulse sequence and its calibration stated, so that artefactual dispersion can be ruled out.

**Benchmark.** [7]

## 7. Chemical-shift perturbation and affinity

**Question.** For binding sites and dissociation constants from CSP titrations, does the paper establish the exchange regime from the behaviour of the peaks, state how the proton and nitrogen shift changes were combined, and show the fitted titration curves with the binding model and concentrations used?

**Why it matters.** A Kd can be read from peak positions only in fast exchange; in intermediate exchange, shift and intensity changes are not linearly related to the fraction bound, and an analysis that ignores exchange effects gives systematically wrong Kd values. Chemical shifts change at a binding site and also at sites affected allosterically or by changes in conformation, so a map of shift changes does not by itself separate direct contact from indirect effects.

**Resolved by.** Spectra across the titration showing whether peaks shift, broaden or appear and disappear; the weighting of the combined shift change and the threshold for a significant change stated; protein and ligand concentrations given and the binding model fitted to several residues; lineshape analysis where peaks broaden; binding-site assignments supported by an independent method where direct contact, rather than an indirect change, is claimed.

**Benchmark.** [9], [10]

## 8. Sample state, oligomerisation and homogeneity

**Question.** Does the paper report the sample conditions (protein concentration, buffer, pH, ionic strength and temperature), show that the protein is in the claimed oligomeric state at NMR concentrations, for example from a rotational correlation time compared with molecular mass, and, for solid-state samples, address heterogeneity such as multiple conformers?

**Why it matters.** NMR samples are concentrated and often held for days, so self-association, aggregation or partial unfolding can change linewidths, relaxation rates and chemical shifts and be misread as dynamics, binding or structure. The rotational correlation time reflects the size of the tumbling species, so it tests whether a protein is monomeric or oligomeric under the measurement conditions. In solid-state samples, coexisting conformations give more than one set of shifts and broadened lines, and preparation conditions can change the spectra.

**Resolved by.** Full sample conditions for every data set; a correlation time estimated from relaxation and compared with that expected for the claimed oligomer, or another measure of the oligomeric state, such as gel filtration with light scattering, at comparable concentration; the spectrum shown to be stable over the time of the measurements; for solid-state work, the preparation described in full, linewidths reported, and peak doubling either assigned to distinct conformers or excluded.

**Benchmark.** [7], [11], [12]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | G. T. Montelione, M. Nilges, A. Bax, P. Güntert, T. Herrmann, J. S. Richardson, C. D. Schwieters, W. F. Vranken, G. W. Vuister, D. S. Wishart, H. M. Berman, G. J. Kleywegt and J. L. Markley, Recommendations of the wwPDB NMR Validation Task Force, Structure 21, 1563–1570 (2013); read as the author manuscript in PubMed Central (PMC3884077) | doi:10.1016/j.str.2013.07.021 | full text | Sec. 1.1: report assignment completeness against the full construct, global referencing corrections and shift outliers, with tools such as LACS and AVS. Sec. 1.2: the ensemble is not a statistically sound estimate of coordinate precision and does not truly represent dynamics; ill-defined regions may reflect dynamics or missing restraints. Phase 3: restraints per residue correlate poorly with accuracy. Sec. 1.3: MolProbity clashes, packing and Ramachandran checks on well-defined regions, as percentiles against X-ray and NMR archives. Sec. 1.4: restraints grouped by sequence separation including inter-chain, ambiguous restraints evaluated with r^-6 summation, violations binned by size with the largest reported. Principal recommendations: coordinates for all assigned residues |
| 2 | H. Zhang, S. Neal and D. S. Wishart, RefDB: a database of uniformly referenced protein chemical shifts, J. Biomol. NMR 25, 173–195 (2003) | doi:10.1023/A:1022836027055 | abstract | Abstract: comparing observed with structure-predicted shifts found that about a quarter of BMRB entries with carbon and nitrogen assignments needed significant re-referencing, nearly 40% of entries appeared to contain at least one assignment error, and about 20% of new entries were still incorrectly referenced |
| 3 | Biological Magnetic Resonance Data Bank (BMRB), Indirect chemical shift referencing, reference information web page (undated; accessed 2026) | https://bmrb.io/ref_info/cshift.shtml | full text | Whole page: carbon, nitrogen and phosphorus shifts referenced indirectly through frequency ratios relative to the proton signal of DSS, with the IUPAC-IUB ratios and their sources (Wishart et al. 1995; Markley et al. 1998) |
| 4 | K. Baskaran, E. Ploskon, R. Tejero, M. Yokochi, D. Harrus et al., Restraint validation of biomolecular structures determined by NMR in the Protein Data Bank, Structure 32, 824–837 (2024); read in PubMed Central (PMC11162339) | doi:10.1016/j.str.2024.02.011 | full text | Introduction and Results: model-versus-restraint validation as a minimum check, and a model with few violations can still be wrong. Restraint violation analysis, Tables 2 and 3 and Figs. 5 and 6: restraints counted by sequence separation; violations binned at 0.1–0.2, 0.2–0.5 and above 0.5 Å per model and ensemble and mapped per residue; ambiguous restraints evaluated by r^-6 summation. Results and Discussion: shifts and restraints mandatory for deposition, NEF or NMR-STAR format, NOESY peak lists encouraged |
| 5 | A. Rosato, J. M. Aramini, C. Arrowsmith, A. Bagaria, D. Baker et al., Blind testing of routine, fully automated determination of protein structures from NMR data, Structure 20, 227–236 (2012); read in PubMed Central (PMC3609704) | doi:10.1016/j.str.2012.01.002 | full text | Results, accuracy and convergence: number of restraints did not correlate with accuracy; conclusions assume nearly complete assignments and artefact-free peak lists. Results, geometric quality: structures with a significantly wrong fold can have excellent geometric scores. Results, agreement with data, and Discussion: the DP score against NOESY peak lists tracked accuracy, and geometric parameters alone are not sufficient |
| 6 | N. J. Fowler, A. Sljoka and M. P. Williamson, A method for validating the accuracy of NMR protein structures, Nat. Commun. 11, 6321 (2020); read in Europe PMC (PMC7749147) | doi:10.1038/s41467-020-20177-1 | full text | Results, comparison with conventional predictors, and Discussion: ensemble RMSD is a poor guide to accuracy but a measure of precision; distance restraint violations do not predict accuracy, partly because violated restraints are often discarded. Results, comparison with crystal structures: NMR structures too flexible in loops with few restraints. Method: rigidity from the structure compared with backbone chemical shifts as an accuracy check, alongside Ramachandran analysis |
| 7 | I. R. Kleckner and M. P. Foster, An introduction to NMR-based approaches for measuring protein dynamics, Biochim. Biophys. Acta 1814, 942–968 (2011); read in PubMed Central (PMC3061256) | doi:10.1016/j.bbapap.2010.10.012 | full text | Secs. 3.4 and 3.5: dispersion fitted with a two-state model; many parameter sets fit equally well; fast-exchange form merges population and shift difference; multiple fields and magnetisation types recommended; pulse imperfections give spurious dispersions. Sec. 3.6: model-free analysis assumes internal motion independent of and faster than tumbling; R2 includes exchange and is affected by anisotropic rotation; data usually at two fields; R1 and R2 depend on tumbling time. Appendix A.1: model comparison by reduced chi-squared, AIC, BIC or F-test |
| 8 | E. J. d'Auvergne and P. R. Gooley, Optimisation of NMR dynamic models II. A new methodology for the dual optimisation of the model-free parameters and the Brownian rotational diffusion tensor, J. Biomol. NMR 40, 121–133 (2008); read in Europe PMC (PMC2758375) | doi:10.1007/s10858-007-9213-3 | full text | Methods: model selection by AIC; at least six data sets at two or more fields. Results, test system: too simple a diffusion tensor causes under-fitting artefacts, including artificial sub-nanosecond motions and fictitious exchange; over-fitting the tensor adds noise without bias. Results, reanalyses: a revised tensor and model selection removed most of the exchange originally reported for one protein |
| 9 | M. P. Williamson, Using chemical shift perturbation to characterise ligand binding, Prog. Nucl. Magn. Reson. Spectrosc. 73, 1–16 (2013) | doi:10.1016/j.pnmrs.2013.02.001 | abstract | Abstract: exchange rate determines the appearance of the titration; Kd can be found from peak positions in fast exchange, typically for Kd above about 3 µM, while slow and intermediate exchange broaden lines and make Kd hard to measure; weighted proton and nitrogen shift changes map the site; CSP cannot easily separate direct binding from allosteric change |
| 10 | C. A. Waudby, A. Ramos, L. D. Cabrita and J. Christodoulou, Two-dimensional NMR lineshape analysis, Sci. Rep. 6, 24826 (2016); read in PubMed Central (PMC4843008) | doi:10.1038/srep24826 | full text | Introduction: analyses that neglect exchange effects can give systematic errors in fitted Kd; in intermediate exchange, shift and intensity changes are not linearly related to binding. Results and Discussion: differential relaxation distorts one-dimensional analyses; parameters need reliable uncertainty estimates, obtained by block bootstrap |
| 11 | P. Rossi, G. V. T. Swapna, Y. J. Huang, J. M. Aramini, C. Anklin et al., A microscale protein NMR sample screening pipeline, J. Biomol. NMR 46, 11–22 (2010); read in Europe PMC (PMC2797623) | doi:10.1007/s10858-009-9386-z | full text | Section on oligomerisation states: rotational correlation time from nitrogen T1/T2 compared with a calibration against molecular mass of known monomers, reliable up to about 25 kDa, used to confirm the oligomeric state found by gel filtration with static light scattering. Buffer optimisation: pH, ionic strength and buffer screened to limit aggregation |
| 12 | B. Reif, S. E. Ashbrook, L. Emsley and M. Hong, Solid-state NMR spectroscopy, Nat. Rev. Methods Primers 1, 2 (2021); read in PubMed Central (PMC8341432) | doi:10.1038/s43586-020-00002-1 | full text | Applications: an amyloid fibril example in which two coexisting conformations give two sets of shifts per atom. Limitations: disordered samples give much broader lines. Reproducibility and data deposition: shifts are sensitive to conformational heterogeneity and sample preparation can change the spectra; report full sample preparation and acquisition parameters; BMRB accepts shifts and restraints |
| 13 | H.-W. Lee, G. Wylie, S. Bansal, X. Wang, A. W. Barb, M. A. Macnaughtan, A. Ertekin, G. T. Montelione and J. H. Prestegard, Three-dimensional structure of the weakly associated protein homodimer SeR13 using RDCs and paramagnetic surface mapping, Protein Sci. 19, 1673–1685 (2010); read in PubMed Central (PMC2975131) | doi:10.1002/pro.447 | full text | Introduction: in a symmetric dimer, intersubunit and intrasubunit NOEs give the same cross-peaks and are hard to tell apart; isotope-filtered NOE experiments on mixed labelled and unlabelled samples isolate intersubunit contacts, at reduced sensitivity, and work poorly for weak dimers |
