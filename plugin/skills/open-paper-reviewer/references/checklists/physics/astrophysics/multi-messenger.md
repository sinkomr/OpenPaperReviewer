---
id: CL-MULTI-MESSENGER
name: Claims of multi-messenger associations
type: claim
field: physics/astrophysics
applies_when: the paper claims that a neutrino, gravitational-wave, cosmic-ray or photon signal shares a source with a signal in another messenger, identifies a counterpart or host galaxy for such a signal, or reports its coincidence in time or direction with a catalogue, alert or transient
version: "0.1"
---

# Claims of multi-messenger associations

A multi-messenger association asserts that signals in two or more messengers, such as high-energy neutrinos, gravitational waves (GW), ultra-high-energy cosmic rays (UHECR) and electromagnetic radiation, come from the same astrophysical source. A careful demonstration shows that the coincidence in time, direction and distance is unlikely to arise by chance among everything that was searched, and that it is physically consistent with one source.

## 1. Search defined in advance and trials counted

**Question.** Were the candidate sources, alerts, time windows, energy thresholds and angular radii fixed before the coincidence was seen, and does the quoted significance account for every source, alert, catalogue and parameter value that was searched, with local and post-trial values both given?

**Why it matters.** A coincidence found by scanning over sources, windows, thresholds or radii is more likely than its local significance suggests, and the correction grows with the number of effectively independent places looked. Post-trial values for scanned excesses can be far below the local ones. When the counterpart is one of many similar sources or flares, the relevant number of trials is the number of such sources or flares, not one.

**Resolved by.** The search choices stated and dated relative to the data or alert; a count of all alerts, sources and parameter values examined, including those that gave nothing; a trials-corrected (global) significance derived from the full search, alongside the local value; where choices were made after seeing the data, that said plainly and the result described as a posteriori.

**Benchmark.** [3], [6], [7]

## 2. Chance-coincidence rate from the data

**Question.** How was the probability of a chance coincidence of this strength estimated, and was it obtained by repeating the same selection and statistic on background data, such as data shifted in time or scrambled in direction, rather than from an analytic estimate alone?

**Why it matters.** The number of unrelated events expected in the same window and region sets the meaning of a coincidence, and it depends on detector rates, sky coverage and selection cuts that analytic estimates can miss. A test statistic is only interpretable once its distribution under background has been built with the same procedure that produced the candidate.

**Resolved by.** The background distribution of the test statistic built from time-shifted, direction-scrambled or rotated data processed exactly like the candidate; the false-alarm probability or rate read from that distribution, with the number of background trials stated; any extrapolation beyond the loudest background trial stated as such; for Bayesian odds, the prior rates of joint and unrelated events stated and the odds calibrated against background.

**Benchmark.** [1], [2]

## 3. Significance of each messenger on its own

**Question.** What is the probability that each individual signal is astrophysical rather than detector background, such as the astrophysical probability of a neutrino alert or the false-alarm rate of a GW candidate, and how does that probability enter the joint claim?

**Why it matters.** A coincidence between an astrophysical signal and a background event in the other messenger is a separate hypothesis from a common source, and it is often the more likely one. Many single neutrino alerts are more likely to be atmospheric than astrophysical, and some alerts are flagged by vetoes as probable background.

**Resolved by.** The astrophysical probability or false-alarm rate of each signal quoted from the instrument team's own estimate; the hypothesis that one signal is astrophysical and the other background tested explicitly alongside the hypotheses of a common source and of pure background; any veto or data-quality flag on the events reported.

**Benchmark.** [1], [2], [4]

## 4. Overlap of localisations

**Question.** Does the paper use the full localisation probability map of each signal, including systematic uncertainty in the reconstruction, to compute the spatial overlap, and does it state the area of each region at a stated containment level?

**Why it matters.** Localisation regions are often large, non-circular and multi-modal, and a circle or a statistical-only contour misstates how probable a given direction is. Contours that leave out reconstruction systematics are too small, so a true source can fall outside them while an unrelated one near their edge appears compatible. The strength of a spatial association depends on how much the probability distributions overlap, not on whether the source falls inside a contour.

**Resolved by.** The localisation maps used, with their version and containment level; systematic uncertainties included, for example by contours calibrated on simulations that vary detector parameters; an overlap integral or likelihood that weights by the probability densities, not a binary inside-or-outside test; the result shown to survive enlarged or alternative contours.

**Benchmark.** [1], [2], [4]

## 5. Time window and expected delays

**Question.** Is the coincidence time window, and any assumed delay between messengers, fixed before the data were examined and justified by a stated emission model, and is the window long enough to include plausible delays without being widened to capture the candidate?

**Why it matters.** Different messengers can be emitted or arrive at different times, so the window has to come from the expected emission physics. A wider window admits more plausible emission scenarios but also more chance coincidences, so a window chosen or widened after seeing the data inflates the significance.

**Resolved by.** The window and delay prior stated with the emission model or earlier search that sets them; the same window applied to the background estimate; for flares and long-lived transients, the definition of the flare period fixed independently of the coincident event; results shown for reasonable alternative windows.

**Benchmark.** [1], [2], [8]

## 6. Other candidates in the localisation region

**Question.** How many unrelated sources or transients of the claimed type, and of types that resemble it, are expected within the localisation region and time window, and how was the proposed counterpart distinguished from them?

**Why it matters.** Large localisation regions contain many unrelated objects, and in optical searches unrelated supernovae alone can outnumber the expected counterpart by orders of magnitude. Without the density of competing candidates, the presence of one plausible object in the region says little about association.

**Resolved by.** The expected number of unrelated sources or transients in the searched volume and time, from survey rates or catalogue densities; the selection that picked the counterpart stated, with properties such as colour, rise time, spectrum or variability that set it apart; for host galaxies, candidates ranked within the distance-resolved localisation, with the number considered given.

**Benchmark.** [5], [9]

## 7. Distance and energy consistency

**Question.** Are the distance, energy output and expected number of detected particles of the proposed source consistent with every messenger, for example the GW distance with the counterpart's redshift and the neutrino flux with the source's luminosity, and are estimates based on one or two events corrected for selection bias?

**Why it matters.** A common source must be at one distance and must produce each signal with a plausible energy budget, so inconsistent distances or energetics argue against the association. The flux inferred from one detected neutrino is biased high, because many fainter similar sources each have a small chance of producing a single event; this can make an association look implausible, or a model look excluded, when it is not.

**Resolved by.** The counterpart's distance compared with the distance-resolved localisation along its line of sight; expected event numbers computed from the source energetics, distance and detector effective area and compared with what was seen; single-event flux estimates treated as upper limits or corrected for the population of similar undetected sources.

**Benchmark.** [2], [6], [9]

## 8. Deflection of charged cosmic rays

**Question.** When cosmic-ray arrival directions are associated with sources, does the paper state the assumed composition or rigidity and magnetic field models, and does it show how the expected deflection compares with the angular scale of the association?

**Why it matters.** Charged cosmic rays are deflected by Galactic and extragalactic magnetic fields by an amount that scales inversely with rigidity, so heavier nuclei at a given energy are deflected more. Galactic field models remain uncertain, especially near the Galactic plane and at low rigidity, and extragalactic fields are poorly constrained, so arrival directions cannot be traced back to sources reliably in all cases. Magnetic fields also delay charged particles, which weakens timing coincidences with transient sources.

**Resolved by.** The composition or rigidity range assumed, with its observational basis; deflections estimated with more than one Galactic field model and their spread compared with the search radius; regions near the Galactic plane treated with care; no timing association claimed for charged particles without an estimate of the magnetic delay.

**Benchmark.** [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | G. Ashton, E. Burns, T. Dal Canton, T. Dent, H.-B. Eggenstein, A. B. Nielsen, R. Prix, M. Was and S. J. Zhu, Coincident detection significance in multimessenger astronomy, Astrophys. J. 860, 6 (2018); read as preprint arXiv:1712.05392 | doi:10.3847/1538-4357/aabfd2 | full text | Sec. II.1 and II.2 (Eqs. 14-15): noise hypotheses for each data set and how the single-messenger Bayes factors enter the joint result. Sec. II.2 (Eq. 11) and III.1.2: spatial association as an overlap integral of the sky posteriors. Sec. III.1.1: uniform prior on the delay between messengers over a stated window. Sec. III.1.3: prior odds built from Poisson rates of joint and single events. Sec. III.3: p-value approach with background from randomly rotated sky localisations |
| 2 | I. Bartos, D. Veske, A. Keivani, Z. Márka, S. Countryman, E. Blaufuss, C. Finley and S. Márka, Bayesian multimessenger search method for common sources of gravitational waves and high-energy neutrinos, Phys. Rev. D 100, 083017 (2019); read as preprint arXiv:1810.11467 | doi:10.1103/PhysRevD.100.083017 | full text | Secs. II to V: hypotheses of a common source, pure background, and chance coincidence of one astrophysical and one background signal. Sec. III.1 (Eqs. 18-19): source distance and neutrino emission energy set the expected Poisson number of neutrinos. Secs. III.2-III.3: GW sky map combined with each neutrino's directional uncertainty. Secs. III.2-III.3: time window of ±250 s adopted from earlier searches. Secs. IV.2-IV.3 and VI: background from time-shifted GW data and empirical neutrino densities, odds used as a test statistic with thresholds set on background, and no extrapolation beyond the loudest background trigger |
| 3 | E. Gross and O. Vitells, Trial factors for the look elsewhere effect in high energy physics, Eur. Phys. J. C 70, 525-530 (2010); read as preprint arXiv:1005.1891 | doi:10.1140/epjc/s10052-010-1470-8 | full text | Sec. 1: when the signal location is not known in advance, the significance must allow for an excess anywhere in the search range. Sec. 2.1: the trial factor as the ratio of global to local p-value, growing with the effective number of independent search regions and with the local significance |
| 4 | R. Abbasi et al. (IceCube Collaboration), IceCat-1: the IceCube Event Catalog of Alert Tracks, Astrophys. J. Suppl. Ser. 269, 25 (2023); read as preprint arXiv:2304.01174 | doi:10.3847/1538-4365/acfa95 | full text | Abstract and Sec. II.2: each alert carries a signalness, its probability of astrophysical origin, about 50% for Gold and 30% for Bronze on average. Sec. II.3: per-event false-alarm rate and expected background counts per stream. Sec. III: contours from log-likelihood thresholds calibrated on simulations that vary the ice model, so systematics enter the contour levels. Secs. III.1 and IV: alerts vetoed by the surface array are flagged as likely atmospheric background |
| 5 | P. S. Cowperthwaite and E. Berger, A comprehensive study of detectability and contamination in deep rapid optical searches for gravitational wave counterparts, Astrophys. J. 814, 25 (2015); read as preprint arXiv:1503.07869 | doi:10.1088/0004-637X/814/1/25 | full text | Sec. II.10 with Tables 1 and 2: in a 100 square-degree search, unrelated Type Ia supernovae are expected in the hundreds, with other fast transients also present. Abstract and conclusions: counterparts are separated from contaminants by colour and rise-time cuts |
| 6 | N. L. Strotjohann, M. Kowalski and A. Franckowiak, Eddington bias for cosmic neutrino sources, Astron. Astrophys. 622, L9 (2019); read as preprint arXiv:1809.06865 | doi:10.1051/0004-6361/201834750 | full text | Abstract and Secs. 2-4: a flux estimated from one detected neutrino overestimates the source, by orders of magnitude for numerous populations, because many fainter similar sources each have a small chance of one event; Sec. 4: single-event fluxes should be treated as upper limits; Secs. 1 and 4: the relevant trial factor involves the number of similar sources or flares; Sec. 4: emission models should not be rejected because of a low predicted flux |
| 7 | R. Alves Batista, J. Biteau, M. Bustamante, K. Dolag, R. Engel, K. Fang, K.-H. Kampert, D. Kostunin, M. Mostafa, K. Murase, F. Oikonomou, A. V. Olinto, M. I. Panasyuk, G. Sigl, A. M. Taylor and M. Unger, Open questions in cosmic-ray research at ultrahigh energies, Front. Astron. Space Sci. 6, 23 (2019) | doi:10.3389/fspas.2019.00023 | full text | Sec. 2.1: deflection falls with rigidity; catalogue and hotspot searches are penalised for scans over energy threshold and angular radius, with post-trial significances far below local ones. Sec. 3.1.2: deflection roughly inversely proportional to rigidity. Sec. 3.2.6: Galactic field models remain uncertain, model deflections agree only above about 20 EV and away from the plane; extragalactic fields poorly constrained and cause energy- and charge-dependent delays |
| 8 | B. Baret, I. Bartos, B. Bouhou, A. Corsi, I. Di Palma, C. Donzaud, V. Van Elewyck, C. Finley, G. Jones, A. Kouchner, S. Márka, Z. Márka, L. Moscoso, E. Chassande-Mottin, M. A. Papa, T. Pradier, P. Raffai, J. Rollins and P. Sutton, Bounding the time delay between high-energy neutrinos and gravitational-wave transients from gamma-ray bursts, Astropart. Phys. 35, 1-7 (2011); read as preprint arXiv:1101.4669 | doi:10.1016/j.astropartphys.2011.04.001 | full text | Secs. 1 to 3: the joint-search time window is derived from emission physics of gamma-ray bursts (durations, high-energy light curves, jet breakout, precursors), giving about ±500 s. Sec. 1: a window's length is a compromise between covering unknown emission mechanisms and keeping the neutrino background low |
| 9 | L. P. Singer, H.-Y. Chen, D. E. Holz, W. M. Farr, L. R. Price, V. Raymond, S. B. Cenko, N. Gehrels, J. Cannizzo, M. M. Kasliwal, S. Nissanke, M. Coughlin, B. Farr, A. L. Urban, S. Vitale, J. Veitch, P. Graff, C. P. L. Berry, S. Mohapatra and I. Mandel, Going the distance: mapping host galaxies of LIGO and Virgo sources in three dimensions using local cosmography and targeted follow-up, Astrophys. J. Lett. 829, L15 (2016); read as preprint arXiv:1603.07333 | doi:10.3847/2041-8205/829/1/L15 | full text | Secs. II and III: GW localisations carry a distance distribution for each sky pixel, so the distance varies across the map. Sec. IV: candidate host galaxies weighted by position in the three-dimensional credible volume, reducing the number of candidates compared with a sky region plus a single distance cut |
