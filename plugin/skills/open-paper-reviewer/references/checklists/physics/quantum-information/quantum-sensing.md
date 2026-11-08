---
id: CL-QUANTUM-SENSING
name: Claims of quantum-enhanced sensing
type: claim
field: physics/quantum-information
applies_when: the paper claims a sensitivity or precision beyond the standard quantum limit or shot-noise limit, Heisenberg scaling, or a metrological gain from entangled, squeezed, NOON or other non-classical states of light, atoms, spins or other probes, whatever the sensor
version: "0.1"
---

# Claims of quantum-enhanced sensing

## 1. What is counted as a resource

**Question.** Which resource is the sensitivity compared against (number of particles or photons, mean energy, number of passes or interrogations, total time), and does the count include every probe used, including those lost before detection, not detected, or discarded by post-selection or heralding, and the time spent preparing and reading out the probes?

**Why it matters.** A gain over the SQL means something only for a stated amount of resources. Counting only the detected photons, or only the runs that passed a post-selection step, can turn a scheme that is worse than a classical one into an apparent enhancement. Sensitivity per unit time falls when preparation, readout and dead time are included, and these overheads are often longer for non-classical states.

**Resolved by.** The resource named and counted at the input of the sensor; overall transmission, detection efficiency and success probability of any post-selection or heralding stated and folded into the comparison; a clear statement of whether the enhancement is unconditional or holds only for the selected events; sensitivity quoted per unit of total measurement time, including overheads.

**Benchmark.** [1], [2], [3]

## 2. The classical comparison

**Question.** Which limit is the claim stated against (the shot-noise or projection-noise limit, or the SQL of continuous measurement set by shot noise and back-action together), and against which classical strategy is the gain measured: uncorrelated probes or a coherent state with the same resource count, run on the same apparatus, and is that the best strategy available without quantum correlations, including repeated or multi-pass use of single probes and more probes run in parallel?

**Why it matters.** The SQL is defined only once the classical resources are specified, and its prefactor depends on the strategy, so a weak reference gives an easy gain; noise below the shot-noise level and noise below the back-action SQL are different claims. Without noise, one probe passed through the system many times reaches the same scaling as an entangled state of many probes, and many uncorrelated sensors in parallel improve with the square root of their number exactly as classical sensors do. A gain over the SQL of one apparatus is not the same as a better sensitivity than other sensors of the same quantity.

**Resolved by.** The limit named and defined; the reference strategy defined with its resource count and measured on the same apparatus where possible, with the same probe number, time and losses; an argument that it is the best classical strategy under the stated constraints, including sequential or multi-pass alternatives; the absolute sensitivity reported in physical units alongside the gain relative to the SQL.

**Benchmark.** [1], [2], [4], [5]

## 3. Calibration of the quantum-noise reference

**Question.** How was the SQL reference level established (the measured vacuum or shot-noise level, or the projection noise computed from a calibrated number of particles), how was that number or level calibrated, and was any detector noise subtracted before the gain was stated?

**Why it matters.** The gain is a ratio to the SQL, so an error in the reference passes directly into the claim: an underestimated particle number enlarges the SQL uncertainty and makes it easier to beat. Optical vacuum noise is read with the signal path blocked, which is valid only with good mode matching and detector dark noise well below the shot noise. Subtracting detection noise gives an inferred gain that a sensor using that detector does not reach.

**Resolved by.** The method for the reference level described, such as a blocked-input vacuum measurement or a coherent-state measurement, with checks of detector linearity and dark noise; the absolute particle or photon number calibrated and its uncertainty carried into the SQL; directly measured and noise-subtracted gains reported separately and labelled as such.

**Benchmark.** [5], [6]

## 4. Enhancement in the estimate, not in the state

**Question.** Is the enhancement shown in the uncertainty of an actual estimate of a known, applied signal after the full measurement sequence, or is it inferred from a property of the probe state, such as reduced variance, a squeezing parameter, a computed Fisher information or faster interference fringes?

**Why it matters.** A squeezed or entangled state shows a potential gain; preparation, signal encoding and readout imperfections can remove it before the parameter is estimated. Fringes that oscillate faster than classical ones, called super-resolution, can be obtained from classical states by filtering and do not by themselves give a sensitivity beyond the SQL. A reduced variance is useful only if the mean signal, for example the spin length or fringe contrast, is kept.

**Resolved by.** A signal of known size applied and estimated through the complete protocol, with the measured uncertainty compared with the SQL for the same resources; for squeezing claims, a metrological parameter that includes the loss of mean signal, not only the reduced variance; super-resolution and super-sensitivity distinguished; witnesses of the state labelled as potential gains.

**Benchmark.** [1], [3], [6]

## 5. Attribution to entanglement or squeezing

**Question.** When the gain is attributed to entanglement or squeezing, does the paper give a criterion that certifies the metrologically useful correlations, such as a squeezing parameter below one or a Fisher information above the number of probes, and does it exclude explanations that need no entanglement?

**Why it matters.** A gain relative to the reference can come from a better operating point, longer interrogation, more passes or lower technical noise, none of which needs quantum correlations. Not every entangled state is useful for sensing, and Heisenberg scaling of the phase can be reached sequentially with a single probe, so scaling or improvement alone does not show that entanglement caused the gain.

**Resolved by.** A stated witness with its threshold and uncertainty, measured on the probe state used for sensing; the same apparatus run with uncorrelated probes under identical conditions as the reference; a resource count that rules out sequential or multi-pass explanations for any scaling claimed.

**Benchmark.** [4], [6]

## 6. Estimator, prior knowledge and number of repetitions

**Question.** How was the sensitivity obtained (from a Fisher information or error-propagation formula at a chosen operating point, or from the spread of estimates produced by a stated estimator), how many repetitions entered it, and what prior knowledge of the parameter did the method assume?

**Why it matters.** The Cramér-Rao bound is reached in general only after many repetitions, and a sensitivity computed at the optimal working point assumes the parameter is already known closely. States with faster fringes leave the phase ambiguous over a shorter range, and with finite prior knowledge the achievable Heisenberg-type precision is, asymptotically, worse than the Fisher-information bound by a factor of π. Error-propagation at points where both slope and noise vanish is very sensitive to technical noise.

**Resolved by.** The estimator named and its uncertainty measured from repeated independent estimates, compared with the Cramér-Rao bound; the number of repetitions stated; the range of parameter values over which the sensitivity holds, and the prior or adaptive scheme used to resolve phase ambiguity; claims of reaching a limit made against the bound that applies to the prior knowledge assumed.

**Benchmark.** [3], [4], [6], [7]

## 7. Heisenberg scaling and noise

**Question.** If the paper claims Heisenberg scaling or a growing gain, is the sensitivity shown over a range of probe numbers with each point measured, and is the claim stated together with the losses and decoherence that bound the gain at larger sizes?

**Why it matters.** With uncorrelated dephasing, loss or depolarisation, the achievable precision follows Heisenberg scaling only for small probe numbers and then returns to the standard scaling, so the asymptotic gain is a constant factor. Entangled states such as GHZ (Greenberger-Horne-Zeilinger) or NOON states decohere faster than product states, which can cancel their advantage at fixed total time. A fit over a few small sizes cannot establish scaling.

**Resolved by.** Measured sensitivity against probe number over the range used, with the fitted exponent and its uncertainty; loss and decoherence rates measured and compared with the known noise bounds for that kind of noise; the claim stated as a finite-size gain or a scaling claim, not extrapolated beyond the measured sizes.

**Benchmark.** [2], [6], [8]

## 8. Quantum noise in the operating sensor

**Question.** Is the sensor limited by quantum noise in the frequency band or averaging time where the gain is claimed, and does the gain persist in the sensor's output spectrum or Allan deviation in the presence of technical noise and drift?

**Why it matters.** Reducing quantum noise improves a sensor only where quantum noise dominates; where technical noise, drift or back-action dominates, a squeezed or entangled probe may give no gain or a smaller one. Ensemble sensors are more exposed to instrumental instability, and a gain seen over one averaging time may vanish at others.

**Resolved by.** The noise budget of the sensor shown, with the quantum-noise contribution identified in the band of interest; spectra or Allan deviations with and without the non-classical resource, taken under the same conditions; the band or averaging time over which the gain holds stated.

**Benchmark.** [2], [5], [6]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | V. Giovannetti et al., Advances in quantum metrology, Nat. Photon. 5, 222 (2011); read as arXiv:1102.2318 | doi:10.1038/nphoton.2011.35 |
| 2 | C. L. Degen et al., Quantum sensing, Rev. Mod. Phys. 89, 035002 (2017); read as arXiv:1611.02427 | doi:10.1103/RevModPhys.89.035002 |
| 3 | E. Polino et al., Photonic quantum metrology, AVS Quantum Sci. 2, 024703 (2020); read as arXiv:2003.05821 | doi:10.1116/5.0007577 |
| 4 | D. Braun et al., Quantum-enhanced measurements without entanglement, Rev. Mod. Phys. 90, 035006 (2018); read as arXiv:1701.05152 | doi:10.1103/RevModPhys.90.035006 |
| 5 | R. Schnabel, Squeezed states of light and their applications in laser interferometers, Phys. Rep. 684, 1 (2017); read as arXiv:1611.03986 | doi:10.1016/j.physrep.2017.04.001 |
| 6 | L. Pezzè et al., Quantum metrology with nonclassical states of atomic ensembles, Rev. Mod. Phys. 90, 035005 (2018); read as arXiv:1609.01609 | doi:10.1103/RevModPhys.90.035005 |
| 7 | W. Górecki et al., π-corrected Heisenberg limit, Phys. Rev. Lett. 124, 030501 (2020); read as arXiv:1907.05428 | doi:10.1103/PhysRevLett.124.030501 |
| 8 | R. Demkowicz-Dobrzański et al., The elusive Heisenberg limit in quantum-enhanced metrology, Nat. Commun. 3, 1063 (2012); read as arXiv:1201.3940 | doi:10.1038/ncomms2067 |
