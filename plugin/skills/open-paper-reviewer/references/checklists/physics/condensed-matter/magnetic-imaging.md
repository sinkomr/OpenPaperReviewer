---
id: T-MAGNETIC-IMAGING
name: Local magnetic imaging
type: technique
field: physics/condensed-matter
applies_when: the paper images stray fields, magnetisation or current flow with nitrogen-vacancy magnetometry, scanning SQUID, Lorentz microscopy, electron holography, Kerr microscopy or X-ray magnetic microscopy, or bases a claim about domains, spin textures, local moments or current paths on such images
version: "0.1"
---

# Local magnetic imaging

Local magnetic imaging is used to claim the arrangement of magnetisation (domains, domain walls, vortices and other spin textures), the size of local moments, and the paths taken by electrical currents. The main methods are nitrogen-vacancy (NV) centre magnetometry, scanning superconducting quantum interference device (SQUID) microscopy including SQUID-on-tip, Lorentz transmission electron microscopy (TEM) and electron holography, magneto-optical Kerr effect (MOKE) microscopy, and X-ray magnetic circular dichroism (XMCD) imaging by photoemission electron microscopy (PEEM) or scanning transmission X-ray microscopy (STXM); none of them measures magnetisation directly, so each claim rests on a model that links the recorded signal to the source.

## 1. Sensor-to-sample distance and spatial resolution

**Question.** For NV and scanning SQUID images, does the paper state the distance between the sensor and the magnetic layer, say how it was determined and with what uncertainty, and compare the resulting resolution with the size of the features it claims to resolve?

**Why it matters.** The stray field of a feature smaller than the sensor-to-sample distance is strongly attenuated, so the distance, not the sensor size alone, sets the resolution of scanning NV and scanning SQUID images; in wide-field NV imaging with a camera, the optical diffraction limit restricts the resolution further. The quantitative values extracted from a stray-field map, such as a moment density, scale with the assumed distance, and an error in it passes almost directly into the result.

**Resolved by.** The distance stated with its uncertainty and the method used to find it, for example a fit to the stray field of a calibration edge or a reference structure with known moment, measured together with the sample; a stated resolution consistent with that distance and, for wide-field NV images, with the optical resolution; the result shown not to depend on the probe, for example by repeating it with a second sensor.

**Benchmark.** [1], [2], [3], [4], [8]

## 2. What the sensor measures and how it is converted to field

**Question.** Which field component does the sensor respond to, how was the sensor's orientation and response calibrated, and was the field at every pixel within the range where the conversion to field is valid?

**Why it matters.** An NV centre measures the projection of the field on its own axis, so the orientation must be known to convert the signal to a field. A large field component perpendicular to that axis mixes the spin states and quenches the resonance contrast and photoluminescence, so regions of strong field can appear dark or give wrong values; temperature drift also shifts the resonance and can mimic a field. A SQUID records flux through its loop, and the field follows only through the loop's effective area; a SQUID-on-tip read without a flux-locked feedback loop responds periodically and nonlinearly to flux, which limits the range over which signal and field are proportional.

**Resolved by.** The sensor axis measured, for example by resonance spectra in a calibrated applied field; the bias field and its alignment stated; the off-axis field estimated and shown to stay within the valid range, or affected regions marked; temperature stability during acquisition reported; for SQUID sensors, the loop's effective area or response function stated with how it was obtained, and, without flux feedback, the working point and the signal range treated as linear.

**Benchmark.** [1], [2], [3], [4], [8]

## 3. From stray field to magnetisation or current

**Question.** When a magnetisation or current density map is reconstructed from a measured field, does the paper state the assumptions (a thin source, a known and uniform magnetisation direction, current conservation), the filters and regularisation used, and how the reconstruction was checked?

**Why it matters.** Many different magnetisation patterns produce the same stray field, so a magnetisation map is unique only once its direction or form is assumed; a two-dimensional current density can be reconstructed uniquely, but the inversion amplifies noise at short length scales. A finite field of view, the choice of field component and unknown offsets cause edge artefacts and spurious background, and the filter that suppresses noise also sets the resolution of the map.

**Resolved by.** The measured field map shown next to the reconstruction; the assumptions and the filter cut-off stated and related to the sensor-to-sample distance; the reconstruction tested against a simulated field from a known source, or the total reconstructed current compared with the applied current; where the magnetisation direction is not known, the claim limited to what the field alone determines.

**Benchmark.** [1], [5]

## 4. Electron phase images

**Question.** For Lorentz TEM and electron holography, how was the magnetic contribution to the phase separated from the electrostatic one, which assumptions convert the phase into a magnetisation, and how were defocus, boundary conditions and the reference wave handled?

**Why it matters.** The electron phase integrates the in-plane induction along the whole beam path, including stray fields outside the specimen, and in holography it is usually dominated by the electrostatic phase from the specimen's thickness and composition, which must be separated, for example by recording a second data set with the specimen turned over. Phase retrieval from defocused images by the transport-of-intensity equation depends on the defocus step, boundary conditions and noise regularisation, and gives artefacts at long length scales. In holography, stray fields that reach the reference wave and linear phase ramps from processing can alter the apparent field.

**Resolved by.** The method used to isolate the magnetic phase stated and shown; specimen thickness measured where a magnetisation value is quoted, with the assumptions about in-plane magnetisation and stray field stated; for transport-of-intensity reconstructions, the defocus values, image alignment and boundary treatment given and the result checked at more than one defocus; for holography, the position of the reference wave relative to the specimen's stray field stated and any phase ramp justified.

**Benchmark.** [6], [7], [8]

## 5. Kerr contrast

**Question.** For Kerr microscopy, which magneto-optical geometry and polarisation were used, which magnetisation component does the contrast represent, and how was non-magnetic contrast removed?

**Why it matters.** Polar, longitudinal and transverse Kerr effects and the quadratic Voigt effect respond to different magnetisation components, and depending on the geometry several of them can contribute to one image at once. Wide-field Kerr images are usually difference images taken against a reference state, so the contrast is relative and its meaning depends on that reference. The resolution is limited by optical diffraction.

**Resolved by.** The plane of incidence, polarisation and analyser setting stated, together with the component they select; where the component matters, images in more than one geometry or a separation scheme that isolates it; the reference image and its magnetic state stated; claimed features larger than the optical resolution.

**Benchmark.** [8]

## 6. X-ray dichroic contrast

**Question.** For XMCD imaging by PEEM or STXM, does the paper state the photon direction relative to the sample, how the dichroic contrast was formed, and what depth of the sample the image represents?

**Why it matters.** XMCD contrast measures the projection of the local magnetisation on the photon propagation direction, so one image constrains only one component, and vector or three-dimensional claims need several sample orientations. Contrast is formed by comparing opposite helicities, or by normalising to a saturated reference, and both steps affect how much of the image reflects magnetisation. PEEM detects electrons from near the surface, while transmission methods average through the whole film, so in a layered or depth-varying sample the two can represent different parts of it.

**Resolved by.** The beam direction and incidence angle given; images at opposite helicities, or the normalisation used, described; for vector or three-dimensional claims, images at several sample orientations; the probing depth of the method compared with the layer thickness and stated where it bears on the claim; the absorption edge used named.

**Benchmark.** [8]

## 7. Conditions at the sample and influence of the probe

**Question.** What field and temperature did the sample experience during imaging, how were they measured, and does the paper show that the probe (laser light, electron or X-ray beam, sensor currents) did not change the magnetic state it reports?

**Why it matters.** Imaging conditions often differ from those of other measurements in the same paper: a TEM specimen sits in the field of the objective lens unless a field-free configuration is used, PEEM allows only limited applied fields, and an imaged state may depend on field history. Laser illumination for NV readout can heat the sample or generate photo-charges, electron beams can damage beam-sensitive materials, and dissipative sensor readout can disturb the system under study.

**Resolved by.** The field and temperature at the sample stated for each image, with the imaging mode that sets them, and the field history described; illumination power or beam dose given; images repeated at lower illumination or dose, or before and after exposure, showing the same state; imaging conditions matched to those of the measurements the images are compared with.

**Benchmark.** [2], [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | F. Casola, T. van der Sar and A. Yacoby, Probing condensed matter physics with magnetometry based on nitrogen-vacancy centres in diamond, Nat. Rev. Mater. 3, 17088 (2018); read as preprint arXiv:1804.08742 | doi:10.1038/natrevmats.2017.88 | full text | Box 1: the NV measures the field projection on its quantisation axis; fast modulations of magnetisation or current are suppressed at distances larger than their wavelength; downward continuation is hampered by noise at large wavevectors; an infinite number of textures give the same stray field, whereas a 2D current can be solved uniquely. Section on magnetic textures: reconstruction is an underconstrained inverse problem needing assumptions; a large field perpendicular to the NV axis quenches spin contrast, with misalignment tolerance under about 10 degrees above 100 G. Section on currents: inversion is noise-limited at high spatial frequency and regularisation is used |
| 2 | M. José Martínez-Pérez and D. Koelle, NanoSQUIDs: Basics & recent advances, Phys. Sci. Rev. 2, 20175001 (2017); read as preprint arXiv:1609.06182 | doi:10.1515/psr-2017-5001 | full text | Sec. I: field resolution is the flux noise divided by the effective area. Sec. II.C (dispersive readout): readout in the voltage state dissipates Joule power that might affect the magnetic system under study. Sec. V: resolution requires the sensor to approach the sample to a distance of the order of or smaller than its loop; Secs. V.A and V.B: ways of setting probe-to-sample distance for planar and SQUID-on-tip sensors |
| 3 | T. Hingant, J.-P. Tetienne, L. J. Martínez, K. Garcia, D. Ravelosona, J.-F. Roch and V. Jacques, Measuring the magnetic moment density in patterned ultrathin ferromagnets with submicrometer resolution, Phys. Rev. Applied 4, 014003 (2015); read as preprint arXiv:1503.00705 | doi:10.1103/PhysRevApplied.4.014003 | full text | Main text (edge-field model, Fig. 2 and fit) and Supplementary Material (fitting procedure): the edge stray-field peak scales with moment density over distance and its width with distance, so distance is fitted together with the moment density; NV axis angles measured by resonance spectra in a calibrated field; measurements with two NV probes of different orientation agree; uncertainties of the fixed inputs combined into the final value |
| 4 | L. Rondin, J.-P. Tetienne, T. Hingant, J.-F. Roch, P. Maletinsky and V. Jacques, Magnetometry with nitrogen-vacancy defects in diamond, Rep. Prog. Phys. 77, 056503 (2014); read as preprint arXiv:1311.5214 | doi:10.1088/0034-4885/77/5/056503 | full text | Secs. II.B.2 and II.B.3: the linear Zeeman relation holds only for transverse fields well below about 100 mT; strong off-axis fields mix spin states and reduce resonance contrast and photoluminescence. Sec. II.E.2: temperature shifts of the zero-field splitting are indistinguishable from field changes in the usual basis. Sec. III.A.2: resolving power set by probe-to-sample distance; magnetic bits resolved close to the sample are not resolved farther away; imaging by photoluminescence quenching is not quantitative |
| 5 | D. A. Broadway, S. E. Lillie, S. C. Scholten, D. Rohner, N. Dontschuk, P. Maletinsky, J.-P. Tetienne and L. C. L. Hollenberg, Improved current density and magnetization reconstruction through vector magnetic field measurements, Phys. Rev. Applied 14, 024076 (2020); read as preprint arXiv:2005.06788 | doi:10.1103/PhysRevApplied.14.024076 | full text | Secs. II.A and II.B: current reconstruction assumes a 2D source at known height, and from Bz alone also current continuity; singularities leave undetermined components such as the offset, and truncation of a finite image gives artefacts and a non-uniform background. Sec. II.C: integrated current compared with the applied current. Sec. III: magnetisation in a 2D plane at known height has infinitely many solutions unless its direction is known and uniform. Secs. IV.B and V: noise amplification in the transformation; a Hanning low-pass filter, with stricter filters reducing noise at the cost of resolution |
| 6 | M. Mitome, Transport of intensity equation method and its applications, Microscopy 70, 69–74 (2021); read on the publisher's site | doi:10.1093/jmicro/dfaa053 | full text | Abstract: artefacts in retrieved phase maps depend on experimental conditions, algorithms and boundary conditions. Secs. 3.2 and 3.3: periodic boundaries give low-frequency artefacts; the inverse Laplacian amplifies low-frequency noise, and a large Tikhonov parameter degrades the quantitative quality of the phase. Secs. 3.2 and 4.1: a long defocus helps low frequencies but degrades the estimate of the intensity derivative. Sec. 3.4: magnification difference, rotation and distortion between defocused images corrected |
| 7 | G. Pozzi, M. Beleggia, T. Kasama and R. E. Dunin-Borkowski, Interferometric methods for mapping static electric and magnetic fields, C. R. Physique 15, 126–139 (2014) | doi:10.1016/j.crhy.2014.01.005 | full text | Abstract and Sec. 5: holography maps projected electric and magnetic fields. Sec. 4: converting fringe spacing to induction times thickness assumes in-plane magnetisation and no fringing field. Secs. 3.3 and 5: the reference wave can be perturbed by long-range fields of the specimen and this must be taken into account; a linear phase ramp in a reconstruction may be misleading |
| 8 | D. V. Christensen et al., 2024 roadmap on magnetic microscopy techniques and their applications in materials science, J. Phys. Mater. 7, 032501 (2024); read as preprint arXiv:2401.04793 | doi:10.1088/2515-7639/ad31b5 | full text | Colour-centre transport section: imaging avoids heating or photo-induced charge only when illumination of the sample is negligible. Colour-centre microscopy section: wide-field NV resolution is set by the optical diffraction limit. Scanning SQUID section: SQUID-on-tip sensors do not operate in a flux-locked loop, limiting dynamic range and linearity. Lorentz TEM section: phase from the vector potential along the beam, retrieved by the transport-of-intensity equation from defocused images; a new objective-lens design was needed to isolate the sample from magnetic fields in an atomic-resolution STEM. Holography section: Lorentz modes are magnetic-field-free; projected in-plane flux density integrated along the beam; magnetic phase small compared with the electrostatic part; 360 degree tilt series separate the two; cooling mitigates beam damage. Kerr section: polar, longitudinal, transverse and quadratic Voigt effects set by geometry and can contribute together; diffraction-limited resolution; common difference imaging against a homogeneous reference. X-ray section: XMCD measures the projection of magnetisation on the photon direction; contrast by helicity reversal or normalisation to saturated images; PEEM surface-sensitive, transmission methods probe the full thickness; several orientations for 3D; applied fields limited in PEEM |
