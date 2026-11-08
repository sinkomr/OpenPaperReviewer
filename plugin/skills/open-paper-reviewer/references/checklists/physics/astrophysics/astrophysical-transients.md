---
id: T-ASTROPHYSICAL-TRANSIENTS
name: Astrophysical transients
type: technique
field: physics/astrophysics
applies_when: the paper detects, localises or classifies a transient such as a fast radio burst, gamma-ray burst, supernova or tidal disruption event, associates it with a host galaxy or with a detection by another instrument or messenger, or infers transient rates or populations
version: "0.1"
---

# Astrophysical transients

## 1. Localisation and its error region

**Question.** How was the position of the transient measured, what are the size and shape of its error region at a stated confidence level, and does the error budget include the systematic error of tying that position to the images used to search for a host or counterpart?

**Why it matters.** A host or counterpart association can be no better than the position it starts from. Single-dish radio positions are limited by the beam width, often several arcminutes, and the elongated beams of linear arrays leave one direction poorly constrained. Registering a position from one instrument onto images from another adds an error that can be many times the centroiding error.

**Resolved by.** The position given with its statistical and systematic errors stated separately, the confidence level and the shape of the region (circle, ellipse or probability map); the method of astrometric tie between instruments and its residuals; the error region drawn on the images used for the association.

**Benchmark.** [1], [4]

## 2. Chance alignment with a host galaxy

**Question.** Does the paper give the probability that a galaxy as bright as the proposed host would fall within the search region by chance, how was the search radius defined, and, if several galaxies are candidates, how were they ranked?

**Why it matters.** Faint galaxies are numerous, so a large error region almost always contains one. The chance probability follows from the surface density of galaxies brighter than the candidate and from an effective radius set by the error region, the offset and the galaxy size; for faint dwarf hosts, sub-arcsecond positions are needed to make it small. A chance probability alone does not rank several candidates or allow for a host too faint to be detected.

**Resolved by.** The chance-coincidence probability with the number counts, band and radius used; or a probabilistic association that gives a posterior for each candidate, states its priors on galaxy brightness, offset and an undetected host, and reports how the result changes under other priors; the depth of the imaging stated; associations below the chosen threshold presented as uncertain.

**Benchmark.** [1], [2], [3]

## 3. Distance from dispersion measure or an assumed host

**Question.** When a distance, energy or luminosity rests on the dispersion measure (DM) of a radio burst or on the redshift of a proposed host, does the paper state each contribution to the DM, the model and uncertainty of the Galactic part, and what the conclusion would be if the host were wrong?

**Why it matters.** The extragalactic DM is what remains after subtracting a Galactic model contribution that is uncertain at the level of tens of per cent and differs between models. The host and local contributions are generally unknown and broadly distributed, so the DM gives an upper bound on redshift rather than a value, and simple conversions from DM to redshift are crude.

**Resolved by.** The Galactic electron-density model named and its uncertainty carried; an assumed host and local contribution stated with its range; redshift from DM quoted as a bound or range; a spectroscopic host redshift where the claim depends on distance; energies and luminosities shown to hold over the allowed range of distance.

**Benchmark.** [2], [4]

## 4. Astrophysical signal or artefact

**Question.** What shows that the candidate is a source on the sky and not terrestrial interference, an instrumental artefact or an image-subtraction residual, and how were candidates screened?

**Why it matters.** Radio interference can mimic the frequency sweep of dispersion, and signals seen in many widely separated beams at once have proved to be local. In optical difference imaging, cosmic rays, ghosts, registration errors and residuals of bright stars produce false candidates, and automatic classifiers trade false candidates against missed real ones at the chosen threshold.

**Resolved by.** For radio bursts, a sweep consistent with the cold-plasma dispersion law, a DM above the Galactic expectation and a pattern across beams consistent with a single sky position; for imaging, the science, reference and difference images shown, detection in more than one epoch or instrument, and the classifier score and threshold with their false-positive and false-negative rates.

**Benchmark.** [4], [6]

## 5. Spectroscopic classification

**Question.** On which spectral features, at what phase relative to peak, and with which template set and match quality was the transient classified, and are neighbouring classes excluded?

**Why it matters.** Supernova classes are defined by the presence or absence of hydrogen, helium and silicon lines whose visibility changes with phase; early spectra can show short-lived features, and some classes are defined only by an absence. Host-galaxy light and narrow host lines distort the spectrum. Template matching is biased towards classes with many templates, especially at low signal-to-noise, and becomes unreliable with host contamination or short rest-frame coverage.

**Resolved by.** The spectrum shown with its phase and the identifying lines marked; the matching code, template library, match quality and acceptance threshold; host light and lines removed or modelled; the next-best classes listed with their match quality; a later spectrum where the class depends on phase.

**Benchmark.** [7], [8]

## 6. Classification without a spectrum

**Question.** When the class rests on a light curve, colour, duration, host or the absence of repeats, does the paper state how pure the classification is expected to be and how the likely contaminants were excluded?

**Why it matters.** Photometric classifiers trained on spectroscopically confirmed events, which are biased towards bright objects, do worse on the unconfirmed sample, and some core-collapse types are often mistaken for type Ia. GRB durations depend on the detector's energy band and sensitivity, so the dividing duration differs between instruments and a single burst's class is a probability. Flares in galaxies with active nuclei and stellar flares can resemble other transients, and a burst seen once may still repeat.

**Resolved by.** The classifier and its training set, with purity and efficiency from simulations of a representative population; for GRBs, the threshold appropriate to the instrument and the probability of each class; for nuclear transients, archival data showing no earlier activity at that position, a host spectrum without signs of an active nucleus and the colour evolution; for radio bursts, the time and sensitivity of follow-up stated before any claim of non-repetition.

**Benchmark.** [4], [5], [9], [10], [11]

## 7. Detection efficiency and selection

**Question.** When a rate, luminosity or energy function, class fraction or distribution of host properties is inferred, was the detection efficiency measured by injecting synthetic events through the full search pipeline, and were the search cuts included?

**Why it matters.** Every survey samples the transient population incompletely, so each detected event stands for others that were missed. Recovery falls on bright regions of galaxies and in poor observing conditions, and radio-burst sensitivity depends strongly on burst width; DM cuts and real-time thresholds select further. Ignoring these biases rates and populations towards events that are easy to find.

**Resolved by.** Injection and recovery through the real-time pipeline, including interference excision and classifiers; efficiency given as a function of brightness or fluence, width, host surface brightness and observing conditions; search cuts stated; rates and distributions corrected with that efficiency.

**Benchmark.** [4], [12], [13]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | J. S. Bloom et al., The observed offset distribution of gamma-ray bursts from their host galaxies: a robust clue to the nature of the progenitors, Astron. J. 123, 1111 (2002); read as arXiv:astro-ph/0010176 | doi:10.1086/338893 |
| 2 | T. Eftekhari and E. Berger, Associating fast radio bursts with their host galaxies, Astrophys. J. 849, 162 (2017); read as arXiv:1705.02998 | doi:10.3847/1538-4357/aa90b9 |
| 3 | K. Aggarwal et al., Probabilistic association of transients to their hosts (PATH), Astrophys. J. 911, 95 (2021); read as arXiv:2102.10627 | doi:10.3847/1538-4357/abe8d2 |
| 4 | E. Petroff et al., Fast radio bursts, Astron. Astrophys. Rev. 27, 4 (2019); read as arXiv:1904.07947 | doi:10.1007/s00159-019-0116-6 |
| 5 | P. S. Cowperthwaite and E. Berger, A comprehensive study of detectability and contamination in deep rapid optical searches for gravitational wave counterparts, Astrophys. J. 814, 25 (2015); read as arXiv:1503.07869 | doi:10.1088/0004-637X/814/1/25 |
| 6 | D. A. Duev et al., Real-bogus classification for the Zwicky Transient Facility using deep learning, Mon. Not. R. Astron. Soc. 489, 3582 (2019); read as arXiv:1907.11259 | doi:10.1093/mnras/stz2357 |
| 7 | A. Gal-Yam, Observational and physical classification of supernovae, in Handbook of Supernovae, ed. A. W. Alsabti and P. Murdin, pp. 195–237 (Springer, 2017); read as arXiv:1611.09353 | doi:10.1007/978-3-319-21846-5_35 |
| 8 | S. Blondin and J. L. Tonry, Determining the type, redshift, and age of a supernova spectrum, Astrophys. J. 666, 1024 (2007); read as arXiv:0709.4488 | doi:10.1086/520494 |
| 9 | R. Kessler et al., Results from the Supernova Photometric Classification Challenge, Publ. Astron. Soc. Pac. 122, 1415 (2010); read as arXiv:1008.1024 | doi:10.1086/657607 |
| 10 | O. Bromberg et al., Short versus long and collapsars versus non-collapsars: a quantitative classification of gamma-ray bursts, Astrophys. J. 764, 179 (2013); read as arXiv:1210.0068 | doi:10.1088/0004-637X/764/2/179 |
| 11 | S. Gezari, Tidal disruption events, Annu. Rev. Astron. Astrophys. 59, 21 (2021); read as arXiv:2104.14580 | doi:10.1146/annurev-astro-111720-030029 |
| 12 | C. Frohmaier et al., Real-time recovery efficiencies and performance of the Palomar Transient Factory's transient discovery pipeline, Astrophys. J. Suppl. Ser. 230, 4 (2017); read as arXiv:1704.02951 | doi:10.3847/1538-4365/aa6d70 |
| 13 | M. Merryfield et al., An injection system for the CHIME/FRB experiment, Astron. J. 165, 152 (2023); read as arXiv:2206.14079 | doi:10.3847/1538-3881/ac9ab5 |
