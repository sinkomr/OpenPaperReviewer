---
id: T-SINGLE-MOLECULE-FLUORESCENCE
name: Single-molecule fluorescence and FRET
type: technique
field: physics/biological
applies_when: the paper reports single-molecule fluorescence or single-molecule FRET data, from surface-immobilized molecules or freely diffusing bursts, and bases a claim on FRET efficiencies, inter-dye distances, conformational states, state populations, transition rates or binding events inferred from them
version: "0.1"
---

# Single-molecule fluorescence and FRET

Single-molecule fluorescence, and in particular single-molecule Förster resonance energy transfer (smFRET), is used to claim distances between two dyes attached to a biomolecule, the conformational states the molecule visits, their populations, and the rates of transitions between them. These are inferred from photon counts in two or more detection channels, recorded from dye-labelled molecules either fixed to a surface and imaged by total internal reflection fluorescence (TIRF) or diffusing through a confocal spot, often with alternating-laser excitation (ALEX) or pulsed interleaved excitation (PIE).

## 1. Correction factors for FRET efficiency

**Question.** Is each reported efficiency an apparent value (proximity ratio) or a corrected FRET efficiency, and if corrected, does the paper state how background, donor leakage into the acceptor channel, direct excitation of the acceptor and the detection factor gamma (and, with alternating excitation, the excitation factor beta) were determined, and give their values?

**Why it matters.** The raw ratio of acceptor to total intensity differs from the FRET efficiency by amounts that depend on the instrument and the dyes, and the gamma factor is a major source of uncertainty in the corrected value. Leaving out a correction, or applying the corrections in the wrong order, shifts efficiencies, most of all at low FRET, and makes values from different instruments or papers impossible to compare.

**Resolved by.** A statement of whether apparent or corrected efficiencies are shown; the correction factors and background levels given, with the populations used to obtain them (donor-only for leakage, acceptor-only for direct excitation, several species or acceptor photobleaching for gamma); the corrections applied in a stated order; where gamma is set for each molecule or each species, the spread of values shown.

**Benchmark.** [1], [2], [3]

## 2. From efficiency to distance

**Question.** When efficiencies are converted to distances, does the paper state the Förster radius used and how it was obtained, including the donor quantum yield at the labelling site, the refractive index and the orientation factor kappa squared, and does it support the assumption of freely rotating dyes with anisotropy or lifetime measurements?

**Why it matters.** The Förster radius depends on the donor quantum yield, the spectral overlap, the refractive index and kappa squared. The quantum yield can change markedly with the labelling site and environment, and the usual value of two thirds for kappa squared holds only when the dyes rotate quickly and freely. Because the dyes sit on flexible linkers, the distance that follows directly from a mean efficiency is a FRET-averaged distance, not the distance between attachment points or dye mean positions, and distances below about 3 nm are less reliable.

**Resolved by.** The Förster radius and every input to it stated, with the quantum yield measured for the labelled construct; donor and acceptor anisotropies, preferably time-resolved, showing sufficient dye mobility, or an uncertainty for kappa squared; a dye model, such as an accessible-volume calculation, used to relate efficiencies to structural distances; an uncertainty on each distance that includes the Förster radius; consistency checks with more than one dye pair or labelling position.

**Benchmark.** [1], [2], [3]

## 3. Dye photophysics and the local environment

**Question.** Could the intensity or efficiency changes the claim rests on come from changes in dye photophysics, such as blinking, triplet or other dark states, quenching, stacking of a dye on the biomolecule, or enhancement of dye fluorescence by a nearby protein, instead of a change in distance, and what control measurements exclude this?

**Why it matters.** Cyanine dyes in particular grow brighter when their local environment restricts their motion, dyes can stack on nucleic acids and change their orientation, and a bound protein can raise one dye's intensity without the anticorrelated change in the other that energy transfer would give. Blinking of the acceptor produces brief drops to donor-only levels, and changes in quantum yield or dye orientation shift the efficiency or the Förster radius. Each of these can create apparent FRET states or transitions that have no structural origin.

**Resolved by.** Donor-only and acceptor-only samples measured at the same labelling sites, with lifetimes and anisotropies reported; anticorrelated donor and acceptor changes shown at transitions; ALEX or PIE stoichiometry used to detect changes in dye brightness; the effect of photostabilizing additives and of excitation intensity on the claimed states checked; for protein binding near a dye, a test of whether the dye intensity changes on binding.

**Benchmark.** [2], [3], [4], [5]

## 4. Effect of labelling on the molecule

**Question.** Does the paper show that the labelled molecule keeps the function and stability of the unlabelled one, state the labelling sites and the labelling efficiency, and say whether donor and acceptor were attached at specific sites or stochastically?

**Why it matters.** Mutations for site-specific labelling and the attached dyes can change the activity, folding or binding of a biomolecule, so the states seen may not be those of the native molecule. When the two dyes are distributed randomly over two sites and have different spectroscopic properties at each site, molecules with swapped labels give different efficiencies for the same structure.

**Resolved by.** Activity or binding assays comparing labelled and unlabelled molecules; the labelling chemistry, sites and degree of labelling reported; for stochastic labelling, evidence that the two label arrangements give the same result or are separated; where possible, the main result reproduced with a second pair of labelling sites.

**Benchmark.** [2], [5]

## 5. Surface immobilization

**Question.** For surface-immobilized molecules, how was the surface passivated and the molecule tethered, what fraction of the detected molecules was bound non-specifically, and is there evidence that tethering does not alter the behaviour being measured?

**Why it matters.** Molecules that stick to a poorly passivated surface, rather than binding through the intended tether, can be immobile, inactive or in altered conformations, and they add to the population being analysed. The tether itself and the nearby surface can perturb conformational dynamics and activity.

**Resolved by.** The passivation method (for example polyethylene glycol for proteins) and the tethering scheme described; a measurement without the tethering agent showing that non-specific binding is a small fraction of specific binding; activity of the tethered molecules checked; results cross-validated with freely diffusing molecules, vesicle encapsulation or a different immobilization strategy.

**Benchmark.** [2], [3]

## 6. Identifying single, doubly labelled molecules

**Question.** What criteria were used to decide that a trace or burst comes from one molecule carrying one active donor and one active acceptor (for example stoichiometry from alternating excitation, single-step photobleaching, colocalization, burst thresholds), how many molecules passed them, and could the criteria bias which states are counted?

**Why it matters.** Molecules lacking an acceptor, or with a bleached or inactive acceptor, look like a zero or low FRET population, and with single-laser excitation they cannot be separated from real low-FRET species. Burst-search thresholds and trace filters change the shape of efficiency histograms, and filtering on particular photobleaching or acceptor behaviour can select some states over others. Features seen in only a few per cent of molecules are especially hard to tell apart from artefacts.

**Resolved by.** The selection criteria and thresholds stated, with the number and fraction of molecules retained; donor-only and acceptor-only species removed using stoichiometry from ALEX or PIE, or by acceptor checks in TIRF; single-step photobleaching of each dye shown for traces used; conclusions shown to be insensitive to the thresholds; rare species supported by more than a handful of molecules and by control constructs.

**Benchmark.** [1], [2], [3], [4]

## 7. Static heterogeneity, dynamics and shot noise

**Question.** When a broad or multi-peaked efficiency distribution is interpreted as several states or as dynamics, does the paper compare the width with that expected from photon shot noise and test whether the broadening comes from interconversion during the observation time or from a static mixture of molecules?

**Why it matters.** Shot noise broadens efficiency histograms even for a single fixed distance. Beyond that, a mixture of static species and a single species switching between states can produce histograms that fit equally well, and transitions faster than the time resolution are averaged into apparent intermediate efficiencies. Changes in dye quantum yield or orientation within a burst or frame can mimic conformational dynamics.

**Resolved by.** The shot-noise-limited width shown alongside the measured distribution; a test for dynamics within bursts or frames, such as burst variance analysis, lifetime-versus-efficiency plots or kernel-density methods, applied together with a static control molecule; the time resolution stated and compared with the timescale of the claimed dynamics; photophysical explanations excluded by controls.

**Benchmark.** [2], [6], [7]

## 8. Assignment of states and kinetic models

**Question.** When states, their number and transition rates are inferred with hidden Markov models or other methods, does the paper state the model, how the number of states was chosen, what assumptions the method makes about noise and heterogeneity between molecules, and how the inferred rates were validated and their uncertainties obtained?

**Why it matters.** Analysis tools agree well when states have clearly separated efficiencies, but model selection and state assignment are the main difficulties in real data, and different tools can infer different numbers of states from the same traces. States that share an efficiency can be told apart only through their dwell-time distributions, so a model without that kinetic structure misses them. Brightness differences between molecules, low signal-to-noise and noise that departs from the method's assumptions all bias the inferred states and rates, and fast transitions missed at the frame rate lead to underestimated rates. Reported uncertainties can be smaller than the finite size of the data set allows.

**Resolved by.** The analysis software, model, priors and criterion for the number of states stated; dwell-time distributions shown with the fitted model; the inferred model simulated with the experimental noise, frame rate and trace lengths and reanalysed to show that the input is recovered; rates given with confidence intervals; trace lengths limited by photobleaching taken into account; for more than two states, the connectivity of the kinetic scheme reported and not only mean dwell times.

**Benchmark.** [2], [3], [7]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | B. Hellenkamp, S. Schmid, O. Doroshenko and others, C. A. M. Seidel, T. D. Craggs and T. Hugel, Precision and accuracy of single-molecule FRET measurements: a multi-laboratory benchmark study, Nat. Methods 15, 669–676 (2018) | doi:10.1038/s41592-018-0085-0 | full text | Results, correction factors and procedure: background, leakage from donor-only, direct excitation from acceptor-only, gamma by global, single-species or per-molecule schemes, beta for alternating excitation, applied in a stated order; without ALEX low-FRET values shift and acceptor bleaching is hard to see; correction moved a low-FRET peak from about 0.25 to 0.15; systematic variation of gamma gives an error of about 10%. Distance sections: apparent distance from mean efficiency is FRET-averaged, not a physical distance, and accessible-volume models give the mean-position distance; Förster radius uncertainty dominated by kappa squared and refractive index; distances below about 3 nm less reliable; dye mobility checked by anisotropy and lifetimes |
| 2 | E. Lerner, A. Barth, J. Hendrix and others, FRET-based dynamic structural biology: challenges, perspectives and an appeal for open-science practices, eLife 10, e60416 (2021) | doi:10.7554/eLife.60416 | full text | "Conjugation": compare labelled and unlabelled molecule function, report labelling efficiency, stochastic labelling with dyes of different properties causes problems. "Immobilization": non-specific binding, alternative schemes, cross-validation. "Spectroscopic characterization": blinking, bleaching, protein-induced enhancement, dye stacking altering kappa squared create artificial FRET species; single-labelled lifetime and anisotropy controls; ALEX or PIE. "Identification" and "User bias": burst search and selection criteria affect histograms; report the fraction of molecules analysed. "Detecting dynamics": averaging of transitions faster than the sampling time, width compared with the shot-noise limit, lifetime-versus-efficiency plots, BVA and 2CDE. "Slow dynamics": hidden Markov models and their remaining accuracy problems. "Determining absolute FRET efficiencies from fluorescence intensities": gamma as the major contribution to uncertainty. "Inter-dye distances", subsections "Fluorescence quantum yield" and "Dye transition dipole orientation factor": quantum yield depends on the labelling position and should be determined for each; kappa squared uncertainty bounded from time-resolved anisotropies; the FRET-averaged distance differs from the distance between mean dye positions. "Dye models": accessible-volume calculations |
| 3 | R. Roy, S. Hohng and T. Ha, A practical guide to single-molecule FRET, Nat. Methods 5, 507–516 (2008); read as the author manuscript in PubMed Central | doi:10.1038/nmeth.1208 | full text | "Surface immobilization" and "The sample chamber": polyethylene glycol passivation for proteins; accept a surface when non-specific spots are under 10% of specifically tethered ones. "FRET efficiency": leakage and direct excitation from single-labelled molecules, gamma from acceptor photobleaching; kappa squared near two thirds only when anisotropy is below about 0.2; protein binding can alter gamma. "Enhancing photostability": oxygen scavenging lengthens dark states, triplet quenchers reduce blinking. "Interpreting data: pitfalls and tips": diagnose blinking with photostabilizers, direct acceptor excitation and intensity dependence; single-step photobleaching; features in under about 5% of molecules are hard to separate from artefacts; hidden Markov modelling for states and rates |
| 4 | A. N. Kapanidis, N. K. Lee, T. A. Laurence, S. Doose, E. Margeat and S. Weiss, Fluorescence-aided molecule sorting: analysis of structure and interactions by alternating-laser excitation of single molecules, Proc. Natl Acad. Sci. USA 101, 8936–8941 (2004) | doi:10.1073/pnas.0401690101 | full text | Introduction: inactive acceptors give species with donor-only characteristics, and substoichiometric labelling limits single-laser FRET. "Principle of ALEX" and "Sorting Species with Different D–A Stoichiometry and D–A Distance Using FAMS": the stoichiometry ratio separates donor-only, acceptor-only and doubly labelled species, so doubly labelled molecules with efficiency near zero are still identified. "FAMS Can Sense Fluorophore Brightness": stoichiometry responds to changes in dye brightness such as donor quenching |
| 5 | H. Hwang and S. Myong, Protein induced fluorescence enhancement (PIFE) for probing protein-nucleic acid interactions, Chem. Soc. Rev. 43, 1221–1229 (2014); read as the author manuscript in PubMed Central | doi:10.1039/c3cs60201j | full text | "History and chemical basis of PIFE": cyanine isomerization competes with fluorescence and a bound protein restricts it, raising the quantum yield; a protein near one dye can raise its intensity without the anticorrelated change of the other. "Application – determination of the protein binding constant, substrate specificity, binding position and kinetics": enhancement depends on the distance of the bound protein from the dye; confirm that the dye does not perturb activity by comparison with standard assays |
| 6 | J. P. Torella, S. J. Holden, Y. Santoso, J. Hohlbein and A. N. Kapanidis, Identifying molecular dynamics in single-molecule FRET experiments with burst variance analysis, Biophys. J. 100, 1568–1577 (2011) | doi:10.1016/j.bpj.2011.01.066 | full text | Introduction and "BVA can distinguish between static and dynamic heterogeneity": broadening beyond shot noise shows heterogeneity but not its origin, and a static three-species mixture and a two-state dynamic model fit the same histogram. "Burst variance analysis": compares the standard deviation within bursts with the shot-noise expectation; changes in quantum yield or orientation factor can mimic dynamics and need controls |
| 7 | M. Götz, A. Barth, S. S. Bohr and others, K. R. Weninger, P. Xu and S. Schmid, A blind benchmark of analysis tools to infer kinetic rate constants from single-molecule FRET trajectories, Nat. Commun. 13, 5402 (2022) | doi:10.1038/s41467-022-33023-3 | full text | "The archetypal 2-state system": tools agree for separated states, most rates slightly underestimated; some reported uncertainties below the finite-data limit. "Directional sequences in a non-equilibrium steady-state system": averaging within a frame creates apparent intermediate efficiencies. "States with overlapping FRET efficiencies": states sharing an efficiency are inferred only kinetically, from multi-exponential dwell-time distributions, and tools without kinetic heterogeneity deviated most. "Full complexity of a black-box experiment": model selection and state allocation the main challenges, the number of states varied between tools, high intensity variation between molecules. Discussion, Table 2: simulate the inferred model and reanalyse, report connectivity, give 95% confidence intervals |
