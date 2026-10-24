---
id: T-MONTE-CARLO-GENERATORS
name: Monte Carlo generators and detector simulation
type: technique
field: physics/particle
applies_when: the paper uses Monte Carlo event generators or detector simulation to predict signals or backgrounds, correct data for detector effects, derive efficiencies or acceptances, or compare a measurement with theory, or relies on a generator tune or simulation-based modelling uncertainty
version: "0.1"
---

# Monte Carlo generators and detector simulation

Monte Carlo (MC) event generators simulate collisions from the hard scattering through the parton shower, hadronisation and decays, and detector simulation models how the resulting particles are recorded. Papers rely on them to predict signal and background yields and shapes, to correct measurements for acceptance and detector effects, and to compare data with theory, so a claim is only as good as the modelling and its stated uncertainty.

## 1. Generator setup stated

**Question.** For each simulated sample, does the paper state the generator and its version, the perturbative order of the hard-scattering calculation, the matching or merging scheme and its parameters, the parton distribution function (PDF) set, the shower and hadronisation model, and the tune?

**Why it matters.** A prediction depends on choices of scales, matching criteria, approximation and phenomenological model, and these choices interact. A tune is fitted for a particular generator version and PDF set, so the same tune used with a different PDF set or version may no longer describe the data it was fitted to. Without these details the simulation cannot be repeated and its known shortcomings cannot be judged.

**Resolved by.** A table of samples giving, for each process, the generator and version, order, matching or merging scheme with its scale settings, PDF set, shower and hadronisation model, tune and normalisation cross-section with its source; any non-default parameters listed.

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

**Resolved by.** Each control and validation region defined, with its expected signal contamination and purity; the transfer factor's source stated and its modelling uncertainties propagated; the simulation shown to describe validation regions between the control and signal regions in the variables the claim uses; control and signal regions fitted together where signal contamination is not negligible.

**Benchmark.** [6]

## 7. Simulated sample size and event weights

**Question.** Are the simulated samples large enough in the bins and regions that matter, including the effective size after negative or large event weights, and is the statistical uncertainty of the simulated templates included in the result?

**Why it matters.** Full detector simulation is expensive, so template bins are often sparsely populated and the templates are themselves estimates with statistical uncertainty. Negative weights from next-to-leading-order matching sharply reduce statistical power: negative fractions of 25 and 40 per cent need about 4 and 25 times as many events for the same precision. Reweighted variations can carry occasional very large weights that make a variation fluctuate bin by bin.

**Resolved by.** The number of simulated events, or the effective number, given for the main samples, with the fraction of negative weights where relevant; the simulation's statistical uncertainty included in the fit, for example by per-bin nuisance parameters; variations checked for large-weight fluctuations, or smoothed with the method stated.

**Benchmark.** [1], [4], [6]

## 8. Particle-level definitions and model dependence of corrections

**Question.** When results are corrected for detector effects or extrapolated beyond the detector acceptance, is the target defined in terms of stable final-state particles in a fiducial region, and is the dependence of the correction on the generator assessed?

**Why it matters.** Quantities internal to a generator, such as the parton-level history, are unphysical and differ between generators, so a result defined by them depends on the generator used. Extrapolation into regions the detector does not observe makes the result depend on the model that supplies it.

**Resolved by.** A fiducial definition in terms of stable particles that matches the detector acceptance; any extrapolation beyond it reported separately, with its model uncertainty; the correction repeated with an alternative generator or with reweighted simulation, and the difference included; the analysis logic made available, for example as preserved analysis code, so others can compare new predictions.

**Benchmark.** [1], [9]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | J. M. Campbell, M. Diefenthaler, T. J. Hobbs, S. Höche, J. Isaacson, F. Kling, S. Mrenna, J. Reuter et al., Event generators for high-energy physics experiments, SciPost Phys. 16, 130 (2024); read as arXiv:2203.11110v4 | doi:10.21468/SciPostPhys.16.5.130 | full text | Sec. 3.3 introduction: generator parameters include scales, matching criteria and the approximation used, plus phenomenological model parameters and the choice of model, all interdependent. Sec. 3.3.1: compact representations of tune uncertainties such as eigentunes. Sec. 3.3.3: tune uncertainties matter most when simulation extrapolates; three classes of uncertainty, with the choice of model the hardest to quantify; all must be considered before concluding that data disagree with the Standard Model. Sec. 4.7.3: negative-weight fractions of about 25% and 40% need about 4 and 25 times as many events. Sec. 4.7.4: scale and PDF variations as event weights; shower starting-scale and tune variations need separate samples |
| 2 | P. Skands, S. Carrazza and J. Rojo, Tuning PYTHIA 8.1: the Monash 2013 Tune, Eur. Phys. J. C 74, 3024 (2014) | doi:10.1140/epjc/s10052-014-3024-y | full text | Abstract and Secs. 3.1, 3.2 and 3.4: the tune is released with a specific generator version and tuned together with a specific PDF set, and the sampling of multi-parton interactions follows the PDF choice. Secs. 2.2, 2.3, 3.3 and 3.5: remaining discrepancies in identified-particle, heavy-flavour and strange-baryon observables and in the Z transverse momentum. Sec. 1.1: a blanket theory uncertainty added to guard against overfitting |
| 3 | A. Buckley, H. Hoeth, H. Lacker, H. Schulz and J. E. von Seggern, Systematic event generator tuning for the LHC, Eur. Phys. J. C 65, 331–357 (2010); read as arXiv:0907.2973 | doi:10.1140/epjc/s10052-009-1196-7 | full text | Sec. 4.3: observable weights in a tune are subjective, and the result should not depend too strongly on them. Sec. 5.2: parameter uncertainties from the fit; best-fit values outside the sampled range point to a problem with the physics model. Sec. 5.3: run-combination and weight variations test the stability of the tune and guard against overtuning. Sec. 6.4: weakly constrained parameters. Sec. 6.5: covariance eigenvectors give the directions of largest and smallest uncertainty. Sec. 6.6: the spread between run combinations exceeds the fit uncertainties |
| 4 | S. Mrenna and P. Skands, Automated parton-shower variations in Pythia 8, Phys. Rev. D 94, 074005 (2016); read as arXiv:1605.08352 | doi:10.1103/PhysRevD.94.074005 | full text | Sec. 1: fixed-order uncertainties are assessed by scale and PDF variations, while shower and non-perturbative variations traditionally need separate runs. Sec. 2.5: variations of non-singular terms complement scale variations and can give larger, more realistic uncertainties away from the singular limits. Sec. 2 introduction: variation weights accumulate over the shower and a rare branching can give one event a very large weight, so variations should be monitored bin by bin |
| 5 | R. D. Ball et al., The PDF4LHC21 combination of global PDF fits for the LHC Run III, J. Phys. G 49, 080501 (2022); read as arXiv:2203.05506 | doi:10.1088/1361-6471/ac7216 | full text | Sec. 6.1: the combined set suits searches and lower-precision observables, while precision measurements should use individual sets, and a large disagreement between data and prediction calls for examining individual sets. Sec. 6.3: prescriptions for PDF uncertainties from Monte Carlo replicas and Hessian eigenvectors, and for combining PDF and strong-coupling uncertainties in quadrature |
| 6 | K. Cranmer, Practical statistics for the LHC, in Proceedings of the 2011 European School of High-Energy Physics, CERN-2014-003, pp. 267–308 (2014); read as arXiv:1503.07622 (2015) | doi:10.48550/arXiv.1503.07622 | full text | Sec. 2.2: a control region constrains the background through an extrapolation factor and assumes no signal there. Sec. 2.4: constraint terms on theoretical uncertainties lack a frequentist interpretation. Sec. 4.1.3: shower, hadronisation and detector-simulation parameters varied up and down one at a time, which does not map out correlated effects. Sec. 4.1.7: sparsely populated simulated templates are estimates with statistical uncertainty, handled by per-bin nuisance parameters. Sec. 4.2: a data-driven estimate rests on assumptions such as negligible signal and no other backgrounds in the control region, which may be violated; taking the extrapolation ratio from simulation makes it a hybrid that again depends on simulation |
| 7 | HEP Software Foundation, J. Apostolakis, M. Asai, S. Banerjee et al., HEP Software Foundation Community White Paper Working Group – Detector Simulation, HSF-CWP-2017-07, arXiv:1803.04165 (2018) | doi:10.48550/arXiv.1803.04165 | full text | Sec. 7.1: observed data-simulation differences in electromagnetic shower widths. Sec. 7.2: simulated hadronic response agrees with data to a few per cent, shower shapes and resolution to 10–20%; several hadronic physics models used to estimate systematic effects. Sec. 5: limitations of data overlay and simulated minimum-bias approaches to pile-up. Sec. 10.2: fast simulation agrees with full simulation for kinematic quantities but less for structure and identification variables, and exotic signatures such as displaced vertices break its assumptions |
| 8 | The ATLAS Collaboration (G. Aad et al.), The ATLAS simulation infrastructure, Eur. Phys. J. C 70, 823–874 (2010); read as arXiv:1005.4568 | doi:10.1140/epjc/s10052-010-1429-9 | full text | Secs. 4 and 4.1: dead material such as cables and cooling is approximated, and a layout with added material was built to study the effect of a poor material description on jet resolution and missing transverse energy. Sec. 5.4: alternative physics lists with different hadronic and electromagnetic models. Sec. 6.2: pile-up and background overlay. Sec. 7: the frozen-shower option suits processes that do not need very accurate calorimeter modelling. Sec. 7.2: the fastest option smears truth objects without modelling efficiencies or fakes. Sec. 7.5: fast simulations compared with full simulation, with differences in jet resolution and hadronic shower properties |
| 9 | C. Bierlich, A. Buckley, J. M. Butterworth et al., Robust independent validation of experiment and theory: Rivet version 3, SciPost Phys. 8, 026 (2020) | doi:10.21468/SciPostPhys.8.2.026 | full text | Sec. 1: fiducial measurements matched to the detector acceptance avoid large theory-based extrapolation and the model dependence it brings. Sec. 3.4.1: objects defined from stable final-state particles, not the unphysical, generator-dependent parton-level history. Sec. 3.5: analysis phase spaces designed to limit extrapolation. Secs. 1 and 1.1: preserved analysis routines give predictions directly comparable with published data, used to validate and tune generators |
