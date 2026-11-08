---
id: T-PRECISION-COLLIDER
name: Precision measurements at colliders
type: technique
field: physics/particle
applies_when: the paper reports a total, fiducial or differential cross section measured at a particle collider, corrects collider data for detector effects by unfolding, extracts a Standard Model parameter such as a mass or coupling from such data, or combines such measurements
version: "0.1"
---

# Precision measurements at colliders

## 1. Definition of the measured quantity

**Question.** Is the measured cross section defined at particle level, in terms of stable final-state particles within a stated fiducial region close to the detector acceptance, and does the paper say which corrections or extrapolations beyond that region it applies and what they depend on?

**Why it matters.** A quantity defined through the generator's parton-level history, or extrapolated into regions the detector did not observe, takes part of its value from the model used for the correction, so a later comparison with a different theory partly compares the model with itself. Subtracting irreducible backgrounds builds in the assumption that the SM predicts them correctly.

**Resolved by.** A fiducial definition in terms of final-state objects (for example, how leptons are dressed with photons and how jets are built), with selection cuts that match the detector-level selection closely; any extrapolation to a larger phase space given as a separate step with its own theory uncertainty; irreducible backgrounds either kept in the definition or subtracted at particle level, with the SM predictions used for the subtraction reported.

**Benchmark.** [1], [2]

## 2. Unfolding method and its model dependence

**Question.** Which unfolding method is used, how was the regularisation strength (or number of iterations) chosen, and does the paper show that the unfolded result does not depend on the MC model used to build the response matrix?

**Why it matters.** Simple bin-by-bin correction factors depend strongly on the simulated distribution and give biased results. Unregularised matrix inversion is unbiased but gives large, oscillating, strongly anti-correlated bins, and regularisation reduces that variance only by pulling the result towards a reference distribution, often the MC truth. Tests on pseudo-data drawn from the same model as the response matrix do not reveal this bias.

**Resolved by.** The method named and its regularisation parameter given with the criterion used to choose it; closure tests with pseudo-data from modified or alternative truth distributions, and the resulting bias included in the uncertainty; the response matrix with its migrations, efficiencies and fake rates described; where useful, the detector-level data and response matrix also published so that a prediction can be folded instead.

**Benchmark.** [3], [2]

## 3. Correlations between bins and between distributions

**Question.** For differential results, does the paper give the full covariance or correlation matrix of the measured bins, statistical and systematic, and are comparisons with predictions made using it, not only the diagonal uncertainties?

**Why it matters.** Unfolding and shared systematic sources correlate neighbouring bins strongly, sometimes negatively, so a chi-squared or a visual comparison that uses only the error bars can give a misleading level of agreement. Without the correlations, a measurement cannot be combined correctly with other distributions or used in a global fit.

**Resolved by.** The statistical covariance matrix of the unfolded bins and the signed shift of each systematic source, bin by bin, published in machine-readable form; agreement with predictions quoted as a chi-squared or likelihood that uses the full covariance; the predictions compared, with their uncertainties, also reported.

**Benchmark.** [2], [3], [12]

## 4. Definition of each systematic source

**Question.** Does the systematic uncertainty table say how each component was evaluated, in particular modelling uncertainties taken from alternative generators or settings, and does it separate genuine uncertainties from cross-checks?

**Why it matters.** Systematic and modelling uncertainties are usually defined as up and down shifts of a simulated distribution, applied one source at a time: the size of each shift is a choice, the interpolation between shifts is ambiguous, and one-at-a-time variations miss correlated effects. A passing cross-check, such as splitting the data, does not need to be added to the uncertainty, and doing so inflates it. A shift estimated from limited MC statistics is itself uncertain and can be mostly a statistical fluctuation.

**Resolved by.** Each source described with the variation applied and why it represents one standard deviation; the treatment of modelling comparisons stated, with their interpolation and extrapolation explained; the statistical precision of each estimated shift given or made negligible by enough simulation; cross-checks reported separately, with any difference compared with the uncertainty on the difference.

**Benchmark.** [4], [5]

## 5. Constrained nuisance parameters and the uncertainty breakdown

**Question.** When the result comes from a profile-likelihood fit, does the paper show how the data constrain and shift the nuisance parameters relative to their prior uncertainties, and is the reported breakdown into statistical and systematic components computed in a way that adds up to the total?

**Why it matters.** In a profile-likelihood fit the data can reduce a systematic uncertainty below its external estimate, and that reduction rests on how the systematic is parametrised, often by an interpolation between up and down templates that is itself ambiguous. The common impacts, obtained by fixing groups of nuisance parameters, do not add up to the total uncertainty and tend to understate the statistical part and overstate the systematic part, which matters when the result is later combined.

**Resolved by.** Post-fit values and uncertainties of the nuisance parameters shown and any strong constraint or shift explained; the parametrisation of each systematic stated, with checks that the fit is stable when it is varied; uncertainty components computed by a method that sums in quadrature to the total, or the post-fit covariance of the parameter of interest and the nuisance parameters given.

**Benchmark.** [5], [6]

## 6. Normalised distributions and the luminosity uncertainty

**Question.** For distributions normalised to their own integral, does the paper give a covariance that includes the effect of the normalisation and say how a goodness of fit should be computed with it; and for absolute cross sections, is the luminosity uncertainty listed as a separate component, with its correlation between data-taking periods?

**Why it matters.** Normalising a distribution cancels the luminosity and other overall normalisation uncertainties, but the bins then sum to a fixed value, so the covariance of all bins is singular and cannot be inverted for a chi-squared, and independently normalised distributions are not simple to combine. For absolute cross sections the luminosity uncertainty is often the leading systematic, it enters every result from the same data set in the same way, and some of its components are correlated between data-taking periods while others are not.

**Resolved by.** The normalisation procedure stated; the covariance of the normalised result given at a precision that allows it to be used, with explicit instructions for building a goodness-of-fit measure; correlations before normalisation also published where distributions may be combined; for absolute results, the luminosity value and uncertainty listed separately with the reference for its calibration, and the correlation of its components between periods stated when periods are combined.

**Benchmark.** [2], [7]

## 7. Theory inputs and the meaning of extracted parameters

**Question.** Which PDF sets, value of the strong coupling, perturbative order, scale choices and non-perturbative corrections enter the predictions or the parameter extraction, how are their uncertainties evaluated, and in which theoretical scheme is any extracted parameter defined?

**Why it matters.** PDF uncertainties from one group's set can underestimate the total, and the uncertainty from missing higher orders is usually estimated by varying scales by a conventional factor of two, which has no probabilistic meaning and can be too small when a coefficient happens to be small. An extracted parameter is correlated with the PDFs used to extract it, and a prediction that uses one strong-coupling value in the PDFs and another in the partonic calculation is inconsistent. A parameter fitted with MC templates is the generator's parameter, and relating it to a scheme defined in field theory needs extra theory input and uncertainty.

**Resolved by.** The PDF sets and strong-coupling value named, with PDF uncertainties evaluated by the set's own prescription; individual PDF sets, not only a combined set, used where the aim is to test the SM or extract its parameters, with the dependence of the result on the set shown; the same strong-coupling value used in the PDFs and in the partonic calculation; the scale-variation prescription stated and the theory uncertainty shown next to the experimental one; the scheme of any extracted mass or coupling stated, with the uncertainty of relating a generator parameter to it.

**Benchmark.** [8], [9], [10]

## 8. Combination with other results

**Question.** When the result is combined with other measurements, does the paper state the correlation assumed for each shared source, show how sensitive the combined value and uncertainty are to those assumptions, and report how much each input contributes?

**Why it matters.** The combined value and its uncertainty depend on the assumed correlations, and in the high-correlation regime assuming full correlation is not conservative: it can shrink the combined uncertainty and produce negative weights. Combining published profile likelihoods without separating their constraint terms counts common systematic sources twice, and symmetric Gaussian approximations fail where uncertainties are not Gaussian, as in the tails of distributions.

**Resolved by.** A table of systematic sources with the correlation assumed between inputs and its justification; the combination repeated with alternative correlation assumptions; information weights or equivalent measures of each input's contribution, with negative weights explained; where possible, a combination at the level of full statistical models with shared nuisance parameters identified, or decomposed uncertainty components that add up to the total.

**Benchmark.** [11], [12], [6]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | C. Bierlich et al., Robust Independent Validation of Experiment and Theory: Rivet version 3, SciPost Phys. 8, 026 (2020); read as arXiv:1912.05451 | doi:10.21468/SciPostPhys.8.2.026 |
| 2 | W. Abdallah et al., Reinterpretation of LHC Results for New Physics: Status and Recommendations after Run 2, SciPost Phys. 9, 022 (2020); read as arXiv:2003.07868 | doi:10.21468/SciPostPhys.9.2.022 |
| 3 | S. Schmitt, Data Unfolding Methods in High Energy Physics, EPJ Web Conf. 137, 11008 (2017); read as arXiv:1611.01927 | doi:10.1051/epjconf/201713711008 |
| 4 | R. Barlow, Systematic Errors: Facts and Fictions, Manchester report MAN/HEP/2002/1, arXiv:hep-ex/0207026 (2002) | doi:10.48550/arXiv.hep-ex/0207026 |
| 5 | K. Cranmer, Practical Statistics for the LHC, lectures at the 2011 European School of High-Energy Physics, CERN-2014-003, pp. 267–308; read as arXiv:1503.07622 (2015) | doi:10.48550/arXiv.1503.07622 |
| 6 | A. Pinto et al., Uncertainty components in profile likelihood fits, Eur. Phys. J. C 84, 593 (2024); read as arXiv:2307.04007 | doi:10.1140/epjc/s10052-024-12877-5 |
| 7 | CMS Collaboration (A. M. Sirunyan et al.), Precision luminosity measurement in proton-proton collisions at 13 TeV in 2015 and 2016 at CMS, Eur. Phys. J. C 81, 800 (2021); read as arXiv:2104.01927 | doi:10.1140/epjc/s10052-021-09538-2 |
| 8 | J. Butterworth et al., PDF4LHC recommendations for LHC Run II, J. Phys. G 43, 023001 (2016); read as arXiv:1510.03865 | doi:10.1088/0954-3899/43/2/023001 |
| 9 | M. Cacciari and N. Houdeau, Meaningful characterisation of perturbative theoretical uncertainties, JHEP 09 (2011) 039; read as arXiv:1105.5152 | doi:10.1007/JHEP09(2011)039 |
| 10 | A. H. Hoang, What Is the Top Quark Mass?, Annu. Rev. Nucl. Part. Sci. 70, 225 (2020); read as arXiv:2004.12915 | doi:10.1146/annurev-nucl-101918-023530 |
| 11 | A. Valassi and R. Chierici, Information and treatment of unknown correlations in the combination of measurements using the BLUE method, Eur. Phys. J. C 74, 2717 (2014); read as arXiv:1307.4003 | doi:10.1140/epjc/s10052-014-2717-6 |
| 12 | K. Cranmer et al., Publishing statistical models: Getting the most out of particle physics experiments, SciPost Phys. 12, 037 (2022); read as arXiv:2109.04981 | doi:10.21468/SciPostPhys.12.1.037 |
