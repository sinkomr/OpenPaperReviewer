---
id: T-DEFECT-QUBITS
name: Defect qubits
type: technique
field: physics/quantum-information
applies_when: the paper reports colour centres or spin defects such as nitrogen-vacancy or silicon-vacancy centres, and bases a claim on optically detected magnetic resonance, spin coherence or relaxation times, charge state, defect identification, spin readout, photon collection or optical linewidths
version: "0.1"
---

# Defect qubits

## 1. Defect species, site and orientation

**Question.** How does the paper establish which defect, and which lattice site and orientation of that defect, produce the signal: by the zero-phonon line and vibronic band, by the spin Hamiltonian (zero-field splitting, g-factor, hyperfine structure), or by more than one of these?

**Why it matters.** Similar defect complexes can sit on inequivalent lattice sites or in different crystallographic orientations that respond differently to fields and light, and the same defect in a different charge state has very different spin and optical properties. Identifying a defect is difficult enough that established practice combines optical signatures, the spin Hamiltonian and theory, so an assignment based on one feature alone can be ambiguous.

**Resolved by.** The emission spectrum shown with the zero-phonon line identified and compared with established values; the spin resonance fitted with a spin Hamiltonian whose parameters match the assigned defect; the orientation fixed by the angular dependence of the resonances on the applied field; where a new defect is proposed, the assignment supported by more than one independent signature or by theory.

**Benchmark.** [1], [3]

## 2. Charge state

**Question.** Does the paper report the fraction of time, or of the ensemble, in the desired charge state under the excitation used, and does it check that charge conversion during illumination or in the dark does not account for the signals interpreted as spin effects?

**Why it matters.** Only one charge state has the spin and optical properties being claimed, and laser light converts defects between charge states: for single NV centres under common green excitation the negative charge state is occupied only about three quarters of the time. Emission from the other charge state adds a background that lowers contrast, and recharging in the dark changes the fluorescence in a way that can be mistaken for spin relaxation, which biases pulsed T1 measurements.

**Resolved by.** The charge-state population measured, for example by charge-state readout or spectral decomposition of the two emission bands; spectral filtering stated; for relaxation measurements, low excitation power, a reference sequence or normalisation that separates charge dynamics from spin relaxation, and a check that T1 does not change with laser power.

**Benchmark.** [1], [4], [5], [7]

## 3. ODMR linewidth and contrast

**Question.** Are the laser and microwave powers stated for each ODMR spectrum, and are linewidths, contrasts or dephasing times derived from them shown to be free of power broadening and of unresolved hyperfine structure?

**Why it matters.** In continuous-wave ODMR both the optical pumping and the microwave drive broaden the resonance, and lowering the powers to narrow the line also lowers the contrast or the count rate, so a quoted linewidth or contrast depends on the powers chosen. Hyperfine lines that merge into one broadened resonance make the linewidth and contrast ambiguous, and converting a linewidth into T2* requires knowing the lineshape.

**Resolved by.** Linewidth and contrast reported against laser and microwave power, or measured with pulsed ODMR or Ramsey sequences that avoid power broadening; the hyperfine structure resolved or accounted for in the fit; any T2* inferred from a linewidth accompanied by the lineshape assumed, or measured directly by free induction decay.

**Benchmark.** [6], [7]

## 4. Which coherence time

**Question.** Does the paper say which coherence time each quoted value is (T2* from free induction decay, T2 from a Hahn echo, or a decoupled T2 from a named sequence with a stated number of pulses), and give the fit function with its stretching exponent and the measured T1 for comparison?

**Why it matters.** T2* is set by static and slow fluctuations, the Hahn-echo T2 by faster noise, and dynamical decoupling extends T2 further as a power law in the number of pulses until T1 limits it, at about half of T1 in nitrogen-vacancy ensembles; values from different sequences are not comparable. Finite pulse widths in multipulse sequences add harmonics to the filter function, so dips in a decoupled coherence curve can be misassigned to a particular nuclear spin or noise frequency.

**Resolved by.** The sequence, number of pulses, magnetic field and temperature stated for each coherence time; the decay plotted with the fit and its exponent; T1 measured under the same conditions; when decoupling is compared with another platform, the same sequence type or the Hahn-echo value also given; spectral features in decoupling data checked against harmonics, for example over a wider frequency range or with a second sequence.

**Benchmark.** [1], [7], [8], [9]

## 5. Spin readout fidelity and sensitivity

**Question.** When a readout fidelity, single-shot readout or a sensitivity is claimed, does the paper give the photon numbers detected for each spin state per readout, the definition of fidelity used, and the initialisation, readout and dead times included in the sensitivity?

**Why it matters.** Conventional optical readout of NV centres yields well under one detected photon per shot and only a modest contrast, so readout noise sits far above the spin projection limit and the fidelity follows from the contrast and the photon number. Measured fidelities often fall below the value predicted from photon statistics because of state changes during readout and imperfect initialisation, and a sensitivity that omits initialisation and readout time overstates what the sensor achieves.

**Resolved by.** Photon-count histograms or mean counts for each spin state with the contrast; the fidelity or signal-to-noise ratio defined explicitly, with the threshold for single-shot readout stated; initialisation fidelity measured or bounded; sensitivity calculated with the full measurement time including overheads, and checked against a measured noise floor.

**Benchmark.** [7], [10]

## 6. Photon collection efficiency and brightness

**Question.** How are the count rate and the collection efficiency defined and measured: at which point in the optical path, with which detector efficiency, dead time and filtering, and is the saturation count rate obtained from a power series that separates emitter light from background?

**Why it matters.** The high refractive index of hosts such as diamond limits how much light leaves a planar surface, to a few per cent for an air objective, so claimed gains from photonic structures depend on what is taken as the baseline. A detector is blind for its dead time after each detection, so high count rates are undercounted, background grows linearly with power and can be counted as emitter light, and the effect of a faster emission rate on spin contrast has to be measured rather than assumed.

**Resolved by.** A saturation curve fitted with a saturating emitter term and a linear background term; detected count rate, detector and filter efficiencies and the resulting collection efficiency stated separately; the comparison structure or planar reference measured under the same conditions; for Purcell-enhancement claims, the lifetime change measured and the spin contrast reported with and without the structure.

**Benchmark.** [2], [10]

## 7. Optical linewidth and spectral diffusion

**Question.** For claims about optical coherence or indistinguishable photons, does the paper compare the measured optical linewidth with the lifetime limit, and state whether linewidths come from single fast scans or from scans averaged over time?

**Why it matters.** The narrowest possible linewidth is set by the excited-state lifetime, and fluctuating charges in the environment shift the line on timescales from shorter than one scan to much longer. A single fast scan can show a narrow line while the time-averaged line is much broader, and it is the averaged line that limits two-photon interference and entanglement rates.

**Resolved by.** The lifetime measured and the lifetime-limited linewidth computed; linewidths reported for single scans and for the scans combined, with scan time and repetition rate; the line position tracked over time; where indistinguishability is claimed, a two-photon interference visibility measured rather than inferred from a linewidth.

**Benchmark.** [1]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | G. Wolfowicz et al., Quantum guidelines for solid-state spin defects, Nat. Rev. Mater. 6, 906 (2021); read as preprint arXiv:2010.16395, titled Qubit guidelines for solid-state spin defects | doi:10.1038/s41578-021-00306-y |
| 2 | R. E. K. Fishman et al., Photon-emission-correlation spectroscopy as an analytical tool for solid-state quantum defects, PRX Quantum 4, 010202 (2023); read as preprint arXiv:2111.01252 | doi:10.1103/PRXQuantum.4.010202 |
| 3 | M. W. Doherty et al., The nitrogen-vacancy colour centre in diamond, Phys. Rep. 528, 1 (2013); read as preprint arXiv:1302.3288 | doi:10.1016/j.physrep.2013.02.001 |
| 4 | N. Aslam et al., Photo-induced ionization dynamics of the nitrogen vacancy defect in diamond investigated by single-shot charge state detection, New J. Phys. 15, 013064 (2013); read as preprint arXiv:1209.0268 | doi:10.1088/1367-2630/15/1/013064 |
| 5 | I. Cardoso Barbosa et al., Impact of charge conversion on NV-center relaxometry, Phys. Rev. B 108, 075411 (2023); read as preprint arXiv:2301.01063 | doi:10.1103/PhysRevB.108.075411 |
| 6 | A. Dréau et al., Avoiding power broadening in optically detected magnetic resonance of single NV defects for enhanced dc magnetic field sensitivity, Phys. Rev. B 84, 195204 (2011); read as preprint arXiv:1108.0178 | doi:10.1103/PhysRevB.84.195204 |
| 7 | J. F. Barry et al., Sensitivity optimization for NV-diamond magnetometry, Rev. Mod. Phys. 92, 015004 (2020); read as preprint arXiv:1903.08176 | doi:10.1103/RevModPhys.92.015004 |
| 8 | N. Bar-Gill et al., Solid-state electronic spin coherence time approaching one second, Nat. Commun. 4, 1743 (2013); read as preprint arXiv:1211.7094 | doi:10.1038/ncomms2771 |
| 9 | M. Loretz et al., Spurious harmonic response of multipulse quantum sensing sequences, Phys. Rev. X 5, 021009 (2015); read as preprint arXiv:1412.5768 | doi:10.1103/PhysRevX.5.021009 |
| 10 | D. A. Hopper et al., Spin readout techniques of the nitrogen-vacancy center in diamond, Micromachines 9, 437 (2018); read as preprint arXiv:1809.05237 | doi:10.3390/mi9090437 |
