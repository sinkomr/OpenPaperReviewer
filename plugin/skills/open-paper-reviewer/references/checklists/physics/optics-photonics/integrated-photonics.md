---
id: T-INTEGRATED-PHOTONICS
name: Integrated photonics
type: technique
field: physics/optics-photonics
applies_when: the paper reports waveguide propagation loss, resonator quality factors, fibre-to-chip coupling or insertion loss, device footprint, fabrication yield or variation, or modulator figures of merit such as half-wave voltage, bandwidth, extinction ratio or energy per bit for a photonic integrated circuit
version: "0.1"
---

# Integrated photonics

Measurements on photonic integrated circuits (PICs) are used to claim the propagation loss of on-chip waveguides, the intrinsic quality factor (Q) of resonators, the loss of couplers between fibre and chip, and the performance of active devices such as electro-optic modulators: half-wave voltage (Vπ), electro-optic (EO) bandwidth, extinction ratio (ER), insertion loss (IL), footprint and energy per bit. Each number is inferred from transmitted power at the chip's input and output, and so depends on how coupling, reflections and fabrication spread were handled.

## 1. Cut-back loss and its uncertainty

**Question.** When propagation loss, or the loss of a repeated component, is obtained by the cut-back method, how many structures and what range of lengths or component counts were measured, how was the device-to-device spread in fibre-to-chip coupling estimated, and is the fitted slope given with an uncertainty that includes that spread?

**Why it matters.** The cut-back slope rests on the assumption that every structure has the same coupling loss, but coupling commonly varies from device to device by a few tenths of a decibel and facet reflections add Fabry-Pérot fringes. When the loss being measured is small compared with that variation, the uncertainty of the slope can exceed the loss itself.

**Resolved by.** Transmission against length or count for several structures, with the linear fit and its uncertainty shown; the coupling spread measured on nominally identical reference waveguides and propagated into the result; the length range chosen so that the total loss difference is well above the coupling spread; fringes averaged or removed by a stated procedure; for very low losses, a method insensitive to coupling, such as a resonator comparison, used instead or as a check.

**Benchmark.** [1]

## 2. Loss from resonator linewidth

**Question.** When loss is derived from a resonator, does the paper separate intrinsic from loaded Q, state how the coupling regime (under- or over-coupled) was determined, and say how resonances that appear as doublets were fitted?

**Why it matters.** The loaded linewidth contains both intrinsic loss and coupling to the bus waveguide, and the same transmission dip depth can arise in the under- and over-coupled regimes, so amplitude data alone can assign the loss to the wrong term. Backscattering from fabrication imperfections couples the clockwise and counter-clockwise modes and splits a resonance into a doublet, which a single-resonance fit does not describe.

**Resolved by.** Loaded linewidth, extinction and the extracted intrinsic and coupling rates given for each quoted resonance; the coupling regime fixed by the phase response or another independent check, not by amplitude alone; split resonances fitted with a model of two coupled modes, or excluded by a stated rule; the frequency axis of the linewidth measurement calibrated, for example with modulation sidebands or a frequency comb, and cross-checked by an independent method such as cavity ring-down for the highest Q values.

**Benchmark.** [2], [3], [4]

## 3. Probe power, scan direction and laser linewidth

**Question.** At what optical power, scan speed and scan direction were resonances recorded, and is the laser linewidth well below the resonance linewidth being measured?

**Why it matters.** Light absorbed in the resonator heats it and shifts the resonance during the scan, even at low power for high-Q devices, so the line shape and apparent width change with scan direction and power. A laser whose own linewidth is comparable to the resonance broadens the measured line and understates Q.

**Resolved by.** Input or on-chip power stated; the same linewidth obtained at two or more powers and in both scan directions, or a symmetric Lorentzian line shape shown; the laser linewidth stated and shown to be much narrower than the resonance; for the narrowest lines, a method insensitive to these effects, such as a phase-sensitive radio-frequency measurement.

**Benchmark.** [3]

## 4. Whether the quoted loss represents the circuit

**Question.** Is the headline loss or Q the most probable value of a distribution over many resonances, devices and wafer positions, or a single best resonance, and does a loss derived from a short resonator agree with direct measurements on long waveguides at the wavelengths of interest?

**Why it matters.** Loss varies between resonances, devices and positions on a wafer, and a single exceptional resonance says little about what a circuit will see. Localised scattering defects become more likely as waveguide area grows, so a long spiral can show more loss than a short ring on the same wafer, and loss also changes with wavelength.

**Resolved by.** Histograms of intrinsic linewidth or loss over many resonances and devices, with the value quoted defined (most probable, mean or best); a wafer map or a statement of where the measured dies came from; loss measured on long waveguides compared with the resonator value and any difference explained; loss given across the wavelength range the claim concerns.

**Benchmark.** [2]

## 5. Coupling loss and what is excluded

**Question.** Is fibre-to-chip coupling loss stated per coupler, with the wavelength, polarisation, fibre type and method used to separate it from on-chip loss, and is it clear whether each quoted device loss includes or excludes the couplers?

**Why it matters.** Grating couplers are strongly wavelength and polarisation dependent, edge couplers have tight alignment tolerance, and coupling efficiency varies between devices. A device insertion loss quoted after subtracting coupler loss, or a coupler efficiency quoted at its peak wavelength only, cannot be compared with values defined differently.

**Resolved by.** Loss per coupler with its bandwidth (stating whether 1 dB or 3 dB) and polarisation-dependent loss; the reference structure or cut-back used to separate coupler and propagation loss; the spread over repeated alignments or nominally identical couplers; every device figure labelled as fibre-to-fibre or on-chip, with the subtracted terms named.

**Benchmark.** [1], [5]

## 6. Fabrication variation and tuning

**Question.** For resonant or interferometric devices, how far do the fabricated resonance wavelengths or operating points vary from design across devices and wafers, how was the device brought to its operating point, and is the tuning power counted in the device's power figures?

**Why it matters.** Nanometre-scale variation in waveguide geometry shifts ring resonances by nanometres, so the operating wavelength of a ring cannot be set by design alone. Heaters correct this and track ambient temperature, but at a cost that can be a large share of the power budget; a demonstration on one device tuned by hand does not show this cost.

**Resolved by.** The distribution of resonance wavelengths or bias points over many devices, ideally across a wafer; the tuning method and the power or trimming needed to reach the target wavelength reported; heater and temperature-control power included wherever energy or power consumption is quoted.

**Benchmark.** [6], [7]

## 7. Modulator figures of merit

**Question.** Are Vπ or the product of Vπ and length, insertion loss, extinction ratio and EO bandwidth reported for the same device at the same bias, wavelength and drive, with the footprint, and is bandwidth given as a measured EO response and not only as a demonstrated line rate?

**Why it matters.** The metrics trade against one another and depend on bias, so a single favourable figure says little; a combined figure such as the product of Vπ, length and loss, or the ratio of extinction ratio to insertion loss, is what allows comparison between devices. The line rate a modulator supports also depends on the modulation format and on equalisation in the drive or receiver, so it is not a substitute for the measured EO bandwidth.

**Resolved by.** A table of Vπ (or Vπ times length), insertion loss, extinction ratio, EO 3 dB bandwidth and footprint for one device, with bias, wavelength and drive amplitude stated; the EO frequency response shown; data-rate demonstrations accompanied by the format, any equalisation or signal processing, and the error-rate threshold; comparisons with other work made on the same combined figures.

**Benchmark.** [6]

## 8. Energy per bit

**Question.** How was the energy per bit obtained: calculated or measured, with which formula, capacitance and voltage swing, and does it include optical losses, the laser power required and any thermal tuning?

**Why it matters.** Energy per bit is commonly computed from the device capacitance and voltage swing, with conventions that differ by a factor of two or more depending on the data-pattern factor assumed, and the capacitance of wiring and of the driving transistor can exceed that of a small device. The electrical charging energy is only part of the total: a lossy or inefficient modulator needs more optical power from the laser, and resonant devices need tuning against temperature drift.

**Resolved by.** The formula used stated, including the data-pattern factor; capacitance measured or simulated for the actual device at its bias, with wiring and driver capacitance included or stated as excluded; the optical contribution and heater or temperature-control power included or given separately; energy figures compared only with others defined the same way.

**Benchmark.** [8]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | Y. Chen, K. Zhang, H. Feng, W. Sun and C. Wang, Design and resonator-assisted characterization of high-performance lithium niobate waveguide crossings, Opt. Lett. 48, 2218 (2023); read as preprint arXiv:2303.01880 | doi:10.1364/OL.485780 | full text | Introduction: in cut-back measurements fibre-chip coupling loss is much larger than a small component loss and varies between devices (commonly about ±0.4 dB), and facet Fabry-Pérot fringes add to the difficulty. Results: cut-back uncertainty combines fit scatter with coupling spread calibrated on reference waveguides; with five devices the uncertainty exceeded the loss being measured; a resonator Q comparison is not affected by coupling variation |
| 2 | J. Liu, G. Huang, R. N. Wang, J. He, A. S. Raja, T. Liu, N. J. Engelsen and T. J. Kippenberg, High-yield, wafer-scale fabrication of ultralow-loss, dispersion-engineered silicon nitride photonic circuits, Nat. Commun. 12, 2236 (2021); read as preprint arXiv:2005.13949 | doi:10.1038/s41467-021-21973-z | full text | "Statistical analysis of microresonator Q factors" and Fig. 3: intrinsic and coupling rates extracted from each resonance fit; histogram of about 10,000 resonances with the most probable value quoted, contrasted with narrow linewidths reported on individual resonances; wafer map per exposure field; linewidth cross-checked by sideband calibration and cavity ring-down; a resonance noted as having no visible mode split. Fig. 4 and text: spiral losses higher than the resonator-derived value, attributed to scattering defects whose probability grows with waveguide area; loss rising at shorter wavelength |
| 3 | Z. Abdallah, Y. G. Boucher, A. Fernandez, S. Balac and O. Llopis, Radio frequency spectral characterization and model parameters extraction of high Q optical resonators, Sci. Rep. 6, 27208 (2016) | doi:10.1038/srep27208 | full text | Introduction: in optical scans self-heating shifts the resonance, so the shape depends on scan direction; light heats the resonator even at low power; a laser linewidth can exceed the resonance width at very high Q; amplitude-only scans carry no phase information. Results, analytical study: the same intensity profile can occur in under- and over-coupled regimes, and the phase response distinguishes them; fitting amplitude and phase together is more accurate than amplitude alone |
| 4 | Q. Li, A. A. Eftekhar, Z. Xia and A. Adibi, Unified approach to mode splitting and scattering loss in high-Q whispering-gallery-mode microresonators, Phys. Rev. A 88, 033816 (2013); read as preprint arXiv:1205.4448 | doi:10.1103/PhysRevA.88.033816 | full text | Abstract and Sec. I: imperfect fabrication breaks the symmetry between clockwise and counter-clockwise modes, which couple and appear as a doublet in transmission; the same scatterers add scattering loss and broaden the linewidth; the paper develops a model that covers both effects |
| 5 | L. Cheng, S. Mao, Z. Li, Y. Han and H. Y. Fu, Grating couplers on silicon photonics: design principles, emerging trends and practical issues, Micromachines 11, 666 (2020) | doi:10.3390/mi11070666 | full text | Sec. 1: edge couplers give high efficiency, broad bandwidth and low polarisation-dependent loss but low alignment tolerance. Sec. 4.1: grating couplers are polarisation selective. Sec. 4.2: grating couplers are highly wavelength sensitive, with 1 dB bandwidth usually below 50 nm; Table 1 mixes 1 dB and 3 dB bandwidths. Sec. 6.1: wafer-level testing with active alignment and polarisation control |
| 6 | A. Rahim, A. Hermans, B. Wohlfeil, D. Petousi, B. Kuyken, D. Van Thourhout and R. Baets, Taking silicon photonics modulators to a higher performance level: state-of-the-art and a review of new technologies, Adv. Photonics 3, 024003 (2021); read as the version in the Ghent University repository | doi:10.1117/1.AP.3.2.024003 | full text | Sec. 1: phase modulators compared by Vπ·L, with Vπ·L·α adding loss; ER/IL as the amplitude-modulator figure; insertion loss, extinction ratio, energy per bit and size listed as metrics; operating speed quoted for on-off keying only; ring-based devices sensitive to temperature and fabrication. Sec. 2.1: one parameter traded off against another (capacitance against speed, doping against loss); efficiencies quoted at stated reverse bias; equalisation and pre-emphasis used to reach line rates, with a 70 Gbaud signal reported from a device of 37 GHz 3 dB bandwidth |
| 7 | H. Jayatilleka, H. Frish, R. Kumar, J. Heck, C. Ma, M. Sakib, D. Huang and H. Rong, Post-fabrication trimming of silicon photonic ring resonators at wafer-scale, J. Lightwave Technol. 39, 5083–5088 (2021); read as preprint arXiv:2203.03503 | doi:10.1109/JLT.2021.3079801 | full text | Abstract and Sec. I: high sensitivity to fabrication variation limits ring manufacturability; nanometre-scale geometry variation shifts resonances by a few nanometres, so resonance wavelengths cannot be set by design; heaters correct this at the cost of a significant part of the power budget, and real-time tuning is still needed for ambient temperature drift |
| 8 | D. A. B. Miller, Attojoule optoelectronics for low-energy information processing and communications, J. Lightwave Technol. 35, 346–396 (2017); read as preprint arXiv:1609.05510 | doi:10.1109/JLT.2017.2647779 | full text | Sec. II.D and its footnote: charging a capacitance costs about CV²/2 per transition, and the commonly quoted CV²/4 per bit assumes random data. Sec. III.A: wire capacitance and the input capacitance of the connected transistor must be counted and can dominate. Sec. III introduction and IV.B: the device energies exclude other energies, especially from optical losses, and low modulator efficiency forces higher optical power. Sec. IV.D: narrow resonances need tuning against temperature drift |
