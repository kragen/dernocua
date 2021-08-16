As explained in file `material-observations.md`, I filled a small
plastic shopping bag with methane, but to my disappointment it did not
rise into the air.  Calculations suggest that methane has
(12+4)/(.79×2×14+.21×2×16) ≈ 55% of the density of air, so should
provide some 500 mg/ℓ of lift.  I didn’t weigh this bag beforehand or
measure its volume, but it surely only contained a liter or two of
air.  Average plastic shopping bags weigh about 5 g, but lightweight
ones weigh as little as 100 mg.  None of the ones I have here weigh
less than 800 mg; a household garbage bag (550 mm × 480 mm) weighs
10.9 g, and another bag nearly as big (470 mm × 460 mm) only weighs
4.5 g.  A 1.1 g pharmacy bag (170 mm × 240 mm) weighed 1.1 g.  Several
bags of intermediate size weigh around 3 g.  The sturdy 8-liter bags
from the sandwich shop weigh a little over 9 g.

If we approximate the volume of the 4.5-g bag as a 470-mm-long
cylinder wih 460-mm half-circumference, it would hold almost 32 ℓ,
enough to lift about 16 g, so it should definitely fly, but only by a
factor of about 3.  (And so should the garbage bag.)  If we scaled it
down by a factor of 3 to a 160-mm-long cylinder with 150-mm
half-circumference and 500 mg of mass, it would only hold 1.1 ℓ and
thus be just on the edge of buoyancy.  Most of my bags seem to be a
lot thicker than that, so they’ll only fly if they hold several
liters.

4.5 g over twice 470 mm × 460 mm is 10.4 g/m², so if the plastic is
close to 1 g/cc (it is — it’s high-density polyethylene, not lead or
something) it’s about 10 μm thick, same as the aluminum foil we get
here.  So this is probably about as good as it gets without going to
gold leaf or exotic composites.  Note that this suggests that ordinary
balloons (and bladder and intestine tissue) stretch even thinner than
this.

Lifting this body into the air would require 115 kg of lift, a sphere
of 2.8 m radius if filled with vacuum, or with methane (45% of the
lift of vacuum) 3.7 m, or 170 m² of surface area.  Hydrogen would
probably be a less dangerous lifting gas for humans suspended below
it, with more tendency to rise upwards when there’s a rupture and less
tendency to radiate heat downwards if it catches on fire.  There’s
still the problem of how to stop falling before the ground kills you,
though.

Unfortunately Mina doesn’t want me to fill a bag with 32 liters of
inflammable gas in the kitchen, which I have to say is an entirely
reasonable preference.  And either compressing the gas or running a
hose to the park seems daunting.  And, although CNG cars are common
here, we don’t have a friend who has one.

A hydrogen generator would be a much more portable solution, and has
the advantage that hydrogen is only 7% of the density of air, so you
get a little over twice as much lift.  A 1-ℓ sphere 124 mm in diameter
has a surface area of 0.048 m² and would thus require 480 mg of 10-μm
polyethylene to enclose it, so the critical limiting scale with those
materials would be about 50 mm in diameter: 65 mℓ, 0.0079 m², 79 mg of
plastic, 79 mg of air displacement.  7% of 1.2 g/ℓ is 80 mg/ℓ, so
you’d need 80 mg of hydrogen to fill a 1-ℓ sphere.  Let’s pick 2 ℓ as
a reasonable size, with a good bit of safety margin for
non-idealities.  If we use a tubular bag that’s 120 mm in diameter, it
will be 177 mm long and, when stretched out flat, 188 mm wide.  At
10 μm two such rectangles are 666 μℓ and thus about 666 mg of HDPE.
The requisite 160 mg of hydrogen is 0.079 mol, which the universal gas
law tells us is 1.9 ℓ — off by 5%.

To make it we need to electrolyze 0.079 mol of water, about 1.4 g,
which seems like an eminently practical amount of water to carry to
the park.  If our Faraday efficiency were 100%, each electron would
liberate a hydrogen ion, so we would need 0.158 moles of electrons,
about 9.5 × 10²² electrons, which turns out to be 15 kilocoulombs, 4.2
amp hours; at 2.4 volts that’s 37 kJ; at 200 watts that’s 3 minutes.
And in practice I think the Faraday efficiency will be more like 60%,
so it would be more like 6 minutes.

[NREL Conference Paper NREL/CP-550-47302 explains that
electrolysis][0] requires 237.2 kJ/mol of electricity and 48.6 kJ/mol
heat.  The number I came up with above is 234 kJ/mol (37/0.158 = 234),
so I guess I did the ideal-Faraday-efficiency calculation right, but
it didn’t occur to me that the reaction was endothermic!  Although
this must be purely by chance, since they’re saying the actual voltage
is 1.229 volts, not 2.4 volts.  “Whereas the practical fuel cell
operates well below 1.23 volts (in the range of 0.750 to 0.900 volts),
the practical electrolysis cell operates above this voltage in the
range of 1.60 to 2.00 volts.”

[0]: https://www.nrel.gov/docs/fy10osti/47302.pdf "Hydrogen Production: Fundamentals and Case Study Summaries, K.W. Harrison, R. Remick, and G.D. Martin, National Renewable Energy Laboratory; A. Hoskin, Natural Resources Canada"

Well, 285.6 kJ/mol * 1.8 V / 1.23 V = 420 kJ/mol, or 66 kJ for
0.158 mol.  So basically 100 kJ.

100 kJ of batteries is about US$4 of lead-acid batteries; the US$8.30
2-kg 7-amp-hour Risttone battery mentioned in file
`energy-autonomous-computing.md` holds 300 kJ, 150 kJ/kg.  A
lithium-ion version would be about ⅙ the weight for the same energy
capacity, or ⅓ for a high-power battery, but those cost ten times as
much per joule or more, and the limiting factor becomes power rather
than energy.  So we’re probably talking about a battery that’s
practical, but a bit cumbersome, to carry to the park.

A different alternative would be to fill the bag with azane, which has
even less lifting power (17.031 g/mol compared to methane’s 16.043 or
air’s 28.9) but can be dissolved 30% by weight in water at 25°,
forming a strongly basic 26°Bé (1.22 g/cc) solution; at 0° this rises
to 47% by weight, and at 60° to something like 10%.  20 ℓ of ideal gas
would be 0.831 mol, 24.0 g of air or 14.2 g of azane, thus lifting
9.8 g.  14.2 g of azane could be dissolved in 47.3 g of aqueous azane
solution occupying about 38 mℓ, then liberated by heating it, as in an
absorption refrigerator.  (And you’d need a “water separator” or
“moisture separator” or “mist eliminator”, also as in an absorption
refrigerator.)  A disadvantage of this is that it has a strong smell
that the vulgar may associate with its use in witchcraft.

At pure azane’s boiling point of -33.4°, its ΔᵥₐₚHΘ is 23.35 kJ/mol,
so perhaps at a higher temperature from aqueous solution it would be a
bit lower; maybe this would require 15 kJ of heating.  This doesn’t
sound like much of an advantage over 66 kJ, but you could supply it
with a candle, or with thermochemical energy storage like muriate of
lime (combined with water in a separate chamber).

The other traditional way to make hydrogen on demand is with lye and
aluminum foil; zinc and muriate of lime reportedly also work, and
hydride of calcium has been used for inflating weather balloons for a
long time.  I guess I should figure out the stoichiometry of this; a
couple of liters seems like it ought to be doable...
