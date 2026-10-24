---
id: T-QUANTUM-OSCILLATIONS
name: Quantum oscillations and high magnetic fields
type: technique
field: physics/condensed-matter
applies_when: the paper reports de Haas-van Alphen or Shubnikov-de Haas oscillations, torque or other measurements in high DC or pulsed fields, or derives Fermi-surface areas, effective masses, quantum lifetimes, carrier densities or a Berry phase from oscillations periodic in inverse field
version: "0.1"
---

# Quantum oscillations and high magnetic fields

Quantum oscillations, periodic in inverse magnetic field, are seen in the magnetisation or magnetic torque (the de Haas-van Alphen, dHvA, effect) and in the resistivity (the Shubnikov-de Haas, SdH, effect). They are used to claim the extremal cross-sections of the Fermi surface, its dimensionality, carrier densities, effective masses and scattering times through the Lifshitz-Kosevich (LK) formula, and a Berry phase from Landau-level (LL) fan diagrams, often from data taken in high DC or pulsed fields.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | A. Carrington, Quantum oscillation studies of the Fermi surface of iron-pnictide superconductors, Rep. Prog. Phys. 74, 124507 (2011); read as arXiv:1110.1326 | doi:10.1088/0034-4885/74/12/124507 | full text | Sec. 1.1: LK formula for the oscillatory torque with temperature, Dingle and spin factors, the torque term depending on the angular derivative of the frequency, quasiparticle mass distinguished from band mass, Onsager relation between frequency and extremal area, only samples with long enough mean free path give a signal. Sec. 3: masses from fits to the temperature factor; frequencies tracked with angle and compared with band calculations needing band shifts; some high-field frequencies possibly from magnetic breakdown or torque interaction; polynomial background subtracted from torque. Sec. 4.1: when oscillations appear only at the highest fields the Fourier peaks are too broad to resolve individual frequencies |
| 2 | S. E. Sebastian, N. Harrison and G. G. Lonzarich, Towards resolution of the Fermi surface in underdoped high-Tc superconductors, Rep. Prog. Phys. 75, 102501 (2012); read as arXiv:1112.1373 | doi:10.1088/0034-4885/75/10/102501 | full text | Sec. 1, Fig. 2 caption: windowing limits frequency resolution, a window function suppresses side lobes from end effects, and curve fitting improves on Fourier analysis only if the number and form of components are known. Secs. 2.4 and 2.5.5: several frequencies can arise from bilayer splitting, magnetic breakdown and warping. Sec. 2.4 and Fig. 6 caption: a harmonic identified by its phase and by its amplitude scaling as the square of the fundamental, departing from the LK expectation that its mass is twice the fundamental mass. Sec. 2.2: spin zeros in the angle dependence of the amplitude used to obtain the g-factor |
| 3 | Y. Ando, Topological insulator materials, J. Phys. Soc. Jpn. 82, 102001 (2013); read as arXiv:1304.5693 | doi:10.7566/JPSJ.82.102001 | full text | Sec. 8.3: inverse-cosine angle dependence suggests a 2D origin but an elongated 3D Fermi surface can mimic it, so a wide angle range is needed; 2D states may sit on planar defects; integer index assigned to conductivity, not resistivity, minima, with resistivity safe only when the longitudinal conductivity is much smaller than the Hall conductivity, and resistivity minima at conductivity maxima in the opposite limit; slope fixed to the Fourier frequency; mass from the temperature dependence of the amplitude, compared with photoemission for a Dirac dispersion; Dingle plot gives the lifetime and quantum mobility. Sec. 8.4: two-band Hall analysis with the surface density fixed by the frequency; a non-topological surface layer has a density twice as large for the same frequency; surface mobility from transport typically exceeds that from SdH. Sec. 5: a trivial accumulation or inversion layer can also give surface-dominated transport |
| 4 | A. A. Taskin and Y. Ando, Berry phase of nonideal Dirac fermions in topological insulators, Phys. Rev. B 84, 035301 (2011); read as arXiv:1103.3096 | doi:10.1103/PhysRevB.84.035301 | full text | Abstract and Sec. I: reported fan-diagram results usually unconvincing, with phases deviating from the exact value. Secs. IV to VI: a finite mass shifts the fan-diagram lines and makes them curved, Zeeman coupling can cancel or add to this, so a straight-line fit should not be used to determine the Berry phase; deviations largest near the quantum limit |
| 5 | S. Das Sarma and F. Stern, Single-particle relaxation time versus scattering time in an impure electron gas, Phys. Rev. B 32, 8442 (1985) | doi:10.1103/PhysRevB.32.8442 | abstract | Abstract: the transport scattering time is at most about twice the single-particle time in typical 3D metals, but can be up to about two orders of magnitude larger in high-mobility heterojunctions with remote impurities |
| 6 | A. Alexandradinata, C. Wang, W. Duan and L. Glazman, Revealing the topology of Fermi-surface wave functions from magnetic quantum oscillations, Phys. Rev. X 8, 011027 (2018) | doi:10.1103/PhysRevX.8.011027 | abstract | Abstract: the Berry phase and the orbital magnetic moment are both encoded as a phase in the Bohr-Sommerfeld quantisation condition, and this phase is robustly quantised only for certain solids and field orientations set by the symmetry of the orbit |
| 7 | S. Takeyama, Bridging the gap between extreme environments and precision measurements: recent progress in megagauss physics, AppliedPhys 2, 6 (2026); read as arXiv:2605.11379v2 | doi:10.3390/appliedphys2020006 | full text | Sec. 3.1: induced pickup voltage scales with the sweep rate; pickup coils calibrated against a reference coil. Sec. 4.4: the temperature before the pulse is the sample temperature only for insulators; for conductors the eddy-current Joule heating, scaling with the square of the sweep rate and with the magnetoconductivity, must be added |
| 8 | H. Mitamura, R. Watanuki, E. Kampert, T. Förster, A. Matsuo, T. Onimaru, N. Onozaki, Y. Amou, K. Wakiya, K. T. Matsumoto, I. Yamamoto, K. Suzuki, S. Zherlitsyn, J. Wosnitza, M. Tokunaga, K. Kindo and T. Sakakibara, Improved accuracy in high-frequency AC transport measurements in pulsed high magnetic fields, Rev. Sci. Instrum. 91, 125107 (2020) | doi:10.1063/5.0014986 | abstract | Abstract: accurate ac transport in short pulses is possible with numerical phase detection over integer periods and a defined phase angle; the dominant low-frequency noise comes from induction by mechanical vibration of wire loops in inhomogeneous fields |
