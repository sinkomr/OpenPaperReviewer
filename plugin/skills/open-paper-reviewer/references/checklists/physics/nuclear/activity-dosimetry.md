---
id: T-ACTIVITY-DOSIMETRY
name: Activity and dosimetry measurements
type: technique
field: physics/nuclear
applies_when: the paper reports a radionuclide activity or activity concentration, standardises a radionuclide, measures activity with a radionuclide calibrator, ionisation chamber or gamma-ray spectrometer, calibrates a dosimeter, or bases a claim on absorbed dose, kerma or traceability to a primary standard
version: "0.1"
---

# Activity and dosimetry measurements

Activity and dosimetry measurements are used to claim the activity of a radioactive source in becquerels (Bq), the absorbed dose or kerma delivered by a radiation field, and that these values are traceable to primary standards held by national metrology institutes (NMIs) through primary and secondary standards dosimetry laboratories (PSDLs and SSDLs). Primary methods include coincidence counting and liquid scintillation counting (LSC) with the triple-to-double coincidence ratio (TDCR) or CIEMAT/NIST efficiency tracing (CNET) methods; secondary measurements use instruments such as re-entrant ionisation chambers (radionuclide or "dose" calibrators), high-purity germanium (HPGe) gamma-ray spectrometers and dosimeters calibrated against those standards.

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

## 8. Efficiency, summing and attenuation in gamma-ray spectrometry

**Question.** For activities obtained by gamma-ray spectrometry, does the paper state how the full-energy peak efficiency was obtained for the sample's geometry, density and composition, and whether true coincidence summing and differences in self-attenuation between the sample and the calibration source were corrected for?

**Why it matters.** Photons emitted in the same decay can be detected together, removing counts from or adding counts to a peak; the effect grows as the source is brought closer to the detector and, if it is not corrected, can make the activity too high or too low. Calculated corrections depend on an accurate model of the detector, and different codes have disagreed widely on summing with X-rays.

**Resolved by.** The efficiency calibration source, its radionuclides, geometry and matrix stated; summing corrections made with a stated method and detector model, or a counting distance at which summing is small; corrections for differences in density and composition between sample and calibration source; activities from several gamma lines of the same radionuclide shown to agree.

**Benchmark.** [9]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | International Atomic Energy Agency (IAEA), Quality Assurance for Radioactivity Measurement in Nuclear Medicine, Technical Reports Series No. 454 (IAEA, Vienna, 2006) | https://www-pub.iaea.org/MTCD/publications/PDF/TRS454_web.pdf | full text | Sec. 4.6: container geometry, composition and wall thickness can significantly affect the activity measurement, and a change of vial type may invalidate earlier calibrations. Sec. 5.4.3.2: impurities with similar emissions cannot be separated, high-energy photon impurities cause anomalous calibrator readings, impurity ratios must be reported, pure beta impurities need decay and LSC. Sec. 5.6: traceability through an unbroken chain to primary standards recognised by BIPM through comparisons. App. VII.8.3, VII.8.6 and VII.8.7: linearity over the range of use, accuracy checked with NMI-traceable sources in the same container and volume, subsidiary calibrations for other containers by assaying aliquots of one solution. App. VIII: traceability applies to a result for a specific radionuclide; sensitivity curves interpolated to other radionuclides do not give traceability; transfers are traceable only with known activity concentration and transferred mass or volume |
| 2 | D. E. Bergeron and J. T. Cessna, An update on 'dose calibrator' settings for nuclides used in nuclear medicine, Nucl. Med. Commun. 39, 500–504 (2018) | doi:10.1097/MNM.0000000000000833 | full text | Introduction: a nuclide-specific dial setting converts chamber current to displayed activity. Table 1 and Sec. 3: separate settings for ampoules, syringes and vials, with volume dependences noted; manufacturer settings biased by up to about 3.4% for one radionuclide; impurities in one radionuclide corrected using germanium spectrometry, and ingrowing impurities biased calibrator readings over time. Discussion: users should verify settings on their own systems. Conclusions: earlier manufacturer settings overestimated activities, some by more than 20% |
| 3 | C. J. Bailat, J. Keightley, Y. Nedjadi and others, International comparison CCRI(II)-S7 on the analysis of uncertainty budgets for 4πβγ coincidence counting, Metrologia 51, Tech. Suppl. 06018 (2014); read as the report hosted by BIPM | doi:10.1088/0026-1394/51/1A/06018 | full text | Abstract and Sec. 1: extrapolation and weighing are dominant components in primary coincidence standardisations. Sec. 4.1 and Table 7: with the same raw data, the maximum-to-minimum ratio of reported components reached 250 (for the half-life), and the half-life contribution matters more for short-lived radionuclides. Sec. 4.2: fitted slopes differed widely, the intercept is robust only if extrapolation stays near the data, some codes remove points without the user knowing. Sec. 4.3 and Conclusions: weighing strongly influences the budget and its evaluation varied 26-fold; reports should describe each contribution |
| 4 | D. E. Bergeron, R. P. Fitzgerald, B. E. Zimmerman and J. T. Cessna, The effect of impurities on calculated activity in the triple-to-double coincidence ratio liquid scintillation method, Appl. Radiat. Isot. 70, 2170–2175 (2012) | doi:10.1016/j.apradiso.2012.02.084 | abstract | Abstract (NIST publication record): unaccounted or wrongly accounted impurities in TDCR can give lower or higher recovered activities, depending on the counting efficiencies of the nuclide and the impurity and on the amount of impurity; model tested with mixed sources |
| 5 | D. E. Bergeron, R. Galea, L. Laureano-Pérez and B. E. Zimmerman, Comparison of 14C liquid scintillation counting at NIST and NRC Canada, Appl. Radiat. Isot. 109, 30–35 (2016); read as PMC4937459 | doi:10.1016/j.apradiso.2015.11.007 | full text | Secs. 1 and 3.1: some cocktail formulations lost several percent of their count rate, about 3% over three weeks in one case, with no reliable correction. Sec. 2.4: efficiency models with a fitted ionisation quenching parameter and an assumed allowed beta spectrum shape. Sec. 3.2: TDCR consistently exceeded CNET, possibly through the assumed beta spectrum; reanalysis with a different shape factor raised activities by about 0.2% to 0.7% and improved agreement between methods. Sec. 4: closer agreement with the certified value after reanalysis |
| 6 | R. Fitzgerald, C. Bailat, C. Bobin and J. D. Keightley, Uncertainties in 4πβ–γ coincidence counting, Metrologia 52, S86–S96 (2015) | doi:10.1088/0026-1394/52/3/S86 | abstract | Abstract (NIST publication record): reports seldom give the rationale for uncertainty estimates or the correlations among components; components covered include measurement variability, extrapolation functions, dead time and resolving time, gravimetric links, and nuclear and atomic data |
| 7 | International Atomic Energy Agency (IAEA), Absorbed Dose Determination in External Beam Radiotherapy: An International Code of Practice for Dosimetry Based on Standards of Absorbed Dose to Water, Technical Reports Series No. 398 (Rev. 1) (IAEA, Vienna, 2024) | doi:10.61092/iaea.ve7q-y94k | full text | Sec. 2.1: traceability of user instruments to primary standards through PSDLs and SSDLs, and validation of primary standards by comparison. Secs. 3.1 and 3.2: calibration coefficient valid under reference conditions; influence quantities; beam quality correction factor rarely measurable directly, otherwise calculated. Sec. 4.4.2: stability, leakage, pre-irradiation, errors after polarity or voltage changes. Sec. 4.4.3: air density, humidity, electrometer, polarity and recombination corrections. Sec. 5.6.1: solid-state detectors only if verified against a reference chamber. Sec. 5.7 and Table 13: combined standard uncertainty of about 0.8% to 0.9% for cobalt-60 with an SSDL calibration |
| 8 | International Atomic Energy Agency (IAEA), Dosimetry of Small Static Fields Used in External Beam Radiotherapy: An International Code of Practice for Reference and Relative Dose Determination, Technical Reports Series No. 483 (IAEA, Vienna, 2017) | https://www-pub.iaea.org/MTCD/Publications/PDF/D483_web.pdf | full text | Sec. 1.1: small-field conditions (loss of lateral charged-particle equilibrium, source occlusion, detector size), corrections for large chambers excessive or unknown, spectrum changes with field size. Sec. 2.1.1.2: volume averaging and fluence perturbation. Sec. 2.3.2.1: uncorrected detector output ratios differed by about 15% between centres, and at least two detector types are advised. Sec. 4.2.1, Table 6: detector size chosen so that volume-averaging correction does not exceed 5% |
| 9 | S. Jonsson, J. Kastlander, T. Vidmar and H. Ramebäck, Experimental validation of corrections factors for γ–γ and γ–X coincidence summing of 133Ba, 152Eu, and 125Sb in volume sources, J. Radioanal. Nucl. Chem. 323, 465–472 (2020) | doi:10.1007/s10967-019-06938-3 | full text | Introduction: true coincidence summing grows as the source–detector distance decreases and, if uncorrected, can make the activity significantly too high or too low; correction codes treat summing and differences in attenuation between sample and calibration source; earlier comparisons found large discrepancies between codes for γ–X summing. Results and Conclusions: activities computed line by line were consistent with the source activity when the detector model was well optimised; a poorly known detector model gave inconsistent results |
