---
id: T-NUCLEAR-ASTROPHYSICS
name: Low-energy nuclear astrophysics
type: technique
field: physics/nuclear
applies_when: the paper measures, extrapolates or evaluates a charged-particle reaction cross section, astrophysical S-factor, resonance strength or thermonuclear reaction rate at stellar energies, with low-energy beams above ground or underground, or with indirect methods such as transfer, Trojan horse or Coulomb dissociation
version: "0.1"
---

# Low-energy nuclear astrophysics

## 1. Background at the lowest energies

**Question.** What is the background in the signal region at each energy, how was it measured (beam off, off resonance, blank backings), and how much of it comes from the environment and how much from beam-induced reactions on contaminants?

**Why it matters.** Signal rates at stellar energies can fall to a few counts per day or per month. Above ground, cosmic rays dominate many gamma-ray spectra; underground, natural radioactivity of materials and a residual neutron flux from the rock remain, and beam reactions on light contaminants such as boron, carbon, oxygen, fluorine or deuterium give gamma rays or neutrons that can fall in the signal region. A background not measured under the same conditions as the signal can be mistaken for reaction yield.

**Resolved by.** Spectra shown with signal and background regions marked; environmental background measured without beam and normalised to the same live time; beam-induced background measured with blank backings or off-resonance runs at the same charge; contaminant reactions identified by their characteristic lines and their contribution subtracted with an uncertainty; shielding and laboratory depth described; enough detail on the background subtraction for a reader to check it.

**Benchmark.** [2], [3]

## 2. Resonances and the reaction rate

**Question.** For each narrow resonance, how were the resonance energy and strength obtained (absolute measurement, or relative to a named standard resonance), which stopping power and target composition entered the thick-target yield, and how are resonances that were searched for but not seen reported? When a reaction rate is given, how was it computed from the resonances and the non-resonant S-factor, and how were the uncertainties of the inputs carried into it?

**Why it matters.** A narrow resonance contributes to the rate linearly in its strength but exponentially in its energy, so a few keV in the resonance energy can matter more than the strength uncertainty. A strength from a thick-target yield combines counts, charge, efficiency and the effective stopping power, and strengths from different measurements can differ systematically unless normalised to common standards. An upper limit given without its confidence level and the distribution used to derive it cannot be carried into a rate. The narrow-resonance formula fails for broad resonances, for interfering levels and for resonances outside the Gamow window whose low-energy wing dominates, and rate limits formed by setting every input to its extreme have no defined statistical meaning.

**Resolved by.** Resonance energies given with the beam energy calibration and the yield-curve fit they rest on; resonance yield profiles shown; strengths given with each factor and its uncertainty, and the reference resonance named when the strength is relative; for unobserved resonances, the upper limit with its confidence level and the method used to derive it; the rate obtained by numerical integration wherever the narrow-resonance formula does not apply, with broad resonances, interference and low-energy wings included; rate uncertainties derived from the distributions of the inputs, for example by Monte Carlo sampling, with the treatment of energies, strengths and upper limits stated.

**Benchmark.** [3], [5]

## 3. Electron screening

**Question.** Does the analysis separate the screened laboratory cross section from the bare cross section, state which screening potential was used or fitted and how, and show how much the low-energy results depend on that choice?

**Why it matters.** Bound electrons in the target lower the Coulomb barrier, so the laboratory cross section exceeds the bare one by a factor that grows rapidly as the energy falls; plasma screening in the star is then applied to the bare value. Screening potentials fitted to laboratory data have often exceeded the adiabatic limit from atomic physics, and the fitted value depends on the assumed shape of the bare S-factor and on the stopping powers. Targets implanted in metals can show larger enhancements still, so a bare S-factor taken from the lowest-energy data inherits these uncertainties.

**Resolved by.** The screening correction stated with its value and origin; when the potential is fitted, the bare S-factor model and the energy range stated and the correlation between them shown; results given with and without the correction, or a range of energies where it is small; the target environment (gas, insulator, metal host) taken into account; independent constraints on the bare cross section, for example from indirect methods, used as a check where available.

**Benchmark.** [1], [2], [6]

## 4. Extrapolation of the S-factor to stellar energies

**Question.** When the data do not reach the Gamow window, which model extrapolates the S-factor (polynomial, potential or cluster model, R-matrix, effective field theory or ab initio calculation), over what energy range was it fitted, and how much does the extrapolated value change under reasonable alternatives?

**Why it matters.** A polynomial fit has no justification beyond the last data point and can miss a low-energy rise from a subthreshold state or a weakly bound final state. In R-matrix fits the extrapolation can depend on the channel radius, background poles, the relative signs of interfering levels and the parameters of subthreshold states, which the data may not fix. Well-justified models can disagree, and that disagreement is part of the uncertainty.

**Resolved by.** The Gamow window for the relevant stellar temperature compared with the energy range of the data; theory-motivated fitting functions, with the data fixing the normalisation; sensitivity to channel radius, background poles and alternative interference solutions shown; constraints from other channels, such as scattering data, ANCs or branching ratios, included where they exist; a model uncertainty added to the extrapolated value.

**Benchmark.** [1], [4]

## 5. Normalisation and comparison with other data sets

**Question.** Are the uncertainties split into point-to-point and common-mode (normalisation) parts, and when the result is fitted together with, or compared against, other data sets, is the normalisation of each treated explicitly?

**Why it matters.** Much of the uncertainty of a data set is often a common factor from target thickness, beam intensity or efficiency, and treating it as independent from point to point distorts both fitted curves and their uncertainties. Data sets on the same reaction often disagree by more than their stated errors, so a combined value needs a stated procedure for the disagreement.

**Resolved by.** Results tabulated with statistical, point-to-point and common-mode uncertainties listed separately; fits that let each data set's normalisation vary within its common-mode uncertainty; the treatment of discrepant data sets stated, such as an error inflation factor; exclusion of earlier data justified.

**Benchmark.** [1], [2], [4]

## 6. Indirect methods

**Question.** For results from transfer reactions, the Trojan horse method or Coulomb dissociation, which reaction model links the measured quantity to the astrophysical cross section, have its conditions been tested in the experiment, and how was the absolute normalisation obtained?

**Why it matters.** Indirect methods avoid the Coulomb barrier and electron screening but depend on reaction theory, so much of their systematic uncertainty is model uncertainty. ANCs from transfer depend on optical potentials and on the reaction being peripheral; the Trojan horse method needs quasi-free kinematics and is often normalised to direct data at higher energy; Coulomb dissociation contains E2, nuclear and multi-step contributions that must be separated from the single-photon E1 part.

**Resolved by.** Peripherality checked by varying the bound-state potential; elastic scattering measured to constrain the optical potentials; for the Trojan horse method, the spectator momentum distribution shown to match quasi-free expectations and the normalisation and its uncertainty stated; for Coulomb dissociation, kinematic cuts and beam energies chosen to suppress nuclear and multi-step effects, with the E2 contribution estimated; comparison with direct data where the energy ranges overlap.

**Benchmark.** [1], [2]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | E. G. Adelberger et al., Solar fusion cross sections II: the pp chain and CNO cycles, Rev. Mod. Phys. 83, 195 (2011); read as arXiv:1004.2318v3 | doi:10.1103/RevModPhys.83.195 |
| 2 | B. Acharya et al., Solar fusion III: New data and theory for hydrogen-burning stars, Rev. Mod. Phys. 97, 035002 (2025); read as arXiv:2405.06470 | doi:10.1103/8lm7-gs18 |
| 3 | C. Broggini et al., LUNA: Status and prospects, Prog. Part. Nucl. Phys. 98, 55 (2018); read as arXiv:1707.07952v4 | doi:10.1016/j.ppnp.2017.09.002 |
| 4 | R. J. deBoer et al., The 12C(α,γ)16O reaction and its implications for stellar helium burning, Rev. Mod. Phys. 89, 035007 (2017); read as arXiv:1709.03144 | doi:10.1103/RevModPhys.89.035007 |
| 5 | R. Longland et al., Charged-particle thermonuclear reaction rates: I. Monte Carlo method and statistical distributions, Nucl. Phys. A 841, 1 (2010); read as arXiv:1004.4136v1 | doi:10.1016/j.nuclphysa.2010.04.008 |
| 6 | M. Aliotta and K. Langanke, Screening effects in stars and in the laboratory, Front. Phys. 10, 942726 (2022) | doi:10.3389/fphy.2022.942726 |
