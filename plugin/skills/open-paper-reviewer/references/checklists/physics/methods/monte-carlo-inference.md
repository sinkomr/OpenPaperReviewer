---
id: T-MONTE-CARLO-INFERENCE
name: Monte Carlo and simulation-based inference
type: technique
field: physics/methods
applies_when: the paper derives parameters, posteriors, confidence regions or predictions from Monte Carlo simulation, Markov chain Monte Carlo sampling, simulated templates or simulation-based (likelihood-free or neural) inference, or interprets data by comparison with simulated events or configurations
version: "0.1"
---

# Monte Carlo and simulation-based inference

## 1. Simulation validated against data

**Question.** Does the paper show that the simulation reproduces the data in regions or control samples where the quantity being inferred does not matter, and does it treat the known imperfections of the simulation as systematic uncertainties, for example through nuisance parameters or alternative simulators?

**Why it matters.** Simulation-based results assume that the simulator describes the system being studied. When it does not, the standard diagnostics of the inference do not detect the problem, and neural inference methods in particular can give poor results under such mismodelling, with no single mitigation that works in every case.

**Resolved by.** Comparisons of simulated and measured distributions in control samples or sidebands, with the level of agreement quantified; the mismodelled aspects named and given nuisance parameters or alternative-model variations, with their effect on the result shown; for learned summaries or surrogates, evidence that they are robust to the nuisance parameters that describe the simulator's known imperfections.

**Benchmark.** [1], [2]

## 2. Inference procedure tested on simulated data with known truth

**Question.** Was the full analysis chain run on simulated data sets generated with known parameter values, and does the paper show that it recovers them with intervals of the stated coverage?

**Why it matters.** A sampler, fitting code or learned posterior can be biased or overconfident without any sign in a single fit to the real data. Approximate SBI methods, including neural posterior and ratio estimators and approximate Bayesian computation, have been found to give overconfident posteriors, so a stated credible level is not reliable until it has been checked.

**Resolved by.** Injection-and-recovery or fake-data tests across the relevant parameter range; simulation-based calibration (ranks of the true values among near-independent posterior draws) or an expected-coverage plot against nominal credibility; for SBI, coverage measured on simulations not used in training, with any recalibration or ensembling stated; a parametric bootstrap where frequentist coverage is claimed.

**Benchmark.** [1], [3], [4], [5]

## 3. Convergence and mixing of the sampler

**Question.** How many chains or walkers were run, from what starting points, for how long, with what burn-in, and which convergence diagnostics were computed for the reported quantities, with what values?

**Why it matters.** No test proves that a chain has converged, and one chain can look stable while independent chains disagree. The traditional potential scale reduction factor (R-hat) can be close to one when chains differ in variance or tails, and a sampler started in one mode may never find another, so results that depend on the starting point are not converged.

**Resolved by.** Several chains from dispersed starting points, with between-chain and within-chain agreement shown; rank-normalised split R-hat below about 1.01 for each reported quantity, or an equivalent diagnostic; trace or rank plots; burn-in stated and justified; a check for multimodality, such as runs from different starts or a sampler designed for several modes, when the posterior may have more than one mode.

**Benchmark.** [6], [7], [8]

## 4. Autocorrelation and Monte Carlo error

**Question.** Does the paper report the integrated autocorrelation time or effective sample size for the quantities it quotes, and is the Monte Carlo error of each quoted value, including interval limits, shown to be small compared with its stated uncertainty?

**Why it matters.** Successive MC or MCMC samples are correlated, so the number of effectively independent samples is smaller than the number drawn, and an error computed as if the samples were independent is too small by the square root of twice the integrated autocorrelation time. Interval limits and tail quantiles need many more effective samples than a mean does.

**Resolved by.** Effective sample size, or autocorrelation time with run length much longer than it, for each reported quantity; errors from an autocorrelation analysis, binning or blocking with the bin size justified, or comparison of independent replica runs; enough effective samples for the interval limits quoted; equilibration shown to be much longer than the autocorrelation time.

**Benchmark.** [6], [7], [8], [9]

## 5. Finite size of simulated samples

**Question.** When simulated samples provide templates, efficiencies, acceptances or expected rates, how large are they compared with the data, and is their statistical uncertainty included in the likelihood or the error budget?

**Why it matters.** A likelihood that treats a simulated prediction as exact neglects its statistical fluctuations. With small simulated samples this can give intervals that are much too narrow and fail to cover the true value, and some undercoverage can persist even with large simulated samples.

**Resolved by.** The number of simulated events or configurations, and their weights, stated per bin or region; a likelihood that accounts for finite simulation statistics, or a demonstration that the simulated uncertainty is negligible; coverage of the final intervals checked with the simulated sample sizes actually used.

**Benchmark.** [10]

## 6. Priors and their influence

**Question.** Is the prior for every parameter stated and justified, and does the paper show how much the reported posterior depends on it?

**Why it matters.** A posterior combines data with prior assumptions, and where the data are weakly informative the prior can set the result. Priors described as uninformative can still imply implausible predictions or favour particular regions of parameter space once transformed or combined in a model.

**Resolved by.** Each prior given with its form, range and reason; a prior predictive check showing what data the priors imply; prior and posterior compared for each key parameter; a sensitivity analysis with alternative reasonable priors, reported as a table or plot of how the main results change.

**Benchmark.** [5], [7]

## 7. Random numbers and independence

**Question.** Does the paper name the random-number generator and how it was seeded, and for parallel or repeated runs, show that the streams are independent and that results do not depend on the generator?

**Why it matters.** Generators that pass standard statistical tests have produced wrong results in physics simulations because of subtle correlations that interact with the algorithm. Passing empirical tests cannot prove the absence of defects, and overlapping or correlated streams in parallel runs make supposedly independent samples dependent.

**Resolved by.** The generator, its period and the seeding scheme stated; a generator with understood quality for demanding simulations; parallel streams shown not to overlap; key results reproduced with a second, different generator or checked against an exactly known case run with the same generator and algorithm.

**Benchmark.** [11], [12]

## 8. Posterior predictive checks

**Question.** Does the paper compare data simulated from the fitted model, using posterior draws or best-fit parameters, with the observed data, including features that the fit was not tuned to?

**Why it matters.** A well-converged posterior describes the parameters of the assumed model, not whether that model describes the data. Without a predictive comparison, a model that misses important structure in the data can still return tight parameter estimates.

**Resolved by.** Replicated data sets or predictive distributions overlaid on the observed data, for the full distribution and for subgroups or summary statistics the model does not fit directly; discrepancies quantified and discussed; where checks fail, model extensions considered and their effect on the result shown.

**Benchmark.** [5], [7], [8]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | K. Cranmer et al., The frontier of simulation-based inference, Proc. Natl. Acad. Sci. USA 117, 30055 (2020); read as preprint arXiv:1911.01429 | doi:10.1073/pnas.1912789117 |
| 2 | P. Cannon et al., Investigating the impact of model misspecification in neural simulation-based inference, arXiv:2209.01845 (2022) | doi:10.48550/arXiv.2209.01845 |
| 3 | S. Talts et al., Validating Bayesian inference algorithms with simulation-based calibration, arXiv:1804.06788 (2018) | doi:10.48550/arXiv.1804.06788 |
| 4 | J. Hermans et al., A trust crisis in simulation-based inference? Your posterior approximations can be unfaithful, arXiv:2110.06581 (2021), published in Transactions on Machine Learning Research (2022) | doi:10.48550/arXiv.2110.06581 |
| 5 | A. Gelman et al., Bayesian workflow, arXiv:2011.01808 (2020) | doi:10.48550/arXiv.2011.01808 |
| 6 | A. Vehtari et al., Rank-normalization, folding, and localization: an improved R-hat for assessing convergence of MCMC, Bayesian Anal. 16, 667 (2021); read as preprint arXiv:1903.08008 | doi:10.1214/20-BA1221 |
| 7 | J. K. Kruschke, Bayesian analysis reporting guidelines, Nat. Hum. Behav. 5, 1282 (2021) | doi:10.1038/s41562-021-01177-7 |
| 8 | D. W. Hogg and D. Foreman-Mackey, Data analysis recipes: using Markov chain Monte Carlo, Astrophys. J. Suppl. Ser. 236, 11 (2018); read as preprint arXiv:1710.06068 | doi:10.3847/1538-4365/aab76e |
| 9 | U. Wolff, Monte Carlo errors with less errors, Comput. Phys. Commun. 156, 143 (2004); read as preprint arXiv:hep-lat/0306017 | doi:10.1016/S0010-4655(03)00467-3 |
| 10 | C. A. Argüelles et al., A binned likelihood for stochastic models, J. High Energy Phys. 06, 030 (2019); read as preprint arXiv:1901.04645 | doi:10.1007/JHEP06(2019)030 |
| 11 | A. M. Ferrenberg et al., Monte Carlo simulations: hidden errors from good random number generators, Phys. Rev. Lett. 69, 3382 (1992) | doi:10.1103/PhysRevLett.69.3382 |
| 12 | F. James and L. Moneta, Review of high-quality random number generators, Comput. Softw. Big Sci. 4, 2 (2020); read as preprint arXiv:1903.01247 | doi:10.1007/s41781-019-0034-3 |
