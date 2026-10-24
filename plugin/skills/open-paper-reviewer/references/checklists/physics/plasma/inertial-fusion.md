---
id: CL-INERTIAL-FUSION
name: Claims of inertial-fusion yield and gain
type: claim
field: physics/plasma
applies_when: the paper claims a fusion yield, ignition, a burning plasma, breakeven or energy gain from a laser-driven, pulsed-power, Z-pinch, plasma-focus or other inertial-confinement (ICF) or magneto-inertial experiment, or infers such an experiment's ion temperature, hot-spot conditions or alpha heating from fusion products
version: "0.1"
---

# Claims of inertial-fusion yield and gain

A claim of this kind asserts that an inertial-confinement fusion (ICF) or magneto-inertial fusion (MIF) experiment, driven by lasers, pulsed power or another driver, released a stated fusion energy, reached ignition or a burning plasma (one heated mainly by its own fusion products, the alpha particles in deuterium-tritium (DT) fuel), or gave a stated energy gain. A careful demonstration states which input energy the gain is measured against, measures the yield and ion temperature with calibrated nuclear diagnostics, shows the neutrons are thermonuclear, and compares the result with repeat shots and with simulations on equal terms.

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

## 4. Ion temperature from neutron spectra

**Question.** How is the ion temperature obtained, and does the paper treat the width of the neutron spectrum as a thermal temperature, or does it account for bulk and residual flows and compare several lines of sight and reactions?

**Why it matters.** The ion temperature in these experiments is usually inferred from the width of the fusion-neutron spectrum, which equals the thermal temperature only for a stationary Maxwellian plasma. A spread of fluid velocities in the burning region adds to the width and inflates the inferred temperature, and directed flows shift and broaden the spectrum differently along different lines of sight. The value is also burn-averaged, weighted towards the hottest, densest parts of the plasma.

**Resolved by.** The temperature called an apparent or spectral temperature where flows are not removed; values from several lines of sight given, with their spread and with the mean-energy shifts; DD and DT temperatures compared where both are measured; the claim checked against the lowest line-of-sight value, or with a stated correction for flows and its uncertainty.

**Benchmark.** [1], [6]

## 5. Thermonuclear or non-thermal origin of the neutrons

**Question.** Does the paper show that the measured fusion products come from a thermal plasma, and not from ions accelerated by electric fields, instabilities or the driver striking cold material (beam-target reactions), before it uses the yield to claim thermonuclear conditions?

**Why it matters.** Beam-target reactions can give large neutron yields from a plasma that is far from thermonuclear conditions, and early pinch experiments that were first read as thermonuclear were later found to be dominated by them. In pinch and plasma-focus devices the yield commonly mixes non-Maxwellian and thermal ion populations, so a thermal temperature cannot be read from it. Isotropy is not by itself proof of a thermal origin, since magnetised beam ions can also give isotropic emission.

**Resolved by.** Neutron spectra measured at two or more angles to the axis of the device, with the energy shift between them used to bound any beam energy; the spectral shape, not only the yield, compared with thermonuclear and beam-target predictions; gamma and scattered-neutron backgrounds in the spectral detectors measured and their effect on the fit stated; any non-thermal contribution bounded, with its uncertainty, before a temperature or triple product is quoted.

**Benchmark.** [1], [7], [8]

## 6. Shot-to-shot variation and the conditions of each shot

**Question.** Is the claimed result from one shot or from several, how do repeat shots with the same design compare, and are the shot-specific conditions that change the yield (target quality, fuel age, drive asymmetry, delivered energy) reported for the headline shot and the repeats?

**Why it matters.** Near the ignition threshold the yield is very sensitive to small changes in implosion conditions, so small differences between nominally identical shots can give large differences in yield, and the best shot need not represent the design. Yields also depend on conditions that vary from shot to shot outside the experimenter's control, such as low-mode asymmetry and the time since the tritium fuel was prepared.

**Resolved by.** All shots of the design reported with their yields, not only the best; the spread between repeats shown and the headline claim stated as a property of one shot or of the design, as the data allow; the delivered energy, target metrology, fuel age and measured asymmetry given for each shot; any differences between the headline shot and the repeats named and their effect estimated.

**Benchmark.** [9], [10]

## 7. Comparison with simulations

**Question.** When the yield or gain is compared with simulations, does the paper state the code, its dimensionality, the physics included and omitted, whether the calculation was made before or after the shot, and which inputs or multipliers were adjusted to match the data?

**Why it matters.** Implosion simulations rely on approximations whose accuracy away from the data used to validate them is not well known, and clean one-dimensional calculations omit degradations such as asymmetry and hydrodynamic instabilities, so measured yields are often a fraction of the calculated value. A post-shot simulation tuned to the measured data does not test the physics in the same way as a prediction, and agreement on one observable such as yield can hide disagreement on others.

**Resolved by.** Pre-shot predictions shown alongside post-shot calculations, with the tuned parameters and their values listed; the ratio of measured to calculated yield given and the degradations included stated; several observables (yield, ion temperature, areal density, burn time, shape) compared, not only yield; any calibration of the simulation to earlier experiments described, with its effect on the comparison.

**Benchmark.** [1], [11]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | S. E. Wurzel and S. C. Hsu, Progress toward fusion energy breakeven and gain as measured against the Lawson criterion, Phys. Plasmas 29, 062103 (2022); read as arXiv:2105.10954 | doi:10.1063/5.0083990 | full text | Secs. III.4, III.6 and III.8: fuel gain, scientific gain (the same as ICF target gain, against laser energy on target), engineering and wall-plug gain defined against different input energies; a chain from laser to absorbed shell energy to hot-spot energy with absorption fractions of order 0.06 to 0.009. Sec. III.6: ignition has many meanings in ICF. Secs. IV.2.1 and IV.2.2: confinement and pressure inferred from areal density, temperature and burn width through models using a yield-over-clean factor from simulation databases, results treated as upper bounds; ion temperature is burn-averaged from neutron time of flight. Sec. IV.2.4: absorbed and external energy differ by a factor of 50 or more in ICF. Sec. IV.3.2: dense plasma focus yields come from non-Maxwellian and thermal ion populations together, so thermal temperatures are not well characterised; early Z-pinch neutrons were attributed to beam-target reactions driven by instabilities |
| 2 | National Research Council, An Assessment of the Prospects for Inertial Fusion Energy (National Academies Press, Washington, DC, 2013) | doi:10.17226/18289 | full text | Appendix A: ignition defined as alpha heating of the hot spot exceeding all losses; target gain as fusion energy over driver energy; engineering gain depends on driver efficiency and target gain, with the target gain needed rising as driver efficiency falls. Appendix G (glossary): a second meaning of ignition for fusion energy, fusion gain exceeding unity; wall-plug efficiency defined separately |
| 3 | R. Betti, A. R. Christopherson, B. K. Spears, R. Nora, A. Bose, J. Howard, K. M. Woo, M. J. Edwards and J. Sanz, Alpha heating and burning plasmas in inertial confinement fusion, Phys. Rev. Lett. 114, 255003 (2015) | doi:10.1103/PhysRevLett.114.255003 | abstract | Abstract: a burning plasma defined by alpha heating exceeding the external energy delivered to the plasma; a simplified implosion model relates this regime to the yield amplification from alpha heating and to measurable quantities such as the Lawson parameter |
| 4 | C. J. Waugh, M. J. Rosenberg, A. B. Zylstra, J. A. Frenje, F. H. Séguin, R. D. Petrasso, V. Yu. Glebov, T. C. Sangster and C. Stoeckl, A method for in situ absolute DD yield calibration of neutron time-of-flight detectors on OMEGA using CR-39-based proton detectors, Rev. Sci. Instrum. 86 (2015) | doi:10.1063/1.4919290 | abstract | Abstract (OSTI record 1182631): time-of-flight yield calibration traced to activation systems cross-calibrated decades earlier; an independent in situ check against proton yields gave a coefficient 1.09 ± 0.02 relative to the previous one; charged-particle anisotropy from field effects was the main calibration error |
| 5 | M. J. Moran, E. J. Bond, T. J. Clancy, M. J. Eckart, H. Y. Khater and V. Y. Glebov, The NIF 4.5-m nTOF detectors, 19th Topical Conference on High-Temperature Plasma Diagnostics, report LLNL-CONF-557603 (2012) | https://www.osti.gov/biblio/1043655 | abstract | Abstract: time-of-flight detectors measured DD and DT yields over about six decades with DT precision better than 5%, but absolute accuracy depends on cross-calibration with independent absolute yield measurements; analysis improved through better characterisation of detector impulse response |
| 6 | A. J. Crilly, B. D. Appelbe, O. M. Mannion, W. Taitano, E. P. Hartouni, A. S. Moore, M. Gatu-Johnson and J. P. Chittenden, Constraints on ion velocity distributions from fusion product spectroscopy, Nucl. Fusion 62 (2022); read as arXiv:2205.04763 | doi:10.1088/1741-4326/ac90d5 | full text | Secs. I and II: ion temperature inferred from spectral width through Brysk's formulae, a thermodynamic temperature only for a stationary Maxwellian. Sec. III.2: fluid velocity variance adds to the width and inflates any measured spectral temperature; its isotropic part cannot be removed. Secs. III.1.2 and III.2: mean energy and width depend on emission direction, and the anisotropic flow part can be extracted given enough lines of sight. Appendix A: DD and DT have reaction-specific limits |
| 7 | R. A. Ryan, P. E. Tsai, A. R. Johansen, A. Youmans, D. P. Higginson, J. M. Mitrani, C. S. Adams, D. A. Sutherland, B. Levitt and U. Shumlak, Time-resolved measurement of neutron energy isotropy in a sheared-flow-stabilized Z pinch, arXiv:2408.05171 (2024) | doi:10.48550/arXiv.2408.05171 | full text | Sec. 1: early pinch neutrons were found to come mainly from beam-target fusion linked to an instability, so beam-target contributions must be measured to interpret the yield. Secs. 2, 2.1 and 2.5: neutron energy spectra at two angles to the pinch axis are compared and the shift fitted with simulated spectra to bound the deuteron beam energy; detectors placed to limit scattering. Abstract: gamma backgrounds measured and their effect on the isotropy result assessed |
| 8 | B. Appelbe and J. Chittenden, Neutron spectra from beam-target reactions in dense Z-pinches, Phys. Plasmas 22, 102703 (2015) | doi:10.1063/1.4933117 | abstract | Abstract (Imperial College Spiral record 10044/1/33085): instabilities accelerate ions that produce beam-target neutrons; the spectra depend on the fields at stagnation and differ between devices; magnetised beam ions can give isotropic emission; beam-target spectra can peak below the thermonuclear energy and differ in shape |
| 9 | A. Lees, R. Betti, J. P. Knauer, V. Gopalaswamy, D. Patel, K. M. Woo, K. S. Anderson, E. M. Campbell, D. Cao et al., Experimentally inferred fusion yield dependencies of OMEGA inertial confinement fusion implosions, Phys. Rev. Lett. 127, 105001 (2021) | doi:10.1103/PhysRevLett.127.105001 | abstract | Abstract: statistical analysis of experiments and simulations finds yield reduced by the beam-to-target radius ratio, by ion-temperature asymmetry from the l = 1 mode, by the time since tritium production and by stability parameters |
| 10 | A. J. Crilly, B. D. Appelbe, E. A. Ferdinandi, S. T. O'Neill, H. Biragnet, N. Chaturvedi, J. P. Chittenden, B. Duhig and P. W. Moloney, Fusion alpha particle momentum deposition in thermonuclear burn dynamics, arXiv:2511.06154 (2025) | doi:10.48550/arXiv.2511.06154 | full text | Paragraph after Eq. (5) on the ignition velocity: the ignition cliff is where the yield is most sensitive to implosion parameters. Paragraph on the baseline design: for designs on the cliff, a shift of a few tens of km/s in the threshold velocity gives a large change in yield |
| 11 | K. D. Humbird, J. L. Peterson and R. G. McClarren, Transfer learning to model inertial confinement fusion experiments, arXiv:1812.06055 (2018); journal version with B. K. Spears added as an author, IEEE Trans. Plasma Sci. 48, 61 (2020) | doi:10.48550/arXiv.1812.06055 | full text | Abstract and Sec. I: ICF simulations must be calibrated to predict experiments, and their accuracy away from validation data is not well known. Sec. III: high-fidelity simulations are not necessarily more predictive than low-fidelity ones and are not an accurate picture of reality (Table VI caption); yield predictions had to be shifted by more than an order of magnitude for most experiments. Sec. IV: hydrodynamic instabilities, asymmetries and other degradations not included in one-dimensional simulations |
