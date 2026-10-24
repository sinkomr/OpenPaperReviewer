---
id: T-NEUTRINO-OSCILLATIONS
name: Neutrino oscillation experiments
type: technique
field: physics/particle
applies_when: the paper measures neutrino oscillation parameters with accelerator, reactor or atmospheric neutrinos, compares near and far detector spectra, reconstructs neutrino energy from final-state particles, or claims a preference for a mass ordering, CP violation or a value of the CP phase
version: "0.1"
---

# Neutrino oscillation experiments

Oscillation experiments compare the number and energy spectrum of neutrinos of a given flavour at a far detector with the prediction for no oscillation, often constrained by a near detector, and use the difference to claim values of the mixing angles, the mass-squared differences, the neutrino mass ordering (normal or inverted) and the charge-parity (CP) violating phase δCP. Every such claim rests on a predicted flux, a model of neutrino–nucleus interactions, and an estimate of the neutrino energy from the particles seen in the detector.

## 1. Flux prediction

**Question.** How was the unoscillated flux predicted for each flavour and, for a beam, each focusing polarity: which hadron-production measurements constrain the simulation, what uncertainty is given to interactions those measurements do not cover, and how large are the wrong-sign and intrinsic electron-neutrino components? For a reactor experiment, how far does the result depend on a predicted spectrum rather than a measured one?

**Why it matters.** Simulated hadron production disagrees with data, and the external data sets can disagree with one another, so a beam flux is only as good as the measurements used to tune it; interactions outside those measurements carry large assigned uncertainties, and beam focusing and alignment dominate in parts of the spectrum. Predicted reactor spectra carry uncertainties of several per cent or more, and measured spectra have shown features the predictions did not contain.

**Resolved by.** The constraining data sets named and the flux uncertainty broken down by source, with correlations between energy bins and flavours given as a covariance; the wrong-sign and intrinsic electron-neutrino fractions stated with their uncertainties; an independent in situ check of the flux where one exists; for reactor experiments, a relative comparison between detectors of the same design, or a stated and realistic spectrum uncertainty where an absolute prediction is used.

**Benchmark.** [1], [2], [3]

## 2. Interaction model and its uncertainties

**Question.** Which neutrino–nucleus interaction models and event generator does the analysis use, which processes (quasi-elastic scattering, multinucleon knockout, pion production, final-state interactions) are varied in the systematic uncertainties and by how much, and was the analysis tested against models outside its own parametrisation?

**Why it matters.** Cross sections for individual channels on nuclear targets are known to only about 20 to 30 per cent, generators disagree with one another, and the model enters both the detection efficiency and the inferred neutrino energy. If the uncertainties span only one model, a process it lacks can be absorbed into the fit and bias the oscillation parameters, for example towards maximal mixing, while the fit still looks good.

**Resolved by.** The generator, its version and the models in it named; the uncertainty parameters listed with their prior and fitted values; systematic uncertainties that span the range of available models, not the variations of one model; the analysis repeated on simulated data made with alternative models, with the resulting shifts in the oscillation parameters compared with their uncertainties.

**Benchmark.** [1], [4], [8]

## 3. Extrapolation from near to far detector

**Question.** How are the near-detector data used to predict the far-detector spectrum, which uncertainties does the near detector constrain, and which remain because the two detectors differ in flux, acceptance, target nucleus or event selection?

**Why it matters.** Flux and cross-section uncertainties cancel between the detectors only in part. Each event rate is a product of flux and cross section, the far spectrum is reshaped by oscillation while the near spectrum is not, the near detector sees an extended source and the far detector a point source, and the target material, containment and backgrounds can differ. The extrapolation therefore still depends on the interaction model.

**Resolved by.** The extrapolation method stated (a far-to-near ratio, a joint fit or a model-based fit); the uncertainty on the far-detector prediction shown before and after the near-detector constraint; the differences in target, geometry and acceptance listed with how each is treated; the uncertainties that remain uncorrelated between the detectors stated; a check that the near-detector fit does not move model parameters to values outside their physical range.

**Benchmark.** [1], [5]

## 4. Electron and muon neutrinos, neutrinos and antineutrinos

**Question.** Where the near detector mostly records muon-neutrino interactions but the far-detector signal consists of electron neutrinos or antineutrinos, what uncertainty does the paper give to the ratio of electron- to muon-neutrino cross sections and of neutrino to antineutrino cross sections, on what is it based, and how are the backgrounds in the far-detector electron-neutrino sample predicted?

**Why it matters.** A near detector in a muon-neutrino beam cannot measure these ratios well, so they come from theory, which predicts differences from the lepton mass, radiative corrections and poorly known form factors. Neutrino and antineutrino events also differ in neutron content and nuclear effects, so an error in these ratios can imitate or hide a CP asymmetry. In some designs these ratios are among the largest systematic uncertainties on δCP. The far-detector sample also contains intrinsic beam electron neutrinos and neutral-current events in which photons from neutral pions are reconstructed as an electron, and these backgrounds are predicted with the same interaction model.

**Resolved by.** The uncertainties on the cross-section ratios listed with their source; separate parameters for electron and muon neutrinos and for neutrinos and antineutrinos, not one shared normalisation; any electron-neutrino sample in the near detector used as a check; the predicted signal and background composition of each far-detector sample given with its uncertainty; the effect on the δCP result shown when these uncertainties are enlarged.

**Benchmark.** [1], [4], [5], [6]

## 5. Neutrino energy reconstruction

**Question.** How is the neutrino energy estimated, from the lepton kinematics assuming quasi-elastic scattering or from the total visible energy, how are undetected neutrons, absorbed pions and particles below threshold accounted for, and what uncertainty is given to the energy scale and to the relation between true and reconstructed energy?

**Why it matters.** The kinematic formula holds only for quasi-elastic scattering; multinucleon events and events with an absorbed pion are assigned the wrong energy and move events into or out of the oscillation dip. Calorimetric reconstruction underestimates the energy when neutrons or mesons escape, and the correction for this comes from a model. A correction wrong by about 20 per cent can bias δCP noticeably without degrading the fit.

**Resolved by.** The estimator defined and the relation between true and reconstructed energy shown for each event sample and interaction channel; energy-scale uncertainties stated separately for leptons, charged hadrons and neutrons, and for neutrinos and antineutrinos; the effect of alternative nuclear models on the reconstructed spectrum and the fitted parameters shown; the hadronic energy response calibrated with test-beam or in situ samples.

**Benchmark.** [1], [7], [8]

## 6. Degeneracies, matter effects and external inputs

**Question.** Which external inputs does the result depend on, such as a reactor value of θ13, the matter density along the baseline or the solar parameters, and does the paper show how δCP, the octant of θ23 and the mass ordering are correlated, for example by giving results separately for each ordering?

**Why it matters.** Appearance rates depend jointly on δCP, θ23 and, through the matter effect, the mass ordering, so different combinations can predict similar event counts. A preference for one ordering or one range of δCP can come mainly from an external constraint, or from agreement between disappearance measurements in different channels, rather than from the appearance data.

**Resolved by.** Results given for both orderings and, where relevant, both octants; external inputs and their uncertainties stated, with results shown with and without each constraint; the matter density and its uncertainty given; joint confidence regions in two parameters, not only one-dimensional profiles.

**Benchmark.** [5], [9], [11]

## 7. Claims about the mass ordering

**Question.** When the paper states a preference for one mass ordering, how is its significance obtained, and does it separate the expected sensitivity from the observed result and report how compatible the data are with each ordering?

**Why it matters.** The two orderings are discrete hypotheses that are not nested, each with free parameters, so the difference in χ² between them does not follow a χ² distribution and its square root is not a significance in the usual sense. Its distribution depends on the true values of other parameters, such as δCP and θ23, and is non-Gaussian when the expected separation is small. A sensitivity computed from data without fluctuations describes a median experiment, not the observed result.

**Resolved by.** The test statistic defined; its distribution under each ordering obtained from pseudo-experiments when the expected separation is small; a p-value for each ordering, with an ordering rejected only if it is rejected for all allowed values of the other parameters; expected and observed results reported separately.

**Benchmark.** [10]

## 8. Claims about CP violation and the value of δCP

**Question.** How were the confidence intervals for δCP and the significance of excluding the CP-conserving values 0 and π obtained, and was their coverage checked with pseudo-experiments rather than read from χ² thresholds?

**Why it matters.** δCP enters the oscillation probabilities through bounded trigonometric functions, near the physical boundary of maximal θ23 mixing and together with the octant and ordering degeneracies, so its test statistic is far from a χ² distribution while the data constrain it weakly. Intervals from fixed thresholds then lack their stated coverage, and how strongly a value is excluded can change by about one standard deviation with the assumed true θ23 and ordering.

**Resolved by.** Intervals built from pseudo-experiments with a Feldman–Cousins or comparable construction; the dependence on the assumed true θ23 and ordering shown; the exclusion of CP conservation quoted together with how it was computed; joint regions in δCP and θ23 given as well as one-dimensional intervals.

**Benchmark.** [9], [11]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | L. Alvarez-Ruso, M. Sajjad Athar, M. B. Barbaro et al., NuSTEC White Paper: Status and challenges of neutrino-nucleus scattering, Prog. Part. Nucl. Phys. 100, 1–68 (2018); read as preprint arXiv:1706.03621 | doi:10.1016/j.ppnp.2018.01.006 | full text | Sec. II.2: electron- and muon-neutrino cross-section differences hard to measure in a beam with few electron neutrinos; neutron content differs between neutrinos and antineutrinos, which matters for δCP; detector efficiency depends on the nuclear model, so systematic errors should span the models. Sec. II.3: channel cross sections known to about 20 to 30 per cent. Sec. III.2: neutral-current neutral-pion events and intrinsic beam electron neutrinos are backgrounds to the electron-neutrino sample, and a missing process changes the predicted rate. Sec. III.3: near detector cancels flux and cross-section uncertainties only in part; oscillated far flux differs from near flux; extended versus point source; different targets and acceptance; beam flux uncertainties typically 10 to 20 per cent. Sec. III.4: kinematic method fails for non-quasi-elastic events; calorimetric method loses energy to neutrons and mesons. Sec. III.6.1: excess high-energy multinucleon events can push the fitted mixing towards maximal or unphysical values. Sec. IV.1: hadron production sculpts the beam flux |
| 2 | L. Aliaga, M. Kordosky, T. Golan et al. (MINERvA Collaboration), Neutrino flux predictions for the NuMI beam, Phys. Rev. D 94, 092005 (2016); read as preprint arXiv:1607.00704 | doi:10.1103/PhysRevD.94.092005 | full text | Sec. III: simulated hadron production tuned to thin- and thick-target data by reweighting; simulation agrees with data only to within about 40 per cent, the uncertainty given to interactions not covered by data; two thin-target data sets disagree by about 25 per cent where they overlap. Sec. V: thin- and thick-target predictions disagree and are not combined. Secs. II and IV to VI: hadron production dominates the flux uncertainty, focusing dominates on the falling edge; wrong-sign and electron-neutrino fractions of the beam; bin-to-bin covariance from many sampled universes; comparison with an in situ flux measurement |
| 3 | A. C. Hayes and P. Vogel, Reactor neutrino spectra, Annu. Rev. Nucl. Part. Sci. 66, 219–244 (2016); read as preprint arXiv:1605.02047 | doi:10.1146/annurev-nucl-102115-044826 | full text | Secs. 3, 7 and 8: conversion and summation predictions with uncertainties of about 5 and up to 20 per cent; forbidden decays a major source. Sec. 5: the observed excess near 5 MeV suggests 1 to 2 per cent uncertainty estimates are too optimistic. Sec. 1: near and far detectors of essentially identical design reduce dependence on absolute flux predictions |
| 4 | K. Mahn, C. Marshall and C. Wilkinson, Progress in measurements of 0.1–10 GeV neutrino–nucleus scattering and anticipated results from future experiments, Annu. Rev. Nucl. Part. Sci. 68, 105–129 (2018); read as preprint arXiv:1803.08848 | doi:10.1146/annurev-nucl-101917-020930 | full text | Sec. I: energy inference relies on the cross-section model, interaction-model uncertainty is a large part of the appearance systematic budget, and mis-modelling can bias oscillation parameters. Sec. VII: neutron multiplicity and energy differ greatly between generators. Sec. VIII: few electron-neutrino cross-section measurements, so models tuned to muon-neutrino data rely on theory for appearance |
| 5 | P. Coloma, P. Huber, J. Kopp and W. Winter, Systematic uncertainties in long-baseline neutrino oscillations for large θ13, Phys. Rev. D 87, 033004 (2013); read as preprint arXiv:1209.5973 | doi:10.1103/PhysRevD.87.033004 | full text | Sec. 2.3: flux errors correlated between near and far detectors; far-detector uncertainty includes near-to-far extrapolation; separate nuisance parameters for flavour ratios the near detector cannot measure; matter density uncertainty of 1 to 5 per cent. Secs. 3 and 5: the near detector constrains only the beam flavour, so the electron- to muon-neutrino cross-section ratio is an external input, and in some designs it dominates the δCP precision |
| 6 | M. Day and K. S. McFarland, Differences in quasielastic cross sections of muon and electron neutrinos, Phys. Rev. D 86, 053003 (2012); read as preprint arXiv:1206.6745 | doi:10.1103/PhysRevD.86.053003 | full text | Secs. III.1 to III.5: differences from kinematic limits, radiative corrections of order 10 per cent, the axial and pseudoscalar form factors and second-class currents, largest at low energy. Sec. IV: these differences enter oscillation measurements and are comparable to current systematic uncertainties; neutrino-antineutrino differences can produce apparent CP asymmetries |
| 7 | M. Martini, M. Ericson and G. Chanfray, Neutrino energy reconstruction problems and neutrino oscillations, Phys. Rev. D 85, 093012 (2012); read as preprint arXiv:1202.4745 | doi:10.1103/PhysRevD.85.093012 | full text | Sec. I: multinucleon events mimic quasi-elastic events without obeying the kinematic relation. Sec. II: the reconstructed and true energy distributions differ substantially once multinucleon events are included. Secs. III and IV: the smearing changes the shape of oscillation signals and must be checked for each experiment and detection method |
| 8 | A. M. Ankowski, P. Coloma, P. Huber, C. Mariani and E. Vagnoni, Missing energy and the measurement of the CP-violating phase in neutrino oscillations, Phys. Rev. D 92, 091301 (2015); read as preprint arXiv:1507.08561 | doi:10.1103/PhysRevD.92.091301 | full text | Introduction: escaping neutrons and undetected pions lower the calorimetric energy, and hadron content differs between neutrinos and antineutrinos. Figs. 1 and 2 and Summary: a missing-energy correction wrong by about 20 per cent biases δCP by about one standard deviation; near and far detectors may differ, so the correction relies on generators; the fit quality barely changes |
| 9 | I. Esteban, M. C. Gonzalez-Garcia, M. Maltoni, T. Schwetz and A. Zhou, The fate of hints: updated global analysis of three-flavor neutrino oscillations, JHEP 09, 178 (2020); read as preprint arXiv:2007.14792 | doi:10.1007/JHEP09(2020)178 | full text | Secs. 2.1 and 2.2: appearance predictions depend jointly on δCP, θ23 and the ordering through the matter term; accelerator data alone and the combined fit prefer different orderings, the combined preference coming from agreement of mass-squared differences between disappearance channels; role of the reactor θ13 constraint. Sec. 4: the δCP profile is non-Gaussian, so its precision is indicative only |
| 10 | M. Blennow, P. Coloma, P. Huber and T. Schwetz, Quantifying the sensitivity of oscillation experiments to the neutrino mass ordering, JHEP 03, 028 (2014); read as preprint arXiv:1311.1822 | doi:10.1007/JHEP03(2014)028 | full text | Secs. II.1 to II.3: the orderings are non-nested hypotheses, so Δχ² has no χ² interpretation; a composite ordering is rejected only if all its parameter values are; median sensitivity defined from a fluctuation-free data set. Secs. III and IV: Gaussian limit of the test statistic, dependence on true δCP and θ23, non-Gaussian distributions when the expected separation is small. Secs. II to IV: an observed outcome can reject one, both or neither ordering, and differs from the median sensitivity |
| 11 | J. Elevant and T. Schwetz, On the determination of the leptonic CP phase, JHEP 09, 016 (2015); read as preprint arXiv:1506.07685 | doi:10.1007/JHEP09(2015)016 | full text | Secs. 2 to 4.1: the δCP test statistic is strongly non-Gaussian because of weak constraints, the bounded dependence on sin δCP, the θ23 octant and boundary and the ordering; χ² thresholds do not give correct coverage, so Feldman–Cousins with pseudo-data is used. Secs. 4.1 and 4.3: rejection of δCP near π/2 ranges from about 2 to 3 standard deviations with the true θ23 and ordering; θ13 fixed to the reactor value, and adding data that prefer a smaller θ13 weakens the rejection; two-dimensional regions closer to the Gaussian limit |
