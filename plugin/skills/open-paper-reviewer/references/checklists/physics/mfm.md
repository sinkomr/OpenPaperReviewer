---
id: T-MFM
name: Magnetic force microscopy (MFM)
type: technique
field: physics
applies_when: the paper shows magnetic force microscopy images or data, or bases a claim about magnetic domains, spin textures, stray fields or the magnetic character of a nanoscale object on them
version: "0.1"
---

# Magnetic force microscopy (MFM)

MFM is used to claim the presence, shape, size and field response of magnetic domains, domain walls and spin textures such as vortices and skyrmions, and to assign magnetic character to nanoscale objects. With a calibrated tip it is also used to report stray-field values.

## 1. Stray field or magnetisation

**Question.** Does the paper distinguish the recorded signal, a cantilever phase or frequency shift proportional to the gradient of the tip–sample force, from the magnetisation pattern it infers, and say how the inference was made?

**Why it matters.** The magnetic part of the signal is the stray field of the sample, mainly its out-of-plane component, differentiated and convolved with the magnetisation distribution of the tip. A stray-field image does not in general determine the magnetisation uniquely, so more than one magnetisation pattern can be consistent with the same image.

**Resolved by.** The paper describes the contrast as stray-field contrast, tests candidate magnetisation patterns by comparing the simulated signal, tip response included, with the measured one, and brings in an independent magnetic measurement where the assignment depends on it.

**Benchmark.** [1], [3]

## 2. Topographic cross-talk

**Question.** Is each magnetic image shown with the topography recorded in the same scan, and does the paper show that the features it calls magnetic are not reproduced from topographic features such as particles, edges or steps?

**Why it matters.** The lifted second pass senses all longer-range tip–sample forces, not only the magnetic one, and a feature in the topography can produce contrast in the magnetic channel. An error in the lift height on a scan line changes the size of the signal on that line.

**Resolved by.** Topography and magnetic channels are shown together with the lift height stated. The magnetic contrast does not follow the topography, persists when the lift height is changed, and responds to a reversal of the tip magnetisation or to an applied field in the way a magnetic signal should.

**Benchmark.** [1], [2], [4]

## 3. Electrostatic forces

**Question.** Does the paper exclude or compensate electrostatic tip–sample forces, in particular where the sample is electrically heterogeneous, for example nanostructures or particles on a substrate?

**Why it matters.** At typical lift heights electrostatic and magnetic forces can be of similar size. Contact-potential differences and fixed charge vary across a heterogeneous sample and give contrast that resembles magnetic contrast and is hard to separate from it, and a single fixed tip bias cannot cancel it everywhere. The effect weighs most for samples with a small magnetic moment.

**Resolved by.** The paper shows at least one of: Kelvin-probe compensation of the local potential during the magnetic scan; the dependence of the signal on tip bias; difference images taken with reversed or removed tip magnetisation; or a change of the contrast with applied magnetic field that identifies it as magnetic.

**Benchmark.** [1], [2], [6]

## 4. Tip–sample perturbation

**Question.** Does the paper show that the stray field of the tip did not change the magnetic state being imaged, and that the magnetisation of the tip stayed fixed during the scan and under any applied field?

**Why it matters.** The tip field can alter the micromagnetic state of the sample, nucleate or move objects such as vortices and skyrmions, and align superparamagnetic particles, so an image may show a state that the measurement produced. The stray field of the sample or an applied field can in turn switch the tip, which inverts the contrast along whole scan lines.

**Resolved by.** The tip coating or moment is stated and matched to the sample, with a reduced-moment tip where the tip field could change the sample. Successive scans of the same area reproduce the pattern, the tip coercivity is given relative to the applied fields, and line-by-line contrast inversions are absent or reported.

**Benchmark.** [1], [2], [4], [6]

## 5. Spatial resolution and feature size

**Question.** Are the sizes the paper reports, such as domain-wall widths, skyrmion or bubble diameters and particle sizes, resolved by the tip at the lift height used, or obtained from a model that includes the tip response?

**Why it matters.** The image is the stray field blurred by the extended magnetisation distribution of the tip, and the tip response depends on the spatial wavelength of the field pattern. Resolution worsens as the magnetic volume of the tip and the tip–sample distance increase, so sizes read directly from an image can differ from the true ones.

**Resolved by.** The paper states the tip type and lift height, gives the resolution under those conditions, for example from a reference sample or a tip transfer function, and derives sizes by fitting a model of the signal that includes the tip.

**Benchmark.** [1], [2], [3], [4]

## 6. Quantitative values

**Question.** If the paper reports stray-field values, magnetic moments or other numbers derived from MFM, was the tip calibrated under the measurement conditions, and is an uncertainty given?

**Why it matters.** Uncalibrated MFM data are qualitative, because the signal depends on the particular tip, its magnetic state and the measurement conditions. Point-probe models of the tip neglect its finite extent.

**Resolved by.** The paper describes the calibration, for example a tip transfer function obtained from a reference sample with a calculable stray field and measured with the same tip, lift height and resolution as the sample, or a direct measurement of the tip field. It reports the uncertainty that results.

**Benchmark.** [1], [3], [4], [5]

## 7. Deconvolution and image processing

**Question.** Does the paper state every processing step applied to the MFM data, including line corrections, filtering and any deconvolution with its regularisation parameter and window, and show that its conclusions do not depend on these choices?

**Why it matters.** Recovering a field map or a tip response by deconvolution is an ill-posed problem that is sensitive to noise. The regularisation parameter trades noise against blurring, and no rule for choosing it works in all cases. Scan-line defects and the way they are corrected also change the result.

**Resolved by.** Unprocessed images are provided next to processed ones. The regularisation criterion is stated and the result is shown to be stable when the parameter is varied, line defects are reported with the correction used, and where possible the result is checked by forward modelling of the signal from a candidate structure.

**Benchmark.** [1], [4], [5]

## 8. Reporting and reproducibility

**Question.** Does the paper report the probe and how it was magnetised, the lift height, the oscillation amplitude, the detected signal and the environment for each image, and show that the main observation is reproduced with another tip or sample area?

**Why it matters.** The signal depends on the magnetisation distribution of the tip, the tip–sample distance and the oscillation amplitude, so images taken under unreported conditions cannot be compared or repeated. Ambiguity about input parameters and measurement procedure has been identified as an obstacle to consistent quantitative results.

**Resolved by.** The methods give these parameters for every image, and the key result is shown with more than one tip or region, or is supported by a measurement on a reference sample under the same conditions.

**Benchmark.** [1], [4], [5]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | D. V. Christensen, U. Staub, T. R. Devidas et al. (53 authors), 2024 roadmap on magnetic microscopy techniques and their applications in materials science, J. Phys. Mater. 7, 032501 (2024); read as preprint arXiv:2401.04793 | doi:10.1088/2515-7639/ad31b5 | full text | Section "Magnetic Force Microscopy" (H. J. Hug et al.; Sec. 4 of the preprint), "Current State of the Technique" with Fig. 1: the signal is the stray-field derivative convolved with the tip magnetisation and stays qualitative without calibration; more magnetic tip volume costs resolution and can alter the sample state; a topographic feature also appears in the magnetic channel. "Future Advances of the Technique": Kelvin-probe and differential imaging separate contrast contributions; deconvolution needs high signal-to-noise data; candidate structures are tested by simulating the signal. Section on scanning SQUID microscopy (Sec. 1 of the preprint), "Probing magnetic materials": a stray-field image has no unique magnetisation solution |
| 2 | M. Jaafar, O. Iglesias-Freire, L. Serrano-Ramón, M. R. Ibarra, J. M. de Teresa, A. Asenjo, Distinguishing magnetic and electrostatic interactions by a Kelvin probe force microscopy–magnetic force microscopy combination, Beilstein J. Nanotechnol. 2, 552–560 (2011) | doi:10.3762/bjnano.2.59 | full text | Introduction and section "Tip–sample interactions" with Table 1: at lift heights of a few tens of nm van der Waals forces are negligible while electrostatic and magnetic forces are comparable; on heterogeneous samples a fixed bias cannot cancel the electrostatic force, and Kelvin-probe compensation or the field dependence of the signal is needed, above all for low-moment samples; a small tip–sample distance improves resolution and sensitivity. "Results and Discussion": tip coating and coercivity chosen so that tip and sample do not disturb each other |
| 3 | IEC TS 62607-9-1:2021, Nanomanufacturing – Key control characteristics – Part 9-1: Traceable spatially resolved nano-scale stray magnetic field measurements – Magnetic force microscopy, edition 1.0 (International Electrotechnical Commission, 2021) | https://webstore.iec.ch/en/publication/31932 | abstract | Abstract on the IEC webstore page: a standardised MFM method for spatially varying magnetic fields on flat specimens; MFM mainly detects the stray-field component perpendicular to the surface; resolution down to 10 nm relies on calibrating the tip with nanostructured reference materials |
| 4 | D. Nečas, P. Klapetek, V. Neu, M. Havlíček, R. Puttock, O. Kazakova, X. Hu, L. Zajíčková, Determination of tip transfer function for quantitative MFM using frequency domain filtering and least squares method, Sci. Rep. 9, 3880 (2019) | doi:10.1038/s41598-019-40477-x | full text | Introduction: contrast follows the tip–sample force gradient and depends on the magnetic state of both; the tip transfer function is obtained from a reference sample with calculable stray field and is specific to the probe; deconvolution is more noise-sensitive than forward modelling. "Optimal Regularisation Parameter": no selection method works in all cases. "Ideal Image Estimation and Instrumentation Errors": tip switching and lift-height errors give scan-line defects. Conclusion: recommended practice for measurement and reporting |
| 5 | X. Hu, G. Dai, S. Sievers, A. Fernández-Scarioni, H. Corte-León, R. Puttock, C. Barton, O. Kazakova, M. Ulvr, P. Klapetek, M. Havlíček, D. Nečas, Y. Tang, V. Neu, H. W. Schumacher, Round robin comparison on quantitative nanometer scale magnetic field measurements by magnetic force microscopy, J. Magn. Magn. Mater. 511, 166947 (2020) | doi:10.1016/j.jmmm.2020.166947 | abstract | Abstract: uncalibrated MFM gives qualitative data; the transfer-function calibration accounts for the finite extent of the tip, unlike point-probe models, but is ill-posed, needs regularisation with further parameters and has been held back by ambiguous input parameters and procedure; a measurement guideline was tested in a comparison between four laboratories |
| 6 | L. Angeloni, D. Passeri, M. Reggente, D. Mantovani, M. Rossi, Removal of electrostatic artifacts in magnetic force microscopy by controlled magnetization of the tip: application to superparamagnetic nanoparticles, Sci. Rep. 6, 26293 (2016) | doi:10.1038/srep26293 | full text | Abstract and Introduction: nanomaterials on a substrate give electrostatic contrast, from fixed charge and topography-dependent capacitive coupling, that is hard to separate from magnetic contrast; a fixed bias works only for homogeneous samples; images with reversed or removed tip magnetisation separate the two if the sample is unaffected by the fields involved. Conclusions: the tip field fully aligned superparamagnetic particles |
