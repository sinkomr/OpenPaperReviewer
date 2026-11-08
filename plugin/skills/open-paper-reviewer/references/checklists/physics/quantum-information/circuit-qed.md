---
id: T-CIRCUIT-QED
name: Microwave resonators and circuit QED
type: technique
field: physics/quantum-information
applies_when: the paper reports internal, coupling or loaded quality factors, loss tangents or frequency shifts of a planar or three-dimensional superconducting resonator, a photon number in it, a qubit-resonator coupling or dispersive shift, or claims strong or ultrastrong coupling in a superconducting circuit
version: "0.1"
---

# Microwave resonators and circuit QED

## 1. Which quality factor is reported

**Question.** Does the paper state whether each quality factor is loaded, coupling (external) or internal, how the resonator was measured (side-coupled to a feedline, inline transmission or reflection), and how the coupling quality factor compares with the internal one?

**Why it matters.** The linewidth gives only the loaded quality factor. Splitting it into coupling and internal parts needs a reference for the size of the resonance, which an uncalibrated inline transmission measurement lacks. When coupling loss is much larger than internal loss the line shape is set by the coupling and the internal value is poorly determined; when it is much smaller the signal is weak.

**Resolved by.** Every quality factor labelled; the measurement configuration given; coupling values reported next to internal ones; internal values taken from resonators whose coupling and internal quality factors are of the same order, or the larger uncertainty outside that regime stated.

**Benchmark.** [1], [2]

## 2. Line-shape model, background and stray paths

**Question.** Is the fitting model given, does it use the complex scattering data and allow for an asymmetric line shape, how were cable delay, gain and the off-resonance background removed, and could a signal path that bypasses the resonator contribute?

**Why it matters.** Impedance mismatch makes the line shape asymmetric, and a model that only adds a rotation overestimates the internal quality factor by an amount that grows with the asymmetry. Interference with a background path makes the internal quality factor uncertain even when the line shape looks symmetric, much more so for overcoupled resonators, and can produce apparent trends when the resonance is tuned. A calibration made at room temperature does not remove mismatches that appear on cooling, and all fit methods lose precision at the low signal-to-noise ratios of single-photon measurements.

**Resolved by.** The model or a named method (for example a circle fit with diameter correction) stated; fits shown in the complex plane as well as in magnitude; raw data over a span wider than the resonance; the normalisation described well enough to repeat; leakage characterised in situ, or a range for the internal quality factor derived from a bound on it; the signal-to-noise ratio of the lowest-power traces stated; calibration at the measurement temperature where the configuration needs it.

**Benchmark.** [1], [2], [3], [4], [5], [6]

## 3. Power at the resonator and photon-number calibration

**Question.** How was the mean photon number in the resonator obtained (from the applied power and the line attenuation, or from an ac Stark shift of a coupled qubit), with what uncertainty, and is the response shown to be linear over the range that was fitted?

**Why it matters.** Loss in superconducting resonators depends on the circulating power, and the power at the device is hard to know: it rests on the attenuation of the cold lines and on the fitted quality factors, and reflections can make it larger on paper than in fact. An ac Stark shift gives the photon number only if χ is known independently, and its linear dependence on power holds only well below the critical photon number. At strong drive the resonance becomes asymmetric and depends on sweep direction, through kinetic-inductance nonlinearity, heating, weak links or vortices.

**Resolved by.** The formula and the attenuation, coupling and quality factors behind the photon number given with an uncertainty; where an ac Stark shift is used, the value and source of χ stated and the photon numbers compared with the critical photon number; a power sweep that reaches the regime the claim concerns, down to the single-photon level where that is claimed; fitted traces free of distortion and of dependence on sweep direction.

**Benchmark.** [1], [7], [10]

## 4. Sample temperature, shielding and trapped flux

**Question.** Are the sample temperature, its thermal anchoring and the magnetic and infrared shielding described, with evidence that the sample reached the quoted temperature?

**Why it matters.** A sample warmer than the refrigerator stage shows less two-level-system loss than it would at the quoted temperature, so loss is under-reported. Stray infrared light from warmer stages creates quasiparticles that can limit the quality factor, and flux trapped on cooling through the transition in a residual field adds loss and a frequency shift.

**Resolved by.** The mounting and thermalisation described; the shielding specified (magnetic shield, light-tight or absorber-coated enclosure, filtered lines); a temperature sweep down to base temperature showing the behaviour expected if the sample follows the thermometer.

**Benchmark.** [1], [8]

## 5. Assigning loss or a frequency shift to one mechanism

**Question.** When a loss or a frequency shift is attributed to one mechanism (two-level systems, quasiparticles, vortices, radiation, seams or a coupled sample), is the attribution supported by its dependence on power, temperature, field or geometry, with the other contributions bounded, and on how many resonators and cooldowns does it rest?

**Why it matters.** Measured loss is a sum of power-dependent and power-independent channels, so a single low-power value is not the two-level-system loss when other losses are comparable to it. Two-level systems and thermal quasiparticles shift the frequency in opposite directions with temperature, and a single-mechanism fit to data containing both returns unphysical parameters. Nominally identical resonators can differ in internal quality factor by up to an order of magnitude and the same resonator can change between cooldowns, so a comparison of one resonator per condition may lie within the spread.

**Resolved by.** Power and temperature sweeps both shown and fitted with consistent parameters; loss and frequency shift analysed together; competing mechanisms measured separately or bounded, including seam and parasitic-mode losses in 3D cavities; several resonators per condition and repeated cooldowns, with ranges or distributions.

**Benchmark.** [1], [11]

## 6. From quality factor to a loss tangent or material property

**Question.** When a loss tangent, surface resistance, kinetic-inductance fraction or other material quantity is derived, is the electromagnetic model of the resonator given, including the participation (filling) factor of the material of interest and the losses of the rest of the structure?

**Why it matters.** The measured quality factor includes losses in walls, conductors, interfaces and joints, and these set the smallest loss tangent that can be resolved. Converting frequency and quality factor into a material property needs a field solution for the actual structure, and when the material of interest holds only a small fraction of the energy the result is sensitive to every other loss channel. Results from different geometries can be compared only through their participation factors.

**Resolved by.** The analytic or numerical model stated; electric and magnetic participation ratios reported for each lossy region; parasitic losses computed or measured with a reference configuration and shown to be small compared with the loss assigned to the material; for 3D cavities, the treatment of seams and joints that carry current described.

**Benchmark.** [1], [9], [11]

## 7. Dispersive shift and the coupling it implies

**Question.** How was the dispersive shift measured (qubit-state-dependent resonator frequency, or photon-number splitting of the qubit line), which model links it to g and the detuning, and is the device in the regime where that model holds?

**Why it matters.** The two-level Jaynes-Cummings expression for the dispersive shift predicts it poorly for a transmon, whose higher levels make the shift depend on its anharmonicity, so a coupling inferred from a two-level formula can be wrong. The perturbative expressions hold only for detuning large compared with g and for photon numbers well below the critical photon number, and fail near the straddling regime where the detuning is comparable to the anharmonicity. The frequencies entering the formulas are bare ones, while measured frequencies are dressed.

**Resolved by.** The dispersive shift measured directly, with the method stated; the model named, including the qubit's higher levels, or a numerical diagonalisation where the device is close to resonance or in the straddling regime; bare and dressed frequencies distinguished; the photon numbers used compared with the critical photon number.

**Benchmark.** [10]

## 8. Strong and ultrastrong coupling claims

**Question.** For a claim of strong coupling, is the splitting measured at low excitation and compared with the linewidths of both the resonator and the qubit or other system, and for a claim of a quantum or ultrastrong regime, is evidence given beyond a single avoided crossing?

**Why it matters.** Strong coupling requires the splitting 2g to exceed the dressed-state linewidth, set by both the resonator and the qubit decay rates. At weak excitation a coupled qubit and resonator respond like two coupled classical oscillators, so a resolved avoided crossing alone shows neither field quantisation nor entanglement; with N emitters the collective coupling grows as the square root of N. In the ultrastrong regime the counter-rotating terms add shifts and change the ground state, which the usual models omit.

**Resolved by.** The splitting, the resonator decay rate and the qubit decay and dephasing rates reported together, with the probe power or photon number at which the splitting was measured; the full avoided crossing shown as the qubit is tuned; the number of coupled emitters stated where it may exceed one; for quantum claims, the square-root photon-number dependence of the higher transitions or a direct state measurement; for ultrastrong claims, the coupling stated relative to the bare system frequencies and spectra fitted with a model that keeps the counter-rotating terms.

**Benchmark.** [10], [12], [13]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | C. R. H. McRae et al., Materials loss measurements using superconducting microwave resonators, Rev. Sci. Instrum. 91, 091101 (2020); read as arXiv:2006.04718 | doi:10.1063/5.0017378 |
| 2 | S. Probst et al., Efficient and robust analysis of complex scattering data under noise in microwave resonators, Rev. Sci. Instrum. 86, 024706 (2015); read as arXiv:1410.3365 | doi:10.1063/1.4907935 |
| 3 | M. S. Khalil et al., An analysis method for asymmetric resonator transmission applied to superconducting devices, J. Appl. Phys. 111, 054510 (2012); read as arXiv:1108.3117 | doi:10.1063/1.3692073 |
| 4 | D. Rieger et al., Fano interference in microwave resonator measurements, Phys. Rev. Applied 20, 014059 (2023); read as arXiv:2209.03036 | doi:10.1103/PhysRevApplied.20.014059 |
| 5 | P. J. Petersan and S. M. Anlage, Measurement of resonant frequency and quality factor of microwave resonators: Comparison of methods, J. Appl. Phys. 84, 3392 (1998); read as arXiv:cond-mat/9805365 | doi:10.1063/1.368498 |
| 6 | H. Wang et al., Cryogenic single-port calibration for superconducting microwave resonator measurements, Quantum Sci. Technol. 6, 035015 (2021); arXiv:2103.01491 | doi:10.1088/2058-9565/ac070e |
| 7 | L. J. Swenson et al., Operation of a titanium nitride superconducting microresonator detector in the nonlinear regime, J. Appl. Phys. 113, 104501 (2013); read as arXiv:1305.4281 | doi:10.1063/1.4794808 |
| 8 | R. Barends et al., Minimizing quasiparticle generation from stray infrared light in superconducting quantum circuits, Appl. Phys. Lett. 99, 113507 (2011); arXiv:1105.4642, which carries an earlier title | doi:10.1063/1.3638063 |
| 9 | J. Krupka, Microwave measurements of electromagnetic properties of materials, Materials 14, 5097 (2021) | doi:10.3390/ma14175097 |
| 10 | A. Blais et al., Circuit quantum electrodynamics, Rev. Mod. Phys. 93, 025005 (2021); read as arXiv:2005.12667 | doi:10.1103/RevModPhys.93.025005 |
| 11 | M. Reagor et al., Reaching 10 ms single photon lifetimes for superconducting aluminum cavities, Appl. Phys. Lett. 102, 192604 (2013); read as arXiv:1302.4408 | doi:10.1063/1.4807015 |
| 12 | Y. Zhu et al., Vacuum Rabi splitting as a feature of linear-dispersion theory: Analysis and experimental observations, Phys. Rev. Lett. 64, 2499 (1990) | doi:10.1103/PhysRevLett.64.2499 |
| 13 | A. Frisk Kockum et al., Ultrastrong coupling between light and matter, Nat. Rev. Phys. 1, 19 (2019); read as arXiv:1807.11636 | doi:10.1038/s42254-018-0006-2 |
