---
id: T-QUANTUM-OSCILLATIONS
name: Quantum oscillations and high magnetic fields
type: technique
field: physics/condensed-matter
applies_when: the paper reports de Haas-van Alphen or Shubnikov-de Haas oscillations, torque or other measurements in high DC or pulsed fields, or derives Fermi-surface areas, effective masses, quantum lifetimes, carrier densities or a Berry phase from oscillations periodic in inverse field
version: "0.1"
---

# Quantum oscillations and high magnetic fields

## 1. Field window and frequency resolution

**Question.** Are the oscillations shown against inverse field, with the background that was subtracted, the field window, any window function and the number of oscillation periods in the window stated for each spectrum?

**Why it matters.** The frequency resolution is set by the width of the window in inverse field. When oscillations appear only at the highest fields, Fourier peaks are too broad to separate close frequencies, end effects of the window produce side lobes, and fitting several components gives better values only if the number and form of the components are already known.

**Resolved by.** Raw and background-subtracted data plotted against inverse field; the background form, field window and window function stated; frequencies that stay put when the window or background is changed; where close frequencies are claimed, a window wide enough to resolve them, or a multi-component fit whose number of components is justified independently.

**Benchmark.** [1], [2]

## 2. Assigning frequencies to orbits

**Question.** How is each frequency assigned to an extremal orbit of the Fermi surface, and does the paper consider harmonics, magnetic breakdown, split orbits and, for torque, interaction effects before counting a frequency as a separate pocket?

**Why it matters.** A spectrum can contain harmonics of a fundamental, frequencies from magnetic breakdown between nearby orbits, components split by bilayer coupling, warping or Zeeman splitting, and, at high field, frequencies from magnetic or torque interaction. The torque signal also depends on how the frequency changes with angle, so it is weak where the frequency is stationary. Band calculations often agree with the data only after bands are shifted.

**Resolved by.** The angle dependence of each frequency over a rotation, compared with calculated extremal areas, with any band shifts stated; harmonics identified by their frequency ratios, amplitudes and masses; breakdown considered for frequencies that appear only at high field; spin zeros or other angle-dependent amplitude features used to tell Zeeman splitting from separate pockets.

**Benchmark.** [1], [2]

## 3. Dimensionality and location of the orbits

**Question.** Where the oscillations are attributed to a two-dimensional surface, layer or interface, does the paper show the frequency against field angle over a wide range of angles, and exclude bulk, defect and trivial surface-layer origins?

**Why it matters.** A frequency that scales as the inverse cosine of the field angle suggests a two-dimensional Fermi surface, but an elongated three-dimensional Fermi surface can give nearly the same scaling over a narrow range of angles. Two-dimensional states can also live on internal planar defects or in trivial accumulation layers, so the angle dependence alone does not locate them on the intended surface.

**Resolved by.** The frequency, and the disappearance of the oscillations near in-plane field, followed to large tilt angles; the bulk carrier density and its contribution to conduction stated; the dependence of the two-dimensional signal on sample thickness or gate voltage, compared with what a surface, defect or bulk origin would give.

**Benchmark.** [3]

## 4. Carrier density from the frequency

**Question.** When a Fermi wavevector or carrier density is derived from a frequency, which Fermi-surface shape and which spin and valley degeneracies are assumed, and does the result agree with the Hall data and with the other pockets?

**Why it matters.** The frequency gives the extremal cross-sectional area of an orbit. Turning that into a density needs an assumed shape and degeneracy; for example a non-topological surface layer carries twice the density of a spin-polarised topological surface state with the same frequency. Several pockets, or a bulk channel, must add up to the density seen in Hall measurements.

**Resolved by.** The relation used between frequency, wavevector and density written out with its assumptions; densities from all observed pockets compared with the Hall density; where bulk and surface channels coexist, a two-channel analysis of the Hall data constrained by the density from the frequency.

**Benchmark.** [1], [3]

## 5. Effective mass from the temperature dependence

**Question.** For each effective mass, does the paper show the oscillation amplitude against temperature with the LK fit, and state the field window, the field value used in the fit and the temperature range?

**Why it matters.** The LK temperature factor depends on the ratio of mass times temperature to field, so the mass depends on which field the amplitude refers to and on how much of the decay the temperature range covers. The mass found this way is the quasiparticle cyclotron mass, which includes many-body renormalisation and differs from the band mass. Amplitudes that do not follow the LK form, such as a harmonic whose mass is not twice that of its fundamental, show that the simple formula does not apply.

**Resolved by.** Amplitude against temperature for each frequency with the fit and its uncertainty; the field window and effective field stated; the mass compared with a calculated band mass or, for a linear dispersion, with the Fermi velocity from photoemission; departures from the LK form reported and discussed, not fitted away.

**Benchmark.** [1], [2], [3]

## 6. Dingle temperature and quantum mobility

**Question.** When the paper quotes a Dingle temperature, quantum lifetime or quantum mobility, does it show the field dependence of the amplitude at fixed temperature, and does it keep these quantities apart from the transport lifetime and Hall mobility?

**Why it matters.** The Dingle factor measures the single-particle lifetime, which counts all scattering events; only samples with a long enough mean free path give oscillations at all. The transport time weights large-angle scattering, and can exceed the single-particle time by up to about a factor of two in three-dimensional metals and by up to about a hundred in modulation-doped two-dimensional systems. A difference between the two mobilities is therefore expected and is not by itself evidence of a special scattering mechanism.

**Resolved by.** A Dingle plot with the mass used in it stated; the Dingle temperature with its uncertainty; the quantum mobility compared with the Hall or transport mobility, with the expected ratio discussed for the scattering in the material.

**Benchmark.** [1], [3], [5]

## 7. Berry phase from a Landau-level fan diagram

**Question.** For a Berry phase taken from a fan diagram, which quantity were the integer indices assigned to (resistivity, conductivity, magnetisation or torque, or a derivative), was the slope fixed to the measured frequency, how far is the extrapolation to zero index, and were Zeeman coupling, a non-linear dispersion and other phase contributions considered?

**Why it matters.** Resistivity minima match conductivity minima only when the longitudinal conductivity is much smaller than the Hall conductivity; when it is much larger, as is common where a conducting bulk is present, they match conductivity maxima, which shifts the intercept by a half. A finite mass or parabolic component and Zeeman coupling bend the fan diagram and move the intercept away from the ideal value, so a straight-line fit can give a phase near the expected value for the wrong reasons. The measured phase offset combines the Berry phase with the orbital magnetic moment and spin terms, and is quantised only under particular symmetry conditions.

**Resolved by.** Longitudinal and Hall data measured together and converted to conductivity before indexing, or a stated reason why resistivity can be used; the slope fixed to the Fourier frequency; data reaching low indices, with the field range and the extrapolation shown; a fit that includes Zeeman and dispersion terms, with independent values of mass, Fermi velocity or g-factor where available; the symmetry argument for a quantised phase stated.

**Benchmark.** [3], [4], [6]

## 8. Pulsed-field measurement conditions

**Question.** For data taken in pulsed fields, does the paper state the sweep rate, compare rising and falling parts of the pulse, estimate the sample temperature during the pulse and say how the field was calibrated?

**Why it matters.** In a conducting sample the changing field drives eddy currents whose heating grows with the square of the sweep rate and with the conductivity, so the sample temperature is not the temperature before the pulse, which affects masses taken from the temperature dependence. Voltages induced in wire loops, in particular by their vibration in an inhomogeneous field, add noise to transport signals, and the field itself is inferred from a pickup coil that must be calibrated.

**Resolved by.** Rising and falling sweeps shown to agree, or the difference explained; the sample temperature during the pulse estimated or measured, and masses checked on the slower part of the pulse or against DC-field data; the pickup-coil calibration stated; wiring loops and their vibration minimised, with the detection frequency and phase-detection method given for ac transport.

**Benchmark.** [7], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | A. Carrington, Quantum oscillation studies of the Fermi surface of iron-pnictide superconductors, Rep. Prog. Phys. 74, 124507 (2011); read as arXiv:1110.1326 | doi:10.1088/0034-4885/74/12/124507 |
| 2 | S. E. Sebastian et al., Towards resolution of the Fermi surface in underdoped high-Tc superconductors, Rep. Prog. Phys. 75, 102501 (2012); read as arXiv:1112.1373 | doi:10.1088/0034-4885/75/10/102501 |
| 3 | Y. Ando, Topological insulator materials, J. Phys. Soc. Jpn. 82, 102001 (2013); read as arXiv:1304.5693 | doi:10.7566/JPSJ.82.102001 |
| 4 | A. A. Taskin and Y. Ando, Berry phase of nonideal Dirac fermions in topological insulators, Phys. Rev. B 84, 035301 (2011); read as arXiv:1103.3096 | doi:10.1103/PhysRevB.84.035301 |
| 5 | S. Das Sarma and F. Stern, Single-particle relaxation time versus scattering time in an impure electron gas, Phys. Rev. B 32, 8442 (1985) | doi:10.1103/PhysRevB.32.8442 |
| 6 | A. Alexandradinata et al., Revealing the topology of Fermi-surface wave functions from magnetic quantum oscillations, Phys. Rev. X 8, 011027 (2018) | doi:10.1103/PhysRevX.8.011027 |
| 7 | S. Takeyama, Bridging the gap between extreme environments and precision measurements: recent progress in megagauss physics, AppliedPhys 2, 6 (2026); read as arXiv:2605.11379v2 | doi:10.3390/appliedphys2020006 |
| 8 | H. Mitamura et al., Improved accuracy in high-frequency AC transport measurements in pulsed high magnetic fields, Rev. Sci. Instrum. 91, 125107 (2020) | doi:10.1063/5.0014986 |
