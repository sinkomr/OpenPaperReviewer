---
id: T-CAVITY-OPTOMECHANICS
name: Cavity optomechanics
type: technique
field: physics/optics-photonics
applies_when: the paper couples a mechanical mode to an optical or microwave cavity and reports a vacuum coupling rate, cooperativity, sideband cooling, a phonon occupancy or ground-state claim, motional sideband asymmetry, optomechanical thermometry, or the effect of laser or thermal noise on the mechanical mode
version: "0.1"
---

# Cavity optomechanics

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

**Resolved by.** The relation used to convert spectral area or linewidth into occupancy stated with every parameter; the inferred occupancy compared with the cooling prediction from measured damping rates, bath occupancy and the cavity linewidth to mechanical frequency ratio; the intrinsic damping measured independently, for example by ring-down, and any inhomogeneous broadening identified; the integration window stated and the result shown to be insensitive to it, or other modes within it accounted for; at high cooperativity, a model that includes strong coupling used where the enhanced coupling is not small compared with the cavity linewidth; the occupancy, and any ground-state probability derived from it, given for the stated mode and cooling power with an uncertainty that lists the contributions from g0, detection efficiency, bath occupancy and noise-floor calibration.

**Benchmark.** [1], [5], [7], [8]

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

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Aspelmeyer et al., Cavity optomechanics, Rev. Mod. Phys. 86, 1391 (2014); read as preprint arXiv:1303.0733 | doi:10.1103/RevModPhys.86.1391 |
| 2 | M. L. Gorodetsky et al., Determination of the vacuum optomechanical coupling rate using frequency noise calibration, Opt. Express 18, 23236 (2010); read as preprint arXiv:1009.4231 | doi:10.1364/OE.18.023236 |
| 3 | B. D. Hauer et al., A general procedure for thermomechanical calibration of nano/micro-mechanical resonators, Ann. Phys. 339, 181 (2013); read as preprint arXiv:1305.0557 | doi:10.1016/j.aop.2013.08.003 |
| 4 | A. M. Jayich et al., Cryogenic optomechanics with a Si3N4 membrane and classical laser noise, New J. Phys. 14, 115018 (2012); read as preprint arXiv:1209.2730 | doi:10.1088/1367-2630/14/11/115018 |
| 5 | S. M. Meenehan et al., Silicon optomechanical crystal resonator at millikelvin temperatures, Phys. Rev. A 90, 011803(R) (2014); read as preprint arXiv:1403.3703, which carries a different title | doi:10.1103/PhysRevA.90.011803 |
| 6 | A. H. Safavi-Naeini et al., Laser noise in cavity-optomechanical cooling and thermometry, New J. Phys. 15, 035007 (2013); read as preprint arXiv:1210.2671 | doi:10.1088/1367-2630/15/3/035007 |
| 7 | A. J. Weinstein et al., Observation and interpretation of motional sideband asymmetry in a quantum electromechanical device, Phys. Rev. X 4, 041003 (2014); read as preprint arXiv:1404.3242 | doi:10.1103/PhysRevX.4.041003 |
| 8 | T. P. Purdy et al., Optomechanical Raman-ratio thermometry, Phys. Rev. A 92, 031802(R) (2015); read as preprint arXiv:1406.7247 | doi:10.1103/PhysRevA.92.031802 |
