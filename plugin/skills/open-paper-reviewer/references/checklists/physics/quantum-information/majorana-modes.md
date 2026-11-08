---
id: CL-MAJORANA-MODES
name: Claims of Majorana modes and topological qubits
type: claim
field: physics/quantum-information
applies_when: the paper claims Majorana zero modes, topological superconductivity, non-Abelian statistics or a topological qubit, or interprets zero-bias conductance peaks, quantized zero-bias conductance, end-to-end correlations, parity measurements, fusion or braiding as evidence for them, whatever the platform
version: "0.1"
---

# Claims of Majorana modes and topological qubits

## 1. Trivial origins of a zero-bias peak

**Question.** Which trivial mechanisms that give a zero-bias peak does the paper consider, such as Andreev bound states from quantum dots, smooth confinement or inhomogeneous potentials, disorder, or Kondo and Yu-Shiba-Rusinov states, and what measurement, beyond the existence of the peak, separates each of them from a Majorana zero mode?

**Why it matters.** A zero-bias peak is what a Majorana zero mode predicts, but trivial bound states can sit at or near zero energy over a wide range of field and gate voltage. Andreev bound states formed at a smooth potential step, often called quasi-Majorana states, can reproduce most proposed local signatures, including a stable and even quantized peak, so a local peak can suggest but not establish a Majorana mode.

**Resolved by.** The trivial mechanisms that apply to the device named, with a measured dependence on field, gate and tunnel barrier compared with what each predicts; a signature that trivial states do not share, such as a bulk transition, end-to-end correlation in a long system or the open-regime conductance, used in addition to the peak; the interpretation stated as consistent with Majorana modes, not as a demonstration, where only local probes were used.

**Benchmark.** [1], [2], [3], [7]

## 2. A bulk topological transition at the right place

**Question.** Does the zero-bias peak appear only beyond a topological transition, located from independently measured parameters such as the induced gap, the g-factor and the chemical potential, and does the paper show the bulk gap closing and reopening there while the parent superconducting gap survives?

**Why it matters.** A Majorana zero mode exists only in the topological phase, which needs a field above a critical value set by the gap and chemical potential. Trivial bound states can produce peaks below that field, and if the parent gap collapses before the transition no Majorana signature is possible. Local tunnelling probes the region near the lead, so a closing and reopening gap seen at one end may be local and not a property of the bulk.

**Resolved by.** The critical field estimated from measured parameters and compared with the field at which the peak appears; a gap closing and reopening shown in a probe sensitive to the bulk, for example nonlocal conductance between two separated leads, in a system longer than the induced coherence length; the parent gap and the induced gap shown to persist above the transition field.

**Benchmark.** [1], [3], [5], [6]

## 3. Induced gap and disorder

**Question.** Does the paper show a hard induced gap, free of subgap states, at zero field, and does it estimate the disorder in the system and compare it with the induced gap, the Zeeman energy and the chemical potential?

**Why it matters.** Weak disorder leaves Majorana modes intact, but strong disorder in the potential or the gap suppresses topological superconductivity and produces trivial zero-bias peaks, some of which look quantized. Subgap states already present at zero field indicate inhomogeneity or interface disorder, and without an estimate of disorder against the gap there is no quantitative way to judge which regime a device is in.

**Resolved by.** Tunnelling spectra at zero field showing the induced gap and the ratio of subgap to above-gap conductance; an estimate of disorder strength or mean free path from transport or materials characterisation compared with the gap and Zeeman energies; the material and interface quality described.

**Benchmark.** [1], [3], [7]

## 4. Stability across parameter space

**Question.** Over what range of field, gate voltages and tunnel-barrier settings does the zero-bias peak persist, how was the region shown chosen within the parameter space explored, and what fraction of the explored space shows the feature?

**Why it matters.** Trivial zero-bias peaks, including quantized ones, occupy a modest but finite fraction of a multi-dimensional parameter space, so a systematic search will find them, and their stability under tuning does not exclude a trivial origin. Majorana modes in a long, clean system should be robust over wide parameter ranges, while a feature that needs extensive gate fine-tuning is harder to reconcile with a topological phase.

**Resolved by.** Two-dimensional maps of conductance against field and each relevant gate, covering the region explored and not only the cuts that show a peak; the search procedure stated, including how many devices and gate configurations were tried and how often the feature appeared; the expected splitting oscillations with field compared with those observed.

**Benchmark.** [1], [3], [4]

## 5. Quantized conductance

**Question.** When the paper reports a zero-bias conductance at or near 2e²/h, does it show how the peak height and width depend on temperature and tunnel coupling, compare any plateau against the tunnel barrier with what the temperature and coupling allow, state the number of conducting channels, and explain any value above 2e²/h?

**Why it matters.** An ideal Majorana zero mode gives 2e²/h at zero temperature for any tunnel coupling, but at finite temperature the peak falls below this value, more so for weak tunnelling, so the height has to be read against the temperature and the coupling, and a value above 2e²/h at finite temperature points to extra channels or another origin. Trivial bound states, quasi-Majorana states and models with no isolated Majorana mode at all can also give quantized peaks and plateaus, so quantization alone does not identify a Majorana mode.

**Resolved by.** The electron temperature measured and compared with the peak width; peak height and width against temperature and barrier transparency, with the tunnel coupling not inferred only from the above-gap conductance; evidence of a single channel; the quantized value shown together with the other signatures in this card, not as stand-alone evidence.

**Benchmark.** [1], [2], [3], [4], [5]

## 6. Non-locality: the two ends together

**Question.** Does the paper show that the zero modes at the two ends of the system are correlated, through measurements at both ends or a nonlocal probe, and is the system long enough compared with the coherence length for such a correlation to be meaningful?

**Why it matters.** The protection and non-Abelian character of Majorana modes rest on their being spatially separated, which purely local probes can only suggest. In short systems overlapping wavefunctions produce end-to-end correlations even for trivial states, and quasi-Majorana states at one end can appear highly non-local by local measures, so a correlation is informative only when the length clearly exceeds the coherence length.

**Resolved by.** Simultaneous tunnelling or nonlocal conductance at both ends over the same field and gate ranges; the system length compared with the measured or estimated coherence length; correlated peaks at both ends shown together with a bulk transition seen in the nonlocal signal; the overlap between the two modes estimated, for example from splitting oscillations or quantum-dot spectroscopy.

**Benchmark.** [1], [2], [3], [6]

## 7. Parity readout and topological qubit claims

**Question.** For a claimed topological qubit or parity measurement, does the paper report the readout fidelity and measurement time, the parity lifetime against quasiparticle poisoning, both the dephasing time and the time for leakage out of the qubit states, and a test that distinguishes a qubit encoded in Majorana modes from one encoded in trivial Andreev states?

**Why it matters.** A Majorana qubit stores information in the joint fermion parity of separated modes, and a stray quasiparticle flips that parity, so poisoning times must exceed operation and readout times. Trivial Andreev states can pass for Majorana modes in local probes and can form a qubit that is initialised and read out in the same way and shows a precession of its own; what separates the two is that in a Majorana qubit the splitting falls and the dephasing time rises together, exponentially in the length of the system over the coherence length, while for Andreev states neither depends much on length. Leakage out of the qubit states is set instead by the bulk gap and cuts the lifetime sharply where that gap closes. Braiding and parity measurements give only Clifford operations, so a universal topological qubit also needs a non-protected gate.

**Resolved by.** Readout assignment errors, measurement time and parity lifetime stated, with poisoning times shown to exceed the operation time; dephasing and leakage times both measured; the splitting and the dephasing time followed together as a function of length or field, compared with the correlated exponential scaling expected for Majorana modes and the weak length dependence expected for Andreev states; the level of protection claimed matched to the operations actually shown.

**Benchmark.** [7], [8], [9]

## 8. Fusion and braiding

**Question.** For a claimed fusion or braiding experiment, does the paper compare the operation sequence with control sequences, show that the timing lies between the adiabatic limit set by the gap and the limits set by poisoning and residual splitting, and exclude trivial ways of obtaining the same outcomes?

**Why it matters.** Braiding is the most direct test of non-Abelian statistics and fusion an indirect one, but a single outcome can be mimicked. Quasiparticle poisoning drives any sequence towards the equal probabilities expected after one braid, and some trivial configurations give them after a single exchange whatever their phases; a parity measurement switched on too fast can give the outcome expected from fusion whether or not zero modes are present; and several trivial low-energy states, or one fine-tuned to zero energy, can reproduce the fusion outcome.

**Resolved by.** A control run alongside the test sequence that would reveal poisoning on the time scale of the experiment, such as the same sequence with no exchange; a double braid shown to give a deterministic flip where a single braid gives equal probabilities, with runs of different numbers of exchanges compared; the dependence of the result on operation speed shown, from the adiabatic regime to the regime where poisoning or splitting erases it.

**Benchmark.** [7], [9], [10]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | E. Prada et al., From Andreev to Majorana bound states in hybrid superconductor–semiconductor nanowires, Nat. Rev. Phys. 2, 575 (2020); read as arXiv:1911.04512 | doi:10.1038/s42254-020-0228-y |
| 2 | A. Vuik et al., Reproducing topological properties with quasi-Majorana states, SciPost Phys. 7, 061 (2019); read as arXiv:1806.02801 | doi:10.21468/SciPostPhys.7.5.061 |
| 3 | H. Pan and S. Das Sarma, Physical mechanisms for zero-bias conductance peaks in Majorana nanowires, Phys. Rev. Research 2, 013377 (2020); read as arXiv:1910.11413 | doi:10.1103/PhysRevResearch.2.013377 |
| 4 | H. Pan et al., Generic quantized zero-bias conductance peaks in superconductor-semiconductor hybrid structures, Phys. Rev. B 101, 024506 (2020); read as arXiv:1906.08193 | doi:10.1103/PhysRevB.101.024506 |
| 5 | F. Setiawan et al., Electron temperature and tunnel coupling dependence of zero-bias and almost-zero-bias conductance peaks in Majorana nanowires, Phys. Rev. B 96, 184520 (2017); read as arXiv:1708.09039 | doi:10.1103/PhysRevB.96.184520 |
| 6 | T. Ö. Rosdahl et al., Andreev rectifier: a nonlocal conductance signature of topological phase transitions, Phys. Rev. B 97, 045421 (2018); read as arXiv:1706.08888 | doi:10.1103/PhysRevB.97.045421 |
| 7 | S. Das Sarma et al., Majorana zero modes and topological quantum computation, npj Quantum Inf. 1, 15001 (2015); read as arXiv:1501.02813 | doi:10.1038/npjqi.2015.1 |
| 8 | R. V. Mishmash et al., Dephasing and leakage dynamics of noisy Majorana-based qubits: Topological versus Andreev, Phys. Rev. B 101, 075404 (2020); read as arXiv:1911.02582 | doi:10.1103/PhysRevB.101.075404 |
| 9 | C. W. J. Beenakker, Search for non-Abelian Majorana braiding statistics in superconductors, SciPost Phys. Lect. Notes 15 (2020); read as arXiv:1907.06497 | doi:10.21468/SciPostPhysLectNotes.15 |
| 10 | D. J. Clarke et al., Probability and braiding statistics in Majorana nanowires, Phys. Rev. B 95, 155451 (2017); read as arXiv:1610.08958 | doi:10.1103/PhysRevB.95.155451 |
