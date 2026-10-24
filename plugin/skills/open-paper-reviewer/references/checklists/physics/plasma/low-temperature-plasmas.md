---
id: T-LOW-TEMPERATURE-PLASMAS
name: Low-temperature and processing plasmas
type: technique
field: physics/plasma
applies_when: the paper bases a claim on a radio-frequency, microwave, dielectric barrier, corona or pulsed discharge, a plasma jet or an electric thruster, for materials processing, plasma medicine, plasma-treated liquids, gas conversion or propulsion, or attributes an effect to plasma species
version: "0.1"
---

# Low-temperature and processing plasmas

Low-temperature plasmas, including radio-frequency (RF) capacitively and inductively coupled discharges, dielectric barrier discharges (DBDs), atmospheric-pressure plasma jets (APPJs) and electric thrusters, are used to claim that a discharge delivers a given power, gas temperature and flux of reactive oxygen and nitrogen species (RONS), ions or photons, and that these cause an effect on a surface, a liquid, cells or tissue, or produce a measured thrust. Each claim depends on how much power reached the plasma, in which discharge mode, with what gas and surroundings, and on how the species were measured.

## 1. Power delivered to the plasma

**Question.** Does the paper report the power dissipated in the plasma, state how it was measured (current and voltage at the electrode, a charge-voltage plot, or the difference between plasma-on and plasma-off readings), and keep it distinct from the generator setting or the power drawn by the device?

**Why it matters.** Part of the power leaving a generator is lost in the matching network, cables, coils and nearby conductors, and incorrect evaluations of RF discharge power are common in the literature. For a small jet the power dissipated in the plasma can be a small fraction of the device input. A charge-voltage plot gives the discharge power only when it is averaged over whole cycles and is free of stray capacitance and inductance, and seemingly minor differences in matching networks and wiring have produced large differences between laboratories using the same reference cell.

**Resolved by.** The dissipated power stated for each condition, with the probe positions and how losses in the matching network, coil and cables were measured and removed; for DBDs, charge-voltage plots averaged over many cycles, the monitor capacitor stated and a check at low voltage without plasma showing no loop area; power density or energy per cycle reported so that conditions and devices can be compared.

**Benchmark.** [1], [2], [3], [4], [5]

## 2. Discharge mode and regime

**Question.** Does the paper identify the discharge mode under the conditions where the effect is claimed, for example filamentary or diffuse operation of a DBD, or the structure of a jet, and show that the mode did not change across the conditions being compared?

**Why it matters.** The same device can run in regimes with different electron densities, energies and spatial structure, and a change of driving frequency, gas composition or gap can move it between them. A filamentary DBD with many microdischarges can look uniform to the eye or to a slow camera. Filamentary discharges are irregular, so conditions differ from cycle to cycle and from place to place, while some gases give a more reproducible effluent.

**Resolved by.** Current waveforms resolved on the time scale of single microdischarges, showing one pulse per half cycle or many spikes; short-exposure images taken together with fast current measurements; the mode named for each condition; where conditions are compared, evidence that the mode is the same, or the change reported as part of the result.

**Benchmark.** [4], [5], [3]

## 3. Gas and target temperature

**Question.** How was the gas temperature measured, and the temperature at the treated target? If it was taken from the rotational spectrum of an excited molecule, does the paper show that the rotational population is in equilibrium with the translational temperature; if a probe was used, was it suitable for use in the plasma?

**Why it matters.** Non-equilibrium plasmas do not guarantee that the rotational distribution of an emitting excited state follows the gas temperature, and non-Boltzmann rotational spectra are common. Charged species and electric fields outside the core of a discharge can disturb conducting probes such as thermocouples, which is why non-conducting fibre-optic probes are used. Gas temperature changes reaction rates and flow, and heating of the target is a separate mechanism from plasma chemistry, so an unmeasured temperature leaves a thermal explanation open.

**Resolved by.** The method stated; for emission spectra, the band and a Boltzmann plot showing a single temperature, with the choice of molecule and state justified for the conditions, or a comparison with an independent method such as Schlieren imaging or a non-conducting fibre-optic probe; the temperature reported at the position of the target as well as near the source.

**Benchmark.** [6], [5], [8]

## 4. Feed gas purity, humidity and ambient air

**Question.** Does the paper give the feed gas purity, the measured water content of the feed gas, the flow rate, and how ambient air reaches the plasma (shielding gas, enclosure, distance to the target), and were these held fixed between the conditions compared?

**Why it matters.** Impurities at the level of parts per million change the densities of atomic oxygen, hydroxyl and hydrogen peroxide substantially, and nominally dry gas can carry enough water to be a main source of hydroxyl radicals. In open jets, air diffuses into the effluent and sets much of the chemistry, and feed-gas water can matter more than ambient humidity. An uncontrolled change in any of these can produce, or hide, the effect being claimed.

**Resolved by.** Gas grade and flow rates stated; feed-gas humidity measured with a hygrometer and reported; the ambient composition controlled by an enclosure or shielding gas, or measured; species or effects shown as a function of humidity or admixture where the claim depends on them.

**Benchmark.** [1], [5], [7]

## 5. Measurement of reactive species

**Question.** For each species whose density or flux supports a claim, is the method quantitative (absorption, laser-induced fluorescence with calibration, mass spectrometry with calibration) with its calibration and model inputs stated, or does the evidence rest on relative emission intensities? For species in liquids, how selective is the probe?

**Why it matters.** Emission intensity depends on the electron density and energy as well as on the density of the emitting species, so optical emission spectroscopy (OES) is hard to use for densities, even qualitatively, in non-equilibrium plasmas. Two-photon absorption laser-induced fluorescence (TALIF) needs a noble-gas calibration and quenching corrections, and different techniques applied to the same reference source have differed systematically, mainly through the quenching rates assumed, while the calibration adds uncertainty to absolute values. In liquids, colorimetric dyes cross-react with other species and spin traps have limited selectivity, so a signal does not identify one species.

**Resolved by.** Absolute densities with the method, calibration, quenching or cross-section data and uncertainties stated; any use of emission line ratios (actinometry) justified for the conditions; agreement with a second technique or with published values for a reference source; for liquid probes, blanks, tests with the possible interfering species added alone, and scavengers whose specificity is stated.

**Benchmark.** [1], [5], [7]

## 6. Electrodes, walls and the target

**Question.** Does the paper describe the electrode and chamber wall materials and their condition (cleaning, conditioning, deposits), and the electrical nature and distance of the target (conducting, grounded, dielectric or liquid), and does it test whether the result depends on them?

**Why it matters.** In processing reactors the balance between radicals and molecules can be set mainly by recombination on the chamber walls, whose coating changes during processing and causes the process to drift. Whether a jet touches its target or not can change the amount of a species delivered to a liquid by orders of magnitude. Charge left on dielectric surfaces persists between cycles and changes the next breakdown.

**Resolved by.** Wall and electrode materials stated, with the cleaning or conditioning done before each run and repeated runs after conditioning; target material, grounding and distance stated, and the jet's contact with the target described; the effect shown to persist when the target or wall condition is changed, or the dependence reported.

**Benchmark.** [9], [5], [4]

## 7. Attributing an effect to a plasma species

**Question.** When an effect on cells, tissue, liquids or surfaces is attributed to a particular species, does the paper separate that species from the other agents the plasma delivers (other reactive species, ultraviolet and vacuum ultraviolet light, electric fields and currents, heat) and from long-lived products formed in the treated liquid?

**Why it matters.** A plasma acts through several pathways at once, and many of the species found in a treated liquid form through secondary reactions there and not in the gas. Which individual species are responsible for a biological effect is still an open question in the field, and a scavenger or trap that is not specific cannot settle it.

**Resolved by.** Controls that remove one agent at a time, such as a magnesium fluoride window that passes vacuum ultraviolet light but blocks particles, changes in distance and feed-gas water, and the long-lived species added at the measured concentration without plasma; isotopic labelling to locate where a species forms; scavengers or antioxidants with their specificity stated; the species measured at the target, not only in the source.

**Benchmark.** [7], [8], [10], [5]

## 8. Facility effects in electric propulsion tests

**Question.** For thrust, efficiency or lifetime measured in a vacuum facility, does the paper report the background pressure (gauge type, location and correction), the effective pumping speed, and the wall material, and does it discuss how these may shift the result from what would be seen in space?

**Why it matters.** The influence of ground-test facilities on thruster performance is a recognised open question, and differences between facilities and between ground and flight performance lead to large margins or reluctance to use a thruster. Plasma-wall interaction and sputtering in the facility also affect assessments of wear.

**Resolved by.** Pressure measurements and effective pumping speed obtained and reported following a recommended practice; performance shown at more than one background pressure or compared with results from other facilities; wall materials and any back-sputtered deposits considered in wear and lifetime claims.

**Benchmark.** [10], [11]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | L. L. Alves, M. M. Becker, J. van Dijk, T. Gans, D. B. Go, K. Stapelmann, J. Tennyson, M. M. Turner and M. J. Kushner, Foundations of plasma standards, Plasma Sources Sci. Technol. 32, 023001 (2023); read as the author manuscript in PubMed Central, PMC12058226 | doi:10.1088/1361-6595/acb810 | full text | Sec. 2.1.1 (GEC reference cell): large unexpected differences in current-voltage measurements between labs, traced to matching networks, cable configuration and stray capacitance and inductance. Sec. 2.1.2 (COST reference microplasma jet): protocols include how to measure and calculate dissipated power, with reproducibility tested across jets and labs. Sec. 3.2 (atomic oxygen case study): ns-TALIF differs systematically from ps-TALIF and VUV absorption in one source, likely through the estimated collisional de-excitation rates, with xenon calibration adding uncertainty to absolute densities; O2 impurities of a few ppm raise atomic oxygen densities markedly, so protocols should specify impurity levels |
| 2 | V. Godyak, RF discharge diagnostics: Some problems and their resolution, J. Appl. Phys. 129, 041101 (2021) | doi:10.1063/5.0024258 | abstract | Abstract: incorrect evaluations of discharge power and inaccurate probe measurements appear in many recent RF diagnostics papers; the review sets out where these errors come from and how to mitigate them |
| 3 | F. Peeters and T. Butterworth, Electrical diagnostics of dielectric barrier discharges, in Atmospheric Pressure Plasma: from Diagnostics to Applications, ed. A. Nikiforov and Z. Chen, IntechOpen (2019) | doi:10.5772/intechopen.80433 | full text | Sec. 2.3: power is the charge-voltage loop area times frequency, integrated over whole cycles. Sec. 2.4: choice and measurement of the monitor capacitor. Secs. 3.3 to 3.5: stray capacitance and inductance distort the loop, checked at low voltage without plasma where any loop area is an artefact; cycle-to-cycle variation calls for averaging. Sec. 1: filamentary discharges usually develop, uniform ones only under some conditions |
| 4 | R. Brandenburg, Dielectric barrier discharges: progress on plasma sources and on the understanding of regimes and single filaments, Plasma Sources Sci. Technol. 26, 053001 (2017); read as the JATS full text in the TIB open repository | doi:10.1088/1361-6595/aa6426 | full text | "The classical operation regime and filamentary plasmas" and "Diffuse DBDs": filamentary and diffuse (glow or Townsend) regimes, their current signatures, the need for short-exposure imaging with fast current measurement because a dense filamentary discharge can look uniform, and the dependence of diffuse operation on gas purity. "Single filaments in volume and on surfaces": charge left on the dielectric and in the volume persists between half-periods and affects the following breakdown. "Electrical behavior and characterization": charge-voltage analysis, distortion by stray capacitance and series resistance, rounded loops whose area no longer equals the dissipated energy, and a recommendation to report specific energy or power density |
| 5 | S. Reuter, T. von Woedtke and K.-D. Weltmann, The kINPen: a review on physics and chemistry of the atmospheric pressure plasma jet and its applications, J. Phys. D: Appl. Phys. 51, 233001 (2018); read as the JATS full text in the TIB open repository | doi:10.1088/1361-6463/aab3ad | full text | "The plasma source kINPen": about 1 W dissipated in the plasma against about 20 W device input. "Electrical diagnostics": dissipated power from plasma-on minus plasma-off readings, with coil losses accounted for. "Probe measurements": because charged species form outside the core plasma, temperatures are measured with non-conducting fibre-optic probes; feed-gas humidity measured with a hygrometer because it governs reproducibility. "From spectral... to highly resolved imaging": OES is hard to use for densities in non-equilibrium plasmas. "Laser spectroscopy techniques": TALIF calibrated against xenon. "Colorimetry/fluorometry": dyes cross-react. "Streamer propagation pathway": argon discharge filamentary and stochastic, helium effluent reproducible. "Reaction chemistry" and "Reactive species": hydroxyl rises with feed-gas water; feed-gas water matters more than ambient humidity. "Interaction with liquids": touching and non-touching jets change hydrogen peroxide production by orders of magnitude. "(V)UV radiation": a magnesium fluoride cover used to isolate the effect of vacuum ultraviolet light |
| 6 | P. J. Bruggeman, N. Sadeghi, D. C. Schram and V. Linss, Gas temperature determination from rotational lines in non-equilibrium plasmas: a review, Plasma Sources Sci. Technol. 23, 023001 (2014) | doi:10.1088/0963-0252/23/2/023001 | abstract | Abstract: non-thermal plasmas do not guarantee that the rotational distribution of an excited diatomic state is in equilibrium with the gas temperature; non-Boltzmann spectra are often found and must be treated with care; the review analyses fitting procedures and gives recommendations on when gas temperatures can be taken from such spectra |
| 7 | Y. Gorbanev, D. O'Connell and V. Chechik, Non-thermal plasma in contact with water: the origin of species, Chem. Eur. J. 22, 3496–3505 (2016) | doi:10.1002/chem.201503771 | full text | "⋅OH radical": DMPO has limited selectivity, so adduct levels do not give exact radical amounts; isotopically labelled water shows that hydroxyl radicals form mainly in the gas phase, partly from water impurity in nominally dry feed gas. "Hydrogen peroxide": its level follows feed-gas humidity. Evaporated sample mixing into the gas explains part of the trapped radicals. "O3/1O2/O": the TEMP probe also responds to ozone. A magnesium fluoride window used to exclude photolysis |
| 8 | T. von Woedtke, A. Schmidt, S. Bekeschus, K. Wende and K.-D. Weltmann, Plasma medicine: a field of applied redox biology, In Vivo 33, 1011–1026 (2019) | doi:10.21873/invivo.11570 | full text | "Plasma Generation and Plasma Sources for Biomedical Applications": plasmas deliver reactive species, UV, visible and infrared light, heat, electric fields and currents, with output strongly dependent on source and parameters; "cold" means below about 40 °C at the target. "Redox Biology as the Scientific Grounding of Plasma Medicine": species in treated liquids are transferred from the plasma or formed in a network of secondary liquid reactions. "Conclusion and Outlook": whether single specific species are responsible remains open |
| 9 | G. Cunge, D. Vempaire, R. Ramos, M. Touzeau, O. Joubert, P. Bodard and N. Sadeghi, Radical surface interactions in industrial silicon plasma etch reactors, Plasma Sources Sci. Technol. 19, 034017 (2010) | doi:10.1088/0963-0252/19/3/034017 | abstract | Abstract: the chamber walls become coated during etching; the chlorine molecule to atom ratio is set mainly by the chemical nature of the walls, explaining process drifts; atom recombination probability differs by more than ten times between coated and clean walls; systematic cleaning and conditioning between wafers proposed for reproducible processing |
| 10 | I. Adamovich, S. D. Baalrud, A. Bogaerts, P. J. Bruggeman, M. Cappelli, V. Colombo and others, The 2017 Plasma Roadmap: low temperature plasma science and technology, J. Phys. D: Appl. Phys. 50, 323001 (2017); read as the JATS full text in the TIB open repository | doi:10.1088/1361-6463/aa76f5 | full text | "Aerospace applications: propulsion and flow control", electric propulsion part: the influence of ground-test facility effects on performance named as a critical open point; better data on plasma-wall interaction and sputtering yields needed to assess wear. "Medical applications": plasma appears to act through multiple pathways, and defining a plasma dose needs a fuller understanding of mechanisms |
| 11 | J. W. Dankanich, M. Walker, M. W. Swiatek and J. T. Yim, Recommended practice for pressure measurement and calculation of effective pumping speed in electric propulsion testing, J. Propuls. Power 33, 668–680 (2017) | doi:10.2514/1.B35478 | abstract | Abstract: differences between facilities and between ground and flight performance lead to large margins or reluctance to adopt electric propulsion; measurement practice must be consistent and repeatable across facilities; the paper gives a recommended practice for pressure measurement and effective pumping speed |
