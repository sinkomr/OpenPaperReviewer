---
id: T-INTEGRATED-PHOTONICS
name: Integrated photonics
type: technique
field: physics/optics-photonics
applies_when: the paper reports waveguide propagation loss, resonator quality factors, fibre-to-chip coupling or insertion loss, device footprint, fabrication yield or variation, or modulator figures of merit such as half-wave voltage, bandwidth, extinction ratio or energy per bit for a photonic integrated circuit
version: "0.1"
---

# Integrated photonics

## 1. Cut-back loss and its uncertainty

**Question.** When propagation loss, or the loss of a repeated component, is obtained by the cut-back method, how many structures and what range of lengths or component counts were measured, how was the device-to-device spread in fibre-to-chip coupling estimated, and is the fitted slope given with an uncertainty that includes that spread?

**Why it matters.** The cut-back slope rests on the assumption that every structure has the same coupling loss, but coupling commonly varies from device to device by a few tenths of a decibel and facet reflections add Fabry-Pérot fringes. When the loss being measured is small compared with that variation, the uncertainty of the slope can exceed the loss itself.

**Resolved by.** Transmission against length or count for several structures, with the linear fit and its uncertainty shown; the coupling spread measured on nominally identical reference waveguides and propagated into the result; the length range chosen so that the total loss difference is well above the coupling spread; fringes averaged or removed by a stated procedure; for very low losses, a method insensitive to coupling, such as a resonator comparison, used instead or as a check.

**Benchmark.** [1]

## 2. Whether the quoted loss represents the circuit

**Question.** Is the headline loss or Q the most probable value of a distribution over many resonances, devices and wafer positions, or a single best resonance, and does a loss derived from a short resonator agree with direct measurements on long waveguides at the wavelengths of interest?

**Why it matters.** Loss varies between resonances, devices and positions on a wafer, and a single exceptional resonance says little about what a circuit will see. Localised scattering defects become more likely as waveguide area grows, so a long spiral can show more loss than a short ring on the same wafer, and loss also changes with wavelength.

**Resolved by.** Histograms of intrinsic linewidth or loss over many resonances and devices, with the value quoted defined (most probable, mean or best); a wafer map or a statement of where the measured dies came from; loss measured on long waveguides compared with the resonator value and any difference explained; loss given across the wavelength range the claim concerns.

**Benchmark.** [2]

## 3. Coupling loss and what is excluded

**Question.** Is fibre-to-chip coupling loss stated per coupler, with the wavelength, polarisation, fibre type and method used to separate it from on-chip loss, and is it clear whether each quoted device loss includes or excludes the couplers?

**Why it matters.** Grating couplers are strongly wavelength and polarisation dependent, edge couplers have tight alignment tolerance, and coupling efficiency varies between devices. A device insertion loss quoted after subtracting coupler loss, or a coupler efficiency quoted at its peak wavelength only, cannot be compared with values defined differently.

**Resolved by.** Loss per coupler with its bandwidth (stating whether 1 dB or 3 dB) and polarisation-dependent loss; the reference structure or cut-back used to separate coupler and propagation loss; the spread over repeated alignments or nominally identical couplers; every device figure labelled as fibre-to-fibre or on-chip, with the subtracted terms named.

**Benchmark.** [1], [3]

## 4. Fabrication variation and tuning

**Question.** For resonant or interferometric devices, how far do the fabricated resonance wavelengths or operating points vary from design across devices and wafers, how was the device brought to its operating point, and is the tuning power counted in the device's power figures?

**Why it matters.** Nanometre-scale variation in waveguide geometry shifts ring resonances by nanometres, so the operating wavelength of a ring cannot be set by design alone. Heaters correct this and track ambient temperature, but at a cost that can be a large share of the power budget; a demonstration on one device tuned by hand does not show this cost.

**Resolved by.** The distribution of resonance wavelengths or bias points over many devices, ideally across a wafer; the tuning method and the power or trimming needed to reach the target wavelength reported; heater and temperature-control power included wherever energy or power consumption is quoted.

**Benchmark.** [4], [5]

## 5. Modulator figures of merit

**Question.** Are Vπ or the product of Vπ and length, insertion loss, extinction ratio and EO bandwidth reported for the same device at the same bias, wavelength and drive, with the footprint, and is bandwidth given as a measured EO response and not only as a demonstrated line rate?

**Why it matters.** The metrics trade against one another and depend on bias, so a single favourable figure says little; a combined figure such as the product of Vπ, length and loss, or the ratio of extinction ratio to insertion loss, is what allows comparison between devices. The line rate a modulator supports also depends on the modulation format and on equalisation in the drive or receiver, so it is not a substitute for the measured EO bandwidth.

**Resolved by.** A table of Vπ (or Vπ times length), insertion loss, extinction ratio, EO 3 dB bandwidth and footprint for one device, with bias, wavelength and drive amplitude stated; the EO frequency response shown; data-rate demonstrations accompanied by the format, any equalisation or signal processing, and the error-rate threshold; comparisons with other work made on the same combined figures.

**Benchmark.** [4]

## 6. Energy per bit

**Question.** How was the energy per bit obtained: calculated or measured, with which formula, capacitance and voltage swing, and does it include optical losses, the laser power required and any thermal tuning?

**Why it matters.** Energy per bit is commonly computed from the device capacitance and voltage swing, with conventions that differ by a factor of two or more depending on the data-pattern factor assumed, and the capacitance of wiring and of the driving transistor can exceed that of a small device. The electrical charging energy is only part of the total: a lossy or inefficient modulator needs more optical power from the laser, and resonant devices need tuning against temperature drift.

**Resolved by.** The formula used stated, including the data-pattern factor; capacitance measured or simulated for the actual device at its bias, with wiring and driver capacitance included or stated as excluded; the optical contribution and heater or temperature-control power included or given separately; energy figures compared only with others defined the same way.

**Benchmark.** [6]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | Y. Chen et al., Design and resonator-assisted characterization of high-performance lithium niobate waveguide crossings, Opt. Lett. 48, 2218 (2023); read as preprint arXiv:2303.01880 | doi:10.1364/OL.485780 |
| 2 | J. Liu et al., High-yield, wafer-scale fabrication of ultralow-loss, dispersion-engineered silicon nitride photonic circuits, Nat. Commun. 12, 2236 (2021); read as preprint arXiv:2005.13949 | doi:10.1038/s41467-021-21973-z |
| 3 | L. Cheng et al., Grating couplers on silicon photonics: design principles, emerging trends and practical issues, Micromachines 11, 666 (2020) | doi:10.3390/mi11070666 |
| 4 | A. Rahim et al., Taking silicon photonics modulators to a higher performance level: state-of-the-art and a review of new technologies, Adv. Photonics 3, 024003 (2021); read as the version in the Ghent University repository | doi:10.1117/1.AP.3.2.024003 |
| 5 | H. Jayatilleka et al., Post-fabrication trimming of silicon photonic ring resonators at wafer-scale, J. Lightwave Technol. 39, 5083 (2021); read as preprint arXiv:2203.03503 | doi:10.1109/JLT.2021.3079801 |
| 6 | D. A. B. Miller, Attojoule optoelectronics for low-energy information processing and communications, J. Lightwave Technol. 35, 346 (2017); read as preprint arXiv:1609.05510 | doi:10.1109/JLT.2017.2647779 |
