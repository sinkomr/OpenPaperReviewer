---
id: T-XRD
name: X-ray diffraction
type: technique
field: physics/condensed-matter
applies_when: the paper identifies phases, reports lattice parameters, strain, crystallite size, phase fractions, texture or epitaxy, or refines a crystal structure, from X-ray diffraction data
version: "0.1"
---

# X-ray diffraction

## 1. Phase identification

**Question.** Is every observed peak assigned, and is every reflection of the claimed phase's reference pattern accounted for in position and relative intensity, with the reference entry identified?

**Why it matters.** A match on a few peaks can be consistent with more than one phase, and some phases give patterns that cannot be told apart once the peaks are broad. Weak unassigned peaks may indicate a second phase, a larger unit cell or a different space group from the one assumed.

**Resolved by.** A fully indexed pattern compared with a named database entry or with a pattern simulated from a cited structure; a stated reason for any missing, extra or mis-scaled peak; a complementary technique where diffraction alone cannot discriminate between candidates.

**Benchmark.** [1], [2]

## 2. Purity and absence of phases

**Question.** Where the paper claims a single-phase sample or the absence of a particular phase, does it state how much crystalline or amorphous material could be present without being detected?

**Why it matters.** Amorphous material gives no sharp peaks and can go unnoticed beside crystalline phases. Minor crystalline phases can lie below the noise, particularly when peaks are broad or counting statistics are poor, so a pattern without extra peaks sets only an upper bound that depends on the instrument and the sample.

**Resolved by.** A detection limit established for the instrument and counting conditions used, for instance with mixtures of known composition; data with enough signal-to-noise for weak peaks to be seen; a test for amorphous content using an internal standard or an independent technique.

**Benchmark.** [1], [4], [5]

## 3. Relative intensities: preferred orientation and particle statistics

**Question.** Where a conclusion rests on relative peak intensities, were preferred orientation and particle statistics tested for or controlled?

**Why it matters.** Non-random orientation of crystallites changes relative intensities and can resemble a second phase or a structural change. Too few diffracting crystallites, or a few large ones among small ones, give intensity errors that cannot be corrected during refinement. Orientation corrections applied in refinement are approximations.

**Resolved by.** Specimen preparation and geometry described and chosen to reduce orientation, for example a rotating capillary or a back- or side-loaded flat specimen; specimen rotation and a suitable particle size for particle statistics; the same material measured in more than one preparation where orientation is at issue; any orientation correction reported with its model and refined values.

**Benchmark.** [1], [2], [5]

## 4. Peak positions and lattice parameters

**Question.** Where a conclusion rests on peak positions or small peak shifts (lattice parameters, strain, composition), was the angular scale calibrated with a standard, and were specimen displacement and transparency accounted for?

**Why it matters.** In reflection geometry a displacement of the specimen surface by a few micrometres shifts the peaks measurably, and zero and displacement corrections correlate with the unit-cell parameters during refinement. Refinement uncertainties describe precision, so a lattice parameter can be quoted to more digits than its accuracy supports. Composition inferred from lattice parameters through Vegard's law adds the deviations of that empirical rule.

**Resolved by.** An internal standard mixed with the sample (an external standard corrects the instrument but not specimen displacement or transparency); the zero or displacement model stated; lattice parameters quoted to a precision consistent with the peak widths and the calibration; an independent composition measurement where Vegard's law is used.

**Benchmark.** [1], [2], [7]

## 5. Peak broadening: crystallite size and microstrain

**Question.** Where crystallite size or microstrain is derived from peak widths, was the instrumental broadening measured and removed, and is it stated how size and strain contributions were separated?

**Why it matters.** Instrument, crystallite size, strain and other defects all broaden peaks, and different analysis methods applied to the same data can return different size and strain values. The result is an apparent, weighted domain size along the diffraction vector: it is not the particle size, and it is not a simple mean unless shape and size distribution are known. For larger crystallites the instrument accounts for most of the width.

**Resolved by.** An instrument profile measured on a suitable standard; several reflections or the whole pattern analysed, not a single peak; the method and its assumptions (crystallite shape, size distribution, strain model) stated, along with the kind of average reported; microscopy used as a check on domain size against particle size.

**Benchmark.** [1], [4], [6]

## 6. Structure refinement: quality of the fit and of the model

**Question.** Where a structural model is refined against the data, does the paper show the fit and the plausibility of the refined model, and not only agreement indices?

**Why it matters.** Profile agreement indices depend on background level and data quality as well as on the model, so no threshold value separates a sound refinement from an unsound one. Least squares will refine more parameters than the data support, and the resulting standard uncertainties express precision only. In single-crystal work, errors such as missed symmetry, wrong atom types and misplaced hydrogen atoms occur in published structures and are not excluded by a low R factor.

**Resolved by.** For powder data: a plot of observed, calculated and difference profiles over the full range; the type of agreement index stated and compared with a structure-free fit; refined distances, displacement parameters and occupancies that are chemically reasonable; the number of refined parameters justified; the way uncertainties were calculated stated. For single-crystal data: a validation report with its alerts addressed, and deposited structure and reflection data.

**Benchmark.** [2], [3], [9]

## 7. Quantitative phase analysis

**Question.** Where phase fractions are reported, is their accuracy assessed beyond the standard uncertainties of the refinement, and were microabsorption, amorphous content and preferred orientation considered?

**Why it matters.** In inter-laboratory comparisons on mixtures of known composition, results varied widely between laboratories, and many were reported with no error estimate or with one derived only from the fit. Absorption contrast between phases (microabsorption) biases X-ray results, and a correction applied when none is needed makes them worse. Crystalline fractions normalised to 100 % say nothing about an amorphous component.

**Resolved by.** The method validated on a mixture of known composition or against an independent technique; absorption contrast and particle size assessed before any microabsorption correction is applied, and particle size reduced where needed; an internal standard where amorphous content is possible; an error estimate with its derivation; the refinement documented as in item 6.

**Benchmark.** [4], [5]

## 8. Thin films and other oriented samples

**Question.** For a thin film or other strongly oriented sample, is a claim about phase content, texture or epitaxy supported by more than a symmetric 2θ/ω scan?

**Why it matters.** A symmetric scan records only lattice planes parallel to the surface, so the peaks that appear depend on orientation as well as on the phases present. A single family of film reflections shows the out-of-plane orientation but not in-plane alignment. Weak additional peaks can arise from other wavelengths diffracting from strong film or substrate reflections, or from the sample mount.

**Resolved by.** Pole figures or azimuthal scans for in-plane orientation, and rocking curves for the spread of orientations; reciprocal-space maps or in-plane diffraction where a strain state is claimed; intensity plotted on a logarithmic scale; a scan of a bare substrate; lines from other wavelengths identified.

**Benchmark.** [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | C. F. Holder, R. E. Schaak, Tutorial on Powder X-ray Diffraction for Characterizing Nanoscale Materials, ACS Nano 13, 7359 (2019) | doi:10.1021/acsnano.9b05157 |
| 2 | L. B. McCusker et al., Rietveld refinement guidelines, J. Appl. Cryst. 32, 36 (1999) | doi:10.1107/S0021889898009856 |
| 3 | B. H. Toby, R factors in Rietveld analysis: How good is good enough?, Powder Diffr. 21, 67 (2006) | doi:10.1154/1.2179804 |
| 4 | I. C. Madsen et al., Outcomes of the International Union of Crystallography Commission on Powder Diffraction Round Robin on Quantitative Phase Analysis: samples 1a to 1h, J. Appl. Cryst. 34, 409 (2001) | doi:10.1107/S0021889801007476 |
| 5 | N. V. Y. Scarlett et al., Outcomes of the International Union of Crystallography Commission on Powder Diffraction Round Robin on Quantitative Phase Analysis: samples 2, 3, 4, synthetic bauxite, natural granodiorite and pharmaceuticals, J. Appl. Cryst. 35, 383 (2002) | doi:10.1107/S0021889802008798 |
| 6 | D. Balzar et al., Size–strain line-broadening analysis of the ceria round-robin sample, J. Appl. Cryst. 37, 911 (2004) | doi:10.1107/S0021889804022551 |
| 7 | J. P. Cline et al., The Optics and Alignment of the Divergent Beam Laboratory X-ray Powder Diffractometer and its Calibration Using NIST Standard Reference Materials, J. Res. Natl. Inst. Stand. Technol. 120, 173 (2015) | doi:10.6028/jres.120.013 |
| 8 | G. F. Harrington, J. Santiso, Back-to-Basics tutorial: X-ray diffraction of thin films, J. Electroceram. 47, 141 (2021) | doi:10.1007/s10832-021-00263-6 |
| 9 | A. L. Spek, Structure validation in chemical crystallography, Acta Cryst. D65, 148 (2009) | doi:10.1107/S090744490804362X |
