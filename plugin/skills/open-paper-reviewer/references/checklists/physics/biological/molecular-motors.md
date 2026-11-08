---
id: T-MOLECULAR-MOTORS
name: Molecular motors and step detection
type: technique
field: physics/biological
applies_when: the paper tracks single motor proteins or other molecular machines with optical or magnetic tweezers, bead or fluorescence tracking, and bases a claim about step size, substeps, dwell times, velocity, stall force, ATP or load dependence, or stepping mechanism on the traces
version: "0.1"
---

# Molecular motors and step detection

## 1. Step detection and its false-positive rate

**Question.** Which algorithm turned the traces into steps, how were its parameters and stopping rule chosen, and does the paper show, on simulated traces with the same noise, sampling rate and dwell times as the data, how often the algorithm finds steps that are not there and misses steps that are?

**Why it matters.** Any step finder can fit steps to noise or merge real steps, and its output depends on tuning parameters, prefiltering and the assumed noise model. Noise in tweezers data is often correlated in time, and an algorithm that assumes white noise can then report many more steps than are present. Steps comparable to the noise and steps after short dwells are the first to be missed, which shifts the step-size and dwell-time distributions.

**Resolved by.** The algorithm, its parameters and the criterion for the number of steps stated; the noise level, its correlation time and the step size compared; a test on simulated or step-injected traces matching the data, reporting detection probability against step size and the rate of spurious steps; the noise model checked against the data, for example by its autocorrelation; uncertainties on step sizes and times, for example by bootstrap; the fitted steps overlaid on raw traces.

**Benchmark.** [1], [2], [3]

## 2. Compliance of the links between motor and probe

**Question.** Through which elements (motor stalk, linkers, DNA handles, antibodies, bead or filament attachment) is the motor coupled to the probe, how stiff are they compared with the trap or probe, and how does the paper correct the probe displacement, the load and the time resolution for them?

**Why it matters.** Compliant links in series mean the probe moves less than the motor, so displacements, working strokes and stiffnesses can be underestimated, and reported values of motor stiffness and force span a wide range partly for this reason. The time resolution of the assay also limits what can be seen: events shorter than the detection window are not detected, so short dwells and fast substeps can be lost.

**Resolved by.** The coupling geometry described; the combined link stiffness measured, for example from the probe's fluctuations when the motor is bound, and used to convert probe displacement to motor displacement; the load on the motor calculated with the link stiffness included; the response time of probe and links compared with the shortest dwells and substeps claimed; where possible, a check with a stiffer coupling or a label closer to the motor.

**Benchmark.** [4], [5]

## 3. One motor per probe

**Question.** What evidence shows that each trace was produced by a single motor and not by two or more motors on the same bead, filament or cargo?

**Why it matters.** The number of motors on a bead is usually unknown, and the common practice of diluting motors until only a fraction of beads move, then assuming Poisson statistics, can underestimate how often several motors engage, because the motor can stretch further than assumed and reach the track from more of the bead surface. Several motors carry a bead further than one, and a cargo moved by several motors can show steps smaller than a single motor's step.

**Resolved by.** The motor-to-bead ratio and the fraction of motile beads reported at several dilutions, with the expected share of multiple-motor events estimated from a model that is stated; run length, velocity and force shown not to change with motor density in the range used; where possible, an independent count, such as photobleaching steps of labelled motors.

**Benchmark.** [3], [6]

## 4. Surface attachment and force geometry

**Question.** How were the motor and its track attached to the bead, coverslip or pedestal, in what orientation, and in what direction does the load act on the motor in this geometry?

**Why it matters.** Nonspecific adsorption to a surface leaves motors in random orientations and can change their activity, and measured displacements and velocities have been shown to depend on the attachment chemistry and orientation. In the common single-bead assay the bead's size and position give the load a component perpendicular to the track that can exceed the component along it; this component shortens attachment and changes detachment forces and stall behaviour, so the measured load dependence is partly a property of the assay geometry.

**Resolved by.** The attachment chemistry stated, preferably specific and at a defined site; motor activity checked after attachment, for example against solution ATPase or gliding velocity; bead size and motor length given and the perpendicular load component estimated; the key result checked in a second geometry, such as a different bead size or a dumbbell assay, or its dependence on geometry discussed.

**Benchmark.** [4], [7]

## 5. Dwell-time analysis

**Question.** How were the dwell-time distributions fitted (binning or maximum likelihood, which functions, how many components), how were dwells shorter than the instrument's dead time or longer than the record handled, and are the numbers of rate-limiting steps or rate constants drawn from the distributions supported by the stated model assumptions?

**Why it matters.** Short dwells are missed when they fall below the detection window, and long ones are cut off at the end of a record, so a fit that ignores these limits biases the rates and the relative weight of components. Histogram fits depend on the binning, and adding exponential components always improves a fit. Lower bounds on the number of hidden steps from the shape of the distribution or the randomness parameter rest on assumptions, such as a linear scheme without branches and with an irreversible final step, that need not hold for the motor.

**Resolved by.** Maximum-likelihood fits of unbinned dwells with the dead time built into the fitted function; extra components justified by a likelihood-ratio or information criterion test; confidence intervals on rates; the number of dwells per condition reported; for alternating or reversible stepping, a kinetic model fitted to the dwell sequence instead of a single histogram; the assumptions behind any number of rate-limiting steps stated and checked.

**Benchmark.** [4], [8], [9], [11]

## 6. ATP and load dependence

**Question.** Over what range of ATP concentrations and loads were velocity, dwell times, stall force and run length measured, was the load held constant during each measurement or does it change as the motor moves, and how were load-dependent rates and Michaelis–Menten parameters extracted?

**Why it matters.** Load changes both the maximum velocity and the apparent Michaelis constant for ATP, and stall force can itself depend on ATP concentration, so a value at one ATP concentration or one load does not describe the motor. In a stationary trap the load rises as the motor moves, so velocities and dwell times are averages over a changing load. Velocity alone cannot separate kinetic models, which differ in their predictions for step ratios and dwell times.

**Resolved by.** Velocity and dwell times measured over a range of ATP concentrations spanning the Michaelis constant, at several loads; constant load from a force clamp, or the load at each step stated; the load direction specified; the forward and backward step fractions and the dwell times before each reported with load; Michaelis–Menten and force-dependent fits shown with their parameters and uncertainties.

**Benchmark.** [10], [11], [12]

## 7. From stepping data to mechanism

**Question.** Which alternative mechanisms does the paper consider, which observable would distinguish them (step size of a labelled head or domain, alternation of dwells, backward steps, ATP and load dependence), and does the inferred kinetic scheme have no more free parameters than the data constrain?

**Why it matters.** The apparent step size of a fluorescent label depends on where it sits on the motor, so the same motion can look like uniform or alternating steps. An observed step need not be one complete chemical cycle: hidden substeps and chemical transitions without movement are invisible in position records, and treating each step as a full cycle misreads step ratios and dwell times, especially near stall. Kinetic schemes with many states can fit the same data, so a good fit does not single one out.

**Resolved by.** Predictions of each candidate mechanism set out and compared with the data, for example label position against apparent step size, or alternating dwell kinetics; conditional dwell times before forward and backward steps reported; the kinetic scheme compared with simpler ones by an information criterion; the claim worded as consistent with the data where alternatives remain.

**Benchmark.** [10], [11], [13], [14], [15]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | S. G. Arunajadai and W. Cheng, Step detection in single-molecule real time trajectories embedded in correlated noise, PLoS ONE 8, e59279 (2013) | doi:10.1371/journal.pone.0059279 |
| 2 | L. Loeff et al., AutoStepfinder: a fast and automated step detection method for single-molecule analysis, Patterns 2, 100256 (2021) | doi:10.1016/j.patter.2021.100256 |
| 3 | B. C. Carter et al., A comparison of step-detection methods: how well can you do?, Biophys. J. 94, 306 (2008) | doi:10.1529/biophysj.107.110601 |
| 4 | A. Månsson et al., Do actomyosin single-molecule mechanics data predict mechanics of contracting muscle?, Int. J. Mol. Sci. 19, 1863 (2018) | doi:10.3390/ijms19071863 |
| 5 | A. L. Nord et al., Kinetic analysis methods applied to single motor protein trajectories, Phys. Chem. Chem. Phys. 20, 18775 (2018) | doi:10.1039/c8cp03056a |
| 6 | Q. Li et al., Quantitative determination of the probability of multiple-motor transport in bead-based assays, Biophys. J. 110, 2720 (2016) | doi:10.1016/j.bpj.2016.05.015 |
| 7 | S. Pyrpassopoulos et al., Modulation of kinesin's load-bearing capacity by force geometry and the microtubule track, Biophys. J. 118, 243 (2020) | doi:10.1016/j.bpj.2019.10.045 |
| 8 | L. S. Milescu et al., Maximum likelihood estimation of molecular motor kinetics from staircase dwell-time sequences, Biophys. J. 91, 1156 (2006) | doi:10.1529/biophysj.105.079541 |
| 9 | M. S. Woody et al., MEMLET: an easy-to-use tool for data fitting and model comparison using maximum-likelihood estimation, Biophys. J. 111, 273 (2016) | doi:10.1016/j.bpj.2016.06.019 |
| 10 | D. Tsygankov et al., Back-stepping, hidden substeps, and conditional dwell times in molecular motors, Phys. Rev. E 75, 021909 (2007); read as preprint arXiv:q-bio/0611051 | doi:10.1103/PhysRevE.75.021909 |
| 11 | D. Chowdhury, Stochastic mechano-chemical kinetics of molecular motors: a multidisciplinary enterprise from a physicist's perspective, Phys. Rep. 529, 1 (2013); read as preprint arXiv:1207.6070 | doi:10.1016/j.physrep.2013.03.005 |
| 12 | K. Visscher et al., Single kinesin molecules studied with a molecular force clamp, Nature 400, 184 (1999) | doi:10.1038/22146 |
| 13 | A. Yildiz et al., Myosin V walks hand-over-hand: single fluorophore imaging with 1.5-nm localization, Science 300, 2061 (2003) | doi:10.1126/science.1084398 |
| 14 | A. Yildiz et al., Kinesin walks hand-over-hand, Science 303, 676 (2004) | doi:10.1126/science.1093753 |
| 15 | J. Jarillo et al., DNA replication: in vitro single-molecule manipulation data analysis and models, Comput. Struct. Biotechnol. J. 19, 3765 (2021) | doi:10.1016/j.csbj.2021.06.032 |
