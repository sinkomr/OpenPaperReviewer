---
id: T-IMAGE-ANALYSIS
name: Quantitative image analysis
type: technique
field: physics/methods
applies_when: the paper extracts numbers from images taken with an optical or electron microscope, camera or scanning probe, such as intensities, sizes, shapes, counts, areas, distances or lattice spacings, by correction, segmentation, thresholding, filtering or an automated or machine-learning pipeline
version: "0.1"
---

# Quantitative image analysis

Quantitative image analysis is used to claim intensities, sizes, shapes, counts, coverages, distances and spacings from images recorded by optical and electron microscopes, cameras and scanning probe microscopes (SPM). Each number depends on how the image was formed, corrected, calibrated and segmented, and on which parts of the sample were imaged.

## 1. Illumination, offset and background correction

**Question.** Does the paper say how the detector offset, uneven illumination or detector response across the field, and the background were corrected before intensities or objects were measured, and how the reference or correction images were obtained?

**Why it matters.** No imaging system illuminates or detects uniformly, so the same object gives a different reading at the centre and at the edge of the field, which affects intensities, segmentation and stitched mosaics. A flat-field reference that does not match the sample, or that was taken in another session, adds error instead of removing it, and a background taken far from the objects can differ from the background next to them.

**Resolved by.** The offset measured without light and subtracted; the flat-field method named, with references acquired in the same session or a correction estimated from the data of each batch; background estimated next to the measured objects; a check that the correction worked, such as a uniform reference image after correction or measured values that do not depend on position in the field.

**Benchmark.** [1], [2], [4], [5]

## 2. Linear range, saturation and file handling

**Question.** Were the images recorded within the linear range of the detector without saturated pixels in the regions measured, and were the measurements made on the original files rather than on copies that were display-adjusted, converted to another bit depth or saved with lossy compression?

**Why it matters.** A saturated pixel no longer reports the intensity, and leaving saturated regions out of the analysis biases it towards dimmer objects. Changes of display curve, bit-depth conversion, pseudo-colouring and lossy formats such as JPEG alter pixel values, and raising the bit depth after acquisition adds no information.

**Resolved by.** Exposure and gain chosen to avoid saturation, with the fraction of saturated pixels checked or reported; intensities measured on raw files kept in a lossless format; display adjustments used only for figures, applied in the same way to all images compared and stated in the legend.

**Benchmark.** [1], [3], [4]

## 3. Pixel calibration, sampling and resolution

**Question.** How was the pixel size calibrated, against which reference and at which magnification and instrument settings, is the sampling fine enough for the smallest feature measured, and are the claimed sizes and separations larger than the resolution of the instrument?

**Why it matters.** The nominal magnification of a microscope can be wrong by several per cent or more, can differ between the x and y directions and can jump between magnification ranges, so every length inherits the error. An image sampled more coarsely than about half the resolution loses detail and can alias, and a feature only a few pixels across cannot be sized reliably.

**Resolved by.** Calibration against a certified scale, grating or known lattice spacing at the settings used, with its uncertainty, and x and y checked separately; pixel size and instrument resolution both stated; the smallest measured feature spanning several pixels; sizes and separations close to the resolution limit stated as such.

**Benchmark.** [1], [2], [3], [6]

## 4. Scanned images: drift, scan lines and probe shape

**Question.** For images built up line by line, as in scanning probe and scanning electron microscopy, does the paper show that drift, scan-line offsets, levelling and the size and shape of the probe have not distorted the distances, angles, heights or shapes being measured?

**Why it matters.** Drift during a scan acts mainly along the slow scan direction and appears as shear, stretching or streaks, which are amplified in strain maps obtained by differentiation. Row alignment and polynomial levelling can remove or alter real features, and background filters remove features larger than their kernel. A probe of finite size broadens features, and where it touches the surface at more than one point the image no longer follows the surface.

**Resolved by.** Scan direction, scan rate and image size stated; images with different scan directions, for example orthogonal pairs, compared or used to correct drift; distortion checked on a known lattice or reference; the levelling and row-alignment method named, with large features masked during fitting; lateral sizes compared with an independently characterised or reconstructed probe shape, and regions where the probe could not follow the surface identified.

**Benchmark.** [7], [8]

## 5. Processing that changes intensities or creates features

**Question.** Were filtering, Fourier masking, deconvolution, denoising or learned restoration applied before measurement or to the images shown, and does the paper show that the features and values claimed are not produced or changed by that processing?

**Why it matters.** Restoration and image-to-image methods based on deep learning add information taken from their training data and can create structures that are hard to detect, and intensities after non-linear denoising may not be quantitative. Not every deconvolution method preserves intensities, and smoothing or background filters remove features on some length scales while keeping others.

**Resolved by.** Each filter or restoration step named with its parameters, and its length scale compared with the size of the features measured; for learned restoration, validation against matched ground-truth images, such as high signal-to-noise acquisitions, with error maps; intensities measured on images not passed through non-linear restoration; new or unexpected features confirmed in the unrestored data or by another method.

**Benchmark.** [1], [8], [9]

## 6. Segmentation and thresholding

**Question.** How were objects separated from the background (algorithm, threshold value or rule, size and shape filters, how touching objects were split, how objects cut by the image border were treated), and was the segmentation checked against a reference such as manual annotation or a sample of known size?

**Why it matters.** Different thresholding and segmentation methods give different outlines for the same image, and where the boundary is placed on a blurred edge sets the measured size, with errors that can depend on object size. Objects cut by the border are incomplete, and a minimum-size filter removes small objects from the distribution. Parameters tuned by eye on the same images that are then analysed can fit those images and not others.

**Resolved by.** The full segmentation recipe stated, with thresholds set by a rule fixed before analysis; the segmentation compared with manual annotation or a reference material, with an agreement measure such as precision, recall or overlap; the treatment of border-touching and small objects stated; for sizes near the resolution limit, a boundary definition justified by how the image is formed.

**Benchmark.** [2], [4], [8], [9], [10]

## 7. Choice of fields of view

**Question.** How were the imaged fields, regions or objects chosen, how many fields and objects were analysed from how many samples, and were the rules for choosing and discarding images set before acquisition?

**Why it matters.** Choosing fields by eye tends to favour those that look good, and a few fields may not represent a sample that varies across its area. Images discarded for blur, saturation or artefacts after their content has been seen can shift the result.

**Resolved by.** Fields chosen by a predetermined rule, at random or automated positions, or by imaging the whole sample in tiles; acquisition or analysis done without knowing the sample identity where practical; the numbers of fields, objects and samples stated; quality criteria for discarding images, such as focus and saturation measures, defined in advance and the number discarded reported.

**Benchmark.** [2], [3], [4]

## 8. Automated and learned pipelines

**Question.** For an automated or machine-learning pipeline, are the software version, parameters and any trained model with its training data identified, and was the pipeline validated on images not used to develop or train it, including images from other sessions, batches or instruments?

**Why it matters.** Different tools and versions apply different steps and can give different results from the same images. A trained model generally performs well only on images similar to its training data, and corrections or classifiers set up on one batch may not transfer to another, so technical differences between batches can appear as differences between samples.

**Resolved by.** Software, versions, parameters and custom scripts stated and archived; for learned models, the training data described and deposited, and the validation metric, score and number of evaluation images reported, with evaluation images kept out of training; the same pipeline applied unchanged to all conditions compared; performance checked for each batch or instrument.

**Benchmark.** [2], [4], [9]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | J. C. Waters, Accuracy and precision in quantitative fluorescence microscopy, J. Cell Biol. 185, 1135–1148 (2009); read via Europe PMC (PMC2712964) | doi:10.1083/jcb.200903097 | full text | "Non-uniform illumination": uneven illumination makes equal concentrations read differently; divide by an image of a uniform sample, collected again each session. "Background fluorescence reduces dynamic range": subtract background measured next to the object. "The detector": saturated pixels cannot be used and cropping them out biases selection. "Resolution in the digital image": pixel size well below the optical resolution so small objects span several pixels. "Image processing and storage": bit-depth conversion, pseudo-colour and lossy compression alter intensities, and not all deconvolution suits quantitation |
| 2 | A. P.-T. Jost and J. C. Waters, Designing a rigorous microscopy experiment: validating methods and avoiding bias, J. Cell Biol. 218, 1452–1466 (2019); read via Europe PMC (PMC6504886) | doi:10.1083/jcb.201812109 | full text | "Nonuniform illumination" and Fig. 4: flat-field division, an inaccurate flat-field adds error; camera offset measured without light and subtracted. Table 2: magnification and pixel size checked with a stage micrometer. "Experimenter bias" and "Strategies to reduce bias": fields chosen because they look good bias results; automated or predetermined field selection and blinding; criteria for skipping fields set in advance. "Measurement validation": validate analysis on known data and do not tune parameters on the data to be analysed. "Methods reporting": software versions and settings reported |
| 3 | J.-Y. Lee and M. Kitaoka, A beginner's guide to rigor and reproducibility in fluorescence imaging experiments, Mol. Biol. Cell 29, 1519–1525 (2018); read via Europe PMC (PMC6080651) | doi:10.1091/mbc.E17-05-0276 | full text | Introduction and "Bias in experimental design": choice of region of interest affects reproducibility; random or predetermined positions, tiling the whole well, coded samples. "Rigor in image acquisition" and Fig. 2: Nyquist sampling at least twice the resolution, undersampling aliases; avoid saturation; raising bit depth after acquisition does not improve images. "Common obstacles during image processing": changing display curves or saving as JPEG alters raw values; analyse the raw file |
| 4 | J. C. Caicedo et al., Data-analysis strategies for image-based cell profiling, Nat. Methods 14, 849–863 (2017); read via Europe PMC (PMC6871000) | doi:10.1038/nmeth.4397 | full text | Step 1, "Field-of-view illumination correction": uneven illumination corrupts segmentation and intensities; prospective references often incomplete; compute corrections per batch. Step 1, "Segmentation": parameters tuned by visual inspection, labelled ground truth for assessment. Step 2, "Image quality control": blur and saturated-pixel measures, thresholds set from their distributions. Step 3: batch effects from technical variation can lead to false conclusions |
| 5 | T. Peng, K. Thorn, T. Schroeder, L. Wang, F. J. Theis, C. Marr and N. Navab, A BaSiC tool for background and shading correction of optical microscopy images, Nat. Commun. 8, 14836 (2017); read via Europe PMC (PMC5472168) | doi:10.1038/ncomms14836 | full text | Introduction: image model with multiplicative flat-field and additive dark-field; shading compromises quantitative analysis and mosaics. Results: correction changed single-cell quantification and removed stitching errors. Discussion: prospective references can mismatch the sample; background drifts over time |
| 6 | M. T. Postek, A. E. Vladár, S. N. Jones and W. J. Keery, Interlaboratory study on the lithographically produced scanning electron microscope magnification standard prototype, J. Res. Natl. Inst. Stand. Technol. 98, 447–467 (1993); read via Europe PMC (PMC4907700) | doi:10.6028/jres.098.033 | full text | Sec. 3 and Conclusion: magnification errors across many instruments, with large spread; jumps between magnification ranges; x and y calibrations often not equal; each instrument to be calibrated and rechecked regularly against a reference standard |
| 7 | C. Ophus, J. Ciston and C. T. Nelson, Correcting nonlinear drift distortion of scanning probe and scanning transmission electron microscopies from image pairs with orthogonal scan directions, Ultramicroscopy 162, 1–9 (2016); read as preprint arXiv:1507.00320, which carries a shorter title | doi:10.1016/j.ultramic.2015.12.002 | full text | Sec. 2.1: drift affects the slow scan direction much more strongly than the fast one. Sec. 2.2: linear drift is an affine distortion (shear, stretch); jumps and hysteresis displace scan lines. Sec. 3.3: streaks are especially pronounced in strain maps because differentiation magnifies noise. Method: orthogonal scan pairs used to correct the distortion |
| 8 | P. Klapetek, D. Nečas and C. Anderson, Gwyddion user guide, chapter 4, Data processing and analysis (online documentation, copyright 2004–2023) | https://gwyddion.net/documentation/user-guide-en/ | full text | "Data levelling and background subtraction": higher-degree levelling can suppress real features and alter statistics; arc, sphere and median backgrounds remove features larger than their radius or kernel. "Scan line artefacts": row alignment modifies data heavily and should be applied with care, using masks. "Grain analysis": threshold, Otsu and watershed marking; removing grains that touch the image edge. "Tip convolution artefacts": tip shape distorts images; certainty map marks where the tip touched at one point only |
| 9 | R. F. Laine, I. Arganda-Carreras, R. Henriques and G. Jacquemet, Avoiding a replication crisis in deep-learning-based bioimage analysis, Nat. Methods 18, 1136–1144 (2021); read via Europe PMC (PMC7611896) | doi:10.1038/s41592-021-01284-3 | full text | Introduction: models perform well mainly on images like their training data and can produce artefacts that are hard to identify. "Assessing DL model predictions" and Box 1: validate against ground truth with error maps; segmentation metrics such as IoU and F1. "Concluding remarks": image restoration is prone to undetected artefacts because it adds information from training data; absolute intensities after denoising may not be quantifiable. "Reporting the use of DL in publications": tool and version, training data, hyperparameters, validation metric, score and evaluation images kept out of training |
| 10 | L. Crouzier, A. Delvallée, S. Ducourtieux, L. Devoille, C. Tromas and N. Feltin, A new method for measuring nanoparticle diameter from a set of SEM images using a remarkable point, Ultramicroscopy 207, 112847 (2019) | doi:10.1016/j.ultramic.2019.112847 | abstract | Abstract: simulations show that conventional boundary methods (active contour and binarisation at half maximum) give size-dependent errors in nanoparticle diameter from scanning electron microscope images; a boundary set from image formation reduced the uncertainty |
