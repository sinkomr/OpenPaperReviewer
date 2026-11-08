---
id: CL-NONLINEAR-DYNAMICS
name: Claims of chaos and pattern formation
type: claim
field: physics/soft-matter
applies_when: the paper claims that a system is chaotic or follows low-dimensional deterministic dynamics, reports a Lyapunov exponent, fractal or correlation dimension from measured data, identifies a bifurcation or route to chaos, or attributes a spatial pattern to a stated instability
version: "0.1"
---

# Claims of chaos and pattern formation

## 1. State-space reconstruction from the data

**Question.** Where the claim rests on a state space reconstructed from a measured time series, does the paper state the observable, the sampling interval, the record length in units of the main time scale of the signal, the delay and the embedding dimension, and how each was chosen?

**Why it matters.** The delay and the embedding dimension change every quantity computed from the reconstruction: too small a dimension leaves the dynamics folded onto itself, and too large a delay makes the reconstruction fold over. Embedding needs evenly sampled data, and interpolating or filtering with a plain frequency cut-off can add or remove dynamics. A record that is short compared with its autocorrelation time, or with what the embedding dimension demands, gives misleading structure.

**Resolved by.** The method used for the delay, such as mutual information or autocorrelation, and for the dimension, such as false nearest neighbours or convergence of an invariant; results repeated over a range of delays and dimensions; evenly sampled data, or a method suited to event data; any filtering stated and justified for nonlinear data; the record length given in characteristic periods and compared with what the claimed dimension requires.

**Benchmark.** [1], [2]

## 2. Dimension estimates

**Question.** For a claimed fractal or low dimension, does the paper show the correlation sum, or its local slope, against scale for a series of embedding dimensions, with a scaling region whose range is stated, a slope that stops growing as the embedding dimension rises, temporally close pairs of points excluded, and the result compared with the largest dimension that the number of data points can return?

**Why it matters.** Pairs of points that are close in time because the signal is autocorrelated, rather than because the orbit returns, bias the estimate low and can give a spurious finite dimension in correlated noise. Stochastic signals with power-law spectra can also give a finite correlation dimension even for long records. The usual algorithm cannot return a dimension larger than about twice the base-ten logarithm of the number of points, so an estimate near that bound does not show low-dimensional dynamics.

**Resolved by.** Plots of the correlation sum and its local slopes for increasing embedding dimension, with the scaling range marked and spanning a stated range of scales; the exclusion window for temporally correlated pairs stated; a dimension well below the bound set by the number of points; the same analysis applied to surrogate or noise data with matched spectrum, giving a clearly different result.

**Benchmark.** [1], [2], [3], [4]

## 3. Lyapunov exponents

**Question.** For a claimed positive largest Lyapunov exponent, does the paper name the algorithm and its parameters, show the growth of separation between nearby trajectories with the fitted range marked, and show that the value is stable across embedding dimensions, neighbourhood sizes and record lengths, and across the scales at which it is measured?

**Why it matters.** Estimates of Lyapunov exponents from data are unstable and often very sensitive to the free parameters of the algorithm, the length of the record and the noise, and embedding in more dimensions than the dynamics need adds spurious exponents. With noise, nearby trajectories separate diffusively at small scales, and noisy oscillations, coloured noise and noisy chaos can be hard to tell apart unless the divergence is examined as a function of scale.

**Resolved by.** The divergence curve shown with a clear range of exponential growth and the fit range stated; the exponent unchanged within its uncertainty over a range of embedding dimensions, neighbourhood sizes and record lengths; the exponent given in inverse time units and the record length expressed in Lyapunov times; an analysis of how the divergence depends on scale, or a comparison with surrogate data, showing that noise alone does not produce it.

**Benchmark.** [1], [5]

## 4. Surrogate tests and what they exclude

**Question.** Is the evidence for nonlinear or deterministic structure tested against surrogate data, with the null hypothesis, the surrogate algorithm, the test statistic and the number of surrogates stated, and is a rejection interpreted only as far as that null hypothesis allows?

**Why it matters.** A linear stochastic process, possibly observed through a static nonlinear measurement function, reproduces many features that are attributed to chaos, and surrogates are the usual way to exclude it. Surrogate algorithms have their own artefacts, such as flattened spectra for short correlated records and spurious high frequencies when the ends of the record do not match, which can produce false rejections. A rejection shows that the data are not consistent with the null hypothesis; it indicates nonlinearity, not necessarily determinism or chaos.

**Resolved by.** The null hypothesis stated; an algorithm such as iteratively refined amplitude-adjusted surrogates, with a check that the surrogates match the spectrum and distribution of the data; the mismatch between the ends of the record removed, for example by choosing a stretch whose ends match; a rank-based test with enough surrogates for the stated significance, for example 19 for a one-sided test at 5 per cent; the statistic chosen before the test, not tuned on the same data; evidence of determinism beyond the rejection, such as a direct test for determinism based on the reconstructed dynamics.

**Benchmark.** [6], [7]

## 5. Stationarity over the record

**Question.** Does the paper show that the dynamics were stationary over the record used for each estimate: control parameters held and logged, transients discarded by a stated rule, and the analysis repeated on separate segments of the record?

**Why it matters.** Surrogates are stationary by construction, so a drifting record can be distinguished from them by its nonstationarity alone, which a surrogate test then reports as nonlinearity. A record taken while a parameter drifts through a bifurcation mixes several attractors, and quantities computed from it describe none of them.

**Resolved by.** Logs of the control parameters and environmental conditions over each record; the length of discarded transients and the reason for it; dimensions, exponents or predictions that agree between segments; a stationarity test such as cross-prediction between segments or a recurrence plot; where drift cannot be avoided, a null hypothesis that includes it.

**Benchmark.** [1], [6], [8]

## 6. Control-parameter scans and the type of bifurcation

**Question.** For a claimed bifurcation, threshold or route to chaos, is the control parameter scanned in steps fine enough near the transition and in both directions, with the ramp rate, waiting times and transients stated, and is the type of bifurcation identified from the measured behaviour near threshold?

**Why it matters.** When a parameter is ramped, the loss of stability is delayed past the bifurcation point, so the apparent threshold depends on the rate of the sweep, and noise can trigger a transition before the bifurcation point. Different bifurcations behave differently near threshold: a supercritical one grows continuously, with an amplitude that rises, for a pitchfork or Hopf bifurcation, as the square root of the distance from threshold, while a subcritical or fold bifurcation jumps to a distant state. Slowing down near threshold differs between bifurcation types, and indicators such as rising variance can fail, for example with multiplicative noise.

**Resolved by.** Sweeps up and down with the rate stated, and the threshold shown not to change when the rate is reduced; the amplitude plotted against the control parameter and fitted with the law expected for the claimed bifurcation, giving the threshold with its uncertainty; any hysteresis loop measured, or its absence shown; recovery times after small perturbations, where slowing down is part of the argument; the noise level stated relative to the rate of the sweep.

**Benchmark.** [9], [10]

## 7. Patterns: onset, wavelength and boundaries

**Question.** For a pattern attributed to a stated instability, does the paper compare the measured threshold, wavelength and, for oscillatory patterns, frequency at onset with a linear stability analysis that uses independently measured parameters, and does it show that the pattern is not set by the boundaries, the size of the container or the way the system is forced?

**Why it matters.** An instability of a uniform state is identified by its threshold, critical wavenumber and frequency, which linear stability analysis predicts. Above threshold a band of wavenumbers can be stable, so the observed wavelength also depends on history, defects and boundaries, and a boundary can fix the wavenumber. Real patterns in finite containers are shaped by their boundaries and defects, so a pattern set mainly by the walls or by non-uniform driving is not evidence for the stated instability.

**Resolved by.** Measured threshold, wavelength and frequency set against the predicted values with their uncertainties; the aspect ratio stated and the wavelength shown to be much smaller than the container, or shown not to scale with its size; the pattern reproduced with different boundary conditions or initial conditions; the spread of wavenumbers and the density of defects reported rather than a single representative image; the onset approached slowly enough for the pattern to settle.

**Benchmark.** [10], [11]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | E. Bradley and H. Kantz, Nonlinear time-series analysis revisited, Chaos 25, 097610 (2015); read as preprint arXiv:1503.07493 | doi:10.1063/1.4917289 |
| 2 | J. Theiler, Spurious dimension from correlation algorithms applied to limited time-series data, Phys. Rev. A 34, 2427 (1986) | doi:10.1103/PhysRevA.34.2427 |
| 3 | J. Theiler, Some comments on the correlation dimension of 1/f^α noise, Phys. Lett. A 155, 480 (1991); abstract read on arXiv:comp-gas/9302001 | doi:10.1016/0375-9601(91)90651-N |
| 4 | J.-P. Eckmann and D. Ruelle, Fundamental limitations for estimating dimensions and Lyapunov exponents in dynamical systems, Physica D 56, 185 (1992) | doi:10.1016/0167-2789(92)90023-G |
| 5 | J. B. Gao et al., Distinguishing chaos from noise by scale-dependent Lyapunov exponent, Phys. Rev. E 74, 066204 (2006) | doi:10.1103/PhysRevE.74.066204 |
| 6 | T. Schreiber and A. Schmitz, Surrogate time series, Physica D 142, 346 (2000); read as preprint arXiv:chao-dyn/9909037 | doi:10.1016/S0167-2789(00)00043-9 |
| 7 | D. T. Kaplan and L. Glass, Direct test for determinism in a time series, Phys. Rev. Lett. 68, 427 (1992) | doi:10.1103/PhysRevLett.68.427 |
| 8 | T. Schreiber, Detecting and analyzing nonstationarity in a time series using nonlinear cross predictions, Phys. Rev. Lett. 78, 843 (1997) | doi:10.1103/PhysRevLett.78.843 |
| 9 | C. Kuehn, A mathematical framework for critical transitions: bifurcations, fast-slow systems and stochastic dynamics, Physica D 240, 1020 (2011); read as preprint arXiv:1101.2899 | doi:10.1016/j.physd.2011.02.012 |
| 10 | P. C. Hohenberg and A. P. Krekhov, An introduction to the Ginzburg-Landau theory of phase transitions and nonequilibrium patterns, Phys. Rep. 572, 1 (2015); read as preprint arXiv:1410.7285 | doi:10.1016/j.physrep.2015.01.001 |
| 11 | M. C. Cross and P. C. Hohenberg, Pattern formation outside of equilibrium, Rev. Mod. Phys. 65, 851 (1993) | doi:10.1103/RevModPhys.65.851 |
