---
id: T-SMALL-FORCE-MEASUREMENT
name: Small-force measurements
type: technique
field: physics/gravitation-precision
applies_when: the paper measures a very small force, torque or acceleration with a torsion balance, torsion pendulum, suspended pendulum, cantilever or similar mechanical oscillator, or bases a claim of a force, a limit on a force or a force sensitivity on such a measurement
version: "0.1"
---

# Small-force measurements

## 1. Thermal noise and the damping model

**Question.** Does the paper compare the measured force or torque noise at the signal frequency with the thermal noise expected from the measured stiffness, quality factor and temperature, and does that estimate use a damping model suited to the signal frequency?

**Why it matters.** The fluctuation-dissipation theorem sets the thermal noise from the mechanical loss, but the noise away from resonance depends on how the loss varies with frequency: internal friction in the suspension gives a different spectrum from velocity damping by gas. Gas damping grows when the gap between a test body and its surroundings is small, so a quality factor measured in another geometry or at another pressure can misstate the noise floor.

**Resolved by.** The noise spectrum shown over the signal band with the thermal prediction drawn on it; the stiffness, quality factor, temperature and pressure stated; the loss mechanism identified, or both internal and gas damping estimated for the actual geometry; any excess over the thermal level quantified and its likely sources named; the integration time needed for the quoted sensitivity consistent with the spectrum.

**Benchmark.** [1], [2], [3], [7]

## 2. Spring constant and readout calibration

**Question.** How were the spring constant or torsion constant and the displacement or angle sensitivity of the readout determined, by which method and at what frequency?

**Why it matters.** Common cantilever calibration methods differ from each other, and from traceable references, by several per cent to around ten per cent, and the thermal method also depends on the optical-lever sensitivity, which is itself a frequent source of variation. Internal friction makes a stiffness depend on frequency, so a value measured at resonance does not carry over unchanged to a signal at another frequency. In measurements of G, ignoring this anelasticity biases the time-of-swing and static-deflection methods upwards, by an amount that can approach the inverse of the quality factor. An angle readout needs its own absolute calibration and a check for non-linearity.

**Resolved by.** The calibration method named, with the quantities it used (dimensions, resonant frequency, quality factor, moment of inertia, reference stiffness); where possible, two independent methods compared on the same device, or a traceable reference; the deflection or angle sensitivity measured and its uncertainty stated; the frequency dependence of the stiffness measured or bounded.

**Benchmark.** [2], [4], [5], [6]

## 3. From deflection to force at the signal frequency

**Question.** How is the measured deflection or twist converted into a force or torque at the signal frequency, which response function and effective lever arm are used, and does the conversion fit where and how the force acts on the test body?

**Why it matters.** Away from zero frequency the response of an oscillator depends on its inertia, stiffness and damping, so the same twist corresponds to different torques at different frequencies. Converting a torque to a force needs an effective lever arm, and that arm depends on how the force is distributed over the body, so the same torque noise corresponds to different force noise for different sources.

**Resolved by.** The response function stated and its parameters measured; forces converted to torques with a lever arm justified for the force in question; where possible, the conversion checked with an independently calibrated torque, for example from an electrostatic actuator whose capacitance gradient, including cross-capacitance terms, has been measured.

**Benchmark.** [2], [7]

## 4. Tilt and ground motion

**Question.** How does the paper measure and correct the coupling of floor tilt and ground motion into the measured twist or deflection?

**Why it matters.** A small tilt of the support can twist a fibre through slight asymmetries at its attachment, and tilt or translation can move the test body relative to nearby electrodes or shields and so change forces on it. The feed-through of tilt into twist can be several per cent, depends on details of the apparatus, even from one part of a pendulum to another, and in a rotating apparatus a tilt of the rotation axis from local vertical can mimic the signal.

**Resolved by.** Tilt sensors recording during the measurement; the tilt coupling measured by deliberately tilting the apparatus by a known amount; the correction applied in the time domain, or a feedback loop that holds the support level, with any remaining offset corrected; the size of the correction and its uncertainty given in the error budget.

**Benchmark.** [7], [8]

## 5. Temperature, magnetic and gravity-gradient couplings

**Question.** For temperature changes and gradients, magnetic fields, tides and gravity gradients from the surroundings, does the paper measure how strongly each couples to the signal, and does it combine that coupling with the size of the disturbance during the measurement?

**Why it matters.** Each of these can twist or push the test body: temperature changes twist the fibre and its mounts, magnetic impurities in the test body or its supports respond to field changes, and gravity gradients from the Earth and nearby masses act on imperfections in the test body's mass distribution. The size of each coupling depends on details of the apparatus, so it has to be measured there rather than assumed.

**Resolved by.** Each disturbance deliberately enlarged, for example with heaters, an external magnet or moved masses, and the response measured; the coupling coefficient multiplied by the disturbance recorded during the data run and listed in the error budget; magnetic moments of the test body measured; tides modelled or removed; gravity gradients measured and compensated or bounded; shielding described.

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

| # | Reference | Identifier |
|---|---|---|
| 1 | P. R. Saulson, Thermal noise in mechanical experiments, Phys. Rev. D 42, 2437 (1990) | doi:10.1103/PhysRevD.42.2437 |
| 2 | C. Rothleitner and S. Schlamminger, Invited Review Article: Measurements of the Newtonian constant of gravitation, G, Rev. Sci. Instrum. 88, 111101 (2017); read as the NIST author manuscript in PubMed Central (PMC8195032) | doi:10.1063/1.4994619 |
| 3 | A. Cavalleri et al., Increased Brownian force noise from molecular impacts in a constrained volume, Phys. Rev. Lett. 103, 140601 (2009); read as arXiv:1107.2520 | doi:10.1103/PhysRevLett.103.140601 |
| 4 | R. S. Gates et al., Atomic force microscope cantilever flexural stiffness calibration: toward a standard traceable method, J. Res. Natl. Inst. Stand. Technol. 116, 703 (2011) | doi:10.6028/jres.116.015 |
| 5 | J. te Riet, A. J. Katan, C. Rankl, S. W. Stahl, A. M. van Buul, I. Y. Phang, A. Gomez-Casado, P. Schön, J. W. Gerritsen, A. Cambi, A. E. Rowan, G. J. Vancso, P. Jonkheijm, J. Huskens, T. H. Oosterkamp, H. Gaub, P. Hinterdorfer, C. G. Figdor and S. Speller, Interlaboratory round robin on cantilever calibration for AFM force spectroscopy, Ultramicroscopy 111, 1659 (2011) | doi:10.1016/j.ultramic.2011.09.012 |
| 6 | K. Kuroda, Does the time-of-swing method give a correct value of the Newtonian gravitational constant?, Phys. Rev. Lett. 75, 2796 (1995) | doi:10.1103/PhysRevLett.75.2796 |
| 7 | L. Carbone et al., Upper limits on stray force noise for LISA, Class. Quantum Grav. 21, S611–S620 (2004); read as arXiv:gr-qc/0310119 | doi:10.1088/0264-9381/21/5/033 |
| 8 | T. A. Wagner et al., Torsion-balance tests of the weak equivalence principle, Class. Quantum Grav. 29, 184002 (2012); read as arXiv:1207.2442 | doi:10.1088/0264-9381/29/18/184002 |
| 9 | C. C. Speake and C. Trenkel, Forces between conducting surfaces due to spatial variations of surface potential, Phys. Rev. Lett. 90, 160403 (2003) | doi:10.1103/PhysRevLett.90.160403 |
| 10 | S. E. Pollack et al., Temporal extent of surface potentials between closely spaced metals, Phys. Rev. Lett. 101, 071101 (2008) | doi:10.1103/PhysRevLett.101.071101 |
| 11 | J. Ke et al., Electrostatic effect due to patch potentials between closely spaced surfaces, Phys. Rev. D 107, 065009 (2023); read as arXiv:2302.14826 | doi:10.1103/PhysRevD.107.065009 |
