---
id: T-CALORIMETRY-JETS
name: Calorimetry, jets and missing energy
type: technique
field: physics/particle
applies_when: the paper measures energies with calorimeters, reconstructs or calibrates jets, uses missing transverse momentum, or bases a claim on a jet energy scale or resolution, a jet or missing-momentum spectrum, an invariant mass built from jets, or a correction for pile-up
version: "0.1"
---

# Calorimetry, jets and missing energy

Calorimeter measurements at colliders are used to claim the energies of particles and of jets (collimated sprays of hadrons), and through them invariant masses, cross-sections and the missing transverse momentum (MET, the momentum imbalance in the plane transverse to the beam) attributed to undetected particles. These claims rest on the jet energy scale (JES) and jet energy resolution (JER), on the definition of the jet, and on how energy from additional simultaneous collisions (pile-up) is removed.

## 1. Calorimeter response to hadrons

**Question.** How was the calorimeter calibrated for hadrons as opposed to electrons and photons, and does the paper show that the hadronic or jet response is linear over the energy range of the claim, or correct for its non-linearity?

**Why it matters.** In most calorimeters a hadron gives a smaller and more variable signal than an electron of the same energy, because part of its energy goes into nuclear break-up and is not seen. The electromagnetic fraction of a hadron shower grows with energy and fluctuates from shower to shower, so the hadron response is non-linear and non-Gaussian, and calibration constants derived with one kind of particle or at one energy bias the signal of another. A response that also depends on the particle type and on where the shower starts adds to this.

**Resolved by.** The calibration particles and energies stated for each calorimeter section; the hadron or jet response shown as a function of energy, with any weighting or simulation-based correction for non-compensation described; the energy resolution given with its stochastic and constant terms for the conditions used; checks of the hadronic scale with in situ physics samples rather than only with electrons.

**Benchmark.** [1]

## 2. Jet definition and the reference level

**Question.** Does the paper state the jet algorithm, its radius parameter, the recombination scheme and the inputs (calorimeter clusters, particle-flow objects or tracks), and is the algorithm infrared and collinear safe? Are results corrected to, and compared with predictions at, a stated particle (hadron) level?

**Why it matters.** A jet is only defined together with its algorithm, parameters and recombination scheme; changing any of them changes the measured energy. Algorithms that are not infrared and collinear safe give predictions that diverge or lose meaning at some order of perturbation theory. Hadronisation shifts the jet momentum roughly as the inverse of the radius while the underlying event and pile-up add roughly as its square, and a parton is not a well-defined object, so corrections to parton level depend on the model.

**Resolved by.** A complete jet definition with radius and inputs; an infrared and collinear safe algorithm, or a stated reason for another; the radius chosen with its sensitivity to hadronisation and soft contamination in mind; results corrected to a particle-level definition that a theorist can reproduce, with any parton-level correction and its model dependence stated separately.

**Benchmark.** [2], [3]

## 3. Jet energy scale calibration and its range

**Question.** Which jet energy scale calibration was applied, does it match the jet collection, pile-up conditions and kinematic range of the analysis, and how were its uncertainty components and their correlations carried into the result?

**Why it matters.** The jet energy scale is set in stages: a pile-up offset, a correction from simulation to the particle-level jet, and residual corrections from data that balance jets against well-measured objects (photons, Z bosons, other jets). Each stage holds for a particular jet type, detector region and momentum range, and beyond the reach of the in situ methods the uncertainty rests on other inputs, such as the measured response to single hadrons. The full uncertainty has many components with different correlations across momentum and rapidity, and reduced sets lose part of that correlation information.

**Resolved by.** The calibration named, with the jet collection and data-taking period it was derived for; the momentum and rapidity range of the claim shown to lie within the in situ calibrated range, or the method used beyond that range and its uncertainty stated; the JES uncertainty propagated as separate components with their correlations, and the reduced set named where one is used; for claims that rest on a peak position or a steeply falling spectrum, the shift from a one-standard-deviation change of the scale shown.

**Benchmark.** [4], [5]

## 4. Flavour and topology dependence of the response

**Question.** Does the flavour composition (quark, gluon, heavy-flavour) and event topology of the analysis sample differ from that of the samples used to calibrate the jet energy scale, and is the corresponding uncertainty evaluated for the analysis sample?

**Why it matters.** Gluon jets contain more, softer particles than quark jets and give a lower calorimeter response, while jets from b and c quarks can carry neutrinos. The in situ calibration samples have a particular quark–gluon mixture, so a sample rich in gluon or heavy-flavour jets inherits a residual bias. The gluon response is also the part that event generators predict least consistently.

**Resolved by.** The flavour composition of the analysis sample estimated and compared with that of the calibration samples; flavour composition and response uncertainties evaluated for that composition, not taken from a default; a dedicated heavy-flavour scale and uncertainty where the claim rests on b or c jets; generator dependence of the response checked with more than one parton shower and hadronisation model.

**Benchmark.** [4], [5]

## 5. Jet energy resolution in data and simulation

**Question.** Was the jet energy resolution measured in data, and was the simulation corrected to match it, with the resolution uncertainty propagated into the result?

**Why it matters.** Resolution sets the width of mass peaks and the migration of events between bins of a steeply falling spectrum, so a simulation with the wrong resolution gives the wrong acceptance, background shape and unfolding. The resolution in data is usually measured from the momentum balance in dijet and photon-plus-jet events, sometimes with the noise from pile-up and electronics measured separately, and it differs from simulation by factors that depend on rapidity.

**Resolved by.** The resolution in data stated as a function of momentum and rapidity, with the method used to measure it; simulation smeared, or otherwise corrected, by the measured data-to-simulation factors; the resolution uncertainty, including the noise term, propagated to the final result; for claims about peak widths or spectral shapes, a check of how the result changes with the resolution.

**Benchmark.** [1], [4], [5]

## 6. Pile-up subtraction and residual dependence

**Question.** How was energy from pile-up removed from jets and from the missing transverse momentum (area-based subtraction, charged-hadron subtraction, per-particle weighting or a pile-up jet identifier), and does the paper show that the results do not depend on the number of pile-up interactions?

**Why it matters.** Subtracting the median pile-up density times the jet area removes the average shift but not the fluctuations, which grow with the jet area and worsen the resolution; it also applies only to infrared safe jet algorithms, for which jet areas can be defined. Track-based methods work only within the tracker, so jets made entirely of pile-up are more frequent at large rapidity, and data-to-simulation agreement for pile-up jet identification is poorer there. Methods tuned for one observable can perform worse for another.

**Resolved by.** The mitigation method and its working point stated; key quantities (jet response, resolution, efficiency and the observable itself) shown in bins of the number of reconstructed vertices or of the mean number of interactions, with a residual offset near zero; the treatment of jets outside the tracker described, with the rate of pile-up jets estimated in data; for large-radius jets and substructure, a method suited to them.

**Benchmark.** [3], [6], [7], [8]

## 7. Missing transverse momentum: definition, scale and resolution

**Question.** How was the missing transverse momentum built (from which objects, how the energy not clustered into objects was treated, and whether the jet calibration was propagated to it), and were its scale and resolution measured in data, for example from the hadronic recoil in Z boson or photon events?

**Why it matters.** Missing transverse momentum is the negative vector sum of everything measured, so any miscalibration, threshold or inefficiency in jets, leptons or soft energy appears in it. If the jet corrections are not propagated, it is inconsistent with the calibrated jets. Its resolution grows with pile-up and with the total activity in the event, so a simulation that does not reproduce these conditions gives the wrong tails.

**Resolved by.** The definition stated, with the objects, thresholds and soft term used and the jet corrections propagated; the response and resolution measured in events without genuine missing momentum, such as Z boson or photon plus jets, and compared with simulation as a function of recoil and of the number of vertices; uncertainties from the jet scale and resolution and from the unclustered energy propagated to the result.

**Benchmark.** [5], [8], [9]

## 8. Instrumental sources of missing momentum

**Question.** How were events with spurious missing transverse momentum removed (calorimeter noise, dead or noisy channels, beam halo, badly measured muons or jets), and does the paper show that the tail of the distribution in the signal region agrees with the expected background after this cleaning?

**Why it matters.** Detector noise, non-collision backgrounds and badly reconstructed objects produce events with large missing momentum that simulation does not model, and they populate exactly the tails where signals of undetected particles are sought. A missing-momentum value alone does not say whether it is compatible with resolution effects; a significance built from the event's resolution can separate genuine from spurious imbalance.

**Resolved by.** The event filters and jet quality requirements stated, with their efficiency and rate of wrongly rejected events; distributions of missing momentum and of jet direction shown before and after cleaning, compared with simulation in control samples; where used, the missing-momentum significance defined and its distribution checked in events without genuine missing momentum.

**Benchmark.** [9]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | R. Wigmans, New developments in calorimetric particle detection, Prog. Part. Nucl. Phys. 103, 109–161 (2018); read as arXiv:1807.03853 | doi:10.1016/j.ppnp.2018.07.003 | full text | Sec. 2.2: energy lost to nuclear binding is invisible and fluctuates, so hadron signals are smaller and more variable than electron signals. Sec. 4.1: the electromagnetic fraction grows with energy, so a non-compensating calorimeter is non-linear for hadrons, with asymmetric response functions, a resolution term from non-compensation, and dependence on particle type and shower start. Sec. 6.1: calibration constants must depend on energy and particle type, otherwise non-linearity results |
| 2 | M. Cacciari, G. P. Salam and G. Soyez, The anti-kt jet clustering algorithm, JHEP 04, 063 (2008); read as arXiv:0802.1189 | doi:10.1088/1126-6708/2008/04/063 | abstract | Abstract: anti-kt behaves like an idealised cone with conical soft jets and equal active and passive areas, and is an infrared and collinear safe replacement for collinear-unsafe cone algorithms |
| 3 | G. P. Salam, Towards jetography, Eur. Phys. J. C 67, 637–686 (2010); read as arXiv:0906.1833 | doi:10.1140/epjc/s10052-010-1314-6 | full text | Sec. 2: algorithm, parameters and recombination scheme together form a jet definition. Sec. 2.1.4: unsafe algorithms break the cancellation of divergences, so predictions fail beyond some order (Table 1). Sec. 4.1.2 and 4.2: partons cannot be rigorously defined, so parton-level corrections are often ill-defined. Secs. 4.3, 4.4 and 5.1.1: hadronisation shift scales roughly as 1/R, underlying event and pile-up as R squared, and jet areas are infrared unsafe except for anti-kt |
| 4 | ATLAS Collaboration (G. Aad et al.), Jet energy scale and resolution measured in proton–proton collisions at √s = 13 TeV with the ATLAS detector, Eur. Phys. J. C 81, 689 (2021); read as arXiv:2007.02645 | doi:10.1140/epjc/s10052-021-09402-3 | full text | Sec. 5 and Fig. 2: calibration chain of pile-up correction, simulation-based calibration, global sequential calibration, eta-intercalibration, Z/photon+jet and multijet balance. Sec. 5.1.3: gluon jets have more, softer particles and a lower calorimeter response. Sec. 5.3: flavour composition and response uncertainties depend on the gluon fraction, gluon response differs between generators, separate b-jet term; above the multijet reach a single-hadron response term is used. Sec. 5.3.1: 125 nuisance parameters, reduced sets lose correlation information. Secs. 6.1 to 6.4: resolution from dijet balance, noise term from random cones, simulation smeared to data |
| 5 | CMS Collaboration (V. Khachatryan et al.), Jet energy scale and resolution in the CMS experiment in pp collisions at 8 TeV, J. Instrum. 12, P02014 (2017); read as arXiv:1607.03663 | doi:10.1088/1748-0221/12/02/P02014 | full text | Secs. 4 to 6: pile-up offset, simulated response and residual corrections from dijet, Z/photon+jet and multijet balance. Sec. 7.3: flavour uncertainty arises when the analysis sample's flavour mixture differs from that of the Z/photon+jet calibration; generators agree for quark jets and differ for gluon jets. Sec. 8: resolution measured with dijet asymmetry and photon+jet balance, with rapidity-binned data-to-simulation scale factors. Sec. 9: uncertainty sources and their correlations in momentum and rapidity |
| 6 | M. Cacciari and G. P. Salam, Pileup subtraction using jet areas, Phys. Lett. B 659, 119–126 (2008); read as arXiv:0707.1378 | doi:10.1016/j.physletb.2007.09.077 | full text | Sec. 2: the pile-up density is the median of momentum over area across jets in each event, and each jet is corrected by area times density; the method applies only to infrared safe jet algorithms. Sec. 3: residual jet-by-jet fluctuations remain. Sec. 4: a full validation needs experimentally realistic tests |
| 7 | G. Soyez, Pileup mitigation at the LHC: a theorist's view, Phys. Rep. 803, 1–158 (2019); read as arXiv:1801.09721 | doi:10.1016/j.physrep.2019.01.007 | full text | Secs. 2.1 and 2.2: subtracting the density times area corrects the average shift but fluctuations growing with the jet area remain; quality judged by a residual offset near zero across pile-up conditions and by the dispersion. Ch. 6 to 8: grooming for large-radius jets. Ch. 11 and 12: charged-track based and other particle-level methods |
| 8 | CMS Collaboration (A. M. Sirunyan et al.), Pileup mitigation at CMS in 13 TeV data, J. Instrum. 15, P09018 (2020); read as arXiv:2003.00503 | doi:10.1088/1748-0221/15/09/P09018 | full text | Sec. 1: an area-based correction acts on the whole jet and cannot remove pile-up from jet shape or substructure observables. Sec. 5.1: resolution against number of interactions, with the better method depending on region and jet size. Sec. 5.3: track-based variables exist only within the tracker; beyond its coverage the fraction of jets from the primary vertex falls to about 18% at 50 interactions, and data-to-simulation scale factors for pile-up jet identification depart from unity by up to about 30%. Sec. 7: missing-momentum resolution against number of vertices |
| 9 | CMS Collaboration (A. M. Sirunyan et al.), Performance of missing transverse momentum reconstruction in proton-proton collisions at √s = 13 TeV using the CMS detector, J. Instrum. 14, P07004 (2019); read as arXiv:1903.06078 | doi:10.1088/1748-0221/14/07/P07004 | full text | Sec. 4.2: jet corrections propagated to missing momentum to correct for calorimeter non-linearity and thresholds; jet scale and resolution uncertainties. Sec. 7: calorimeter noise and beam halo produce spurious high missing momentum; filters remove most of it, after which data and simulation agree. Sec. 9: scale and resolution from hadronic recoil in Z and photon events, resolution growing with vertices. Sec. 10: significance separates genuine missing momentum from resolution effects |
