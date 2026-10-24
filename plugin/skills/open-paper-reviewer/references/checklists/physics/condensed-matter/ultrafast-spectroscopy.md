---
id: T-ULTRAFAST-SPECTROSCOPY
name: Photoluminescence and ultrafast spectroscopy
type: technique
field: physics/condensed-matter
applies_when: the paper reports steady-state or time-resolved photoluminescence, a photoluminescence quantum yield, or pump-probe, transient absorption or transient reflection data, or bases a claim about carrier or exciton lifetimes, recombination, trapping, transfer or emission efficiency on them
version: "0.1"
---

# Photoluminescence and ultrafast spectroscopy

Steady-state and time-resolved photoluminescence (PL), the photoluminescence quantum yield (PLQY) and pump-probe or transient absorption (TA) spectroscopy are used to claim lifetimes of carriers and excitons, rates of recombination, trapping and transfer, emission efficiencies, and the identity of excited states. Each of these is inferred from light emitted or absorbed after optical excitation, so the result depends on how strongly the sample was excited, how the time axis and instrument response were handled, and which model turned the data into rates and assignments.

## 1. Excitation density

**Question.** Does the paper state the pump fluence or power density, spot size, repetition rate, photon energy and absorbed fraction, convert these into an initial density of excitations, and show whether the dynamics and spectra change with that density?

**Why it matters.** At low density the signal scales linearly with pump power and the decay does not depend on it; at higher density, Auger recombination, exciton-exciton annihilation, second-order radiative recombination and slower cooling of hot carriers add fast or altered components that are not the low-density dynamics. The density depends on focus size, absorption and thickness, so a fluence quoted without these cannot be compared with another measurement or with operating conditions.

**Resolved by.** The fluence and the method used to obtain the initial carrier or exciton density, including spot size, absorption and thickness; a fluence series over a wide range showing linear signal scaling and unchanged decay shape in the regime used for the claim, or a rate model fitted across all fluences when the claim concerns processes of higher order; the density range compared with the conditions to which the conclusion is applied.

**Benchmark.** [1], [2], [4], [5]

## 2. Heating, damage and sample stability

**Question.** Does the paper show that the sample was not changed by the light during the measurement: repeated scans that agree, spectra or decays taken before and after, a check at a lower repetition rate or fluence, and a stable signal before time zero?

**Why it matters.** Solid samples have no solvent to carry heat away and are more prone to laser damage and accumulated heating, which depend on fluence and repetition rate. Photodegradation or photochemical change during a long acquisition alters the quantity being measured. If the time between pulses is not much longer than the slowest decay, long-lived states build up from pulse to pulse and add an offset or change the kinetics, and an unstable baseline before time zero makes it hard to tell the signal from noise, scattered pump light or drift.

**Resolved by.** Pump fluence and repetition rate stated and kept below a threshold for change that the paper has measured; the time between pulses compared with the longest decay time; for solutions, a flowed, stirred or moved sample so that the same volume is not excited by many pulses; for solids, a moved or scanned spot or a demonstration that repeated exposure leaves the signal unchanged; repeated data sets that agree; data before time zero shown in the kinetic traces.

**Benchmark.** [1], [2], [3]

## 3. Time zero, instrument response and coherent artefacts

**Question.** Does the paper state the instrument response function (IRF) and how it was measured, how time zero was set at each probe wavelength, and how signals during pulse overlap were treated, and are any time constants close to or below the IRF width supported by fits that include it?

**Why it matters.** A broadband probe is chirped, so time zero shifts with wavelength unless corrected. Near zero delay, cross-phase modulation, two-photon absorption in solvent or substrate and scattered pump light add signals that are not population dynamics. In time-resolved PL the measured decay is the true decay convolved with the IRF, which can itself depend on the detected wavelength. A time constant comparable to the IRF that is read directly from the data, without these steps, can be an instrument effect.

**Resolved by.** The IRF width and how it was measured, for example by pump-probe cross-correlation, by scattered excitation light, or with a reference of known lifetime; chirp correction described and checked on a solvent or substrate measurement; the overlap region either modelled or excluded, with a blank measured under the same conditions; decays fitted by reconvolution with the measured IRF; any sub-IRF time constant reported with its uncertainty and compared with the IRF width.

**Benchmark.** [1], [2], [3], [6]

## 4. Fitting decays and reporting lifetimes

**Question.** For each quoted lifetime, does the paper give the fitted function, the time window, the number of components and the reason for it, the residuals, and the definition of any average lifetime?

**Why it matters.** Several sums of exponentials can fit the same noisy decay, so adding components can improve a fit without each component meaning a separate process. An average or effective lifetime depends on how the components are weighted and can hide competing pathways, and a single wavelength or a single time constant can omit processes visible elsewhere in the data.

**Resolved by.** The model stated together with its physical basis; weighted residuals and goodness-of-fit statistics shown, with tests used to choose between models with different numbers of components; the fit window and background treatment stated; the individual components and amplitudes reported, not only an average; kinetics shown at several wavelengths alongside the full spectra; for decays that are not exponential, a time-dependent or differential decay time, or a physical rate model, instead of a single constant.

**Benchmark.** [3], [5], [6]

## 5. What a decay time measures

**Question.** When a decay time is presented as a recombination lifetime, a trapping time or a transfer rate, does the paper show that the decay is set by that process and not by carrier diffusion, surface or interface recombination, charge extraction into adjacent layers, or a carrier-density dependence of the recombination?

**Why it matters.** A single-exponential lifetime has a simple meaning only when recombination is linear in the excess carrier density, as in a doped sample under low injection. In an intrinsic sample both carrier types are excited, so the decay time changes with density as the decay proceeds. In layer stacks and devices, extraction to transport layers, interface recombination and the charging of electrodes also change the PL decay, so a faster decay cannot simply be read as faster recombination.

**Resolved by.** The injection regime identified and the decay time treated as a function of density or time where needed; controls that isolate each pathway, such as films with and without passivated surfaces or transport layers and different thicknesses; a rate or drift-diffusion model fitted to data at several fluences, with the fluence stated for every decay shown.

**Benchmark.** [1], [5]

## 6. Quantum yield

**Question.** Is the PLQY measured by a stated method, absolute with an integrating sphere or relative to a named standard, with the excitation wavelength and intensity, the absorbance of the sample, and corrections for reabsorption and detector response given?

**Why it matters.** A relative measurement depends on the standard's quantum yield under the conditions used, on matching absorbance and emission range, and on a low absorbance to avoid inner-filter effects; many papers use standards outside their verified conditions or do not name them. In integrating-sphere measurements on films and concentrated samples, emitted light is reabsorbed and partly re-emitted, and methods that ignore this overestimate the quantum yield, most at high absorbance or high yield.

**Resolved by.** The method and instrument described; for relative measurements, a standard with an established value used within its verified solvent and excitation range, absorbance below about 0.1, the same cell and refractive-index correction; for absolute measurements, a calibrated sphere with spectrally resolved detection that separates excitation from emission and accounts for indirect excitation and self-absorption; the excitation wavelength and intensity stated; an uncertainty given, typically several per cent at best.

**Benchmark.** [7], [8], [9], [10]

## 7. Assignment of transient features and kinetic models

**Question.** How was each positive, negative or derivative-shaped feature in the transient spectra assigned, and, when species-associated spectra or microscopic rate constants are reported, what kinetic model was imposed and was it tested?

**Why it matters.** A transient spectrum is a sum of overlapping ground-state bleach, stimulated emission and excited-state absorption, and in thin films and semiconductors it also contains photoinduced changes of refractive index and reflectivity, band-gap renormalisation and hot-carrier contributions; positive or derivative-like features are not necessarily excited-state absorption. Sequential global analysis gives spectra that may be mixtures of several species, and target analysis yields pure-species spectra only under the kinetic scheme assumed and the assumption that each spectrum keeps its shape over time.

**Resolved by.** Steady-state absorption and emission spectra shown as references for the bleach and stimulated emission; assignments checked by fluence dependence, spectral shape and, where relevant, spectroelectrochemistry, molecular reference compounds or simultaneous transmission and reflection; thin-film interference and substrate response evaluated; the number of components justified, for example by singular value decomposition; the kinetic scheme stated, compared with alternatives, and shown to give physically reasonable spectra.

**Benchmark.** [1], [2], [3], [4]

## 8. Emission spectra and assignment of emission peaks

**Question.** Are the emission spectra corrected for the spectral response of the detection system, and is each emission peak assigned (free or bound exciton, charged exciton, defect, band-to-band) on evidence beyond its energy, such as its dependence on excitation power and temperature measured over a wide range?

**Why it matters.** Uncorrected spectra misplace peak positions and relative intensities, and a non-linear detector distorts intensity ratios. Reabsorption in thick or concentrated samples changes the measured spectrum. The power-law exponent of emission intensity against excitation power is often used to classify a peak, but it lies between one and two for excitonic emission, departs from a single power law when the power is varied over more than about two decades, and changes with excitation wavelength, so an exponent from a narrow range is weak evidence.

**Resolved by.** Spectra corrected for detector and spectrometer response and plotted with a stated intensity unit; detector linearity checked over the intensity range used; sample thickness or concentration chosen, or a correction applied, so that reabsorption is small; peak assignments supported by power dependence over a stated range together with temperature dependence, absorption or excitation spectra, or comparison with reference samples.

**Benchmark.** [7], [10], [11]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | K.-C. Chou, D. C. Zeitz, M. Khvichia and J. Z. Zhang, Tutorial: Transient absorption spectroscopy for probing ultrafast dynamics, ACS Phys. Chem. Au 6, 584–596 (2026); read in PubMed Central (PMC13397461) | doi:10.1021/acsphyschemau.6c00027 | full text | Sec. 2.4: group velocity dispersion chirps the probe so time zero varies with wavelength and must be corrected; the IRF is set by the pump-probe cross-correlation; near zero delay, cross-phase modulation and two-photon absorption from solvent or substrate contaminate the signal. Sec. 2.5: in the linear regime signal scales with pump power and decays do not depend on density, which is needed for intrinsic lifetimes; at high fluence Auger recombination and exciton-exciton annihilation add fluence-dependent fast components; a power series maps kinetic order, staying below the photodegradation threshold. Sec. 3.1: chirp correction using the coherent artefact in a blank. Secs. 3.4 to 3.6: sequential-model spectra may be combinations of species; target analysis rests on a postulated scheme and assumes constant spectral shapes; rate constants are then mapped onto mechanisms |
| 2 | R. Berera, R. van Grondelle and J. T. M. Kennis, Ultrafast transient absorption spectroscopy: principles and application to photosynthetic systems, Photosynth. Res. 101, 105–118 (2009); read in PubMed Central (PMC2744833) | doi:10.1007/s11120-009-9454-y | full text | "The principle of ultrafast transient absorption spectroscopy" and Fig. 1: a difference spectrum sums ground-state bleach, stimulated emission and excited-state absorption; coherent artefact and cross-phase modulation at early times are excluded or modelled. "Equipment" section: the fraction excited depends on focus size, concentration and extinction coefficient; lower pulse energies used for annihilation-free conditions, while shorter pulse spacing lets long-lived triplet or charge-separated states build up. "The transient absorption setup": white-light chirp described by a polynomial in the analysis; IRF measured by frequency mixing or transient birefringence; samples flowed or shaken to avoid repeated exposure and degradation. "Collection of transient absorption spectra": spectra before time zero for the baseline; repeated runs to test reproducibility and sample stability. "Data analysis": sequential spectra are generally mixtures; pure-species spectra need a specific kinetic model |
| 3 | A. J. King, L. Chen, A. B. Maurer and J. Huang, A guide to transient absorption spectroscopy for porous crystalline materials in photocatalysis, Nat. Commun. 17, 5280 (2026); read in PubMed Central (PMC13269924) | doi:10.1038/s41467-026-73511-4 | full text | "Common limitations": artefacts from uncorrected dispersion, solvent, cross-phase modulation and thin-film interference; measuring solvent or substrate alone; omitting pre-time-zero data hides baseline stability and the origin of fast features; single-wavelength kinetics, unjustified multi-exponential fits and average lifetimes can mask processes; singular value decomposition and global analysis. "Practical considerations": solid samples are more susceptible to laser damage and thermal accumulation, requiring control of fluence and repetition rate; positive features may arise from refractive-index changes. "Working principles": steady-state absorption and emission spectra to identify bleach and stimulated emission, and spectroelectrochemistry for oxidised or reduced species. Table 1: compare kinetics with the cross-correlation width; check derivative-like features by spectral shape and fluence dependence |
| 4 | M. B. Price, J. Butkus, T. C. Jellicoe, A. Sadhanala, A. Briane, J. E. Halpert, K. Broch, J. M. Hodgkiss, R. H. Friend and F. Deschler, Hot-carrier cooling and photoinduced refractive index changes in organic–inorganic lead halide perovskites, Nat. Commun. 6, 8420 (2015) | doi:10.1038/ncomms9420 | full text | Abstract and Results: initial carrier density derived from optical density, film thickness and pump fluence; at higher excitation densities a phonon bottleneck slows carrier cooling; a sub-band-gap derivative feature explained by band-gap renormalisation and hot carriers; photoinduced reflectivity changes distort transient absorption spectra and must be included to extract physical constants; simultaneous transmission and reflection measurements |
| 5 | L. Krückemeier, B. Krogmeier, Z. Liu, U. Rau and T. Kirchartz, Understanding transient photoluminescence in halide perovskite layer stacks and solar cells, Adv. Energy Mater. 11, 2003489 (2021); read as preprint arXiv:2102.08730 | doi:10.1002/aenm.202003489 | full text | Introduction: reducing a decay to the time constant of a single exponential makes misinterpretation likely, and with contact layers a faster decay cannot simply mean faster recombination. Sec. 2: differential decay time from the derivative of the PL. Sec. 2.1: a lifetime is well defined for a doped sample in low-level injection; in intrinsic films in high-level injection the decay time depends on carrier density, and simulated decays show radiative and Auger recombination at high density. Sec. 2.2: surface recombination. Secs. 3 to 5: charge extraction, interface charging and electrode charging alter the PL decay, which depends strongly on pulse fluence in devices. Sec. 6: measured decays on films, layer stacks and devices; without the laser fluence such data are hard to compare |
| 6 | N. Boens, W. Qin, N. Basarić, J. Hofkens, M. Ameloot, J. Pouget, J.-P. Lefèvre, B. Valeur, E. Gratton, M. vandeVen et al., Fluorescence lifetime standards for time and frequency domain fluorescence spectroscopy, Anal. Chem. 79, 2137–2149 (2007); read as the author manuscript in PubMed Central (PMC6816264) | doi:10.1021/ac062160k | full text | Opening (unlabelled) section: lifetime standards test instruments for systematic errors and correct the wavelength-dependent time response of detectors. "Theory": the observed decay is the true decay convolved with the IRF, usually measured with scattered excitation light; reference convolution with a single-exponential standard corrects the colour effect. "Single-curve fitting": weighted residuals, reduced chi-square, autocorrelation, Durbin-Watson and runs tests to judge fit quality and to choose between one and two exponentials |
| 7 | A. M. Brouwer, Standards for photoluminescence quantum yield measurements in solution (IUPAC Technical Report), Pure Appl. Chem. 83, 2213–2228 (2011); read as the published version in the University of Amsterdam repository | doi:10.1351/PAC-REP-10-09-31 | full text | Sec. 1: the relative quantum yield equation with absorption factors and refractive indices; different excitation wavelengths for sample and standard are not advisable. Sec. 2: absorbance typically below 0.1 to avoid inner-filter effects, same cell and absorbance for sample and standard, correction for the spectral response of the detection system and a check of detector linearity, similar emission range. Sec. 4: only three standards well established, to within about 4%. Sec. 5: in a survey of about 250 papers, standards used at unverified excitation wavelengths, mismatched ranges, and standards not named |
| 8 | C. Würth, M. Grabolle, J. Pauli, M. Spieles and U. Resch-Genger, Relative and absolute determination of fluorescence quantum yields of transparent samples, Nat. Protoc. 8, 1535–1550 (2013) | doi:10.1038/nprot.2013.087 | abstract | Abstract: protocols for relative quantum yields with a conventional spectrometer and absolute quantum yields with a calibrated integrating sphere, addressing typical sources of uncertainty; achievable uncertainties of 5 to 10% |
| 9 | J. C. de Mello, H. F. Wittmann and R. H. Friend, An improved experimental determination of external photoluminescence quantum efficiency, Adv. Mater. 9, 230–232 (1997) | doi:10.1002/adma.19970090308 | abstract | Abstract: an integrating-sphere method for the external quantum yield of thin-film samples, with spectrally resolved detection that separates excitation and emission, suited to small Stokes shifts, low yields and scattering samples |
| 10 | T.-S. Ahn, R. O. Al-Kaysi, A. M. Müller, K. M. Wentz and C. J. Bardeen, Self-absorption correction for solid-state photoluminescence quantum yields obtained from integrating sphere measurements, Rev. Sci. Instrum. 78, 086105 (2007) | doi:10.1063/1.2768926 | abstract | Abstract: self-absorption affects integrating-sphere quantum yield measurements; a correction that uses the observed yield and the luminescence spectrum and accounts for absorption and re-emission; earlier methods overestimate the true yield, especially at high absorbance or high yield |
| 11 | T. Schmidt, K. Lischka and W. Zulehner, Excitation-power dependence of the near-band-edge photoluminescence of semiconductors, Phys. Rev. B 45, 8989–8994 (1992) | doi:10.1103/PhysRevB.45.8989 | abstract | Abstract: excitonic emission scales with excitation power to an exponent between 1 and 2; the power law fails when power varies over more than two orders of magnitude; the exponent changes with excitation wavelength; a model relating the exponents of free-exciton, bound-exciton and free-to-bound emission |
