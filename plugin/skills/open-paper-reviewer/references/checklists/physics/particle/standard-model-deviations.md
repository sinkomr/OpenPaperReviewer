---
id: CL-STANDARD-MODEL-DEVIATIONS
name: Claims of deviations from the Standard Model
type: claim
field: physics/particle
applies_when: the paper reports an anomaly, tension or deviation between a measured quantity and its Standard Model prediction, quotes a significance for that difference, combines such differences in a global fit, or interprets them as a sign of new physics
version: "0.1"
---

# Claims of deviations from the Standard Model

## 1. The prediction and its uncertainty budget

**Question.** Which SM prediction is the measurement compared with, at what order in perturbation theory, and does the paper give its uncertainty broken down by source, including an estimate for the higher-order terms that were not calculated?

**Why it matters.** A prediction is a sum of contributions known with very different precision, and its uncertainty is often dominated by one or two of them, such as hadronic effects. Uncertainties from missing higher orders are usually estimated by varying unphysical scales over a conventional range, which has no probabilistic meaning and can be too narrow when the last known term happens to be small.

**Resolved by.** The prediction cited or derived, with its central value and an itemised uncertainty table; the contribution that dominates the uncertainty named; the method for missing higher orders stated, with a check that the conclusion survives a more generous estimate.

**Benchmark.** [1], [3], [4]

## 2. The measured and predicted quantities defined alike

**Question.** Is the measured quantity defined in the same way as the predicted one: the same region of phase space, the same treatment of radiated photons, and corrections for acceptance or efficiency whose dependence on the simulation used to derive them is stated?

**Why it matters.** A measurement corrected to a region the detector did not observe, or to an idealised level such as the process without radiation, relies on a theoretical model, usually through simulation, and the correction carries that model into the result. If the measurement and the calculation treat radiation or kinematic limits differently, the comparison can show a deviation that is not there or hide one that is.

**Resolved by.** The measured quantity defined in terms of observable final-state particles in a region close to what the detector accepts, with the prediction computed for the same definition; any extrapolation or correction to an idealised level stated, with the model used for it and the uncertainty it adds; radiated photons treated the same way in the measurement and in the prediction.

**Benchmark.** [3], [10]

## 3. Non-perturbative and data-driven inputs

**Question.** Where the prediction uses non-perturbative inputs, from lattice quantum chromodynamics (QCD), dispersion relations built on experimental data, or models, does the paper show whether independent determinations of those inputs agree, and how much the size of the deviation changes from one determination to another?

**Why it matters.** Non-perturbative inputs often set the precision of the prediction. Data-driven evaluations can rest on experimental data sets that disagree with each other beyond their quoted uncertainties, and lattice results differ in how well they control the continuum limit, the volume and the quark masses. The spread between groups that use different approximations can understate the true uncertainty if the groups share an error.

**Resolved by.** The source of each non-perturbative input named; independent determinations compared, with the deviation quoted against each where they differ; tensions among the input data sets stated and covered by an enlarged uncertainty; lattice inputs taken from results, or averages, that meet stated quality criteria for the continuum limit, finite volume and quark masses.

**Benchmark.** [1], [2], [3]

## 4. Inputs independent of the tested effect

**Question.** Are the SM parameters that enter the prediction (couplings, masses, mixing-matrix elements) taken from measurements that the claimed new effect would leave unchanged, and does the paper say which observables were used to fix them?

**Why it matters.** If an input parameter is fitted to observables that a new effect would also shift, the fit can absorb part of the effect and hide or distort the deviation. A test for new physics in one class of processes is therefore entangled with how the SM parameters were determined.

**Resolved by.** A list of the observables used to fix each input; inputs taken from processes that the new effect is assumed not to touch, with that assumption stated; the result shown not to depend on including or excluding observables that the new effect could alter; input uncertainties propagated into the prediction.

**Benchmark.** [3], [5]

## 5. How the theoretical uncertainty enters the significance

**Question.** How is the theoretical uncertainty combined with the experimental one to give the quoted significance (as a Gaussian error, as a range for an unknown bias, or by another model), and does the paper show how the significance changes with that choice?

**Why it matters.** A theoretical uncertainty is not the spread of a random variable and can only be modelled. Different reasonable models of it give different p-values and significances for the same difference. When one uncertainty dominates, underestimating it lowers the true significance sharply: if it is too small by a factor of two, a quoted five standard deviations is about two and a half.

**Resolved by.** The model for each theoretical uncertainty stated, with the separate sources kept apart where possible; the significance given under at least one alternative treatment; the size of the increase in the theoretical uncertainty that would remove the tension stated, so that a reader can judge whether it is plausible.

**Benchmark.** [6], [7]

## 6. Global significance across the observables examined

**Question.** How many observables, bins, channels or ratios were compared with the SM in arriving at the deviation, was that set fixed before the comparison, and does the paper give a significance that accounts for all of them as well as the largest single one?

**Why it matters.** When many quantities are compared with predictions, some are expected to differ by several standard deviations by chance alone. Reporting the most discrepant observable, or a subset chosen after seeing the data, overstates the evidence. The relevant set may extend beyond the paper to all the analyses of the same data, and differences of three or four standard deviations have often faded with more data.

**Resolved by.** The full set of observables compared stated, with the criterion that chose it; a global significance, or a goodness of fit to all of them, quoted next to the local one; the result of a global fit shown to be stable when observables are added or removed; the wording of the claim (evidence or observation) matched to the global significance.

**Benchmark.** [3], [7]

## 7. Consistency with other measurements of the same quantity

**Question.** Does the paper compare its result with all other measurements of the same quantity, state whether they are mutually consistent, and account for correlations between them when combining them or quoting a combined deviation?

**Why it matters.** A deviation seen by one experiment and not by others with comparable precision points to an unrecognised effect in one of them as readily as to new physics. Averages of inconsistent measurements need an enlarged uncertainty, and a hidden effect in one input can move the central value of the average. Shared data or shared systematic uncertainties make results less independent than they appear.

**Resolved by.** Other measurements of the same quantity shown alongside the new one, including those that see no deviation; a compatibility test across them; any combination made with the correlations between shared systematic sources and overlapping data stated, and with the uncertainty enlarged where the inputs disagree; the dependence of the combined deviation on any single input shown.

**Benchmark.** [3], [8]

## 8. Related observables and the interpretation

**Question.** Where the deviation is interpreted as new physics, does the paper check the interpretation against other observables that the same new effect would change, and does it weigh that interpretation against an unrecognised experimental or theoretical effect?

**Why it matters.** A physical model of new physics, or an effective field theory, predicts correlated deviations in other processes, and an interpretation is credible only if it is consistent with the whole data set. An explanation that fits one observable while ignoring others that constrain the same couplings is not tested. The less expected the new physics, the more likely an unnoticed systematic effect is the cause.

**Resolved by.** The observables that the proposed effect would also change named, with their measured values shown to be consistent with it, preferably in a global fit; the parameters of the interpretation shown not to be excluded by other data; experimental and theoretical explanations within the SM listed and addressed before new physics is invoked.

**Benchmark.** [3], [7], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | T. Aoyama et al., The anomalous magnetic moment of the muon in the Standard Model, Phys. Rep. 887, 1 (2020); read as arXiv:2006.04822 | doi:10.1016/j.physrep.2020.07.006 |
| 2 | S. Aoki et al., Review of lattice results concerning low-energy particle physics, Eur. Phys. J. C 77, 112 (2017); read as arXiv:1607.00299 | doi:10.1140/epjc/s10052-016-4509-7 |
| 3 | T. R. Junk and L. Lyons, Reproducibility and replication of experimental particle physics results, Harvard Data Sci. Rev. 2(4) (2020); read as arXiv:2009.06864 | doi:10.1162/99608f92.250f995b |
| 4 | M. Cacciari and N. Houdeau, Meaningful characterisation of perturbative theoretical uncertainties, JHEP 09 (2011) 039; read as arXiv:1105.5152 | doi:10.1007/JHEP09(2011)039 |
| 5 | J. Charles et al., Future sensitivity to new physics in Bd, Bs and K mixings, Phys. Rev. D 89, 033016 (2014); read as arXiv:1309.2293 | doi:10.1103/PhysRevD.89.033016 |
| 6 | J. Charles et al., Modeling theoretical uncertainties in phenomenological analyses for particle physics, Eur. Phys. J. C 77, 214 (2017); read as arXiv:1611.04768 | doi:10.1140/epjc/s10052-017-4767-z |
| 7 | L. Lyons, Discovering the significance of 5 sigma, arXiv:1310.1284 (2013) | doi:10.48550/arXiv.1310.1284 |
| 8 | J. Erler and R. Ferro-Hernández, Alternative to the application of PDG scale factors, Eur. Phys. J. C 80, 541 (2020); read as arXiv:2004.01219 | doi:10.1140/epjc/s10052-020-8115-3 |
| 9 | I. Brivio and M. Trott, The Standard Model as an effective field theory, Phys. Rep. 793, 1 (2019); read as arXiv:1706.08945 | doi:10.1016/j.physrep.2018.11.002 |
| 10 | C. Bierlich et al., Robust Independent Validation of Experiment and Theory: Rivet version 3, SciPost Phys. 8, 026 (2020); read as arXiv:1912.05451 | doi:10.21468/SciPostPhys.8.2.026 |
