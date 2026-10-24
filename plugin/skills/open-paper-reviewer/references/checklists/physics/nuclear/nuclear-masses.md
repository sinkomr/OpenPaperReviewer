---
id: T-NUCLEAR-MASSES
name: Nuclear mass measurements
type: technique
field: physics/nuclear
applies_when: the paper reports atomic or nuclear masses, mass excesses, binding energies, Q-values, separation energies or isomer excitation energies measured with a Penning trap, a storage ring or a multi-reflection time-of-flight spectrometer, or bases a claim about shell structure, nuclear models or nucleosynthesis on such masses
version: "0.1"
---

# Nuclear mass measurements

Mass measurements of stable and short-lived nuclides are used to claim atomic masses, mass excesses and the binding energies, Q-values, separation energies and isomer excitation energies derived from them. The main methods compare an ion with reference ions of well-known mass: Penning traps through cyclotron-frequency ratios, measured by time-of-flight ion-cyclotron resonance (TOF-ICR) or phase-imaging ion-cyclotron resonance (PI-ICR); multi-reflection time-of-flight (MR-TOF) spectrometers through flight-time ratios; and storage rings through revolution frequencies, in Schottky mass spectrometry (SMS) of cooled ions or in isochronous mass spectrometry (IMS).

## 1. Reference masses and the primary result

**Question.** Which reference ion or ions was each result measured against, how well known are their masses and how close are they in mass-to-charge ratio to the ion of interest, and does the paper report the measured frequency or time-of-flight ratio with the reference named, as well as the derived mass?

**Why it matters.** These methods measure a mass relative to a reference, so an error in the reference mass passes directly into the result, and some systematic shifts grow with the mass difference between the two ions. A mass published without the primary ratio and the reference cannot be recalculated when the reference mass is later revised, and it cannot be correctly weighted in a combined evaluation.

**Resolved by.** The reference nuclide and charge state named for each result, with the mass value and its source; references close in mass-to-charge ratio, or a mass doublet, where the highest accuracy is claimed; the frequency or time-of-flight ratio tabulated with its statistical and systematic uncertainties; the conversion from ion to atomic mass stated, including the electron and, where relevant, molecular binding corrections.

**Benchmark.** [1], [2]

## 2. Systematic shifts of the spectrometer

**Question.** What mass-dependent and residual systematic uncertainties were applied, how were they determined (for example by cross-reference measurements of carbon-cluster ions or by remeasuring nuclides of well-known mass in the same run), and how were drifts of the magnetic field between reference measurements handled?

**Why it matters.** Field imperfections and ion-motion effects give frequency-ratio shifts that grow with the mass difference from the reference, and a residual systematic term is usually added so that test measurements agree within their errors. These values depend on the instrument, the technique and the mass range tested, so a value taken from another setup or a different range may not apply. Field drift between reference measurements adds a further uncertainty that grows with the time between them.

**Resolved by.** The mass-dependent and residual terms stated with the measurements and mass range that established them; the interpolation of reference measurements in time described, with the drift rate and the uncertainty it contributes; nuclides of well-known mass measured under the same conditions and their deviations from literature values shown, with a consistency measure such as a Birge ratio.

**Benchmark.** [1], [2], [4]

## 3. Contaminant ions and ion number

**Question.** Which other ion species (isobars, molecules, isomers) were delivered with the ion of interest, how were they removed or resolved, and does the paper show that the result does not depend on the number of ions stored at once?

**Why it matters.** Purification before the precision measurement has limited resolving power, so close isobars and isomers can remain. When ions of different mass are stored together, their Coulomb interaction pulls the measured frequencies towards each other, and in phase-imaging measurements a second species can also shift the measured phase; both effects can move a result by more than its stated uncertainty. In time-of-flight spectra an unidentified contaminant near the peak shifts the fitted position.

**Resolved by.** The purification method and its resolving power stated; the composition of the delivered beam identified; frequencies or ratios analysed against the number of detected ions per cycle and extrapolated to one ion, or data restricted to very few ions; for phase-imaging, the correction or timing scheme for several species stated; possible unresolved contaminants considered in the uncertainty.

**Benchmark.** [2], [3], [4]

## 4. Isomers and state identification

**Question.** Could a long-lived isomer have been present in the measured sample, was the resolving power sufficient to separate it at its excitation energy, and does the paper state whether the reported mass belongs to the ground state, to an isomer, or to an unresolved mixture?

**Why it matters.** An unresolved isomer moves the measured mass towards a weighted mean of the two states, and the ground-state mass can be recovered only if the excitation energy and the production ratio are known. Which state is the ground state is itself uncertain for some nuclides, and isomer half-lives of fully stripped ions in a storage ring can differ from those of neutral atoms. Assigning the result to the wrong state shifts every quantity derived from it.

**Resolved by.** The resolving power compared with the excitation energies of known or expected isomers; the isomer-to-ground-state ratio measured, for example by resolving both peaks or by decay spectroscopy, or bounded; for an unresolved mixture, the correction and the uncertainty it adds stated; the state assignment argued from independent evidence, with reference to evaluated isomer data.

**Benchmark.** [1], [4], [5]

## 5. Time-of-flight calibration

**Question.** For multi-reflection time-of-flight results, how was the flight time converted to mass-to-charge ratio (one reference with an independently measured time offset, or two references), did the calibrant and the ion of interest make the same number of turns, and how were drifts of the flight time during the run corrected?

**Why it matters.** The flight time depends on the square root of the mass-to-charge ratio plus an offset, and with a single reference the result is only as good as the independent determination of that offset. A calibrant that makes a different number of turns from the ion of interest brings in a further calibration term whose uncertainty grows with the difference. Flight times drift with voltages and temperature, and a time-resolved correction both removes the drift and broadens the peaks.

**Resolved by.** The calibration relation and the calibrant ions stated, with how the offset was obtained; the number of turns given for calibrant and ion of interest; the drift correction described, with the interval between calibration points; each calibration contribution listed in the uncertainty budget.

**Benchmark.** [1], [4]

## 6. Peak shape and spectra with few events

**Question.** For time-of-flight spectra, which peak-shape model was used and where did its parameters come from, how were overlapping peaks fitted, and how was the statistical uncertainty of a peak position estimated when it rests on few events?

**Why it matters.** Time-of-flight peaks are often asymmetric with long tails, so the fitted position depends on the shape model and on whether that model describes the ion of interest as well as the calibrant. When two peaks overlap, some fitting methods pull their positions together, which biases both the masses and any isomer excitation energy. With only tens of events, uncertainties based on a normal distribution can understate the true scatter.

**Resolved by.** The peak shape taken from a high-statistics peak measured under the same conditions, with the choice of model justified and its uncertainty propagated; fitted spectra shown with the data for each result; any correction for overlapping peaks described and included in the uncertainty; statistical uncertainties for low-count peaks obtained from resampling or simulation.

**Benchmark.** [4]

## 7. Storage-ring calibration and isochronicity

**Question.** For storage-ring results, which reference nuclides were used, how are they distributed in mass-to-charge ratio and revolution time relative to the unknowns, what calibration function was fitted, and was the calibration tested by recalculating each reference mass from the others?

**Why it matters.** The isochronous condition holds over only a limited range of mass-to-charge ratio, and resolving power falls quickly outside it. Ion species with different momentum distributions or energy losses can follow the calibration curve differently, so references of one kind can give systematic deviations for nuclides of another kind. Magnetic-field drifts during the run shift the revolution times of all ions.

**Resolved by.** The reference nuclides listed with their masses; unknown masses interpolated within the range covered by references rather than extrapolated; a leave-one-out test in which each reference is treated as unknown, with a normalised chi value compared with its expected range; drift corrections described; for isochronous measurements, the momentum or velocity of each ion measured, or the deviation from isochronicity otherwise corrected or bounded.

**Benchmark.** [6], [7]

## 8. Derived quantities and the mass surface

**Question.** Where the paper derives separation energies, Q-values, shell gaps or other mass differences, which other masses does it combine with its own, are any of them estimates from trends in the mass surface rather than measured values, and does a feature it interprets as nuclear structure rest on a single measured mass?

**Why it matters.** Evaluated mass tables also list values estimated from the smoothness of the mass surface, flagged as estimates, whose uncertainties are judgments and which fail where the structure changes unexpectedly. An irregularity in a derived quantity can come from one incorrect mass as well as from nuclear structure, and evaluators treat an isolated deviation from regularity as a possible sign of incorrect data until a remeasurement settles it.

**Resolved by.** The source and edition of every other mass used stated, with estimated values identified and not treated as measurements; derived quantities given with uncertainties that include those of the other masses; a structural feature supported by more than one nuclide, or by an independent measurement of the mass it depends on.

**Benchmark.** [1]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | W. J. Huang, M. Wang, F. G. Kondev, G. Audi and S. Naimi, The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures, Chin. Phys. C 45, 030002 (2021) | doi:10.1088/1674-1137/abddb0 | full text | Secs. 3 and 3.2: only primary data are used so that values can be recalibrated; publishing absolute masses instead of the measured ratio is not recommended practice because they change with the reference mass. Sec. 3.3.1: electron binding, and above about 10^-10 molecular binding, must be included. Sec. 3.3.2: MR-TOF relation of flight time to the square root of mass-to-charge plus an offset, one reference where the offset is measured independently, two references otherwise; in time-of-flight methods, isomer cross-contamination can shift masses. Sec. 3.4.1: the ground-state mass of an unresolved mixture follows only if excitation energy and production ratio are known, otherwise a correction with an added uncertainty; bare ions can have much longer isomer lifetimes. Sec. 4.1.1: normalised chi (Birge ratio) and error inflation for inconsistent data. Secs. 4.4 and 4.5: consistency factors per laboratory and method, and data conflicting with the adjusted values examined and possibly excluded. Sec. 5.1: a mass deviating from the regularity of the mass surface is treated as possibly incorrect data, to be settled by remeasurement. Sec. 5.2: unmeasured masses estimated from trends of the mass surface and flagged with '#'; such estimates fail if unexpected changes of deformation occur |
| 2 | D. A. Nesterenko, T. Eronen, Z. Ge, A. Kankainen and M. Vilen, Study of radial motion phase advance during motion excitations in a Penning trap and accuracy of JYFLTRAP mass spectrometer, Eur. Phys. J. A 57, 302 (2021); read as arXiv:2107.05631 | doi:10.1140/epja/s10050-021-00608-3 | full text | Secs. 2.3.3 and 3.3: with more than one ion species in the trap a phase shift arises that moved a test result by about 2 keV unless corrected; avoided by shorter pulses or by cleaning to one species. Sec. 3.2: magnetic-field drift and linear interpolation between reference measurements, with the uncertainty it adds over hours. Sec. 3.4: count-rate class analysis, frequencies of two species shifting towards each other with ion number. Sec. 3.5: carbon-cluster cross-reference measurements give a mass-dependent shift per mass unit and a residual term, whose values depend on the mass range tested |
| 3 | K. Blaum, Sz. Nagy and G. Werth, High-accuracy Penning trap mass measurements with stored and cooled exotic ions, J. Phys. B 42, 154015 (2009); read as arXiv:0904.4712 | doi:10.1088/0953-4075/42/15/154015 | full text | Sec. 3: mass-selective buffer-gas cooling in a preparation trap purifies the sample with a resolving power of about 10^5, below that of the precision trap. Sec. 2: single-ion measurements remove frequency shifts from the Coulomb field of other stored ions |
| 4 | S. Ayet San Andrés, C. Hornung, J. Ebert, W. R. Plaß, T. Dickel, H. Geissel, C. Scheidenberger et al., High-resolution, accurate multiple-reflection time-of-flight mass spectrometry for short-lived, exotic nuclei of a few events in their ground and low-lying isomeric states, Phys. Rev. C 99, 064313 (2019); read as arXiv:1901.11278 | doi:10.1103/PhysRevC.99.064313 | full text | Sec. IV.1: time-resolved calibration corrects drifts and broadens peaks. Secs. IV.3 and IV.4: asymmetric peak-shape model with parameters from a high-statistics peak. Sec. IV.6: maximum-likelihood fitting pulls overlapping peaks together, with an iterative correction. Sec. IV.9: empirical statistical uncertainty about 25% above the normal-distribution estimate; calibration term that grows with the difference in turns; unresolved contaminants, non-ideal ejection and space charge in the budget. Sec. V.1: known masses remeasured and compared with the evaluation, with a Birge ratio. Sec. V.2: isomer-to-ground-state ratios measured |
| 5 | F. G. Kondev, M. Wang, W. J. Huang, S. Naimi and G. Audi, The NUBASE2020 evaluation of nuclear physics properties, Chin. Phys. C 45, 030001 (2021) | doi:10.1088/1674-1137/abddae | full text | Sec. 1: the mass evaluation needs unambiguous identification of each state involved in a mass measurement, and NUBASE2020 can serve as a reference for identifying nuclides in mass spectra. Sec. 2.2: flags for nuclides where it is unclear which state is the ground state, for orderings reversed by new mass data and for isomers of uncertain existence; isomers with half-lives of 100 ns or more included because their masses can be measured directly |
| 6 | M. Zhang, X. Zhou, M. Wang, Y. H. Zhang, Yu. A. Litvinov, H. S. Xu et al., Bρ-defined isochronous mass spectrometry and mass measurements of 58Ni fragments, Eur. Phys. J. A 59, 27 (2023); read as arXiv:2209.05701 | doi:10.1140/epja/s10050-023-00928-6 | full text | Secs. I and II: isochronicity holds only over a limited mass-to-charge range; calibrating one isospin series with references from another gave systematic deviations, attributed to different momentum distributions and energy losses. Secs. III.1 to III.5: velocity measured for each ion; magnetic-field drifts corrected. Sec. IV.1: leave-one-out test of the references with a normalised chi value |
| 7 | Y. H. Zhang, Yu. A. Litvinov, T. Uesaka and H. S. Xu, Storage ring mass spectrometry for nuclear structure and astrophysics research, Phys. Scr. 91, 073002 (2016); read as arXiv:1811.12003 | doi:10.1088/0031-8949/91/7/073002 | full text | Secs. 3 and 3.1: velocity spread of a few per cent in uncooled secondary beams, negligible for electron-cooled ions. Sec. 3.2: isochronous conditions hold in a narrow part of the spectrum and resolving power falls off quickly away from it; knowing each ion's rigidity or velocity allows correction. Sec. 4.3: masses calibrated against nuclides of well-known mass |
