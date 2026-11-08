---
id: CL-QUANTUM-ADVANTAGE
name: Claims of quantum advantage
type: claim
field: physics/quantum-information
applies_when: the paper claims that a quantum device outperforms classical computers or performs a computation beyond their reach, using terms such as quantum advantage, supremacy, speedup or utility, or projects such an advantage at larger scale, whatever the platform or task
version: "0.1"
---

# Claims of quantum advantage

## 1. The task and the kind of advantage claimed

**Question.** Does the paper define the computational task precisely, state which kind of advantage it claims (over every possible classical algorithm, over the best available algorithm, or over a specific algorithm or method), and give the evidence that the task is hard for classical computers?

**Why it matters.** An advantage over a chosen classical algorithm is weaker than one over the best available algorithm, and a weak baseline can produce an apparent advantage trivially. The hardness of sampling and simulation tasks usually rests on complexity-theoretic conjectures about the ideal task, which do not automatically cover the instance sizes and the noisy version of the task that a device performs.

**Resolved by.** The task stated with its inputs, outputs and success criterion; the claim placed in a named category of speedup; the complexity-theoretic arguments cited, with what they assume and whether they apply at the sizes and noise levels of the experiment.

**Benchmark.** [1], [2]

## 2. The classical baseline

**Question.** Which classical algorithms were compared, are they the strongest available for this task, including methods that exploit the structure of the specific instances such as limited depth, limited entanglement, the connectivity or the noise, and were they implemented and run, or only estimated?

**Why it matters.** Classical cost estimates depend on the algorithm and on how well it is implemented, and hardness conjectures are revised as better simulation algorithms appear. Generic or unoptimised codes, or a runtime extrapolated from a single method, can greatly overstate the classical cost.

**Resolved by.** A survey of the relevant classical methods and the reasons the chosen ones are the strongest; optimised implementations run on the same instances wherever that is feasible; for larger instances, cost estimates that state the algorithm, memory, hardware and assumptions behind them; the distinction between a measured classical runtime and an estimated one kept clear.

**Benchmark.** [1], [2], [3]

## 3. What is counted as the cost

**Question.** Which figure of merit is compared (wall-clock time, time to reach a solution with a target success probability or accuracy, energy or monetary cost), and does it include every step on both sides: programming and compilation, repetitions, readout, data input and output, and classical pre- and post-processing?

**Why it matters.** Counting only the pure run time of the quantum device leaves out programming, readout and the repetitions needed to reach a target success probability, and the classical resources should grow with problem size as the quantum resources do. For projected advantages, loading data into and reading results out of a quantum device is slow, and error-corrected gates are much slower than classical operations, so small speedups such as quadratic ones may not pay off within a practical run time.

**Resolved by.** The metric defined together with the success probability or accuracy it refers to; the total cost on each side broken into its parts; the classical hardware stated and scaled comparably with the quantum hardware; for projected advantages, end-to-end resource estimates that include error correction and input and output.

**Benchmark.** [2], [4]

## 4. Scaling with problem size

**Question.** Is the advantage shown as a trend over a range of problem sizes, with the settings of both the quantum and the classical methods optimised at each size, or does it rest on a single size or on an extrapolation?

**Why it matters.** A result at one size says little about how the costs grow, and extrapolation from small sizes is unreliable. Running a method with a fixed setting that is longer than needed at small sizes flattens its apparent scaling and can create a speedup that is not there. Asymptotic statements say little about a particular finite device, so a claim about one experiment needs concrete classical cost estimates at that size.

**Resolved by.** Cost against problem size for both sides, with run times and other settings optimised at each size; the range of sizes and the fitted scaling given with uncertainties; the claim stated clearly as either a finite-size claim with a concrete classical cost or a scaling claim; the selection of problem instances described, with results for the hardest instances as well as the typical ones.

**Benchmark.** [1], [2], [3]

## 5. Verification of the output

**Question.** How does the paper show that the device performed the claimed task correctly in the regime where its output cannot be checked by classical computation, and what assumptions link the checks it can make to that regime?

**Why it matters.** Checking samples from the flat distributions of sampling tasks directly needs exponentially many samples, and scores such as XEB need the ideal output probabilities, which are costly to compute in exactly the regime claimed. Trust is therefore built in smaller or simplified circuits, or from benchmarks of individual components, which assumes that no new source of error appears in the full computation; XEB stands in for the fidelity only under assumptions about the noise.

**Resolved by.** The verification method named with its assumptions; agreement with exact classical simulation over the range of sizes where it is possible, showing how the agreement trends towards the claimed regime; component benchmarks combined with an error model and compared with whole-circuit measurements; for tasks whose answers can be checked efficiently, that check reported.

**Benchmark.** [1], [3], [5]

## 6. Noise and the hardness of the noisy task

**Question.** At the fidelity, error and loss rates achieved, is the noisy task the device actually performs still hard for classical computers, and does the classical comparison include algorithms that simulate the noisy device and exploit that noise?

**Why it matters.** Enough noise makes a hard distribution easy to simulate. With a constant rate of depolarizing noise per gate, and circuits deep enough for their outputs to anti-concentrate, random circuit sampling can be simulated classically in polynomial time in the asymptotic limit, and the outputs of noisy circuits approach the uniform distribution as circuits grow. Boson sampling with lost photons can be simulated efficiently when fewer than about the square root of the photons sent in survive, or when every path passes through enough lossy elements.

**Resolved by.** Measured fidelities, error rates and loss rates; the experiment placed relative to the known regimes of classical simulability for that kind of noise; classical algorithms that reproduce the noisy output to the same fidelity included in the baseline; how the margin over those algorithms changes with size.

**Benchmark.** [1], [3], [7], [8]

## 7. Spoofing the benchmark

**Question.** Could a classical algorithm pass the test used to certify the device without performing the task, and does the paper compare the device's score with the strongest known classical strategies for passing that test?

**Why it matters.** Linear XEB rewards putting probability on likely outputs, which can be done without reproducing the ideal distribution, and classical algorithms that sample a few qubits from their exact marginals already score above random guessing for shallow circuits. Tensor-network methods can reach scores comparable to those of noisy devices of moderate size, and a simulator allowed to post-select can pass some tests.

**Resolved by.** The certification test and the score stated; the score compared with those of known spoofing algorithms at the same size and depth; arguments or evidence that the test cannot be passed cheaply; more than one test, including tests that probe the distribution beyond a single score.

**Benchmark.** [1], [6], [7]

## 8. Error mitigation and the accuracy of computed values

**Question.** Where the claim rests on computing a physical quantity, such as an expectation value, which error-mitigation methods were used, with what noise model and sampling overhead, and how was the accuracy of the mitigated values established?

**Why it matters.** Error mitigation reduces bias at the cost of extra repetitions whose number grows exponentially with the total error of the circuit, so it works only up to a limited circuit size. Its results keep a residual bias when the assumed noise model is incomplete, for example when noise is correlated, or when amplifying the noise changes its form.

**Resolved by.** The mitigation methods named, with the noise model and how it was characterised; the sampling overhead and the total error per circuit reported; mitigated values compared with exact results where these exist and with classical approximate methods of stated accuracy; the uncertainty of the final values including the residual bias.

**Benchmark.** [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | A. W. Harrow and A. Montanaro, Quantum computational supremacy, Nature 549, 203 (2017); read as arXiv:1809.07442 | doi:10.1038/nature23458 |
| 2 | T. F. Rønnow et al., Defining and detecting quantum speedup, Science 345, 420 (2014); read as arXiv:1401.2910 | doi:10.1126/science.1252319 |
| 3 | D. Hangleiter and J. Eisert, Computational advantage of quantum random sampling, Rev. Mod. Phys. 95, 035001 (2023); read as arXiv:2206.04079 (HTML version, Secs. I to V.2) | doi:10.1103/RevModPhys.95.035001 |
| 4 | T. Hoefler et al., Disentangling hype from practicality: on realistically achieving quantum advantage, Commun. ACM 66(5), 82 (2023); read as arXiv:2307.00523 | doi:10.1145/3571725 |
| 5 | J. Eisert et al., Quantum certification and benchmarking, Nat. Rev. Phys. 2, 382 (2020); read as arXiv:1910.06343 | doi:10.1038/s42254-020-0186-4 |
| 6 | B. Barak et al., Spoofing linear cross-entropy benchmarking in shallow quantum circuits, 12th Innovations in Theoretical Computer Science Conference (ITCS 2021), LIPIcs 185, 30:1–30:20 (2021); read as arXiv:2005.02421 | doi:10.4230/LIPIcs.ITCS.2021.30 |
| 7 | D. Aharonov et al., A polynomial-time classical algorithm for noisy random circuit sampling, Proceedings of the 55th Annual ACM Symposium on Theory of Computing (STOC 2023), 945 (2023); read as arXiv:2211.03999 | doi:10.1145/3564246.3585234 |
| 8 | M. Oszmaniec and D. J. Brod, Classical simulation of photonic linear optics with lost particles, New J. Phys. 20, 092002 (2018); read as arXiv:1801.06166 | doi:10.1088/1367-2630/aadfa8 |
| 9 | Z. Cai et al., Quantum error mitigation, Rev. Mod. Phys. 95, 045005 (2023); read as arXiv:2210.00921 | doi:10.1103/RevModPhys.95.045005 |
