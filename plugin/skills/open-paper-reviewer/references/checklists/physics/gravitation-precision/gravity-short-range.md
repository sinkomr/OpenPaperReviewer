---
id: T-GRAVITY-SHORT-RANGE
name: Measurements of G and short-range gravity
type: technique
field: physics/gravitation-precision
applies_when: the paper reports a value of the Newtonian constant G, or tests the gravitational inverse-square law or searches for a Yukawa-type or fifth force between laboratory bodies, using torsion balances, pendulums, cantilevers, atom interferometers or Casimir force measurements
version: "0.1"
---

# Measurements of G and short-range gravity

## 1. Source and test mass characterisation

**Question.** How were the mass, dimensions, density distribution and position of each source and test mass measured, and how does each of them enter the calculated gravitational signal?

**Why it matters.** Bodies close to each other cannot be treated as point masses: the signal is an integral over their density distributions, so density variation, shape errors and position errors pass directly into G or into a short-range limit. Dense metals cannot be checked by X-ray imaging, so homogeneity is often inferred from a sacrificed sample, and tanks, holders and mounts add mass that has to be modelled.

**Resolved by.** Masses, dimensions and positions measured with stated uncertainties; a direct check of density homogeneity, or a source whose density is uniform by construction; shapes chosen or verified so that the integral is well defined; the mass integration including every supporting part, with the sensitivity of the result to each geometric parameter given; in fits, these parameters treated as constrained by their independent measurements; masses of low magnetic susceptibility that conduct electricity.

**Benchmark.** [1], [4]

## 2. Casimir and van der Waals backgrounds

**Question.** At separations below about ten micrometres, how does the paper account for the Casimir or van der Waals force, which theory and material properties were used to calculate it, and how does the uncertainty of that calculation enter any limit on a new force?

**Why it matters.** The Casimir force rises steeply as the gap closes; for millimetre-sized bodies it equals the Newtonian force near 13 µm between plates and near 2.5 µm between a sphere and a plate. Its calculated value depends strongly on the model of the dielectric response used, and corrections for finite temperature, finite conductivity and roughness all vary with separation, so an error in the subtracted background can mimic or hide a new force. A rigid shield keeps the bodies some tens of micrometres apart, so at smaller separations there is none, and any limit is set by the experimental and theoretical uncertainty of the electromagnetic force.

**Resolved by.** The Casimir calculation stated in full: dielectric model, optical data, temperature, roughness and finite-size corrections; the limit derived with the theoretical uncertainty included; the effect of plausible alternative material models and of patch forces on the limit shown.

**Benchmark.** [4], [5], [6], [7]

## 3. Separation and the Newtonian signal in short-range tests

**Question.** How was the absolute separation between the surfaces determined, and how was the Newtonian force between the actual finite bodies calculated and removed or nulled?

**Why it matters.** Forces at short range vary steeply with separation, so an error in the zero of the separation scale shifts both the subtracted backgrounds and any inferred deviation. Separations found from mechanical or electrical contact can be unreliable, since asperities on the surfaces touch first. Finite bodies give a large Newtonian signal whose size depends on the full geometry; null and partial-null designs reduce it, but only to the extent that the geometry matches the design.

**Resolved by.** Separation found by an independent method, such as capacitance or electrostatic calibration, and the zero treated as a fitted parameter constrained by that measurement; the residual potential between the surfaces measured at each separation, with its dependence on separation shown; the Newtonian signal computed by integration over the measured geometry, including holes, coatings and supports; for null designs, the residual Newtonian signal and its sensitivity to misalignment given; the alignment procedure stated; vibration from the moving source kept out of the signal band.

**Benchmark.** [4], [5], [7]

## 4. From the data to a limit on a new force

**Question.** How is the measured force, or its absence, converted into a limit in the strength–range plane of a Yukawa-type interaction, which experimental parameters are free or constrained in that fit, and at what confidence level?

**Why it matters.** The limit on α at a given λ depends on integrating the modified potential over each body, which differs from the point-mass result once λ approaches the size of the bodies or the gap between them. It also depends on how geometric and calibration parameters are treated and on the statistical procedure, and a limit in Yukawa form does not carry over directly to other forms such as power laws.

**Resolved by.** The potential and its parameterisation stated; the finite-size integration carried out; masses, dimensions, the separation zero and the force calibration constrained by independent measurements and varied in the fit; the confidence level and the procedure stated; any conversion to another form of deviation stated.

**Benchmark.** [4], [5]

## 5. Agreement with other measurements of G

**Question.** How does the reported value of G compare with the CODATA recommended value and with individual earlier measurements by different methods, and does the paper discuss the agreement in light of the known excess spread between them?

**Why it matters.** Published values of G disagree by much more than their stated uncertainties, and CODATA enlarges all of them by a common factor so that every normalised residual falls to two or less. The spread points to unrecognised systematic effects or uncertainty missing from budgets, so a new value with a small stated uncertainty does not settle the question by itself, and a value far from the others needs a correspondingly full account of systematic effects.

**Resolved by.** A comparison with the recommended value and with individual measurements, grouped by method; an uncertainty budget that addresses the effects known to have biased earlier methods; where possible, a check of the result by a second experimental approach, or a repeated measurement with a changed configuration; any interpretation as new physics supported by tests designed for it, such as comparisons at several length scales.

**Benchmark.** [1], [2], [3]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | C. Rothleitner and S. Schlamminger, Invited Review Article: Measurements of the Newtonian constant of gravitation, G, Rev. Sci. Instrum. 88, 111101 (2017); read as the NIST author manuscript in PubMed Central (PMC8195032) | doi:10.1063/1.4994619 |
| 2 | P. J. Mohr et al., CODATA recommended values of the fundamental physical constants: 2022, Rev. Mod. Phys. 97, 025002 (2025); read as arXiv:2409.03787 | doi:10.1103/RevModPhys.97.025002 |
| 3 | C. Merkatas et al., Shades of dark uncertainty and consensus value for the Newtonian constant of gravitation, Metrologia 56, 054001 (2019) | doi:10.1088/1681-7575/ab3365 |
| 4 | E. G. Adelberger et al., Tests of the gravitational inverse-square law, Annu. Rev. Nucl. Part. Sci. 53, 77 (2003); read as arXiv:hep-ph/0307284 | doi:10.1146/annurev.nucl.53.041002.110503 |
| 5 | J. Murata and S. Tanaka, Review of short-range gravity experiments in the LHC era, Class. Quantum Grav. 32, 033001 (2015); read as arXiv:1408.3588 | doi:10.1088/0264-9381/32/3/033001 |
| 6 | R. O. Behunin et al., Modeling electrostatic patch effects in Casimir force measurements, Phys. Rev. A 85, 012504 (2012) | doi:10.1103/PhysRevA.85.012504 |
| 7 | G. L. Klimchitskaya et al., The Casimir force between real materials: experiment and theory, Rev. Mod. Phys. 81, 1827 (2009); read as arXiv:0902.4022 | doi:10.1103/RevModPhys.81.1827 |
