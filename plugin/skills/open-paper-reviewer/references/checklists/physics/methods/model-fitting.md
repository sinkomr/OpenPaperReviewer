---
id: T-MODEL-FITTING
name: Fitting models to data
type: technique
field: physics/methods
applies_when: the paper fits a model, lineshape, set of peaks, decay or other function to data and bases a claim on the fitted parameters, on the number of components found, or on one model fitting better than another
version: "0.1"
---

# Fitting models to data

Fitting is used to claim values of physical parameters, such as peak positions, widths, areas, lifetimes and rates, to claim that a component such as an extra peak or decay is present, and to claim that one model describes the data better than another. Each of these depends on the model chosen, the error model assumed and the way the fit was carried out, as well as on the data.

## 1. Choice of model and number of components

**Question.** Is the functional form of the model, including the lineshape, the number of peaks or decay components and the background, stated in full and justified on physical grounds or by independent evidence, and is the number of free parameters matched to what the data can resolve?

**Why it matters.** A model with enough components will fit almost any data set, so a good fit alone does not show that each component is real. Two components can be separated only when they differ by more than a limit set by the signal-to-noise ratio, for decays a minimum ratio of time constants, so components closer than that are not determined by the data.

**Resolved by.** The complete model written out, with the physical origin of each component and the reason for the lineshape and background chosen; the separations between components compared with the resolution the noise allows; fewer components shown to fit worse, and more components shown not to be needed.

**Benchmark.** [1], [2]

## 2. Correlated and poorly determined parameters

**Question.** Does the paper report the correlations between fitted parameters, as a correlation matrix or joint confidence regions, and show that each parameter a claim rests on is determined by the data on its own and not only in combination with others?

**Why it matters.** In fits with many parameters, such as sums of exponentials or overlapping peaks, the data often fix a few combinations of parameters while individual parameters remain almost undetermined, even when the fit looks good. A parameter that trades off against another can take a wide range of values with almost no change in the fit, and a fit started from a different point can settle in a different minimum.

**Resolved by.** Correlation coefficients or joint confidence contours for the parameters that carry the claim; claims stated in terms of combinations the data determine when individual parameters are not; the fit repeated from several starting values, or the parameter space scanned, showing that the same minimum is reached.

**Benchmark.** [2], [3], [4]

## 3. Weighting and error model

**Question.** Which objective function and weights were used, and do they match the noise in the data: counting statistics for counted events, uncertainties that change across the range, uncertainties in the independent variable, and any scatter beyond the measurement errors?

**Why it matters.** Weighted least squares gives the best estimates only when the weights reflect the variance of each point and the errors are Gaussian and confined to the dependent variable, conditions rarely met in practice. For counted data such as spectra and decay histograms, least-squares approximations to the Poisson likelihood can bias peak areas, widths and other parameters, even at high counts.

**Resolved by.** The objective function and the weights stated; for counted data, a Poisson likelihood or a demonstration that the bias of the method used is small compared with the quoted uncertainty; weights taken from measured or modelled variances; uncertainties in the independent variable and any extra scatter included in the error model.

**Benchmark.** [1], [5], [6], [7]

## 4. Residuals and goodness of fit

**Question.** Are the residuals, preferably normalised by their uncertainties, shown across the whole fitting range, and is the quality of the fit judged by more than a single number such as a reduced chi-squared or a coefficient of determination?

**Why it matters.** Structure in the residuals shows a missing component, a wrong lineshape or an incorrect error model, and a high coefficient of determination does not by itself show that a model fits. The reduced chi-squared is itself noisy, especially for small data sets, and for a nonlinear model its number of degrees of freedom is not well defined.

**Resolved by.** A residual plot with each fit that carries a claim, over the stated fitting range; the distribution of normalised residuals compared with what the error model predicts; any structure in the residuals discussed, together with the effect of changing the fitting range.

**Benchmark.** [8], [9]

## 5. Comparing models and testing for an added component

**Question.** When a claim rests on one model being preferred, or on a component being present, which criterion or test was used to compare the models, and are its assumptions met?

**Why it matters.** Adding parameters improves the fit, so a lower minimum of the objective function does not on its own favour the larger model. The likelihood ratio and F tests do not follow their standard distributions when the simpler model sits on the boundary of the parameter space, as when testing whether a peak's amplitude is zero, so nominal false-positive rates can be wrong. Information criteria penalise extra parameters in different ways and can lead to different conclusions from the same data.

**Resolved by.** The criterion or test named, with its value for each model compared; for the presence of a component, a significance calibrated by simulation, such as a parametric bootstrap or posterior predictive check, instead of a standard table; the conclusion shown not to depend on the choice of criterion.

**Benchmark.** [9], [10], [11]

## 6. Fixed parameters, constraints and limits

**Question.** Which parameters were fixed, tied to others or bounded, at what values and on what basis, and does the paper show how the results change when those choices are changed?

**Why it matters.** Fixing a parameter removes its uncertainty from the fit, which in general makes the quoted uncertainties of the other parameters smaller, and fixing or bounding parameters also steers which minimum the fit reaches. A parameter that ends at a bound has no error in at least one direction, and the error matrix then means little.

**Resolved by.** A list of free, fixed, tied and bounded parameters, with the source of each fixed value; the headline parameters shown for a range of reasonable fixed values, or with the fixed parameters released or marginalised over; any parameter that reached a bound reported, with its effect on the result.

**Benchmark.** [1], [4]

## 7. How fitted uncertainties were obtained

**Question.** How were the uncertainties of fitted parameters obtained, by the covariance matrix, a profile of the likelihood or chi-squared, Monte Carlo simulation or resampling, and were any error bars rescaled to make the reduced chi-squared equal one?

**Why it matters.** Uncertainties from the covariance matrix include correlations but not nonlinearities, so they can misstate intervals that are asymmetric or not elliptical. Rescaling errors to make the reduced chi-squared equal one assumes that the model is correct and the errors Gaussian, and leaves the reader unable to separate a poor model from underestimated noise.

**Resolved by.** The method named for each quoted uncertainty, with the confidence level; asymmetric intervals from a likelihood profile or simulation where the likelihood is far from parabolic; a Monte Carlo or resampling check of the uncertainties of the headline parameters; any rescaling stated, with its factor and justification.

**Benchmark.** [1], [4], [12]

## 8. Instrument response and resolution

**Question.** Where the fitted widths, lifetimes or splittings are not much larger than the instrumental resolution or response time, was the model convolved with the instrument response, how was that response measured, and was its width fixed or fitted?

**Why it matters.** The measured signal is the true signal convolved with the instrument response, so fitting an unconvolved model to features close to the resolution returns widths or lifetimes that partly reflect the instrument. How short a lifetime or how narrow a feature can be measured depends on the response width and on the number of counts, and fitting the response width as a free parameter costs considerable precision.

**Resolved by.** The instrument response or resolution function stated, with how and when it was measured; fits carried out by convolving the model with that response; the fitted widths or lifetimes compared with the response width; any parameter of the response that was fitted named, with its effect on the uncertainties of the headline parameters.

**Benchmark.** [13]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | D. W. Hogg, J. Bovy and D. Lang, Data analysis recipes: Fitting a model to data, arXiv:1008.4686 (2010) | doi:10.48550/arXiv.1008.4686 | full text | Abstract and Sec. 2: a fit is justified by a generative model of the data. Abstract and Secs. 2 and 4: weighted least squares assumes known Gaussian uncertainties in one coordinate only, conditions said to be rarely met. Sec. 4: the standard covariance matrix holds only under strict conditions; posterior moments, bootstrap and jackknife as alternatives, nuisance parameters marginalised. Sec. 6: adjusting variances until chi-squared looks reasonable is rarely a good idea. Secs. 7 and 8: uncertainties in both coordinates and intrinsic scatter put into the likelihood |
| 2 | A. A. Istratov and O. F. Vyvenko, Exponential analysis in physical phenomena, Rev. Sci. Instrum. 70, 1233–1257 (1999) | doi:10.1063/1.1149581 | abstract | Abstract (read from the Crossref record): two decay components can be resolved only if their time constants differ by more than a limit set by the signal-to-noise ratio; comparison of numerical methods for fitting exponentials |
| 3 | M. K. Transtrum, B. B. Machta, K. S. Brown, B. C. Daniels, C. R. Myers and J. P. Sethna, Perspective: Sloppiness and emergent theories in physics, biology, and beyond, J. Chem. Phys. 143, 010901 (2015); read as arXiv:1501.07668 | doi:10.1063/1.4923066 | full text | Sec. I, "Parameter indeterminacy and sloppiness", and in a fit of a sum of exponentials each rate is almost completely undetermined while combinations of rates are constrained. Fig. 1: Fisher information eigenvalues of many multiparameter models spread over many orders of magnitude |
| 4 | F. James and M. Winkler, Minuit 2, documentation of the C++ re-implementation of the Minuit function minimisation package, HTML edition in the ROOT documentation (read 2026) | https://root.cern/root/htmldoc/guides/minuit2/Minuit2.html | full text | Sec. 2.5.2: the error matrix includes correlations but not nonlinearities; fixing a parameter generally makes the errors of the others smaller. Sec. 2.5.3: MINOS errors include nonlinearities and are generally asymmetric. Secs. 6.3.1 and 6.4: limits can block the minimiser, and fixing parameters is used to guide the fit to the right minimum. Sec. 6.3.2: a parameter at its limit makes the error matrix essentially meaningless. Sec. 6.7: starting far from the solution can lead to unphysical local minima |
| 5 | NIST/SEMATECH e-Handbook of Statistical Methods, Sec. 4.4.5.2, Accounting for non-constant variation across the data (read 2026) | https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd452.htm | full text | Whole page: optimal weights are inversely proportional to the variance at each point; weights from a model of the variance are preferred to raw replicate variances; poorly estimated weights can make estimates worse; weighted residuals used to check the fit |
| 6 | J. W. Fowler, Maximum-likelihood fits to histograms for improved parameter estimation, J. Low Temp. Phys. 176, 414–420 (2014); read as arXiv:1312.5622 | doi:10.1007/s10909-014-1098-4 | full text | Secs. 2 and 3: chi-squared cost functions with data or model weights bias the fitted area and width of histogrammed peaks, Neyman weighting most strongly; only the Poisson maximum-likelihood cost gives an unbiased area. Sec. 4: least-squares code adapted to the Poisson likelihood |
| 7 | P. J. Humphrey, W. Liu and D. A. Buote, χ² and Poissonian data: biases even in the high-count regime and how to avoid them, Astrophys. J. 693, 822–829 (2009); read as arXiv:0811.2796 | doi:10.1088/0004-637X/693/1/822 | abstract | Abstract: common chi-squared approximations for Poisson data bias fitted parameters by as much as the statistical error or more, even at high counts, unless the number of bins is far below the square root of the total counts; the C-statistic recommended instead |
| 8 | NIST/SEMATECH e-Handbook of Statistical Methods, Sec. 4.4.4, How can I tell if a model fits my data? (read 2026) | https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd44.htm | full text | Whole page: graphical residual analysis is the primary tool for validating a model; structure in residuals shows a poor fit; a high R-squared does not guarantee a good fit; numerical tests mainly confirm the plots |
| 9 | R. Andrae, T. Schulze-Hartung and P. Melchior, Dos and don'ts of reduced chi-squared, arXiv:1012.3754 (2010) | doi:10.48550/arXiv.1012.3754 | full text | Sec. 2.4 and 2.6: degrees of freedom are not well defined for nonlinear models and can lie anywhere from 0 to N−1. Sec. 3: reduced chi-squared is itself uncertain, which limits its use to compare models. Sec. 4: normalised residuals tested against a Gaussian, cross-validation and bootstrap recommended instead |
| 10 | R. Protassov, D. A. van Dyk, A. Connors, V. L. Kashyap and A. Siemiginowska, Statistics, handle with care: detecting multiple model components with the likelihood ratio test, Astrophys. J. 571, 545–559 (2002); read as arXiv:astro-ph/0201547 | doi:10.1086/339856 | full text | Secs. 1 and 3.1: the likelihood ratio and F tests need nested models and a null value inside the parameter space; testing a line of zero flux lies on the boundary. Sec. 3.2: simulated false-positive rates differ from the nominal 5%. Secs. 4.1 and 5.2: posterior predictive p-values and parametric bootstrap to calibrate the test |
| 11 | A. R. Liddle, Information criteria for astrophysical model selection, Mon. Not. R. Astron. Soc. 377, L74–L78 (2007); read as arXiv:astro-ph/0701113 | doi:10.1111/j.1745-3933.2007.00306.x | full text | Sec. 2.2: the Akaike and Bayesian information criteria penalise the number of parameters in different ways, the latter growing with the number of data points. Abstract and Sec. 3: the two approaches give significantly different conclusions from the same data |
| 12 | R. Andrae, Error estimation in astronomy: A guide, arXiv:1009.2755 (2010) | doi:10.48550/arXiv.1009.2755 | full text | Sec. 3.2.1: rescaling errors to make reduced chi-squared one is bad practice, as it assumes Gaussian errors, a linear model and that the model is true. Sec. 3.3: the Fisher matrix gives only elliptical contours and can be a poor approximation. Secs. 3.4 and 4.3: Monte Carlo and bootstrap estimates |
| 13 | A. L. Trinh and A. Esposito, Biochemical resolving power of fluorescence lifetime imaging: untangling the roles of the instrument response function and photon-statistics, Biomed. Opt. Express 12, 3775–3788 (2021) | doi:10.1364/BOE.428070 | full text | Sec. 1: the measured signal is the convolution of the decay with the instrument response, which is commonly taken to limit the shortest measurable lifetime; decays fitted by iterative reconvolution with a known response. Secs. 3.2 and 4: the shortest measurable lifetime depends on the response width and the photon budget. Sec. 3.3: fitting the response width itself causes a considerable loss of precision |
