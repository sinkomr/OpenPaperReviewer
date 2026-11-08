---
id: T-ACTIVITY-DOSIMETRY
name: Activity and dosimetry measurements
type: technique
field: physics/nuclear
applies_when: the paper reports a radionuclide activity or activity concentration, standardises a radionuclide, measures activity with a radionuclide calibrator, ionisation chamber or gamma-ray spectrometer, calibrates a dosimeter, or bases a claim on absorbed dose, kerma or traceability to a primary standard
version: "0.1"
---

# Activity and dosimetry measurements

## 1. Traceability for the radionuclide measured

**Question.** Does the paper name the chain that links each activity value to a primary standard for the same radionuclide, including the instrument, the calibration factor or dial setting and where it came from, the reference source with its certificate, date and uncertainty, and the range of activity over which the instrument was shown to be linear?

**Why it matters.** Traceability belongs to a result for a particular radionuclide: an instrument calibrated with other radionuclides, or an efficiency or sensitivity curve interpolated to a new radionuclide, does not give a direct link to a primary standard. Calibration settings supplied with commercial calibrators have differed from primary standards by several percent and, in the past, by more than 20%.

**Resolved by.** The calibration factor determined with a standard of the same radionuclide in the same instrument, or a reference source of that radionuclide certified by a laboratory with demonstrated traceability; each link in the chain given with its uncertainty; manufacturer settings checked against such a source before use; linearity checked over the activity range used; where the primary standard is held abroad, evidence that it is recognised through international comparisons.

**Benchmark.** [1], [2]

## 2. Source geometry, container and transfer of activity

**Question.** Were the measured sources in the same container type, filling volume or mass and position as the sources used for calibration, and how was activity transferred or diluted between the standard and the measured source?

**Why it matters.** The response of an ionisation chamber depends on the container's geometry, composition and wall thickness and on the filling volume, so calibration settings determined for one container, often a sealed ampoule, need not hold for a vial or syringe. Activity transferred by dilution remains traceable only if the activity concentration and the transferred mass or volume are known, and weighing is one of the dominant uncertainty components in primary standardisation, one that laboratories have evaluated in very different ways.

**Resolved by.** Calibration factors stated for the container and volume actually used, or a correction measured by assaying aliquots of one solution in both containers; transfers made by weighing or with a calibrated dispenser; the weighing method, balance calibration and buoyancy correction described and their uncertainty evaluated; the activity concentration per unit mass reported.

**Benchmark.** [1], [2], [3]

## 3. Radionuclidic purity and ingrowth

**Question.** How was the radionuclidic purity of the source established, by which technique and with what detection limit, and are impurities and any ingrowing progeny corrected for at the reference time of the activity?

**Why it matters.** An impurity can emit radiation that cannot be told apart from that of the radionuclide of interest, high-energy photons from an impurity give anomalous calibrator readings, and pure beta-emitting impurities are invisible to gamma-ray spectrometry. In efficiency-calculated LSC, an impurity that is not accounted for, or is accounted for wrongly, can make the recovered activity either too low or too high, depending on the counting efficiencies of the two radionuclides and the impurity fraction.

**Resolved by.** A high-resolution gamma-ray spectrum with impurity-to-parent activity ratios at the reference date; pure beta-emitting impurities measured after the main radionuclide has decayed, for example by LSC; each correction and its uncertainty stated; measurements timed, or corrected, for impurities that grow in during the campaign.

**Benchmark.** [1], [2], [4]

## 4. Efficiency model and extrapolation in primary methods

**Question.** For activities obtained by coincidence counting or by calculated LSC efficiencies, does the paper state the model and its inputs (extrapolation function, range of efficiencies covered and fit weights; beta spectrum shape factor, ionisation quenching parameter and decay scheme for LSC), show how sensitive the activity is to them, and show that the LSC sources were stable during counting?

**Why it matters.** In coincidence counting the activity comes from extrapolating to full efficiency; when several laboratories fitted the same data, their slopes differed widely, the intercept stayed robust only when the extrapolation stayed close to the data, and some fitting codes dropped points without the user knowing. In LSC the calculated efficiency depends on the assumed beta spectrum shape and quenching parameter: changing the assumed shape has moved activities by several tenths of a percent and was a possible cause of a systematic difference between TDCR and CNET results, and some scintillation cocktails have lost several percent of their count rate over weeks, a loss the efficiency model does not follow.

**Resolved by.** The extrapolation function, efficiency range, weighting and any excluded points stated, with residuals shown and an alternative extrapolation tried; for LSC, the quenching parameter, spectrum shape and decay data stated with their sources and varied to give an uncertainty component; count rates of LSC sources shown to be stable over the counting period; agreement shown between two methods with different model dependence, such as TDCR and CNET, or LSC and coincidence counting.

**Benchmark.** [3], [5], [6]

## 5. Components of the activity uncertainty budget

**Question.** Does the uncertainty budget list the components specific to the activity measurement (counting statistics, extrapolation or efficiency model, dead time and resolving times, background, weighing, decay data and the half-life used to correct to the reference time), say how each was evaluated, and identify correlations between them?

**Why it matters.** When laboratories evaluated uncertainties from the same raw data of one primary measurement, their individual components differed by up to a factor of 250, so a combined uncertainty alone does not show what was included. The half-life contribution becomes important for short-lived radionuclides, and published reports often omit the reasoning behind each estimate and the correlations among components.

**Resolved by.** A table of uncertainty components with the method of evaluation for each; the reference date and time of the activity, with the half-life used and its uncertainty; correlated components, such as shared weighings or decay data, identified and treated; the combined uncertainty consistent with what comparable primary or secondary measurements achieve.

**Benchmark.** [3], [6]

## 6. Dosimeter calibration, beam quality and influence quantities

**Question.** For doses measured with an ionisation chamber or other dosimeter, does the paper state the calibration coefficient (quantity, reference beam quality, calibrating laboratory, date), how it was converted to the beam quality of the measurement, and which corrections for influence quantities (air density, humidity, electrometer, polarity, ion recombination, leakage) were applied under which reference conditions?

**Why it matters.** A calibration coefficient is valid only under the reference conditions of the calibration, and a beam quality different from the calibration quality needs a beam quality correction factor, which few laboratories can measure directly and which is otherwise calculated. Influence quantities such as air density, polarity and recombination must be corrected, and readings taken before the chamber has stabilised after a change of polarity or voltage can carry errors larger than the correction itself. With an SSDL calibration, the combined standard uncertainty of absorbed dose to water in a cobalt-60 beam is typically just under 1%, so a smaller claimed uncertainty needs justification.

**Resolved by.** The calibration certificate details and the route of traceability to a PSDL or SSDL; the source of the beam quality correction factor, measured or calculated, and the beam quality specifier; each correction factor with its value; depth, field size and source distance given; stability, leakage and pre-irradiation checks reported; an uncertainty budget that separates the calibration step from the user's measurement.

**Benchmark.** [7]

## 7. Detector response outside reference conditions

**Question.** When dose is measured far from the calibration conditions, for example in small or non-uniform fields, steep dose gradients or a different energy spectrum, or with solid-state or other non-reference detectors, does the paper show that the detector's response was corrected for, or verified under, those conditions?

**Why it matters.** A detector reports the mean dose over its sensitive volume and perturbs the particle fluence; in small fields, loss of lateral charged-particle equilibrium and volume averaging make the corrections for larger chambers excessive or unknown, and the spectrum changes with field size. Uncorrected detector readings for the same nominal small field have differed by about 15% between centres, which is why at least two detector types are advised for such measurements.

**Resolved by.** The detector's size compared with the field size, chosen so that the volume-averaging correction stays small; published output correction factors applied with their uncertainties; results from at least two detector types that agree after correction; solid-state detectors verified against a reference ionisation chamber; the conditions of the measurement compared explicitly with those of the calibration.

**Benchmark.** [7], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | International Atomic Energy Agency (IAEA), Quality Assurance for Radioactivity Measurement in Nuclear Medicine, Technical Reports Series No. 454 (IAEA, Vienna, 2006) | https://www-pub.iaea.org/MTCD/publications/PDF/TRS454_web.pdf |
| 2 | D. E. Bergeron and J. T. Cessna, An update on 'dose calibrator' settings for nuclides used in nuclear medicine, Nucl. Med. Commun. 39, 500 (2018) | doi:10.1097/MNM.0000000000000833 |
| 3 | C. J. Bailat et al., International comparison CCRI(II)-S7 on the analysis of uncertainty budgets for 4πβγ coincidence counting, Metrologia 51, Tech. Suppl. 06018 (2014); read as the report hosted by BIPM | doi:10.1088/0026-1394/51/1A/06018 |
| 4 | D. E. Bergeron et al., The effect of impurities on calculated activity in the triple-to-double coincidence ratio liquid scintillation method, Appl. Radiat. Isot. 70, 2170 (2012) | doi:10.1016/j.apradiso.2012.02.084 |
| 5 | D. E. Bergeron et al., Comparison of 14C liquid scintillation counting at NIST and NRC Canada, Appl. Radiat. Isot. 109, 30 (2016); read as PMC4937459 | doi:10.1016/j.apradiso.2015.11.007 |
| 6 | R. Fitzgerald et al., Uncertainties in 4πβ–γ coincidence counting, Metrologia 52, S86–S96 (2015) | doi:10.1088/0026-1394/52/3/S86 |
| 7 | International Atomic Energy Agency (IAEA), Absorbed Dose Determination in External Beam Radiotherapy: An International Code of Practice for Dosimetry Based on Standards of Absorbed Dose to Water, Technical Reports Series No. 398 (Rev. 1) (IAEA, Vienna, 2024) | doi:10.61092/iaea.ve7q-y94k |
| 8 | International Atomic Energy Agency (IAEA), Dosimetry of Small Static Fields Used in External Beam Radiotherapy: An International Code of Practice for Reference and Relative Dose Determination, Technical Reports Series No. 483 (IAEA, Vienna, 2017) | https://www-pub.iaea.org/MTCD/Publications/PDF/D483_web.pdf |
