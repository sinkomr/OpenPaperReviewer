---
id: T-GALAXY-SURVEYS
name: Galaxy surveys and large-scale structure
type: technique
field: physics/astrophysics
applies_when: the paper measures galaxy or quasar clustering from a survey catalogue, such as correlation functions, power spectra, baryon acoustic oscillations, redshift-space distortions or angular clustering, or bases a cosmological constraint on such statistics, photometric redshift distributions or covariances from mock catalogues
version: "0.1"
---

# Galaxy surveys and large-scale structure

Galaxy surveys are used to claim measurements of large-scale structure: two-point statistics such as the correlation function and power spectrum, the baryon acoustic oscillation (BAO) scale, redshift-space distortions (RSD) and the cosmological parameters inferred from them. Each rests on comparing the observed galaxy density with the density expected from the survey's selection function, which a random catalogue represents, using spectroscopic or photometric redshifts (photo-z) and a covariance matrix that is usually estimated from mock catalogues.

## 1. Angular selection function and random catalogue

**Question.** How were the footprint, the veto masks and the completeness in each region of the sky defined, and how were the random points generated so that they follow the same selection as the galaxies?

**Why it matters.** Clustering is measured against the random catalogue, so any difference between where galaxies could have been observed and where randoms are placed appears as spurious clustering. Areas near bright stars, poor imaging, tile centres and regions of low fibre or redshift completeness all change the expected density, and the choice of completeness thresholds changes the sample.

**Resolved by.** The mask described, with the veto masks and the area each removes; completeness defined per sector or pixel, with any cut on it stated; randoms drawn with density proportional to the completeness, cut by the same vetoes and many times denser than the galaxies; separate regions of the survey with different photometry treated as separate selection functions or shown to agree; mask and random files released or described well enough to rebuild.

**Benchmark.** [1], [2]

## 2. Radial selection, integral constraints and the window

**Question.** How was the redshift distribution of the randoms set (drawn from the observed galaxy redshifts, from a smooth fit, or from a model), and does the model compared with the data include the survey window and the integral constraints that this choice and the normalisation of the density impose?

**Why it matters.** Taking the mean density and the radial selection function from the data forces the measured fluctuations to integrate to zero over the footprint and in each redshift slice. This suppresses power on scales near the survey size and changes the multipoles, most in small or narrow surveys and in analyses that rely on the largest scales, and ignoring it can bias fitted parameters and degrade the fit.

**Resolved by.** The method of assigning redshifts to randoms stated, with the weights used in it; the survey window computed from the randoms and convolved with the model, or a measurement corrected for it; global and radial integral constraints modelled where large scales matter, or shown on mocks with the same footprint to be small compared with the statistical errors; the same procedure applied to mocks as to the data.

**Benchmark.** [1], [2], [3]

## 3. Targets without redshifts: fibre collisions and redshift failures

**Question.** How were targets that received no redshift handled, both those lost to fibre or slit collisions and those whose spectra gave no secure redshift, and does the paper show that the correction is adequate on the scales used in the analysis?

**Why it matters.** Close pairs on the sky cannot always both be observed, so the missing galaxies are concentrated in close pairs and the loss depends on scale. Redshift failures depend on galaxy brightness and on observing conditions, so they are not random. Upweighting a nearest neighbour restores clustering on large scales but leaves biases on small scales that can exceed sample variance, especially in the quadrupole.

**Resolved by.** The fraction of targets affected by each kind of loss stated; the weighting or modelling scheme described, with its assumptions; redshift-failure weights that account for the dependence on brightness and observing conditions; a test on mocks with the same collision pattern showing the residual bias is small compared with the errors over the fitted range, or a fitting range that stops where the correction becomes unreliable.

**Benchmark.** [1], [2], [4]

## 4. Imaging systematics: maps tested and weights derived

**Question.** Which maps of survey properties and foregrounds (for example stellar density, Galactic extinction, seeing, depth, sky brightness and airmass) were tested against galaxy density, by what criterion was each map corrected or left out, and does the paper show the dependence of density on each map before and after correction?

**Why it matters.** Variations in depth, seeing, stellar contamination and extinction change the number of galaxies detected and selected, and so imprint large-scale patterns that look like clustering. Leaving out a map that does contaminate the sample usually costs more than including a map that does not, and maps that are correlated with each other make it hard to tell which one is responsible.

**Resolved by.** The full list of maps tested, with the resolution and the fitting form used for each; the significance threshold for applying a correction, calibrated on mocks; plots of galaxy density against each map before and after weighting, consistent with no trend afterwards; cross-correlations between the corrected galaxy field and the maps shown to be small compared with the signal; regions with extreme survey properties masked and the area removed stated.

**Benchmark.** [1], [5], [6]

## 5. Effect of the corrections on the measured signal

**Question.** Does the paper estimate, on mocks with and without injected contamination, how much true clustering the systematic correction removes or leaves behind, and does it include that bias and the uncertainty of the weights in the result?

**Why it matters.** Any regression of galaxy density on survey maps also removes chance correlations between the maps and the true density field, so the corrected clustering is biased low, by an amount that grows with the number of maps. Corrections that model only an additive contamination leave a bias when the contamination is multiplicative.

**Resolved by.** The full correction pipeline run on mocks without contamination, to measure how much signal it removes, and on mocks with known contamination, to measure how much it recovers; the resulting bias either corrected or shown to be small compared with the errors; the effect of the correction on the covariance, or on the parameter constraints, tested; results shown with and without the weights, and for alternative sets of maps or methods.

**Benchmark.** [5], [6]

## 6. Photometric redshifts and redshift distributions

**Question.** For samples with photometric redshifts, how was the redshift distribution of each sample or tomographic bin estimated and calibrated, how representative is the calibration sample of the galaxies used, how large is the outlier fraction, and is the uncertainty in the mean and width of each distribution carried into the cosmological result?

**Why it matters.** Angular clustering and its cosmological interpretation depend directly on the redshift distribution: errors in its mean shift distance-scale results, errors in its width change the inferred clustering amplitude, and a fraction of outliers reduces the amplitude. Spectroscopic calibration samples are often incomplete in ways that depend on colour and redshift, and wrong calibration redshifts bias both the mean and the width.

**Resolved by.** The photo-z method and calibration data named, with the magnitude and colour range they cover compared with the target sample; the spectroscopic success rate and the treatment of incomplete or wrong calibration redshifts stated; an independent check of the distributions, for example cross-correlation with an overlapping spectroscopic sample; nuisance parameters for the mean and width of each distribution, or for the outlier fraction, marginalised over with stated priors.

**Benchmark.** [7]

## 7. Covariance matrix from a finite number of mocks

**Question.** How many independent mock catalogues were used to estimate the covariance, compared with the number of data points in the fitted data vector and the number of parameters, and were the corrections for the noise in the estimated covariance and its inverse applied to the likelihood and the quoted errors?

**Why it matters.** The inverse of a covariance estimated from a finite number of realisations is biased, which makes the likelihood too narrow and the confidence regions too small; the bias grows with the ratio of data points to realisations. Noise in the covariance also adds scatter to the best-fit parameters, which inflates the true parameter errors even after the inverse has been corrected.

**Resolved by.** The number of mocks and the length of the data vector stated, with mocks well outnumbering data points; the standard correction to the inverse covariance applied, and the parameter errors increased for covariance noise with the factors stated; the choice of bin width discussed in light of the number of mocks; where mocks are few, a method designed for that case, such as a shrinkage estimator, used and justified.

**Benchmark.** [8], [9], [10]

## 8. Fidelity and completeness of the covariance

**Question.** Do the mocks or analytic model used for the covariance reproduce the survey geometry, mask, redshift distribution, number density and clustering of the data, are the realisations independent, and does the covariance include the contribution from density modes larger than the survey?

**Why it matters.** A covariance from mocks with the wrong number density, clustering amplitude or footprint misstates the shot noise and sample variance. Realisations drawn from overlapping volumes are correlated, which acts as a smaller number of mocks. Modes larger than the survey couple the measured band powers through the mean density in the survey volume; this super-sample covariance is absent from simulations in periodic boxes and can dominate the non-Gaussian part of the errors on non-linear scales.

**Resolved by.** The mocks described, with their clustering, number density and redshift distribution compared with the data; the survey mask and the same selection and weights applied to each mock; the independence of realisations stated, or the correlation between them accounted for; super-sample covariance included in the covariance or the background density fitted as a parameter, where the analysis uses non-linear scales.

**Benchmark.** [10], [11]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | A. J. Ross, W. J. Percival, A. G. Sánchez, L. Samushia, S. Ho et al., The clustering of galaxies in the SDSS-III Baryon Oscillation Spectroscopic Survey: analysis of potential systematics, Mon. Not. R. Astron. Soc. 424, 564–590 (2012); read as preprint arXiv:1203.6499 | doi:10.1111/j.1365-2966.2012.21235.x | full text | Sec. 2.2: mask built from sectors of uniform tiling, veto masks for bright stars, non-photometric fields and tile centres, completeness thresholds, randoms placed in valid sectors and culled by completeness. Secs. 3.5 and 4: the two Galactic caps treated as separate selection functions and their densities and clustering compared. Sec. 3.2: fibre-collision and redshift-failure weights by nearest-neighbour upweighting, and their effect on clustering. Sec. 5.1: galaxy density depends on stellar density, seeing and extinction; cross-correlation with systematic maps. Sec. 5.2: stellar-density weights. Abstract: drawing random redshifts from the galaxy sample gave the least systematic error |
| 2 | B. Reid, S. Ho, N. Padmanabhan, W. J. Percival, J. Tinker et al., SDSS-III Baryon Oscillation Spectroscopic Survey Data Release 12: galaxy target selection and large-scale structure catalogues, Mon. Not. R. Astron. Soc. 455, 1553–1573 (2016); read as preprint arXiv:1509.06529 | doi:10.1093/mnras/stv2382 | full text | Secs. 5.1 and 5.1.1: sector completeness and veto masks with the area each removes. Sec. 5.2: randoms with density proportional to completeness, assigned redshifts drawn from the weighted galaxy redshifts. Sec. 6.1: collided targets upweight a neighbour; small-scale clustering stays biased and anisotropic. Sec. 6.3: redshift failures depend on fibre magnitude and are weighted using neighbours on the same plate and date. Sec. 1: catalogues, masks and code released |
| 3 | A. de Mattia and V. Ruhlmann-Kleider, Integral constraints in spectroscopic surveys, J. Cosmol. Astropart. Phys. 2019(08), 036 (2019); read as preprint arXiv:1904.08851 | doi:10.1088/1475-7516/2019/08/036 | full text | Secs. 2.1 to 2.4: setting the mean density from the data (global constraint) or the radial selection from the data redshifts (radial constraint) suppresses modes near the survey size and alters the multipoles; window convolution. Sec. 4: on mocks, ignoring the radial constraint biases RSD parameters by about 30% of the statistical error and worsens the fit. Sec. 4.4: deep, narrow or small surveys and large-scale analyses are most affected |
| 4 | C. Hahn, R. Scoccimarro, M. R. Blanton, J. L. Tinker and S. Rodríguez-Torres, The effect of fiber collisions on the galaxy power spectrum multipoles, Mon. Not. R. Astron. Soc., article stx185 (2017); read as preprint arXiv:1609.01714 | doi:10.1093/mnras/stx185 | full text | Abstract: fibre collisions affect the power spectrum monopole and quadrupole beyond sample variance on scales smaller than about k = 0.1 h/Mpc. Sec. III.1: nearest-neighbour upweighting leaves residuals that exceed sample variance on small scales, by several times for the quadrupole. Secs. III.2 and III.3: line-of-sight reconstruction and an effective-window model as alternatives |
| 5 | J. Elvin-Poole, M. Crocce, A. J. Ross et al. (Dark Energy Survey Collaboration), Dark Energy Survey year 1 results: galaxy clustering for combined probes, Phys. Rev. D 98, 042006 (2018); read as preprint arXiv:1708.01536 | doi:10.1103/PhysRevD.98.042006 | full text | Sec. V.1: survey-property maps of depth, seeing, exposure time, sky brightness and airmass per band, plus stellar density and extinction, tested. Sec. V.2: weights from fits of density against each map, applied iteratively until no map exceeds a significance threshold calibrated on mocks; extreme regions masked. Secs. VII.2 to VII.4: bias from the correction measured on contaminated and uncontaminated mocks, and effect on the covariance tested |
| 6 | N. Weaverdyck and D. Huterer, Mitigating contamination in LSS surveys: a comparison of methods, Mon. Not. R. Astron. Soc. 503, 5061–5084 (2021); read as preprint arXiv:2007.14499 | doi:10.1093/mnras/stab709 | full text | Secs. III.2 and III.3: regression on templates removes chance correlations with the true signal, biasing the cleaned power low unless debiased. Secs. IV.2 and IV.3: additive-only cleaning biases two-point statistics when contamination is multiplicative. Secs. VII.2 and VII.3: all methods overfit as templates are added, but neglecting a contaminating template costs more than overfitting. Sec. IX: recommendations, including regression diagnostics |
| 7 | J. A. Newman and D. Gruen, Photometric redshifts for next-generation surveys, Annu. Rev. Astron. Astrophys. 60, 363–414 (2022); read as preprint arXiv:2206.13633 | doi:10.1146/annurev-astro-032122-014611 | full text | Sec. 1.2.1: an outlier fraction reduces clustering amplitudes and must be corrected or marginalised over. Sec. 1.2.2: the mean of each bin's distribution matters most for BAO distances and its width for clustering amplitude; uncertainty marginalised by repeating the inference. Secs. 4.2.1 and 4.2.2: incomplete spectroscopic samples and wrong calibration redshifts bias the mean and width. Sec. 4.2.6: cross-correlation redshifts and their own systematics, such as magnification and evolving galaxy bias |
| 8 | J. Hartlap, P. Simon and P. Schneider, Why your model parameter confidences might be too optimistic: unbiased estimation of the inverse covariance matrix, Astron. Astrophys. 464, 399–404 (2007); read as preprint arXiv:astro-ph/0608064 | doi:10.1051/0004-6361:20066170 | full text | Sec. 3.1: the inverse of an estimated covariance is biased, making confidence regions too small; correction factor depending on the numbers of bins and realisations, valid only when bins are fewer than realisations minus two. Sec. 6: advises against using more bins than realisations |
| 9 | S. Dodelson and M. D. Schneider, The effect of covariance estimator error on cosmological parameter constraints, Phys. Rev. D 88, 063537 (2013); read as preprint arXiv:1304.2593 | doi:10.1103/PhysRevD.88.063537 | full text | Sec. III: noise in a simulation-based covariance adds parameter variance beyond the inverse-bias correction, growing with the number of bins and falling with the number of simulations. Sec. IV: analyses with hundreds of simulations may underestimate parameter errors by several per cent; shrinkage estimators and other ways to reduce the number of simulations needed |
| 10 | W. J. Percival, A. J. Ross, A. G. Sánchez, L. Samushia et al., The clustering of galaxies in the SDSS-III Baryon Oscillation Spectroscopic Survey: including covariance matrix errors, Mon. Not. R. Astron. Soc. 439, 2531–2541 (2014); read as preprint arXiv:1312.4841 | doi:10.1093/mnras/stu112 | full text | Secs. 2 to 4: correction factors for parameter errors and for the scatter of best fits, depending on the numbers of mocks, bins and parameters. Abstract and Sec. 6: even several hundred mocks raise errors noticeably. Sec. 6: bin width chosen in light of covariance noise. Secs. 6.1 and 7: mocks must be independent and reflect the survey geometry and mask; correlated mocks act as fewer mocks |
| 11 | M. Takada and W. Hu, Power spectrum super-sample covariance, Phys. Rev. D 87, 123504 (2013); read as preprint arXiv:1302.6994 | doi:10.1103/PhysRevD.87.123504 | full text | Abstract, Sec. I and Sec. II.3: modes larger than the survey add a covariance through the response to the background density, absent from periodic-box simulations. Sec. III.2 and Fig. 3: super-sample covariance dominates or matches the other non-Gaussian term on non-linear scales. Sec. IV: include it in the covariance or fit the background density as a parameter |
