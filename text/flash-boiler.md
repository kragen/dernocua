Normally we think of steam engines as being fairly slow, needing
minutes to hours to get up a head of steam.  But what if our heating
elements and the spaces between them are really thin?  They could have
the fractal-heat-exchanger structure I described in Dercuano, where a
very large and very rumpled surface pierced with many thin, short
“capillaries” permits the transfer of a great deal of thermal energy
into water or another working fluid very quickly.

Suppose you have 1-mm-diameter heating elements made of copper pierced
or separated with 1-mm-diameter water channels.  What’s the time
constant of the relaxation of this thermal system when the copper is
much hotter than the water?

[Copper has a thermal conductivity][0] of 401 W/m/K, liquid water of
0.5918 W/m/K, and steam around 0.01 W/m/K.  My first thought is that a
crude approximation is that the water in the middle of the passages is
insulated from the heat from the copper by about 200 microns of water
plus an insignificant amount of copper, which would give you about
3kW/m^2/K.  Each passage, if circular, has a circumference of about 3
mm, so that’s 9 watts per millimeter of passage per kelvin.  A
millimeter of passage has on the order of 1 mg of water in it, and 9
watts would heat a milligram of 4.184 kJ/kg/K water at about 2000
kelvins per second, so under these assumptions the characteristic
relaxation time is about half a millisecond.

[0]: https://en.wikipedia.org/wiki/List_of_thermal_conductivities

That is, if you have a temperature difference of 1000 K, you’ll have
9000 W per mm of passage, which will be heating the mg of water in
that mm by 2 megakelvins per second, so every microsecond the water
closes 1/500 of the remaining temperature gap.

However, if you have Leidenfrost stuff going on, the water will start
to be insulated from the walls by a layer of steam, which will slow
the process down by a factor of 60 or so, up to timescales of 30 ms or
so.  On the other hand, if you have turbulent flow that recirculates
the mass flow of water or steam from the center of the passage to the
walls and back on submillisecond timescales, the process will
accelerate further.  On the gripping hand, hot steam condensing onto
cold water also accelerates heat transfer, which is how nucleate
boiling transfers heat.

So I think millimeter galleries being about a millisecond is probably
about right.  Maybe in reality it’s a tenth of a millimeter or
something because it sure takes a lot more than 10 milliseconds for
hot water flowing through a 10-millimeter pipe to cool down to the
temperature around the pipe, but maybe that’s mostly because the
concrete around the pipe is less conductive than copper.

Copper has some advantages for this kind of boiler thing, although
it’s not as strong as some other metals.  It has great conductivity
and tends not to corrode until well above boiling.

PV = nRT, and the molar mass of water is like 18 grams.  At one
atmosphere and 0° a mole should be 1 mol RT/P = 22.4 liters and 1/18
mol should be 1.25 liters.  At 100° it’s 1.70 liters, so 1 cc of water
boils into 1.7 liters at that temperature, but it’s not doing any work
at that point, since it’s at 0 gauge pressure.  At 250° at 1 atm it’s
2.38 liters.

Suppose the steam is pushing a piston 10 cm in a cylinder of 20 mm
diameter, thus 314 mm².  That’s 31.4 milliliters of steam volume.  For
it to do 1000 J of work over that distance, it needs 10 kN, which
means averaging 31 MPa, 314 atmospheres.  This would need to be
supercritical steam; water’s critical point is about 22 MPa at 650 K
(377°).  At 250° its vapor pressure is only about 3 MPa, so it would
only do about 100 J of work, which is still pretty okay.

At 250° at 3 MPa the ideal gas law gives us a volume of 80 ml for 1 g
of water.  PV/RT is about 390 mg, so if we have more water than this,
some of it will remain liquid.  Say 500 mg.

Heating 500 mg of water to 250° should cost about 0.5 g × 4.184 J/g/K
× 230° = 480 J, though I guess the specific heat goes down a little at
higher temperature, and then boiling it (normally 44 kJ/mol) only
takes about 32 kJ/mol or 1.8 kJ/g, so about another 900 J, for a total
of about 1.4 kJ.  This is not a very efficient steam engine, under
10%.

If we want the 1.4 kJ to be lost in the sensible heat of some copper
as it drops from 300° to 250°, well, copper’s specific heat is 0.385
J/g/K (at room temperature anyway), so that’s about 73 g of copper.
This is an unreasonably large amount of copper to put in contact with
500 mg of water, so a better approach may be to maintain the
temperature of the copper at 300° (to keep it from oxidizing) by
running electricity through it as the water boils.  Alternatively, we
could use a smaller amount of copper at a higher temperature and just
sacrifice it; copper boils at 2562°, and so we’d only need 1.6 g of
copper at that temperature to boil the water, though at that
temperature the specific heat might be significantly lower.  And of
course the engine won’t work for many iterations.

Dumping 1.4 kJ into the copper electrically during the millisecond of
boiling would require 1.4 MW.  If we use 2000 V, above which we start
to encounter special problems, we need 700 A, requiring 2.86 ohms or
less to avoid needing even higher voltages.  If we dump this in from a
capacitor, the capacitor needs to have an ESR that’s not too large
compared to those 3 ohms.

This is pretty challenging.  AVX’s “BestCap” low-ESR supercaps
include, say, the BZ01CB153Z_B, which handles 12 volts, 15
millifarads, and 420 milliohms (at 1 kHz, which is a good speed for
this).  This is 28 mm × 17 mm × 6 mm, more or less, and an energy
capacity of about 1.1 J.  You’d need 1300 such caps to hold the 1400
J, totaling 3.7 liters; a bit awkward.

It gets worse, though.  That’s a time constant of 6 milliseconds, so
in 1 ms you can only get about 15% of the energy out of it.  Other
supercaps are similar.  Aluminum electrolytics are faster but even
bulkier.

No, resistance heating is not the way to go.  The right way to
flash-boil the water is with a packed bed of little balls of something
inert, like quartz or aluminum oxide or porcelain.  You can heat it to
the requisite temperature by blowing hot air over a Kanthal or
Nichrome filament and then over the packed bed, then pump in the water
once the packed bed is hot.

Granite’s specific heat is 0.79 J/g/K, fused silica 0.703, crystalline
quartz sand 0.835.  Alumina (thermal conductivity 30 W/m/K, still far
better than the water) is 0.96 J/g/K, I think, and doesn’t melt until
2277°.  At 1100° the 1400 kJ might need 1.3 grams.  1-mm balls of
fused silica might withstand the thermal shock better than the
stronger but more expansive aluminum oxide, though, even though
alumina conducts heat better: granite’s thermal conductivity is about
1.8-3.8 W/m/K, fused silica around 1.4 W/m/K, sapphire closer to 27.
Embedding copper wires below the surface might help.

Such oxides could perhaps also improve the efficiency and compactness
of the engine by withstanding higher temperatures without corroding.
If one gram of steam is at 600° instead of 250°, then nRT/P at one
atmosphere would be 4 liters instead of 2.38 liters; at 3 MPa it’s 134
ml.  If allowed to expand to only 31.4 ml, nRT/V gives us 12.8 MPa; if
this pressure were constant throughout this expansion, because the
steam is generated exactly as fast as it expands, it does 400 J of
work.  If the pressure is higher at first, because steam generation
finishes earlier, it could do more.

I haven’t calculated here the energy needed to heat the water and then
steam to this temperature, but the 1.4 kJ above was to heat half this
amount of water to 250° and then boil it off at that temperature, so
probably it’d be around 3 kJ.

How do you power the resistance heater?  Suppose you have four 18650s
(weighing 250 g or so) and you use the 1800-mAh 15C types sold for
quadcopters.  Each can provide nominally 27 A at 3.7 V, which is 100
W.  So all four together can provide 400 W, thus providing these 3 kJ
of heat over 7.5 seconds.  So they could activate this piston every
few seconds.
