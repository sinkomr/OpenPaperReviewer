---
id: T-MOLECULAR-DYNAMICS-EVIDENCE
name: Molecular dynamics as evidence
type: technique
field: physics/biological
applies_when: the paper uses molecular dynamics, enhanced sampling or related biomolecular simulations to support a mechanism, a conformational change, a binding mode, a free energy, a pathway or the interpretation of an experiment
version: "0.1"
---

# Molecular dynamics as evidence

## 1. Force field and model fitted to the system

**Question.** Does the paper name the force field, water model and model resolution (all-atom or coarse-grained, explicit or implicit solvent and membrane) and justify them for this kind of system, citing tests against experimental data for comparable molecules?

**Why it matters.** Force fields differ in how well they reproduce experimental data, and a force field that does well for folded proteins can give disordered regions that are too compact or secondary structure that is too stable or too weak. Membranes, disordered proteins, nucleic acids, glycans and ligands each need parameters validated for them, and cut-off and electrostatics settings are part of the model. A mechanism that appears only with one force field may reflect that force field rather than the molecule.

**Resolved by.** The exact force field, version and water model stated, with cut-offs and electrostatics consistent with its parameterisation; references showing that it reproduces experimental data for the relevant class of system; parameters for non-standard molecules described and tested; for a claim that depends on a balance of interactions, the key result repeated with a second force field or shown to be insensitive to the choice.

**Benchmark.** [1], [2], [3], [4]

## 2. Starting structure, protonation states and set-up

**Question.** Does the paper state where the starting structure came from and how missing parts were modelled, which protonation and tautomer states were assigned to titratable residues and ligands and on what basis, and the composition of the simulated system (box size, ions and salt concentration, lipids)?

**Why it matters.** Conventional MD holds protonation states fixed, so an assignment made once from a single structure decides the charges for the whole run, and residues in active sites or inserted in membranes can have pKa values far from those in solution. Errors in preparation produce a system that runs smoothly but is not the one intended, and a stable equilibration does not show that the set-up was correct.

**Resolved by.** The source of the starting coordinates and every modelled or mutated segment given; the protonation state of each titratable residue near the site of interest stated, with the pKa estimate or experimental evidence behind it, and alternative states tested where the assignment is uncertain or may change with conformation, for example by constant pH simulations; a table of system composition and the restraints, thermostat and barostat used.

**Benchmark.** [1], [4], [5]

## 3. Equilibration and sampling relative to the process

**Question.** Does the paper show how equilibration was separated from production, and is the total sampling long compared with the slowest process the claim depends on, with time series or other diagnostics showing that the quantities of interest have stopped drifting?

**Why it matters.** Starting coordinates bias any average that includes the early part of a run. A simulation shorter than the time needed to cross the relevant barriers several times cannot give equilibrium populations, and no analysis of a trajectory can reveal states it never visited. Sampling cannot be proven adequate; diagnostics can only show where it is not.

**Resolved by.** The discarded equilibration period stated and justified, for example by time series of energies, box size and slow structural measures; the observable behind the claim plotted against simulation time; an estimate of the number of statistically independent samples, from autocorrelation or block averaging; a statement of the timescale of the process compared with the simulated time, and enhanced sampling used when the process is out of reach of plain MD.

**Benchmark.** [1], [4], [6]

## 4. Independent replicas and starting conditions

**Question.** How many independent simulations were run for each system or condition, how were they started (different velocities, different starting structures), and do the conclusions hold in each of them?

**Why it matters.** Runs that differ only in initial velocities, numerical precision or hardware can follow different paths through a rugged energy landscape, so a conclusion drawn from a single trajectory is often not reproduced. Frames from one trajectory are correlated and do not count as independent samples, and replicas begun from the same experimental structure are themselves partly correlated.

**Resolved by.** Several independent replicas per condition, started from varied structures where possible; the observable or event behind the claim reported for each replica, not only pooled; uncertainty estimated from the spread between replicas; a comparison between systems (such as wild type and mutant) shown to exceed the differences between replicas of the same system.

**Benchmark.** [1], [6], [7]

## 5. Collective variables and bias in enhanced sampling

**Question.** For enhanced sampling, does the paper state the method and its parameters, justify the collective variables (the coordinates along which the bias acts) as capturing the slow motions of the process, and show how the bias was removed and the result checked for convergence?

**Why it matters.** Methods that bias chosen collective variables work only as well as those variables capture the slow degrees of freedom; when a slow motion is left out, the free energy surface converges poorly, and enhanced sampling does not by itself guarantee convergence. Reweighting recovers unbiased averages only where the biased and unbiased ensembles overlap well. In replica exchange, the replicas are correlated in ways that standard error estimates do not handle.

**Resolved by.** The collective variables, bias parameters and deposition or exchange settings listed; evidence that the result does not depend on the choice of variables, for example from a different set of variables or from unbiased runs started at the end states; the free energy profile shown as it evolves with simulation time, or from independent runs; for replica exchange, acceptance rates and round trips across the replica ladder.

**Benchmark.** [1], [6], [8]

## 6. Populations, free energies and pathways from few transitions

**Question.** When the paper reports relative populations, free energies, rates or a pathway, how many transitions between the states were observed, is the claim supported by more than one or a few events, and, if the result comes from steered or otherwise driven simulations, how far from equilibrium was the driving?

**Why it matters.** A ratio of populations reflects a free energy difference only if the simulation has reached equilibrium between the states or contains many transitions, and estimates built from a handful of transitions are inaccurate. A single observed event shows that a route is possible in the model, but not that it is the main route or that its rate is right. Driven simulations, such as pulling along a chosen coordinate, do not sample an equilibrium ensemble, and free energies from their work values converge slowly because the rare low-work events dominate the average.

**Resolved by.** The number of observed transitions in each direction reported; populations or free energies obtained from runs with repeated crossings, or from enhanced sampling with reweighting, and given with uncertainties; a pathway claim supported by several independent events or by a method that samples the transition ensemble, and its rate compared with experiment where possible; for driven simulations, the pulling rate stated and the result shown not to change when the driving is made slower; snapshots presented as typical accompanied by the distribution of the relevant measure over all trajectories.

**Benchmark.** [1], [6], [8]

## 7. Comparison with experiment

**Question.** Does the paper compute from the simulations quantities that can be compared directly with measurements (for example nuclear magnetic resonance (NMR) observables, small-angle X-ray scattering (SAXS) profiles, Förster resonance energy transfer (FRET) distances or binding data), state the forward model used to calculate them, and report the agreement for the full set of available data?

**Why it matters.** Experiments measure averages over many molecules and over time, so single structures or short stretches of trajectory are not expected to match them, and the comparison needs the ensemble average of the measured quantity. The formulas that back-calculate experimental observables from structures are approximate and have their own errors. When experimental data are used to restrain or reweight a simulation, agreement with those same data does not test the result.

**Resolved by.** Observables averaged over the simulated ensemble and compared with experiment, with the forward model and its expected error named; agreement shown for data that were not used to build or refine the ensemble, or by cross-validation; disagreement reported and discussed rather than omitted; new or published experiments that test a prediction specific to the proposed mechanism.

**Benchmark.** [1], [2], [9], [10]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | Editorial, Reliability and reproducibility checklist for molecular dynamics simulations, Commun. Biol. 6, 268 (2023) | doi:10.1038/s42003-023-04653-0 |
| 2 | K. Lindorff-Larsen et al., Systematic validation of protein force fields against experimental data, PLoS ONE 7, e32131 (2012) | doi:10.1371/journal.pone.0032131 |
| 3 | P. Robustelli et al., Developing a molecular dynamics force field for both folded and disordered protein states, Proc. Natl. Acad. Sci. USA 115, E4758–E4766 (2018) | doi:10.1073/pnas.1800690115 |
| 4 | E. Braun et al., Best practices for foundations in molecular simulations, Living J. Comput. Mol. Sci. 1, 5957 (2018); read as the author manuscript in PubMed Central (PMC6884151) | doi:10.33011/livecoms.1.1.5957 |
| 5 | V. Martins de Oliveira et al., Constant pH molecular dynamics simulations: current status and recent applications, Curr. Opin. Struct. Biol. 77, 102498 (2022); read as the author manuscript in PubMed Central (PMC9933785) | doi:10.1016/j.sbi.2022.102498 |
| 6 | A. Grossfield et al., Best practices for quantification of uncertainty and sampling quality in molecular simulations, Living J. Comput. Mol. Sci. 1, 5067 (2019); read in PubMed Central (PMC6286151) | doi:10.33011/livecoms.1.1.5067 |
| 7 | B. Knapp et al., Avoiding false positive conclusions in molecular simulation: the importance of replicas, J. Chem. Theory Comput. 14, 6127 (2018) | doi:10.1021/acs.jctc.8b00391 |
| 8 | J. Hénin et al., Enhanced sampling methods for molecular dynamics simulations, Living J. Comput. Mol. Sci. 4, 1583 (2022); read as preprint arXiv:2202.04164 | doi:10.33011/livecoms.4.1.1583 |
| 9 | W. Boomsma et al., Combining experiments and simulations using the maximum entropy principle, PLoS Comput. Biol. 10, e1003406 (2014) | doi:10.1371/journal.pcbi.1003406 |
| 10 | T. Fröhlking et al., Refinement of molecular dynamics ensembles using experimental data and flexible forward models, J. Chem. Phys. 158, 214120 (2023); read as preprint arXiv:2303.09372 | doi:10.1063/5.0151163 |
