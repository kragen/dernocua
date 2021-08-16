The shower tank in Mina’s bathroom holds 25 ℓ, though a typical shower
is more like 20 ℓ, and the water is preheated by a gas on-demand
heater.  Unfortunately the plumbing was apparently done by the same
idiot or would-be murderer who installed the deadly fake electrical
system, because the water arrives at the shower tank at a lukewarm
temperature of about 30°.  Raising it to a luxurious 41° would be
desirable; currently I do this by pouring boiling water into the top
from a pot.

If we disregard the variation of water’s specific heat over the
relevant range, v₀t₀ + v₁t₁ = 41° 20 ℓ, t₀ = 30°, t₁ = 100°, and v₀ +
v₁ = 20 ℓ, so v₁ = 20 ℓ - v₀ and we have 30°v₀ + 100°(20 ℓ - v₀) = 41°
20 ℓ = (30° - 100°)v₀ + 100°20 ℓ, so v₀ = (41° - 100°)20 l / (30° -
100°) = (41° - 100°)/(30° - 100°)20 ℓ = (59/70)20 ℓ = 16.9 ℓ, so 3.1 ℓ
is the amount of boiling water to add, and indeed lerp(30°, 100°,
3.1ℓ/20ℓ) is 40.85°.  If it’s just a matter of adding energy to 20 ℓ
of 30° water, though, it’s 921 kJ.

But maybe we could use a much smaller heating unit using
thermochemical energy storage, for example with muriate of lime (see
file `muriate-thermal-mass.md` in Derctuo) sealed in a sturdy plastic
bag.  The idea is that you have some kind of “heat pack” that you dunk
in the tank, then activate, and it adds 921 kJ of heat to the water,
and you have a nice shower and then fish it out of the tank and go
recharge the heat pack.

How small can 921 kJ be?  Fully hydrating the anhydrous salt to the
hexahydrate gives you (2608.01 - 795.42 = 1812.59) kJ/mol (at
110.983 g/mol, that’s 16.3321 kJ/g), but I think you can get further
heat by dissolving the salt and diluting the solution; I’m not sure.
6 mol of water weighs 108.09 g, 2% less than the mass of the anhydrous
salt it would fully hydrate, dropping the energy density of the heat
pack to about 8.1 kJ/g.

This would give us a 114-gram heat pack, which is a *lot* less than
the 3.1 kg of boiling water.

It wouldn’t quite work that well, though: the hexahydrate dehydrates
to the tetrahydrate above 30°, and the tetrahydrate only has an
enthalpy of formation of -2009.99 kJ/mol, leaving only
1214.57 kJ/mol — a third of the stored heat is inaccessible at
temperatures above 30°.  We need less water, though, only 72.06 g/mol.
So you get 1214.57 kJ per 183 g of heat pack, or 6.6 kJ/g, pushing the
heat pack mass up to 140 g.

This same phenomenon limits the temperatures the heat pack will expose
its envelope to.  The various hydration forms have these
characteristics, according to wikipedia and my calculations:

    | H₂O |           | decomposition    | enthalpy of formation |              |            |            |                |              |
    |-----+-----------+------------------+-----------------------+--------------+------------+------------+----------------+--------------|
    |   0 | 2.15 g/cc | 772–775° (melts) | -795.42 kJ/mol        | 110.98 g/mol | 0          | 8.274 kJ/g | 72.89 J/mol/K  | 0.6568 J/g/K |
    |   1 | 2.24 g/cc | 260°             | -1110.98 kJ/mol       | 129.00 g/mol | 2.446 kJ/g | 5.828 kJ/g | 106.23 J/mol/K | 0.8235 J/g/K |
    |   2 | 1.85 g/cc | 175°             | -1403.98 kJ/mol       | 147.01 g/mol | 4.140 kJ/g | 4.134 kJ/g | 172.92 J/mol/K | 1.176 J/g/K  |
    |   4 | 1.83 g/cc | 45.5°            | -2009.99 kJ/mol       | 183.04 g/mol | 6.636 kJ/g | 1.638 kJ/g | 251.17 J/mol/K | 1.372 J/g/K  |
    |   6 | 1.71 g/cc | 30°              | -2608.01 kJ/mol       | 219.07 g/mol | 8.274 kJ/g | 0          | 300.7 J/mol/K  | 1.373 J/g/K  |

The two reversed columns of energy density say that, for example, the
tetrahydrate (plus the water to hydrate it the rest of the way) is an
energy store of 1.638 kJ/g, but in hydrating the anhydrous salt to the
tetrahydrate we produced 6.636 kJ/g of heat.  If that heat couldn’t go
anywhere else, it would have raised the temperature of the resulting
material by 4837°; the reason this salt doesn’t explode is that it
stops absorbing water once it gets warm enough.

In particular, the corresponding calculation for the monohydrate
produces a result of 2970°, so if water is limited enough, even in a
small region, you should be able to reach 260° by hydrating the
muriate of lime.

For a plastic bag, this might be bad; [nylon 6][0] melts at 220° and
[nylon 6,6][1] melts at 264°, and those are the likely plastics
available in a supermarket oven bag.  It would also be a problem if
one part of the material reached 100° while nearby some water was
still pure — the water might boil, float the bag, and burst the bag
with steam pressure.  So it might be best to compromise on energy
density in order to limit the maximum possible temperature; while in
theory you could do this by diluting anhydrous muriate of lime with
glass beads or something, I think it’s probably better to mix together
two hydration levels to set the maximum temperature they can reach
when fully hydrated to below 100°.

[0]: https://en.wikipedia.org/wiki/Nylon_6
[1]: https://en.wikipedia.org/wiki/Nylon_66

Drying the muriate for reuse [can be tricky; a 01964 US patent
3,339,618A][2] describes the situation at the time.  The guy had come
up with a spray-drying process using 370° air to produce anhydrous
calcium chloride.

[2]: https://patents.google.com/patent/US3339618

A different source gives a much lower enthalpy for hydrating muriate
of lime.  A third source mentions that through repeated cycling, some
amount of the salt will hydrolyze into marine acid air; I’d think that
a small amount of chalk in the mix would be adequate to prevent this,
but they seem to think it’s a harder problem.
