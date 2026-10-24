---
id: T-QUANTUM-TRANSPORT
name: Quantum transport in mesoscopic devices
type: technique
field: physics/condensed-matter
applies_when: the paper reports conductance quantization, quantized Hall or edge-state transport in a device, Aharonov-Bohm or other interference oscillations, weak localization or antilocalization, nonlocal resistance, Coulomb blockade or shot noise, or bases a claim about coherence, edge channels or quasiparticle charge on them
version: "0.1"
---

# Quantum transport in mesoscopic devices

Low-temperature transport through small devices is used to claim quantized conductance in point contacts and edge channels, phase-coherent interference such as Aharonov-Bohm (AB) oscillations and weak localization (WL) or weak antilocalization (WAL), nonlocal transport, single-electron charging (Coulomb blockade) and the charge or Fano factor of the carriers from shot noise. Each claim compares a measured conductance, voltage or noise with a quantum of conductance, a flux quantum or an energy scale, so contacts, terminal geometry and the electron temperature enter directly.

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

## 3. Electron temperature and excitation

**Question.** Is the electron temperature of the device measured, not only the temperature of the refrigerator, and is the excitation small compared with the thermal energy and the energy scales on which the claim rests?

**Why it matters.** Below about 100 mK electrons decouple from the lattice because the electron-phonon coupling becomes weak, so dissipated power and electromagnetic noise reaching the sample keep the electrons hotter than the refrigerator unless the wiring is well filtered. The electron temperature sets thermal smearing of plateaus, the width of Coulomb peaks, the amplitude of interference and the thermal noise floor, and a finite bias smears features in a similar way. A temperature dependence plotted against refrigerator temperature can flatten where the electrons stop cooling, which can be mistaken for intrinsic saturation.

**Resolved by.** The electron temperature measured in the device or a neighbouring structure with a primary method, such as the width of a Coulomb peak, Johnson noise or the thermal-to-shot-noise crossover, and compared with the refrigerator temperature; filtering and thermalization of the lines described; the excitation voltage stated and shown to be below the thermal energy, or the result shown to be independent of it.

**Benchmark.** [1], [4], [5]

## 4. Aharonov-Bohm and other interference oscillations

**Question.** Does the period of the claimed oscillations agree with the enclosed area in the device, with that area and its uncertainty stated, are the h/e and h/2e components distinguished, and are periodic oscillations separated from aperiodic conductance fluctuations?

**Why it matters.** The h/e period follows from the area enclosed by the interfering paths, and the h/2e component arises from time-reversed paths with a phase fixed at zero field; the two survive ensemble averaging differently. When the field penetrates the arms of a ring, aperiodic fluctuations appear alongside the periodic signal, and with a small ratio of ring radius to arm width the two are hard to separate. Reciprocity makes a two-terminal conductance even in field, which constrains how the phase of two-terminal oscillations can be read.

**Resolved by.** The oscillation period, or the peak position in a Fourier transform, compared with the range of areas allowed by the inner and outer dimensions of the device; the h/e and h/2e components identified; periodic and aperiodic contributions separated by their field scales; for claims about the phase, a multi-terminal geometry or an argument that reciprocity does not fix it.

**Benchmark.** [1]

## 5. Fits to weak localization and antilocalization

**Question.** Which magnetoconductance formula was fitted, is its regime (dimensionality, diffusive transport, field range) shown to apply to the device, which parameters were free, and does the interpretation of the fitted prefactor and coherence length allow for other explanations?

**Why it matters.** WL and WAL formulas differ between two-dimensional and quasi-one-dimensional samples and hold only at weak fields in the diffusive regime; in narrow channels the effective width and the coherence length are fitted together and can trade off. The prefactor of the commonly used formula is often read as a count of conducting channels, but measured values span a wide range, depend on gaps, bulk states and coupling between surfaces, and are not independent fitting parameters in more complete theories. The temperature dependence of the conductivity also contains an interaction correction that competes with the interference correction.

**Resolved by.** The formula stated with its validity conditions checked against measured mean free path, coherence length and sample width; the fit range stated and the classical background handled explicitly; free and fixed parameters listed with uncertainties; the coherence length followed with temperature; claims about the number of channels or about surface states supported by an independent measurement, not by the prefactor alone; the interaction contribution to the temperature dependence considered.

**Benchmark.** [1], [7]

## 6. Nonlocal signals and measurement artefacts

**Question.** For a claimed nonlocal resistance, does the paper compare the signal with the classical current-spreading contribution expected from the measured resistivity and geometry, and show that thermoelectric, leakage and common-mode contributions of the measurement circuit are excluded?

**Why it matters.** Current spreading from the injection contacts gives a nonlocal voltage that decays roughly exponentially with distance over the channel width and scales with the local resistivity. Joule heating with mismatched contact resistances, input bias currents, crosstalk, leakage, finite common-mode rejection and charging of cable capacitances can each produce a nonlocal voltage, and in lock-in measurements these signals can be larger than the effect of interest and of either sign. Edge-channel transport can give genuine nonlocality, so a nonlocal signal by itself does not identify its origin.

**Resolved by.** The current-spreading estimate computed from measured local resistance and the actual geometry and compared with the data, ideally at several injector-detector spacings; first and second harmonics and both lock-in channels reported; the signal shown to be independent of frequency, input impedance and grounding configuration, or the current source and detection circuit isolated; dc and ac results compared.

**Benchmark.** [1], [8], [9]

## 7. Coulomb blockade and quantum dots

**Question.** Does the paper show that the conditions for Coulomb blockade hold (charging energy well above the thermal energy, tunnel resistances well above h/e²), present stability diagrams from which charging energy, lever arm and level spacing are extracted, and show that transport is through the intended single dot?

**Why it matters.** Single-electron charging requires weakly coupled leads and a charging energy that exceeds the thermal energy. Disorder can form unintended dots in narrow channels, and two dots in series conduct only where charge states of both are degenerate, so a set of conductance peaks alone does not identify a single dot. Conversion of gate voltage to energy relies on the lever arm, and the absolute electron number cannot be read from transport alone when the current becomes too small to detect.

**Resolved by.** Coulomb diamonds over a range of bias and gate voltage, with charging energy, lever arm and level spacing extracted from their slopes and heights; regular, closing diamonds consistent with one dot; excited-state lines identified separately from the addition spectrum; peak width and height followed with temperature to identify the regime; where the electron number is claimed, a charge sensor or other independent count.

**Benchmark.** [1], [5], [10], [11]

## 8. Shot noise and the Fano factor

**Question.** How was the noise setup calibrated, how was the amplifier background removed, and does the extraction of a Fano factor or effective charge account for the electron temperature, heating and the relevant relaxation lengths?

**Why it matters.** A Fano factor or charge follows from the ratio of current noise to current and from the crossover from thermal to shot noise near bias voltages of the order of the thermal energy, so errors in gain, background or electron temperature pass directly into it. Noise in a diffusive conductor depends on the length relative to the electron-electron and inelastic relaxation lengths, and heating raises or inelastic scattering suppresses the value expected without interactions. Low-frequency 1/f noise and pick-up add to the measured spectrum.

**Resolved by.** The gain and background calibrated, for example from Johnson noise at several known temperatures or conductances, with the electron temperature obtained from the same calibration; the amplifier background measured and subtracted; the full noise against bias fitted with the finite-temperature expression, with the fit range and parameters stated; sample length compared with the relaxation lengths and reservoirs large enough to avoid heating; the measurement band chosen above the 1/f corner.

**Benchmark.** [4], [6]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | C. W. J. Beenakker and H. van Houten, Quantum transport in semiconductor nanostructures, Solid State Physics 44, 1–228 (1991); read as arXiv:cond-mat/0412664 | doi:10.1016/S0081-1947(08)60091-0 | full text | Sec. III.B.1: plateaus near multiples of 2e²/h only after correcting for a series resistance from the wide regions and contacts; deviations typically 1%, against 1 part in 10⁷ for the quantum Hall effect, partly from a background resistance that cannot be fixed precisely; thermal smearing of the steps. Sec. III.A.2: reciprocity relation making the two-terminal resistance even in field. Sec. II.B.2: 2D and quasi-1D weak-localization formulas; effective width and coherence length fitted together, effective width below the lithographic width. Sec. II.D: h/e from the enclosed area with sample-specific phase, h/2e from time-reversed paths survives ensemble averaging, field in the arms adds aperiodic fluctuations separated by a large radius-to-width ratio. Sec. III.F.2: periodic oscillations in narrow channels explained by Coulomb blockade of segments between impurities. Secs. IV.A.1 and IV.B.2: edge channels give nonlocal transport; non-ideal contacts affect the measured Hall resistance |
| 2 | F. Delahaye and B. Jeckelmann, Revised technical guidelines for reliable dc measurements of the quantized Hall resistance, Metrologia 40, 217–223 (2003); read as the 2002 draft posted by the BIPM as working document CCEM/2002-01 of the 23rd CCEM meeting | doi:10.1088/0026-1394/40/5/302 | full text | Draft Sect. 2: the quantum Hall effect breaks down at a critical current. Sect. 4: contact resistances checked by two- and three-terminal measurements. Sect. 5.1: longitudinal voltage measured on both sides with the measurement current, ideally unmeasurable on the plateau. Sects. 5.2 and 5.3: Hall resistance checked against temperature and current. Sect. 5.4: checked for invariance under field reversal. Sect. 5.5: Hall resistance the same at the Hall contact pairs along the device |
| 3 | D. A. Abanin and L. S. Levitov, Conformal invariance and shape-dependent conductance of graphene samples, Phys. Rev. B 78, 035416 (2008); read as arXiv:0804.4043 | doi:10.1103/PhysRevB.78.035416 | full text | Introduction: two-terminal conductance depends on aspect ratio and geometry, unlike four-probe resistivity, so observed plateaus are often distorted. Section on the conformal mapping approach and Figs. 2–3: for non-square samples the conductance is non-monotonic, with minima or maxima at plateau centres; added contact resistance changes the values |
| 4 | F. Giazotto, T. T. Heikkilä, A. Luukanen, A. M. Savin and J. P. Pekola, Opportunities for mesoscopics in thermometry and refrigeration: physics and applications, Rev. Mod. Phys. 78, 217–274 (2006); read as arXiv:cond-mat/0508093, titled there Thermal properties in mesoscopics | doi:10.1103/RevModPhys.78.217 | full text | Secs. II.C.2 and II.D: electron-phonon heat flow weak at low temperature; electrons heated by thermal noise in their electromagnetic environment unless properly filtered. Sec. III: electrons typically decouple thermally from the lattice below about 100 mK. Secs. III.B and III.C: Coulomb-blockade and shot-noise thermometers as primary thermometers, the latter from the crossover from Johnson to shot noise at bias of order kT/e |
| 5 | Y. Alhassid, The statistical theory of quantum dots, Rev. Mod. Phys. 72, 895–968 (2000); read as arXiv:cond-mat/0102268 | doi:10.1103/RevModPhys.72.895 | full text | Sec. I.A: charge quantization needs conductance well below e²/h and kT well below e²/C; classical and quantum Coulomb-blockade regimes. Secs. II.D and II.E: peak width of order kT; peak height falls as 1/T in the quantum regime and is temperature independent in the classical regime |
| 6 | Ya. M. Blanter and M. Büttiker, Shot noise in mesoscopic conductors, Phys. Rep. 336, 1–166 (2000); read as arXiv:cond-mat/9910158 | doi:10.1016/S0370-1573(99)00123-4 | full text | Sec. I.C: 1/f noise affected early experiments and is set aside from thermal and shot noise. Sec. II.D, Eq. (62), and Sec. II.F.1, Eq. (71): finite-temperature noise with the coth crossover at bias of order kT/e. Secs. II.F.4 and II.G: diffusive-wire Fano factor 1/3; electron heating raises it and inelastic scattering suppresses it with length; very large reservoirs used to avoid electron heating |
| 7 | H.-Z. Lu and S.-Q. Shen, Weak localization and weak anti-localization in topological insulators, Proc. SPIE 9167, 91672E (2014); read as arXiv:1409.1299 | doi:10.1117/12.2063426 | full text | Sec. 2.3 and Table 1: fits with the Hikami-Larkin-Nagaoka formula give prefactors from about -0.3 to -1.1, read as one or two surface bands although bulk and surface carriers coexist. Sec. 3.1: weights depend on the gap-to-Fermi-energy ratio, so they are not independent fit parameters; hybridization of top and bottom surfaces opens a gap (Fig. 4). Secs. 4 and 6: bulk states and the interaction correction compete with antilocalization in the temperature dependence |
| 8 | F. Volmer, T. Bisswanger, A. Schmidt, C. Stampfer and B. Beschoten, Charge-induced artifacts in nonlocal spin-transport measurements: how to prevent spurious voltage signals, Phys. Rev. Applied 18, 014028 (2022); read as arXiv:2112.02047 | doi:10.1103/PhysRevApplied.18.014028 | full text | Secs. II A to II H: seven charge-induced nonlocal signals: current spreading estimated as Iρ exp(-πL/w), thermoelectric voltages at first and second harmonics, input bias currents, crosstalk, leakage through finite input impedance, finite common-mode rejection and capacitor charging; relevance differs between dc and ac. Sec. III: phase-shifted, frequency-dependent signals in the lock-in Y channel; a virtual ground removes signals driven by the common-mode voltage |
| 9 | A. De Sanctis, J. D. Mehew, S. Alkhalifa, C. P. Tate, A. White, A. R. Woodgate, M. F. Craciun and S. Russo, Novel circuit design for high-impedance and non-local electrical measurements of two-dimensional materials, Rev. Sci. Instrum. 89, 024705 (2018); read as arXiv:1801.10135 | doi:10.1063/1.5020044 | full text | Abstract and the section on non-local and high-impedance measurements: incomplete common-mode rejection with finite amplifier input impedance and cable leakage gives a nonlocal signal that can exceed the true one and have opposite sign; residual zero-field signal attributed to Joule heating with mismatched contact resistances; floating the voltage probes with optocouplers removes the artefact |
| 10 | R. Hanson, L. P. Kouwenhoven, J. R. Petta, S. Tarucha and L. M. K. Vandersypen, Spins in few-electron quantum dots, Rev. Mod. Phys. 79, 1217–1265 (2007); read as arXiv:cond-mat/0610433 | doi:10.1103/RevModPhys.79.1217 | full text | Secs. II.D to II.F: constant-interaction model, addition energy, diamond slopes set by capacitance ratios, excited-state lines in the bias window. Secs. II.C and V: a nearby point contact as charge sensor gives the absolute electron number even when no current through the dot is detected |
| 11 | W. G. van der Wiel, S. De Franceschi, J. M. Elzerman, T. Fujisawa, S. Tarucha and L. P. Kouwenhoven, Electron transport through double quantum dots, Rev. Mod. Phys. 75, 1–22 (2002); read as arXiv:cond-mat/0205350 | doi:10.1103/RevModPhys.75.1 | full text | Sec. II.A: two dots in series conduct only at triple points where charge states of both dots are degenerate, giving a honeycomb stability diagram; barriers must be opaque enough for a well-defined electron number on each dot |
