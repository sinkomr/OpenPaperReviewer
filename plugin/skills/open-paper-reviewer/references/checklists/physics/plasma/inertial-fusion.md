---
id: CL-INERTIAL-FUSION
name: Claims of inertial-fusion yield and gain
type: claim
field: physics/plasma
applies_when: the paper claims a fusion yield, ignition, a burning plasma, breakeven or energy gain from a laser-driven or pulsed-power inertial-confinement (ICF) or magneto-inertial implosion, or infers such an experiment's ion temperature, hot-spot conditions or alpha heating from fusion products
version: "0.1"
---

# Claims of inertial-fusion yield and gain

## 1. Which input energy the gain is measured against

**Question.** Does the paper state which energy is the denominator of each quoted gain (fusion energy over driver energy delivered to the target, over energy absorbed by the capsule or fuel, over energy stored in the driver, or over electrical energy drawn from the grid), and does it name the gain accordingly?

**Why it matters.** The energy chain from the grid to the fuel loses most of the energy at each step, and in laser-driven implosions the energy absorbed by the fuel can be fifty or more times smaller than the laser energy on target. A gain above one against absorbed or fuel energy is therefore a very different result from a gain above one against driver energy, and neither is an engineering or wall-plug gain.

**Resolved by.** The fusion energy and each input energy given as numbers with uncertainties, each ratio named (for example target gain, fuel gain, scientific gain, engineering gain) and defined in the text; the driver energy measured where it enters the target, with the driver efficiency stated separately if a wider claim about energy is made; no unqualified use of "gain" or "breakeven" in the title or abstract.

**Benchmark.** [1], [2]

## 2. Definition of ignition or a burning plasma

**Question.** Which definition of ignition or of a burning plasma does the paper use, which measured quantities does it compare with that definition, and which model turns the measurements into the quantities the definition needs?

**Why it matters.** The terms have several meanings in use: alpha heating exceeding all losses from the hot spot, alpha heating exceeding the energy delivered to the hot spot from outside, a stated amplification of the yield by alpha heating, or simply fusion energy exceeding driver energy. Hot-spot pressure, confinement time and alpha heating are not measured directly: they are inferred from yield, temperature, areal density and burn duration through simplified models, some calibrated on simulations, and these inferences can be upper bounds.

**Resolved by.** The definition stated, with a reference, and applied consistently in the abstract and the text; the measured inputs (yield, burn-averaged ion temperature, areal density, burn width, hot-spot size) listed with uncertainties; the model and its assumptions stated, with the effect of those assumptions on the conclusion shown; the margin above the threshold given with its uncertainty, not only a statement that it was exceeded.

**Benchmark.** [1], [2], [3]

## 3. Absolute neutron yield

**Question.** How was the absolute fusion yield measured, how is each yield diagnostic calibrated, and do independent diagnostics (for example activation, neutron time-of-flight and charged-particle detectors) agree on the same shots?

**Why it matters.** Neutron time-of-flight detectors give precise relative yields, but their absolute accuracy rests on cross-calibration against an independent absolute measurement, and a chain of cross-calibrations can carry an offset of several per cent for years before an independent check finds it. The reference methods have errors of their own, such as anisotropic emission of the charged particles used for an in situ calibration.

**Resolved by.** Each yield diagnostic named with its calibration route and date; the yield given with an uncertainty that includes the calibration; agreement between at least two independent methods shown for the headline shots; the conversion from neutron yield to fusion energy stated, including the reaction (DD or DT) and any secondary reactions counted; the yield range of the claim shown to lie within the range over which the diagnostics were calibrated.

**Benchmark.** [4], [5]

## 4. Shot-to-shot variation and the conditions of each shot

**Question.** Is the claimed result from one shot or from several, how do repeat shots with the same design compare, and are the shot-specific conditions that change the yield (target quality, fuel age, drive asymmetry, delivered energy) reported for the headline shot and the repeats?

**Why it matters.** Near the ignition threshold the yield is very sensitive to small changes in implosion conditions, so small differences between nominally identical shots can give large differences in yield, and the best shot need not represent the design. Yields also depend on conditions that vary from shot to shot outside the experimenter's control, such as low-mode asymmetry and the time since the tritium fuel was prepared.

**Resolved by.** All shots of the design reported with their yields, not only the best; the spread between repeats shown and the headline claim stated as a property of one shot or of the design, as the data allow; the delivered energy, target metrology, fuel age and measured asymmetry given for each shot; any differences between the headline shot and the repeats named and their effect estimated.

**Benchmark.** [6], [7]

## 5. Comparison with simulations

**Question.** When the yield or gain is compared with simulations, does the paper state the code, its dimensionality, the physics included and omitted, whether the calculation was made before or after the shot, and which inputs or multipliers were adjusted to match the data?

**Why it matters.** Implosion simulations rely on approximations whose accuracy away from the data used to validate them is not well known, and clean one-dimensional calculations omit degradations such as asymmetry and hydrodynamic instabilities, so measured yields are often a fraction of the calculated value. A post-shot simulation tuned to the measured data does not test the physics in the same way as a prediction, and agreement on one observable such as yield can hide disagreement on others.

**Resolved by.** Pre-shot predictions shown alongside post-shot calculations, with the tuned parameters and their values listed; the ratio of measured to calculated yield given and the degradations included stated; several observables (yield, ion temperature, areal density, burn time, shape) compared, not only yield; any calibration of the simulation to earlier experiments described, with its effect on the comparison.

**Benchmark.** [1], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | S. E. Wurzel and S. C. Hsu, Progress toward fusion energy breakeven and gain as measured against the Lawson criterion, Phys. Plasmas 29, 062103 (2022); read as arXiv:2105.10954 | doi:10.1063/5.0083990 |
| 2 | National Research Council, An Assessment of the Prospects for Inertial Fusion Energy (National Academies Press, Washington, DC, 2013) | doi:10.17226/18289 |
| 3 | R. Betti et al., Alpha heating and burning plasmas in inertial confinement fusion, Phys. Rev. Lett. 114, 255003 (2015) | doi:10.1103/PhysRevLett.114.255003 |
| 4 | C. J. Waugh et al., A method for in situ absolute DD yield calibration of neutron time-of-flight detectors on OMEGA using CR-39-based proton detectors, Rev. Sci. Instrum. 86 (2015) | doi:10.1063/1.4919290 |
| 5 | M. J. Moran et al., The NIF 4.5-m nTOF detectors, 19th Topical Conference on High-Temperature Plasma Diagnostics, report LLNL-CONF-557603 (2012) | https://www.osti.gov/biblio/1043655 |
| 6 | A. Lees et al., Experimentally inferred fusion yield dependencies of OMEGA inertial confinement fusion implosions, Phys. Rev. Lett. 127, 105001 (2021) | doi:10.1103/PhysRevLett.127.105001 |
| 7 | A. J. Crilly et al., Fusion alpha particle momentum deposition in thermonuclear burn dynamics, arXiv:2511.06154 (2025) | doi:10.48550/arXiv.2511.06154 |
| 8 | K. D. Humbird et al., Transfer learning to model inertial confinement fusion experiments, arXiv:1812.06055 (2018); journal version with B. K. Spears added as an author, IEEE Trans. Plasma Sci. 48, 61 (2020) | doi:10.48550/arXiv.1812.06055 |
