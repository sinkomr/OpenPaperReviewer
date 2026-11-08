---
id: T-SCANNING-PROBE
name: Scanning probe microscopy
type: technique
field: physics/condensed-matter
applies_when: the paper shows atomic force microscopy topography, magnetic force, Kelvin probe force, piezoresponse force or conductive atomic force microscopy data, or bases a claim about feature size, layer thickness, magnetic domains, surface potential, ferroelectricity or local conductivity on them
version: "0.1"
---

# Scanning probe microscopy

## 1. Tip shape and lateral dimensions

**Question.** When the paper reports lateral sizes, widths, spacings or shapes of features from AFM images, does it state the tip radius, and say whether and how the values were corrected for the shape of the tip?

**Why it matters.** An AFM image is the surface dilated by the tip, so features comparable in size to the tip appear wider and with gentler slopes, and narrow gaps or the bases of steep walls that the tip cannot reach do not appear at all. Lateral sizes of small particles read directly from images can be much larger than the real ones, while the height of an isolated particle on a flat substrate is not affected by the tip shape.

**Resolved by.** The tip type and radius stated, and the tip shape characterised, for example by blind estimation from the images or on a tip-characterisation sample, wherever sizes carry the claim; sizes of small objects taken from heights, or corrected by a model of the tip, with uncorrected lateral values presented as upper limits; for densely packed or aggregated particles, a size method suited to that case with its uncertainty estimated.

**Benchmark.** [1], [2]

## 2. Heights of thin layers and soft objects

**Question.** Where a thickness, layer number or step height is derived from AFM heights, in particular for a thin layer on a different substrate or for a soft object, does the paper state the imaging mode, setpoint and force, and show that the height does not depend on them?

**Why it matters.** The apparent height of one material on another includes differences in tip–sample interaction and in adsorbed layers, and depends on the feedback settings and the imaging force; reported thicknesses of a single graphene layer span roughly a factor of four for these reasons. Models that treat tip and sample as rigid do not hold for soft samples or very small objects that deform under the tip.

**Resolved by.** The mode, setpoint, imaging force and environment stated; heights measured at more than one setpoint or force, or between layers of the same material as well as between layer and substrate; heights taken from histograms or averages over an area, not from a single line profile; for soft objects, an estimate of the deformation at the force used.

**Benchmark.** [2], [3]

## 3. Topography in the signal channel

**Question.** Is each MFM, KPFM or PFM map shown together with the topography recorded in the same scan, with the lift height or mode stated, and does the paper show that the features it interprets are not reproduced from topographic features such as particles, edges, steps or slopes?

**Why it matters.** A small particle in the topography can produce contrast in the lifted MFM channel. In KPFM, ac cross-talk makes the signal depend on the tip–sample distance and leaves topography-related footprints in the potential map, most of all in lift mode. In lateral PFM, surface slope, friction and contamination produce contrast unrelated to polarisation.

**Resolved by.** Topography and signal shown side by side, with line profiles through the interpreted features in both channels; contrast that persists where the topography is flat and responds to a change that should affect only the signal, such as reversing the tip magnetisation, applying a field or switching the polarisation; for KPFM, a detection mode less prone to cross-talk or a check of the dependence on tip–sample distance.

**Benchmark.** [4], [5], [6]

## 4. Electrostatic forces in magnetic force microscopy

**Question.** Does the paper exclude or compensate electrostatic tip–sample forces in its MFM data, in particular where the sample is electrically heterogeneous, for example nanostructures or particles on a substrate?

**Why it matters.** At lift heights of a few tens of nanometres, electrostatic and magnetic forces can be of similar size. Contact-potential differences and fixed charge vary across a heterogeneous sample and give contrast that resembles magnetic contrast, and a single fixed tip bias cannot cancel them everywhere. The effect weighs most for samples with a small magnetic moment.

**Resolved by.** At least one of: Kelvin-probe compensation of the local potential during the magnetic scan; the dependence of the signal on tip bias, which is parabolic for an electrostatic contribution; or difference images taken with reversed or removed tip magnetisation. A change of the contrast with applied magnetic field shows that part of it is magnetic, but does not remove the electrostatic part.

**Benchmark.** [4], [7], [8]

## 5. Magnetic contrast and tip perturbation

**Question.** Does the paper treat MFM contrast as a stray-field signal sensed by a magnetic tip, test any magnetisation pattern it infers against a simulated signal, and show that the tip did not create or change the magnetic state it images?

**Why it matters.** The magnetic signal is the derivative of the sample stray field, mainly its out-of-plane component, convolved with the magnetisation of the tip, so a magnetisation pattern is an inference that needs a model. A more magnetic tip gives a larger signal but lower resolution and a greater risk of altering the sample: tip fields can nucleate or move vortices and skyrmions and fully align superparamagnetic particles. An applied field or the sample's own field can in turn switch the tip, which inverts the contrast along whole scan lines.

**Resolved by.** Contrast described as stray-field contrast, with candidate magnetisation patterns compared through their simulated signal; the tip coating or moment stated and matched to the sample, with a low-moment tip where the tip field could change the state; the tip coercivity given relative to the applied fields; successive scans of the same area reproducing the pattern; line-by-line contrast inversions absent or reported.

**Benchmark.** [4], [7], [8], [9], [10]

## 6. Quantitative magnetic fields and surface potentials

**Question.** If the paper reports stray-field values, magnetic moments or sizes from MFM, or absolute surface potentials, work functions or potential differences from KPFM, how was the probe calibrated, which detection mode was used, and what uncertainty results?

**Why it matters.** Uncalibrated MFM is qualitative, because the signal depends on the particular tip and on the spatial wavelength of the field pattern. Calibration with a tip transfer function is specific to the probe and requires a regularised, ill-posed inversion whose parameter choice changes the result, and direct deconvolution of images is more sensitive to noise than forward modelling. KPFM measures a contact-potential difference to the tip, so absolute values depend on the tip and on surface contamination, and amplitude-modulated lift-mode KPFM averages the potential over the cantilever and tip cone and can report only part of a real potential step.

**Resolved by.** For MFM, a tip calibrated on a reference sample with a calculable stray field, measured with the same tip, lift height and resolution as the sample, with the regularisation criterion and the resulting uncertainty stated, or a comparison with simulated signals. For KPFM, the detection mode stated, with frequency-modulated detection preferred for quantitative values; the method checked on a reference structure with a known potential difference; absolute work functions referred to a reference measured with the same tip; atmosphere and humidity stated.

**Benchmark.** [4], [9], [10], [11], [12]

## 7. Ferroelectricity from piezoresponse

**Question.** Where PFM phase contrast, written domains or local hysteresis loops are used to claim ferroelectricity or piezoelectricity, does the paper exclude non-piezoelectric sources of the response and support the claim with other measurements?

**Why it matters.** Electrostatic forces from surface charge, charge injection, ion migration, electrochemical reactions in the surface water layer and electrostriction can all produce hysteresis loops and long-lived written contrast in materials that are not ferroelectric. PFM is necessary but not sufficient to establish ferroelectricity, and the PFM amplitude is not a quantitative measure of piezoelectric coefficients except in limited geometries.

**Resolved by.** Contrast between domains of opposite polarisation and switching between them shown together, with images before and after poling, not hysteresis loops or written contrast alone; humidity stated or controlled, and electrostatic, charge-injection, ionic and electrochemical contributions considered for the material; structural, chemical or macroscopic electrical evidence for a polar phase from other techniques; piezoelectric coefficients quoted only with a calibration of the detection and a statement of its limits.

**Benchmark.** [6], [13]

## 8. Contact and tip condition in conductive AFM

**Question.** When C-AFM currents, current maps or local current–voltage curves are used to claim local conductivity, layer thickness, breakdown or switching, does the paper state the tip, cantilever stiffness, contact force, current limit and environment, and show that the tip stayed conductive throughout?

**Why it matters.** The current depends on the effective contact area, which is set by the contact force, the tip radius and the stiffness of the materials. Conductive tip coatings degrade under current, first raising the contact resistance and then losing conduction, and the intermediate state can give stable but misleading curves, such as an overestimated oxide thickness. In air, a water layer at the junction can add a gap that the applied force does not remove, and soft cantilevers can be unsuitable for quantitative current–voltage measurements.

**Resolved by.** The tip conductivity checked before and after the measurements, for example on a metal reference; spring constant, contact force and current compliance stated; atmosphere and humidity stated, with the bias polarity chosen to avoid local anodic oxidation; comparisons between samples made with the same tip, or with tips shown to agree; scans after measurement showing no damage to the sample.

**Benchmark.** [14]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | J. S. Villarrubia, Algorithms for scanned probe microscope image simulation, surface reconstruction, and tip estimation, J. Res. Natl. Inst. Stand. Technol. 102, 425 (1997) | doi:10.6028/jres.102.030 |
| 2 | P. Klapetek et al., Atomic force microscopy analysis of nanoparticles in non-ideal conditions, Nanoscale Res. Lett. 6, 514 (2011) | doi:10.1186/1556-276X-6-514 |
| 3 | C. J. Shearer et al., Accurate thickness measurement of graphene, Nanotechnology 27, 125704 (2016) | doi:10.1088/0957-4484/27/12/125704 |
| 4 | D. V. Christensen et al., 2024 roadmap on magnetic microscopy techniques and their applications in materials science, J. Phys. Mater. 7, 032501 (2024); read as preprint arXiv:2401.04793 | doi:10.1088/2515-7639/ad31b5 |
| 5 | S. Barbet et al., Cross-talk artefacts in Kelvin probe force microscopy imaging: A comprehensive study, J. Appl. Phys. 115, 144313 (2014) | doi:10.1063/1.4870710 |
| 6 | A. Gruverman et al., Piezoresponse force microscopy and nanoferroic phenomena, Nat. Commun. 10, 1661 (2019) | doi:10.1038/s41467-019-09650-8 |
| 7 | M. Jaafar et al., Distinguishing magnetic and electrostatic interactions by a Kelvin probe force microscopy–magnetic force microscopy combination, Beilstein J. Nanotechnol. 2, 552 (2011) | doi:10.3762/bjnano.2.59 |
| 8 | L. Angeloni et al., Removal of electrostatic artifacts in magnetic force microscopy by controlled magnetization of the tip: application to superparamagnetic nanoparticles, Sci. Rep. 6, 26293 (2016) | doi:10.1038/srep26293 |
| 9 | D. Nečas et al., Determination of tip transfer function for quantitative MFM using frequency domain filtering and least squares method, Sci. Rep. 9, 3880 (2019) | doi:10.1038/s41598-019-40477-x |
| 10 | IEC TS 62607-9-1:2021, Nanomanufacturing – Key control characteristics – Part 9-1: Traceable spatially resolved nano-scale stray magnetic field measurements – Magnetic force microscopy, edition 1.0 (International Electrotechnical Commission, 2021) | https://webstore.iec.ch/en/publication/31932 |
| 11 | X. Hu et al., Round robin comparison on quantitative nanometer scale magnetic field measurements by magnetic force microscopy, J. Magn. Magn. Mater. 511, 166947 (2020) | doi:10.1016/j.jmmm.2020.166947 |
| 12 | A. Axt et al., Know your full potential: Quantitative Kelvin probe force microscopy on nanoscale electrical devices, Beilstein J. Nanotechnol. 9, 1809 (2018) | doi:10.3762/bjnano.9.172 |
| 13 | R. K. Vasudevan et al., Ferroelectric or non-ferroelectric: Why so many materials exhibit "ferroelectricity" on the nanoscale, Appl. Phys. Rev. 4, 021302 (2017) | doi:10.1063/1.4979015 |
| 14 | L. Jiang et al., Understanding current instabilities in conductive atomic force microscopy, Materials 12, 459 (2019) | doi:10.3390/ma12030459 |
