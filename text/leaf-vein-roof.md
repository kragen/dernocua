Cheap roofs are mostly made out of corrugated galvanized sheet steel,
but this has several disadvantages.  A typical price is
[AR$2070/1.1m²][a85] (US$12/m²) for 500-μm-thick (25-gauge, in the
Argentine system) corrugated galvanized steel, so the cost is not
insignificant.  The metal has no real insulating properties,
reradiating all the heat of the sunlight that it absorbs, and although
its finish is initially quite reflective, soon after installation it
corrodes enough to absorb a lot of sunlight.  It’s kind of heavy (4.4
kg/m²).  It tends to make a lot of noise when things fall on it.  You
have to drill holes in it to fasten it to things, which creates water
leaks when it rains.  It’s a pain to bend or cut.

[a85]: https://articulo.mercadolibre.com.ar/MLA-799068036-chapas-techo-galvanizadas-acanalada-c-25-ternium-oferta-_JM?searchVariation=40210427267

Maybe you could make a better material out of a sandwich panel.  Take
a layer of aluminum foil (50¢/m², see file `aluminum-foil.md`) and lay
down a layer of aluminum window screen on top of it; [a 1.2 m × 30 m
roll costs AR$13244][a86], US$81, US$2.25/m².  Or 200-μm-thick
galvanized steel window screen, [at AR$9053 for 1 m × 30 m][a91],
US$1.90/m².  Or fiberglass window screen; [a 1 m × 30 m roll costs
AR$5377][a87], US$33, US$1.10/m² — though that vendor says it’s
actually not glass but plastic!  On top of the window screen, add a
50mm layer of expanded vermiculite (0.1 kg/ℓ, US$0.23/ℓ, according to
file `refractories.md`), previously moistened with waterglass
(US$2/kg) and a second layer of window screen.  Now press down the
whole pile to ensure good contact among the vermiculite particles, and
solidify the waterglass, either by letting it dry or by gassing it
with CO₂.

(Dehydrated alabaster is a possible alternative binder, and it’s
cheaper at US$0.30/kg, but it won’t coat the vermiculite grains as
nicely, so you might end up using a lot more of it.)

[a91]: https://articulo.mercadolibre.com.ar/MLA-782275624-tejido-tela-mosquitera-galvanizado-rollo-1-x-30-mts-_JM
[a87]: https://articulo.mercadolibre.com.ar/MLA-904121645-tela-mosquitero-de-fibra-vidrio-rollo-1-metro-x-30-metros-mm-_JM
[a86]: https://articulo.mercadolibre.com.ar/MLA-886617841-tejido-tela-mosquitera-aluminio-rollo-120x30-mts-no-se-oxida-_JM

(A layer of chicken wire ([US$40 per roll of 1 m × 25 m][a88], thus
US$1.60/m²) or hardware cloth ([US$82 per roll][a89], thus US$3.30/m²)
might provide additional strength and stiffness.  220g/m² woven
fiberglass cloth for composites is [US$3.50/m²][a90].)

[a90]: https://articulo.mercadolibre.com.ar/MLA-615625188-fibra-de-vidrio-en-tela-roving-220-grsm2-multiples-usos-_JM
[a89]: https://articulo.mercadolibre.com.ar/MLA-907005386-tejido-electrosoldado-50x50mm-16-malla-1x25-m-alambre-_JM
[a88]: https://articulo.mercadolibre.com.ar/MLA-922604748-tejido-hexagonal-gallinero-1-x-1-m-x-25-m-importador-_JM

The window screens provide tensile stiffness, and the somewhat springy
vermiculite provides shear strength and impact absorption.  The
aluminum foil reflects the sunlight and adds a little extra stiffness,
and the vermiculite provides insulation.  The waterglass sticks it all
together, and in particular keeps the aluminum foil from flapping in
the wind.

Let’s guess the weight of the waterglass is about the same as that of
the vermiculite, which turns out to be 5 kg/m².  So 1 m² is US$0.50
(foil) + US$4 (screens) + US$11.50 (5 kg vermiculite) + US$10 (5 kg
waterglass) = US$26.  So our panels weigh 10 kg/m² and cost US$26/m²,
each twice as much as the corrugated steel we were hoping to improve
on.  But now we have insulation and corrosion resistance, the panels
absorb sound and can be cut with a box cutter, and we can drive screws
into them without impairing their water resistance.  And they’re still
fireproof.

Loose vermiculite might conduct heat at [0.06 W/m/K][a92], but with
the waterglass it’s probably more like 0.1 W/m/K.  So if our
vermiculite roof is at 45° and the indoors is at 20°, it will conduct
about 50 W/m², which seems like a lot, even if it’s only 5% of what
enters through an open window.  This is a U-value of 2 W/m²/K.

[a92]: https://www.vermiculite.org/wp-content/uploads/2014/09/Vermiculite-Data.pdf

What’s the flexural strength of the panels?  It seems like it ought to
be something reasonable, but I’m not sure how to calculate it.

In this form, we haven’t yet achieved a Pareto improvement but only a
tradeoff; however, we’ve come within a stone’s throw of the price and
weight of the standard approach.  Can we improve these panels further?

Because we don’t need super high temperature resistance, it’s probably
better to use fiberglass insulation (US$0.026/ℓ, about 0.025 W/m/K,
and also lower density, 0.02 kg/ℓ) or, if properly fireproofed,
styrofoam at [US$1/m² for 20mm][a93] (US$0.05/ℓ, 0.033 W/m/K); both of
these have several times lower thermal conductivity than vermiculite.
(Fiberglass is much less rigid, though, so perhaps it should be
installed below the roofing panels rather than integrated into them.)
Then maybe we could use a thinner vermiculite layer, just to provide a
little stiffness, or a layer of gypsum.  Or two layers of gypsum
separated by a lower-density layer.

[a93]: https://articulo.mercadolibre.com.ar/MLA-624937603-plancha-de-telgopor-1m-x-1m-x-20mm-casa-scalise-_JM

You could use perlite, LECA, or pumice, instead of vermiculite; all of
these are stiffer than vermiculite but also denser and more expensive.
Fired-clay ceramic made porous by the burnout of organic materials
like sawdust or yerba mate is another possibility; though not
commercially available, it's easy to make, and even at 75% or 80%
burned-out filler, it’s still pretty solid.

In a similar way, it ought to be possible to dilute the vermiculite
with another granulated material of about the same granulometry, but
much lower density and strength, without interrupting the continuous
network of vermiculite grains in the finished composite.  Let’s call
this bulking additive “filler”.  Crude reasoning suggests that the
dilution could be up to a factor of 3: in a close packing of spheres,
each sphere is in contact with 12 others, and to form a 3-dimensional
network rather than a 2-dimensional one, at least 4 of those spheres
need to be non-filler.  See file `glass-foam.md` for one filler
possibility; styrofoam and foamed starch are two others.

If the vermiculite grains form a continuous network, these filler
grains could be removed once the material has solidified.  Organics
could be simply burned out; foamed starch could be washed out with
water much more quickly than the water would affect dried waterglass;
anhydrous calcium chloride is a candidate filler that could be washed
out with water and would also instantly, irreversibly harden any
waterglass it came in contact with during the mixing process, keeping
the bulk of each calcium chloride grain from being dissolved.  Calcium
chloride is fairly cheap (US$1.60/kg) and could be reused.

There are other candidate aqueous binder systems that could be
similarly activated by surface contact with grains of a water-soluble
“filler”, including aqueous solutions of soluble carbonates and
phosphates (I wrote about some of these in my Dercuano note on
powder-bed 3-D printing processes) and Sorel cement (where the
“filler” grains would be magnesium chloride).  Reversing the roles,
aqueous calcium chloride itself is capable of forming a thin coating
on grains of aggregate such as vermiculite, and then being hardened by
surface contact with “filler” grains of anhydrous soluble carbonate or
phosphate, or possibly of solid *potassium* silicate.

By carrying out such a “dilution” at multiple granulometry scales, it
might be possible to get much lower vermiculite densities.  Suppose
2-mm expanded vermiculite grains mixed 1:1 with 2-mm filler grains can
successfully form a continuous vermiculite network, with a little
binder, which seems likely.  Then if the resulting 50%-vermiculite
mixture is mixed 1:1 with 5-mm filler grains, the same process should
repeat at larger scales: the vermiculite-network regions should be
able to form a continuous-phase network around the 5-mm filler grains,
for a 25%-vermiculite solid.  A third stage of dilution with 12-mm
filler grains would repeat the process, leaving a 12½%-vermiculite
solid network with “pores” at different scales of 12 mm, 5 mm, and 2
mm, filled with useless filler particles, effectively a foamed foam.

Such high-porosity solids might be useful for a variety of purposes
other than construction insulation.

A thin layer of quartz sand under the aluminum foil, once bonded with
waterglass or something similar, would harden the aluminum-foil
surface greatly against abrasion and impact, as well as providing a
great deal more stiffness per dollar than metal reinforcement could.
Construction sand (relatively pure quartz) costs US$0.03/kg and weighs
about 2.4 g/cc.  A 500-μm-thick layer would thus cost about US$0.04/m²
per side and weigh 1.2 kg/m² (2.4 kg/m² on both sides).  This would
probably require the panel as a whole to be very stiff, because this
layer of effectively mortar would crack off very easily if the surface
flexed much.  Gypsum is more expensive, but lighter and more flexible,
so it might be a better option.  Gypsum used as a binder for other
lightweight, stiff aggregate such as expanded perlite might be better
still.
