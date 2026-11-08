---
id: T-MACROSCOPIC-QUANTUM-TESTS
name: Tests of quantum mechanics at large scales
type: technique
field: physics/gravitation-precision
applies_when: the paper reports matter-wave interference of large molecules, clusters or nanoparticles, a quantum state of motion of a levitated or optomechanical system, or bounds on collapse models, decoherence mechanisms or macroscopicity derived from such experiments
version: "0.1"
---

# Tests of quantum mechanics at large scales

## 1. Quantum interference versus classical fringes

**Question.** For near-field (Talbot-Lau type) interference, does the paper compare the measured fringe visibility with both the quantum prediction and the classical moiré or shadow prediction for the same geometry, and does it show how the visibility depends on particle velocity or de Broglie wavelength?

**Why it matters.** In a three-grating near-field interferometer, classical particles on straight paths also produce a moiré fringe pattern, so fringes alone do not show wave behaviour. The two descriptions differ in how the visibility depends on velocity: the classical visibility does not depend on it, while the quantum visibility varies with wavelength.

**Resolved by.** Visibility measured as a function of velocity, wavelength or grating separation and compared with both models, each including the same particle-grating interaction; a design in which the expected quantum visibility clearly exceeds the largest classical value; the classical calculation stated, not only asserted.

**Benchmark.** [1]

## 2. Grating interaction, velocity spread and particle identity

**Question.** How does the model include the van der Waals or Casimir-Polder interaction with material gratings and the measured velocity distribution, and how does the paper establish that the detected particles are intact particles of the mass that the claim refers to?

**Why it matters.** Polarisable particles passing a material grating pick up a velocity-dependent phase that grows with particle size, so the visibility becomes very sensitive to the velocity spread. Detection by ionisation and mass spectrometry can fragment large particles, and surface detection makes intact particles hard to tell from fragments, so the mass of the interfering object may differ from the one quoted.

**Resolved by.** The interaction potential and its parameters stated and their effect on the predicted visibility shown, or optical gratings used where the interaction would dominate; the velocity distribution measured and used in the model; mass spectra or another identification showing the selected mass, with fragmentation and the mass distribution of the beam accounted for.

**Benchmark.** [1]

## 3. Decoherence from gas and thermal radiation

**Question.** For the stated pressure, gas composition, environment temperature and internal temperature of the particle, does the paper calculate the decoherence rates from gas collisions, from emission, absorption and scattering of thermal radiation, and from scattering of trapping or grating light, and compare them with the observed coherence or the effect claimed?

**Why it matters.** For large particles a single gas collision usually reveals which path was taken, so collisional decoherence scales with pressure and cross-section and does not fall for smaller superpositions. Thermal emission rises steeply with the internal temperature, and absorbed laser light heats particles well above their surroundings. Loss of visibility that the budget misses can be taken for a new effect, and an underestimated budget overstates the sensitivity to modified dynamics.

**Resolved by.** Pressure measured at the experiment and the gas composition given; the internal temperature measured or bounded, not assumed equal to the environment; rates calculated in the appropriate wavelength limit with the dielectric properties used; pressure or internal temperature varied deliberately and the visibility shown to follow the predicted dependence.

**Benchmark.** [1], [3], [4]

## 4. Dephasing distinguished from decoherence

**Question.** How does the paper bound the loss of visibility from grating or trap vibrations, from inertial forces such as gravity and the rotation of the Earth, and from fluctuating fields, and does it separate these phase-averaging effects from decoherence?

**Why it matters.** Classical noise that shifts the fringes differently for different particles or runs washes out the pattern without any which-path information reaching the environment, yet it reduces the visibility in the same way. Grating vibrations of a few nanometres can remove the fringes, and an acceleration shifts them by an amount that depends on transit time, so a spread of velocities turns it into visibility loss.

**Resolved by.** The vibration spectrum measured and converted into phase noise; inertial phase shifts calculated for the velocity distribution and compensated, for example by orienting the gratings or by pulsed gratings that fix the interaction time; the stability of the fringe phase over the measurement shown.

**Benchmark.** [1]

## 5. Excess noise as a test of collapse models

**Question.** When a bound on a collapse model comes from heating, force noise, diffusion or radiation emission, does the paper model every ordinary noise source, treat the residual as a bound, and say what an unexplained excess would need to show before it could be attributed to collapse?

**Why it matters.** Non-interferometric tests compare the measured noise with the sum of thermal, gas, radiation, radioactive and other contributions, and the collapse bound is set by the residual. Overestimating the known contributions makes the bound look tighter than it is, and an unexplained excess is at most a hint, because any unmodelled source gives the same signature.

**Resolved by.** An itemised noise budget, each term supported by an independent measurement such as temperature, pressure or background radiation; the residual with its uncertainty converted into a bound at a stated confidence level; the sensitivity of the bound to each subtraction shown; any excess tested against the dependence on mass and density that the model predicts before an interpretation is offered.

**Benchmark.** [5]

## 6. Which model, and excluded or bounded

**Question.** Does the paper state which model and variant its result applies to (for example CSL with white or coloured noise, dissipative CSL, or DP), give the result as a region of that model's parameter space at stated values of the other parameters, and say whether it excludes the model, a proposed parameter value, or only a range?

**Why it matters.** Results are bounds on the collapse rate λ at each correlation length r_C, not on the model as a whole, so a bound at one r_C does not carry over to another, and proposed values of λ span many orders of magnitude. Coloured and dissipative variants add parameters such as a frequency cutoff or a noise temperature, and some predictions, notably radiation emission, depend strongly on the noise spectrum. A model is excluded outright only where a version without free parameters predicts more than the bound allows.

**Resolved by.** An exclusion plot in the plane of λ and r_C, or a bound on the DP cutoff length, with its confidence level; the variant and any extra parameters stated; comparison with specific proposed values without claiming more than the bound covers; the assumptions the bound depends on, such as mass distribution and noise spectrum, listed.

**Benchmark.** [5], [6]

## 7. Measures of macroscopicity

**Question.** When the paper claims a more macroscopic superposition than before, which measure does it use, how is it computed from the mass, superposition size, coherence time and demonstrated visibility, and is the comparison with earlier experiments made with the same measure?

**Why it matters.** Many measures of macroscopicity exist; they are not equivalent, can rank the same states differently, and several depend on a choice of partition, observable or branches. Mass or particle number alone is not a measure: a large system with a short coherence time can rank below a lighter one. A value needs coherence between the distinct states to be shown, not only populations.

**Resolved by.** The measure named and calculated with its inputs and assumptions given, including the fraction of the expected visibility actually demonstrated; comparisons made with the same measure applied to the other experiments; the claim of size limited to what the measure supports.

**Benchmark.** [2], [7]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | K. Hornberger et al., Colloquium: Quantum interference of clusters and molecules, Rev. Mod. Phys. 84, 157 (2012); read as arXiv:1109.5937 | doi:10.1103/RevModPhys.84.157 |
| 2 | S. Nimmrichter and K. Hornberger, Macroscopicity of mechanical quantum superposition states, Phys. Rev. Lett. 110, 160403 (2013); read as arXiv:1205.3447 | doi:10.1103/PhysRevLett.110.160403 |
| 3 | O. Romero-Isart, Quantum superposition of massive objects and collapse models, Phys. Rev. A 84, 052121 (2011); read as arXiv:1110.4495 | doi:10.1103/PhysRevA.84.052121 |
| 4 | C. Gonzalez-Ballestero et al., Levitodynamics: Levitation and control of microscopic objects in vacuum, Science 374, eabg3027 (2021); read as arXiv:2111.05215 | doi:10.1126/science.abg3027 |
| 5 | M. Carlesso et al., Present status and future challenges of non-interferometric tests of collapse models, Nat. Phys. 18, 243 (2022); read as arXiv:2203.04231 | doi:10.1038/s41567-021-01489-5 |
| 6 | A. Bassi et al., Models of wave-function collapse, underlying theories, and experimental tests, Rev. Mod. Phys. 85, 471 (2013); read as arXiv:1204.4325 | doi:10.1103/RevModPhys.85.471 |
| 7 | F. Fröwis et al., Macroscopic quantum states: Measures, fragility, and implementations, Rev. Mod. Phys. 90, 025004 (2018); read as arXiv:1706.06173 | doi:10.1103/RevModPhys.90.025004 |
