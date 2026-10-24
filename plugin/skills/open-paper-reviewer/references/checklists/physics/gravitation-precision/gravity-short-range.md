---
id: T-GRAVITY-SHORT-RANGE
name: Measurements of G and short-range gravity
type: technique
field: physics/gravitation-precision
applies_when: the paper reports a value of the Newtonian constant G, or tests the gravitational inverse-square law or searches for a Yukawa-type or fifth force between laboratory bodies, using torsion balances, pendulums, cantilevers, atom interferometers or Casimir force measurements
version: "0.1"
---

# Measurements of G and short-range gravity

Laboratory gravity experiments are used to claim a value of the Newtonian constant of gravitation G, or a deviation from, or a limit on deviations from, the inverse-square law, often expressed as a Yukawa-type force of strength α and range λ. Both rest on calculating the Newtonian attraction of real, finite bodies and separating it from much larger forces of other origins.

## 1. Source and test mass characterisation

**Question.** How were the mass, dimensions, density distribution and position of each source and test mass measured, and how does each of them enter the calculated gravitational signal?

**Why it matters.** Bodies close to each other cannot be treated as point masses: the signal is an integral over their density distributions, so density variation, shape errors and position errors pass directly into G or into a short-range limit. Dense metals cannot be checked by X-ray imaging, so homogeneity is often inferred from a sacrificed sample, and tanks, holders and mounts add mass that has to be modelled.

**Resolved by.** Masses, dimensions and positions measured with stated uncertainties; a direct check of density homogeneity, or a source whose density is uniform by construction; shapes chosen or verified so that the integral is well defined; the mass integration including every supporting part, with the sensitivity of the result to each geometric parameter given; in fits, these parameters treated as constrained by their independent measurements.

**Benchmark.** [1], [5]

## 2. Fibre anelasticity and the spring constant

**Question.** Where the torsion constant of a fibre or the stiffness of a suspension enters the result, at what frequency was it determined, and does the analysis correct for its dependence on frequency?

**Why it matters.** Internal friction makes the stiffness of a fibre depend on frequency. The time-of-swing method assumes the stiffness is the same at the two oscillation frequencies it compares, and the static-deflection method uses a stiffness measured at the free oscillation frequency; in both cases ignoring anelasticity biases G upwards, by an amount that can approach the inverse of the quality factor.

**Resolved by.** Fibre material, quality factor and loss angle stated; the anelastic correction applied with its uncertainty, based on a measured or bounded frequency dependence; or a method in which the fibre stiffness does not enter, with the residual dependence on it shown to be small.

**Benchmark.** [1], [2]

## 3. Environmental and parasitic couplings in G measurements

**Question.** How were tides, gravity gradients from the Earth and nearby masses, and electrostatic and magnetic forces on the test body separated from the signal of the source masses?

**Why it matters.** Tidal changes in local gravity can be far larger than the force from laboratory source masses, and horizontal gradients from the surroundings act on a torsion balance. A test body on an insulating fibre is not grounded, so charge on it produces spurious torques; contact potentials and parasitic capacitances affect electrostatic servo methods, and an omitted cross-capacitance term can bias the result. Magnetic or electrically insulating masses add forces of their own. Atom gradiometers need the local gravity gradient known or removed.

**Resolved by.** The signal modulated by moving the source masses between positions, with the background recorded; tides modelled or removed; gradients of the surroundings measured and their effect estimated; charge on the test body controlled by grounding, discharge or a conductive coating; electrostatic actuators calibrated including cross terms; masses of low magnetic susceptibility that conduct electricity; for gradiometers, extra measurements with repositioned source masses that remove the gradient of the Earth.

**Benchmark.** [1]

## 4. Electrostatic, magnetic and mechanical backgrounds at short range

**Question.** For forces measured at sub-millimetre separations, how does the paper bound forces from contact-potential differences, surface patch potentials, magnetic impurities and mechanical coupling of the moving source to the detector, and was the residual potential between the surfaces measured at each separation?

**Why it matters.** A potential difference of about ten millivolts between millimetre-thick plates 0.1 mm apart gives an electrostatic force as large as gravity, and it grows as the gap closes while the Newtonian force between plates does not. Even at equal average potential, patch potentials from crystal grains and contaminants give a force whose distance dependence resembles that of the Casimir force. Ferromagnetic inclusions whose fields are hard to detect with standard magnetometers can give forces comparable to gravity, and vibration from the moving source can reach the detector through the apparatus.

**Resolved by.** A rigid, grounded conducting shield between source and detector where the separation allows; surfaces coated with a material whose work function varies little; the residual potential measured and compensated, with its dependence on separation shown; the patch force estimated with a stated model of the surface potential and included in the error budget; non-magnetic machining and handling, magnetic screening, and checks for fields produced by the moving source; vibration isolation, and a design in which the signal appears at a frequency different from that of the source motion.

**Benchmark.** [5], [7], [8], [9]

## 5. Casimir and van der Waals backgrounds

**Question.** At separations below about ten micrometres, how does the paper account for the Casimir or van der Waals force, which theory and material properties were used to calculate it, and how does the uncertainty of that calculation enter any limit on a new force?

**Why it matters.** The Casimir force rises steeply as the gap closes; for millimetre-sized bodies it equals the Newtonian force near 13 µm between plates and near 2.5 µm between a sphere and a plate. Its calculated value depends strongly on the model of the dielectric response used, and corrections for finite temperature, finite conductivity and roughness all vary with separation, so an error in the subtracted background can mimic or hide a new force. A rigid shield keeps the bodies some tens of micrometres apart, so at smaller separations there is none, and any limit is set by the experimental and theoretical uncertainty of the electromagnetic force.

**Resolved by.** The Casimir calculation stated in full: dielectric model, optical data, temperature, roughness and finite-size corrections; the limit derived with the theoretical uncertainty included; the effect of plausible alternative material models and of patch forces on the limit shown.

**Benchmark.** [5], [6], [8], [9]

## 6. Separation and the Newtonian signal in short-range tests

**Question.** How was the absolute separation between the surfaces determined, and how was the Newtonian force between the actual finite bodies calculated and removed or nulled?

**Why it matters.** Forces at short range vary steeply with separation, so an error in the zero of the separation scale shifts both the subtracted backgrounds and any inferred deviation. Separations found from mechanical or electrical contact can be unreliable, since asperities on the surfaces touch first. Finite bodies give a large Newtonian signal whose size depends on the full geometry; null and partial-null designs reduce it, but only to the extent that the geometry matches the design.

**Resolved by.** Separation found by an independent method, such as capacitance or electrostatic calibration, and the zero treated as a fitted parameter constrained by that measurement; the Newtonian signal computed by integration over the measured geometry, including holes, coatings and supports; for null designs, the residual Newtonian signal and its sensitivity to misalignment given; the alignment procedure stated.

**Benchmark.** [5], [6], [9]

## 7. From the data to a limit on a new force

**Question.** How is the measured force, or its absence, converted into a limit in the strength–range plane of a Yukawa-type interaction, which experimental parameters are free or constrained in that fit, and at what confidence level?

**Why it matters.** The limit on α at a given λ depends on integrating the modified potential over each body, which differs from the point-mass result once λ approaches the size of the bodies or the gap between them. It also depends on how geometric and calibration parameters are treated and on the statistical procedure, and a limit in Yukawa form does not carry over directly to other forms such as power laws.

**Resolved by.** The potential and its parameterisation stated; the finite-size integration carried out; masses, dimensions, the separation zero and the force calibration constrained by independent measurements and varied in the fit; the confidence level and the procedure stated; any conversion to another form of deviation stated.

**Benchmark.** [5], [6]

## 8. Agreement with other measurements of G

**Question.** How does the reported value of G compare with the CODATA recommended value and with individual earlier measurements by different methods, and does the paper discuss the agreement in light of the known excess spread between them?

**Why it matters.** Published values of G disagree by much more than their stated uncertainties, and CODATA enlarges all of them by a common factor so that every normalised residual falls to two or less. The spread points to unrecognised systematic effects or uncertainty missing from budgets, so a new value with a small stated uncertainty does not settle the question by itself, and a value far from the others needs a correspondingly full account of systematic effects.

**Resolved by.** A comparison with the recommended value and with individual measurements, grouped by method; an uncertainty budget that addresses the effects known to have biased earlier methods; where possible, a check of the result by a second experimental approach, or a repeated measurement with a changed configuration; any interpretation as new physics supported by tests designed for it, such as comparisons at several length scales.

**Benchmark.** [1], [3], [4]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | C. Rothleitner and S. Schlamminger, Invited Review Article: Measurements of the Newtonian constant of gravitation, G, Rev. Sci. Instrum. 88, 111101 (2017); read as the NIST author manuscript in PubMed Central (PMC8195032) | doi:10.1063/1.4994619 | full text | Sec. III.A: tides change g by far more than the source-mass force; horizontal gradients act on a torsion balance. Sec. IV.A.2: insulating silica fibres leave the bob ungrounded, so charge gives spurious forces. Secs. IV.A.2.a and IV.A.2.b: frequency-dependent fibre stiffness biases static-deflection and time-of-swing results high unless corrected, with bounds of order 1/Q. Sec. IV.A.2.c: contact potentials, parasitic capacitances and an omitted cross-capacitance term. Secs. IV.D.3 and IV.D.4: for atom gradiometers the Earth's gradient is known only to a few per cent and is removed with repositioned source masses. Secs. IV.C.2 and V: density variation must be integrated over, dense masses examined destructively, liquid sources need tank modelling, shape tolerances; masses should have low magnetic susceptibility and conduct electricity. Sec. I: spread beyond stated uncertainties, dark uncertainty, repeating with another experimental approach. Sec. VI: Birge ratio about five; a dedicated experiment at two length scales to test new physics |
| 2 | K. Kuroda, Does the time-of-swing method give a correct value of the Newtonian gravitational constant?, Phys. Rev. Lett. 75, 2796 (1995) | doi:10.1103/PhysRevLett.75.2796 | abstract | Abstract: if fibre damping is a constant imaginary part of the stiffness, the real part must vary with frequency, and the time-of-swing method then biases G upwards |
| 3 | P. J. Mohr, D. B. Newell, B. N. Taylor and E. Tiesinga, CODATA recommended values of the fundamental physical constants: 2022, Rev. Mod. Phys. 97, 025002 (2025); read as arXiv:2409.03787 | doi:10.1103/RevModPhys.97.025002 | full text | Sec. XIV and Table XXX: the 16 input values of G from different methods. Sec. XV.A: G is determined separately as a weighted mean, and an expansion factor of 3.9 reduces all normalised residuals to 2 or less |
| 4 | C. Merkatas, B. Toman, A. Possolo and S. Schlamminger, Shades of dark uncertainty and consensus value for the Newtonian constant of gravitation, Metrologia 56, 054001 (2019) | doi:10.1088/1681-7575/ab3365 | abstract | Abstract: measurements of G disagree more than their stated uncertainties imply; standard practice inflates uncertainties by a factor or a random effect to account for dark uncertainty |
| 5 | E. G. Adelberger, B. R. Heckel and A. E. Nelson, Tests of the gravitational inverse-square law, Annu. Rev. Nucl. Part. Sci. 53, 77–121 (2003); read as arXiv:hep-ph/0307284 | doi:10.1146/annurev.nucl.53.041002.110503 | full text | Sec. 1.1.1: Yukawa parameterisation. Sec. 3.3.1: 10 mV between 1-mm plates 0.1 mm apart gives a force equal to gravity, growing as the gap closes; patch fields from crystal planes and contaminants; gold has small work-function variation. Sec. 3.3.2: Casimir force equals the Newtonian force near 13 µm (plates) and 2.5 µm (sphere-plane); temperature, conductivity and roughness corrections vary with separation and can mimic an anomaly. Sec. 3.3.3: rigid conducting shield limits the separation to tens of micrometres. Sec. 3.3.4: iron inclusions with hard-to-detect fields and fields from the moving attractor. Sec. 3.3.5: mechanical coupling of attractor motion, reduced by vibration isolation and a signal frequency different from the drive. Sec. 3.4: null and partial-null designs. Sec. 4.1.4: separations from contact unreliable, capacitance used. Sec. 4.1.5: α and λ free, hole masses, dimensions, separation zero and torque calibration constrained by independent measurements, 95% confidence limits. Sec. 4.4.1: surfaces touched at about 33 nm because of protruding crystals |
| 6 | J. Murata and S. Tanaka, Review of short-range gravity experiments in the LHC era, Class. Quantum Grav. 32, 033001 (2015); read as arXiv:1408.3588 | doi:10.1088/0264-9381/32/3/033001 | full text | Secs. 2.1.2 and 2.1.3: relative and null measurements and what nulling does and does not improve. Secs. 2.2.1 to 2.2.3: deriving α as a function of λ, power-law alternative, finite-size integration needed when λ approaches the gap. Secs. 3.1 and 5.2: below about 10 µm shielding is hard to place, so limits come from Casimir experiments and are bounded by the experimental and theoretical precision of electromagnetic forces whose theory is complex. Secs. 3.2 and 4: a Yukawa α can mislead when comparing with power-law models |
| 7 | C. C. Speake and C. Trenkel, Forces between conducting surfaces due to spatial variations of surface potential, Phys. Rev. Lett. 90, 160403 (2003) | doi:10.1103/PhysRevLett.90.160403 | abstract | Abstract: patch potentials can give a force large compared with the Casimir force, with a broadly similar dependence on the closest separation |
| 8 | R. O. Behunin, F. Intravaia, D. A. R. Dalvit, P. A. Maia Neto and S. Reynaud, Modeling electrostatic patch effects in Casimir force measurements, Phys. Rev. A 85, 012504 (2012) | doi:10.1103/PhysRevA.85.012504 | abstract | Abstract: surface potential variations give forces between neutral conductors at micrometre separations that must be accounted for; a patch model shows they can contribute significantly and change which Casimir theory the data favour |
| 9 | G. L. Klimchitskaya, U. Mohideen and V. M. Mostepanenko, The Casimir force between real materials: experiment and theory, Rev. Mod. Phys. 81, 1827–1885 (2009); read as arXiv:0902.4022 | doi:10.1103/RevModPhys.81.1827 | full text | Abstract: problems in applying Lifshitz theory to real materials. Sec. II.D.1: calculated forces depend strongly on the dielectric model used for metals. Sec. III.A: permittivity obtained from tabulated optical data. Sec. I.D: Casimir measurements used to constrain hypothetical new forces. Sec. III.B.1: patch potentials of polycrystalline films can simulate the Casimir force. Sec. IV.A: residual potential and separation on contact found by electrostatic calibration, absolute separation built from it with interferometric piezo calibration |
