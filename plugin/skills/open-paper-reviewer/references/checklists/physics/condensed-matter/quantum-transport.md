---
id: T-QUANTUM-TRANSPORT
name: Quantum transport in mesoscopic devices
type: technique
field: physics/condensed-matter
applies_when: the paper reports conductance quantization, quantized Hall or edge-state transport in a device, Aharonov-Bohm or other interference oscillations, weak localization or antilocalization, nonlocal resistance, Coulomb blockade or shot noise, or bases a claim about coherence, edge channels or quasiparticle charge on them
version: "0.1"
---

# Quantum transport in mesoscopic devices

## 1. Series resistance and conductance plateaus

**Question.** When conductance plateaus are reported at multiples of e²/h or 2e²/h, does the paper state what series resistance was subtracted, how it was determined independently of the plateaus, and whether the same value holds across the whole gate and field range shown?

**Why it matters.** A point-contact measurement includes the ohmic contacts, leads and wide two-dimensional regions in series with the constriction, and plateaus land near the quantized values only after this resistance is removed. Plateau quantization in such devices is typically good to about one per cent, not to metrological accuracy, partly because the background is uncertain. If the series resistance is chosen so that the plateaus line up with the quantized values, the plateau values are no longer a test of quantization.

**Resolved by.** Raw conductance shown before any correction; the subtracted resistance stated, with its origin, and measured separately, for example in a four-terminal configuration or from the wide-region resistance; one fixed value used for all curves; the claimed quantization supported by plateau flatness and step spacing, with the deviation from the quantized values and its uncertainty quoted.

**Benchmark.** [1]

## 2. Quantized Hall and edge-state plateaus

**Question.** When a Hall or edge-channel resistance is claimed to be quantized, does the paper show four-terminal Hall and longitudinal resistance together, with the longitudinal resistance vanishing on the plateau, the same Hall value at several contact pairs, and the contact resistances, measurement current and temperature at which this holds?

**Why it matters.** Quantization of the Hall resistance comes with vanishing dissipation, so a plateau value without the simultaneous longitudinal resistance does not establish it. Non-ideal or resistive contacts can shift the measured Hall resistance away from the quantized value, and too large a current breaks the quantization down. A two-terminal conductance in a magnetic field mixes longitudinal and Hall conductivities in a way that depends on the sample's aspect ratio, so its plateaus can be distorted or show peaks and dips that do not reflect the underlying conductivities.

**Resolved by.** Four-terminal Hall and longitudinal data on the same sweeps, with the residual longitudinal resistance on the plateau and the deviation of the Hall value from h/(νe²) quoted with uncertainties; the Hall value compared at more than one contact pair and for both field directions; contact resistances measured, for example in a three-terminal configuration; the plateau shown to be unchanged over a range of current and temperature; two-terminal data, where used, interpreted with the device geometry taken into account.

**Benchmark.** [1], [2], [3]

## 3. Aharonov-Bohm and other interference oscillations

**Question.** Does the period of the claimed oscillations agree with the enclosed area in the device, with that area and its uncertainty stated, are the h/e and h/2e components distinguished, and are periodic oscillations separated from aperiodic conductance fluctuations?

**Why it matters.** The h/e period follows from the area enclosed by the interfering paths, and the h/2e component arises from time-reversed paths with a phase fixed at zero field; the two survive ensemble averaging differently. When the field penetrates the arms of a ring, aperiodic fluctuations appear alongside the periodic signal, and with a small ratio of ring radius to arm width the two are hard to separate. Reciprocity makes a two-terminal conductance even in field, which constrains how the phase of two-terminal oscillations can be read.

**Resolved by.** The oscillation period, or the peak position in a Fourier transform, compared with the range of areas allowed by the inner and outer dimensions of the device; the h/e and h/2e components identified; periodic and aperiodic contributions separated by their field scales; for claims about the phase, a multi-terminal geometry or an argument that reciprocity does not fix it.

**Benchmark.** [1]

## 4. Fits to weak localization and antilocalization

**Question.** Which magnetoconductance formula was fitted, is its regime (dimensionality, diffusive transport, field range) shown to apply to the device, which parameters were free, and does the interpretation of the fitted prefactor and coherence length allow for other explanations?

**Why it matters.** WL and WAL formulas differ between two-dimensional and quasi-one-dimensional samples and hold only at weak fields in the diffusive regime; in narrow channels the effective width and the coherence length are fitted together and can trade off. The prefactor of the commonly used formula is often read as a count of conducting channels, but measured values span a wide range, depend on gaps, bulk states and coupling between surfaces, and are not independent fitting parameters in more complete theories. The temperature dependence of the conductivity also contains an interaction correction that competes with the interference correction.

**Resolved by.** The formula stated with its validity conditions checked against measured mean free path, coherence length and sample width; the fit range stated and the classical background handled explicitly; free and fixed parameters listed with uncertainties; the coherence length followed with temperature; claims about the number of channels or about surface states supported by an independent measurement, not by the prefactor alone; the interaction contribution to the temperature dependence considered.

**Benchmark.** [1], [7]

## 5. Nonlocal signals and measurement artefacts

**Question.** For a claimed nonlocal resistance, does the paper compare the signal with the classical current-spreading contribution expected from the measured resistivity and geometry, and show that thermoelectric, leakage and common-mode contributions of the measurement circuit are excluded?

**Why it matters.** Current spreading from the injection contacts gives a nonlocal voltage that decays roughly exponentially with distance over the channel width and scales with the local resistivity. Joule heating with mismatched contact resistances, input bias currents, crosstalk, leakage, finite common-mode rejection and charging of cable capacitances can each produce a nonlocal voltage, and in lock-in measurements these signals can be larger than the effect of interest and of either sign. Edge-channel transport can give genuine nonlocality, so a nonlocal signal by itself does not identify its origin.

**Resolved by.** The current-spreading estimate computed from measured local resistance and the actual geometry and compared with the data, ideally at several injector-detector spacings; first and second harmonics and both lock-in channels reported; the signal shown to be independent of frequency, input impedance and grounding configuration, or the current source and detection circuit isolated; dc and ac results compared.

**Benchmark.** [1], [8], [9]

## 6. Coulomb blockade and quantum dots

**Question.** Does the paper show that the conditions for Coulomb blockade hold (charging energy well above the thermal energy, tunnel resistances well above h/e²), present stability diagrams from which charging energy, lever arm and level spacing are extracted, and show that transport is through the intended single dot?

**Why it matters.** Single-electron charging requires weakly coupled leads and a charging energy that exceeds the thermal energy. Disorder can form unintended dots in narrow channels, and two dots in series conduct only where charge states of both are degenerate, so a set of conductance peaks alone does not identify a single dot. Conversion of gate voltage to energy relies on the lever arm, and the absolute electron number cannot be read from transport alone when the current becomes too small to detect.

**Resolved by.** Coulomb diamonds over a range of bias and gate voltage, with charging energy, lever arm and level spacing extracted from their slopes and heights; regular, closing diamonds consistent with one dot; excited-state lines identified separately from the addition spectrum; peak width and height followed with temperature to identify the regime; where the electron number is claimed, a charge sensor or other independent count.

**Benchmark.** [1], [5], [10], [11]

## 7. Shot noise and the Fano factor

**Question.** How was the noise setup calibrated, how was the amplifier background removed, and does the extraction of a Fano factor or effective charge account for the electron temperature, heating and the relevant relaxation lengths?

**Why it matters.** A Fano factor or charge follows from the ratio of current noise to current and from the crossover from thermal to shot noise near bias voltages of the order of the thermal energy, so errors in gain, background or electron temperature pass directly into it. Noise in a diffusive conductor depends on the length relative to the electron-electron and inelastic relaxation lengths, and heating raises or inelastic scattering suppresses the value expected without interactions. Low-frequency 1/f noise and pick-up add to the measured spectrum.

**Resolved by.** The gain and background calibrated, for example from Johnson noise at several known temperatures or conductances, with the electron temperature obtained from the same calibration; the amplifier background measured and subtracted; the full noise against bias fitted with the finite-temperature expression, with the fit range and parameters stated; sample length compared with the relaxation lengths and reservoirs large enough to avoid heating; the measurement band chosen above the 1/f corner.

**Benchmark.** [4], [6]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | C. W. J. Beenakker and H. van Houten, Quantum transport in semiconductor nanostructures, Solid State Physics 44, 1 (1991); read as arXiv:cond-mat/0412664 | doi:10.1016/S0081-1947(08)60091-0 |
| 2 | F. Delahaye and B. Jeckelmann, Revised technical guidelines for reliable dc measurements of the quantized Hall resistance, Metrologia 40, 217 (2003); read as the 2002 draft posted by the BIPM as working document CCEM/2002-01 of the 23rd CCEM meeting | doi:10.1088/0026-1394/40/5/302 |
| 3 | D. A. Abanin and L. S. Levitov, Conformal invariance and shape-dependent conductance of graphene samples, Phys. Rev. B 78, 035416 (2008); read as arXiv:0804.4043 | doi:10.1103/PhysRevB.78.035416 |
| 4 | F. Giazotto et al., Opportunities for mesoscopics in thermometry and refrigeration: physics and applications, Rev. Mod. Phys. 78, 217 (2006); read as arXiv:cond-mat/0508093, titled there Thermal properties in mesoscopics | doi:10.1103/RevModPhys.78.217 |
| 5 | Y. Alhassid, The statistical theory of quantum dots, Rev. Mod. Phys. 72, 895 (2000); read as arXiv:cond-mat/0102268 | doi:10.1103/RevModPhys.72.895 |
| 6 | Ya. M. Blanter and M. Büttiker, Shot noise in mesoscopic conductors, Phys. Rep. 336, 1 (2000); read as arXiv:cond-mat/9910158 | doi:10.1016/S0370-1573(99)00123-4 |
| 7 | H.-Z. Lu and S.-Q. Shen, Weak localization and weak anti-localization in topological insulators, Proc. SPIE 9167, 91672E (2014); read as arXiv:1409.1299 | doi:10.1117/12.2063426 |
| 8 | F. Volmer et al., Charge-induced artifacts in nonlocal spin-transport measurements: how to prevent spurious voltage signals, Phys. Rev. Applied 18, 014028 (2022); read as arXiv:2112.02047 | doi:10.1103/PhysRevApplied.18.014028 |
| 9 | A. De Sanctis et al., Novel circuit design for high-impedance and non-local electrical measurements of two-dimensional materials, Rev. Sci. Instrum. 89, 024705 (2018); read as arXiv:1801.10135 | doi:10.1063/1.5020044 |
| 10 | R. Hanson et al., Spins in few-electron quantum dots, Rev. Mod. Phys. 79, 1217 (2007); read as arXiv:cond-mat/0610433 | doi:10.1103/RevModPhys.79.1217 |
| 11 | W. G. van der Wiel et al., Electron transport through double quantum dots, Rev. Mod. Phys. 75, 1 (2002); read as arXiv:cond-mat/0205350 | doi:10.1103/RevModPhys.75.1 |
