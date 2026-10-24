---
id: T-MONTE-CARLO-INFERENCE
name: Monte Carlo and simulation-based inference
type: technique
field: physics/methods
applies_when: the paper derives parameters, posteriors, confidence regions or predictions from Monte Carlo simulation, Markov chain Monte Carlo sampling, simulated templates or simulation-based (likelihood-free or neural) inference, or interprets data by comparison with simulated events or configurations
version: "0.1"
---

# Monte Carlo and simulation-based inference

Monte Carlo (MC) simulation, Markov chain Monte Carlo (MCMC) sampling and simulation-based inference (SBI, also called likelihood-free inference) are used to claim parameter values with credible or confidence intervals, to compare models, and to interpret data through simulated predictions. Each result depends on a simulator that matches the real system, a sampler that has explored the target distribution, and an inference step whose own error is known.

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

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | K. Cranmer, J. Brehmer and G. Louppe, The frontier of simulation-based inference, Proc. Natl. Acad. Sci. USA 117, 30055–30062 (2020); read as preprint arXiv:1911.01429 | doi:10.1073/pnas.1912789117 | full text | Sec. 3.3 (preprocessing and postprocessing): the usual diagnostics do not address a simulator that is not an accurate description of the system; misspecification is usually handled with extra nuisance parameters, and learned summaries can be made robust to them; a parametric bootstrap with the simulator can calibrate inference for proper coverage; other checks such as known expectation values, and passing checks does not guarantee correctness |
| 2 | P. Cannon, D. Ward and S. M. Schmon, Investigating the impact of model misspecification in neural simulation-based inference, arXiv:2209.01845 (2022) | doi:10.48550/arXiv.2209.01845 | abstract | Abstract: neural SBI methods have mostly been tested on well-specified problems; misspecification can severely degrade their performance, and none of the mitigation strategies tested prevented failure in every case |
| 3 | S. Talts, M. Betancourt, D. Simpson, A. Vehtari and A. Gelman, Validating Bayesian inference algorithms with simulation-based calibration, arXiv:1804.06788 (2018) | doi:10.48550/arXiv.1804.06788 | full text | Abstract: simulation-based calibration validates inferences from algorithms that produce posterior samples, detecting inaccurate computation and inconsistent model implementations. Sec. 4.1: the rank of each prior draw among the posterior samples is uniform when the computation is correct. Sec. 4.2: too-narrow posteriors give a U-shaped rank histogram; correlated draws bias the ranks. Sec. 5.1: thin MCMC output by effective sample size |
| 4 | J. Hermans, A. Delaunoy, F. Rozet, A. Wehenkel, V. Begy and G. Louppe, A trust crisis in simulation-based inference? Your posterior approximations can be unfaithful, arXiv:2110.06581 (2021), published in Transactions on Machine Learning Research (2022) | doi:10.48550/arXiv.2110.06581 | full text | Abstract and Sec. 3: neural posterior and ratio estimation, sequential neural likelihood and approximate Bayesian computation can all give overconfident posteriors. Sec. 2.2: expected coverage of highest-posterior-density regions as the diagnostic. Secs. 3.4 and 4: ensembles and post-hoc recalibration improve coverage |
| 5 | A. Gelman, A. Vehtari, D. Simpson, C. C. Margossian, B. Carpenter, Y. Yao, L. Kennedy, J. Gabry, P.-C. Bürkner and M. Modrák, Bayesian workflow, arXiv:2011.01808 (2020) | doi:10.48550/arXiv.2011.01808 | full text | Sec. 4.1: fit simulated data from known parameters and check recovery. Sec. 4.2: simulation-based calibration, drawing parameters from the prior, simulating, refitting and checking calibration over many runs. Sec. 2.4: prior predictive checks show what the prior implies for observable data. Sec. 6.1: posterior predictive checks compare replicated data from posterior draws with the observed data, including subgroups the model omits. Sec. 6.3: prior influence assessed by comparing prior and posterior and refitting with alternative priors |
| 6 | A. Vehtari, A. Gelman, D. Simpson, B. Carpenter and P.-C. Bürkner, Rank-normalization, folding, and localization: an improved R-hat for assessing convergence of MCMC, Bayesian Anal. 16, 667–718 (2021); read as preprint arXiv:1903.08008 | doi:10.1214/20-BA1221 | full text | Sec. 1.2: traditional R-hat can be near one when chains differ in variance or have heavy tails, and says little about tails. Sec. 1.1: diagnostics work best with chains started from diverse points. Sec. 2: at least four chains, rank-normalised split R-hat below 1.01, rank-normalised effective sample size above 400, convergence checked for reported quantiles and intervals. Secs. 2 and 3.2: effective sample size can be greatly overestimated from a single chain in a multimodal posterior |
| 7 | J. K. Kruschke, Bayesian analysis reporting guidelines, Nat. Hum. Behav. 5, 1282–1291 (2021) | doi:10.1038/s41562-021-01177-7 | full text | Step 1C: explain and justify the prior for every parameter, with a prior predictive check (Step 1E) and sensitivity analysis. Step 2B: report a convergence statistic such as R-hat for each parameter, with several chains. Step 2C: report effective sample size, with large values needed for stable interval limits. Step 3A: posterior predictive check. Step 5: sensitivity of results to alternative priors, reported as tables |
| 8 | D. W. Hogg and D. Foreman-Mackey, Data analysis recipes: using Markov chain Monte Carlo, Astrophys. J. Suppl. Ser. 236, 11 (2018); read as preprint arXiv:1710.06068 | doi:10.3847/1538-4365/aab76e | full text | Sec. V: no simple test proves convergence; integrated autocorrelation time sets the Monte Carlo error; compare halves of the chain and independently started walkers. Sec. VII: burn-in, and several starts when the posterior may be multimodal. Sec. VIII: report quantile summaries; trace and posterior predictive plots; a good-looking trace does not guarantee convergence. Sec. IX: results that depend on initialisation indicate that the sampler has not converged |
| 9 | U. Wolff, Monte Carlo errors with less errors, Comput. Phys. Commun. 156, 143–153 (2004); read as preprint arXiv:hep-lat/0306017 | doi:10.1016/S0010-4655(03)00467-3 | full text | Sec. 2.2: the naive error ignoring autocorrelations is too small by the square root of twice the integrated autocorrelation time, and only that reduced number of samples is effectively independent; replica runs give a consistency test. Sec. 2.1: run length must be much longer than the autocorrelation time. Sec. 3.2: binning has a systematic error that decays slowly with bin size |
| 10 | C. A. Argüelles, A. Schneider and T. Yuan, A binned likelihood for stochastic models, J. High Energy Phys. 06, 030 (2019); read as preprint arXiv:1901.04645 | doi:10.1007/JHEP06(2019)030 | full text | Sec. 2: the common likelihood treats the simulated expectation as the true rate and neglects its stochastic nature. Sec. 4.2: this leads to undercoverage, still present with large simulated samples. Sec. 5: parameter uncertainties can be vastly underestimated when simulated samples are small |
| 11 | A. M. Ferrenberg, D. P. Landau and Y. J. Wong, Monte Carlo simulations: hidden errors from good random number generators, Phys. Rev. Lett. 69, 3382 (1992) | doi:10.1103/PhysRevLett.69.3382 | abstract | Abstract: a widely used cluster Monte Carlo algorithm gave wrong results when combined with random number generators regarded as high quality, because of subtle correlations in the generators |
| 12 | F. James and L. Moneta, Review of high-quality random number generators, Comput. Softw. Big Sci. 4, 2 (2020); read as preprint arXiv:1903.01247 | doi:10.1007/s41781-019-0034-3 | full text | Sec. 1: a generator thought to be the best gave a wrong answer for a phase-transition problem; passing any number of empirical tests cannot prove the absence of defects; prefer generators whose defects are understood; the period must far exceed the sequence used. Secs. 3.2 and 5.1: independent, non-overlapping sequences for separate runs |
