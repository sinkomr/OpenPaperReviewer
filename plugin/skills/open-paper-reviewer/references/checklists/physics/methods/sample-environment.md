---
id: T-SAMPLE-ENVIRONMENT
name: Sample environment control
type: technique
field: physics/methods
applies_when: the paper bases a claim on the magnetic field, strain, electric field or atmosphere at the sample, on hysteresis between sweep directions in temperature, field or gate voltage, on coercive fields or field-cooled and zero-field-cooled comparisons, or on data from a strain cell
version: "0.1"
---

# Sample environment control

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

**Benchmark.** [1], [3], [6]

## 4. Strain transmitted to the sample

**Question.** How was the strain in the sample determined, as distinct from the displacement or voltage applied by the strain device, and how were the strain-free point and the uniformity of strain across the measured region established?

**Why it matters.** Applied displacement reaches the sample through epoxy or another bond that deforms, so the strain in the sample is less than the nominal value from the displacement and sample length. Strain is not uniform near the bonded ends, an asymmetric mount bends the sample, and long thin samples can buckle. Differential thermal contraction between sample and device adds strain on cooling, so zero applied voltage is not zero strain.

**Resolved by.** A displacement or strain sensor read at the measurement temperature, with its calibration and any shift between cool-downs stated; the transfer through the bond estimated or measured; the strain-free point located with its uncertainty; the measured region kept away from the bonded ends and the mounting described, including sample dimensions, bond thickness and symmetry.

**Benchmark.** [4]

## 5. Atmosphere and exposure

**Question.** In what atmosphere was the sample stored, mounted and measured (vacuum, inert gas, exchange gas or air, with humidity where relevant), how long was it exposed to air, and does the paper separate effects of the atmosphere from the effect it claims?

**Why it matters.** Species adsorbed on unprotected surfaces add charge traps and can change the properties being measured, and degradation driven by the ambient can be confused with the response to other stresses such as light, bias or temperature. Without the atmosphere and exposure history, another laboratory cannot reproduce the conditions.

**Resolved by.** The atmosphere, pressure of any exchange gas, humidity and illumination stated for storage, preparation and measurement, with the time between preparation and measurement; key results repeated in a controlled atmosphere or after encapsulation; drifts with time shown and assigned either to the sample or to the environment.

**Benchmark.** [3], [5]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | M. Sawicki et al., Sensitive SQUID magnetometry for studying nanomagnetism, Semicond. Sci. Technol. 26, 064006 (2011); read as preprint arXiv:1101.4764 | doi:10.1088/0268-1242/26/6/064006 |
| 2 | A. Quintana-Nedelcos et al., On the correct estimation of the magnetic entropy change across the magneto-structural transition from the Maxwell relation: Study of MnCoGeBx alloy ribbons, J. Alloys Compd. 694, 1189 (2017) | doi:10.1016/j.jallcom.2016.10.116 |
| 3 | Y. Yu. Illarionov et al., Insulators for 2D nanoelectronics: the gap to bridge, Nat. Commun. 11, 3385 (2020) | doi:10.1038/s41467-020-16640-8 |
| 4 | C. W. Hicks et al., Piezoelectric-based apparatus for strain tuning, Rev. Sci. Instrum. 85, 065003 (2014); read as preprint arXiv:1403.4368 | doi:10.1063/1.4881611 |
| 5 | M. V. Khenkin et al., Consensus statement for stability assessment and reporting for perovskite photovoltaics based on ISOS procedures, Nat. Energy 5, 35 (2020) | doi:10.1038/s41560-019-0529-5 |
| 6 | T. Bar et al., Kinetic spinodal instabilities in the Mott transition in V2O3: evidence from hysteresis scaling and dissipative phase ordering, Phys. Rev. Lett. 121, 045701 (2018); read as preprint arXiv:1808.00693 | doi:10.1103/PhysRevLett.121.045701 |
