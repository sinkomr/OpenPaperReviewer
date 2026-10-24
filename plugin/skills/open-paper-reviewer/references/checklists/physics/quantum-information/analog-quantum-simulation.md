---
id: T-ANALOG-QUANTUM-SIMULATION
name: Analog quantum simulation
type: technique
field: physics/quantum-information
applies_when: the paper uses a controllable quantum system, such as ultracold atoms in optical lattices, Rydberg atom arrays, trapped ions or superconducting circuits, to emulate a model Hamiltonian, and bases a claim about its ground state, phases, thermodynamics or dynamics on the measurements
version: "0.1"
---

# Analog quantum simulation

An analog quantum simulator (AQS) is a controllable quantum system, such as ultracold atoms in an optical lattice, an array of Rydberg atoms or a chain of trapped ions, whose own Hamiltonian is engineered to reproduce a model of interest. It is used to claim properties of that model, such as its phase diagram, correlations, thermodynamics or dynamics far from equilibrium, often in regimes that classical computers cannot reach and with no error correction to guarantee the result.

## 1. From the platform to the target model

**Question.** Does the paper derive the model it claims to simulate from the microscopic Hamiltonian of the platform, state the approximations used (for example a single band, a two-level truncation, perturbative or phonon-mediated couplings, or a time-averaged effective Hamiltonian under periodic driving), and estimate the size of the terms it neglects?

**Why it matters.** The target model is usually an effective description that holds only in a limit. Higher-order terms, extra internal levels, residual coupling to motion and the heating or micromotion of driven systems add terms that the target model lacks, and an observed effect may come from them instead of from the model.

**Resolved by.** The mapping written out with its conditions of validity; the leading neglected terms estimated for the parameters used; observables chosen or checked so that the neglected terms do not change them, for example by measuring in a basis insensitive to residual spin-motion coupling or by keeping the duration well below the heating time of a driven system; where the effective model fails in part of the parameter range, that range excluded or treated separately.

**Benchmark.** [2], [7], [8]

## 2. Calibration and verification of the implemented Hamiltonian

**Question.** How were the parameters of the implemented Hamiltonian, such as couplings, fields, tunnelling and interaction energies, determined, and were they measured on the device by a method that does not assume the result being claimed?

**Why it matters.** Without error correction, the accuracy of an analog simulation is limited by how well its Hamiltonian is calibrated, and errors from imperfect calibration add to errors from noise and decoherence. A parameter inferred from the design or from a model, instead of measured, can differ from the true value, vary across the system, or drift during the data taking, and the model then simulated is not the one named.

**Resolved by.** Each parameter measured directly, for example by spectroscopy of single couplings, pair oscillations or global precession, or reconstructed by Hamiltonian learning from data taken on the device; the measured values and their spread across sites given with uncertainties and drift over the run; for larger systems where direct calibration does not scale, a reconstructed Hamiltonian compared with the intended one, including any terms that should be absent.

**Benchmark.** [2], [3], [4]

## 3. Validation in tractable regimes and extrapolation beyond them

**Question.** Is the simulator checked against exact or controlled calculations in a regime where those are possible, and what supports the results in the regime the headline claim is about, where they are not?

**Why it matters.** Agreement with classical calculations in a tractable regime is the basic check that the device works, but it does not show that it stays reliable when parameters, size or evolution time are pushed into the untested regime, where new errors can appear. Agreement between two simulators can also mislead if both share the same kind of imperfection.

**Resolved by.** A benchmark against exact or controlled numerics for small systems, short times or limiting parameters, using the same protocol and observables as the main result; an argument or test that no new error source enters when moving to the claimed regime, such as unchanged calibration, a time-reversal or echo check, or the robustness tests of item 5; where available, comparison with a simulator on a different platform or with a different encoding of the same model, with the shared assumptions stated.

**Benchmark.** [1], [2], [3], [4]

## 4. Comparison with numerical methods

**Question.** When results are compared with numerical simulations, does the paper name the method and its approximations, show that the calculation is converged, and say which parameters of the calculation were measured independently and which were adjusted to fit the data?

**Why it matters.** Numerical methods for many-body problems carry their own systematic errors, from truncation of the bond dimension, a sign problem, a constrained-path or fixed-node approximation, a finite cluster or uncontrolled approximations such as mean-field theory. A discrepancy can then come from the numerics as well as from the device. If temperature, a coupling or a decay rate is fitted, agreement partly reflects the fit, not a test of the simulator.

**Resolved by.** The method stated with its controlled and uncontrolled approximations; convergence shown in the relevant parameters (bond dimension, time step, cluster or system size); the same geometry, size, inhomogeneity and imperfections included in the calculation as in the experiment; free parameters listed, fixed from independent measurements where possible, and the effect of fitting them reported; where methods disagree, more than one method used or the disagreement stated.

**Benchmark.** [1], [3], [5], [8]

## 5. Disorder, decoherence and heating

**Question.** Does the paper give the time scales of decoherence, heating and particle loss next to the duration of the protocol, and does it test how sensitive the claimed observable is to disorder and noise of the size present in the device?

**Why it matters.** Static disorder in the couplings and fields can shift a critical point, change apparent critical exponents or create phases that the ideal model does not have. Decoherence sets the longest time over which coherent dynamics can be followed, and several small imperfections, each of a few per cent, can add up to the damping or loss of contrast that is then read as physics.

**Resolved by.** Measured coherence, heating and loss times compared with the evolution or ramp time; the residual disorder in each parameter measured and included in the comparison with theory; a test of robustness, for example deliberately adding a known amount of disorder or noise, or varying it, and showing that the observable responds as expected; damping or loss of contrast accounted for by an error budget built from independently measured imperfections before it is attributed to the model.

**Benchmark.** [1], [3], [9]

## 6. State preparation, temperature and entropy

**Question.** How does the paper show that the prepared state is the one the claim is about (a ground state, a thermal state at a stated temperature, or a well-defined initial state), and how was the temperature or entropy measured?

**Why it matters.** States are often prepared by ramping parameters, and a ramp that is too fast near a small energy gap leaves the system excited; the gap usually shrinks with system size, so a ramp adequate for a small system may not be adequate for a larger one. Temperature is hard to measure in strongly correlated systems: methods that assume an entropy-conserving loading or rely on theory are secondary thermometers, and a temperature obtained by fitting the same theory that is being tested cannot then confirm it.

**Resolved by.** For ramped preparation, results for several ramp speeds or a reverse ramp showing that the state no longer depends on the speed, or the excitations quantified; the temperature or entropy per particle measured, with the method named as primary or secondary and its assumptions and range stated; heating during loading measured, for example by a round trip that returns to the starting conditions; the temperature compared with the energy scale of the claimed phase.

**Benchmark.** [2], [6]

## 7. Finite size, boundaries and inhomogeneity

**Question.** When the paper claims a phase, a phase transition or a property of the thermodynamic limit, how does it account for the finite size, the open boundaries and any trapping potential or spatial inhomogeneity of the system?

**Why it matters.** A finite system shows a crossover, not a sharp transition, and boundaries can create their own inhomogeneity, especially with long-range interactions. In a trapped gas several phases coexist at different densities, so an average over the cloud mixes them. Finite-size scaling applied without allowing for disorder can return a shifted critical point and a biased critical exponent.

**Resolved by.** Results for several system sizes, with a crossover shown to sharpen as size grows and quantities designed to locate transitions in finite systems, such as scaled order parameters or the Binder cumulant; local or site-resolved observables in a homogeneous region, or the local-density approximation used with its limits stated; boundary conditions modelled in the comparison with theory; extrapolations to infinite size shown with their uncertainties.

**Benchmark.** [1], [2], [5], [6]

## 8. Detection, readout errors and post-selection

**Question.** What are the preparation and detection error rates of the measurement, how do they enter the reported observables and correlations, and are any runs discarded or corrected?

**Why it matters.** Imaging and state detection have finite fidelity, crosstalk and loss, and the chance of at least one error in a snapshot grows with system size. Some schemes record only part of the information: atom loss may be read as an excited state, and fluorescence imaging in a lattice can detect only the parity of the site occupation, because pairs of atoms are lost during imaging. Correlation functions built from such data mix detection errors with the physics.

**Resolved by.** Preparation and detection error rates measured, for example false-positive and false-negative rates or the fidelity of distinguishing occupied from empty sites; the correction method stated and raw data shown next to corrected data; the effect of parity projection or loss on each observable discussed; the rule for discarding runs, such as those with defects in the initial array, stated with the fraction discarded.

**Benchmark.** [2], [9], [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | P. Hauke, F. M. Cucchietti, L. Tagliacozzo, I. Deutsch and M. Lewenstein, Can one trust quantum simulators?, Rep. Prog. Phys. 75, 082401 (2012); read as preprint arXiv:1109.6457 | doi:10.1088/0034-4885/75/8/082401 | full text | Sec. IV, on non-universal analog simulators: comparison with classical simulation in a tractable regime gives no guarantee in the interesting regime; cross-validation between platforms can mislead if they share imperfections; in one comparison numerics corrected the assumed temperature by up to 30%. Sec. V: proposes checking the sensitivity of the simulation to added noise and disorder. Secs. VI and VII with the Appendix: disorder can create or destroy phases, and finite-size scaling that ignores disorder gives a shifted critical point and too large a critical exponent. Sec. VIII: reduced fidelity falls for low-temperature initial states |
| 2 | C. Monroe, W. C. Campbell, L.-M. Duan, Z.-X. Gong, A. V. Gorshkov, P. W. Hess, R. Islam, K. Kim, N. M. Linke, G. Pagano, P. Richerme, C. Senko and N. Y. Yao, Programmable quantum simulations of spin systems with trapped ions, Rev. Mod. Phys. 93, 025001 (2021); read as preprint arXiv:1912.07845 | doi:10.1103/RevModPhys.93.025001 | full text | Sec. II: verify that the intended Hamiltonian is implemented; small-system agreement with theory, cross-platform comparison and forward-backward evolution as checks, with scaling up adding imperfections. Sec. II.A: higher-order terms beyond the Ising model and spin-motion entanglement, non-adiabatic errors, SPAM error probability growing with qubit number, detection crosstalk, decoherence sources growing with system size. Sec. II.B: Ising couplings measured by spectroscopy, pair oscillations and global precession. Sec. III.A.2: error bars include estimated drifts of the couplings; ramp profiles compared; ramps must be slow against a gap whose scaling with size is often unknown. Sec. III.B.2: a finite system shows a crossover that sharpens with size, analysed with scaled order parameters and the Binder cumulant. Sec. IV.C (prethermalization): open boundaries with long-range interactions create inhomogeneity in an otherwise homogeneous chain |
| 3 | A. J. Daley, I. Bloch, C. Kokail, S. Flannigan, N. Pearson, M. Troyer and P. Zoller, Practical quantum advantage in quantum simulation, Nature 607, 667–676 (2022); read as the accepted manuscript in the Strathclyde repository (Strathprints 82197) | doi:10.1038/s41586-022-04940-6 | full text | Secs. I and III.A: without error correction, accuracy is limited by calibration of the implemented model, alongside decoherence and noise; calibration errors can be estimated by Hamiltonian learning; decoherence bounds the time over which coherent dynamics can be followed. Sec. II: methods with uncontrolled approximations such as mean-field need benchmarking against controlled ones; Fig. 2 shows matrix-product-state truncation errors. Sec. IV.A: calibration errors grow slowly in time. Sec. IV.B and Box 3: beyond classical reach, verification by cross-platform comparison and by Hamiltonian learning, comparing the reconstructed Hamiltonian with the intended one |
| 4 | J. Eisert, D. Hangleiter, N. Walk, I. Roth, D. Markham, R. Parekh, U. Chabaud and E. Kashefi, Quantum certification and benchmarking, Nat. Rev. Phys. 2, 382–390 (2020); read as preprint arXiv:1910.06343 | doi:10.1038/s42254-020-0186-4 | full text | Section on certification protocols: in the paragraph before Box 4, Hamiltonian learning recovers the parameters of an assumed model from data; in the paragraph after Box 4, quantum simulators are commonly certified by comparison with classical simulation in classically tractable regimes, which assumes that no new error sources arise outside the certified regime, and cross-platform verification or self-validation can in some instances give stronger statements |
| 5 | J. P. F. LeBlanc, A. E. Antipov, F. Becca, I. W. Bulik, G. K.-L. Chan, C.-M. Chung, Y. Deng, M. Ferrero, T. M. Henderson, C. A. Jiménez-Hoyos, E. Kozik, X.-W. Liu, A. J. Millis, N. V. Prokof'ev, M. Qin, G. E. Scuseria, H. Shi, B. V. Svistunov, L. F. Tocchio, I. S. Tupitsyn, S. R. White, S. Zhang, B.-X. Zheng, Z. Zhu and E. Gull, Solutions of the two-dimensional Hubbard model: benchmarks and results from a wide range of numerical algorithms, Phys. Rev. X 5, 041041 (2015) | doi:10.1103/PhysRevX.5.041041 | full text | Abstract and Sec. I: comparing many methods identifies their uncertainties and systematic errors, and extrapolation to the thermodynamic limit with quantified uncertainty is needed for meaningful comparison. Secs. III and IV: method-specific systematic errors such as the constrained-path approximation to the sign problem, Trotter-step extrapolation, DMRG extrapolation in the number of kept states and finite-size extrapolation |
| 6 | D. C. McKay and B. DeMarco, Cooling in strongly correlated optical lattices: prospects and challenges, Rep. Prog. Phys. 74, 054401 (2011); read as preprint arXiv:1010.0198 | doi:10.1088/0034-4885/74/5/054401 | full text | Sec. 1.2: with a trap, phases of the uniform model appear in shells, often treated by the local-density approximation, with trap effects on critical behaviour beyond it. Sec. 2: entropy, not temperature alone, controls the phases. Sec. 2.1: lessons from cryogenic thermometry, such as checking consistency between thermometers. Sec. 4: distinguishes primary from secondary thermometers. Sec. 4.1: the isentropic-loading assumption relies on theory and on adiabaticity that heating violates; heating can be measured by a load and unload round trip; global adiabaticity may need much longer ramps than used. Sec. 4.6: the mature methods need extensive theoretical input |
| 7 | A. Eckardt, Colloquium: Atomic quantum gases in periodically driven optical lattices, Rev. Mod. Phys. 89, 011004 (2017); read as preprint arXiv:1606.08041 | doi:10.1103/RevModPhys.89.011004 | full text | Sec. II: the effective Hamiltonian of a driven system is obtained by a high-frequency expansion truncated at low order, with micromotion on top, and is accurate only for times short compared with a heating time. Sec. III.I: higher-order corrections modify interactions. Sec. IV.C: resonant interband and intraband excitations cause heating, whose time scale must exceed the duration of the experiment |
| 8 | A. Browaeys and T. Lahaye, Many-body physics with individually controlled Rydberg atoms, Nat. Phys. 16, 132–142 (2020); read as preprint arXiv:2002.07413 | doi:10.1038/s41567-019-0733-z | full text | Sec. IV: the spin-model mapping assumes coherent excitation and a laser uniform over the array. Sec. V: dynamics compared with a many-body Schrödinger-equation solution that includes the experimental imperfections, as a benchmark where exact calculation is possible. Sec. VII: fidelity requires understanding the limits of the excitation scheme and mapping the complex Rydberg level structure onto two-level systems |
| 9 | S. de Léséleuc, D. Barredo, V. Lienhard, A. Browaeys and T. Lahaye, Analysis of imperfections in the coherent optical excitation of single atoms to Rydberg states, Phys. Rev. A 97, 053803 (2018); read as preprint arXiv:1802.10424 | doi:10.1103/PhysRevA.97.053803 | full text | Sec. II: preparation errors, false positives (a lost ground-state atom read as Rydberg) and false negatives reduce contrast, and each is modelled and measured. Secs. III and IV: damping results from several small effects of a few per cent each, explained by models built from independently measured imperfections |
| 10 | C. Gross and W. S. Bakr, Quantum gas microscopy for single atom and spin detection, Nat. Phys. 17, 1316–1323 (2021); read as preprint arXiv:2010.15407 | doi:10.1038/s41567-021-01370-5 | full text | Section on optical lattices: site-occupation reconstruction gives a fidelity well above 99% for distinguishing zero from one atom at typical signal-to-noise. Section on quantum gas microscopy: near-resonant imaging light removes atom pairs by light-assisted collisions, so microscopes detect the parity of site occupation. Section on new directions and Fig. 3: bilayer schemes are used to circumvent parity projection |
