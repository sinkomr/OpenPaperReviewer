---
id: T-ASTROPHYSICAL-TRANSIENTS
name: Astrophysical transients
type: technique
field: physics/astrophysics
applies_when: the paper detects, localises or classifies a transient such as a fast radio burst, gamma-ray burst, supernova or tidal disruption event, associates it with a host galaxy or with a detection by another instrument or messenger, or infers transient rates or populations
version: "0.1"
---

# Astrophysical transients

Transient studies claim that a short-lived source, such as a fast radio burst (FRB), gamma-ray burst (GRB), supernova (SN) or tidal disruption event (TDE), is astrophysical, belongs to a given class, lies in a given host galaxy at a given distance, or coincides with a detection by another instrument or messenger. These claims rest on a position and its error region, on spectra, light curves or durations, and on the rate of unrelated sources that could produce the same match by chance.

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

## 4. Coincidence with another detection

**Question.** When the transient is linked to a detection by another instrument or messenger, such as a gamma-ray, radio, optical, neutrino or gravitational-wave event, does the paper estimate how often unrelated events would match as well within the same time window and sky area?

**Why it matters.** Unrelated detections and noise triggers can fall within the time window and sky region by chance. The significance of a coincidence depends on the background rate in each channel, the width of the allowed delay window and the overlap of the localisations, and wider windows or higher background rates lower it. A search of a large error region for a counterpart turns up many unrelated transients, with hundreds of supernovae expected in a deep optical search of about 100 square degrees.

**Resolved by.** The rate of unrelated events in each channel, the time window and its physical justification, and the overlap of the localisations, combined into a false-alarm probability or odds with the assumptions stated; for counterpart searches, the expected number of unrelated transients in the region and the colour, timescale or host criteria used to reject them.

**Benchmark.** [5], [6]

## 5. Astrophysical signal or artefact

**Question.** What shows that the candidate is a source on the sky and not terrestrial interference, an instrumental artefact or an image-subtraction residual, and how were candidates screened?

**Why it matters.** Radio interference can mimic the frequency sweep of dispersion, and signals seen in many widely separated beams at once have proved to be local. In optical difference imaging, cosmic rays, ghosts, registration errors and residuals of bright stars produce false candidates, and automatic classifiers trade false candidates against missed real ones at the chosen threshold.

**Resolved by.** For radio bursts, a sweep consistent with the cold-plasma dispersion law, a DM above the Galactic expectation and a pattern across beams consistent with a single sky position; for imaging, the science, reference and difference images shown, detection in more than one epoch or instrument, and the classifier score and threshold with their false-positive and false-negative rates.

**Benchmark.** [4], [7]

## 6. Spectroscopic classification

**Question.** On which spectral features, at what phase relative to peak, and with which template set and match quality was the transient classified, and are neighbouring classes excluded?

**Why it matters.** Supernova classes are defined by the presence or absence of hydrogen, helium and silicon lines whose visibility changes with phase; early spectra can show short-lived features, and some classes are defined only by an absence. Host-galaxy light and narrow host lines distort the spectrum. Template matching is biased towards classes with many templates, especially at low signal-to-noise, and becomes unreliable with host contamination or short rest-frame coverage.

**Resolved by.** The spectrum shown with its phase and the identifying lines marked; the matching code, template library, match quality and acceptance threshold; host light and lines removed or modelled; the next-best classes listed with their match quality; a later spectrum where the class depends on phase.

**Benchmark.** [8], [9]

## 7. Classification without a spectrum

**Question.** When the class rests on a light curve, colour, duration, host or the absence of repeats, does the paper state how pure the classification is expected to be and how the likely contaminants were excluded?

**Why it matters.** Photometric classifiers trained on spectroscopically confirmed events, which are biased towards bright objects, do worse on the unconfirmed sample, and some core-collapse types are often mistaken for type Ia. GRB durations depend on the detector's energy band and sensitivity, so the dividing duration differs between instruments and a single burst's class is a probability. Flares in galaxies with active nuclei and stellar flares can resemble other transients, and a burst seen once may still repeat.

**Resolved by.** The classifier and its training set, with purity and efficiency from simulations of a representative population; for GRBs, the threshold appropriate to the instrument and the probability of each class; for nuclear transients, archival data showing no earlier activity at that position, a host spectrum without signs of an active nucleus and the colour evolution; for radio bursts, the time and sensitivity of follow-up stated before any claim of non-repetition.

**Benchmark.** [4], [6], [10], [11], [12]

## 8. Detection efficiency and selection

**Question.** When a rate, luminosity or energy function, class fraction or distribution of host properties is inferred, was the detection efficiency measured by injecting synthetic events through the full search pipeline, and were the search cuts included?

**Why it matters.** Every survey samples the transient population incompletely, so each detected event stands for others that were missed. Recovery falls on bright regions of galaxies and in poor observing conditions, and radio-burst sensitivity depends strongly on burst width; DM cuts and real-time thresholds select further. Ignoring these biases rates and populations towards events that are easy to find.

**Resolved by.** Injection and recovery through the real-time pipeline, including interference excision and classifiers; efficiency given as a function of brightness or fluence, width, host surface brightness and observing conditions; search cuts stated; rates and distributions corrected with that efficiency.

**Benchmark.** [4], [13], [14]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | J. S. Bloom, S. R. Kulkarni and S. G. Djorgovski, The observed offset distribution of gamma-ray bursts from their host galaxies: a robust clue to the nature of the progenitors, Astron. J. 123, 1111–1148 (2002); read as arXiv:astro-ph/0010176 | doi:10.1086/338893 | full text | Secs. III.1 and IV.1 to IV.5: levels of astrometric tie, from about a milliarcsecond within one instrument to tens of milliarcseconds from ground to space images and about 300 mas for radio to optical. Sec. V: host assignment is partly subjective. Sec. VI.1: chance probability from a Poisson model with the surface density of galaxies brighter than the host and an effective radius set by the localisation error, offset and half-light radius |
| 2 | T. Eftekhari and E. Berger, Associating fast radio bursts with their host galaxies, Astrophys. J. 849, 162 (2017); read as arXiv:1705.02998 | doi:10.3847/1538-4357/aa90b9 | full text | Sec. II: chance coincidence from galaxy number counts and a search radius from localisation, offset and half-light radius; dwarf hosts at moderate redshift need localisation of a few tenths of an arcsecond. Sec. III: DM gives a maximum redshift that trims candidates, useful only at modest DM; host and local contributions not generally known. Sec. V: faint hosts beyond spectroscopic reach |
| 3 | K. Aggarwal, T. Budavári, A. T. Deller, T. Eftekhari, C. W. James, J. X. Prochaska and S. P. Tendulkar, Probabilistic association of transients to their hosts (PATH), Astrophys. J. 911, 95 (2021); read as arXiv:2102.10627 | doi:10.3847/1538-4357/abe8d2 | full text | Sec. II: chance-coincidence probability gives no likelihood or ranking of several candidates and uses a semi-arbitrary radius. Sec. IV: priors on galaxy brightness, offset and an unseen host. Sec. V.2: results depend on the offset distribution; a zero unseen-host prior assigns hosts even when the true host is undetected; the 0.95 threshold is arbitrary and all associations are uncertain to some degree |
| 4 | E. Petroff, J. W. T. Hessels and D. R. Lorimer, Fast radio bursts, Astron. Astrophys. Rev. 27, 4 (2019); read as arXiv:1904.07947 | doi:10.1007/s00159-019-0116-6 | full text | Secs. 1.1, 4.1.1 and 4.1.8: interference can mimic the dispersive sweep; signals in many separated beams traced to local sources; multibeam checks reject them. Sec. 2.2.1: DM split into Galactic, intergalactic and host parts; Galactic models uncertain at tens of per cent; DM-to-redshift rule called crude. Secs. 4.3.1 and 4.3.2: single-dish positions limited to the beam, often arcminutes; elongated beams of linear arrays. Secs. 6.5, 6.6 and 7.1: DM search cuts and wide or narrow-band bursts that searches miss; simulations needed to infer intrinsic distributions. Sec. 6.7: a single burst does not rule out repetition |
| 5 | G. Ashton, E. Burns, T. Dal Canton, T. Dent, H.-B. Eggenstein, A. B. Nielsen, R. Prix, M. Was and S. J. Zhu, Coincident detection significance in multimessenger astronomy, Astrophys. J. 860, 6 (2018); read as arXiv:1712.05392 | doi:10.3847/1538-4357/aabfd2 | full text | Sec. I: unrelated detections can coincide, and a p-value is not the probability that the events are unrelated. Secs. III.1.1 to III.1.3: odds of a common source combine the temporal window, the spatial overlap of the localisations and the background rates; wider windows or higher background rates lower the significance |
| 6 | P. S. Cowperthwaite and E. Berger, A comprehensive study of detectability and contamination in deep rapid optical searches for gravitational wave counterparts, Astrophys. J. 814, 25 (2015); read as arXiv:1503.07869 | doi:10.1088/0004-637X/814/1/25 | full text | Secs. II.8 to II.10: contaminating classes including stellar flares and nuclear variability; hundreds of type Ia supernovae expected in a search of about 100 square degrees. Secs. III and IV.2: colour, rise-time and brightness-change cuts and detection on more than one night reject most contaminants |
| 7 | D. A. Duev et al., Real-bogus classification for the Zwicky Transient Facility using deep learning, Mon. Not. R. Astron. Soc. 489, 3582–3590 (2019); read as arXiv:1907.11259 | doi:10.1093/mnras/stz2357 | full text | Sec. 1: difference images contain false detections from radiation hits, optical ghosts, registration errors and misestimated noise. Sec. 2.1: early bogus examples collected to filter typical artefacts such as those from bright stars. Secs. 2.2 and 3.3: the score threshold trades false-positive against false-negative rates, chosen per science case |
| 8 | A. Gal-Yam, Observational and physical classification of supernovae, in Handbook of Supernovae, ed. A. W. Alsabti and P. Murdin, pp. 195–237 (Springer, 2017); read as arXiv:1611.09353 | doi:10.1007/978-3-319-21846-5_35 | full text | Secs. 1 and 3.3: classes defined by silicon, helium and other peak spectral lines, type Ic by the absence of hydrogen and helium. Sec. 4.1: short-lived early flash-ionised lines. Sec. 5: late emergence of hydrogen. Secs. 3.1 and 3.5: events reclassified. Figure captions in Secs. 3.1 and 4.3: narrow host-galaxy lines in the spectra and their subtraction. Sec. 6: class names to keep assumptions about physical origin separate from observed properties |
| 9 | S. Blondin and J. L. Tonry, Determining the type, redshift, and age of a supernova spectrum, Astrophys. J. 666, 1024–1047 (2007); read as arXiv:0709.4488 | doi:10.1086/520494 | full text | Secs. III.1 and III.2: correlation height and overlap combined into a quality parameter with a threshold. Sec. IV.1: more type Ia templates than all other types together, so low signal-to-noise spectra risk being classed as Ia. Sec. V.5: redshift and age accuracy fall at low signal-to-noise, with host-galaxy contamination and as rest-frame overlap shrinks. Sec. III.2: correlations with small overlap are meaningless |
| 10 | R. Kessler et al., Results from the Supernova Photometric Classification Challenge, Publ. Astron. Soc. Pac. 122, 1415–1431 (2010); read as arXiv:1008.1024 | doi:10.1086/657607 | full text | Secs. II.5 and V: the spectroscopic training subset was biased towards type Ia and bright events, and performance was worse on the unconfirmed sample. Sec. IV: efficiency and purity as figures of merit. Sec. V: a type Ic and a type II-P template were frequent false Ia tags |
| 11 | O. Bromberg, E. Nakar, T. Piran and R. Sari, Short versus long and collapsars versus non-collapsars: a quantitative classification of gamma-ray bursts, Astrophys. J. 764, 179 (2013); read as arXiv:1210.0068 | doi:10.1088/0004-637X/764/2/179 | full text | Throughout: duration distributions depend on the detector's band, so the duration at which the two classes are equally likely differs between instruments; a burst of a given duration has a class probability, not a firm class, and no firm conclusion follows from a single burst |
| 12 | S. Gezari, Tidal disruption events, Annu. Rev. Astron. Astrophys. 59, 21–58 (2021); read as arXiv:2104.14580 | doi:10.1146/annurev-astro-111720-030029 | full text | Sec. 2: nuclear transients treated as tidal disruptions only after excluding an active nucleus or a supernova; variable active nuclei can mimic flares. Sec. 2.1: candidates with earlier evidence of an active nucleus, or bright before the flare, set aside. Secs. 2.2 and 2.3: inactive hosts and a blue colour without evolution used to select; a candidate later doubted after mid-infrared variability |
| 13 | C. Frohmaier, M. Sullivan, P. E. Nugent, D. A. Goldstein and J. DeRose, Real-time recovery efficiencies and performance of the Palomar Transient Factory's transient discovery pipeline, Astrophys. J. Suppl. Ser. 230, 4 (2017); read as arXiv:1704.02951 | doi:10.3847/1538-4365/aa6d70 | full text | Sec. I: every survey samples transients incompletely, which biases rates, luminosity functions and host studies unless corrected. Sec. II.2: synthetic sources injected into real images. Sec. III.1: recovery falls with host surface brightness, poor seeing and bright sky |
| 14 | M. Merryfield et al., An injection system for the CHIME/FRB experiment, Astron. J. 165, 152 (2023); read as arXiv:2206.14079 | doi:10.3847/1538-3881/ac9ab5 | abstract | Abstract: selection effects bias the observed burst population; synthetic bursts injected into the real-time pipeline map intrinsic properties to detection; sensitivity depends strongly on burst width, and interference classifiers could be retrained to recover wide bursts |
