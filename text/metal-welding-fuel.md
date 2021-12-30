I was watching an Abom79 video about spray welding (or “thermal flame
spraying”) and it occurred to me that maybe you can dispense with the
welding gas entirely.

Suppose you wanted a welding torch, or better a metal-cutting torch,
that used *only* iron filings as fuel, perhaps only for emergency
situations.  Clearly burning iron or steel can produce a high enough
temperature to burn iron or steel in a stream of oxygen, and I think
compressed air would also work, though it isn’t the usual practice.
You could think of this as a thermic lance adapted to use powder.

You could imagine that the “flame” it produced could be quite small,
perhaps submillimeter in size.  Perhaps initial ignition could be
provided by an arc igniting iron filings suspended in air within an
ignition chamber; once ignition was achieved, though, it would
probably be more practical to continue combustion outside the torch
body in eddies of more-slowly-moving gas, just because otherwise the
rapid heat production seems certain to destroy the torch, even if the
combustion chamber is pyrolytic graphite.  Maybe if you water-cooled
the walls or something.

The enthalpy of formation of formation of Fe2O3 is -824.2 kJ/mol, and
its molar mass is 159.687 g/mol, of which 2×55.845 = 111.690 g is the
iron fuel.  Unlike the case with things like propane, the combustion
product is liquid rather than gaseous (Fe2O3 melts at only 1539° but
doesn’t boil until 2664° according to PubChem; magnetite, which melts
at 2623°, oxidizes to hematite upon sufficient roasting in air, while
producing magnetite from hematite normally requires reduction with
hydrogen, though presumably a much higher temperature would also work)
so heat is not carried away nearly as rapidly.  At ordinary
temperature its heat capacity is some 103.9 J/mol/K, which would give
us an extrapolated “maximum flame temperature” of some 7900 K above
ambient (824200/103.9); [NIST gives 68.2 J/mol/K][0] in liquid form,
giving an even higher maximum temperature.

[0]: https://webbook.nist.gov/cgi/cbook.cgi?ID=C1345251&Type=JANAFL&Table=on#JANAFL

The stoichiometric mixture of iron filings and oxygen, which is
probably reasonably close to optimal for this sort of thing, would be
two moles of iron (111.690 g, as explained above) to three of atomic
oxygen (48 g) or 1.5 moles of oxygen molecules.  Solid iron weighs
7.874 g/cc, so this is about 14 cc of iron; a room-temperature mole of
an ideal gas is about 24 liters at atmospheric pressure and 20°, so to
burn those 14 ml of iron we would need 36 STP liters of pure oxygen or
172 of ordinary air.  A more practical point of view is that 111.690
*mg* of iron would occupy 14 μl and need 172 *ml* of uncompressed air
to burn it, yielding 824 J.

Probably about as far as you can compress air in practical terms is
some 4000 psi, in medieval units, or 28 MPa or 270 atm; if it were to
behave as an ideal gas at this concentration, then when cooled to room
temperature, it would have a density of some 0.33 g/cc; the 172 ml of
room-temperature air would then occupy some 640 μl.

If this mixture of air and iron were burned and squirted out in a
100-micron-wide burning jet, I feel like it could get pretty hot, but
how hot would I guess depend on the equilibrium between the process of
combustion generating heat; the process of radiation, which would cool
the jet; and the processes of of expansion and mixing with cooler air,
which would tend to expand the jet out pretty rapidly.

The maximum energy density of this mixture would be 824 J per (640 +
14)μl, which is about 1.3 MJ/l, similar to primary-battery levels and
almost up to rocket-propellant levels.  It isn’t obvious to me how to
calculate the maximum power per unit area that could be supplied by
the hot jet; that would seem to depend on the achievable gas velocity
and combustion velocity of the jet.

The 78% nitrogen mixed into air has a heat capacity of 29.124 J/mol/K,
and there would be 5.6 moles of nitrogen per mole of Fe2O3, adding a
considerable extra “thermal mass” of 162 J/mol/K to the 103.9 J/mol/K
of solid Fe2O3 or 68.2 J/mol/K of liquid Fe2O3.  Still,
824200/(162+104) is still 3100 K, which is still way hotter than we
need.

The relatively small amount of carbon mixed into steel will produce
carbon monoxide or dioxide; in the context of burning in highly
compressed 78%-nitrogen air this is not significant, but of course it
has a very visible effect when steel sparks are burning on their own.

You’d probably want to either sift the metal powder down into the gas
jet, as modern spray-welding torches do, or ensure that the gas
blowing up through the metal powder reservoir was traveling fast
enough to prevent flashbacks into the metal reservoir.

Speaking of water cooling, some metals can burn in steam instead of
air; this has the potential advantage that steam is 89% oxygen rather
than 21% and wouldn’t need to be compressed the way air is.  However,
I don’t think iron can burn this way.  Water’s enthalpy of formation
is -285.83 kJ/mol, so stealing the three oxygen moles for a mole of
Fe2O3 would take 860 kJ.  So I think the reaction would be
endothermic.  Powdered aluminum or magnesium would work, though, and
although aluminum oxide would be a nuisance if you were trying to weld
or cut steel, magnesium oxide might be tolerable.
