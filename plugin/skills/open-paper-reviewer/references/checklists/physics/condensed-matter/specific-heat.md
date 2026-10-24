---
id: T-SPECIFIC-HEAT
name: Specific heat and calorimetry
type: technique
field: physics/condensed-matter
applies_when: the paper reports heat capacity from relaxation, ac or adiabatic calorimetry or differential scanning calorimetry, or bases a claim about a phase transition, its order or bulk nature, a latent heat, an entropy, an electronic coefficient or a Schottky term on it
version: "0.1"
---

# Specific heat and calorimetry

Specific heat is used to claim that a phase transition is bulk and of a given order, to measure latent heats and the entropy released, and to extract electronic, lattice, magnetic and Schottky (two-level) contributions. It is measured by relaxation (heat-pulse) calorimetry, alternating-current (ac) calorimetry, adiabatic calorimetry or differential scanning calorimetry (DSC), and in each case the sample's share is obtained from a total that includes the platform, adhesive and any container.

## 1. Sample mass and the sample's share of the signal

**Question.** Does the paper give the sample mass with its uncertainty, and show what fraction of the total measured heat capacity the sample contributes over the temperature range of the claim?

**Why it matters.** The accuracy of a relaxation calorimeter is generally a percentage of the total heat capacity, so when the sample is small compared with the platform and adhesive, the sample value left after subtraction carries a large relative error. The mass error passes directly into a specific heat per gram or per mole, and a sample of a few milligrams represents the material only if it is pure and homogeneous.

**Resolved by.** Mass, molar mass and the formula unit stated; the ratio of sample to addenda heat capacity shown or stated where the claimed feature lies; an uncertainty that includes the addenda and mass terms; evidence that the piece measured is phase-pure, not only the batch it came from.

**Benchmark.** [1], [4]

## 2. Addenda measurement and subtraction

**Question.** Was the addenda (platform, grease or other adhesive, and any container) measured separately under the same conditions as the sample, including the same adhesive in a similar amount and the same magnetic fields, and was the adhesive used only where its own heat capacity is smooth and reproducible?

**Why it matters.** The adhesive adds heat capacity of its own. A common vacuum grease has an anomaly near its melting range, between about 260 K and 325 K, where its heat capacity is reproducible only to about 5 per cent. Below about 10 K the platform's own heat capacity can depend on field, and thermometer calibrations change with field. An addenda measured under other conditions leaves residual features in the subtracted data that can be read as sample anomalies.

**Resolved by.** Addenda measured with the adhesive on the platform before the sample was mounted, at each field used; the adhesive chosen for the temperature range; the addenda curve shown, or its size stated, next to the sample data; a check that any claimed feature is absent from the addenda.

**Benchmark.** [1], [2]

## 3. Thermal contact and internal equilibrium

**Question.** For relaxation calorimetry, does the paper report the quality of the thermal contact between sample and platform (for example the coupling parameter of a two-time-constant fit and the fit deviation), and show that the sample reaches internal equilibrium quickly compared with the measurement time?

**Why it matters.** When the sample takes longer to equilibrate internally than the measurement allows, the heat capacity obtained is too small. Contact through the grease can degrade with cooling, through differential contraction or at a structural transition, and powders are generally measured less accurately than single crystals.

**Resolved by.** Coupling and fit quality reported across the temperature range, especially near the claimed anomaly, with poorly coupled points remeasured or excluded by a stated rule; thin, flat samples or several small pieces for poor thermal conductors; powders pressed or wrapped in foil and checked against a reference; a remounted sample giving the same result.

**Benchmark.** [1], [3], [4]

## 4. Sharp and first-order transitions

**Question.** Near a sharp or first-order transition, how were the data taken and analysed (temperature rise per point, standard fit or analysis of the full heating and cooling curve, heating and cooling directions), and are the peak shape and any latent heat quoted from a method able to resolve them?

**Why it matters.** The standard relaxation fit assumes a heat capacity that is constant over each heat pulse, so it does not capture a latent heat, and a peak narrower than the temperature rise is smeared or missed. Any dynamic method averages over a temperature interval, making sharp peaks lower, broader and shifted, and hysteresis is seen only if a pulse crosses the whole transition. Ac calorimetry detects only the reversible part of the response, so it can locate a first-order transition but does not measure its latent heat.

**Resolved by.** The temperature rise per point stated and small compared with the transition width; slope analysis or long heat pulses that cross the transition, compared with standard data where they overlap; heating and cooling compared; any latent heat reported separately from the continuous heat capacity and obtained by a method that captures it.

**Benchmark.** [1], [3], [4], [5]

## 5. Ac calorimetry: working frequency and absolute values

**Question.** For ac calorimetry, does the paper show that the working frequency lies in the range where the temperature oscillation is inversely proportional to the heat capacity, and say whether the values are absolute or scaled, and if scaled, to what?

**Why it matters.** The simple relation between oscillation amplitude and heat capacity holds only between a lower frequency set by the thermal link to the bath and an upper frequency at which the sample decouples from heater and thermometer. An apparently inverse-frequency amplitude does not by itself ensure accuracy, since the phase shows the sample beginning to decouple earlier. In many set-ups, such as pressure cells, the heat delivered to the sample is not known, so the data are relative and are often normalised to another measurement.

**Resolved by.** Frequency dependence of amplitude and phase measured at several temperatures (and pressures, where relevant) showing the expected behaviour at the working point; addenda determined from an empty cell; for relative data, the scaling stated and the claims limited to relative changes; absolute values cross-checked against relaxation or adiabatic data.

**Benchmark.** [2], [5]

## 6. DSC: baseline, reference and sample runs

**Question.** For heat capacity from DSC, were baseline, reference (such as sapphire) and sample runs made with the same temperature programme and crucibles, was the baseline shown to be reproducible, and is the stated accuracy smaller than the effect claimed?

**Why it matters.** DSC obtains heat capacity as a ratio to a reference after removing the empty-crucible baseline, so baseline drift between runs passes into the result. Typical accuracy is about 1 to 2 per cent, poorer for heat-flux instruments, and differences smaller than that are not resolved.

**Resolved by.** Temperature programme, heating rate, purge gas, crucibles and sample and reference masses stated; repeated baselines shown to agree; the reference measured as an unknown and compared with its tabulated values; an uncertainty stated and compared with the size of the claimed effect.

**Benchmark.** [4], [6]

## 7. Lattice, Schottky and nuclear backgrounds

**Question.** How were the lattice (phonon) contribution and any Schottky contributions (nuclear, crystal-field or from paramagnetic impurities) determined and subtracted, over what temperature range was each fitted, and how much do the extracted electronic or magnetic terms change with that choice?

**Why it matters.** The Debye model is a reasonable approximation only for simple, isotropic crystals, and the effective Debye temperature of a real solid varies with temperature, so a low-temperature power law fitted over too wide a range assigns lattice heat capacity to other terms. A linear term need not come from conduction electrons; lattice vacancies, for example, can also give one. The lattice entropy near a transition can be large, and a nuclear term that rises as the inverse square of temperature below about 1 K, and grows with field, complicates the extraction of linear coefficients and jumps.

**Resolved by.** The lattice term taken from a non-magnetic or non-superconducting analogue of similar mass, or from data in which the transition is suppressed by field; the fit form and range stated; nuclear and other Schottky terms fitted with a field dependence consistent with their origin; results shown for more than one reasonable choice of background.

**Benchmark.** [4], [7]

## 8. Size of the anomaly and entropy balance

**Question.** Is the size of the anomaly at the transition (the jump in heat capacity, the jump normalised by the electronic coefficient, or the entropy released) reported together with the construction used for a broadened transition, compared with the value expected for the claimed state, and checked by an entropy balance?

**Why it matters.** A broadened transition makes the jump ambiguous unless it is constructed by a stated rule. A residual linear term well below the transition can show that part of the sample does not take part, which reduces the jump, so a small anomaly may come from a minority of the sample. For a second-order transition the entropies of the two states must match at the transition, which constrains any extrapolated normal-state curve, and the entropy of magnetic ordering can be compared with the value expected for full ordering of local moments.

**Resolved by.** An equal-entropy construction of the jump, with onset and midpoint temperatures given; the residual and normal-state electronic coefficients reported; the normalised jump compared with the weak-coupling value of about 1.43 for a superconductor, or the magnetic entropy compared with R ln 2 for spin one-half moments; an entropy balance shown; a claim of a bulk transition supported by an anomaly of a size consistent with the whole sample.

**Benchmark.** [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | Quantum Design, Physical Property Measurement System Heat Capacity Option User's Manual, part 1085-150, Rev. M7 (December 2017); read as the copy hosted by the KTH Nanolab | https://www.nanophys.kth.se/nanolab/ppms/4307-004%20Dynacool%20Digital%20User%20Manual%20Set/07%201085-150%20Rev%20M7%20Heat%20Capacity%20Option%20User's%20Manual.pdf | full text | Sec. 1.4: accuracy, a percentage of the total, is lost when the sample is small compared with the addenda; slow internal equilibration makes the result too small; flat samples for poor conductors; the standard fit assumes constant heat capacity over a cycle. Sec. 4.3: two-tau model with a grease conductance; Sec. 4.3.3.6: error terms include addenda, mass and fit deviation. Sec. 4.3.4.1: a first-order peak narrower than the temperature rise is smeared or missed. Sec. 4.3.4.2: a sharp feature may shift with sweep direction. Sec. 5.4: field corrections to thermometer calibration. Sec. 6.2.4.1: one grease has an anomaly between 260 K and 325 K, reproducible to about 5%. Sec. 6.2.5: addenda depends on field below about 10 K. Sec. 7.3.1: addenda includes the grease and is measured at each field before the sample is mounted. Sec. 13.2.3: coupling below about 90% calls for remounting; cracked grease from differential contraction or structural transitions |
| 2 | S. Tagliati and A. Rydh, Absolute accuracy in membrane-based ac nanocalorimetry, Thermochim. Acta 522, 66–71 (2011); read as preprint arXiv:1203.2049 | doi:10.1016/j.tca.2011.04.006 | full text | Secs. 2 to 5: the simple relation between amplitude and heat capacity holds only in a frequency window; the addenda is determined from an empty cell; at high frequency the sample decouples through its thermal link; grease adds heat capacity and should be measured before the sample is mounted. Sec. 4: the phase shows decoupling earlier than the amplitude, so apparent inverse-frequency behaviour is not enough for absolute accuracy. Sec. 5: choice of working frequency for accuracy |
| 3 | A. Scheie, LongHCPulse: Long pulse heat capacity on a Quantum Design PPMS, J. Low Temp. Phys. 193, 60–73 (2018); read as preprint arXiv:1705.07129 | doi:10.1007/s10909-018-2042-9 | full text | Sec. I: the standard method assumes constant heat capacity over a pulse and is insensitive to latent heat, so long pulses are needed for first-order transitions. Sec. II.B: hysteresis is captured only if a pulse crosses the whole transition. Sec. III.B: sample and platform do not equilibrate instantly, because of the finite conductance between them, so data just after the heater switches are discarded. Sec. III.C: short-pulse data are taken to correct the long-pulse analysis |
| 4 | J. Biele, M. Grott, M. E. Zolensky, A. Benisek and E. Dachs, The specific heat of astro-materials: review of theoretical concepts, materials and techniques, Int. J. Thermophys. 43, 144 (2022); read as the open-access version PMC9343321 | doi:10.1007/s10765-022-03046-5 | full text | "Theory" and "'Calorimetric' Debye temperatures and their fit": the Debye model suits only simple isotropic crystals and the calorimetric Debye temperature varies with temperature; a nuclear term matters below about 1 K, depends on field and falls as 1/T² above its peak; a low-temperature linear term need not come from conduction electrons and can come from lattice vacancies. "Determination of Lattice Heat Capacity": the lattice term must be estimated over the whole range of an anomaly, for example by fitting regions it does not affect or by comparison with an isostructural compound. "Heat-pulse relaxation calorimetry (PPMS)": accuracy depends on sample mass and geometry, is lower for powders than crystals, and earlier software failed at first-order transitions. "Differential scanning calorimetry": the three-curve method, accuracy about 1–2%, heat-flux instruments less accurate. "Important notes for experimental cP data": small samples must be pure and homogeneous; dynamic methods make sharp peaks lower, broader and shifted |
| 5 | H. Wilhelm, AC-calorimetry at high pressure and low temperature, Adv. Solid State Phys. 43, 889 (2003); read as preprint arXiv:cond-mat/0303457 | doi:10.1007/978-3-540-44838-9_63 | full text | Introduction and Sec. 1: ac calorimetry is sensitive but less accurate in absolute terms; the signal follows the inverse-frequency law only between two cut-off frequencies set in part by the pressure medium. Secs. 2 and 3: the heat supplied to the sample is not known, so values are relative and normalised to other data; frequency tests at several temperatures and pressures are needed. Sec. 2: ac calorimetry detects only the reversible part and is not the tool for a latent heat, though it can locate a first-order transition |
| 6 | J. E. Daw, Measurement of specific heat capacity using differential scanning calorimeter, Idaho National Laboratory report INL/EXT-08-15056 (2008) | doi:10.2172/941744 | full text | Sec. 2 (Approach): three runs (empty-crucible baseline, reference of known specific heat, sample) under the same programme; specific heat obtained as a ratio to the reference; baselines compared with recent ones and the holder adjusted if they drift; the reference compared with tabulated values to gain confidence |
| 7 | G. R. Stewart, Superconductivity in iron compounds, Rev. Mod. Phys. 83, 1589–1652 (2011); read as preprint arXiv:1106.1618 | doi:10.1103/RevModPhys.83.1589 | full text | Sec. II.B: entropy of magnetic ordering compared with R ln 2 for a spin one-half local moment. Sec. III.B.1: normal-state electronic term from an entropy match at a second-order transition, with the large phonon term taken from a non-superconducting neighbouring composition. Sec. III.B.3.a: broadened transitions analysed by an equal-area (equal-entropy) construction; a residual linear term can mean part of the sample is not superconducting, reducing the jump. Sec. III.B.3.b: a Schottky upturn above the transition makes the jump harder to determine. Sec. III.B.4: weak-coupling value of the normalised jump is 1.43 |
