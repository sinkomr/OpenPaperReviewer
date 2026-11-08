---
id: T-PLASMA-TURBULENCE
name: Turbulence and transport in plasmas
type: technique
field: physics/plasma
applies_when: the paper measures plasma density, temperature or potential fluctuations, their spectra, correlation lengths or cross-phases, infers a turbulent flux or diffusivity from fluctuations or power balance, or compares measured turbulence or transport with gyrokinetic or fluid simulations
version: "0.1"
---

# Turbulence and transport in plasmas

## 1. Spatial and wavenumber response

**Question.** Does the paper state where in the plasma the measurement is localised, with what radial and perpendicular resolution, and which range of wavenumbers it can detect, and does it compare that range with the scales of the turbulence it makes claims about?

**Why it matters.** A finite sample volume averages out structures smaller than itself, so it acts as a low-pass filter in wavenumber: fluctuations with wavelengths near the spot size are not detected, and the measured amplitude, spectrum and correlation length all depend on the size of the volume. Each diagnostic covers only part of the wavenumber range, so a statement about turbulence at scales the diagnostic cannot see does not follow from its data.

**Resolved by.** The sample volume or point spread function given in physical units and in units of the relevant gyroradius; the detectable wavenumber range stated for each data set; amplitudes and correlation lengths described as those of the filtered signal, or corrected with a stated model of the response; claims about a given scale backed by a diagnostic that covers it.

**Benchmark.** [1], [2]

## 2. From measured signal to fluctuation amplitude

**Question.** When a fluctuation amplitude such as a relative density or temperature fluctuation level is quoted, does the paper say how the measured signal was converted into it, what model or assumptions the conversion uses, and how instrument noise was removed from the quoted level?

**Why it matters.** Most diagnostics do not measure the fluctuating quantity directly: beam emission intensity relates to density through a collisional-radiative model, the power returned to a reflectometer or scattering system is not simply proportional to the density fluctuation, a single radiometer channel is dominated by thermal noise, and a probe's ion saturation current mixes density and temperature. An amplitude taken straight from the raw signal can therefore be off by a model-dependent factor or include noise.

**Resolved by.** The conversion model named and its inputs given, for example the atomic-physics coefficient for beam emission or full-wave modelling for reflectometry; amplitudes reported in arbitrary units where no conversion was made, with comparisons then limited to spectral shapes; the method used to remove uncorrelated noise, such as cross-correlation of channels, stated and the remaining noise level shown; the contribution of temperature to probe signals discussed.

**Benchmark.** [1], [3]

## 3. Laboratory-frame frequency and Doppler shift

**Question.** When frequency spectra, propagation directions or phase velocities are interpreted, does the paper account for the Doppler shift from plasma flow, and say how the flow was measured and how frequency was converted to wavenumber or spatial scale?

**Why it matters.** Fluctuations are measured in the laboratory frame, where the observed frequency is the plasma-frame frequency plus a Doppler shift from the radial electric field and flows. When the shift dominates, the measured frequency mainly reflects the poloidal wavenumber and the flow, not the turbulence dynamics, and turning time records into spatial scales relies on the frozen-turbulence (Taylor) assumption.

**Resolved by.** An independent measurement of the flow or radial electric field at the same location; frequency spectra shown alongside the estimated Doppler shift; the direction of propagation stated in the plasma frame; the assumption behind any conversion from time to space stated and checked, for example with direct wavenumber measurements.

**Benchmark.** [1], [2]

## 4. Spectral, correlation and cross-phase estimates

**Question.** For each spectrum, coherence, cross-phase, correlation length or two-point wavenumber-frequency spectrum, does the paper state the record length, the number of independent realisations averaged, the channel separations, and the definition used for derived quantities such as the correlation length?

**Why it matters.** Averaging over realisations suppresses uncorrelated noise only slowly, so coherence has a noise floor of about one over the square root of the number of realisations, and noise biases the measured cross-phase. A two-point estimate of the local wavenumber needs channels closer than the correlation length. Correlation lengths are defined in more than one way, and different definitions or normalisations can create an apparent disagreement with other work or with simulation.

**Resolved by.** Spectral estimation parameters given (window, segment length, number of realisations); the coherence noise floor shown on coherence plots and cross-phases reported only where coherence exceeds it; channel separations compared with the correlation length; correlation length and normalisation defined, with the same definition applied to any data or simulation compared.

**Benchmark.** [1], [2]

## 5. Turbulent flux from fluctuation measurements

**Question.** When a fluctuation-driven particle or heat flux is computed from correlated density, potential or temperature fluctuations, does the paper say how each fluctuating quantity was obtained, whether temperature fluctuations were measured or neglected, and how the probe or channel separation enters the electric field estimate?

**Why it matters.** Probe-based fluxes usually take the electric field from the difference in floating potential between two pins and the density from the ion saturation current. The floating potential differs from the plasma potential by a term proportional to the electron temperature, so neglected temperature fluctuations, or a temperature that differs between pins, change the inferred field and flux; in simulations the resulting flux differed from the true flux by several times, and at some positions even in sign.

**Resolved by.** Electron temperature fluctuations measured, or their effect on the potential and the flux bounded; fields from floating potentials identified as such, with the temperature term discussed; the pin geometry and separation given and compared with the turbulence scale; the density and field fluctuations behind the flux shown, not only the flux.

**Benchmark.** [3]

## 6. Separating turbulent from neoclassical and convective transport

**Question.** When a turbulent flux or diffusivity is inferred from power or particle balance, does the paper state the sources and sinks used, how the neoclassical part was computed and subtracted, how convective and conductive heat fluxes were treated, and over what radial range the result is reliable?

**Why it matters.** Power balance gives the total flux, which is the sum of neoclassical and turbulent parts, so the turbulent part is a remainder that inherits the uncertainties of the sources, of the neoclassical calculation and of the measured gradients; inferred heat fluxes typically carry uncertainties of 10 to 30 per cent. Near the axis and the edge the remainder can be unreliable, and a diffusivity from steady-state balance differs from one obtained by perturbative (heat-pulse or modulation) methods.

**Resolved by.** The interpretive code, the source and sink terms and the neoclassical code named; the turbulent and neoclassical fluxes plotted with uncertainties; convective losses given or shown to be small, and model fluxes compared with conductive plus convective losses; the radial range of validity stated; steady-state and perturbative diffusivities kept distinct.

**Benchmark.** [4], [1]

## 7. Synthetic diagnostics for comparison with simulation

**Question.** When measured fluctuations are compared with gyrokinetic or fluid simulations, was the simulation output passed through a synthetic diagnostic that models the instrument's spatial, wavenumber and temporal response and the laboratory-frame Doppler shift, and was the same analysis applied to both data sets?

**Why it matters.** Raw simulation output contains wavenumbers and resolution the diagnostic does not have. Applying a synthetic diagnostic usually lowers the fluctuation amplitude and lengthens the correlation length, so comparing raw output with measurement can create or hide disagreement. A synthetic diagnostic is itself a model, and it can also produce agreement that is fortuitous.

**Resolved by.** The synthetic diagnostic described, including its transfer function and any Doppler treatment; filtered and unfiltered simulation results shown; identical analysis routines applied to measured and synthetic signals; the simulation resolving the wavenumbers and frequencies the diagnostic detects; the synthetic diagnostic tested or its parameters varied within their uncertainty.

**Benchmark.** [1], [5]

## 8. Sensitivity to input gradients and the choice of observables

**Question.** Does the comparison with simulation account for the sensitivity of the predicted fluxes to the input profiles and gradients, by scans within their uncertainties, and does it compare fluctuation quantities such as amplitudes, spectra, correlation lengths and cross-phases as well as fluxes?

**Why it matters.** Turbulent fluxes near a critical gradient rise steeply with the gradient, so a change of the input gradient within typical uncertainties can change the predicted flux several times. Agreement in a flux alone can come from compensating errors, and quantities that integrate many effects, such as diffusivities, are weak tests; agreement at one level of observable does not guarantee agreement at another.

**Resolved by.** The uncertainties of the input gradients given and simulations repeated across them, or a flux-matched case found within them; several observables compared at different levels, from fluctuation amplitudes and spectra to cross-phases and fluxes; a stated validation metric that includes experimental uncertainties, systematic ones included; disagreements reported as well as agreements.

**Benchmark.** [1], [5]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | A. E. White, Validation of nonlinear gyrokinetic transport models using turbulence measurements, J. Plasma Phys. 85, 925850102 (2019) | doi:10.1017/S0022377818001253 |
| 2 | M. J. Choi, Leveraging turbulence data from fusion experiments, Rev. Mod. Plasma Phys. 9, 22 (2025); read as preprint arXiv:2412.20130 | doi:10.1007/s41614-025-00198-3 |
| 3 | F. P. Gennrich and A. Kendl, Analysis of the temperature influence on Langmuir probe measurements on the basis of gyrofluid simulations, Plasma Phys. Control. Fusion 54, 015012 (2012); read as preprint arXiv:1109.3600 | doi:10.1088/0741-3335/54/1/015012 |
| 4 | D. Carralero et al., On the role of density fluctuations in the core turbulent transport of Wendelstein 7-X, Plasma Phys. Control. Fusion 64, 044006 (2022); read as preprint arXiv:2110.00277 | doi:10.1088/1361-6587/ac4d14 |
| 5 | P. W. Terry et al., Validation in fusion research: towards guidelines and best practices, Phys. Plasmas 15, 062503 (2008); read as preprint arXiv:0801.2787 | doi:10.1063/1.2928909 |
