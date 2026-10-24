---
id: T-LASER-PLASMA-ACCELERATION
name: Laser-plasma acceleration
type: technique
field: physics/plasma
applies_when: the paper reports electrons accelerated by a laser- or beam-driven plasma wakefield, or ions accelerated by an intense laser, and bases a claim about energy, energy spread, charge, divergence, emittance or stability on spectrometer, scintillator, image plate or track detector data
version: "0.1"
---

# Laser-plasma acceleration

Laser wakefield acceleration (LWFA), plasma wakefield acceleration driven by a particle beam (PWFA) and laser-driven ion acceleration, for example by target normal sheath acceleration (TNSA), are used to claim particle beams of a given energy, energy spread, charge, divergence and emittance from centimetre-scale or smaller plasmas. These quantities are inferred from single shots recorded on magnetic spectrometers, Thomson parabola spectrometers (TPS), scintillating screens, image plates (IP), radiochromic film (RCF) and CR-39 track detectors, from a source that varies from shot to shot.

## 1. Spectrometer energy scale and resolution

**Question.** How was the energy scale of the magnetic spectrometer obtained (measured field map or model, particle tracking, entrance angle assumed), what is its energy resolution at the quoted energies, and is a quoted energy spread larger than that resolution?

**Why it matters.** A dipole spectrometer maps position on a screen to energy only for a known field and a known entrance angle. Field models that misrepresent the fringe field can shift the energy scale by tens of percent at low energy, and a beam that enters at an angle that changes from shot to shot is assigned the wrong energy unless the angle is measured. The finite resolution of the spectrometer sets a floor, and a measured spread close to that floor is an upper limit, not a value.

**Resolved by.** The field measured, for example with a Hall probe, and used in the tracking; the entrance angle measured on each shot, for example with a second screen or a screen before the magnet, or limited by an aperture, with its effect on the energy estimated; the resolution given as a function of energy, including divergence; energy spreads near the resolution reported as upper limits.

**Benchmark.** [1], [2], [3]

## 2. Charge calibration of screens and image plates

**Question.** How was the signal on the scintillating screen or image plate converted to charge or particle number: which absolute calibration, for which screen or plate type and particle, how was it transferred to the imaging system used, and were the charge densities within the linear range?

**Why it matters.** Published absolute calibrations of the same screen types differ by about a factor of two, scintillators saturate at high charge density and lose efficiency after large accumulated doses, and the collection efficiency of the camera and optics enters the result directly. Image plate signal fades with the time between exposure and scanning, and the response per particle depends on the particle type and energy, so a calibration for one species or scanner does not carry over to another.

**Resolved by.** The calibration source and screen or plate type named, with its stated uncertainty; the transfer to the experiment made with a reference light source or a cross-calibration on the same shots; peak charge densities shown to be below the onset of saturation; for image plates, the scan delay stated and corrected, and a response function for the particle, energy range and scanner used.

**Benchmark.** [4], [5], [6]

## 3. Divergence and emittance

**Question.** How were divergence and emittance measured (screen before the magnet, pepper-pot mask, quadrupole scan, energy-resolved focusing), is the emittance stated as projected or slice and as normalised with or without the energy spread, and is the value above the resolution of the method?

**Why it matters.** Beams from plasma accelerators have percent-level energy spread, which makes the measured emittance depend on how the beam was transported and focused: chromatic effects in quadrupoles enlarge the projected emittance, and a quadrupole scan analysed without them can be biased. The usual conversion from geometric to normalised emittance holds only for small energy spread, and projected emittance exceeds slice emittance when beam properties vary along the bunch. Pepper-pot and screen-based methods have a resolution floor that very small source emittances can reach.

**Resolved by.** The method, the distance from the source and any optics between source and measurement stated; the energy spread at the measurement point given and included in the analysis; emittance stated as projected or slice, with the definition (rms or fitted) and the fraction of charge included; the resolution of the method estimated, and values at that level reported as upper limits; divergence given with its definition and energy dependence.

**Benchmark.** [7], [8], [9]

## 4. Ion species and detector response

**Question.** For ion spectra, how were species and charge states separated, what does each detector respond to, and how were saturation, the energy thresholds of the detector and background from X-rays and electrons handled?

**Why it matters.** A magnetic spectrometer selects by energy only and is adequate only when one species dominates, while a Thomson parabola separates ions by charge-to-mass ratio. RCF stacks give a coarse spectrum through the energy threshold of each layer, CR-39 tracks overlap and saturate at high flux or long etching, and spectrometers sample only the part of the beam that passes their entrance pinhole or slit. Image plates respond to X-rays and scattered particles near the ion trace as well as to the ions.

**Resolved by.** The detector for each species named, with its energy thresholds and calibration; traces of different species or charge states shown to be separated where the claim needs it; CR-39 track densities kept below overlap, or etching checked; background measured beside the trace and subtracted; the solid angle of the spectrometer stated, and any extrapolation to the whole beam justified with an angularly resolved measurement.

**Benchmark.** [6], [10]

## 5. Definition of the quoted energy

**Question.** Is the headline energy a peak, a mean or a maximum (cut-off) energy, how is it defined against the detector noise level, and how many particles or how much charge lie at that energy?

**Why it matters.** For broad, exponential-like spectra the maximum energy depends on the detection method, its sensitivity and the rule used to separate signal from background, so a higher cut-off can reflect a more sensitive detector rather than a better accelerator. A maximum energy or a narrow peak carrying few particles says little about the beam that applications can use.

**Resolved by.** The full absolutely calibrated spectrum shown, in particles or charge per unit energy; the rule defining any cut-off stated, together with the noise level and the number of particles at the cut-off; the charge within any quasi-monoenergetic peak given with the peak width; comparisons with earlier work made on calibrated spectra or conversion efficiency, not on cut-off energies alone.

**Benchmark.** [11]

## 6. Shot-to-shot variation and which shots are shown

**Question.** Are the energy, charge, divergence and pointing given as distributions over a run of shots under the stated conditions, what fraction of those shots shows the claimed feature, and where does any single shot shown sit within those distributions?

**Why it matters.** Shot-to-shot variation in plasma accelerators is large compared with conventional accelerators, reported as typically a few percent in energy, tens of percent in charge and around a milliradian in pointing, and it arises largely from uncontrolled injection by self-trapping and from small irregularities in the drive laser. A single shot from the best end of the distribution can therefore look very different from the typical beam.

**Resolved by.** The number of shots and the fraction showing the claimed feature stated; mean and spread of energy, charge, divergence and pointing over a run of consecutive shots; spectra shown as averages with their spread alongside any single shot; drive laser parameters recorded on each shot and correlated with the beam parameters.

**Benchmark.** [3], [12]

## 7. Drive laser and target conditions

**Question.** Does the paper give the drive laser parameters on target (energy, pulse duration, focal spot and the fraction of energy in it, temporal contrast and prepulse level) and the target parameters (gas density profile, or foil material, thickness and surface condition), with how each was measured?

**Why it matters.** The energy and number of accelerated particles depend strongly on these parameters. In ion acceleration, prepulse level and duration change the target before the main pulse arrives and strongly influence the maximum proton energy, and experiments that look similar can differ because these conditions are hard to control. In wakefield acceleration, small drifts in laser parameters drive drifts in electron energy.

**Resolved by.** Peak intensity derived from measured energy, duration and focal spot, not from nominal values; contrast measured over the relevant time window and stated; target density or thickness measured, with its uncertainty and, for gas targets, its profile; these parameters reported for the shots shown and their variation over the run.

**Benchmark.** [10], [11], [12]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | M. V. Ambat, I. A. Settle, J. Shamlian, R. Boni, H. G. Rinderknecht and J. L. Shaw, Assessment of errors in analytic modeling of permanent magnet electron spectrometers for laser-plasma accelerators, Rev. Sci. Instrum. 96 (2025); read as the OSTI record 3012997 | doi:10.1063/5.0281827 | abstract | Abstract: calibration sources are scarce, so Hall probe field measurements serve as the calibration standard; a field model that overestimates the fringe field gave absolute energy errors up to 60% below 80 MeV and under 8% above; a simple block model suffices if uncertainties up to 5% in absolute energy and 1% in resolution can be tolerated |
| 2 | C. I. Hojbota, H. T. Kim, J. H. Shin, C. Aniculaesei, B. S. Rao and C. H. Nam, Accurate single-shot measurement technique for the spectral distribution of GeV electron beams from a laser wakefield accelerator, AIP Adv. 9, 085229 (2019); read as arXiv:1907.02239 | doi:10.1063/1.5117311 | abstract | Abstract: a dipole spectrometer with several scintillating screens and trajectory tracking recovers beam angle, divergence and spectrum together from one shot, and is more accurate when shot-to-shot pointing fluctuations are significant |
| 3 | S. M. Hooker, Developments in laser-driven plasma accelerators, Nat. Photon. 7, 775–782 (2013); read as arXiv:1406.5118 | doi:10.1038/nphoton.2013.234 | full text | Sec. III.3: an early measured energy spread is given only as below the spectrometer resolution. Sec. III.4, Fig. 5: spectra shown as mean and standard deviation over many shots. Sec. V.1: typical shot-to-shot variation of 1–5% in energy, 5–50% in charge and 0.5–3 mrad in pointing, high compared with conventional accelerators, linked largely to self-trapping |
| 4 | A. Buck, K. Zeil, A. Popp, K. Schmid, A. Jochmann, S. D. Kraft, B. Hidding, T. Kudyakov, C. M. S. Sears, L. Veisz, S. Karsch, J. Pawelke, R. Sauerbrey, T. Cowan, F. Krausz and U. Schramm, Absolute charge calibration of scintillating screens for relativistic electron detection, Rev. Sci. Instrum. 81, 033301 (2010) | doi:10.1063/1.3310275 | abstract | Abstract: eight screens used for laser-plasma electrons calibrated with picosecond bunches from a linear accelerator; linear over several orders of magnitude, with saturation for some screens at about 10–100 pC/mm²; a constant light source as reference to transfer one calibration to other set-ups |
| 5 | T. Kurz, J. P. Couperus, J. M. Krämer, H. Ding, S. Kuschel, A. Köhler, O. Zarini, D. Hollatz, D. Schinkel, R. D'Arcy, J.-P. Schwinkendorf, J. Osterhoff, A. Irman, U. Schramm and S. Karsch, Calibration and cross-laboratory implementation of scintillating screens for electron bunch charge determination, Rev. Sci. Instrum. 89, 093303 (2018) | doi:10.1063/1.5041755 | abstract | Abstract (read as the Crossref record): linear response at low charge density with onset of saturation at nC/mm²; absolute calibration factor about half the earlier reference value, implying earlier charges may be overestimated; efficiency drops after long irradiation; a constant reference source for transfer between laboratories |
| 6 | D. Doria, P. Martin, H. Ahmed, A. Alejo, M. Cerchez, S. Ferguson, J. Fernandez-Tobias, J. S. Green, D. Gwynne, F. Hanton, J. Jarrett, D. A. Maclellan, A. McIlvenny, P. McKenna, J. A. Ruiz, M. Swantusch, O. Willi, S. Zhai, M. Borghesi and S. Kar, Calibration of BAS-TR image plate response to GeV gold ions, Rev. Sci. Instrum. 93, 033304 (2022); read as arXiv:2202.10385 | doi:10.1063/5.0079564 | full text | Sec. I and III.1: image plate response follows the energy deposited in the active layer, and model parameters depend on radiation type and plate; calibration against CR-39 behind a Thomson parabola that separates charge states. Sec. II: CR-39 etching checked to stop pits overlapping; background from X-rays and scattered ions near the trace. Sec. III: signal fades after exposure, so readings are corrected to a fixed scan delay |
| 7 | C. A. Lindstrøm and M. Thévenet, Emittance preservation in advanced accelerators, J. Instrum. 17, P05016 (2022); read as arXiv:2201.08876 | doi:10.1088/1748-0221/17/05/P05016 | full text | Sec. 1.2: definitions of rms normalised, slice, projected and multi-shot emittance; projected exceeds slice when properties vary along the bunch; the normalised-to-geometric relation holds exactly only for negligible energy spread. Sec. 3.2, Eq. (3.4): the relative growth of the squared projected emittance from chromaticity scales with the square of the energy spread, while slice emittance is unaffected |
| 8 | A. Mostacci, M. Bellaveglia, E. Chiadroni, A. Cianchi, M. Ferrario, D. Filippetto, G. Gatti and C. Ronsivalle, Chromatic effects in quadrupole scan emittance measurements, Phys. Rev. ST Accel. Beams 15, 082802 (2012) | doi:10.1103/PhysRevSTAB.15.082802 | abstract | Abstract: with significant energy spread, quadrupole scan emittance measurements may be affected depending on beam properties and quadrupole arrangement, motivated in part by beam transport in plasma-based accelerators; the error is evaluated for single and double quadrupole schemes |
| 9 | G. G. Manahan, E. Brunetti, C. Aniculaesei, M. P. Anania, S. Cipiccia, M. R. Islam, D. W. Grant, A. Subiel, R. P. Shanks, R. C. Issac, G. H. Welsh, S. M. Wiggins and D. A. Jaroszynski, Characterization of laser-driven single and double electron bunches with a permanent magnet quadrupole triplet and pepper-pot mask, New J. Phys. 16, 103006 (2014) | doi:10.1088/1367-2630/16/10/103006 | abstract | Abstract (read as the OpenAlex record): pepper-pot emittance of laser wakefield bunches; the source emittance of about 1 π mm mrad was resolution limited, and emittance grew about fivefold through the quadrupoles because of the energy spread |
| 10 | A. Macchi, M. Borghesi and M. Passoni, Ion acceleration by superintense laser-plasma interaction, Rev. Mod. Phys. 85, 751–793 (2013); read as arXiv:1302.1775 | doi:10.1103/RevModPhys.85.751 | full text | Sec. II.5: RCF layers respond above a depth-set energy threshold and give a coarse spectrum; CR-39 tracks overlap and saturate at high flux or long etching; magnetic spectrometers select by energy only and suit beams dominated by protons, while a Thomson parabola separates charge-to-mass ratios; spatial selection by slit or pinhole; image plates absolutely calibrated. Secs. III.4 and III.5.1: prepulse level and duration strongly influence maximum proton energy and can suppress acceleration from thin foils |
| 11 | A. Macchi, A review of laser-plasma ion acceleration, preprint arXiv:1712.06443 (2017) | doi:10.48550/arXiv.1712.06443 | full text | Sec. II introduction and Sec. V: the cut-off energy may be ambiguous for broad exponential-like spectra, depending on detection method, sensitivity and noise discrimination; calibrated differential spectra are a safer indicator. Sec. II.1: a higher cut-off may reflect detector sensitivity, with far fewer particles at the cut-off; conversion efficiencies compared. Sec. II.2: high contrast needed to avoid preplasma; hard-to-control conditions may explain variations between similar experiments |
| 12 | A. R. Maier, N. M. Delbos, T. Eichner, L. Hübner, S. Jalas, L. Jeppe, S. W. Jolly, M. Kirchen, V. Leroux, P. Messner, M. Schnepp, M. Trunk, P. A. Walker, C. Werle and P. Winkler, Decoding sources of energy variability in a laser-plasma accelerator, Phys. Rev. X 10, 031039 (2020) | doi:10.1103/PhysRevX.10.031039 | abstract | Abstract and popular summary: laser-plasma accelerators are very sensitive to small irregularities in the drive laser; correlating laser and electron-beam parameters over 100,000 consecutive shots identifies sources of energy drift and jitter and predicts the drift from measured laser parameters |
