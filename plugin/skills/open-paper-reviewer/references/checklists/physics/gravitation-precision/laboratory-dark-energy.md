---
id: T-LABORATORY-DARK-ENERGY
name: Laboratory searches for dark energy
type: technique
field: physics/gravitation-precision
applies_when: the paper searches for, or sets limits on, screened scalar fields such as chameleons or symmetrons using atom interferometry, torsion balances, neutron bouncing or interferometry, or Casimir-type force measurements, or quotes, compares or reinterprets an excluded region for such fields
version: "0.1"
---

# Laboratory searches for dark energy

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

| # | Reference | Identifier |
|---|---|---|
| 1 | C. Burrage and J. Sakstein, Tests of chameleon gravity, Living Rev. Relativ. 21, 1 (2018); read as arXiv:1709.09071 | doi:10.1007/s41114-018-0011-x |
| 2 | P. Brax et al., Testing screened modified gravity, Universe 8, 11 (2021); read as arXiv:2201.10817 | doi:10.3390/universe8010011 |
| 3 | A. Upadhye, Dark energy fifth forces in torsion pendulum experiments, Phys. Rev. D 86, 102003 (2012); read as arXiv:1209.0211 | doi:10.1103/PhysRevD.86.102003 |
| 4 | H. Lemmel et al., Neutron interferometry constrains dark energy chameleon fields, Phys. Lett. B 743, 310 (2015); read as arXiv:1502.06023 | doi:10.1016/j.physletb.2015.02.063 |
| 5 | C. Burrage et al., Probing dark energy with atom interferometry, J. Cosmol. Astropart. Phys. 2015(03), 042 (2015); read as arXiv:1408.1409 | doi:10.1088/1475-7516/2015/03/042 |
| 6 | D. O. Sabulsky et al., Experiment to detect dark energy forces using atom interferometry, Phys. Rev. Lett. 123, 061102 (2019); read as arXiv:1812.08244 | doi:10.1103/PhysRevLett.123.061102 |
| 7 | P. Brax and G. Pignol, Strongly coupled chameleons and the neutronic quantum bouncer, Phys. Rev. Lett. 107, 111301 (2011); read as arXiv:1105.3420 | doi:10.1103/PhysRevLett.107.111301 |
| 8 | E. G. Adelberger et al., Tests of the gravitational inverse-square law, Annu. Rev. Nucl. Part. Sci. 53, 77 (2003); read as arXiv:hep-ph/0307284 | doi:10.1146/annurev.nucl.53.041002.110503 |
| 9 | B. Elder et al., Chameleon dark energy and atom interferometry, Phys. Rev. D 94, 044051 (2016); read as arXiv:1603.06587 | doi:10.1103/PhysRevD.94.044051 |
| 10 | P. Brax et al., Detecting chameleons through Casimir force measurements, Phys. Rev. D 76, 124034 (2007); read as arXiv:0709.2075 | doi:10.1103/PhysRevD.76.124034 |
