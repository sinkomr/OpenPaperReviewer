---
id: T-HIGH-PRESSURE
name: High-pressure experiments
type: technique
field: physics/condensed-matter
applies_when: the paper reports data taken in a diamond anvil, other opposed-anvil, piston-cylinder or gas pressure cell, or bases a claim about a pressure-induced transition, a pressure-temperature phase diagram or a pressure dependence on transport, magnetisation or other measurements in such a cell
version: "0.1"
---

# High-pressure experiments

## 1. Pressure gauge and scale

**Question.** Which gauge gave the pressure (ruby fluorescence, a Raman gauge, a superconducting or resistive manometer, an X-ray marker), which published calibration converted its reading to pressure, and at what temperature were the high-pressure and ambient reference readings taken?

**Why it matters.** Optical gauges are secondary scales: a line shift becomes a pressure only through a calibration, calibrations differ, and pressures from different laboratories can be compared only when the scale is named. Ruby lines also shift with temperature and with non-hydrostatic stress, and a ruby scale calibrated near 4.5 K has been found to differ by about 6% from the best room-temperature scale.

**Resolved by.** The gauge and the calibration named, for ruby a stated scale such as the one endorsed by the international high-pressure association in 2020, used within its stated pressure and temperature range; the ambient reference line measured at the temperature of the pressure reading, or a temperature correction stated; the reading uncertainty given, and the agreement between gauges shown where more than one was used.

**Benchmark.** [1], [2], [3], [4]

## 2. Pressure from the diamond Raman edge

**Question.** Where the pressure comes from the Raman spectrum of the diamond anvil, which calibration was used, does it cover the pressure range of the experiment, and was the result checked against a gauge or pressure marker inside the sample chamber?

**Why it matters.** The high-frequency edge of the anvil's first-order Raman band follows the normal stress at the culet face, not the pressure of the medium around the sample. It is converted to sample pressure only through an empirical calibration against a pressure marker, so the calibration chosen and its range determine the quoted pressure.

**Resolved by.** The calibration named and used within its range; the spectrum and the edge position shown for representative pressures; a cross-check against ruby where ruby is still usable, or against the lattice parameter of a metal marker of known equation of state measured by X-ray diffraction in the same chamber.

**Benchmark.** [4], [5]

## 3. Pressure at the temperature of the measurement

**Question.** Was the pressure determined at the temperature where the claimed effect is seen, or only at room temperature after loading, and how was the change of pressure on cooling and warming taken into account?

**Why it matters.** In a clamped piston-cylinder cell the pressure falls on cooling, by a few tenths of a gigapascal between room temperature and about 2 K, with a kink where the medium freezes, and at low applied pressure it can fall to zero. In anvil cells loaded with condensed gases the pressure can change by tens of per cent on cooling at low pressure. A pressure taken from a room-temperature reading can therefore differ substantially from the pressure at which the data were recorded.

**Resolved by.** A manometer read in situ at low temperature, such as the superconducting transition of a lead sample in the same cell, or an optical gauge read at the measurement temperature; for data over a wide temperature range, the pressure given as a function of temperature together with the interpolation used; room-temperature and low-temperature pressures both reported.

**Benchmark.** [6], [7], [12]

## 4. Pressure medium and its hydrostatic limit

**Question.** Which pressure-transmitting medium was used, and were the pressures and temperatures of the claim within the range where that medium is liquid and hydrostatic?

**Why it matters.** Each liquid medium solidifies above a pressure that depends on the medium and is lower at lower temperature, and beyond that line the sample is under non-hydrostatic stress. Media differ widely: at room temperature some liquids solidify near 1 GPa while helium stays close to hydrostatic to about 30 GPa, and at low temperature several organic media give non-hydrostatic conditions from low pressure. Uniaxial stress can change pressure-sensitive properties, and elastically soft samples can be affected even when the gauge shows little broadening.

**Resolved by.** The medium named with its loading method, or the absence of a medium stated; the pressure and temperature range of the claim compared with published hydrostatic limits and freezing lines for that medium; where the claim depends on hydrostatic conditions, a medium within its hydrostatic range, or the result reproduced in a second medium; features that coincide with freezing of the medium identified and not attributed to the sample.

**Benchmark.** [7], [8], [9]

## 5. Pressure distribution and stress at the sample

**Question.** How large is the pressure difference across the sample chamber and across the sample, how was it measured, and how large is the sample relative to the chamber?

**Why it matters.** Pressure in an anvil cell is not uniform: gradients and deviatoric stress develop even in good media, scale with the area sampled and grow when the medium solidifies. A single gauge, or a gauge linewidth averaged over the whole chamber, cannot separate a pressure gradient from uniaxial stress and can miss a small gradient. A sample that fills much of the chamber is less well surrounded by the medium, and any transition measured across a pressure spread is broadened by it.

**Resolved by.** Gauges at several positions in the chamber, or the width of a sharp reference transition such as the superconducting transition of a lead manometer, used to give the pressure spread at each pressure; that spread carried into the pressure uncertainty and compared with the width of the claimed transition; the sample dimensions and chamber size stated, with the sample small enough to be surrounded by the medium.

**Benchmark.** [3], [7], [10], [12]

## 6. Leads, insulation and current paths in a pressure cell

**Question.** For transport in an anvil cell, how were the leads brought to the sample and insulated from a metal gasket and from each other, was a four-terminal configuration kept at every pressure, and could current flow around the sample through the gasket or the chamber wall?

**Why it matters.** In an anvil cell the leads cross the gasket, which is usually metallic, so they must stay insulated under load as the gasket deforms. Current that by-passes the sample through the chamber wall makes a van der Pauw resistivity smaller than the true value, and the error is larger for more resistive samples.

**Resolved by.** The gasket, insulation and lead arrangement described, including insulation of the chamber wall; four-terminal data at every pressure with the contact configuration named; the quality of the sample inside the cell shown, for example by a residual resistivity and resistance ratio comparable with measurements outside the cell, and the transition used to follow pressure shown to stay sharp.

**Benchmark.** [10], [11]

## 7. Cell background in magnetisation

**Question.** For magnetisation measured in a pressure cell, how large is the sample signal compared with the signal of the cell, how was the cell contribution measured and removed at each pressure, and how was the sample moment extracted from the detector response?

**Why it matters.** The sample in a pressure cell is small and the cell surrounds it, so the cell's moment, including temperature-dependent contributions from impurities in anvils and gaskets, can be comparable with that of the sample. The cell response changes with pressure as the gasket deforms and parts move, so an empty-cell measurement at ambient pressure does not remove it exactly. When the sample signal is small, standard dipole fits are sensitive to the fitted sample position and can produce anomalies that are not in the sample.

**Resolved by.** The loaded-cell signal shown together with the empty-cell background measured under the same field and temperature conditions; the background correction allowing for changes of cell geometry with pressure; the extraction method stated, for example a fit to the difference signal or another method suited to small signals; sample mass and volume given so that the moment per unit mass can be checked.

**Benchmark.** [12], [13]

## Sources

| # | Reference | Identifier |
|---|---|---|
| 1 | G. Shen et al., Toward an international practical pressure scale: a proposal for an IPPS ruby gauge (IPPS-Ruby2020), High Press. Res. 40, 299 (2020) | doi:10.1080/08957959.2020.1791107 |
| 2 | K. Syassen, Ruby under pressure, High Press. Res. 28, 75 (2008) | doi:10.1080/08957950802235640 |
| 3 | Y. Feng et al., Invited Article: High-pressure techniques for condensed matter physics at low temperature, Rev. Sci. Instrum. 81, 041301 (2010) | doi:10.1063/1.3400212 |
| 4 | F. Datchi et al., Optical pressure sensors for high-pressure–high-temperature studies in a diamond anvil cell, High Press. Res. 27, 447 (2007) | doi:10.1080/08957950701659593 |
| 5 | Y. Akahama and H. Kawamura, Pressure calibration of diamond anvil Raman gauge to 310 GPa, J. Appl. Phys. 100, 043516 (2006) | doi:10.1063/1.2335683 |
| 6 | L. Xiang et al., Characterization of the pressure coefficient of manganin and temperature evolution of pressure in piston-cylinder cells, Rev. Sci. Instrum. 91, 095103 (2020); read as preprint arXiv:2007.11703 | doi:10.1063/5.0022650 |
| 7 | N. Tateiwa and Y. Haga, Evaluations of pressure-transmitting media for cryogenic experiments with diamond anvil cell, Rev. Sci. Instrum. 80, 123901 (2009); read as preprint arXiv:1001.0454 | doi:10.1063/1.3265992 |
| 8 | S. Klotz et al., Hydrostatic limits of 11 pressure transmitting media, J. Phys. D: Appl. Phys. 42, 075413 (2009) | doi:10.1088/0022-3727/42/7/075413 |
| 9 | M. S. Torikachvili et al., Solidification and loss of hydrostaticity in liquid media used for pressure measurements, Rev. Sci. Instrum. 86, 123904 (2015) | doi:10.1063/1.4937478 |
| 10 | R. Jaramillo et al., Four-probe electrical measurements with a liquid pressure medium in a diamond anvil cell, Rev. Sci. Instrum. 83, 103902 (2012) | doi:10.1063/1.4757178 |
| 11 | J. Yang et al., The effect of by-pass current on the accuracy of resistivity measurement in a diamond anvil cell, Chin. Phys. Lett. 30, 060701 (2013) | doi:10.1088/0256-307X/30/6/060701 |
| 12 | N. Tateiwa et al., Miniature ceramic-anvil high-pressure cell for magnetic measurements in a commercial superconducting quantum interference device magnetometer, Rev. Sci. Instrum. 82, 053906 (2011); read as preprint arXiv:1106.4071 | doi:10.1063/1.3590745 |
| 13 | N. Hiraoka et al., Design of opposed-anvil-type high-pressure cell for precision magnetometry and its application to quantum magnetism, J. Phys. Soc. Jpn. 90, 074001 (2021); read as preprint arXiv:2010.08314 | doi:10.7566/JPSJ.90.074001 |
