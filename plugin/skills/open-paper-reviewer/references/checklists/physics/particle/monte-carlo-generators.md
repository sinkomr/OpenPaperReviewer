---
id: T-MONTE-CARLO-GENERATORS
name: Monte Carlo generators and detector simulation
type: technique
field: physics/particle
applies_when: the paper uses Monte Carlo event generators or detector simulation to predict signals or backgrounds, correct data for detector effects, derive efficiencies or acceptances, or compare a measurement with theory, or relies on a generator tune or simulation-based modelling uncertainty
version: "0.1"
---

# Monte Carlo generators and detector simulation

## 1. Generator setup stated

**Question.** For each simulated sample, does the paper state the generator and its version, the perturbative order of the hard-scattering calculation, the matching or merging scheme and its parameters, the parton distribution function (PDF) set, the shower and hadronisation model, and the tune?

**Why it matters.** A prediction depends on choices of scales, matching criteria, approximation and phenomenological model, and these choices interact. A tune is fitted for a particular generator version and PDF set, so the same tune used with a different PDF set or version may no longer describe the data it was fitted to. Without these details the simulation cannot be repeated and its known shortcomings cannot be judged.

**Resolved by.** A table of samples giving, for each process, the generator and version, order, matching or merging scheme with its scale settings, PDF set, shower and hadronisation model, tune and normalisation cross-section with its source; any non-default parameters listed; the fraction of negative weights and the effective sample size given.

**Benchmark.** [1], [2]

## 2. Origin and independence of the tune

**Question.** Which data were the tune and any other adjusted parameters fitted to, do those data overlap with the distributions later used to validate the simulation or to make the measurement, and is an uncertainty on the tuned parameters propagated?

**Why it matters.** A tune is a fit with subjectively chosen weights for the observables, and it leaves known discrepancies in observables the model cannot describe; parameters may also be weakly constrained. Agreement with the data used in the fit does not test the simulation where it is used to extrapolate, which is where tune uncertainties matter most.

**Resolved by.** The tune and the data behind it named; validation shown on distributions not used in the tune; the observables relevant to the analysis checked against the tune's known discrepancies; tune uncertainties propagated, for example through variation or eigenvector tunes, rather than the central tune alone.

**Benchmark.** [1], [2], [3]

## 3. Perturbative and PDF variations

**Question.** Which variations are used for the uncertainty of the generator prediction: renormalisation and factorisation scales in the hard process and the shower, the PDF and the strong coupling, the matching and merging parameters and the shower starting scale; and how is each one evaluated?

**Why it matters.** Scale variations alone can understate the shower uncertainty, and terms away from the singular limits give a separate, sometimes larger, contribution. Scale and PDF variations can be carried as event weights, but the shower starting scale and tune parameters cannot and need separate samples, which are often left out because of their cost. PDF and strong-coupling uncertainties follow prescriptions that differ between sets given as replicas and sets given as eigenvectors, and a single combined PDF set may not suffice for precision measurements or when data and prediction disagree.

**Resolved by.** A list of every variation with its range (for example factors of two in the scales, with the combinations used); PDF and strong-coupling uncertainties computed with the prescription of the PDF set and combined as it recommends; shower and matching variations included, by weights where possible and by separate samples otherwise; the size of each variation shown for the observables the claim rests on.

**Benchmark.** [1], [4], [5]

## 4. Choice of model and comparisons between generators

**Question.** Where an uncertainty is taken from the difference between two generators, two shower or hadronisation models or two detector physics models, does the paper say what the difference is meant to cover, and how it enters the fit (as a nuisance parameter, with what correlation across bins and regions)?

**Why it matters.** The choice of phenomenological model is the hardest modelling uncertainty to quantify, and a difference between two models is not a confidence interval. Varying one source up and down at a time does not map out correlated effects, and constraint terms placed on theoretical uncertainties lack a clear frequentist interpretation. A claimed deviation from the Standard Model needs all these modelling uncertainties to have been considered.

**Resolved by.** Each model comparison named, with an argument for why the models span the plausible range; the treatment in the statistical model stated, including whether the difference is symmetrised, how it is interpolated and whether it is correlated across bins and regions; the result shown to be stable, or the uncertainty enlarged, when an additional model is tried.

**Benchmark.** [1], [6], [7]

## 5. Detector simulation fidelity and corrections from data

**Question.** For the objects and variables the analysis uses, how was the detector simulation validated against data, which corrections derived from data (efficiencies, energy scales and resolutions, pile-up profile) were applied to simulation, and, where a fast or parametrised simulation was used, was it validated for those variables?

**Why it matters.** Simulated hadronic calorimeter response can agree with data to a few per cent while shower shapes and resolution agree only to 10 to 20 per cent, and the material description is approximate. Fast simulations reproduce kinematic quantities well but are less reliable for internal structure, identification variables and unusual signatures such as displaced or late decays. The way pile-up is modelled has its own limits.

**Resolved by.** Data and simulation compared for each object's efficiency, scale and resolution, with the corrections and their uncertainties stated; pile-up reweighting described; any fast or parametrised simulation compared with full simulation or data for the variables the claim uses, with any difference carried as an uncertainty; for unusual signatures, evidence that the simulation's assumptions hold.

**Benchmark.** [7], [8]

## 6. Control regions and extrapolation to the signal region

**Question.** Where simulation is normalised or checked in control regions, are those regions free of signal, close in kinematics to the signal region, and separate from the regions used to validate the result; and how is the extrapolation from control to signal region justified and given an uncertainty?

**Why it matters.** A control-region estimate is as trustworthy as its assumptions: little signal in the control region, no unmodelled backgrounds there, and a known transfer factor to the signal region. When the transfer factor comes from simulation, the simulation's modelling uncertainty returns through it. Agreement in a region whose normalisation was fitted there says little about the extrapolation.

**Resolved by.** Each control and validation region defined, with its expected signal contamination and purity; the transfer factor's source stated and its modelling uncertainties propagated; the simulation shown to describe validation regions between the control and signal regions in the variables the claim uses; where the background is extrapolated from data, for example with two variables and four regions, the factorisation tested in validation regions; control and signal regions fitted together where signal contamination is not negligible.

**Benchmark.** [6]

## 7. Particle-level definitions and model dependence of corrections

**Question.** When results are corrected for detector effects or extrapolated beyond the detector acceptance, is the target defined in terms of stable final-state particles in a fiducial region, and is the dependence of the correction on the generator assessed?

**Why it matters.** Quantities internal to a generator, such as the parton-level history, are unphysical and differ between generators, so a result defined by them depends on the generator used. Extrapolation into regions the detector does not observe makes the result depend on the model that supplies it.

**Resolved by.** A fiducial definition in terms of stable particles that matches the detector acceptance; any extrapolation beyond it reported separately, with its model uncertainty; the correction repeated with an alternative generator or with reweighted simulation, and the difference included; the analysis logic made available, for example as preserved analysis code, so others can compare new predictions.

**Benchmark.** [1], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | J. M. Campbell et al., Event generators for high-energy physics experiments, SciPost Phys. 16, 130 (2024); read as arXiv:2203.11110v4 | doi:10.21468/SciPostPhys.16.5.130 |
| 2 | P. Skands et al., Tuning PYTHIA 8.1: the Monash 2013 Tune, Eur. Phys. J. C 74, 3024 (2014) | doi:10.1140/epjc/s10052-014-3024-y |
| 3 | A. Buckley et al., Systematic event generator tuning for the LHC, Eur. Phys. J. C 65, 331 (2010); read as arXiv:0907.2973 | doi:10.1140/epjc/s10052-009-1196-7 |
| 4 | S. Mrenna and P. Skands, Automated parton-shower variations in Pythia 8, Phys. Rev. D 94, 074005 (2016); read as arXiv:1605.08352 | doi:10.1103/PhysRevD.94.074005 |
| 5 | R. D. Ball et al., The PDF4LHC21 combination of global PDF fits for the LHC Run III, J. Phys. G 49, 080501 (2022); read as arXiv:2203.05506 | doi:10.1088/1361-6471/ac7216 |
| 6 | K. Cranmer, Practical statistics for the LHC, in Proceedings of the 2011 European School of High-Energy Physics, CERN-2014-003, pp. 267–308 (2014); read as arXiv:1503.07622 (2015) | doi:10.48550/arXiv.1503.07622 |
| 7 | HEP Software Foundation, J. Apostolakis, M. Asai, S. Banerjee et al., HEP Software Foundation Community White Paper Working Group – Detector Simulation, HSF-CWP-2017-07, arXiv:1803.04165 (2018) | doi:10.48550/arXiv.1803.04165 |
| 8 | The ATLAS Collaboration (G. Aad et al.), The ATLAS simulation infrastructure, Eur. Phys. J. C 70, 823 (2010); read as arXiv:1005.4568 | doi:10.1140/epjc/s10052-010-1429-9 |
| 9 | C. Bierlich et al., Robust independent validation of experiment and theory: Rivet version 3, SciPost Phys. 8, 026 (2020) | doi:10.21468/SciPostPhys.8.2.026 |
