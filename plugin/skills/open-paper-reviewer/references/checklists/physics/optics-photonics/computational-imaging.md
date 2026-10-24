---
id: T-COMPUTATIONAL-IMAGING
name: Super-resolution and computational imaging
type: technique
field: physics/optics-photonics
applies_when: the paper claims resolution beyond the diffraction limit or a resolution gain, or bases images on structured illumination, single-molecule localisation, phase retrieval, regularised or learned reconstruction, or imaging through or inside scattering media such as tissue or diffusers
version: "0.1"
---

# Super-resolution and computational imaging

Super-resolution and computational imaging methods are used to claim images with detail finer than the diffraction limit of the optics, or images recovered from measurements that are not themselves images, such as speckle through a scattering medium. Examples are structured illumination microscopy (SIM), single-molecule localisation microscopy (SMLM), phase retrieval and coherent computational microscopy, and reconstructions that use a prior, a regularisation term or a trained neural network. The image is the output of an algorithm, so each claim depends on how resolution was defined and measured, on what the reconstruction adds or removes, and on tests against objects whose structure is known.

## 1. Resolution criterion and how it was measured

**Question.** Which criterion defines each quoted resolution (separation of two known features, width of a line profile, Fourier ring correlation (FRC) with a stated threshold, or the extent of the Fourier spectrum), on which object and data set was it measured, and at what signal level?

**Why it matters.** Different criteria give different numbers for the same image, and localisation precision, or the width of one isolated feature, which varies with contrast, is not the same as resolution. FRC needs a chosen threshold, can hide variation across the image, and reads too high when the two half-images share signal, for example from repeated localisations of the same molecule. Resolution also depends on the signal-to-noise ratio and on the labelling, so a value measured on a bright test sample may not hold for the data behind the claim.

**Resolved by.** The criterion named with its threshold or target; resolution measured on the data that carry the claim, or on a test object imaged under the same conditions and signal level; for FRC, half-images that are statistically independent, with any correction for repeated localisations stated; the spatial variation of resolution shown or discussed; two-point separations of features with known spacing where a specific resolution is claimed.

**Benchmark.** [1], [2], [3]

## 2. Reference for the resolution gain and the assumptions behind it

**Question.** Against what reference is a resolution gain stated (the diffraction limit computed for which numerical aperture, wavelength and type of illumination, or a conventional image of the same object), and does the paper state the assumptions about the object that the reconstruction relies on?

**Why it matters.** Resolution in coherent and computational imaging is defined and reported in inconsistent ways, so stated gains are often not comparable between papers, or even with the paper's own reference image. Linear structured illumination improves resolution by about a factor of two, so a larger gain from such a method depends on something more, such as a non-linear response or an assumption about the object. A gain that rests on such an assumption, for example sparsity, positivity or a bounded object, holds only for objects that meet it.

**Resolved by.** The numerical aperture, wavelength and illumination used for the reference limit stated, with the formula or the expected spatial-frequency coverage of the system; a conventional or deconvolved image of the same field acquired for comparison; a standard resolution target, such as a spoke pattern, imaged with the method; every prior assumption about the object listed alongside the resolution claim, with the range of objects for which it holds.

**Benchmark.** [3], [4]

## 3. Reconstruction artefacts of the method

**Question.** Does the paper check its reconstructions for the artefacts known for its method, and report the reconstruction parameters and quality measures that would reveal them?

**Why it matters.** Reconstruction can create structure that is not in the sample, such as side lobes and ringing next to bright features or reconstructed noise in regions of low modulation contrast, and it can remove, merge or brighten real structure. In SIM these follow from a mismatch between the optical transfer function used in the reconstruction and the real imaging conditions, often from spherical aberration caused by refractive index differences, from sample motion or uneven illumination between pattern angles, from bleaching, or from unsuitable reconstruction parameters such as the Wiener filter setting. In SMLM, errors concentrate where emitters are dense, and repeated blinking of one molecule creates clusters that are not present in the sample.

**Resolved by.** The reconstruction settings that govern these artefacts stated, such as the transfer function and filter setting used in SIM; method-specific quality measures reported, such as modulation contrast-to-noise and Fourier spectra of raw and reconstructed SIM data, or emitter density per frame, drift correction and the treatment of repeated localisations in SMLM; the reconstruction compared with a diffraction-limited image of the same field, for example as an error map, with regions of disagreement discussed.

**Benchmark.** [2], [4], [5]

## 4. Priors, regularisation and learned reconstructions

**Question.** What prior, regularisation term or trained model enters the reconstruction, how were its strength and parameters chosen, and for a trained model, what data was it trained on and how similar are they to the samples in the paper?

**Why it matters.** A reconstruction that uses a prior or a trained network can produce structure that reflects the prior or the training data rather than the sample, and such artefacts can be hard to identify. Trained models work well mainly on data like their training data, and a network trained on one scattering medium is sensitive to changes in that medium, so performance on new samples is uncertain unless tested.

**Resolved by.** The prior, constraint or regularisation term stated, with its weight and how that weight was chosen; the training data described (instrument, modality, sample type, signal level), with the model version and main settings; evaluation on data that were excluded from training and resemble the paper's samples; checks that the features carrying the claim are present in the raw data or in a reconstruction without the learned prior; for scattering media, tests on media not seen in training.

**Benchmark.** [3], [6], [7]

## 5. Validation against known structure

**Question.** Was the reconstruction tested on samples or simulations whose structure is known, under conditions matching the measurement (emitter density, signal level, thickness, scattering), and with a quantitative measure of agreement?

**Why it matters.** Without a known object, a reconstruction error cannot be told apart from real structure. A high resolution value does not ensure low error, since local resolution and local error can differ. Reconstruction programs also differ in performance on the same data, which is why community benchmarks use realistic simulated data with known ground truth.

**Resolved by.** Reference structures with known geometry, such as test targets or biological structures with well-characterised spacing, imaged with the method; simulated data with known ground truth generated at the density and signal level of the experiment; agreement given as a number, such as an error or correlation measure, with the reconstruction shown to be closer to ground truth than the raw input; where possible, an independent method of higher resolution applied to the same structures.

**Benchmark.** [2], [5], [6], [8]

## 6. Labelling and sampling of the structure

**Question.** In fluorescence super-resolution, is the density of labels or localisations high enough for the resolution claimed, and does the paper state the size of the labels, that is the distance between the fluorophore and the target molecule?

**Why it matters.** Resolution is limited by how densely the structure is sampled as well as by localisation precision, and a reanalysis of an early Nyquist-based sampling rule suggested that about five times denser sampling is needed. Labels displace the fluorophore from its target, by about 10 nanometres for an antibody and up to about 20 nanometres for a primary and secondary antibody pair, which matters when the claimed features are of similar size.

**Resolved by.** Label or localisation density stated and related to the claimed resolution, with an estimate of the fraction of targets detected; the labelling method and its linkage error stated and included in size and distance estimates; claimed features larger than the combined effect of precision, sampling and linkage error, or a discussion of why they are not.

**Benchmark.** [1], [2]

## 7. Imaging through or inside scattering media

**Question.** For imaging through or inside a scattering medium, does the paper state the depth or thickness in scattering and transport mean free paths for the actual sample, whether the medium was a thin diffuser, a phantom or tissue, the field of view against the memory-effect range, what guide star or feedback was used, and whether the medium stayed stable over the acquisition?

**Why it matters.** Unscattered light decays exponentially with depth, and the angular range over which one correction or speckle correlation holds (the memory effect) is inversely proportional to thickness, so the usable field of view shrinks in thick media. Living tissue can decorrelate within milliseconds, many demonstrations, especially of learning-based methods, use thin diffusers or static samples, and iterative phase retrieval can converge unstably. A method shown under easy conditions may not carry over to thick or changing media.

**Resolved by.** Depth and thickness given in mean free paths, with how these were measured; field of view stated against the memory-effect range, or the method used to join several patches; the guide star or feedback described, including whether it needs access to or labelling inside the sample; decorrelation time of the medium compared with acquisition time; tests on media representative of the intended use; for phase retrieval, repeated reconstructions from different starting points showing the same result.

**Benchmark.** [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | R. P. J. Nieuwenhuizen, K. A. Lidke, M. Bates, D. Leyton Puig, D. Grünwald, S. Stallinga and B. Rieger, Measuring image resolution in optical nanoscopy, Nat. Methods 10, 557–562 (2013); read as the author manuscript in PubMed Central, PMC4149789 | doi:10.1038/nmeth.2448 | full text | Introduction: localisation precision alone or labelling density alone does not measure resolution, which also depends on labelling, structure and processing. Main text: FRC from two statistically independent half-sets with a threshold of about 1/7; repeated localisations of one emitter correlate the halves and give too optimistic values, corrected with an estimated parameter Q; trade-off between labelling density and precision. Discussion: the measure depends on signal-to-noise ratio and spectral content |
| 2 | M. Lelek, M. T. Gyparaki, G. Beliu, F. Schueder, J. Griffié, S. Manley, R. Jungmann, M. Sauer, M. Lakadamyali and C. Zimmer, Single-molecule localization microscopy, Nat. Rev. Methods Primers 1, 39 (2021); read as the author manuscript in PubMed Central, PMC9160414 | doi:10.1038/s43586-021-00038-x | full text | Box 1: resolution limited by precision and by sampling density; a reanalysis of the early Nyquist criterion suggested about fivefold denser sampling; FRC needs a user-defined threshold and can hide spatial variation; nuclear pore complexes as a reference structure with known distances. Fluorescent labelling strategies: linkage error of about 10 nm for antibodies, about 20 nm with indirect labelling. Quantitative analyses: repeated blinking gives artefactual clusters and overcounting; overlapping emitters and drift as artefacts |
| 3 | R. Horstmeyer, R. Heintzmann, G. Popescu, L. Waller and C. Yang, Standardizing the resolution claims for coherent microscopy, Nat. Photonics 10, 68–71 (2016); read as the authors' manuscript posted by the Caltech Biophotonics Laboratory | doi:10.1038/nphoton.2015.279 | full text | Opening section: resolution in coherent imaging is defined and reported inconsistently, and noise affects resolution limits. "Standard part 1": report the expected non-zero spatial-frequency coverage of the system; reported distance metrics vary (half-pitch, edge-to-edge, width of a single feature, which varies with contrast). "Standard part 2": resolution beyond the physical limit by assuming a bounded sample, sparsity, positivity or a regularisation term; such a priori assumptions must be stated, with the samples to which the method applies. "Standard part 3": a spoke (Siemens star) target, with resolution reported at several positions across the field of view |
| 4 | G. Ball, J. Demmerle, R. Kaufmann, I. Davis, I. M. Dobbie and L. Schermelleh, SIMcheck: a toolbox for successful super-resolution structured illumination microscopy, Sci. Rep. 5, 15915 (2015); read in Europe PMC, PMC4648340 | doi:10.1038/srep15915 | full text | Opening section: linear SIM doubles conventional resolution laterally and axially. "Structured illumination data checks": side lobes and intensity dips around bright features indicate mismatch between the sample conditions and the optical transfer function, mostly from spherical aberration caused by depth and refractive index; sample motion, illumination variation between angles and bleaching checked in raw data; reconstructed noise where modulation contrast is low; sub-optimal reconstruction parameters diagnosed. Methods: modulation contrast-to-noise ratio, reconstructed Fourier plots and intensity histograms, with a suggested Wiener filter setting |
| 5 | S. Culley, D. Albrecht, C. Jacobs, P. M. Pereira, C. Leterrier, J. Mercer and R. Henriques, Quantitative mapping and minimization of super-resolution optical imaging artifacts, Nat. Methods 15, 263–266 (2018); read as the author manuscript in PubMed Central, PMC5884429 | doi:10.1038/nmeth.4605 | full text | Main text: reconstructions can lose, merge or brighten structures, with errors concentrated where emitters are dense; comparison with a diffraction-limited reference of the same field gives an error map and global scores; local FRC resolution does not track local error; artefacts below the reference resolution are not detected |
| 6 | R. F. Laine, I. Arganda-Carreras, R. Henriques and G. Jacquemet, Avoiding a replication crisis in deep-learning-based bioimage analysis, Nat. Methods 18, 1136–1144 (2021); read as the author manuscript in PubMed Central, PMC7611896 | doi:10.1038/s41592-021-01284-3 | full text | Figure 1 legend: a model performs well mainly on images similar to its training data. Figure 2 legend: when new data are not well represented in the training data, the model may generate artefacts and biases that are hard to identify. "Assessing DL model predictions": comparison with ground truth using error maps and similarity metrics; predictions should be closer to ground truth than the raw input; structures not easily visible in the raw data should be cross-validated. "Reporting the use of DL in publications": describe the training data, model version and main hyperparameters, and the validation, with evaluation data absent from training data |
| 7 | S. Gigan, O. Katz, H. B. de Aguiar, E. R. Andresen, A. Aubry et al., Roadmap on wavefront shaping and deep imaging in complex media, J. Phys. Photonics 4, 042501 (2022); read as the arXiv version, arXiv:2111.14908, whose section numbers are used here | doi:10.1088/2515-7647/ac76f9 | full text | Introduction: ballistic photons decay exponentially with depth. Sec. 6: guide stars needed to focus inside scattering media, each with its own access requirements; in vivo decorrelation time around 1 ms. Sec. 10: decorrelation times of 50 ms to 2.5 s in living tissue; learning-based experimental results so far only for thin diffusers. Sec. 12: a network trained on a fixed diffuser is susceptible to changes of the scattering medium. Sec. 14: memory-effect angular range inversely proportional to sample thickness, limiting field of view; convergence instability of iterative phase retrieval; acquisition must be shorter than decorrelation time |
| 8 | D. Sage, T.-A. Pham, H. Babcock, T. Lukes, T. Pengo, J. Chao, R. Velmurugan, A. Herbert, A. Agrawal, S. Colabrese et al., Super-resolution fight club: assessment of 2D and 3D single-molecule localization microscopy software, Nat. Methods 16, 387–395 (2019); read as the author manuscript in PubMed Central, PMC6684258 | doi:10.1038/s41592-019-0364-4 | full text | Results, "Realistic 3D simulations", and Methods 2.1: experimental data lack ground truth, so 36 software packages were assessed on realistic simulated data sets with known fluorophore positions at several densities and noise levels. Discussion: the choice of localisation software greatly affects the final image, and high-density 3D performance was mediocre at high and poor at low signal-to-noise ratio |
