---
id: T-TRACKING-PID
name: Tracking and particle identification
type: technique
field: physics/particle
applies_when: the paper reconstructs charged-particle tracks or vertices, applies track, vertex or particle identification selections, quotes tracking efficiency, fake rate, momentum scale or resolution, vertex resolution or misidentification rates, or bases a claim on identified hadrons, leptons or displaced vertices
version: "0.1"
---

# Tracking and particle identification

Tracking reconstructs the paths of charged particles from hits in a detector in a magnetic field, giving their momenta and the positions of primary and displaced vertices; particle identification (PID) assigns each track a species, such as pion, kaon, proton, electron or muon, from energy loss (dE/dx), time of flight, Cherenkov light or the response of calorimeters and muon chambers. Claims built on them rest on efficiencies, fake and misidentification rates, momentum scales and resolutions that are usually taken from simulation and corrected with data.

## 1. Track reconstruction efficiency measured in data

**Question.** How is the tracking efficiency defined (which particles count, in which acceptance, and by what hit-matching rule between simulated particles and tracks), and is it measured in data, for example with a tag-and-probe method, in the momentum, angular and occupancy range of the analysis instead of being taken from simulation alone?

**Why it matters.** An efficiency from simulation depends on the matching rule and on how well the detector, its inactive modules and its occupancy are modelled, and differences between data and simulation can depend on momentum, pseudorapidity, track multiplicity and the number of simultaneous collisions (pileup). Tag-and-probe measurements usually use muons, which do not undergo hadronic interactions, so they do not by themselves give the efficiency for pions, kaons or protons.

**Resolved by.** The matching rule and acceptance stated; the efficiency, or the ratio of data to simulation, measured in data in bins of momentum, pseudorapidity and multiplicity or pileup that cover the analysis sample, with simulation reweighted to the observed multiplicity; a separate uncertainty for hadrons from hadronic interactions and the material description; the per-track correction and its uncertainty multiplied through for final states with several tracks.

**Benchmark.** [1], [2]

## 2. Fake and lost tracks in busy events

**Question.** What fraction of the selected tracks are fake (not made by one particle), how does that fraction change with the track-quality selection and with pileup, and, where tracks are close together as in the cores of energetic jets, how many tracks are lost and is that loss measured in data?

**Why it matters.** Fake tracks come from random combinations of hits and become more frequent as occupancy rises, and the quality selections that suppress them also remove some real tracks. Where particles are close together, their hits merge or are shared and tracks are lost, so an efficiency measured on isolated tracks does not hold inside dense jets.

**Resolved by.** The fake rate stated for the quality selection used and for the pileup of the data; the trade-off between efficiency and fake rate shown when the selection is tightened or loosened; for dense environments, a data-driven estimate of the fraction of lost tracks, for example from merged clusters, with its uncertainty and a comparison with simulation.

**Benchmark.** [1], [3]

## 3. Material description

**Question.** How well does the simulated detector material match the real detector, how was this checked in data, and how does the uncertainty on the material enter the hadron tracking efficiency, the resolution and the energy-loss corrections used in the analysis?

**Why it matters.** Hadronic interactions in the detector material are a main cause of lost hadron tracks and the largest source of secondary particles, and the material also sets multiple scattering and energy loss. Simulated geometries can miss components or place them wrongly, so an efficiency or resolution taken from simulation inherits any error in the material model.

**Resolved by.** The material model checked against data, for example by mapping hadronic-interaction vertices and photon conversions, or by the rate at which track segments extend through the detector; disagreements found and corrected or covered by an uncertainty; the material uncertainty propagated into the hadron tracking efficiency and stated per track.

**Benchmark.** [1], [2], [4]

## 4. Momentum scale, alignment and charge-dependent biases

**Question.** How are the momentum scale and resolution calibrated and checked in data, for example with the masses of known resonances, are the checks made separately for the two charges and as a function of angle and momentum over the range of the claim, and how is the tracker alignment constrained against distortions that the track residuals do not reveal?

**Why it matters.** Some coherent distortions of the tracker barely change the hit residuals that alignment minimises, yet bias the measured curvature with opposite sign for positive and negative particles, which shifts reconstructed masses with charge, angle and azimuth. The magnetic field map and the treatment of energy loss also bias the momentum, and a scale fixed at one mass or momentum range need not hold at another.

**Resolved by.** Reconstructed resonance masses, for example of the J/psi, Upsilon or Z, shown against pseudorapidity, azimuth and charge, with the residual variation stated; alignment that uses constraints sensitive to these distortions, such as resonance masses or cosmic-ray tracks; the momentum resolution measured in data and compared with simulation; the scale and resolution uncertainties carried into any mass, momentum or energy on which the claim rests, including at momenta beyond the calibration resonances.

**Benchmark.** [1], [5], [6]

## 5. Primary vertices, displaced vertices and pileup

**Question.** How are vertex efficiency, position resolution and impact-parameter resolution determined in data, how are merging and splitting of nearby vertices under pileup handled, and how often is the wrong primary vertex chosen for the collision of interest?

**Why it matters.** As pileup grows, nearby collisions merge into one reconstructed vertex or one collision splits into two, so the number of vertices stops being proportional to the number of collisions, and tracks are assigned to the wrong collision. The vertex chosen for the hard collision, often the one with the largest summed squared track momentum, is sometimes a pileup vertex, most often for final states with few or soft charged particles.

**Resolved by.** The vertex resolution measured in data, for example by splitting each vertex's tracks into two halves and comparing the fitted positions, with the pull widths stated; vertex efficiency, merging, splitting and fake rates given as a function of pileup; the probability of choosing the wrong primary vertex given for the final state studied; impact-parameter resolution compared between data and simulation where lifetime or displacement information enters the claim.

**Benchmark.** [1], [7]

## 6. Particle identification performance from calibration samples

**Question.** Are the PID efficiency and misidentification rates taken from data calibration samples in which the particle species is known from the decay kinematics without any PID requirement, are those samples background-subtracted, and are they binned in momentum, pseudorapidity and occupancy and reweighted to match the signal sample?

**Why it matters.** PID detectors are hard to simulate well, and their response depends on momentum, angle, event occupancy and running conditions such as alignment, temperature and gas pressure. A calibration sample has different kinematics and occupancy from the signal sample, so a single average efficiency, or one taken from a sample whose trigger or selection biased the PID variables, does not transfer.

**Resolved by.** The calibration decays named, for example D* to D0 pi with D0 to K pi, Lambda to p pi, K0S to pi pi and J/psi to mu mu, with the selection shown not to bias the PID variables; background removed by a fit to the parent mass; efficiencies and misidentification rates in bins of momentum, pseudorapidity and occupancy, reweighted to the signal kinematics; systematic uncertainties from the binning, from differences between calibration and signal samples and from the background subtraction; the kinematic range not covered by the calibration samples stated.

**Benchmark.** [8], [9]

## 7. Misidentification and the momentum range of separation

**Question.** For each pair of species that matters to the claim, does the paper give the identification efficiency together with the misidentification rate at the working point used, over the momentum range of the signal, and does it estimate the background that misidentified particles contribute to the result?

**Why it matters.** Each PID method separates species only over a limited momentum range: dE/dx bands cross, time-of-flight differences shrink below the timing resolution, and Cherenkov detectors have thresholds. Hadrons are taken for muons through decays in flight, showers that reach the muon system and random matching, and these rates depend on momentum and on how busy the event is. An efficiency quoted without the matching misidentification rate does not show how pure the identified sample is.

**Resolved by.** Efficiency and misidentification rate for each relevant species pair, at the chosen working point and as a function of momentum, measured on samples of known species; the momentum regions without separation stated and either excluded or treated as background; the contribution of misidentified particles to the signal region, estimated with data-driven rates and given with its uncertainty.

**Benchmark.** [6], [8], [9]

## 8. Tracks and vertices from displaced decays

**Question.** Where the claim depends on particles produced away from the collision point, such as the daughters of K0S or Lambda decays or of hypothesised long-lived particles, how do the track and vertex efficiencies change with production radius and transverse impact parameter, and is that dependence checked in data with displaced decays of known particles?

**Why it matters.** Standard track finding usually requires tracks to point back to the beam line and to have hits in the innermost layers, so its efficiency falls steeply for particles produced at larger radii. Dedicated passes for displaced tracks recover part of that efficiency but add many fake tracks and fake vertices, so an efficiency measured on prompt tracks, or taken from simulation alone, does not transfer to displaced tracks.

**Resolved by.** The track and vertex efficiencies given as a function of production radius or impact parameter over the range of the signal; the fake-track and fake-vertex rates of any displaced-tracking step, including their dependence on pileup; the efficiency checked in data with K0S, Lambda or similar decays across that radial range, with the difference from simulation covered by a stated uncertainty, for example from varying the material model.

**Benchmark.** [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | CMS Collaboration, Description and performance of track and primary-vertex reconstruction with the CMS tracker, JINST 9, P10009 (2014); read as preprint arXiv:1405.6569 | doi:10.1088/1748-0221/9/10/P10009 | full text | Abstract and Sec. 2: inefficiency mainly from hadronic interactions in the material; material in simulation checked with nuclear interactions and photon conversions. Sec. 4.4: fraction of fake tracks falls roughly exponentially with the number of layers with hits; loose, tight and high-purity selections trade efficiency against fake rate. Sec. 4.3: field map and propagator bias. Sec. 5: simulated particle and track associated when 75% of hits are shared; efficiency and fake rate defined. Sec. 5.1.2: pileup degrades efficiency and fake rate for low-momentum tracks. Sec. 5.1.3: tag-and-probe with Z to mu mu; small efficiency loss with pileup in data not reproduced by simulation. Sec. 6.1: split-vertex resolution, pull widths, vertex efficiency against pileup, and the balance between resolving and splitting nearby vertices |
| 2 | LHCb Collaboration, Measurement of the track reconstruction efficiency at LHCb, JINST 10, P02007 (2015); read as preprint arXiv:1408.1251 | doi:10.1088/1748-0221/10/02/P02007 | full text | Sec. 4: tag-and-probe with J/psi to mu mu, the probe reconstructed without the subdetector under test. Sec. 7: ratio of data to simulation in bins of momentum and pseudorapidity, simulation reweighted to the data track multiplicity, efficiency lower at higher multiplicity, poorer agreement at low momentum. Sec. 9: muons do not probe hadronic interactions, so hadrons carry an extra uncertainty from a 10% material uncertainty |
| 3 | ATLAS Collaboration, Performance of the ATLAS track reconstruction algorithms in dense environments in LHC Run 2, Eur. Phys. J. C 77, 673 (2017); read as preprint arXiv:1704.07983 | doi:10.1140/epjc/s10052-017-5225-7 | full text | Sec. 5.1: truth-matching probability defines good and fake tracks; fake fraction rises with pileup. Secs. 5.3 and 5.4: efficiency falls towards the jet axis because of merged and shared clusters; loosening the shared-cluster limit raises the fake count. Sec. 6: fraction of lost tracks in jet cores measured in data from pixel dE/dx with templates, with systematic uncertainties and a comparison with simulation |
| 4 | M. Aaboud et al. (ATLAS Collaboration), Study of the material of the ATLAS inner detector for Run 2 of the LHC, JINST 12, P12009 (2017); read as preprint arXiv:1707.02826 | doi:10.1088/1748-0221/12/12/P12009 | full text | Sec. 1: nuclear interactions with material are the largest source of secondaries, so tracking efficiency depends on the material model. Secs. 4 and 5: material measured with hadronic-interaction vertices, photon conversions and track-extension efficiency. Sec. 6: missing or misplaced components found in the simulated geometry and corrected. Sec. 7: uncertainties of the method |
| 5 | CMS Collaboration, Alignment of the CMS tracker with LHC and cosmic ray data, JINST 9, P06009 (2014); read as preprint arXiv:1403.2286 | doi:10.1088/1748-0221/9/06/P06009 | full text | Sec. 4.4: weak modes barely change the residuals; a twist biases the track curvature; cosmic rays and the Z mass used as constraints. Sec. 7: residual-based validation is largely insensitive to weak modes. Sec. 9.1: a twist-like mode shifts the Z mass with pseudorapidity with opposite sign for the two charges; Z mass against pseudorapidity varied by more than 5 GeV without the mass constraint and became nearly flat with it |
| 6 | CMS Collaboration, Performance of CMS muon reconstruction in pp collision events at sqrt(s) = 7 TeV, JINST 7, P10002 (2012); read as preprint arXiv:1206.4071 | doi:10.1088/1748-0221/7/10/P10002 | full text | Sec. 5.3: hadron misidentification as muons measured with pions, kaons and protons from K0S, Lambda and phi decays; causes are decays in flight, punch-through and random matching in busy events; momentum dependence. Sec. 6: momentum scale and resolution from J/psi and Z masses and from cosmic rays; Z peak varies with azimuth with opposite sign for the two charges, attributed to residual misalignment |
| 7 | ATLAS Collaboration, Reconstruction of primary vertices at the ATLAS experiment in Run 1 proton-proton collisions at the LHC, Eur. Phys. J. C 77, 332 (2017); read as preprint arXiv:1611.10235 | doi:10.1140/epjc/s10052-017-4887-5 | full text | Sec. 5.1: merged, split and fake vertices defined; hard-scatter vertex chosen by largest summed squared transverse momentum. Sec. 5.2: wrong-vertex rate depends on the final state, worst for soft charged particles. Sec. 6: split-vertex resolution measured in data and compared with simulation. Secs. 7 and 8: merging dominates at high pileup, so the vertex count is not linear in pileup |
| 8 | R. Aaij et al. (LHCb Collaboration), Selection and processing of calibration samples to measure the particle identification performance of the LHCb experiment in Run 2, EPJ Tech. Instrum. 6, 1 (2019); read as preprint arXiv:1803.00824 | doi:10.1140/epjti/s40485-019-0050-z | full text | Secs. 2 and 4: PID hard to simulate, so performance measured on decays whose kinematics identify the species without PID; response depends on momentum, occupancy and running conditions; selection must not bias the PID variables. Secs. 4 and 5: background subtracted with sPlot; efficiencies in bins of momentum, pseudorapidity and multiplicity, reweighted to the reference sample; systematic uncertainties from binning, sample differences and weights; limited kinematic coverage |
| 9 | C. Lippmann, Particle identification, Nucl. Instrum. Meth. A 666, 148–172 (2012); read as preprint arXiv:1101.3276 | doi:10.1016/j.nima.2011.03.009 | full text | Sec. 1.2: separation power defined; each method works only in a limited momentum range. Sec. 3.5: dE/dx bands lie close together near minimum ionisation so separation fails over a momentum range. Secs. 3.6 and 3.7.3: overlapping tracks and high occupancy degrade dE/dx resolution. Sec. 4.1: time-of-flight separation lost once the time difference approaches the timing resolution. Sec. 5: Cherenkov threshold. Sec. 2.3.3: muon identification efficiency quoted with its misidentification rate |
| 10 | G. Aad et al. (ATLAS Collaboration), Performance of the reconstruction of large impact parameter tracks in the inner detector of ATLAS, Eur. Phys. J. C 83, 1081 (2023); read as preprint arXiv:2304.12867 | doi:10.1140/epjc/s10052-023-12024-6 | full text | Secs. 1 and 5.1: standard tracking with strict pointing requirements loses efficiency for transverse impact parameters beyond 5 mm; large-radius tracking recovers part of it. Secs. 4.2 and 6.2: large-radius tracking produces many fake tracks, controlled by tighter selections; its fake fraction grows faster than linearly with pileup. Sec. 6.3: K0S vertices in data used as a standard candle against decay radius. Sec. 6.3.1: per-track efficiency uncertainty from material and physics-list variations covers the data-simulation difference |
