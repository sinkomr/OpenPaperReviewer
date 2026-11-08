---
id: T-AXION-SEARCHES
name: Axion and hidden-sector searches
type: technique
field: physics/particle
applies_when: the paper reports a haloscope, helioscope, light-shining-through-walls or hidden-photon search, or bases a limit on, or a candidate for, an axion-photon coupling, an axion-like particle or a dark photon kinetic mixing on such data
version: "0.1"
---

# Axion and hidden-sector searches

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

| # | Reference | Identifier |
|---|---|---|
| 1 | B. M. Brubaker et al., HAYSTAC axion search analysis procedure, Phys. Rev. D 96, 123008 (2017); read as arXiv:1706.08388 | doi:10.1103/PhysRevD.96.123008 |
| 2 | P. Sikivie, Invisible axion search methods, Rev. Mod. Phys. 93, 015004 (2021); read as arXiv:2003.02206 | doi:10.1103/RevModPhys.93.015004 |
| 3 | N. Du et al. (ADMX Collaboration), Search for invisible axion dark matter with the Axion Dark Matter Experiment, Phys. Rev. Lett. 120, 151301 (2018); read as arXiv:1804.05750 | doi:10.1103/PhysRevLett.120.151301 |
| 4 | I. G. Irastorza and J. Redondo, New experimental approaches in the search for axion-like particles, Prog. Part. Nucl. Phys. 102, 89 (2018); read as arXiv:1801.08127 | doi:10.1016/j.ppnp.2018.05.003 |
| 5 | V. Anastassopoulos et al. (CAST Collaboration), New CAST limit on the axion-photon interaction, Nat. Phys. 13, 584 (2017); read as arXiv:1705.02290 | doi:10.1038/nphys4109 |
| 6 | J. Redondo and A. Ringwald, Light shining through walls, Contemp. Phys. 52, 211 (2011); read as arXiv:1011.3741 | doi:10.1080/00107514.2011.563516 |
| 7 | R. Bähre et al., Any light particle search II technical design report, JINST 8, T09001 (2013); read as arXiv:1302.5647 | doi:10.1088/1748-0221/8/09/T09001 |
| 8 | A. Caputo et al., Dark photon limits: a handbook, Phys. Rev. D 104, 095029 (2021); read as arXiv:2105.04565 | doi:10.1103/PhysRevD.104.095029 |
