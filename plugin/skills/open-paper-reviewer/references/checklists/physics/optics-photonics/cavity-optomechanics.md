---
id: T-CAVITY-OPTOMECHANICS
name: Cavity optomechanics
type: technique
field: physics/optics-photonics
applies_when: the paper couples a mechanical mode to an optical or microwave cavity and reports a vacuum coupling rate, cooperativity, sideband cooling, a phonon occupancy or ground-state claim, motional sideband asymmetry, optomechanical thermometry, or the effect of laser or thermal noise on the mechanical mode
version: "0.1"
---

# Cavity optomechanics

Cavity optomechanics couples a mechanical mode to an optical or microwave cavity through radiation pressure, and is used to claim a vacuum optomechanical coupling rate (g0), a cooperativity, cooling of the mechanical mode by the red-detuned sideband to a stated mean phonon occupancy, operation near or in the quantum ground state, and quantum signatures such as an asymmetry between the Stokes and anti-Stokes motional sidebands. Each of these numbers is inferred from noise spectra of the light leaving the cavity, so it depends on how the detection is calibrated, on the temperature of the mode's bath, and on noise carried by the laser.

## 1. Vacuum coupling rate

**Question.** How was g0 determined: from a known frequency or phase modulation used to calibrate the detected cavity frequency noise, from a thermal calibration with an effective mass and a known temperature, or from simulation alone, and under what probe power and bath conditions?

**Why it matters.** The frequency shift per unit displacement and the effective mass are each fixed only once a displacement normalisation is chosen, so values built from them can differ by convention while g0 does not. A thermal calibration of g0 or of displacement assumes the mode holds the thermal energy of a known temperature and is not changed by dynamical backaction from the probe, and the transduction factor it yields belongs to one data set.

**Resolved by.** g0 measured with a calibration tone of known modulation depth applied to the laser, with the detection scheme, the ratio of mechanical to calibration peak and the noise bandwidth stated; the probe power low enough, or the detuning chosen, so that optical spring and damping are negligible during the calibration; the mode occupancy used in the calibration justified by a measurement at a stated bath temperature; where a displacement or effective mass is quoted, the mode shape and normalisation point stated; a simulated g0 compared with the measured one.

**Benchmark.** [1], [2], [3]

## 2. Intracavity photon number and cooperativity

**Question.** How were the intracavity photon number, the enhanced coupling and the cooperativity obtained from the input power, are the measured optical spring and optical damping as functions of detuning and power consistent with them, and is radiation pressure distinguished from photothermal forces?

**Why it matters.** The enhanced coupling scales with the square root of the intracavity photon number, which depends on the power that reaches the cavity, the external coupling fraction, the cavity linewidth and the detuning. Errors in any of these pass into the cooperativity and the predicted cooling. The optical spring and damping follow from the same parameters, so a mismatch between their measured and predicted values points to an error in one of them. Photothermal forces from absorbed light can also shift and damp the mode, mimicking the radiation-pressure response while adding heat and not supporting quantum-coherent coupling.

**Resolved by.** The input power stated at a named point with coupling losses measured; the cavity linewidth, external coupling fraction and detuning measured and given with uncertainties; the mechanical frequency shift and linewidth plotted against detuning or power and fitted together with one parameter set; any disagreement between fitted and independently measured parameters stated and its effect on the cooperativity given; the photothermal contribution to the spring and damping estimated or shown to be small, for example from its different dependence on detuning, power or modulation frequency.

**Benchmark.** [1], [4]

## 3. Bath temperature and absorption heating

**Question.** Does the paper show that the mechanical mode is in thermal equilibrium with the stated bath temperature when the cooling is weak, and how does it measure or bound heating of the mode and its surroundings by absorbed light?

**Why it matters.** The final occupancy depends on the thermal occupancy of the bath the mode is coupled to, and at millikelvin temperatures that bath can be much hotter than the cryostat because of optical absorption. Absorption heating grows with power, so the bath temperature measured at low power may not hold at the power used for cooling. A calibration that assumes the cryostat temperature then gives the wrong occupancy.

**Resolved by.** The occupancy measured at weak probing against cryostat temperature, showing that it follows the expected thermal occupancy over a range where the mode thermalises, with any departure stated and corrected for; the dependence of the bath occupancy on optical power measured and included in the analysis of the cooled state; the thermometer used for the cryostat or sample stage named.

**Benchmark.** [1], [5], [7], [8]

## 4. Occupancy inferred from cooled spectra

**Question.** How is the final occupancy obtained from the measured spectrum, and is it consistent with the measured optical damping, the bath occupancy, the intrinsic mechanical damping and the sideband resolution of the cavity?

**Why it matters.** Sideband cooling reduces the occupancy roughly in proportion to the ratio of intrinsic to total mechanical damping, down to a quantum limit set by the ratio of cavity linewidth to mechanical frequency, so an inferred occupancy far below this prediction needs explanation. The measured linewidth can include frequency jitter of the mechanical mode, so it does not always equal the energy damping rate that the cooling formula uses. Nearby mechanical modes or substrate motion within the integration window add to the area attributed to the mode. As the enhanced coupling approaches the cavity linewidth, the mode hybridises with the cavity, the spectrum splits and the weak-coupling cooling formula no longer applies.

**Resolved by.** The relation used to convert spectral area or linewidth into occupancy stated with every parameter; the inferred occupancy compared with the cooling prediction from measured damping rates, bath occupancy and the cavity linewidth to mechanical frequency ratio; the intrinsic damping measured independently, for example by ring-down, and any inhomogeneous broadening identified; the integration window stated and the result shown to be insensitive to it, or other modes within it accounted for; at high cooperativity, a model that includes strong coupling used where the enhanced coupling is not small compared with the cavity linewidth.

**Benchmark.** [1], [5], [8]

## 5. Classical laser noise

**Question.** Were the phase and amplitude noise of the cooling and probe lasers measured at the mechanical frequency, and does the paper show how much they add to the mode occupancy and how they change the measured spectrum?

**Why it matters.** Laser phase and amplitude noise at the mechanical frequency drive the mode through radiation pressure and add phonons that look like thermal motion. The same noise is correlated with the mechanical response, which squashes or raises the noise floor near the sidebands and produces Fano-shaped lines, biasing an occupancy read from the spectrum.

**Resolved by.** The laser phase and amplitude noise at the mechanical frequency measured, for example with a calibrated interferometer and a photodiode, and given as a noise photon number; the added heating computed from it; spectra fitted with a model that includes noise correlations where they matter; a filter cavity or quieter laser used, or a test such as changing the filtering, showing that the result does not change.

**Benchmark.** [1], [4], [6]

## 6. Sideband asymmetry and Raman-ratio thermometry

**Question.** When an occupancy or a quantum signature is inferred from the ratio or difference of Stokes and anti-Stokes sidebands, how was the detection gain at the two sideband frequencies calibrated, which detection scheme was used, and how were laser noise and readout backaction excluded as sources of the asymmetry?

**Why it matters.** The sideband ratio gives the occupancy without knowing g0 or the detection efficiency only if the gain is the same at both frequencies, or measured at each. Classical laser noise and thermal noise in the cavity can create or mask an asymmetry, so an asymmetry alone does not show quantum behaviour. With linear detection the asymmetry can be attributed to correlations in the measurement noise and not to mechanical zero-point motion, so the stated interpretation depends on the scheme.

**Resolved by.** The frequency response of the detection measured at both sidebands, for example with a calibration tone or a thermal reference over a range of cryostat temperatures; the detection scheme and the interpretation it supports stated; laser and cavity noise measured and shown to be small, or included, and the asymmetry checked against probe power; readout cooperativity kept low or its heating corrected for; the inferred occupancy cross-checked against an independent thermal calibration.

**Benchmark.** [4], [6], [7], [8]

## 7. What a ground-state claim refers to

**Question.** Does a claim of ground-state cooling state the occupancy with an uncertainty that includes the calibration, which mode and operating point it refers to, and whether readout heating and any half-quantum or noise-floor terms are included?

**Why it matters.** For a thermal state, a mean occupancy below one corresponds to a ground-state probability above one half, so the claim rests on the absolute calibration of occupancy, which items 1 to 6 bear on. An occupancy measured with one detection scheme can contain terms from field fluctuations that another scheme assigns differently, and the readout beam can heat the mode it measures.

**Resolved by.** The occupancy and its uncertainty given with the contributions from g0, detection efficiency, bath occupancy and noise-floor calibration listed; the ground-state probability or occupancy stated for the mode and cooling power in question; readout heating and laser-noise heating subtracted or bounded; agreement between two calibration routes, such as sideband asymmetry and a thermal calibration, shown.

**Benchmark.** [1], [5], [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Aspelmeyer, T. J. Kippenberg and F. Marquardt, Cavity optomechanics, Rev. Mod. Phys. 86, 1391–1452 (2014); read as preprint arXiv:1303.0733 | doi:10.1103/RevModPhys.86.1391 | full text | Sec. II.2.1: effective mass depends on the normalisation of the mode function. Sec. III.1: photothermal forces from absorption can mimic retarded radiation forces but destroy the coherence needed for quantum optomechanics. Sec. III.2: g0 is the coupling times the zero-point amplitude and the enhanced coupling is g0 times the square root of the intracavity photon number. Secs. V.2.1 and V.2.2: optical spring and optical damping set by detuning and power. Sec. VII.1: final occupancy from optical and intrinsic damping and bath occupancy, quantum limit set by cavity linewidth over four times the mechanical frequency, ground-state probability 1/(1+n); experiments limited by laser reheating of the sample; laser noise heats the mode; sideband weights used as a thermometer, with excess laser noise able to add to the asymmetry. Sec. VII.2: cooling becomes less efficient near strong coupling, with normal-mode splitting of order 2g |
| 2 | M. L. Gorodetsky, A. Schliesser, G. Anetsberger, S. Deléglise and T. J. Kippenberg, Determination of the vacuum optomechanical coupling rate using frequency noise calibration, Opt. Express 18, 23236–23246 (2010); read as preprint arXiv:1009.4231 | doi:10.1364/OE.18.023236 | full text | Sec. 1: the coupling per displacement and the effective mass are individually ambiguous under rescaling of displacement, while g0 is not. Sec. 2: g0 from the ratio of the thermal frequency-noise peak to a known phase-modulation peak, needing a known occupancy, thermal equilibrium and low power to exclude dynamical backaction |
| 3 | B. D. Hauer, C. Doolin, K. S. D. Beach and J. P. Davis, A general procedure for thermomechanical calibration of nano/micro-mechanical resonators, Ann. Phys. 339, 181–207 (2013); read as preprint arXiv:1305.0557 | doi:10.1016/j.aop.2013.08.003 | full text | Sec. V: effective mass depends on mode shape and on the position at which displacement is measured. Sec. III: thermomechanical calibration relies on equipartition at temperature T and a fitted transduction factor that depends on the set-up and must be found for each data set |
| 4 | A. M. Jayich, J. C. Sankey, K. Børkje, D. Lee, C. Yang, M. Underwood, L. Childress, A. Petrenko, S. M. Girvin and J. G. E. Harris, Cryogenic optomechanics with a Si3N4 membrane and classical laser noise, New J. Phys. 14, 115018 (2012); read as preprint arXiv:1209.2730 | doi:10.1088/1367-2630/14/11/115018 | full text | Sec. 2: optical spring and damping fitted together, with the fitted external coupling fraction about 20% above the independent estimate; Fano-shaped sidebands. Secs. 4 to 6: classical amplitude and phase noise and their correlation produce sideband asymmetry, so asymmetry alone does not show quantum behaviour, and neglecting the correlation biases the inferred phonon number. Sec. 7: laser noise measured; filter cavity proposed to remove it |
| 5 | S. M. Meenehan, J. D. Cohen, S. Gröblacher, J. T. Hill, A. H. Safavi-Naeini, M. Aspelmeyer and O. Painter, Silicon optomechanical crystal resonator at millikelvin temperatures, Phys. Rev. A 90, 011803(R) (2014); read as preprint arXiv:1403.3703, which carries a different title | doi:10.1103/PhysRevA.90.011803 | full text | Calibration discussion: occupancy at 4 K and low power sat about 1.3 times the expected fridge occupancy, applied as a systematic correction; sideband asymmetry compared with the thermal model. Results at 10 mK: the mode stays far hotter than the fridge because of absorption-induced heating, with occupancy rising with intracavity photon number. Linewidth discussion: measured linewidth broadened beyond energy decay by frequency jitter |
| 6 | A. H. Safavi-Naeini, J. Chan, J. T. Hill, S. Gröblacher, H. Miao, Y. Chen, M. Aspelmeyer and O. Painter, Laser noise in cavity-optomechanical cooling and thermometry, New J. Phys. 15, 035007 (2013); read as preprint arXiv:1210.2671 | doi:10.1088/1367-2630/15/3/035007 | full text | Sec. 2.4.1: laser phase noise adds phonons in proportion to the noise photon number at the mechanical frequency. Secs. 2.4.2 and 2.4.3: noise squashing and anti-squashing bias the inferred occupancy and can mask the quantum sideband asymmetry. Sec. 3 and App. E: phase noise measured, filter test, separate cooling and readout modes, readout at low cooperativity |
| 7 | A. J. Weinstein, C. U. Lei, E. E. Wollman, J. Suh, A. Metelmann, A. A. Clerk and K. C. Schwab, Observation and interpretation of motional sideband asymmetry in a quantum electromechanical device, Phys. Rev. X 4, 041003 (2014); read as preprint arXiv:1404.3242 | doi:10.1103/PhysRevX.4.041003 | full text | Theory: with linear detection the asymmetry is attributed to detector noise correlations, with photodetection to mechanical fluctuations. Experiment: separate gain factors for the two sidebands from a cryostat temperature sweep; noise floor calibrated separately; cavity thermal noise adds to the imbalance; back-action heating corrected; independent calibration of occupancy suggested |
| 8 | T. P. Purdy, P.-L. Yu, N. S. Kampel, R. W. Peterson, K. Cicak, R. W. Simmonds and C. A. Regal, Optomechanical Raman-ratio thermometry, Phys. Rev. A 92, 031802(R) (2015); read as preprint arXiv:1406.7247 | doi:10.1103/PhysRevA.92.031802 | full text | Main text: Stokes to anti-Stokes ratio gives occupancy without g0 or detection efficiency once the heterodyne frequency response is measured; laser noise, detuning, nearby modes within the integration window (tens of percent change) and readout backaction assessed; intrinsic damping from ring-down; physical temperature cross-checked against a diode thermometer within 10% |
