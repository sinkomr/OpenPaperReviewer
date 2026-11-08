---
id: T-CAVITY-QED
name: Cavity quantum electrodynamics
type: technique
field: physics/amo
applies_when: the paper couples atoms to an optical or microwave cavity mode and reports a coupling strength, cooperativity, vacuum Rabi or normal-mode splitting, strong coupling, Purcell enhancement, cavity-enhanced emission or single-photon nonlinearities of an atom-cavity system
version: "0.1"
---

# Cavity quantum electrodynamics

## 1. Rate and cooperativity conventions

**Question.** Does the paper define g, κ and γ (field or energy decay, half or full widths, angular or cyclic frequency) and the formula used for the cooperativity, so that its numbers can be compared with other work and with the strong-coupling criterion it applies?

**Why it matters.** The literature uses several conventions that differ by factors of two: the atom-cavity exchange runs at 2g, the empty-cavity linewidth is 2κ when κ is the field decay rate, and one common cooperativity is twice another. Mixing conventions within a paper, or between a paper and the work it compares with, changes a claimed cooperativity or a strong-coupling margin by a factor of two or four.

**Resolved by.** Each rate defined in words and by formula, with its relation to the measured linewidths; the cooperativity formula stated and, where results are compared with other work, converted to a common convention; the single-atom value kept separate from any collective value for N atoms.

**Benchmark.** [1], [2]

## 2. Cavity parameters and mode structure

**Question.** How were κ, the finesse and the mode waist obtained (ringdown, linewidth against a calibrated frequency scale, or calculated from mirror data), and does the paper account for split or nearly degenerate cavity modes, such as two polarisation modes, and for the atomic transitions that couple to each?

**Why it matters.** The ideal coupling follows from the dipole matrix element and the mode volume, and the cooperativity from the finesse and the waist, so any error in these inputs passes into the claimed g and C. A linewidth read from a length scan needs an independent frequency calibration, and losses from scatter, absorption or clipping reduce the finesse and the useful output without being visible in the mirror transmission. Mirror birefringence splits the mode into two polarisations, and an atom with several Zeeman sublevels couples to them with different strengths, which reshapes the spectrum.

**Resolved by.** κ measured directly by ringdown or by a linewidth with a calibrated frequency axis, and quoted with the free spectral range; the waist and mode volume derived from the stated geometry; transmission and losses separated where the output efficiency matters; any polarisation-mode splitting measured and included in the model, together with the relevant atomic transitions and their coupling coefficients.

**Benchmark.** [2], [4], [5], [6]

## 3. Atom number, position and motion

**Question.** How many atoms couple to the mode in each data set, how is that number known, and how do the atoms' positions in the standing wave, their motion and any trap-induced light shifts enter the quoted coupling?

**Why it matters.** With N atoms the collective coupling grows as the square root of N, so a splitting from several atoms can be mistaken for single-atom coupling, and a single-atom g inferred from an ensemble inherits the uncertainty in N. The coupling varies along the standing wave and across the mode, so atoms spread over many positions see a reduced average coupling, and motion and position-dependent light shifts from the trap broaden and shift the spectrum. Selecting data by a signal that depends on coupling strength can bias the result towards the best-coupled events.

**Resolved by.** The atom number determined by a stated method, such as discrete steps in transmission or a loading statistic, with the probability of more than one atom given for single-atom claims; the position distribution and temperature stated and included in the model, or a localisation measurement; trap light shifts measured or calculated; any post-selection rule stated with the fraction of data kept and a check that the result does not depend on the threshold.

**Benchmark.** [1], [2], [4], [5], [7]

## 4. Strong-coupling criterion and resolved splitting

**Question.** Which criterion for strong coupling does the paper apply, and does the measured splitting exceed the relevant linewidths when it is mapped against atom-cavity detuning, rather than being inferred from a single spectrum or from a fit?

**Why it matters.** Strong coupling requires the coherent coupling to exceed both decay rates; when the cooperativity is large but g is smaller than the cavity linewidth, the spectrum shows only a dip in transmission and no resolved pair of peaks. A doublet at a single detuning can also come from two nearly degenerate cavity modes, and sublevel-dependent light shifts with optical pumping by the probe can make the peaks unequal, whereas the coupled system shows an avoided crossing as the detuning is varied.

**Resolved by.** g, κ and γ given with uncertainties and compared explicitly using a stated criterion; spectra at several atom-cavity detunings showing the avoided crossing; the splitting compared with the full widths of the peaks; the data shown alongside a model with stated free parameters.

**Benchmark.** [1], [2], [4]

## 5. Classical and quantum signatures

**Question.** When the paper claims a quantum effect of the atom-cavity system, does it rest on evidence beyond the normal-mode splitting, such as the photon-number dependence of the spectrum, photon statistics or a nonlinear response at the single-photon level?

**Why it matters.** The vacuum Rabi splitting seen with a weak probe follows from linear absorption and dispersion by the intracavity atoms and is reproduced by a model of coupled classical oscillators. It establishes strong coupling but not the quantised nature of the field. Signatures that lack a classical explanation include resonances spaced by the square roots of successive photon numbers and a nonlinear response that differs from classical saturation.

**Resolved by.** The normal-mode spectrum presented as evidence of strong coupling only; quantum claims supported by measurements such as Rabi oscillations with frequencies in the ratio of square roots of successive integers, multi-photon resonances of the dressed-state ladder, or photon correlations; a comparison with a semiclassical or saturation model showing that it fails to reproduce the feature.

**Benchmark.** [1], [3], [7], [8]

## 6. Probe strength and saturation

**Question.** What was the mean intracavity photon number during the measurement, how does it compare with the saturation photon number of the system, and does the result stay the same when the probe power is changed?

**Why it matters.** The linear vacuum Rabi spectrum and the classical and quantum descriptions agree only in the weak-excitation limit. A strong probe saturates the atom, reduces and distorts the splitting and can pump the atom between sublevels, and in a high-cooperativity cavity the saturation photon number can be far below one. Conversely, a claimed nonlinear effect must be distinguished from ordinary saturation by its dependence on probe power.

**Resolved by.** The intracavity photon number stated or plotted with the data, and compared with the saturation photon number; spectra at two or more probe powers showing the same splitting; for nonlinear claims, the dependence on probe power measured and compared with a model of saturation.

**Benchmark.** [1], [4], [7]

## 7. Purcell enhancement and emission into the mode

**Question.** For a claimed Purcell enhancement, does the paper state whether it refers to emission into the cavity mode or to the total decay rate, measure it against a reference without the resonant cavity, and give the detuning, the atomic position and the regime in which its formula holds?

**Why it matters.** The cavity-enhanced emission rate equals twice the cooperativity times the free-space rate only on resonance, at an antinode, for the right polarisation and in the bad-cavity regime where κ greatly exceeds g. A cavity that covers a small solid angle can raise emission into its mode many times over while changing the total decay rate by a few per cent, so the two must not be confused. The fraction of photons that leave through the intended mirror also depends on the ratio of output coupling to total cavity loss, not on the cooperativity alone.

**Resolved by.** The enhanced quantity named and measured, for example the rate into the mode or the total lifetime, against a reference taken with the cavity detuned or absent; the detuning, position averaging and polarisation included; the stated formula and its validity conditions; the output-coupling and loss rates given when an extraction efficiency is claimed.

**Benchmark.** [1], [2], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | H. Tanji-Suzuki et al., Interaction between atomic ensembles and optical resonators: classical description, Adv. At. Mol. Opt. Phys. 60, 201 (2011); read as arXiv:1104.3594 | doi:10.48550/arXiv.1104.3594 |
| 2 | A. Reiserer and G. Rempe, Cavity-based quantum networks with single atoms and optical photons, Rev. Mod. Phys. 87, 1379 (2015); read as arXiv:1412.2889 | doi:10.1103/RevModPhys.87.1379 |
| 3 | Y. Zhu et al., Vacuum Rabi splitting as a feature of linear-dispersion theory: analysis and experimental observations, Phys. Rev. Lett. 64, 2499 (1990) | doi:10.1103/PhysRevLett.64.2499 |
| 4 | A. Boca et al., Observation of the vacuum Rabi spectrum for one trapped atom, Phys. Rev. Lett. 93, 233603 (2004); read as arXiv:quant-ph/0410164 | doi:10.1103/PhysRevLett.93.233603 |
| 5 | D. Hunger et al., A fiber Fabry–Perot cavity with high finesse, New J. Phys. 12, 065038 (2010); read as arXiv:1005.0067 | doi:10.1088/1367-2630/12/6/065038 |
| 6 | S. Kuhr et al., Ultrahigh finesse Fabry-Pérot superconducting resonator, Appl. Phys. Lett. 90, 164101 (2007); read as arXiv:quant-ph/0612138 | doi:10.1063/1.2724816 |
| 7 | I. Schuster et al., Nonlinear spectroscopy of photons bound to one atom, Nat. Phys. 4, 382 (2008); read as arXiv:0803.2712 | doi:10.1038/nphys940 |
| 8 | M. Brune et al., Quantum Rabi oscillation: a direct test of field quantization in a cavity, Phys. Rev. Lett. 76, 1800 (1996) | doi:10.1103/PhysRevLett.76.1800 |
| 9 | D. J. Heinzen et al., Enhanced and inhibited visible spontaneous emission by atoms in a confocal resonator, Phys. Rev. Lett. 58, 1320 (1987) | doi:10.1103/PhysRevLett.58.1320 |
