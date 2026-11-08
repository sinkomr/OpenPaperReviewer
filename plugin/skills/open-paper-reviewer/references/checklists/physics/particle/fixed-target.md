---
id: T-FIXED-TARGET
name: Fixed-target and beam-dump experiments
type: technique
field: physics/particle
applies_when: the paper searches for new particles made by a proton or electron beam on a fixed target or in a beam dump, through decays or scattering behind a shield or a resonance in the products, or normalizes a yield or limit to particles on target
version: "0.1"
---

# Fixed-target and beam-dump experiments

## 1. Beam exposure

**Question.** How was the number of beam particles on target measured (which beam-intensity monitor, how it was calibrated and how stable it was), what is the uncertainty of the quoted POT or EOT, and which spill-quality selections define the exposure?

**Why it matters.** Every expected signal yield, and therefore every limit on a coupling, scales directly with the exposure. Beam-intensity monitors such as current transformers or toroids need an absolute calibration and a check of long-term stability, and spills with abnormal beam conditions have to be removed in the same way from the exposure and from the data.

**Resolved by.** The monitor named, with its calibration method, stability and the resulting exposure uncertainty, which is typically a few per cent; the spill or beam-quality criteria stated and applied identically to exposure and data; the exposure uncertainty propagated into the yield or limit; where possible, a cross-check of the normalization against a known process recorded in the same data.

**Benchmark.** [1], [2]

## 2. Production in the target or dump

**Question.** Which production processes are included for the proposed particle (meson decays, bremsstrahlung, direct production, production by secondary particles in a thick target), which model and external data set each production rate and spectrum, and how large is the uncertainty assigned to them, including that from where the beam actually strikes?

**Why it matters.** The expected signal depends on the spectra of the parent mesons or of the radiating beam particles, and different production treatments for the same model can differ by large factors. In a thick target, secondary and re-interacting particles contribute a large part of the flux and are a leading source of its uncertainty. If part of the beam strikes material other than the nominal target or dump, the produced spectra change, and this can dominate the flux uncertainty.

**Resolved by.** Each production channel listed with the generator or calculation behind it; hadron production tuned to measured data on a matching target material and beam energy, with the phase space not covered by data stated; the effect of secondary interactions in the target included; a theory uncertainty for each production model, for example from varying form factors or comparing approximations; beam position, size and alignment measured and their effect on the flux propagated; the production model checked against a measured rate where one is available.

**Benchmark.** [1], [3], [4], [5]

## 3. Muons and punch-through from the dump

**Question.** How are the muons produced in the dump, and hadrons that pass through the absorber (punch-through), prevented from faking a signal, and is the simulated flux of these particles checked against a measurement?

**Why it matters.** A proton dump produces a very large muon flux from the decays of pions, kaons and short-lived resonances, and muons that scatter in or interact with material near the detector can create neutral long-lived particles whose decays look like the signal. The background estimate relies on a simulation of this flux, and measured muon rates can differ from simulation by tens of per cent, with larger differences between simulation codes at high momentum.

**Resolved by.** The absorber, magnetic or passive shield and active vetoes described, with their measured or simulated efficiency; the simulated muon and hadron flux compared with a measurement made with the same kind of target, with a correction or added uncertainty where they differ; muon-induced backgrounds evaluated with that validated flux.

**Benchmark.** [2], [6]

## 4. Neutrino-induced backgrounds

**Question.** How are interactions of neutrinos from the dump in the detector, in the decay volume and in nearby material estimated and suppressed, and are these estimates checked with data?

**Why it matters.** Neutrino interactions in material upstream of or inside the decay volume produce neutral long-lived particles whose decays can mimic a signal, so the residual gas in the decay volume and the material around it matter. In searches for scattering of new particles in a detector, neutrino scattering gives the same signature and can limit proton-dump searches unless it is reduced by beam configuration, timing or kinematics.

**Resolved by.** The pressure in the decay volume and the material near it stated, with taggers or vetoes for interactions upstream; the neutrino flux and cross-sections used for the estimate stated with their uncertainties; the neutrino background constrained in situ with control samples, such as charged-current or neutral-current events away from the signal region; any beam configuration or timing selection used to reduce it described and its effect measured.

**Benchmark.** [3], [6], [7], [8]

## 5. Backgrounds unrelated to the beam

**Question.** How is the background from cosmic rays and other sources unrelated to the beam measured, and how is it scaled to the beam-on live time?

**Why it matters.** A surface or shallow detector sees cosmic muons, neutrons and their secondaries at a rate that can exceed any signal unless vetoes and timing remove them. An estimate scaled from a prototype or from another site depends on the overburden and the detector, and is weaker than a measurement made with the detector itself.

**Resolved by.** Beam-off data, random triggers or a time window before the spill used to measure the beam-unrelated rate in the same detector and selection; the scaling to the beam-on live time stated; veto efficiencies measured; the timing relation between the beam spill and the event window given.

**Benchmark.** [3], [8]

## 6. Background estimates at the level of a few events

**Question.** For a search that expects few or no background events, how many beam particles did the background simulation represent compared with the exposure, how was the result extrapolated, and are random coincidences of unrelated tracks included?

**Why it matters.** Simulating showers in a thick dump is expensive, so background samples often represent far fewer beam particles than the experiment received, and the estimate then rests on scaling or extrapolation whose assumptions can fail. Random combinations of tracks from different particles in the same time window can form a fake vertex or pair and become a dominant background at high rates.

**Resolved by.** The simulated exposure stated next to the real one; any scaling, biasing or extrapolation described with a test of its validity and an uncertainty; the background estimate also derived from data, for example from control regions or loosened selections; the time resolution, the coincidence window and the expected rate of random coincidences stated, with the vertex or timing requirements that reject them.

**Benchmark.** [6], [8], [10]

## 7. Acceptance and decay probability

**Question.** How was the signal acceptance computed: the angular and energy distribution of the produced particle, the probability that it decays inside the decay volume for each lifetime, the acceptance for its decay products and the reconstruction efficiency, and are all of these shown across the claimed mass and coupling range?

**Why it matters.** The number of signal events is a product of production, geometric acceptance, decay probability and decay-product acceptance. The decay probability depends on the lab-frame decay length, so the excluded region is bounded on one side by too few particles produced and on the other by decays inside the shield. Simplified geometry, an approximate angular and energy distribution or an assumed acceptance for the decay products can move either boundary, and estimates from different groups for the same experiment can differ for these reasons.

**Resolved by.** The full chain from production to reconstructed signal described, with the geometry of target, shield and decay volume; the decay-product acceptance and reconstruction efficiency computed from a detector simulation, not assumed; the acceptance shown as a function of mass and lifetime; both boundaries of the excluded region explained in terms of production and decay length; the model conventions, couplings and widths stated so the result can be reinterpreted.

**Benchmark.** [5], [9]

## 8. Target thickness and normalization to a reference process

**Question.** For a thin-target measurement or search, how were the target thickness and density, the beam attenuation in the target, the beam composition and the interactions outside the target accounted for, and is the signal normalized to a reference process recorded in the same data?

**Why it matters.** A rate per target nucleus needs the areal density of the target, a correction for the beam attenuated in the target and a subtraction of interactions in material other than the target, which is measured with the target removed. For a secondary beam, the fraction of the wanted particle type must be measured. Expressing the signal relative to a known process, such as quantum electrodynamics (QED) trident production in the same acceptance and mass window, reduces the dependence on luminosity and acceptance.

**Resolved by.** The target material, thickness, density and fraction of an interaction or radiation length stated; the attenuation correction and the empty-target subtraction quantified; beam particle identification and purity stated; where a reference process is used, its expected rate compared with the observed one and the ratio used to set the signal scale; the effect of the target thickness on backgrounds such as photon conversion stated.

**Benchmark.** [9], [10], [11]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | K. Abe et al. (T2K Collaboration), T2K neutrino flux prediction, Phys. Rev. D 87, 012001 (2013); read as arXiv:1211.0469 | doi:10.1103/PhysRevD.87.012001 |
| 2 | C. Ahdida et al. (SHiP Collaboration), Measurement of the muon flux from 400 GeV/c protons interacting in a thick molybdenum/tungsten target, Eur. Phys. J. C 80, 284 (2020); read as arXiv:2001.04784, which carries a different title | doi:10.1140/epjc/s10052-020-7788-y |
| 3 | A. A. Aguilar-Arevalo et al. (MiniBooNE-DM Collaboration), Dark matter search in nucleon, pion, and electron channels from a proton beam dump with MiniBooNE, Phys. Rev. D 98, 112004 (2018); read as arXiv:1807.06137 | doi:10.1103/PhysRevD.98.112004 |
| 4 | S. Foroughi-Abari and A. Ritz, Dark sector production via proton bremsstrahlung, Phys. Rev. D 105, 095045 (2022); read as arXiv:2108.05900 | doi:10.1103/PhysRevD.105.095045 |
| 5 | M. Ovchynnikov et al., Sensitivities to feebly interacting particles: public and unified calculations, Phys. Rev. D 108, 075028 (2023); read as arXiv:2305.13383 | doi:10.1103/PhysRevD.108.075028 |
| 6 | M. Anelli et al. (SHiP Collaboration), A facility to Search for Hidden Particles at the CERN SPS, technical proposal CERN-SPSC-2015-016 (2015) | doi:10.48550/arXiv.1504.04956 |
| 7 | G. Lanfranchi et al., The search for feebly interacting particles, Annu. Rev. Nucl. Part. Sci. 71, 279 (2021); read as arXiv:2011.02157 | doi:10.1146/annurev-nucl-102419-055056 |
| 8 | M. Battaglieri et al. (BDX Collaboration), Dark matter search in a Beam-Dump eXperiment at Jefferson Lab, proposal to the Jefferson Lab Program Advisory Committee, arXiv:1607.01390 (2016) | doi:10.48550/arXiv.1607.01390 |
| 9 | J. D. Bjorken et al., New fixed-target experiments to search for dark gauge forces, Phys. Rev. D 80, 075018 (2009); read as arXiv:0906.0580 | doi:10.1103/PhysRevD.80.075018 |
| 10 | R. Essig et al., An electron fixed target experiment to search for a new vector boson A′ decaying to e+e−, J. High Energy Phys. 2011, 009 (2011); read as arXiv:1001.2557 | doi:10.1007/JHEP02(2011)009 |
| 11 | N. Abgrall et al. (NA61/SHINE Collaboration), Measurements of cross sections and charged pion spectra in proton-carbon interactions at 31 GeV/c, Phys. Rev. C 84, 034604 (2011); read as arXiv:1102.0983 | doi:10.1103/PhysRevC.84.034604 |
