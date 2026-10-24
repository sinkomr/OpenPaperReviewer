---
id: T-NUCLEAR-ASTROPHYSICS
name: Low-energy nuclear astrophysics
type: technique
field: physics/nuclear
applies_when: the paper measures, extrapolates or evaluates a charged-particle reaction cross section, astrophysical S-factor, resonance strength or thermonuclear reaction rate at stellar energies, with low-energy beams above ground or underground, or with indirect methods such as transfer, Trojan horse or Coulomb dissociation
version: "0.1"
---

# Low-energy nuclear astrophysics

Low-energy experiments are used to claim cross sections, astrophysical S-factors (the cross section with its steep Coulomb-barrier energy dependence divided out), resonance strengths and thermonuclear reaction rates in the Gamow window, the narrow energy range where a reaction proceeds in a star. Because these cross sections are tiny, the claims rest on low-background measurements, often in underground laboratories, on extrapolation from higher energies, on corrections for electron screening, and on indirect methods such as asymptotic normalisation coefficients (ANCs) from transfer reactions, the Trojan horse method and Coulomb dissociation.

## 1. Target, beam and effective energy

**Question.** How were the target thickness, composition and depth profile, the beam energy and its spread, and the beam intensity determined; was the target monitored for degradation and contaminant build-up during irradiation; and which stopping powers converted the yields into cross sections at a stated effective energy?

**Why it matters.** At these energies the cross section changes steeply with energy, so the measured yield is an average over the energy lost in the target, and an error in the stopping power, the target composition or the beam energy shifts both the effective energy and the deduced S-factor. Solid targets change under intense beams and collect carbon and other contaminants, and their composition cannot be taken from the production process alone.

**Resolved by.** Target thickness and composition measured after production and again after irradiation, for example by resonance scans, nuclear reaction analysis or other ion beam analysis; target stability followed through the run; the source and uncertainty of the stopping powers stated; the effective energy defined and its uncertainty carried into the S-factor; for gas targets, the density profile and the method of measuring beam intensity described; the beam energy calibrated against known resonances or thresholds; reported quantities identified as yields or as cross sections corrected for energy spread.

**Benchmark.** [1], [3], [4]

## 2. Background at the lowest energies

**Question.** What is the background in the signal region at each energy, how was it measured (beam off, off resonance, blank backings), and how much of it comes from the environment and how much from beam-induced reactions on contaminants?

**Why it matters.** Signal rates at stellar energies can fall to a few counts per day or per month. Above ground, cosmic rays dominate many gamma-ray spectra; underground, natural radioactivity of materials and a residual neutron flux from the rock remain, and beam reactions on light contaminants such as boron, carbon, oxygen, fluorine or deuterium give gamma rays or neutrons that can fall in the signal region. A background not measured under the same conditions as the signal can be mistaken for reaction yield.

**Resolved by.** Spectra shown with signal and background regions marked; environmental background measured without beam and normalised to the same live time; beam-induced background measured with blank backings or off-resonance runs at the same charge; contaminant reactions identified by their characteristic lines and their contribution subtracted with an uncertainty; shielding and laboratory depth described; enough detail on the background subtraction for a reader to check it.

**Benchmark.** [2], [3]

## 3. Detection efficiency, summing and angular distribution

**Question.** How was the detection efficiency determined over the full energy range of the emitted radiation, and how were coincidence summing, the angular distribution of the emitted radiation and the branching to each final state handled?

**Why it matters.** Capture gamma rays reach several MeV, beyond common calibration sources, so efficiencies rest on simulations that need validation at high energy. A close, efficient geometry sums cascade gamma rays and moves counts between transitions, which matters most for capture to the ground state. A detector at a single angle gives the total cross section only if the angular distribution is known, and extrapolating each transition separately needs its own yield.

**Resolved by.** Efficiency from calibrated sources, extended to high energy with resonances that emit known cascades and compared with a validated simulation; summing corrections stated, or a near-4π calorimetric detector used where only the total cross section is needed; angular distributions measured at several angles, or the assumed distribution stated with its uncertainty; for activation, the collection fraction of product nuclei and the counting efficiency given; branching ratios reported with angle corrections.

**Benchmark.** [2], [3]

## 4. Resonances and the reaction rate

**Question.** For each narrow resonance, how were the resonance energy and strength obtained (absolute measurement, or relative to a named standard resonance), which stopping power and target composition entered the thick-target yield, and how are resonances that were searched for but not seen reported? When a reaction rate is given, how was it computed from the resonances and the non-resonant S-factor, and how were the uncertainties of the inputs carried into it?

**Why it matters.** A narrow resonance contributes to the rate linearly in its strength but exponentially in its energy, so a few keV in the resonance energy can matter more than the strength uncertainty. A strength from a thick-target yield combines counts, charge, efficiency and the effective stopping power, and strengths from different measurements can differ systematically unless normalised to common standards. An upper limit given without its confidence level and the distribution used to derive it cannot be carried into a rate. The narrow-resonance formula fails for broad resonances, for interfering levels and for resonances outside the Gamow window whose low-energy wing dominates, and rate limits formed by setting every input to its extreme have no defined statistical meaning.

**Resolved by.** Resonance energies given with the beam energy calibration and the yield-curve fit they rest on; resonance yield profiles shown; strengths given with each factor and its uncertainty, and the reference resonance named when the strength is relative; for unobserved resonances, the upper limit with its confidence level and the method used to derive it; the rate obtained by numerical integration wherever the narrow-resonance formula does not apply, with broad resonances, interference and low-energy wings included; rate uncertainties derived from the distributions of the inputs, for example by Monte Carlo sampling, with the treatment of energies, strengths and upper limits stated.

**Benchmark.** [3], [5]

## 5. Electron screening

**Question.** Does the analysis separate the screened laboratory cross section from the bare cross section, state which screening potential was used or fitted and how, and show how much the low-energy results depend on that choice?

**Why it matters.** Bound electrons in the target lower the Coulomb barrier, so the laboratory cross section exceeds the bare one by a factor that grows rapidly as the energy falls; plasma screening in the star is then applied to the bare value. Screening potentials fitted to laboratory data have often exceeded the adiabatic limit from atomic physics, and the fitted value depends on the assumed shape of the bare S-factor and on the stopping powers. Targets implanted in metals can show larger enhancements still, so a bare S-factor taken from the lowest-energy data inherits these uncertainties.

**Resolved by.** The screening correction stated with its value and origin; when the potential is fitted, the bare S-factor model and the energy range stated and the correlation between them shown; results given with and without the correction, or a range of energies where it is small; the target environment (gas, insulator, metal host) taken into account; independent constraints on the bare cross section, for example from indirect methods, used as a check where available.

**Benchmark.** [1], [2], [6]

## 6. Extrapolation of the S-factor to stellar energies

**Question.** When the data do not reach the Gamow window, which model extrapolates the S-factor (polynomial, potential or cluster model, R-matrix, effective field theory or ab initio calculation), over what energy range was it fitted, and how much does the extrapolated value change under reasonable alternatives?

**Why it matters.** A polynomial fit has no justification beyond the last data point and can miss a low-energy rise from a subthreshold state or a weakly bound final state. In R-matrix fits the extrapolation can depend on the channel radius, background poles, the relative signs of interfering levels and the parameters of subthreshold states, which the data may not fix. Well-justified models can disagree, and that disagreement is part of the uncertainty.

**Resolved by.** The Gamow window for the relevant stellar temperature compared with the energy range of the data; theory-motivated fitting functions, with the data fixing the normalisation; sensitivity to channel radius, background poles and alternative interference solutions shown; constraints from other channels, such as scattering data, ANCs or branching ratios, included where they exist; a model uncertainty added to the extrapolated value.

**Benchmark.** [1], [4]

## 7. Normalisation and comparison with other data sets

**Question.** Are the uncertainties split into point-to-point and common-mode (normalisation) parts, and when the result is fitted together with, or compared against, other data sets, is the normalisation of each treated explicitly?

**Why it matters.** Much of the uncertainty of a data set is often a common factor from target thickness, beam intensity or efficiency, and treating it as independent from point to point distorts both fitted curves and their uncertainties. Data sets on the same reaction often disagree by more than their stated errors, so a combined value needs a stated procedure for the disagreement.

**Resolved by.** Results tabulated with statistical, point-to-point and common-mode uncertainties listed separately; fits that let each data set's normalisation vary within its common-mode uncertainty; the treatment of discrepant data sets stated, such as an error inflation factor; exclusion of earlier data justified.

**Benchmark.** [1], [2], [4]

## 8. Indirect methods

**Question.** For results from transfer reactions, the Trojan horse method or Coulomb dissociation, which reaction model links the measured quantity to the astrophysical cross section, have its conditions been tested in the experiment, and how was the absolute normalisation obtained?

**Why it matters.** Indirect methods avoid the Coulomb barrier and electron screening but depend on reaction theory, so much of their systematic uncertainty is model uncertainty. ANCs from transfer depend on optical potentials and on the reaction being peripheral; the Trojan horse method needs quasi-free kinematics and is often normalised to direct data at higher energy; Coulomb dissociation contains E2, nuclear and multi-step contributions that must be separated from the single-photon E1 part.

**Resolved by.** Peripherality checked by varying the bound-state potential; elastic scattering measured to constrain the optical potentials; for the Trojan horse method, the spectator momentum distribution shown to match quasi-free expectations and the normalisation and its uncertainty stated; for Coulomb dissociation, kinematic cuts and beam energies chosen to suppress nuclear and multi-step effects, with the E2 contribution estimated; comparison with direct data where the energy ranges overlap.

**Benchmark.** [1], [2]

## Sources

| # | Reference | Identifier | Access | Where it supports the item |
|---|---|---|---|---|
| 1 | E. G. Adelberger et al., Solar fusion cross sections II: the pp chain and CNO cycles, Rev. Mod. Phys. 83, 195–245 (2011); read as arXiv:1004.2318v3 | doi:10.1103/RevModPhys.83.195 | full text | Sec. II.B: laboratory screening enhancement with potential Ue; fitted values exceed the adiabatic estimate and depend on the assumed bare S-factor; stopping powers lower than tabulated as a possible cause. Sec. II.C: a polynomial fit gives no basis for extrapolating past the last data point; theory-motivated fitting functions with data fixing the normalisation; extra uncertainty when justified models differ; R-matrix basics. Sec. II.D: data sets that disagree beyond their errors handled with an inflation factor. Sec. IX.A.3: low-energy data need energy-loss corrections that require the target profile, composition and monitoring of carbon build-up. Sec. XII: indirect methods carry more model dependence; ANCs need peripheral transfer and constrained optical potentials; Coulomb dissociation has E2, nuclear and multi-photon effects; Trojan horse needs quasi-free checks and normalisation to direct data |
| 2 | B. Acharya et al., Solar fusion III: New data and theory for hydrogen-burning stars, Rev. Mod. Phys. 97, 035002 (2025); read as arXiv:2405.06470 | doi:10.1103/8lm7-gs18 | full text | Sec. VI.C: gamma-ray angular distribution not known and detectors at one angle raise the common-mode error of prompt-gamma data; data excluded when uncertainties are not split into statistical and systematic parts or when the background subtraction cannot be checked. Sec. VI.D: common-mode and point-to-point errors separated and data-set normalisations fitted. Sec. XII.A: screening potential usually fitted with the bare S-factor; values from gas targets often above the adiabatic limit; stopping-power errors and bare-cross-section assumptions as uncertainty sources; large enhancements in metal hosts; low-energy experiments limited by intrinsic and cosmic-ray backgrounds. Sec. XIV.C: ANC uncertainties mainly from the optical model; Trojan horse relies on quasi-free kinematics, with recent work aimed at its systematic uncertainties |
| 3 | C. Broggini, D. Bemmerer, A. Caciolli and D. Trezzi, LUNA: Status and prospects, Prog. Part. Nucl. Phys. 98, 55–84 (2018); read as arXiv:1707.07952v4 | doi:10.1016/j.ppnp.2017.09.002 | full text | Sec. 3.1: signal rates down to a few counts per month; environmental background from cosmic rays, radioactivity and a residual neutron flux from the rock; beam-induced background from contaminants such as boron, carbon, oxygen, fluorine and deuterium, to be identified and removed. Sec. 3.3: solid-target thickness, stoichiometry and impurities must be measured after production, for example by resonance scans and ion beam analysis; target stability under intense beams monitored; beam intensity in gas targets from a calorimeter. Sec. 3.4: efficiency from simulation validated with sources and resonance cascades up to about 7 MeV; calorimetric 4π detectors dilute angular and branching effects but sum cascades, while extrapolation needs each transition from a spectroscopic detector; activation used for some reactions |
| 4 | R. J. deBoer et al., The 12C(α,γ)16O reaction and its implications for stellar helium burning, Rev. Mod. Phys. 89, 035007 (2017); read as arXiv:1709.03144 | doi:10.1103/RevModPhys.89.035007 | full text | Sec. VI.A.1: separating point-to-point from overall systematic uncertainties is critical for fitting several data sets. Sec. VI.A.2: reported quantities are often yields, related to cross sections through beam energy spread and stopping power. Secs. VII.B and VII.C: different interference sign solutions give large differences in the extrapolated S-factor; channel radii and background poles are correlated model parameters whose effect must be tested; subthreshold-state ANCs as a source of uncertainty |
| 5 | R. Longland, C. Iliadis, A. E. Champagne, J. R. Newton, C. Ugalde, A. Coc and R. Fitzgerald, Charged-particle thermonuclear reaction rates: I. Monte Carlo method and statistical distributions, Nucl. Phys. A 841, 1–30 (2010); read as arXiv:1004.4136v1 | doi:10.1016/j.nuclphysa.2010.04.008 | full text | Secs. 2.2 to 2.4: the narrow-resonance formula holds only when partial widths and the Maxwell-Boltzmann factor are nearly constant over the resonance; broad resonances, low-energy wings of resonances outside the Gamow peak and interfering levels need numerical integration. Sec. 3.2: resonance strength enters the narrow-resonance rate linearly and resonance energy exponentially; conventional upper and lower rate limits lack statistical meaning. Sec. 5.3: rates and their uncertainties from Monte Carlo sampling of input distributions. Sec. 3.4: an upper limit reported without confidence level and probability density cannot be propagated; authors urge reporting all three. Sec. 5.1.1: resonance energy from the thick-target yield curve, with uncertainty from beam energy calibration, yield fit, target inhomogeneity and dead layers. Sec. 5.1.2: strengths come from counts, stopping power, efficiency and charge, typically 15 to 20 per cent uncertain; literature strengths renormalised to standard resonances |
| 6 | M. Aliotta and K. Langanke, Screening effects in stars and in the laboratory, Front. Phys. 10, 942726 (2022) | doi:10.3389/fphy.2022.942726 | full text | Sec. 4 (experimental approaches): screening energy obtained by fitting low-energy data with an exponential enhancement on an extrapolated bare cross section; fitted values generally above the adiabatic limit, with molecular-target effects and stopping powers among proposed causes and larger values in deuterated metals; indirect methods such as the Trojan horse method to obtain bare cross sections |
