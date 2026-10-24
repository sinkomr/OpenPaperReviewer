---
id: T-STATISTICAL-INFERENCE-HEP
name: Statistical inference in particle physics
type: technique
field: physics/particle
applies_when: the paper claims a discovery, evidence or significance for a signal, or sets an upper limit, exclusion region or confidence interval on a signal rate, cross section, coupling or other parameter using a likelihood fit, CLs, Feldman-Cousins or Bayesian limits
version: "0.1"
---

# Statistical inference in particle physics

Particle physics searches and measurements use a likelihood model of signal, background and systematic effects to claim a discovery significance, to exclude signal hypotheses with upper limits, or to quote confidence or credible intervals. The usual tools are the profile likelihood ratio, the modified frequentist CLs method (the signal-plus-background p-value divided by one minus the background-only p-value), the Feldman-Cousins unified intervals, Bayesian limits, nuisance parameters for systematic uncertainties, and the Asimov dataset (a representative dataset in which every observable equals its expected value) used to estimate expected sensitivity.

## 1. Test statistic and the physical boundary

**Question.** Which test statistic was used for each result, is it one-sided or two-sided, and how does it handle a signal strength constrained to be non-negative and a fitted signal that comes out negative or above the tested value?

**Why it matters.** Discovery tests, upper limits and two-sided intervals need different test statistics, which differ in which fluctuations count against the hypothesis. A statistic that does not match the claim, or one that ignores the physical boundary, changes the p-value and the limit for the same data.

**Resolved by.** The test statistic written out, or named with a reference that defines it, for discovery and for limits separately; a statement of how a negative or large best-fit signal enters it; the same definition used for the observed and the expected results.

**Benchmark.** [1], [2]

## 2. Distribution of the test statistic

**Question.** Was the distribution of the test statistic taken from asymptotic formulae or from pseudo-experiments, and if asymptotic, does the paper show that the conditions for them hold, for example with enough events, no parameter at a boundary of its range and no parameter that is undefined when the signal is absent?

**Why it matters.** The chi-square forms from Wilks' theorem and its extensions hold only for large samples and under regularity conditions. With few events, low background, a parameter on its boundary, a signal parameter such as mass that has no meaning under the background-only hypothesis, non-nested or misspecified models, the true p-value can differ from the asymptotic one, and intervals can lose their stated coverage.

**Resolved by.** The method stated for each p-value and limit; where counts are small or a regularity condition fails, the asymptotic result compared with pseudo-experiments generated under the tested hypothesis, or pseudo-experiments used throughout; for intervals, coverage checked by simulation over the relevant range of the true parameter.

**Benchmark.** [1], [2], [3]

## 3. Limit-setting prescription and low sensitivity

**Question.** Which prescription produced each limit or interval (CLs, a plain frequentist p-value, Feldman-Cousins or another), was it fixed before the data were seen, and how is a limit stronger than the expected one, or an exclusion where the experiment has little sensitivity, explained?

**Why it matters.** A plain one-sided frequentist limit excludes, at the stated rate, signals to which the experiment has no sensitivity, and gives anomalously strong limits when the background fluctuates low. CLs suppresses this but over-covers by an amount that depends on the signal. Choosing between an upper limit and a two-sided interval after looking at the data makes intervals under-cover for some values of the parameter, and a two-sided unified interval at 90 or 95% confidence that excludes zero is not a discovery.

**Resolved by.** The prescription and confidence level named for every limit; for unified intervals, the ordering rule stated and no data-driven switch between one- and two-sided results; observed limits shown with the expected limit under the background-only hypothesis, so that a downward fluctuation is visible; any interval that excludes zero described with its significance, not as evidence for a signal on that basis alone.

**Benchmark.** [2], [4], [5]

## 4. Priors in Bayesian limits

**Question.** For Bayesian limits or credible intervals, are the priors on the parameter of interest and on the nuisance parameters stated, and does the paper show how the result changes under other reasonable priors?

**Why it matters.** A Bayesian limit depends on the prior, and a prior that is flat in one parameter is not flat in a nonlinear function of it, so a different parametrisation can give a different result. The uniform prior commonly used for a signal rate does not represent a degree of belief; it is a recipe whose frequentist properties, such as coverage, need to be studied, and some intervals built on it under-cover.

**Resolved by.** The prior for every parameter given explicitly, including its range and parametrisation; a sensitivity study with at least one alternative prior, such as a reference or Jeffreys prior; where frequentist language is used, the coverage of the Bayesian interval studied; enough information, such as a best estimate with its uncertainty even in the unphysical region, for the result to be combined with others.

**Benchmark.** [2], [5]

## 5. Nuisance parameters and their constraints

**Question.** Which systematic uncertainties enter the likelihood as nuisance parameters, what constraint term or auxiliary measurement fixes each one and with what functional form, how are they correlated between channels and samples, and are they profiled or integrated out, including in the pseudo-experiments?

**Why it matters.** Nuisance parameters reduce bias from an imperfect model but enlarge the statistical uncertainty, and the result depends on how each is constrained. A p-value computed at profiled nuisance values can be too high or too low when the true values differ. Integrating nuisance parameters over a prior inside a frequentist test gives a hybrid that does not guarantee coverage. Templates taken from sparsely populated simulated samples carry their own statistical uncertainty. Correlations omitted or assumed wrongly between channels change a combined result.

**Resolved by.** A list or table of the nuisance parameters with the source, size and form of each constraint (for example Gaussian, log-normal or Poisson auxiliary measurement); the statistical uncertainty of simulated templates included where samples are small, for example with a nuisance parameter per bin; the correlation scheme between channels and samples stated; the treatment, profiling or marginalisation, named, and for pseudo-experiments, how the auxiliary measurements or nuisance parameters were varied; the effect of the leading uncertainties on the result shown.

**Benchmark.** [2], [5], [6]

## 6. Background model and its form

**Question.** When the background shape comes from a fitted function, how was its form chosen, and is the uncertainty from that choice included in the result and shown to give little bias in the fitted signal?

**Why it matters.** Small changes in the assumed background shape can shift the apparent size and position of a signal. Fitting with a single chosen function that differs from the true shape can bias the signal estimate and make intervals under-cover, and adding nuisance parameters is unlikely to repair a functional form that is badly wrong.

**Resolved by.** The candidate background models and the rule for choosing among them stated; the choice treated as a systematic uncertainty, for example as a discrete nuisance parameter with a penalty for extra parameters; pseudo-experiments generated from alternative shapes and fitted with the chosen model, showing the bias in the signal and the coverage.

**Benchmark.** [3], [7]

## 7. Look-elsewhere effect

**Question.** When a signal parameter such as a mass, width or position was scanned, are both the local and the global significance given, is the search region over which the global value applies defined, and how was the global value computed?

**Why it matters.** A local p-value assumes the position of the signal was fixed in advance. The probability of finding an equally significant excess anywhere in the search region under the background-only hypothesis can be much larger, by a trial factor that grows with the local significance and with the number of effectively independent regions. Which search region is relevant is partly a matter of choice.

**Resolved by.** The local and global significances both reported, with the search range used for the global value stated; the global p-value obtained from background-only pseudo-experiments or from an upcrossing approximation, with the method stated; claims of discovery or evidence based on the global value.

**Benchmark.** [2], [3], [8]

## 8. Expected sensitivity and the reported statistical model

**Question.** Are the expected significance or expected limit given with their spread, how were they computed (for example from an Asimov dataset or pseudo-experiments), and is enough of the likelihood or statistical model published for others to reproduce, reinterpret or combine the result?

**Why it matters.** An observed limit or significance can only be judged against what the experiment expected and how far that varies with statistical fluctuations. Asimov-based bands are an approximation and can be too narrow when the uncertainty of the signal strength depends on its value. A limit published without the model behind it cannot be combined correctly, and dropping correlations or assuming Gaussian uncertainties changes the inferred constraints.

**Resolved by.** The median expected result shown with bands of one and two standard deviations, and the method for them stated, with pseudo-experiments where the asymptotic bands are doubtful; the observed result placed within those bands; the best-fit value and its uncertainty given; the full statistical model, or at least the likelihood with nuisance parameters and correlations, made available in a standard format.

**Benchmark.** [1], [2], [5], [6]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | G. Cowan, K. Cranmer, E. Gross and O. Vitells, Asymptotic formulae for likelihood-based tests of new physics, Eur. Phys. J. C 71, 1554 (2011); read as preprint arXiv:1007.1727 | doi:10.1140/epjc/s10052-011-1554-0 | full text | Sec. 2: definitions of the two-sided, one-sided discovery and one-sided upper-limit statistics and their variants for a signal strength bounded at zero, differing in which fluctuations count against the hypothesis. Sec. 3: asymptotic distributions exact only in the large-sample limit, with Monte Carlo advised for very small samples; Sec. 3.2 defines the Asimov dataset. Secs. 4.1 to 4.3: median expected significance and limits from the Asimov dataset, with error bands |
| 2 | G. Cowan, 40. Statistics, in S. Navas et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110, 030001 (2024), revised August 2023 | https://pdg.lbl.gov/2024/reviews/rpp2024-rev-statistics.pdf | full text | Sec. 40.2.2.2: nuisance parameters reduce bias but enlarge statistical errors; constraints from control measurements. Sec. 40.3.2.1: Wilks' theorem needs large samples and regularity conditions; p-values at profiled nuisance values can be too high or too low; marginal model for nuisance parameters. Sec. 40.3.2.2: local and global p-values, ambiguity of the search region, upcrossing approximation. Secs. 40.2.6.1 and 40.4.1: flat prior not invariant under reparametrisation, prior sensitivity analysis, Jeffreys prior. Sec. 40.4.2.2: coverage determined by Monte Carlo. Sec. 40.4.2.4: exclusion with no sensitivity, CLs conservative and over-covering, flip-flopping, excluding zero at 90 or 95% not a discovery, uniform prior as a recipe whose lower limits can under-cover, report an estimate even if unphysical. Sec. 40.5: median expected limit and significance with one- and two-sigma bands |
| 3 | S. Algeri, J. Aalbers, K. D. Morå and J. Conrad, Searching for new phenomena with profile likelihood ratio tests, Nat. Rev. Phys. 2, 245–252 (2020); read as preprint arXiv:1911.10237, which carries a different title | doi:10.1038/s42254-020-0169-5 | full text | Sec. 2: five conditions for Wilks' theorem (enough data, interior, identifiable, nested, correctly specified). Sec. 3.1 to 3.4: failures from small samples, parameters on a boundary, parameters not identifiable under the null (look-elsewhere), non-nested models; toy Monte Carlo under the null recommended when asymptotics are in doubt. Sec. 3.5: nuisance parameters trade bias against variance and are unlikely to fix a badly wrong functional form |
| 4 | G. J. Feldman and R. D. Cousins, Unified approach to the classical statistical analysis of small signals, Phys. Rev. D 57, 3873–3889 (1998); read as preprint arXiv:physics/9711021 | doi:10.1103/PhysRevD.57.3873 | full text | Sec. III: choosing an upper limit or central interval after seeing the data (flip-flopping) under-covers; standard constructions can give empty intervals. Sec. IV: likelihood-ratio ordering principle. Sec. VI: an experiment seeing fewer events than the expected background gets a stronger limit, so the sensitivity (average upper limit with no signal) should be reported alongside |
| 5 | K. Cranmer, Practical statistics for the LHC, lectures at the 2011 European School of High-Energy Physics, arXiv:1503.07622 (2015) | doi:10.48550/arXiv.1503.07622 | full text | Sec. 2.4: constraint terms as surrogates for auxiliary measurements, theory uncertainties without frequentist meaning. Sec. 4.1.6: consistent pairings of Gaussian, Poisson and log-normal constraints. Sec. 4.1.7: sparsely populated simulated templates handled with a nuisance parameter per bin. Sec. 5.2: CLs defined, motivated by arbitrarily small limits after downward fluctuations. Sec. 5.8: CLs over-covers, approaching full coverage for small signals. Sec. 5.4: toys randomise auxiliary measurements; randomising nuisance parameters gives a hybrid p-value. Sec. 5.5.4: Asimov bands too narrow when the uncertainty depends on the signal strength. Sec. 6: sensitivity to the choice of prior recommended. Sec. 6.1: hybrid marginalisation of nuisance parameters does not guarantee coverage |
| 6 | K. Cranmer, S. Kraml, H. B. Prosper et al., Publishing statistical models: Getting the most out of particle physics experiments, SciPost Phys. 12, 037 (2022); read as preprint arXiv:2109.04981 | doi:10.21468/SciPostPhys.12.1.037 | full text | Secs. 2.1 and 2.2: the full statistical model, with auxiliary data constraining nuisance parameters, is the starting point for reinterpretation and combination; likelihoods alone lead to double-counted constraints in combinations. Secs. 4.1 and 4.2.1: dropping correlations or using Gaussian approximations changes the inferred constraints; full correlation information should be published |
| 7 | P. D. Dauncey, M. Kenzie, N. Wardle and G. J. Davies, Handling uncertainties in background shapes: the discrete profiling method, JINST 10, P04015 (2015); read as preprint arXiv:1408.6865 | doi:10.1088/1748-0221/10/04/P04015 | full text | Sec. 2: small changes in background shape shift the apparent signal size and position; the function choice treated as a discrete nuisance parameter. Sec. 3.3: fitting with a single wrong function gives bias and under-coverage in pseudo-experiments. Sec. 4: penalty for the number of parameters; bias and coverage tests |
| 8 | E. Gross and O. Vitells, Trial factors for the look elsewhere effect in high energy physics, Eur. Phys. J. C 70, 525–530 (2010); read as preprint arXiv:1005.1891 | doi:10.1140/epjc/s10052-010-1470-8 | full text | Sec. 1: a mass undefined under the background-only hypothesis breaks Wilks' regularity conditions; the probability of an excess anywhere in the range exceeds the fixed-mass probability. Sec. 2: upcrossing bound estimated from a few background-only simulations. Sec. 2.1: trial factor grows linearly with the fixed-mass significance and the effective number of independent regions |
