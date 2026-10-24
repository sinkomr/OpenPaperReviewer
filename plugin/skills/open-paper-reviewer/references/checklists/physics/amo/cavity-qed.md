---
id: T-CAVITY-QED
name: Cavity quantum electrodynamics
type: technique
field: physics/amo
applies_when: the paper couples atoms to an optical or microwave cavity mode and reports a coupling strength, cooperativity, vacuum Rabi or normal-mode splitting, strong coupling, Purcell enhancement, cavity-enhanced emission or single-photon nonlinearities of an atom-cavity system
version: "0.1"
---

# Cavity quantum electrodynamics

Cavity quantum electrodynamics (cavity QED) experiments with atoms are used to claim a coupling strength g between an atom and a cavity mode, a cooperativity C that compares g with the cavity field decay rate κ and the atomic decay rate γ, the strong-coupling regime shown by a vacuum Rabi (normal-mode) splitting, Purcell enhancement of emission into the cavity mode, and nonlinear quantum effects at the level of single photons. Each of these is inferred from cavity transmission, reflection or emission and rests on how the rates are defined, how many atoms couple, and where they sit in the mode.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | H. Tanji-Suzuki, I. D. Leroux, M. H. Schleier-Smith, M. Cetina, A. T. Grier, J. Simon and V. Vuletić, Interaction between atomic ensembles and optical resonators: classical description, Adv. At. Mol. Opt. Phys. 60, 201–237 (2011); read as arXiv:1104.3594 | doi:10.48550/arXiv.1104.3594 | full text | Sec. 4.1: single-atom cooperativity from finesse and waist, noted as twice the C parameter common in cavity QED, and identified with the Purcell factor including a factor of 4 at the antinode; splitting smaller than the cavity linewidth gives only a transmission dip. Secs. 4.1 and 4.3: a splitting appears in a linear classical dispersion model. Sec. 5.1: ensemble cooperativity N H η with H the average of the squared mode function, one half for random positions. Secs. 2 and 4.1: the classical results agree with quantum ones only at low saturation. Sec. 6: the classical normal-mode splitting equals the vacuum Rabi frequency 2g, giving the cooperativity as 4g²/(κΓ) |
| 2 | A. Reiserer and G. Rempe, Cavity-based quantum networks with single atoms and optical photons, Rev. Mod. Phys. 87, 1379–1418 (2015); read as arXiv:1412.2889 | doi:10.1103/RevModPhys.87.1379 | full text | Secs. I.1 to I.3: g from dipole moment and single-photon field, κ from length and finesse as a field decay rate, empty-cavity full width 2κ, γ as half the spontaneous rate, C = g²/(2κγ), cooperativity N C for N atoms. Sec. I.2, Fig. 2: dressed states show avoided crossings as the atom-cavity detuning is varied. Sec. I.3.1: strong coupling needs g to exceed γ and κ. Sec. I.3.2, Eqs. 12 and 13: cavity emission rate 2Cγ on resonance with κ much larger than g, and output fraction set by the output-coupling share of κ. Secs. II.2.2 and II.2.3: atom number from steps in transmission; localisation, motion and time-varying light shifts reduce and fluctuate the coupling |
| 3 | Y. Zhu, D. J. Gauthier, S. E. Morin, Q. Wu, H. J. Carmichael and T. W. Mossberg, Vacuum Rabi splitting as a feature of linear-dispersion theory: analysis and experimental observations, Phys. Rev. Lett. 64, 2499–2502 (1990) | doi:10.1103/PhysRevLett.64.2499 | abstract | Abstract: the split transmission of a cavity containing an atomic ensemble can be read as a vacuum Rabi splitting or explained more simply by the linear absorption and dispersion of the atoms |
| 4 | A. Boca, R. Miller, K. M. Birnbaum, A. D. Boozer, J. McKeever and H. J. Kimble, Observation of the vacuum Rabi spectrum for one trapped atom, Phys. Rev. Lett. 93, 233603 (2004); read as arXiv:quant-ph/0410164 | doi:10.1103/PhysRevLett.93.233603 | full text | Trap and cooling paragraphs: position-dependent coupling and trap light shifts that depend on the excited sublevel shape the spectrum; agreement only for low temperature and well-coupled trap sites. Loading paragraph: probability of more than one atom estimated and selection threshold shown not to matter. Probe paragraphs and footnote 26: weak probe with intracavity photon number plotted and critical photon number stated; splitting still seen atom by atom when the drive intensity is changed by factors from 1/4 to 2 and at atom-cavity detunings of ±13 MHz. Footnote 30: sublevel-dependent Stark shifts with optical pumping by the probe make the peak heights unequal. Theory paragraph and footnote 24: model includes all Zeeman transitions and two nearly degenerate polarisation modes from mirror birefringence |
| 5 | D. Hunger, T. Steinmetz, Y. Colombe, C. Deutsch, T. W. Hänsch and J. Reichel, A fiber Fabry–Perot cavity with high finesse, New J. Phys. 12, 065038 (2010); read as arXiv:1005.0067 | doi:10.1088/1367-2630/12/6/065038 | full text | Sec. 5.4: finesse from free spectral range over a linewidth calibrated with RF sidebands; polarisation-mode splitting of about 200 MHz. Sec. 5.2: ringdown cross-check; scatter and absorption losses compared with transmission. Secs. 4.2 to 4.6: waist, mode volume, g and cooperativity from geometry, cooperativity set by finesse and waist. Sec. 5.6: g extracted from an atomic ensemble with square-root-of-N scaling, uncertainty dominated by N |
| 6 | S. Kuhr, S. Gleyzes, C. Guerlin, J. Bernu, U. B. Hoff, S. Deléglise, S. Osnaghi, M. Brune, J.-M. Raimond, S. Haroche, E. Jacques, P. Bosland and B. Visentin, Ultrahigh finesse Fabry-Pérot superconducting resonator, Appl. Phys. Lett. 90, 164101 (2007); read as arXiv:quant-ph/0612138 | doi:10.1063/1.2724816 | full text | Setup paragraph: two orthogonally polarised modes separated by 1.2 MHz so that atoms couple to a single mode. Mode-characterisation paragraph: damping time measured by injecting a microwave pulse and probing the decaying field with Rydberg atoms after a delay |
| 7 | I. Schuster, A. Kubanek, A. Fuhrmanek, T. Puppe, P. W. H. Pinkse, K. Murr and G. Rempe, Nonlinear spectroscopy of photons bound to one atom, Nat. Phys. 4, 382–385 (2008); read as arXiv:0803.2712 | doi:10.1038/nphys940 | full text | Introduction: the normal-mode spectrum can equally be described by linear dispersion or coupled oscillators and is a benchmark of strong coupling, not of quantum behaviour. Results and appendices: a two-photon resonance of the dressed-state ladder, quadratic in probe intensity, absent from semiclassical saturation simulations; probe kept below atomic saturation; post-selection on localisation keeps about 15% of atom-present intervals |
| 8 | M. Brune, F. Schmidt-Kaler, A. Maali, J. Dreyer, E. Hagley, J. M. Raimond and S. Haroche, Quantum Rabi oscillation: a direct test of field quantization in a cavity, Phys. Rev. Lett. 76, 1800–1803 (1996) | doi:10.1103/PhysRevLett.76.1800 | abstract | Abstract: Rabi oscillations of Rydberg atoms in small fields in a microwave cavity contain Fourier components at frequencies in the ratio of square roots of successive integers, giving direct evidence of field quantisation and the photon-number distribution |
| 9 | D. J. Heinzen, J. J. Childs, J. E. Thomas and M. S. Feld, Enhanced and inhibited visible spontaneous emission by atoms in a confocal resonator, Phys. Rev. Lett. 58, 1320–1323 (1987) | doi:10.1103/PhysRevLett.58.1320 | abstract | Abstract: emission into the resonator modes rises about 19-fold on resonance and falls about 42-fold off resonance, while the total spontaneous rate changes by only about +1.6% and −0.5%; checked against light escaping from the sides of the resonator |
