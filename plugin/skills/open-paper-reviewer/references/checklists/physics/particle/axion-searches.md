---
id: T-AXION-SEARCHES
name: Axion and hidden-sector searches
type: technique
field: physics/particle
applies_when: the paper reports a haloscope, helioscope, light-shining-through-walls or hidden-photon search, or bases a limit on, or a candidate for, an axion-photon coupling, an axion-like particle or a dark photon kinetic mixing on such data
version: "0.1"
---

# Axion and hidden-sector searches

These experiments are used to claim limits on, or candidate signals of, the coupling of axions and axion-like particles (ALPs) to photons, or the kinetic mixing of hidden (dark) photons with ordinary photons, over a range of masses. Haloscopes look for dark matter converting to photons in a resonant cavity in a magnetic field, helioscopes for solar axions converting to X-rays, and light-shining-through-walls (LSW) experiments for photons that convert to a weakly interacting particle and back across an opaque wall.

## 1. Inputs to the expected signal power

**Question.** For a haloscope, does the paper state how each input to the expected signal power was obtained (magnetic field, cavity volume, form factor, loaded quality factor, antenna coupling, losses between cavity and amplifier) and how the system noise temperature was measured and tracked over the scan, with an uncertainty for each?

**Why it matters.** The coupling that a scan can exclude follows directly from the expected signal power divided by the system noise temperature, so an error in any one input moves the whole limit. Some inputs, such as the form factor, usually come from a field simulation and not a measurement, and the noise temperature drifts as the cavity and amplifiers are tuned.

**Resolved by.** Each input stated with how it was found, measured quantities such as quality factor and coupling recorded for each tuning step, the noise temperature calibrated repeatedly during the run (for example by Y-factor measurements against a known thermal source) with the spread shown, and the combined uncertainty of the sensitivity given, including any input left out of it and the reason.

**Benchmark.** [1], [2], [3]

## 2. Signal efficiency of the analysis chain

**Question.** Does the paper show how much of a real signal survives the processing (baseline removal, filtering, combining and rebinning of spectra), and was that efficiency measured with synthetic signals passed through the full analysis?

**Why it matters.** The filters that remove the receiver baseline from each spectrum also remove part of a narrow signal, and combining spectra can correlate neighbouring bins. If the attenuation is not measured and corrected, the quoted limit is stronger than the data support.

**Resolved by.** The attenuation of the signal by each processing step quantified, with simulated or software-injected signals of known strength run through the same pipeline as the data and the correction applied to the limit; where possible, synthetic signals injected into the hardware at frequencies spread over the scan and shown to be recovered at the expected strength.

**Benchmark.** [1], [3]

## 3. Dark matter assumptions behind the limit

**Question.** Which local dark matter density, fraction of dark matter in the searched particle and signal lineshape (velocity distribution) does a haloscope limit assume, and does the paper show how the limit changes under other reasonable choices?

**Why it matters.** A haloscope limit on the coupling scales with the assumed local density and fraction, and different conventions for the density are in use, so limits from different searches are not comparable unless the assumptions match. A lineshape narrower than the true signal, or one in a different reference frame, overstates the sensitivity.

**Resolved by.** The density, fraction and lineshape stated with the limit; results under a second lineshape or density shown or the scaling given; earlier limits rescaled to the same assumptions before being compared; the limit worded as conditional on the particle making up the stated share of dark matter.

**Benchmark.** [1], [3], [4]

## 4. Candidates, rescans and tests of the signal's origin

**Question.** What threshold flagged candidates, how were candidates rescanned, and for any candidate that persisted, what tests showed whether it behaves as the searched signal (dependence on cavity tuning and on magnetic field) or comes from interference?

**Why it matters.** Scans over many frequency bins produce excess power by chance, and narrowband radio-frequency interference persists like a real signal. A genuine haloscope signal follows the cavity response as the cavity is detuned and scales with the square of the magnetic field, which interference does not.

**Resolved by.** The threshold and the confidence it was set to give stated, and fixed before candidates were examined; each candidate rescanned to at least the original sensitivity; persistent candidates tested by detuning the cavity, changing or switching off the field, or comparing with an independent measurement of the radio environment at the site, with the outcome of each test reported.

**Benchmark.** [1], [2], [3]

## 5. Scan coverage and gaps in the exclusion

**Question.** Does the exclusion plot show which frequencies or masses were actually covered at the stated sensitivity, and does the paper list ranges removed because of mode crossings, interference vetoes, cut spectra or injected test signals?

**Why it matters.** A haloscope scan is tuned in steps, and parts of the range are lost to other cavity modes, vetoed interference, discarded spectra and the frequencies of test injections. A limit drawn as a smooth band over the whole range can hide regions where the sensitivity is much weaker or absent.

**Resolved by.** The limit given bin by bin or as a curve that shows notches and gaps; each excluded range listed with its reason; the rules for discarding spectra stated, for example a cut on how far the noise in a spectrum exceeds the expected white noise; the number of spectra that contribute at each frequency shown or stated.

**Benchmark.** [1], [3]

## 6. Helioscope pointing, background and coherence

**Question.** For a helioscope, how were the pointing at the Sun, the background in the signal region and the efficiency of the X-ray optics and detector established, which solar flux model enters the limit, and over what mass range is the conversion coherent for the gas conditions used?

**Why it matters.** The signal is a small excess of X-rays during solar tracking over the background in the same detector region, so a background taken from a different region, time or condition can create or hide an excess. Conversion is coherent only while the phase difference between axion and photon over the magnet length is small, so in vacuum the sensitivity falls steeply above a mass of order 0.01 to 0.02 eV unless a buffer gas restores coherence.

**Resolved by.** Pointing accuracy checked by surveys or by imaging the Sun, with the accuracy stated relative to the solar disc; background taken from non-tracking periods in the signal region of the same detector, with its exposure; optics and detector efficiency calibrated with X-ray sources or a test beamline; the flux model and its uncertainty stated; the mass range of each limit matched to the gas pressures used.

**Benchmark.** [2], [4], [5]

## 7. Light-shining-through-walls leakage, cavities and checks

**Question.** For an LSW experiment, how is light leaking around or through the wall excluded, how were the power build-up and mode matching of the production and regeneration cavities measured, and which checks (magnet off, changed polarisation, detuned regeneration cavity, dark runs) were made?

**Why it matters.** The regenerated signal scales with the fourth power of the coupling, so the expected photon rate is tiny and a small leak of the primary or control light, or detector dark counts, can mimic it. Resonant regeneration helps only if both cavities resonate at the same frequency in the same spatial mode, so the gain assumed in the limit holds only if that matching is shown.

**Resolved by.** The light tightness of the wall and the suppression of control light quantified against the expected signal; detector efficiency and dark count rate measured; cavity build-up and mode overlap measured during data taking, not only by design; data compared with runs that have the magnet off, the polarisation rotated, the regeneration cavity detuned or the laser off; the mass range of the limit limited to where conversion stays coherent, or gaps filled by gas.

**Benchmark.** [2], [4], [6], [7]

## 8. Hidden photons: polarisation and recast limits

**Question.** When a limit on hidden photon kinetic mixing is set, or recast from an axion search, does the paper state the assumption about the hidden photon's polarisation, the direction to which the detector is sensitive, and the measurement times, and does it use the corresponding conversion factor?

**Why it matters.** A dark matter hidden photon produces a field along its own polarisation, so the signal depends on the angle between that polarisation and the detector's sensitive direction, which changes as the Earth rotates. Recasting an axion limit with an averaged angle factor can overstate the sensitivity when measurements are short compared with the coherence time or a day, and an axion search that vetoes candidates by switching off the magnet cannot be recast at all.

**Resolved by.** The polarisation scenario stated (fixed or randomised); the detector's location, orientation and the timing of measurements reported; the angle factor computed for that scenario and timing at the stated confidence level; no recast where the analysis relied on the magnetic field to accept or reject candidates; for LSW hidden-photon limits, the mass dependence of the conversion shown.

**Benchmark.** [6], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | B. M. Brubaker, L. Zhong, S. K. Lamoreaux, K. W. Lehnert and K. A. van Bibber, HAYSTAC axion search analysis procedure, Phys. Rev. D 96, 123008 (2017); read as arXiv:1706.08388 | doi:10.1103/PhysRevD.96.123008 | full text | Secs. II and VI.1: signal power depends on field squared, volume, form factor, loaded quality factor, coupling, loss and local density; noise temperature from Y-factor measurements repeated during the run. App. D: uncertainty budget, with the simulated form factor reliable to better than 10% but left out of it. Secs. V.1 and VIII.1: the baseline filter attenuates signals and correlates bins; attenuation found by simulation. App. F: hardware synthetic signals as a check, cut from the data. Sec. VII.1 and App. E: halo lineshape and density by convention; a wider lab-frame lineshape weakens the limit by about 20% (Sec. VII.1) to 25% (App. E). Fig. 8 caption: some earlier limits rescaled to the same density; notches from cut spectra, an intruder mode and injections. Secs. III and VIII.2: candidate threshold. Sec. IX.1: rescan to the original sensitivity and persistence; a footnote in Sec. IX: a persistent candidate would be tested by repeating the rescan at other field values |
| 2 | P. Sikivie, Invisible axion search methods, Rev. Mod. Phys. 93, 015004 (2021); read as arXiv:2003.02206 | doi:10.1103/RevModPhys.93.015004 | full text | Sec. IV.1-IV.2: haloscope signal power and radiometer signal-to-noise; candidates above threshold checked with more data, and told apart from environmental peaks by their dependence on cavity frequency and on field squared. Sec. VI.0.1: helioscope conversion coherent only for small phase over the magnet length, buffer gas extends the mass range, tracking time. Sec. VIII: LSW regenerated power with cavities on both sides, which must be tuned to the same frequency |
| 3 | N. Du et al. (ADMX Collaboration), Search for invisible axion dark matter with the Axion Dark Matter Experiment, Phys. Rev. Lett. 120, 151301 (2018); read as arXiv:1804.05750 | doi:10.1103/PhysRevLett.120.151301 | full text | Calibration paragraphs: noise temperature from on- and off-resonance noise fitted with a model of the receiver chain. Analysis paragraphs: many software signals injected into raw spectra to find the effect of background subtraction. Candidates above threshold rescanned; persistent candidates matched to signals in a measurement of external radio interference at the site and removed. Fig. 4: limits for two lineshapes, each with its own density, assuming the axion is all dark matter; a vetoed interference range and discarded spectra with excess noise |
| 4 | I. G. Irastorza and J. Redondo, New experimental approaches in the search for axion-like particles, Prog. Part. Nucl. Phys. 102, 89-159 (2018); read as arXiv:1801.08127 | doi:10.1016/j.ppnp.2018.05.003 | full text | Sec. 4.1: local dark matter density and its range, and the fraction of dark matter in axions as a parameter. Sec. 6.1: helioscope coherence and buffer gas, low-background X-ray detectors and optics, background from non-alignment periods. Sec. 5.1: LSW probability scales with the fourth power of coupling, field and length times cavity build-up; resonant regeneration needs mode matching and phase locking |
| 5 | V. Anastassopoulos et al. (CAST Collaboration), New CAST limit on the axion-photon interaction, Nat. Phys. 13, 584-590 (2017); read as arXiv:1705.02290 | doi:10.1038/nphys4109 | full text | Sec. II: background from non-tracking periods in the signal spot of the same detector; pointing checked by surveys and by filming the Sun; optics calibrated at an X-ray test facility, detector efficiency with an X-ray tube, whole system with an in-situ source. Sec. I: coherence lost above about 0.02 eV in vacuum; gas filling covers higher masses. Sec. III: parametrised solar Primakoff flux enters the likelihood |
| 6 | J. Redondo and A. Ringwald, Light shining through walls, Contemp. Phys. 52, 211-236 (2011); read as arXiv:1011.3741 | doi:10.1080/00107514.2011.563516 | full text | Sec. 4: LSW probability is the product of two conversion probabilities; backgrounds from ambient light, cosmic rays and detector noise. Fig. 6 caption: laser in a light-tight hut, detector in a dark cabinet. Sec. 4.2: checks with magnet on and off, polarisation and gas pressure. Secs. 3 and 4.2: loss of coherence at higher mass leaves gaps, filled with gas. Secs. 2.2 and 4.2: hidden photon LSW needs no field, and its conversion probability depends on the hidden photon mass, vanishing as the mass goes to zero |
| 7 | R. Bähre et al., Any light particle search II technical design report, JINST 8, T09001 (2013); read as arXiv:1302.5647 | doi:10.1088/1748-0221/8/09/T09001 | full text | Sec. 3.2.1-3.2.3: both cavities share frequency and spatial mode, with alignment tolerances and build-up kept near maximum; dichroic optics keep primary and control light from the detector. Sec. 3.1.2: checks with regeneration cavity build-up, magnets on and off, polarisation changes, detuned cavity dark frames and laser-off runs. Table 1: detector efficiency and dark count rate |
| 8 | A. Caputo, A. J. Millar, C. A. J. O'Hare and E. Vitagliano, Dark photon limits: a handbook, Phys. Rev. D 104, 095029 (2021); read as arXiv:2105.04565 | doi:10.1103/PhysRevD.104.095029 | full text | Sec. I: many dark photon limits are recast axion limits, and polarisation is the key difference; searches that veto with the magnetic field cannot be recast. Secs. III-V: fixed and randomised polarisation, the angle factor for axial and planar detectors. Sec. VI: daily modulation from Earth's rotation and dependence on location, orientation and timing. Sec. V.7 and Table 2 caption: details of orientation and timing often missing from papers |
