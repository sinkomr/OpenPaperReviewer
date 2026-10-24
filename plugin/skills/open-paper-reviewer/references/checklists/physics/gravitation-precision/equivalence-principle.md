---
id: T-EQUIVALENCE-PRINCIPLE
name: Tests of the equivalence principle
type: technique
field: physics/gravitation-precision
applies_when: the paper tests the universality of free fall or the weak or strong equivalence principle with a torsion balance, a space accelerometer, an atom interferometer or lunar laser ranging, or quotes, combines or interprets an Eotvos parameter
version: "0.1"
---

# Tests of the equivalence principle

Tests of the equivalence principle (EP) compare the free-fall accelerations of two bodies of different composition towards a common source, using torsion balances, differential accelerometers in space, dual-species atom interferometers or lunar laser ranging (LLR), and claim a limit on, or a value of, the Eotvos parameter: the difference in acceleration divided by the mean acceleration. Distinguishing the weak equivalence principle (WEP), which concerns composition, from the strong equivalence principle (SEP), which also covers gravitational self-energy, matters for LLR.

## 1. Signal definition and modulation

**Question.** Does the paper state the source body the acceleration difference is measured towards, the frequency and phase at which a violation would appear, and how that signal is separated from effects that are fixed to the apparatus, for example by reversing the composition dipole or swapping the species, and by a run with two bodies of the same material? Where the two test masses share a platform, how is leakage of the common-mode acceleration into the differential signal calibrated?

**Why it matters.** A violation is a small differential signal at one known frequency, and any disturbance at that frequency or a harmonic of it can mimic it. Effects that follow the apparatus frame rather than the test bodies, and short transient events in the data, can leave a signal at the violation frequency that only a reversal or a same-material reference reveals. A mismatch in scale factor or alignment between the two sensors converts residual platform acceleration into an apparent differential acceleration.

**Resolved by.** The source, the violation frequency and the expected signal phase stated; data taken with the composition dipole reversed, or with the measurement sequence permuted so that instrumental shifts change sign while the violation does not, and the result formed from the difference; a same-material or reference configuration giving a null result at the same sensitivity; transients identified by a stated rule, with injected mock signals showing the treatment does not remove a real violation; the differential sensitivity and its coupling to common-mode acceleration measured in flight or in situ, for example by driving the platform at a known frequency, and the residual common-mode acceleration at the violation frequency stated.

**Benchmark.** [1], [2], [3]

## 2. Gravity-gradient couplings

**Question.** How large are the couplings between local and Earth gravity gradients and the imperfections of the test-mass configuration (mass multipole moments of a pendulum, off-centring of the test masses, or differences in initial position and velocity of two atomic species), and were they measured directly and suppressed or corrected?

**Why it matters.** Gradients acting on test masses whose centres of mass do not coincide produce a differential force that does not depend on composition, and in many experiments this is the leading systematic. Its size depends on the local mass distribution and on the geometry of the test masses, so it cannot be bounded from design values alone.

**Resolved by.** The gradient measured, for example with a gradiometer pendulum or from the gradient signal at a harmonic of the violation frequency; gradients compensated with nearby masses, or the coupling suppressed by symmetric test bodies or, in atom interferometers, by a gradient-compensation scheme; the coupling measured by deliberately enlarging the gradient or the offset (rotating the compensators, displacing the masses or atom clouds) and scaled to normal operating conditions, with its residual entered in the error budget.

**Benchmark.** [1], [2], [3], [4]

## 3. Thermal effects

**Question.** What temperature variations and gradients are present at the violation frequency, what is the measured sensitivity of the differential signal to them, and how was that sensitivity obtained?

**Why it matters.** Temperature variations and gradients act on the test masses, their housing and the read-out electronics and can produce a differential signal, and they are often modulated at the violation frequency itself, for example by the day-night cycle on the ground or by the orbit and attitude in space. When the temperature at the violation frequency is below the sensor noise, only an upper bound on this systematic is possible.

**Resolved by.** Thermal shielding and control described; the thermal sensitivity measured by applying gradients or heater signals much larger than in normal operation, at or near the violation frequency, and scaled to the measured or bounded temperature variations; for LLR, thermal expansion of reflector mounts and other effects with the synodic period estimated and included.

**Benchmark.** [1], [2], [4], [7]

## 4. Magnetic, tilt and electromagnetic couplings

**Question.** How were couplings of the test masses or atoms to magnetic fields and gradients, and of the apparatus to tilts, and in atom interferometers to light shifts and the quadratic Zeeman effect, bounded at the violation frequency, and does the error budget list each one?

**Why it matters.** Magnetic impurities in the test bodies, tilt that twists a torsion fibre, and species-dependent Zeeman and light shifts each produce a differential signal that does not come from gravity. In atom interferometers these shifts depend on the species' mass and atomic structure, so they do not cancel between the two species.

**Resolved by.** Magnetic shielding described and the coupling measured with a deliberately enlarged field of both polarities, then scaled to the shielded field; tilt monitored and controlled, with its feed-through measured by applying a known tilt; for atom interferometers, magnetically insensitive states, a measured field gradient and a measured or bounded differential light shift; a table of every systematic with its correction and uncertainty.

**Benchmark.** [1], [2], [3], [4]

## 5. Species-dependent phases in atom interferometers

**Question.** For dual-species atom-interferometer tests, how does the paper separate a differential acceleration from phases that depend on mass or beam geometry, such as recoil phases, wavefront effects that differ between clouds of different size or temperature, and rotation effects, and how well is the common-mode noise between species rejected?

**Why it matters.** The two species have different masses, recoil velocities and sometimes different transitions, so phases that cancel in a single-species gravimeter need not cancel in the difference. A phase that scales with recoil or with initial kinematics can mimic an EP signal, and common-mode rejection is weaker for pairs of very different mass.

**Resolved by.** The acceleration extracted from the dependence on momentum transfer or interrogation time, so that terms with a different scaling are removed; beam-direction and detection-order reversals that change the sign of known parasitic phases; beam angles and frequencies calibrated to null the dependence on initial position and velocity; the dependence of the phase on cloud width measured to bound wavefront effects; the common-mode rejection ratio stated for the chosen pair.

**Benchmark.** [3], [4]

## 6. Test-mass composition and construction

**Question.** Does the paper give the actual composition, including alloying elements, of each test mass, the composition-dependent quantities that differ between them, and how the masses were made alike in mass, shape and position?

**Why it matters.** A test is only sensitive to a violation through the difference in composition between the two bodies, and the predicted size of the effect for a given pair depends on the model, through quantities such as nuclear binding and electrostatic energies per unit mass. Differences in mass, shape or centring between the bodies add couplings to gradients that do not depend on composition.

**Resolved by.** Elemental composition of each body stated; a table of the relevant charges per unit mass (for example baryon number, neutron excess or model charges) for the pair used; an argument for the choice of materials in terms of those differences; matched masses and outer dimensions, or a stated correction where they differ.

**Benchmark.** [1], [2], [5]

## 7. Interpretation of the Eotvos parameter

**Question.** Is the quoted Eotvos parameter defined explicitly, including the acceleration it is normalised to, and when it is compared with other tests or turned into a limit on a new interaction, does the paper state the model, the coupling charge and the range assumed?

**Why it matters.** The Eotvos parameter is not a single universal number: it depends on the materials compared and on the source, and a test of one pair constrains only certain combinations of violation parameters. Values from experiments that use different pairs, sources or ranges can be compared only through a stated theoretical framework, and a given charge can differ little between one pair of materials, or be small for one source, leaving that test insensitive to it.

**Resolved by.** The definition and normalising acceleration given for each source (Earth, Sun, galactic centre); limits on a new interaction stated for a named charge, such as baryon number or baryon minus lepton number, as a function of range; comparisons with other experiments made through the same model, with the sensitivity of each pair to its parameters shown.

**Benchmark.** [1], [4], [5], [6]

## 8. Lunar laser ranging: weak versus strong equivalence principle and model dependence

**Question.** For LLR tests, how is the composition-dependent (WEP) contribution separated from the self-energy (SEP) contribution, which fitted parameters correlate with the EP term, and how do the quoted uncertainties account for unmodelled effects?

**Why it matters.** LLR measures the combined difference in the free-fall accelerations of the Earth and Moon towards the Sun, so a composition effect and a self-energy effect could cancel; separating them needs a laboratory test with Earth-like and Moon-like materials. The EP term is extracted from a fit with many correlated parameters, and radiation pressure, thermal expansion, tides, nutation and lunar interior models act on the same synodic signal.

**Resolved by.** A laboratory WEP result for Earth-like and Moon-like materials used to isolate the SEP term, with the combination stated; the correlations of the EP parameter with other fitted parameters given; radiation pressure and thermal effects estimated and corrected; the uncertainty shown to cover model differences, for example by comparing solutions or analyses, not only the formal fit error.

**Benchmark.** [4], [7], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | T. A. Wagner, S. Schlamminger, J. H. Gundlach and E. G. Adelberger, Torsion-balance tests of the weak equivalence principle, Class. Quantum Grav. 29, 184002 (2012); read as arXiv:1207.2442 | doi:10.1088/0264-9381/29/18/184002 | full text | Sec. 2 and Sec. 3: gravity gradients coupled to pendulum imperfections limit current experiments; symmetric pendulum, gradient compensators designed from gradiometer data, compensators rotated 180 degrees to double the gradient and set the correction; each driving term (tilt, gradient, temperature, magnetic field) deliberately exaggerated and scaled to normal conditions, e.g. gradients of 15 K/m against about 44 mK/m, a permanent magnet of both polarities; tilt feed-through measured by tilting; test bodies of identical mass and outer dimensions, dipole inverted to cancel frame-fixed effects. Sec. 1, Eq. 6, and Sec. 3, Tables 1 and 3: Eotvos parameter set by the difference in charge per mass and the source's charge, with Z, N, B and dilaton charges per mass listed, and results given for Earth, Sun and galactic sources with their horizontal accelerations. Sec. 4.1: limits for a B minus L charge versus range |
| 2 | P. Touboul et al. (MICROSCOPE Collaboration), MICROSCOPE mission: final results of the test of the equivalence principle, Phys. Rev. Lett. 129, 121102 (2022); read as arXiv:2209.15487 | doi:10.1103/PhysRevLett.129.121102 | full text | Abstract and results: a same-material Pt reference pair serves as a control with a null result; temperature variations are the main systematic, with thermal sensitivity measured in heater sessions and only an upper bound at the EP frequency; glitches that could imprint at the EP frequency masked by a stated rule and checked with injected mock signals; measurement equation with differential-mode sensitivity matrix through which the common-mode acceleration enters, calibrated in dedicated sessions by shaking the satellite at a known frequency, and residual linear acceleration at the EP frequency stated; off-centrings estimated through the Earth gravity-gradient signal at twice the EP frequency; EP frequency set by orbit plus spin; magnetic effects below requirements given the payload shield; test-mass alloy compositions in Table 1 |
| 3 | P. Asenbaum, C. Overstreet, M. Kim, J. Curti and M. A. Kasevich, Atom-interferometric test of the equivalence principle at the 10^-12 level, Phys. Rev. Lett. 125, 191101 (2020); read as arXiv:2005.11624 | doi:10.1103/PhysRevLett.125.191101 | full text | Gravity-gradient paragraph and Fig. 2: initial position and velocity couple to gradients; pulse frequency shifts compensate, calibrated by displacing the isotopes; beam angles calibrated for horizontal kinematics and rotation. Electromagnetic section and Table 1: quadratic Zeeman phase from a measured field gradient and a bounded differential light shift, with a full error budget. Systematic-error discussion: mass-dependent recoil phases separated by reversing beamsplitter direction; acceleration taken from the slope versus momentum transfer; run permutations of beam direction, detection fringe and imaging order change the sign of instrumental shifts |
| 4 | G. M. Tino, L. Cacciapuoti, S. Capozziello, G. Lambiase and F. Sorrentino, Precision gravity tests and the Einstein equivalence principle, Prog. Part. Nucl. Phys. 112, 103772 (2020); read as arXiv:2002.02907 | doi:10.1016/j.ppnp.2020.103772 | full text | Sec. 3.1.1: torsion-balance gradients couple to geometric asymmetries; compensators, gradiometer, tilt sensing, thermal and magnetic effects calibrated by modulating each driving parameter; temperature variations occurring naturally at the diurnal frequency. Sec. 3.2: LLR combines a composition term and a self-energy term, so an independent laboratory test with Earth- and Moon-like bodies is needed to exclude cancellation. Secs. 3.3.3 to 3.3.6: gravity gradients limit atom tests; dual-species results limited by quadratic Zeeman effect and wavefront curvature; common-mode rejection much weaker for pairs of different mass; species choice compared with dilaton and standard-model-extension frameworks |
| 5 | T. Damour, Theoretical aspects of the equivalence principle, Class. Quantum Grav. 29, 184001 (2012); read as arXiv:1202.6311 | doi:10.1088/0264-9381/29/18/184001 | full text | Sec. 3, Eqs. 3.3 to 3.25 and Table I: the Eotvos parameter depends on the difference of composition-dependent dilaton charges (Coulomb and surface binding terms) of the two materials and on the source; the predicted structure can guide the choice of materials; a two-parameter model lets different material pairs and LLR be compared on the same footing |
| 6 | C. M. Will, The confrontation between general relativity and experiment, Living Rev. Relativ. 17, 4 (2014); read as arXiv:1403.7377 | doi:10.12942/lrr-2014-4 | full text | Sec. 2.1.1, Eqs. 1 and 2: the Eotvos ratio is a sum over interactions of a violation parameter times the difference in the bodies' fractions of energy from that interaction, so a limit constrains violation parameters only through the test-body composition |
| 7 | J. G. Williams, S. G. Turyshev and D. Boggs, Lunar laser ranging tests of the equivalence principle, Class. Quantum Grav. 29, 184004 (2012); read as arXiv:1203.2150 | doi:10.1088/0264-9381/29/18/184004 | full text | Secs. 2.1 and 6: LLR is sensitive to either WEP or SEP violations, which displace the lunar orbit along the Earth-Sun line with a 29.53-day cos D signature. Secs. 4 and 5: solar radiation pressure taken from an external estimate; thermal expansion of reflector mounts with the same period as the EP signal; nutation parameters correlated 0.90 with the EP term; lunar interior models and correlations with GM, eccentricity and Love number listed |
| 8 | T. W. Murphy Jr, Lunar laser ranging: the millimeter challenge, Rep. Prog. Phys. 76, 076901 (2013); read as arXiv:1309.6294 | doi:10.1088/0034-4885/76/7/076901 | full text | Sec. 2.1.1: the Earth-Moon pair differs in self-energy and in having an iron core, so LLR is also sensitive to WEP, and laboratory tests with Earth- and Moon-like objects help separate the cases. Secs. 5.1 to 5.4: many correlated fit parameters, partly modelled effects, a gap between millimetre range uncertainties and model residuals, and step-by-step comparison of independent analysis codes |
