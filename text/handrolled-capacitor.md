Suppose you wanted to hand-roll an oil capacitor out of paper, oil,
and aluminum foil.  The capacitance is C = εA/d; ε₀ ≈ 8.8541878 pF/m,
so with 100-μm-thick paper soaked in oil with a relative permittivity
of 5 (though [both mineral oil and vegetable oil are closer to 2][3],
you get 0.44 μF/m².  Two typical aluminum-foil rolls of 10 m × 400 mm
(see file aluminum-foil.md) with an equal amount of paper will form a
3.5 μF capacitor.  [Mineral oil breaks down around 10–15 MV/m][0] so
this thickness is good to about 1000–1500 V.

[0]: https://en.wikipedia.org/wiki/Dielectric_strength
[3]: https://www.engineeringtoolbox.com/relative-permittivity-d_1660.html

A more polarizable liquid like glycerin ([relative permittivity
41.2–42.5][1]) could improve capacitance and energy density by an
order of magnitude, if the dielectric strength doesn’t suffer; in fact
it’s [reported to be 165 kV/cm = 16.5 MV/m at 55°][2], slightly
higher, and higher still at lower temperatures.  Propylene glycol
might be another appealing alternative.  Like most polar liquids, both
of these are hygroscopic and would therefore need to be sealed
thoroughly against water penetration if water is to be avoided.
However, I’m not sure that, even if anhydrous, you wouldn’t suffer the
same streamer-formation problem found in water-dielectric capacitors,
where upon prolonged exposure to high voltage, streamers
(high-conductivity paths maintained by current flow along them) form
through the fluid.  [Electrolysis is known to be a problem with
glycerin][7], presumably as a result of ionic contamination, but could
possibly be suppressed with a thin insulating layer of glass.

[1]: https://en.wikipedia.org/wiki/Relative_permittivity
[2]: https://ieeexplore.ieee.org/document/8662210
[7]: https://www.pupman.com/listarchives/1997/november/msg00362.html

To reduce water absorption, incorporating a stronger desiccant than
glycerin into the capacitor [was suggested by EEVblog user
Zero999][5]; [coppercone2 listed desiccant alternatives][6], though I
suspect some of the stronger ones in their list might be able to
deprotonate the glycerin!

> P2O5 >> BaO > Mg(ClO4)2, CaO, MgO, KOH (fused), conc H2SO4, CaSO4,
> Al2O3 > KOH (sticks), silica gel, Mg(ClO4)2·3 H2O > NaOH (fused),
> 95% H2SO4, CaBr2, CaCl2 (fused) > NaOH (sticks), Ba(ClO4)2, ZnCl2
> (sticks), ZnBr2 > CaCl2 (technical) > CuSO4 > Na2SO4, K2CO3

Metal hydrides beat anything on the list, I think.

[5]: https://www.eevblog.com/forum/beginners/dielectric-constant-for-glycerin/msg2285412/#msg2285412
[6]: https://www.eevblog.com/forum/beginners/dielectric-constant-for-glycerin/msg2286903/#msg2286903

An important question for high-κ dielectrics is what their electrical
relaxation time is; [glycerol evidently is on the order of 10 ns][4],
much longer than water but much shorter than the relaxation time of
ion-movement relaxation mechanisms.  This means that at higher
frequencies a glycerin-dielectric capacitor would exhibit much lower
capacitances.  Small amounts of water in the glycerin speed this up
enormously, down into the subnanosecond range with 20% water.  For
non-RF uses of capacitors this is adequately fast.  [Other researchers
report much a slower relaxation time when encapsulated in
silicone][8], in the 10 μs range, but they didn’t extend their
dielectric spectroscopy to the sub-microsecond range, and it looks
like the relative permittivity of their composite only dropped from
about 20 to about 13.

[4]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5428894/ "Electrical Characterization of Glycerin:Water Mixtures: Implications for Use as a Coupling Medium in Microwave Tomography, by Paul M. Meaney, Colleen J. Fox, Shireen D. Geimer, and Keith D. Paulsen, IEEE Trans Microw Theory Tech. 02017 May; 65(5): 1471–1478.  Published online 2017 Jan 31.  PMCID: PMC5428894, NIHMSID: NIHMS834917, PMID: 28507391, 10.1109/TMTT.2016.2638423"
[8]: https://backend.orbit.dtu.dk/ws/files/132699850/Glycerol_as_high_permittivity_liquid_filler_in_dielectric_silicone_elastomers_2_.pdf