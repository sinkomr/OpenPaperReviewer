---
id: T-SAMPLE-ENVIRONMENT
name: Sample environment control
type: technique
field: physics/methods
applies_when: the paper bases a claim on the magnetic field, pressure, strain, electric field or atmosphere at the sample, on hysteresis between sweep directions in temperature, field or gate voltage, on field-cooled and zero-field-cooled comparisons, or on data from a pressure or strain cell
version: "0.1"
---

# Sample environment control

Sample environments are used to claim that a property was measured under stated conditions of temperature, magnetic field, electric field, pressure, strain or atmosphere, and to claim how the property depends on those conditions, including hysteresis and dependence on history such as field-cooled (FC) and zero-field-cooled (ZFC) protocols. Each such claim assumes that the conditions at the sample are the ones set or read at the instrument, for example in a superconducting magnet, a piston-cylinder cell, a diamond anvil cell (DAC) or a piezoelectric strain cell.

## 1. Magnetic field at the sample

**Question.** How was the magnetic field at the sample determined, and was the remanent field of the magnet measured or corrected, in particular for data at low fields, near zero field or on hysteresis loops?

**Why it matters.** Many magnetometers and cryostats with superconducting magnets have no field sensor at the sample, so the quoted field is inferred from the magnet current. Flux pinned in the windings leaves a trapped field of up to tens of oersted, opposite to the last large field, so the real field near nominal zero differs from the set value. Plotted against the nominal field, this can invert hysteresis loops or make a non-magnetic sample appear to have a coercive field.

**Resolved by.** The way the field was set and measured stated, including whether the magnet was reset before low-field data; the remanent field measured with a paramagnetic reference or a field sensor at the sample position, under the same field history as the data; low-field data and coercive fields corrected for it, or shown to be much larger than it.

**Benchmark.** [1]

## 2. History and cooling protocol

**Question.** For each data set, does the paper state the full thermal and field history (the field applied while cooling, the temperature from which the sample was cooled, the order of field changes, and any reset between runs), and are field-cooled and zero-field-cooled curves taken with stated and comparable protocols?

**Why it matters.** Where the response depends on history, the same nominal temperature and field can give different results after different paths, and the difference is easily read as a physical effect. A nominal zero-field cool takes place in whatever field the magnet has trapped from its last large field. Near a hysteretic first-order transition, quantities derived from isothermal data depend on whether the sample was returned to a reference state before each measurement.

**Resolved by.** The protocol for each curve given in the text or caption: cooling field, starting temperature, sweep direction and rate, waiting times and the residual field during a nominal zero-field cool; where history matters, each measurement started from a stated reference state, such as warming above the transition between isotherms; the comparison between protocols shown with both curves on the same axes.

**Benchmark.** [1], [2]

## 3. Sweep direction, rate and apparent hysteresis

**Question.** For temperature, field or gate-voltage sweeps, are the sweep direction, range and rate stated, are both directions shown, and does the paper show how any hysteresis or drift depends on the sweep rate and on the time spent at each point?

**Why it matters.** A difference between up and down sweeps can come from the apparatus rather than the sample: in a temperature sweep the sample lags the thermometer by its thermal time constant times the sweep rate, so warming and cooling curves separate even for a transition without hysteresis; field drift from flux creep continues for hours after a field change; and charge trapping in a gate insulator shifts the threshold between forward and reverse sweeps. Real hysteresis at a first-order transition can also widen with sweep rate, so a width quoted at one rate does not by itself characterise the sample.

**Resolved by.** Sweep direction, range, rate and settling times stated for each data set; both sweep directions shown; hysteresis measured at several rates or with waits at fixed values, and quasistatic values obtained from the rate dependence; for temperature sweeps, a reference with a transition known to have no hysteresis measured in the same setup at the same rates; for gated devices, the bias history before the sweep stated.

**Benchmark.** [1], [3], [9]

## 4. Pressure at the measurement temperature

**Question.** How was the pressure at the sample determined at the temperature of each measurement, and is it a value measured in situ at low temperature rather than the pressure set at room temperature or inferred from the applied load?

**Why it matters.** Pressure estimated from force and area is uncertain because of friction and dimensional changes. In a piston-cylinder cell the pressure falls continuously on cooling, with a steeper drop where the pressure medium solidifies, by a few tenths of a gigapascal between room temperature and a few kelvin; at low loads it can fall to zero. Pressure in a DAC can also change on cooling, by tens of per cent at low pressure with some media. A gauge read at one temperature fixes the pressure only there.

**Resolved by.** The manometer named and located with the sample, such as the superconducting transition of lead, a manganin coil or ruby fluorescence; pressure measured at or near the temperatures of the claims, or a calibrated pressure-temperature curve for that cell, medium and filling used to assign it; the uncertainty of the pressure stated and carried into any phase boundary or pressure coefficient.

**Benchmark.** [4], [5]

## 5. Pressure medium and hydrostatic conditions

**Question.** Which pressure-transmitting medium was used, does it stay liquid or hydrostatic over the pressures and temperatures of the claims, and does the paper show how uniform the pressure is across the sample?

**Why it matters.** Every liquid medium solidifies above a pressure that falls as temperature falls, and a solid medium transmits shear stress, so the sample sees pressure gradients and uniaxial stress. Media differ widely: some solidify at about 1 to 2.5 GPa even at room temperature, while helium, nitrogen and argon stay close to hydrostatic to about 10 GPa at low temperature. Solidification of the medium can itself produce anomalies in the measured property of the sample.

**Resolved by.** The medium named with its known solidification line or hydrostatic limit, and the claims placed relative to it; the uniformity checked, for example by the width of the ruby fluorescence line at the temperature of the measurement; features that coincide with solidification of the medium identified and not attributed to the sample; where possible, key results repeated with a more hydrostatic medium.

**Benchmark.** [4], [5], [6]

## 6. Strain transmitted to the sample

**Question.** How was the strain in the sample determined, as distinct from the displacement or voltage applied by the strain device, and how were the strain-free point and the uniformity of strain across the measured region established?

**Why it matters.** Applied displacement reaches the sample through epoxy or another bond that deforms, so the strain in the sample is less than the nominal value from the displacement and sample length. Strain is not uniform near the bonded ends, an asymmetric mount bends the sample, and long thin samples can buckle. Differential thermal contraction between sample and device adds strain on cooling, so zero applied voltage is not zero strain.

**Resolved by.** A displacement or strain sensor read at the measurement temperature, with its calibration and any shift between cool-downs stated; the transfer through the bond estimated or measured; the strain-free point located with its uncertainty; the measured region kept away from the bonded ends and the mounting described, including sample dimensions, bond thickness and symmetry.

**Benchmark.** [7]

## 7. Atmosphere and exposure

**Question.** In what atmosphere was the sample stored, mounted and measured (vacuum, inert gas, exchange gas or air, with humidity where relevant), how long was it exposed to air, and does the paper separate effects of the atmosphere from the effect it claims?

**Why it matters.** Species adsorbed on unprotected surfaces add charge traps and can change the properties being measured, and degradation driven by the ambient can be confused with the response to other stresses such as light, bias or temperature. Without the atmosphere and exposure history, another laboratory cannot reproduce the conditions.

**Resolved by.** The atmosphere, pressure of any exchange gas, humidity and illumination stated for storage, preparation and measurement, with the time between preparation and measurement; key results repeated in a controlled atmosphere or after encapsulation; drifts with time shown and assigned either to the sample or to the environment.

**Benchmark.** [3], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. Sawicki, W. Stefanowicz and A. Ney, Sensitive SQUID magnetometry for studying nanomagnetism, Semicond. Sci. Technol. 26, 064006 (2011); read as preprint arXiv:1101.4764 | doi:10.1088/0268-1242/26/6/064006 | full text | Secs. II.3.1 and II.3.2: no absolute field sensor, so the field follows from the power-supply current; flux pinned in the magnet leaves a trapped field opposite to the last large field, up to about 30 Oe in a 7 T magnet, which inverts loops and can make a diamagnetic substrate look ferromagnetic; remanent field calibrated with a paramagnetic Dy2O3 or Pd reference; a magnet reset helps only near zero field. Sec. II.3.3 and Fig. 8: field drift from flux creep and escape recorded over about 3 hours at a set field of 1 kOe, with a trapped field of about -15 Oe when 1 kOe is approached from 10 kOe without a reset, and drift about ten times smaller after a reset. Sec. III and Fig. 13: FC and ZFC curves with the sweep protocol stated |
| 2 | A. Quintana-Nedelcos, J. L. Sánchez Llamazares, C. F. Sánchez-Valdés, P. Álvarez Alonso, P. Gorria, P. Shamba and N. A. Morley, On the correct estimation of the magnetic entropy change across the magneto-structural transition from the Maxwell relation: Study of MnCoGeBx alloy ribbons, J. Alloys Compd. 694, 1189–1195 (2017) | doi:10.1016/j.jallcom.2016.10.116 | abstract | Abstract: two thermal procedures for measuring isothermal magnetisation at a first-order transition are compared; reliable values need the thermal and magnetic history taken into account, by measuring each isotherm in one direction after a thermal cycle |
| 3 | Y. Yu. Illarionov, T. Knobloch, M. Jech, M. Lanza, D. Akinwande, M. I. Vexler, T. Mueller, M. C. Lemme, G. Fiori, F. Schwierz and T. Grasser, Insulators for 2D nanoelectronics: the gap to bridge, Nat. Commun. 11, 3385 (2020) | doi:10.1038/s41467-020-16640-8 | full text | Section on border traps and device stability with Fig. 5: hysteresis and bias-temperature instability share an origin in charge trapping in border traps, giving different thresholds in forward and reverse sweeps; trap time constants depend on gate bias, and the hysteresis width changes with sweep speed. Box 2: trap time constants are thermally activated. Section on interface quality and device performance: adsorbates on unprotected channels contribute to interface trap density |
| 4 | L. Xiang, E. Gati, S. L. Bud'ko, R. A. Ribeiro, A. Ata, U. Tutsch, M. Lang and P. C. Canfield, Characterization of the pressure coefficient of manganin and temperature evolution of pressure in piston-cylinder cells, Rev. Sci. Instrum. 91, 095103 (2020); read as preprint arXiv:2007.11703 | doi:10.1063/5.0022650 | full text | Introduction: pressure from force and area is ambiguous because of friction and dimensional changes, and differential thermal expansion of cell and medium changes the pressure on cooling. Sec. III.2: pressure falls continuously on cooling, more steeply where the medium solidifies, by about 0.26 to 0.47 GPa between 300 K and 1.8 K. Secs. III.2 and VI.2: the lead transition fixes the pressure near 7 K only. Sec. IV: a separate calibration is needed for other cells, media or filling factors. Appendix: a low initial pressure drops to zero near 200 K |
| 5 | N. Tateiwa and Y. Haga, Evaluations of pressure-transmitting media for cryogenic experiments with diamond anvil cell, Rev. Sci. Instrum. 80, 123901 (2009); read as preprint arXiv:1001.0454 | doi:10.1063/1.3265992 | full text | Introduction: liquid media solidify on cooling and their shear stress makes the pressure non-hydrostatic at low temperature. Sec. III and Sec. IV: fourteen media compared by ruby line broadening at 77 K, which reflects pressure gradients and uniaxial stress; some media solidify at about 1.2 to 2.4 GPa at room temperature, while nitrogen, argon and helium stay close to hydrostatic to 10 GPa; pressure changes on cooling of about 30 to 40% at 2 GPa for helium and nitrogen |
| 6 | M. S. Torikachvili, S. K. Kim, E. Colombier, S. L. Bud'ko and P. C. Canfield, Solidification and loss of hydrostaticity in liquid media used for pressure measurements, Rev. Sci. Instrum. 86, 123904 (2015) | doi:10.1063/1.4937478 | abstract | Abstract: solidification lines of nine liquid pressure media mapped to 2.3 GPa using resistance anomalies of a sample, separating hydrostatic from non-hydrostatic conditions; the room-temperature freezing pressure is the upper limit for the medium to count as hydrostatic |
| 7 | C. W. Hicks, M. E. Barber, S. D. Edkins, D. O. Brodsky and A. P. Mackenzie, Piezoelectric-based apparatus for strain tuning, Rev. Sci. Instrum. 85, 065003 (2014); read as preprint arXiv:1403.4368 | doi:10.1063/1.4881611 | full text | Section on current methods: the piezoelectric stacks lengthen on cooling, which can strain a sample beyond the range of the stacks; section on the apparatus: the design cancels this thermal expansion. Section on the apparatus: epoxy deformation cannot be ignored in finding the sample strain; a strain gauge measures the displacement, with temperature dependence and shifts between cool-downs. Appendices A and B and Table I: load transfer length through the epoxy, strain inhomogeneity near the ends and bending from asymmetric mounting. Section on sample mounting: buckling of thin samples from the Euler formula. Fig. 3 caption: uncertainty in the zero-strain point |
| 8 | M. V. Khenkin, E. A. Katz, A. Abate et al., Consensus statement for stability assessment and reporting for perovskite photovoltaics based on ISOS procedures, Nat. Energy 5, 35–49 (2020) | doi:10.1038/s41560-019-0529-5 | abstract | Abstract: inconsistent procedures and reported parameters make stability results hard to reproduce; the consensus adds procedures to separate degradation induced by the ambient from other stress factors, and lists the procedural details to report for reproducibility |
| 9 | T. Bar, S. K. Choudhary, M. A. Ashraf, K. S. Sujith, S. Puri, S. Raj and B. Bansal, Kinetic spinodal instabilities in the Mott transition in V2O3: evidence from hysteresis scaling and dissipative phase ordering, Phys. Rev. Lett. 121, 045701 (2018); read as preprint arXiv:1808.00693 | doi:10.1103/PhysRevLett.121.045701 | full text | Main text, Dynamic hysteresis: the onset temperatures on heating and cooling shift with the temperature ramp rate as a power law, and the quasistatic transition temperatures are obtained from fits over many rates. Supplement II.2: a control sample with a transition without hysteresis, measured at 5 to 40 K/min in the same cryostat, shows no difference between heating and cooling and no shift with rate. Supplement IV: relaxation time of the sample and substrate to the bath temperature of about 3 s |
