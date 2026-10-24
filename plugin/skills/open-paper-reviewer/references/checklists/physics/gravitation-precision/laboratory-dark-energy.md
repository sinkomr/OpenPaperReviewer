---
id: T-LABORATORY-DARK-ENERGY
name: Laboratory searches for dark energy
type: technique
field: physics/gravitation-precision
applies_when: the paper searches for, or sets limits on, screened scalar fields such as chameleons or symmetrons using atom interferometry, torsion balances, neutron bouncing or interferometry, or Casimir-type force measurements, or quotes, compares or reinterprets an excluded region for such fields
version: "0.1"
---

# Laboratory searches for dark energy

Laboratory searches for dark energy look for a fifth force from a scalar field whose effects are hidden in dense environments by a screening mechanism, as in chameleon and symmetron models, using atom interferometry, torsion balances, ultracold neutrons and Casimir-type force measurements. They claim a detected force or, more often, an excluded region in the model's parameter space, and that region is only as reliable as the calculation that turns the apparatus into a predicted signal.

## 1. Model and parameter conventions

**Question.** Does the paper name the model it tests, give the form of the potential and the coupling, state which parameters were fixed and at what values (for a chameleon the power-law index n, the energy scale Lambda and the coupling strength, written as beta or as a mass scale M; for a symmetron its mass, self-coupling and coupling scale), and use the same conventions when it compares its result with other experiments?

**Why it matters.** The predicted force depends strongly on these parameters, so a limit for one power-law index, one energy scale or one symmetron mass says little about other values: constraints are typically strongest for a few index values and weaken or vanish for others. Bounds are quoted in several conventions, and a comparison that mixes them, or that sets the energy scale to the dark-energy value in one result but not another, is not like for like.

**Resolved by.** The potential, coupling function and every fixed parameter stated; excluded regions shown as a function of the parameters left free, for each index or symmetron mass considered; other results converted to the same convention, with the conversion given, before they are plotted together.

**Benchmark.** [1], [2], [3], [4]

## 2. Screening of the source and of the test particle

**Question.** For the parameter values the paper excludes, does it show whether the source mass and the test particle or test body (atom, neutron, pendulum or plate) are screened, by evaluating the thin-shell condition for their actual size and density, and does it treat partial screening where neither limit applies?

**Why it matters.** In a screened theory only a thin outer shell of a dense body sources the scalar force, so the force between two bodies depends on both screening factors, not only on the coupling. A large dense source is strongly screened, which is why small sources inside the vacuum give stronger limits. An atom or ultracold neutron is usually unscreened, but not over all parameter space, and where a test particle is partly screened the effective coupling is reduced.

**Resolved by.** The screening factor of each body computed from its dimensions and density for the excluded parameter range, with the criterion used; a statement of where the test particle is assumed unscreened and a check that this holds; regions where the assumption fails either treated with a calculation that includes partial screening or left out of the excluded region.

**Benchmark.** [1], [2], [5], [6], [7]

## 3. Vacuum chamber, walls and residual gas

**Question.** Does the calculation of the expected signal include the vacuum chamber: its size and shape, the wall material, the residual gas density and composition, and whether the field inside reaches its vacuum minimum or is limited by the chamber size?

**Why it matters.** Inside a chamber the field often cannot reach the value it would take in an infinite vacuum, and instead settles at a value set by the chamber size, which makes the background field and the predicted force depend on the apparatus. The walls also shield the interior from sources outside the vacuum, so a source must sit inside the chamber to produce a signal. In experiments that vary the gas pressure, the predicted signal depends on the gas density at each pressure.

**Resolved by.** Chamber dimensions, wall material, pressure and residual gas stated; the background field computed for the chamber and the regime (vacuum minimum or chamber-limited) identified for the excluded parameters; the source placed inside the vacuum; for pressure-modulated measurements, the gas density at each setting and its effect on the predicted field.

**Benchmark.** [1], [2], [4], [5]

## 4. Shields, membranes and windows between source and detector

**Question.** Where a conducting membrane, foil, window or chamber wall lies between the source and the detector, does the paper compute how much it attenuates the scalar force over the parameter range it excludes?

**Why it matters.** Torsion balances and Casimir-type experiments place a conducting shield between attractor and detector to suppress electrostatic and Casimir backgrounds, and the shield sets the smallest separation that can be reached. A shield that is thick compared with the scalar field's range inside its material develops a thin shell and screens the scalar force as well, with a suppression that grows rapidly with the shield thickness and changes with the model parameters.

**Resolved by.** The thickness and material of every intervening layer given; the attenuation of the scalar force through it calculated as a function of the model parameters and applied to the predicted signal; the part of parameter space in which the shield screens the signal identified and the excluded region cut back accordingly.

**Benchmark.** [1], [2], [3], [8]

## 5. Background forces

**Question.** How are the Newtonian attraction of the source, electrostatic forces from potential differences and surface patch potentials, Casimir or Casimir-Polder forces, and magnetic effects separated from the scalar force, and is each one estimated from a measurement of the actual apparatus?

**Why it matters.** At short range these forces can exceed a scalar force, and some vary with separation in a way close enough to a new force that they are hard to tell apart. In atom interferometers, magnetic or electric field gradients near the source produce a false acceleration through Zeeman or Stark shifts, and microscopic magnetic contamination can rival the forces being sought.

**Resolved by.** The Newtonian force computed from the measured source geometry and density and subtracted, or cancelled by a null geometry; potential differences and patch potentials measured or bounded, with coatings chosen to limit them; a magnetic field survey of the source and a bound on field-gradient shifts; each background listed with its correction and uncertainty.

**Benchmark.** [5], [6], [8]

## 6. Calculation of the predicted signal

**Question.** How was the predicted force, phase or energy shift computed for the actual geometry (thin-shell formulas for spheres, plane-parallel or one-dimensional approximations, the proximity-force approximation for a sphere near a plate, first-order perturbation theory, or a full numerical solution of the non-linear field equation), and is the accuracy of that method stated over the excluded parameter range?

**Why it matters.** The field equation is non-linear, so the signal depends on the full geometry of source, chamber and test region. Analytic approximations can differ from numerical solutions by tens of percent, and by larger factors in strongly non-linear regimes or outside their conditions of validity, such as the sphere-plate approximation at separations comparable to the sphere radius.

**Resolved by.** The method named with its conditions of validity; a numerical solution of the field equation for the real geometry, including the chamber and source shape, or a geometric correction factor derived from one; the difference between approximate and numerical results stated and carried into the excluded region; parameter regions where the method fails marked and not claimed.

**Benchmark.** [3], [4], [6], [7], [9], [10]

## 7. Modulation and the expected signature

**Question.** Does the modulation used to extract the signal (moving the source, changing the separation or orientation, changing the gas pressure, or calibrating at a reference separation) preserve the scalar signal, and does the paper compare the data with the predicted dependence on that modulated parameter?

**Why it matters.** The measured quantity is usually a difference between two configurations, so the relevant prediction is the difference in scalar force between them, not the force in one. A scalar force that is nearly constant over the range of separations can be removed by calibrating at a reference separation, and a reference configuration that carries part of the scalar signal reduces the sensitivity. The dependence on separation or gas pressure is also the main feature that distinguishes a screened scalar force from ordinary backgrounds.

**Resolved by.** The predicted scalar signal in each configuration and their difference computed; a check that the calibration or reference configuration does not remove or share the signal; the data shown against separation, position or pressure with the predicted curve for representative excluded parameters.

**Benchmark.** [1], [4], [6], [10]

## 8. Boundaries of the excluded region

**Question.** Does the paper state every boundary of its excluded region and the cause of each, including where stronger coupling makes the test particle, source or shield screened and removes the signal, and does it confine its claim to the parameter range where its assumptions hold, including the range where quantum corrections to the model's potential remain small?

**Why it matters.** In screened theories a stronger coupling does not always give a larger signal: as the coupling increases, the bodies in the experiment become screened, the signal stops growing with the coupling, and the shape of the excluded region changes there. Symmetron tests are sensitive only to masses near the inverse of the experiment's length scale, so a bound for one symmetron mass does not carry over to others. In parts of parameter space the one-loop corrections to the potential are as large as the classical terms, so the classical calculation of the force no longer describes the model there.

**Resolved by.** The excluded region drawn with each edge attributed to its cause (sensitivity, screening of the source, test particle or shield, chamber size, validity of the calculation); the parameter range of each assumption stated; regions where the assumptions fail left open or analysed separately; where relevant, the region with large quantum corrections marked; symmetron bounds given for each stated mass.

**Benchmark.** [1], [2], [3], [5], [6], [10]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | C. Burrage and J. Sakstein, Tests of chameleon gravity, Living Rev. Relativ. 21, 1 (2018); read as arXiv:1709.09071 | doi:10.1007/s41114-018-0011-x | full text | Sec. 2.1: chameleon potential with index n, scale Lambda and coupling written as M or beta; the dark-energy value of Lambda as a special case. Sec. 3.1: only a thin shell of a screened body sources the force; mapping of bounds to common parameters. Sec. 3.4: the field inside a chamber may not reach its minimum and settles where its mass matches the chamber size; non-spherical geometries need numerical solutions; laboratory tests reach only a narrow range of symmetron masses. Sec. 4.1.1: the membrane between pendulum and attractor may or may not develop a thin shell, complicating the modelling. Sec. 4.1.2: varying gas pressure changes the chameleon force, a possible signature. Sec. 4.3: atoms unscreened over a large part of parameter space. Secs. 5.1 and 6: the n = 1 and n = -4 models tightly constrained, with large regions left for other n when Lambda takes the dark-energy value; some bounds reported only for n = 1 or for one f(R) model |
| 2 | P. Brax, S. Casas, H. Desmond and B. Elder, Testing screened modified gravity, Universe 8, 11 (2021); read as arXiv:2201.10817 | doi:10.3390/universe8010011 | full text | Sec. III.1: a thin electrostatic shielding sheet between the torsion-balance plates attenuates the torque by a factor set by scalar mass and sheet width. Sec. III.2: neutron energy shifts from first-order perturbation theory; a screened neutron has a reduced effective coupling. Sec. III.3: a screened source weakens the force while atoms are typically unscreened; the strongest bounds come from a small source inside the vacuum, since a wall between bodies screens; the chamber size sets the ambient field; numerical 3D solutions for irregular geometries. Sec. III.5: chameleon bounds depend on n and M; symmetron tests are sensitive only near the length scale set by the symmetron mass, and the plotted bounds hold for one mass |
| 3 | A. Upadhye, Dark energy fifth forces in torsion pendulum experiments, Phys. Rev. D 86, 102003 (2012); read as arXiv:1209.0211 | doi:10.1103/PhysRevD.86.102003 | full text | Sec. II.3: a quantum stability condition requires one-loop corrections to stay below the classical potential, and Sec. IV.3 marks the regions that fail it separately from the excluded regions. Sec. III.4: the grounded electrostatic foil also suppresses the chameleon signal, by a factor that grows rapidly with its thickness in units of the Compton wavelength. Sec. IV.2: the one-dimensional plane-parallel approximation underestimates the torque of a 3D calculation by a factor of about 2.5 near beta of one in the current geometry. Sec. IV.3: Lambda fixed to the dark-energy value, constraints shown against beta and n, and vanishing at large n as the force weakens and foil suppression grows |
| 4 | H. Lemmel, Ph. Brax, A. N. Ivanov, T. Jenke, G. Pignol, M. Pitschmann, T. Potocar, M. Wellenzohn, M. Zawisky and H. Abele, Neutron interferometry constrains dark energy chameleon fields, Phys. Lett. B 743, 310–314 (2015); read as arXiv:1502.06023 | doi:10.1016/j.physletb.2015.02.063 | full text | Introduction: neutrons as small test particles that can be unscreened. Sec. III: the chameleon field forms a profile inside an evacuated cell; the cell moved across the beam to map the profile, and helium admitted at four pressures with the highest pressure as phase reference. Sec. IV: analytic one-dimensional vacuum solution, numerical field for finite pressure reduced to a two-dimensional cross-section, and an effective chamber length for the fall of the field near the walls; upper limits on beta for n from 1 to 4, weakening as n increases |
| 5 | C. Burrage, E. J. Copeland and E. A. Hinds, Probing dark energy with atom interferometry, J. Cosmol. Astropart. Phys. 2015(03), 042 (2015); read as arXiv:1408.1409 | doi:10.1088/1475-7516/2015/03/042 | full text | Sec. 3, Eq. 3.2 and Appendices A and E: an atom is unscreened because its nucleus is small; the screening factor falls below one at small coupling scale M, and the Fig. 4 caption ties the flat part of the excluded region to that partial shielding; Sec. 3 notes an earlier neutron analysis revised to include partial screening. Appendix C and Fig. 1: residual gas density and chamber size decide whether the field reaches equilibrium, and otherwise the chamber size sets it. Appendix D: the walls shield the interior from external sources, so the source must be inside the vacuum. Sec. 3: Newtonian gravity of the source included in the total force; Stark, Zeeman and scattered-light effects judged negligible at the first target level, with systematics expected to limit near 10^-9 g |
| 6 | D. O. Sabulsky, I. Dutta, E. A. Hinds, B. Elder, C. Burrage and E. J. Copeland, Experiment to detect dark energy forces using atom interferometry, Phys. Rev. Lett. 123, 061102 (2019); read as arXiv:1812.08244 | doi:10.1103/PhysRevLett.123.061102 | full text | Signal extraction: source moved between two positions so its acceleration changes sign. Systematics: Newtonian attraction subtracted; false acceleration from the source's magnetic field gradient via the second-order Zeeman shift, estimated from a field survey; electric field gradient bounded from an assumed surface charge. Limits: one-dimensional field multiplied by a geometric factor from a full 3D non-linear numerical solution including chamber and source; source screened and atoms unscreened; regions where these assumptions fail handled separately |
| 7 | P. Brax and G. Pignol, Strongly coupled chameleons and the neutronic quantum bouncer, Phys. Rev. Lett. 107, 111301 (2011); read as arXiv:1105.3420 | doi:10.1103/PhysRevLett.107.111301 | full text | Opening and field calculation: macroscopic bodies screen strongly coupled chameleons, while bouncing ultracold neutrons are not screened because their wavefunctions extend micrometres above the mirror; field above the mirror computed from a plate in vacuum. Energy shifts by first-order perturbation theory, with the conditions of validity listed (strong coupling, small field, small chameleon mass times wavefunction scale) |
| 8 | E. G. Adelberger, B. R. Heckel and A. E. Nelson, Tests of the gravitational inverse-square law, Annu. Rev. Nucl. Part. Sci. 53, 77–121 (2003); read as arXiv:hep-ph/0307284 | doi:10.1146/annurev.nucl.53.041002.110503 | full text | Sec. 3.3.1: potential differences and patch fields between surfaces, gold coatings to limit them. Sec. 3.3.2: the Casimir force can exceed gravity at micrometre separations and is hard to distinguish from a new force. Sec. 3.3.3: a conducting membrane between detector and attractor suppresses electrostatic and Casimir backgrounds and limits the smallest separation. Sec. 3.3.4: magnetic contamination can rival gravitational forces. Sec. 3.4: null and partial-null geometries cancel the Newtonian signal |
| 9 | B. Elder, J. Khoury, P. Haslinger, M. Jaffe, H. Müller and P. Hamilton, Chameleon dark energy and atom interferometry, Phys. Rev. D 94, 044051 (2016); read as arXiv:1603.06587 | doi:10.1103/PhysRevD.94.044051 | full text | Sec. 4 and Appendix: full 3D non-linear solution by relaxation for the real chamber and source. Secs. 5.1 and 6: the thin-shell estimate exceeded it by about 20 percent. Sec. 5.2: a spherical chamber in place of the real cylindrical one changed the acceleration by about 18 percent. Secs. 5.3, 5.4 and 7.1: source offsets and a bore changed it by under 1 percent, and a different source shape and material by about 5 percent |
| 10 | P. Brax, C. van de Bruck, A.-C. Davis, D. F. Mota and D. Shaw, Detecting chameleons through Casimir force measurements, Phys. Rev. D 76, 124034 (2007); read as arXiv:0709.2075 | doi:10.1103/PhysRevD.76.124034 | full text | Plate and sphere-plate sections: chameleon pressure has regimes that scale differently with separation from the Casimir pressure; a sizeable force needs thin shells, which requires beta above about 10^3 for the test masses; the sphere-plate approximation fails at the largest separations; static measurements calibrated at a reference separation are insensitive to forces that are nearly constant there |
