---
id: T-MW-RESONATOR
name: Microwave resonator measurements
type: technique
field: physics
applies_when: the paper reports a resonance frequency, quality factor, loss tangent or frequency shift of a planar or cavity microwave resonator obtained from network-analyser scattering data, at room or cryogenic temperature, or bases a claim about loss, a material property or a coupling on such values
version: "0.1"
---

# Microwave resonator measurements

Resonance frequencies and quality factors extracted from the scattering parameters of a planar or cavity resonator are used to claim low microwave loss, to assign loss to a material, interface or mechanism, and to derive material quantities (loss tangent, permittivity, surface impedance, kinetic inductance) or couplings from frequency shifts. None of these is measured directly: each comes from a fit of a line shape recorded through cables, amplifiers and a sample holder.

## 1. Which quality factor is reported

**Question.** Does the paper state whether each quality factor is loaded, coupling (external) or internal, how the resonator was coupled and measured (side-coupled to a feedline, inline transmission, or reflection), and how the coupling quality factor compares with the internal one?

**Why it matters.** The linewidth gives only the loaded quality factor; dividing it into coupling and internal parts needs an absolute reference for the size of the resonance, which an inline transmission measurement lacks unless the lines are calibrated. When coupling loss is much larger than internal loss the line shape is set by the coupling and the internal value is poorly determined, and when it is much smaller the signal is weak.

**Resolved by.** Every quality factor is labelled, the measurement configuration is given, coupling values are reported next to internal ones, and internal values are taken from resonators whose coupling and internal quality factors are of the same order, or the larger uncertainty outside that regime is stated.

**Benchmark.** [1], [2], [4]

## 2. Line-shape model and fit

**Question.** Is the fitting model given, does it use the complex scattering data rather than the magnitude alone, does it account for an asymmetric line shape, and are example fits and parameter uncertainties shown?

**Why it matters.** Impedance mismatch near the resonator rotates the resonance circle and makes the line shape asymmetric; a model that only adds a rotation overestimates the internal quality factor, by an amount that grows with the asymmetry and with the coupling strength. Magnitude-only fits are less accurate than vector fits except for very noisy data, and every method degrades sharply at low signal-to-noise ratio, which is the condition of low-power measurements.

**Resolved by.** The model equation or a named method (for example a circle fit with diameter correction) is given, fits are shown in the complex plane as well as in magnitude, the asymmetry angle and statistical uncertainties are reported, and the signal-to-noise ratio of the lowest-power traces is stated or evident from the data shown.

**Benchmark.** [1], [2], [3], [5]

## 3. Background, cable delay and stray paths

**Question.** Does the paper say how the off-resonance background was handled (cable delay, gain and attenuation, baseline ripple, neighbouring modes), at what temperature the lines were calibrated, and whether a signal path that bypasses the resonator could contribute?

**Why it matters.** The measured response is the resonator response scaled and rotated by the lines and added to any leakage or crosstalk. Interference between the resonant signal and a background path shifts the extracted internal quality factor systematically, even when the line shape looks symmetric and more strongly for overcoupled resonators, and it can produce apparent trends when the resonance is tuned in frequency. A calibration made at room temperature does not remove mismatches that appear on cooling, and the choice of normalisation changes the fitted values.

**Resolved by.** The normalisation procedure is described well enough to be repeated, raw data over a span wider than the resonance are shown, and either the leakage is characterised in situ or a systematic uncertainty range for the internal quality factor is derived from a bound on its amplitude; where the geometry requires it, calibration at the measurement temperature is described.

**Benchmark.** [1], [2], [4], [5], [6]

## 4. Power in the resonator and linearity

**Question.** Is the power at the resonator, or the mean photon number, given together with how it was estimated, and is the response shown to be linear over the range that was fitted?

**Why it matters.** Loss in superconducting resonators depends on the circulating power, so quality factors can be compared only at a stated power, and the power at the device is hard to know because it rests on the attenuation of the cold lines and is altered by reflections. At strong drive the resonance becomes asymmetric and hysteretic through kinetic-inductance nonlinearity, heating, weak links or vortex penetration, and a linear line-shape model no longer describes the data.

**Resolved by.** The photon-number estimate and the line attenuation behind it are given with an uncertainty, a power sweep is shown that reaches the regime the claim concerns (down to the single-photon level where that is what is claimed), and the fitted traces are shown or stated to be free of distortion and of dependence on sweep direction.

**Benchmark.** [1], [7]

## 5. Sample temperature and shielding

**Question.** Are the sample temperature, the thermal anchoring of the sample, and the magnetic and infrared shielding described, with evidence that the sample reached the quoted temperature?

**Why it matters.** A sample that stays warmer than the refrigerator stage shows less two-level-system loss than it would at the quoted temperature, so the loss is under-reported. Stray infrared radiation from warmer stages creates quasiparticles that limit the quality factor, and magnetic flux trapped on cooling through the transition in a residual field adds both loss and a frequency shift.

**Resolved by.** The mounting and thermalisation are described, the shielding is specified (magnetic shield, light-tight or absorber-coated enclosure, filtered lines), and a temperature sweep down to base temperature shows the behaviour expected if the sample follows the thermometer.

**Benchmark.** [1], [8]

## 6. Assigning loss or a frequency shift to one mechanism

**Question.** When a loss or a frequency shift is attributed to a single mechanism (two-level systems, quasiparticles, vortices, radiation, a coupled sample), is the attribution supported by the measured dependence on power, temperature, field or geometry, with the other contributions bounded?

**Why it matters.** Measured loss is a sum of power-dependent and power-independent channels, so a single low-power value is not the two-level-system loss when radiation, vortex, parasitic-mode or residual quasiparticle losses are comparable to it. With rising temperature, two-level systems and thermal quasiparticles move the frequency in opposite directions, and a single-mechanism fit to data that contain both returns unphysical parameters; drive power shifts the frequency as well.

**Resolved by.** Power and temperature sweeps are both shown and fitted with consistent parameters, loss and frequency shift are analysed together, and the competing mechanisms are either measured separately or bounded.

**Benchmark.** [1], [7]

## 7. From quality factor and frequency to a material property

**Question.** When a material quantity (loss tangent, permittivity, surface resistance, penetration depth, conductivity) is derived, is the electromagnetic model of the resonator given, including the fraction of the stored energy that resides in the material of interest and the losses of the rest of the structure?

**Why it matters.** The measured quality factor includes parasitic losses in walls, conductors and the rest of the fixture; these set the smallest loss tangent that can be resolved and must be small and calculable. Converting frequency and quality factor into material parameters needs a field solution for the actual structure, and if the material of interest holds only a small fraction of the energy the result is sensitive to every other loss channel.

**Resolved by.** The analytic or numerical model is stated, filling (participation) factors and geometric factors are reported, and the parasitic losses are computed or measured with a reference configuration and shown to be small compared with the loss assigned to the material.

**Benchmark.** [1], [9]

## 8. Variability and reporting

**Question.** On how many resonators, chips and cooldowns does each conclusion rest, and are the spread, the variation in time, and the conditions needed for comparison (temperature, coupling quality factor, power, fit method, filling factor) reported?

**Why it matters.** Nominally identical resonators on one chip can differ in internal quality factor by up to an order of magnitude, the same resonator can differ between cooldowns, and loss fluctuates in time. A difference between two materials or processes that rests on one resonator each may therefore lie within the spread.

**Resolved by.** Several resonators per condition and repeated cooldowns are reported with distributions or ranges, the variation in time is characterised or averaged over a stated period, and the conditions listed in the question are tabulated.

**Benchmark.** [1]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | C. R. H. McRae, H. Wang, J. Gao, M. R. Vissers, T. Brecht, A. Dunsworth, D. P. Pappas and J. Mutus, Materials loss measurements using superconducting microwave resonators, Rev. Sci. Instrum. 91, 091101 (2020); arXiv:2006.04718 | doi:10.1063/5.0017378 | full text | Read in the arXiv version; sections cited by title. "Measurement mode and fitting", "Resonator coupling": inline transmission cannot separate cable loss from resonator loss; a rotation-only fit overestimates internal Q; the normalisation should be traceable; coupling Q should be close to internal Q. "Impedance matching and calibration", "Power and temperature sweeps", "Total loss" (Fig. 6): a room-temperature calibration is only assumed to hold when cold; power at the device is hard to determine; loss is a sum of power-dependent and power-independent channels; two-level-system and quasiparticle frequency shifts have opposite sign. "Temperature and thermalization", "Vortex loss": poor thermalisation under-reports loss; flux trapped on cooling adds loss and a frequency shift. "Filling factor", "Measurement variability", "Conclusions and outlook": the energy fraction in the material of interest must be known; Q varies between nominally identical resonators, between cooldowns and in time; list of quantities to report. |
| 2 | S. Probst, F. B. Song, P. A. Bushev, A. V. Ustinov and M. Weides, Efficient and robust analysis of complex scattering data under noise in microwave resonators, Rev. Sci. Instrum. 86, 024706 (2015); arXiv:1410.3365 | doi:10.1063/1.4907935 | full text | Sec. I: loaded Q combines internal and coupling terms, and an uncalibrated inline transmission trace lacks the baseline needed to separate them. Sec. III: amplitude, phase offset and cable delay of the environment have to be removed before the circle fit. Secs. IV and V (Fig. 4): parameter errors from the fit covariance; fitted values are stable only above a signal-to-noise ratio of a few tens. |
| 3 | M. S. Khalil, M. J. A. Stoutimore, F. C. Wellstood and K. D. Osborn, An analysis method for asymmetric resonator transmission applied to superconducting devices, J. Appl. Phys. 111, 054510 (2012); arXiv:1108.3117 | doi:10.1063/1.3692073 | full text | Sec. II (Eqs. 15 to 17) and Sec. IV: mismatched lines make the line shape asymmetric; a rotation-only analysis overestimates internal Q, with an error that grows with asymmetry and with coupling and can even give negative values; the diameter correction removes it. |
| 4 | D. Rieger, S. Günzler, M. Spiecker, A. Nambisan, W. Wernsdorfer and I. M. Pop, Fano interference in microwave resonator measurements, Phys. Rev. Applied 20, 014059 (2023); arXiv:2209.03036 | doi:10.1103/PhysRevApplied.20.014059 | full text | Secs. II, IV (Fig. 4), V and VI: a background path interfering with the resonant signal gives a systematic uncertainty in internal Q of a few per cent at critical coupling, rising steeply for overcoupled resonators; it is present even for symmetric line shapes and can mimic trends in frequency sweeps; a range derived from a bound on the leakage, or in-situ characterisation of the leakage, is proposed. |
| 5 | P. J. Petersan and S. M. Anlage, Measurement of resonant frequency and quality factor of microwave resonators: Comparison of methods, J. Appl. Phys. 84, 3392–3402 (1998); arXiv:cond-mat/9805365 | doi:10.1063/1.368498 | full text | Sec. II: crosstalk, a reference plane displaced from the coupling ports, and nearby resonances distort the resonance circle. Secs. V and VII: a magnitude-only Lorentzian fit is less accurate than vector methods except for very noisy data, vector data allow crosstalk and delay to be corrected, and all seven methods compared degrade sharply below a signal-to-noise ratio of about 10. |
| 6 | H. Wang, S. Singh, C. R. H. McRae, J. C. Bardin, S.-X. Lin, N. Messaoudi, A. R. Castelli, Y. J. Rosen, E. T. Holland, D. P. Pappas and J. Y. Mutus, Cryogenic single-port calibration for superconducting microwave resonator measurements, Quantum Sci. Technol. 6, 035015 (2021); arXiv:2103.01491 | doi:10.1088/2058-9565/ac070e | abstract | Abstract: in reflection measurements, impedance mismatches in the cryogenic chain have to be accounted for by calibrating the chain while it is cold. |
| 7 | L. J. Swenson, P. K. Day, B. H. Eom, H. G. Leduc, N. Llombart, C. M. McKenney, O. Noroozian and J. Zmuidzinas, Operation of a titanium nitride superconducting microresonator detector in the nonlinear regime, J. Appl. Phys. 113, 104501 (2013); arXiv:1305.4281 | doi:10.1063/1.4794808 | full text | Abstract and Sec. II (Figs. 3 and 5): strong drive makes the response nonlinear and bifurcating, through heating, weak links, vortex penetration or kinetic-inductance nonlinearity; the resonance shifts to lower frequency, becomes asymmetric and depends on sweep direction, so the linear transfer function has to be replaced. |
| 8 | R. Barends, J. Wenner, M. Lenander, et al., Minimizing quasiparticle generation from stray infrared light in superconducting quantum circuits, Appl. Phys. Lett. 99, 113507 (2011); arXiv:1105.4642 | doi:10.1063/1.3638063 | full text | Read in the arXiv version, which carries an earlier title. Abstract, Fig. 1 and the accompanying text: infrared light from the 4 K stage generates quasiparticles that limit resonator Q for a sample shielded only by a metal box; adding an absorber-coated shield at the sample temperature raised Q by an order of magnitude or more. |
| 9 | J. Krupka, Microwave measurements of electromagnetic properties of materials, Materials 14, 5097 (2021) | doi:10.3390/ma14175097 | full text | Sec. 3.2: resonance frequency and Q are converted to complex permittivity through a solution of Maxwell's equations for the fixture, and wall losses have to be computed separately. Secs. 4 and 7: the electric-energy filling factor and the parasitic losses of the cell determine the loss-tangent resolution; parasitic losses must be small and calculable, and rigorous results need numerical modelling of the cell with the sample. |
