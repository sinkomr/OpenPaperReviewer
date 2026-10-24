---
id: T-SMALL-FORCE-MEASUREMENT
name: Small-force measurements
type: technique
field: physics/gravitation-precision
applies_when: the paper measures a very small force, torque or acceleration with a torsion balance, torsion pendulum, suspended pendulum, cantilever or similar mechanical oscillator, or bases a claim of a force, a limit on a force or a force sensitivity on such a measurement
version: "0.1"
---

# Small-force measurements

Torsion balances, pendulums, cantilevers and other mechanical oscillators are used to claim the size of a very small force or torque, a limit on one, or the force sensitivity of an instrument. The force is inferred from a displacement or twist through a calibrated stiffness and response, and has to be separated from thermal noise, environmental couplings, electrostatic forces and drift.

## 1. Thermal noise and the damping model

**Question.** Does the paper compare the measured force or torque noise at the signal frequency with the thermal noise expected from the measured stiffness, quality factor and temperature, and does that estimate use a damping model suited to the signal frequency?

**Why it matters.** The fluctuation-dissipation theorem sets the thermal noise from the mechanical loss, but the noise away from resonance depends on how the loss varies with frequency: internal friction in the suspension gives a different spectrum from velocity damping by gas. Gas damping grows when the gap between a test body and its surroundings is small, so a quality factor measured in another geometry or at another pressure can misstate the noise floor.

**Resolved by.** The noise spectrum shown over the signal band with the thermal prediction drawn on it; the stiffness, quality factor, temperature and pressure stated; the loss mechanism identified, or both internal and gas damping estimated for the actual geometry; any excess over the thermal level quantified and its likely sources named; the integration time needed for the quoted sensitivity consistent with the spectrum.

**Benchmark.** [1], [2], [3], [7]

## 2. Spring constant and readout calibration

**Question.** How were the spring constant or torsion constant and the displacement or angle sensitivity of the readout determined, by which method and at what frequency?

**Why it matters.** Common cantilever calibration methods differ from each other, and from traceable references, by several per cent to around ten per cent, and the thermal method also depends on the optical-lever sensitivity, which is itself a frequent source of variation. Internal friction makes a stiffness depend on frequency, so a value measured at resonance does not carry over unchanged to a signal at another frequency. An angle readout needs its own absolute calibration and a check for non-linearity.

**Resolved by.** The calibration method named, with the quantities it used (dimensions, resonant frequency, quality factor, moment of inertia, reference stiffness); where possible, two independent methods compared on the same device, or a traceable reference; the deflection or angle sensitivity measured and its uncertainty stated; the frequency dependence of the stiffness measured or bounded.

**Benchmark.** [2], [4], [5], [6]

## 3. From deflection to force at the signal frequency

**Question.** How is the measured deflection or twist converted into a force or torque at the signal frequency, which response function and effective lever arm are used, and does the conversion fit where and how the force acts on the test body?

**Why it matters.** Away from zero frequency the response of an oscillator depends on its inertia, stiffness and damping, so the same twist corresponds to different torques at different frequencies. Converting a torque to a force needs an effective lever arm, and that arm depends on how the force is distributed over the body, so the same torque noise corresponds to different force noise for different sources.

**Resolved by.** The response function stated and its parameters measured; forces converted to torques with a lever arm justified for the force in question; where possible, the conversion checked with an independently calibrated torque, for example from an electrostatic actuator whose capacitance gradient has been measured.

**Benchmark.** [2], [7]

## 4. Tilt and ground motion

**Question.** How does the paper measure and correct the coupling of floor tilt and ground motion into the measured twist or deflection?

**Why it matters.** A small tilt of the support can twist a fibre through slight asymmetries at its attachment, and tilt or translation can move the test body relative to nearby electrodes or shields and so change forces on it. The feed-through of tilt into twist can be several per cent, depends on details of the apparatus, even from one part of a pendulum to another, and in a rotating apparatus a tilt of the rotation axis from local vertical can mimic the signal.

**Resolved by.** Tilt sensors recording during the measurement; the tilt coupling measured by deliberately tilting the apparatus by a known amount; the correction applied in the time domain, or a feedback loop that holds the support level, with any remaining offset corrected; the size of the correction and its uncertainty given in the error budget.

**Benchmark.** [7], [8]

## 5. Temperature, magnetic and gravity-gradient couplings

**Question.** For temperature changes and gradients, magnetic fields and gravity gradients from the surroundings, does the paper measure how strongly each couples to the signal, and does it combine that coupling with the size of the disturbance during the measurement?

**Why it matters.** Each of these can twist or push the test body: temperature changes twist the fibre and its mounts, magnetic impurities in the test body or its supports respond to field changes, and gravity gradients from the Earth and nearby masses act on imperfections in the test body's mass distribution. The size of each coupling depends on details of the apparatus, so it has to be measured there rather than assumed.

**Resolved by.** Each disturbance deliberately enlarged, for example with heaters, an external magnet or moved masses, and the response measured; the coupling coefficient multiplied by the disturbance recorded during the data run and listed in the error budget; magnetic moments of the test body measured; gravity gradients measured and compensated or bounded; shielding described.

**Benchmark.** [2], [7], [8]

## 6. Charge, contact and patch potentials

**Question.** How does the paper control or bound electrostatic forces from charge on the test body, from contact-potential differences and from spatial and temporal variation of surface potentials between the test body and nearby surfaces?

**Why it matters.** A test body on an insulating fibre is not grounded, and charge on it gives spurious forces. Contact potentials can reach hundreds of millivolts, and even at equal average potential the patch structure of real surfaces gives a force whose size depends on how the surface potential is correlated across the surface. Surface potentials also fluctuate in time, which adds low-frequency force noise.

**Resolved by.** A conducting coating and a grounded shield; the charge measured and controlled, for example by ultraviolet discharge, with its rate stated; the residual potential difference measured and compensated, for example by reversing an applied voltage; the patch force estimated with a stated model of the surface potential and included in the error budget; the measured potential noise compared with the signal band.

**Benchmark.** [2], [8], [9], [10], [11]

## 7. Separating the signal from drift

**Question.** How was the signal modulated, at what frequency compared with the drift and the noise spectrum, and how was the drift removed without absorbing or creating signal?

**Why it matters.** Fibres drift as they slowly unwind, a thermally activated process, and most noise sources rise at low frequency, so an unmodulated or slowly modulated signal is hard to separate from drift. Fitting and subtracting a drift model can remove part of a signal, or leave a residual that looks like one, if the model and the modulation are not chosen together.

**Resolved by.** The signal modulated, for example by moving a source between positions at regular intervals or by rotating the apparatus, with the frequency chosen near the minimum of the noise spectrum; the drift model and fitting interval stated, such as a low-order polynomial fitted with the signal over whole modulation cycles; the drift rate reported and reduced where possible, for example by baking the fibre; a check that the result does not depend on the drift model.

**Benchmark.** [2], [7], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | P. R. Saulson, Thermal noise in mechanical experiments, Phys. Rev. D 42, 2437 (1990) | doi:10.1103/PhysRevD.42.2437 | abstract | Abstract: the fluctuation-dissipation theorem applied to low-loss oscillators; when loss is internal, modelled as a constant imaginary spring constant, the off-resonance thermal noise spectrum differs from the velocity-damping prediction by one power of frequency |
| 2 | C. Rothleitner and S. Schlamminger, Invited Review Article: Measurements of the Newtonian constant of gravitation, G, Rev. Sci. Instrum. 88, 111101 (2017); read as the NIST author manuscript in PubMed Central (PMC8195032) | doi:10.1063/1.4994619 | full text | Sec. III.A: tides and horizontal gravity gradients from the Earth and nearby masses as backgrounds; source position changed at regular intervals to modulate the signal. Sec. IV.A.1: internal versus velocity (gas) damping, most balances limited by internal damping, torque noise from the fluctuation-dissipation theorem, signal placed at the minimum of the noise curve, measurement time follows from the spectral density. Sec. IV.A.2: an insulating fibre leaves the bob ungrounded, charge gives spurious forces, remedies include ultraviolet discharge and conductive coatings; Sec. IV.A.2.a: slow unwinding drift of the fibre suppressed in the analysis, equilibrium readings taken close in time; torsion constant from inertia and period. Sec. IV.A.2.c: contact potentials up to several hundred millivolts, reduced by voltage reversal; capacitance gradient of an electrostatic actuator measured separately; angle-calibration uncertainty. Sec. IV.A.2.d: a full rotation used to check encoder non-linearity |
| 3 | A. Cavalleri, G. Ciani, R. Dolesi, A. Heptonstall, M. Hueller, D. Nicolodi, S. Rowan, D. Tombolato, S. Vitale, P. J. Wass and W. J. Weber, Increased Brownian force noise from molecular impacts in a constrained volume, Phys. Rev. Lett. 103, 140601 (2009); read as arXiv:1107.2520 | doi:10.1103/PhysRevLett.103.140601 | abstract | Abstract: residual-gas damping, and the thermal force noise tied to it, rises markedly when the gap to the surrounding walls is smaller than the test body; measured with two torsion pendulums of different geometry |
| 4 | R. S. Gates, M. G. Reitsma, J. A. Kramar and J. R. Pratt, Atomic force microscope cantilever flexural stiffness calibration: toward a standard traceable method, J. Res. Natl. Inst. Stand. Technol. 116, 703–727 (2011) | doi:10.6028/jres.116.015 | full text | Secs. 6 and 8: methods compared with an SI-traceable electrostatic force balance agree within about 11%; the thermal method has a systematic uncertainty of about 10%, with much of its variation attributed to the optical-lever sensitivity measured in contact, and a correction factor of almost 20%. Table 1: thermal results from two instruments on one cantilever differ by about 8% |
| 5 | J. te Riet, A. J. Katan, C. Rankl, S. W. Stahl, A. M. van Buul, I. Y. Phang, A. Gomez-Casado, P. Schön, J. W. Gerritsen, A. Cambi, A. E. Rowan, G. J. Vancso, P. Jonkheijm, J. Huskens, T. H. Oosterkamp, H. Gaub, P. Hinterdorfer, C. G. Figdor and S. Speller, Interlaboratory round robin on cantilever calibration for AFM force spectroscopy, Ultramicroscopy 111, 1659–1669 (2011) | doi:10.1016/j.ultramic.2011.09.012 | abstract | Abstract: round robin of eight laboratories and ten atomic force microscopes comparing the thermal noise and Sader methods; applying both methods on one instrument served as a consistency check; a miscalibrated cantilever distorts derived parameters |
| 6 | K. Kuroda, Does the time-of-swing method give a correct value of the Newtonian gravitational constant?, Phys. Rev. Lett. 75, 2796 (1995) | doi:10.1103/PhysRevLett.75.2796 | abstract | Abstract: if damping is a frequency-independent imaginary part of the spring constant, the real part must depend on frequency, so a stiffness assumed equal at different frequencies biases the result |
| 7 | L. Carbone, A. Cavalleri, R. Dolesi, C. D. Hoyle, M. Hueller, S. Vitale and W. J. Weber, Upper limits on stray force noise for LISA, Class. Quantum Grav. 21, S611–S620 (2004); read as arXiv:gr-qc/0310119 | doi:10.1088/0264-9381/21/5/033 | full text | Sec. 2: floor tilt moves the pendulum relative to the sensor. Sec. 3: thermal torque noise from stiffness, quality factor and temperature; torque obtained from twist through the pendulum transfer function. Sec. 3.1: tilt coupling measured by deliberately tilting the apparatus; it is the dominant excess noise, considerably higher than tilt-twist couplings reported before, and likely of electrostatic origin. Secs. 3.2 and 3.3: magnetic moments of the pendulum measured with an applied field; temperature-to-twist coupling. Sec. 4: tilt correction applied in the time domain; noise a factor 10 above thermal before and 3 to 5 after correction. Sec. 5: effective lever arm differs for different force sources. Sec. 2: test-mass charging rate about one charge per second; bake-out cut thermally activated fibre drift by about a factor 100 |
| 8 | T. A. Wagner, S. Schlamminger, J. H. Gundlach and E. G. Adelberger, Torsion-balance tests of the weak equivalence principle, Class. Quantum Grav. 29, 184002 (2012); read as arXiv:1207.2442 | doi:10.1088/0264-9381/29/18/184002 | full text | Sec. 2: signal modulated by a rotating turntable, rotation rate chosen against thermal and turntable noise. Sec. 3: most noise sources rise as frequency falls; fibre twists under tilt through asymmetry at the upper attachment, feed-through about 5%, measured by deliberately tilting and corrected; tilts of the rotation axis from local vertical listed among effects that can mimic the signal; tilt held by feedback with a residual offset corrected; gravity gradients compensated and their coupling measured by doubling the gradient; temperature gradients and magnetic fields enlarged on purpose and the response scaled to normal conditions; twist fitted with turntable harmonics and a second-order polynomial drift over whole rotations; gold coating and gold-coated shield against work-function variation. Sec. 5: fused-silica fibres with very high Q gave mHz noise power only a factor 6 below tungsten, for reasons not yet understood |
| 9 | C. C. Speake and C. Trenkel, Forces between conducting surfaces due to spatial variations of surface potential, Phys. Rev. Lett. 90, 160403 (2003) | doi:10.1103/PhysRevLett.90.160403 | abstract | Abstract: methods for estimating the force between conductors from spatially varying surface potential; the force can be large and has a separation dependence similar to the Casimir force |
| 10 | S. E. Pollack, S. Schlamminger and J. H. Gundlach, Temporal extent of surface potentials between closely spaced metals, Phys. Rev. Lett. 101, 071101 (2008) | doi:10.1103/PhysRevLett.101.071101 | abstract | Abstract: surface-potential changes between a test body and its housing are a major low-frequency noise source; a torsion balance measured potential fluctuations between gold-coated plates, flat at about 30 µV/√Hz above 0.1 mHz and rising below |
| 11 | J. Ke, W.-C. Dong, S.-H. Huang, Y.-J. Tan, W.-H. Tan, S.-Q. Yang, C.-G. Shao and J. Luo, Electrostatic effect due to patch potentials between closely spaced surfaces, Phys. Rev. D 107, 065009 (2023); read as arXiv:2302.14826 | doi:10.1103/PhysRevD.107.065009 | abstract | Abstract: spatial and temporal surface-potential variations cause errors in precision experiments; the patch force depends on how surface potentials are correlated and scales with separation and patch size; a model for the frequency dependence of temporal fluctuations |
