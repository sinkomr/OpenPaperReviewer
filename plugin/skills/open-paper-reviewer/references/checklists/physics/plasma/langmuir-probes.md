---
id: T-LANGMUIR-PROBES
name: Langmuir probes
type: technique
field: physics/plasma
applies_when: the paper reports electron temperature, plasma density, plasma or floating potential, or an electron energy distribution measured with a single, double or emissive electrostatic probe, or bases a claim on a probe current-voltage characteristic
version: "0.1"
---

# Langmuir probes

## 1. Sheath regime and the ion collection model

**Question.** Does the paper give the probe dimensions and compare them with the Debye length and the collision mean free paths, and does it name the sheath or ion collection model (thin sheath, orbital motion limited, radial motion or other) used to turn the ion current into a density, with evidence that the plasma lies within that model's range of validity?

**Why it matters.** The ion current does not saturate, because the sheath and therefore the collecting area grow with bias by an amount that depends on the probe radius in Debye lengths. Different collection theories applied to the same curve can give densities that differ by a factor of two or more, up to an order of magnitude, and collisions outside the sheath can make a fitted density too high.

**Resolved by.** Probe radius and length, Debye length and mean free paths stated; the collection model named and shown to suit that regime, including its treatment of sheath expansion; the density compared with a second model, with the electron side of the curve or with an independent diagnostic, and the spread reported.

**Benchmark.** [1], [2], [3]

## 2. Electron temperature and the assumed distribution

**Question.** Over what range of bias was the electron temperature fitted, how was the ion current removed first, and does the paper show that the electron distribution is Maxwellian over that range, or else report the measured distribution? For a double probe, does it recognize which part of the distribution the fitted temperature describes?

**Why it matters.** The classical analysis returns a single temperature only for Maxwellian electrons. Non-Maxwellian and two-temperature distributions are common in gas discharges and at the edge of magnetic confinement devices, and the fitted temperature then depends on the bias range chosen. A double probe's temperature reflects only electrons energetic enough to reach the more negative electrode, so in a non-Maxwellian plasma it describes the slope of the distribution near the floating potential, not the bulk. A distribution obtained from the second derivative of the curve requires differentiating noisy data, and the smoothing used can distort its low-energy part and limit its dynamic range.

**Resolved by.** The electron current shown on a logarithmic scale with the fit range marked and the ion-current subtraction described; where the plot is not straight, the measured distribution reported with the differentiation method, energy resolution and dynamic range; temperature and density from integrals of the distribution compared with the classical values; a double-probe temperature checked against a single-probe distribution where the plasma may be non-Maxwellian.

**Benchmark.** [1], [4], [8], [13]

## 3. Plasma potential

**Question.** How was the plasma potential found (from the knee of the curve, from the zero of the second derivative, or with an emissive probe), and for an emissive probe, which technique was used and how was its offset from the plasma potential treated?

**Why it matters.** Locating the plasma potential on a Langmuir probe curve is uncertain, and the error passes into the electron density, the electron temperature and the energy scale of any distribution. The floating-point technique for emissive probes is expected to read about 1.5 times the electron temperature (in volts) below the plasma potential because of space charge around the emitting probe, and measured offsets of about twice the electron temperature have been reported, so the error grows with the electron temperature.

**Resolved by.** The method named, with an uncertainty for the potential; for a Langmuir probe, the potential located from the derivatives of the curve and not by eye; for an emissive probe, the technique (floating point, inflection point or separation point), the heating and emission level described, and floating-point values corrected for the expected offset or checked against the inflection-point technique.

**Benchmark.** [1], [4], [5], [6]

## 4. Radio-frequency and other fluctuations

**Question.** In a radio-frequency or otherwise fluctuating plasma, was the probe compensated, for example with filters tuned to the drive frequency and its harmonics, and does the paper show that the compensation was sufficient?

**Why it matters.** When the plasma potential oscillates relative to the probe, the time-averaged electron side of the curve is distorted while the ion side is nearly unaffected, so quantities taken from the electron side are in error. The distortion can be hard to see in the curve itself and becomes clear only in its second derivative.

**Resolved by.** The compensation design stated, with the tuned frequencies and the attenuation or impedance reached at the fundamental and harmonics; a test of adequacy, such as the second derivative shown or compensated and uncompensated curves compared; in a magnetized plasma, filter components shown not to saturate in the field.

**Benchmark.** [4], [7]

## 5. Magnetized plasmas

**Question.** When the plasma is magnetized, does the paper compare the probe dimensions with the electron and ion Larmor radii, state the probe orientation relative to the field, and use an analysis method valid for that degree of magnetization?

**Why it matters.** A magnetic field changes how electrons reach the probe, so the electron side of the curve no longer follows the unmagnetized theory and the apparent plasma potential is lowered. The second-derivative method for the distribution holds only in very weak fields, and stronger fields need other methods.

**Resolved by.** Larmor radii and probe size given and the orientation stated; temperature and potential taken from a part of the curve, or from a magnetized-probe method, that is valid at the stated field; the second-derivative method used only where the field is shown to be weak enough; results checked against an independent diagnostic where possible.

**Benchmark.** [4], [8], [9]

## 6. Surface contamination

**Question.** How was the probe surface cleaned before and during the measurements, and does the paper compare curves swept up and down in bias, or repeated over time, to show that there is no hysteresis?

**Why it matters.** Layers on the probe surface can carry a potential that changes during a sweep, which distorts the curve and can make electron energies appear higher than they are. Heating the probe is of limited help, and drawing large electron currents can damage the tip or change its surface.

**Resolved by.** The cleaning procedure stated, such as ion bombardment, heating or a pulsed bias technique; curves for both sweep directions overlaid and shown to agree; repeated curves shown to be stable over the measurement time; the bias above the plasma potential limited.

**Benchmark.** [4], [10]

## 7. Perturbation of the plasma by the probe

**Question.** Is the probe shown not to perturb the plasma: is its effective collecting area compared with the area of the chamber wall when it draws electron current, is the reference for a single probe stable and the circuit resistance accounted for, and is a monitor of the plasma shown to be unchanged while the probe is swept?

**Why it matters.** Current balance means that an electrode collecting electrons can pull the plasma potential towards its own bias and change the density, temperature and distribution it is meant to measure; a probe is non-perturbing only when its effective area is small compared with the wall area, by a threshold set by the electron-to-ion mass ratio. A single probe's readings are unreliable when the plasma potential follows a discharge electrode, whereas a floating double probe has little influence on the discharge. Resistance in the probe circuit, including the sheath at the reference electrode, also distorts the measured curve.

**Resolved by.** The ratio of effective probe area to wall area stated and compared with the mass-ratio threshold; the reference electrode for a single probe described, with the resistance of the probe circuit and its effect on the curve estimated, or a double probe used where no stable reference exists; a second probe or discharge monitor shown to be unaffected by the sweep; probe holder size given relative to the plasma.

**Benchmark.** [11], [12], [14]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | V. A. Godyak and B. M. Alexandrovich, Comparative analyses of plasma probe diagnostics techniques, J. Appl. Phys. 118, 233302 (2015); abstract read from the Crossref record | doi:10.1063/1.4937446 |
| 2 | F. F. Chen, Langmuir probe analysis for high density plasmas, Phys. Plasmas 8, 3029 (2001); abstract read from the Crossref record | doi:10.1063/1.1368874 |
| 3 | T. E. Sheridan, How big is a small Langmuir probe?, Phys. Plasmas 7, 3084 (2000); abstract read from the Crossref record | doi:10.1063/1.874162 |
| 4 | A. Caldarelli et al., Data processing techniques for ion and electron-energy distribution functions, Phys. Plasmas 30, 040501 (2023); read as preprint arXiv:2211.03254 | doi:10.1063/5.0133840 |
| 5 | J. P. Sheehan et al., A comparison of emissive probe techniques for electric potential measurements in a complex plasma, Phys. Plasmas 18, 073501 (2011); abstract read from the Crossref record | doi:10.1063/1.3601354 |
| 6 | J. P. Sheehan et al., Recommended practice for use of emissive probes in electric propulsion testing, J. Propul. Power 33, 614 (2017); abstract read on the Princeton University research portal | doi:10.2514/1.B35697 |
| 7 | A. P. Paranjpe et al., A tuned Langmuir probe for measurements in rf glow discharges, J. Appl. Phys. 67, 6718 (1990); abstract read from the Crossref record | doi:10.1063/1.345109 |
| 8 | Tsv. K. Popov, M. Dimitrova, P. Ivanova, J. Kovačič, T. Gyergyek, R. Dejarnac, J. Stöckel, M. A. Pedrosa, D. López-Bruna and C. Hidalgo, Advances in Langmuir probe diagnostics of the plasma potential and electron-energy distribution function in magnetized plasma, Plasma Sources Sci. Technol. 25, 033001 (2016); abstract read from the Crossref record | doi:10.1088/0963-0252/25/3/033001 |
| 9 | M. Sugawara, Electron probe current in a magnetized plasma, Phys. Fluids 9, 797 (1966); abstract read from the Crossref record | doi:10.1063/1.1761746 |
| 10 | E. P. Szuszczewicz and J. C. Holmes, Surface contamination of active electrodes in plasmas: Distortion of conventional Langmuir probe measurements, J. Appl. Phys. 46, 5134 (1975); abstract read from the Crossref record | doi:10.1063/1.321572 |
| 11 | S. D. Baalrud et al., Interaction of biased electrodes and plasmas: sheaths, double layers, and fireballs, Plasma Sources Sci. Technol. 29, 053001 (2020); read as preprint arXiv:1911.06424 | doi:10.1088/1361-6595/ab8177 |
| 12 | E. O. Johnson and L. Malter, A floating double probe method for measurements in gas discharges, Phys. Rev. 80, 58 (1950); abstract read on the APS journal page | doi:10.1103/PhysRev.80.58 |
| 13 | Z. Xiong et al., Reliability of double probe measurements in nanodusty plasmas, Plasma Sources Sci. Technol. 32, 035001 (2023); abstract read on the University of Minnesota research portal | doi:10.1088/1361-6595/acbcef |
| 14 | V. A. Godyak and V. I. Demidov, Probe measurements of electron-energy distributions in plasmas: what can we measure and how can we achieve reliable results?, J. Phys. D: Appl. Phys. 44, 233001 (2011); abstract read from the Crossref record | doi:10.1088/0022-3727/44/23/233001 |
