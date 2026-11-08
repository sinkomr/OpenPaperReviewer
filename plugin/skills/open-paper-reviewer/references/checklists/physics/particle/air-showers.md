---
id: T-AIR-SHOWERS
name: Cosmic-ray and air-shower arrays
type: technique
field: physics/particle
applies_when: the paper uses a ground array of particle detectors, fluorescence or Cherenkov telescopes to reconstruct extensive air showers, and reports a cosmic-ray energy spectrum, mass composition, depth of shower maximum, muon content, arrival-direction anisotropy or a test of hadronic interaction models
version: "0.1"
---

# Cosmic-ray and air-shower arrays

## 1. Event selection and shower reconstruction

**Question.** Which conditions must an event meet to be used (minimum number of triggered stations, the station with the largest signal surrounded by working stations, zenith-angle range, quality cuts on the telescope profile), and what angular and core-position resolution and which lateral distribution function does the paper use for that selection?

**Why it matters.** Showers that land near the edge of the array or next to inactive stations are poorly contained, and their core position, shower size and direction can be biased. The angular resolution of a surface array depends strongly on the number of stations hit, and the assumed lateral distribution function enters the shower-size estimate on which the energy rests.

**Resolved by.** The selection stated in full, with a containment condition such as a working hexagon of stations around the largest signal; angular and core resolution given as a function of station multiplicity or energy; the lateral distribution function stated and the effect of changing it included in the systematic uncertainty.

**Benchmark.** [1], [2]

## 2. Energy estimator and absolute energy scale

**Question.** How is the measured shower size converted to energy: is the absolute scale set by a calorimetric measurement of the longitudinal profile (fluorescence or Cherenkov light), or by simulation; how is the shower size corrected for attenuation with zenith angle; and how large is the energy-scale uncertainty and what are its components?

**Why it matters.** An energy assigned from simulated showers depends on the hadronic interaction model and on the composition assumed. A calorimetric energy needs the absolute telescope calibration, the fluorescence yield, the atmospheric transmission and a correction for energy carried away by neutrinos and muons, each of which adds to an overall scale uncertainty of order 10 to 15%. Because the spectrum is steep, a scale shift of that size changes the flux at a given energy by tens of per cent, and scales differ between experiments by a similar amount.

**Resolved by.** The calibration chain stated, for example a fit of the surface-detector estimator against fluorescence energies in a sample of hybrid events recorded in clear atmosphere; the zenith correction derived from data, as by the constant-intensity method; a table of energy-scale uncertainties with their sources; the flux uncertainty from the energy scale shown separately; comparisons with other experiments that allow for the difference in energy scales.

**Benchmark.** [1], [2], [3], [7]

## 3. Energy resolution and migration in a steep spectrum

**Question.** Does the paper give the energy resolution and bias as a function of energy, including near the trigger threshold, and correct the spectrum for events that migrate between energy bins?

**Why it matters.** With a steeply falling spectrum, resolution moves more events up into a bin from below than out of it, so an uncorrected spectrum is distorted, most of all where the resolution is poor. Near threshold, triggering favours upward fluctuations of the signal and showers of some primary types, so the bias depends on energy and on composition, and showers selected at a fixed size are enriched in light primaries.

**Resolved by.** Resolution and bias parameterised from data or validated simulation; a forward-folding or unfolding correction with its size and uncertainty stated; spectral fits restricted to energies where the detector is fully efficient, or a composition-dependent efficiency treated as a systematic uncertainty below that.

**Benchmark.** [2], [3]

## 4. Exposure and directional exposure

**Question.** Above what energy is the array fully efficient for all primary types, how is the exposure computed (from the geometric aperture of active cells and the live time, or from simulation), what is its uncertainty, and for arrival-direction results, how are variations of the exposure with time and direction handled?

**Why it matters.** Above full efficiency the exposure follows from geometry and the record of working stations; below it, the exposure depends on simulation and on the assumed composition. Changes in the number of active stations with time, together with weather effects on trigger efficiency, imprint modulations of a few per cent on the event rate that can mimic or hide an anisotropy.

**Resolved by.** The full-efficiency threshold demonstrated with data or simulation for light and heavy primaries; the exposure computed from the time history of active cells, with its uncertainty and the detector uptime stated; for anisotropy studies, events weighted for the exposure in each sidereal-time bin or a differential method, such as comparing eastward and westward events, that cancels direction-independent rate variations, with the result checked at the solar and antisidereal frequencies.

**Benchmark.** [1], [2], [4]

## 5. Atmospheric conditions and long-term stability

**Question.** Are the reconstructed quantities corrected for changes in atmospheric pressure and air density and for the geomagnetic field, are telescope data restricted to, or corrected for, measured aerosol and cloud conditions, and is the stability of the detector response over the data-taking period shown?

**Why it matters.** Pressure changes how far a shower has developed when it reaches the ground, and air density changes its lateral spread, so the signal at a fixed distance from the core varies with weather; this produces seasonal and daily modulations of the event rate and a systematic error in the energy if uncorrected. Aerosols and clouds change the light that reaches the telescopes, and slow drifts in detector calibration can shift the energy scale with time.

**Resolved by.** Weather and geomagnetic corrections stated with their size; atmospheric monitoring described and the selection of telescope data on aerosol optical depth and cloud cover given; spectra or mean energies compared between time periods, seasons and zenith-angle bands and shown to agree within the stated uncertainties.

**Benchmark.** [1], [2], [4], [5]

## 6. Depth of shower maximum: acceptance and resolution

**Question.** For Xmax results, how does the paper handle the limited field of view of the telescopes and the Xmax resolution: by a fiducial selection that leaves the distribution unbiased, or by quoting detector-level values that must be compared with simulations passed through the same detector; and are the acceptance and resolution published?

**Why it matters.** A telescope sees only part of the atmosphere, so showers with very shallow or very deep maxima are lost and the tails of the Xmax distribution are undersampled, which shifts the mean and narrows the width. The width also includes the detector resolution. Means corrected for acceptance and means quoted at detector level cannot be compared directly, between experiments or with models, without a common treatment.

**Resolved by.** A fiducial field-of-view selection with the residual bias stated, or a full forward-folding of simulated showers through detector, atmosphere and reconstruction; the resolution estimated from a full detector simulation, checked with showers seen by two telescope sites, and subtracted from the width; acceptance and resolution given as functions of energy so that others can fold predictions; the systematic uncertainty on the Xmax scale stated with its components.

**Benchmark.** [3], [6], [7]

## 7. Mass composition and dependence on hadronic interaction models

**Question.** When Xmax or muon observables are converted to ⟨ln A⟩, its variance or fractions of primary types, does the paper give the result for each of several current hadronic interaction models, state how much the conclusion changes between them, and check that each model gives a physically allowed result?

**Why it matters.** The conversion relies on air-shower simulations whose hadronic models are extrapolated beyond collider energies and into the forward region that colliders measure poorly. Different models give ⟨ln A⟩ values that differ by several tenths from Xmax, and by more from ground-particle observables, and a model can yield an unphysical result, such as a negative variance of ln A, which is evidence against that model rather than a measurement of composition.

**Resolved by.** The measured observables reported separately from their interpretation; the interpretation given for more than one model with the spread shown; the energy-scale and Xmax-scale uncertainties propagated into ⟨ln A⟩; conclusions about composition that hold for all models considered, or that are stated as model-dependent.

**Benchmark.** [3], [6], [8]

## 8. Muon content and the reliability of simulations

**Question.** Where a claim rests on the muon content of showers, or on any quantity whose value is taken from simulation, does the paper allow for the known excess of muons in data over current simulations, and does it test the simulations against independent observables of the same showers?

**Why it matters.** Current hadronic models predict fewer muons than are observed, with a deficit that grows with energy and that differs between models. The muon number depends strongly on how energy is shared between charged and neutral pions in each interaction, so composition inferred from muons, and energies assigned by arrays that rely on simulation, inherit this uncertainty.

**Resolved by.** Muon measurements corrected for detector effects and compared with several models; composition from muons checked against composition from Xmax; tests that use the longitudinal profile and the ground signal of the same events, so that the simulation is constrained independently of the energy scale; any rescaling of the simulated muon number stated with its uncertainty.

**Benchmark.** [3], [8], [9]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | The Pierre Auger Collaboration (A. Aab et al.), The Pierre Auger Cosmic Ray Observatory, Nucl. Instrum. Methods Phys. Res. A 798, 172 (2015); read as arXiv:1502.01323 | doi:10.1016/j.nima.2015.06.058 |
| 2 | The Pierre Auger Collaboration (A. Aab et al.), Measurement of the cosmic-ray energy spectrum above 2.5×10^18 eV using the Pierre Auger Observatory, Phys. Rev. D 102, 062005 (2020); read as arXiv:2008.06486 | doi:10.1103/PhysRevD.102.062005 |
| 3 | K.-H. Kampert and M. Unger, Measurements of the cosmic ray composition with air shower experiments, Astropart. Phys. 35, 660 (2012); read as arXiv:1201.0018 | doi:10.1016/j.astropartphys.2012.02.004 |
| 4 | The Pierre Auger Collaboration (A. Aab et al.), Cosmic-ray anisotropies in right ascension measured by the Pierre Auger Observatory, Astrophys. J. 891, 142 (2020); read as arXiv:2002.06172 | doi:10.3847/1538-4357/ab7236 |
| 5 | The Pierre Auger Collaboration (J. Abraham et al.), Atmospheric effects on extensive air showers observed with the surface detector of the Pierre Auger Observatory, Astropart. Phys. 32, 89 (2009); read as arXiv:0906.5497 | doi:10.1016/j.astropartphys.2009.06.004 |
| 6 | The Pierre Auger Collaboration (A. Aab et al.), Depth of maximum of air-shower profiles at the Pierre Auger Observatory. I. Measurements at energies above 10^17.8 eV, Phys. Rev. D 90, 122005 (2014); read as arXiv:1409.4809 | doi:10.1103/PhysRevD.90.122005 |
| 7 | R. Abbasi et al., for the Pierre Auger and Telescope Array Collaborations, Report of the working group on the composition of ultra high energy cosmic rays, JPS Conf. Proc. 9, 010016 (2016); read as arXiv:1503.07540 | doi:10.7566/JPSCP.9.010016 |
| 8 | J. Albrecht et al., The muon puzzle in cosmic-ray induced air showers and its connection to the Large Hadron Collider, Astrophys. Space Sci. 367, 27 (2022); read as arXiv:2105.06148 | doi:10.1007/s10509-022-04054-5 |
| 9 | The Pierre Auger Collaboration (A. Aab et al.), Testing hadronic interactions at ultrahigh energies with air showers measured by the Pierre Auger Observatory, Phys. Rev. Lett. 117, 192001 (2016) | doi:10.1103/PhysRevLett.117.192001 |
