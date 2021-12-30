In Dercuano I wrote a bit about a family of likely-feasible powder-bed
3-D printing processes where you print the shape by selectively
depositing some “flux” in a powder bed (for example, by inkjet
deposition of a dissolved aqueous binder, or by trickling granulated
binder from a vibrating chute or screw extruder, like making a sand
painting), then bake the whole powder bed to activate the flux,
forming a solid object.  I had done a few manual tests with 100-micron
quartz flour and various different candidate fluxes fired at IIRC
1040°, getting some promising results.

Well, now I have a lower-temperature version of the process that I
have a lot of confidence in, although I haven’t tried it.

Lye-glass 3-D printing
----------------------

The powder bed consists of sieved pulverized soda-lime glass, which is
one of the candidate fluxes I’d tried at the higher temperatures.  The
flux is lye.  The lye becomes very reactive when heated past its
melting point of about 320°, capable of attacking soda-lime glass at
corrosion rates millimeters per minute, and forms waterglass with the
surfaces of the glass particles, which is less reactive and has a
higher melting range than the lye; it bonds the glass particles
together into a solid mass.  This is too viscous and has too much
surface tension to infiltrate the rest of the mass, so unfluxed glass
particles remain inert; soda-lime glass generally doesn’t soften below
some 700°, so at this baking temperature, the glass won’t stick
together.

Generally molten lye is considered a material meriting the sort of
respect we accord to molten steel, lava, or RFNA (unless we’re
cleaning our ovens, in which case we often treat it casually), but in
this case we’re dealing with very small quantities which exist for
only a short time within the hot powder bed.  If the glass granules
have a size on the order of 100 microns, they might each occupy 0.6
nanoliters and be associated with an additional 0.4 nanoliter void
space.  If the lye is initially deposited as a 1-molar solution,
that’s about 4% by weight or 3% by volume, so we have about 0.01 nl of
lye for each 0.6-nl glass granule, distributed among the “necks”
connecting it to its neighbors; even the mass in the fluxed zone is
98% inert glass and 2% molten lye, and the overall powder bed might be
more like 0.2% molten lye and 99.8% inert glass.  A 1-kg printed glass
piece might include some 20 g of lye before firing.

After baking the powder bed, first at 100° long enough to drive off
any water and then at 350°-500° to sinter the lye-fluxed glass
particles, depowdering the finished object should be straightforward,
and the leftover powder can be sieved and reused.  The total kiln time
should be on the order of an hour, more for thicker powder beds
through which the heat will propagate more slowly; slow heating and
cooling may also be necessary to prevent breakage.  Pressure will not
be needed to cause sintering, and may not be effective, since the
rigid support from the unfluxed particles will prevent any significant
compaction of the fluxed particles.

### Variations ###

Although I’m now pretty confident that the above will work, there are
a number of variations that might be better; some are sure things,
others less so.

#### Aqueous lye thickeners, including no-bake waterglass ####

If the lye is deposited as a liquid solution, inkjet-style, it may be
helpful to use ethanol as part or all of the solvent to reduce the
surface tension and thus the size of the binder droplets, as well as
accelerating evaporation.  To prevent it from spreading out through
the powder bed once deposited, it may be helpful to either use a very
high lye concentration, like 50% (12M), or to include alkali-tolerant
thickeners (especially thixotropic thickeners) to get high viscosity
and avoid filling the void spaces in the powder bed.  Such thickeners
would become part of the final workpiece, which probably rules out
most organic chemicals, since they would char and turn the glass
black.

Being able to use lower lye concentrations in the flux would be
valuable because concentrated lye solutions are super annoying.

Of course the most obvious thixotropic alkali-tolerant thickener to
use would be waterglass itself, in which case you don’t need the lye
at all and may not need the baking step either.  Exposure to carbon
dioxide, either as a gassing step after printing or just from the
atmosphere, may provide adequate strength.

#### Pure amorphous silica powder bases ####

Fused silica, silica gel, or silica fume (perhaps granulated) may be a
more suitable powder base than the cheap-as-dirt soda-lime glass
discussed above.  Their absence of alkaline-earth metals enables them
to react more readily with alkalis, they have much lower thermal
coefficients of expansion, and they do not sinter on their own until
higher temperatures, perhaps 1000°-1600°.  But the resulting
soda-silica glass is much more vulnerable to corrosion from water than
conventional soda-lime glass.  You might be able to add borax to the
flux, perhaps reducing or eliminating the lye, to get a borosilicate
glass instead of a soda-lime glass.  But you need a *lot* of boria for
borosilicate glass, like 8%-15%, and borax only dissolves at like 25
g/l at room temperature, up to 250 g/l at 70°.  Using very porous
powder bases like silica fume or dehydrated silica gel might ease this
constraint, but will tend to produce a lot of porosity in the final
print.

#### Desiccants in the powder base ####

Incorporating desiccants into the powder base is another possible way
to prevent binder droplets from spreading out once deposited; they
don’t need to be stronger desiccants than the lye, just strong enough
to diminish the free liquid volume somewhat and keep the lye from
escaping.  Promising desiccants for this purpose include silica gel
itself, activated alumina (incompletely calcined aluminum hydroxide),
quicklime, and zeolites.

#### Cristobalite or other crystalline silica polymorphs as the powder base ####

A totally different powder base that perhaps could form waterglass
with lye more easily than soda-lime glass or quartz sand (see below
about the crude sand experiment) is cristobalite; [Hachgenei et al.’s
US patent 5,215,732][0] explains that at room temperature,
cristobalite (or “tempered quartz sand” containing a mixture including
cristobalite, the other high-temperature polymorph tridymite, and
amorphous silica) is so much more reactive than quartz that you can
convert it completely into waterglass by boiling it in 50% lye at
112°-146° for only three hours, even with a 2:1 ratio of silicon to
sodium (“modulus”).  Higher ratios of sodium to silicon naturally run
faster.  He gives the sand grain size as “in general, ... 0.1 to 0.8
mm,” so the corrosion was advancing toward the center of the sand
grains at around 30 nm/s, times or divided by four.  He reports being
able to thus “temper” quartz by calcining it “above 1000° C.,
preferably at 1300° to 1600° C., with the addition of catalytic
quantities of alkali”, and, presumably, not annealing it back to
alpha-quartz.

[0]: https://patents.google.com/patent/US5215732A/en "Method for Producing Alkali Metal Silicates by Heating Cristobalite or Tempered Quartz Sand With NaOH or KOH Under Atmospheric Pressure"

#### Blowing powdered flux onto a powder bed bound with a temporary binder ####

My original flux-deposition notes contemplated depositing the flux as
a powder, for a fully dry 3-D printing process.  It’s desirable to use
as fine a powder as possible, because the grain of the powders limits
the dimensional precision of the workpiece; even if you deposit your
flux with 10-micron precision, each 100-micron-wide flux particle that
becomes part of a surface is going to produce roughness on the order
of 50 microns.  Similar concerns apply to the powder-bed particles: if
your flux particles are sticking together 100-micron-wide particles of
aggregate, you’re going to get surface roughnesses on the order of 100
microns.  But using fine floury powders for the powder bed isn’t
problematic; however, fine floury powders of flux tend to clump up
into larger lumps, as the surface forces between particles overwhelm
their weight and inertia.

I’ve written about various approaches to solving this problem in file
`trickler.md`, but a new one occurred to me in this context.  If you
can blow the flux powder through a nozzle with a compressed air blast,
you can do an excellent job of breaking up aggregates, because the
aerodynamic forces on the particles tend to scale with their surface
area, just like the surface adhesion forces they’re fighting, not with
their volume.  So you can blow very fine dust through a quite fine
nozzle, although once you’re down in the sub-ten-micron range you
start having safety concerns.  But of course if you’re blowing that
air blast onto a powder bed, those same aerodynamic forces will tend
to disrupt the powder bed, which is why I’d never considered this
solution before.

The objective here is for the powder bed to be an unbound, loose
powder after baking, except in the places where enough flux was
deposited to enable it to bake to a solid.  So you’d think that
including a binder in the powder bed would be totally
counterproductive.  But if we use a *sacrificial temporary* binder
that bakes off during the baking process without leaving a residue, it
could still work!

Suitable sacrificial temporary binders might include water (as used in
traditional fired-clay ceramics), ethanol, gasoline, kerosene,
toluene, turpentine, d-limonene, acetone, ethyl acetate, dimethyl
sulfoxide, isopropanol, formamide, hydroxylamine, sulfur, naphthalene,
and various salts of ammonium (chloride, carbonate or bicarbonate or
carbamate, acetate, sulfate); most of my notes on these are in file
`inorganic-burnout.md` in Derctuo.

Some of these candidate sacrificial binders, like water and ethyl
acetate, are ordinarily liquids, which means that the powder bed is
sort of more of a paste bed; the powder base might be premixed with
the liquid, so that the recoater trowels on one layer after another
like drywall mud or construction mortar.  This could lead to geometric
disturbances from subsequent recoating layers, though that might be
solvable; the usual practice with construction mortar is to minimize
this problem by including barely enough water in your mortar to make
it plastic, and as soon as you trowel it onto the wall, it loses
enough water to lose its plasticity.

Alternatively, the recoating could be done with a powder recoater in
the usual way, which is gentle enough not to perturb previous layers,
then misted with the sacrificial binder liquid.

Other candidates, like ammonium chloride and ammonium carbonate, are
ordinarily solid, so if the base powder particles are bonded together
by them, it becomes a solid object, which avoids the issue of
geometric disturbances when recoating, but poses the problem of how to
get the sacrificial binder into the powder.  If it’s just mixed in as
separate particles, it won’t be form bonds between the base powder
particles that are adjacent in their final position.  Ammonium
carbonate is water-soluble; it could be sprayed onto the base powder
once it is in position, or the base powder could be mixed with an
aqueous solution of it, and in either case we would need to evaporate
the solvent to get to solidity.  Ammonium chloride has an additional
power: it can be “sublimed” at convenient temperatures, so it could be
analogously infused into the powder once it is in place without
needing a liquid solvent.  Or it can be formed in situ by reacting
ammonia with muriatic acid.

See file `two-binder-powder-bed-printing.md` for more variations on
the theme.

### In-situ temporary binder creation ###

Some candidate temporary binders, like muriate of ammonia, can be
produced in situ in the powder bed by applying two different reagents
at different times; in that case, ammonia and muriatic acid can be
infiltrated into the powder bed in gas form, one after the other,
where they will react to form the salt.

### Salt as flux ###

Some of the alternative powder-bed bases such as cristobalite or
amorphous quartz offer the possibility of using ordinary muriate of
soda as a less annoying alternative to lye that activates at higher
temperatures.  It has been used for [salt-glazing of pottery][1] for
600 years.  At 1100°-1200° in a steam atmosphere it forms muriatic
acid gas and lye; the former escapes, driving the reaction forward,
while the latter fluxes the silica as before.

Wikipedia claims that silicates of iron are even more effective fluxes
for this purpose, so reduced (ferrous) iron helps even more, and red
clays are well-known to be lower-firing; however, ferrous silicate on
its own is fayalite olivine, and olivine is the canonical high-melting
mineral at the high-temperature extreme of Bowen’s reaction series.
But I think *fayalite* olivine may indeed be low-melting; [a 01993
abstract in Science][2] gives its melting point as 1478 K, which is
only 1205°.  So some ferrous iron in the powder bed may help the
process along.

[1]: https://en.wikipedia.org/wiki/Salt_glaze_pottery#Process
[2]: https://pubmed.ncbi.nlm.nih.gov/17841870/ "High-Temperature XAS Study of Fe2SiO4 Liquid: Reduced Coordination of Ferrous Iron, Jackson et al., 10.1126/science.262.5131.229 "

### Soda ash ###

Higher-temperature powder-bed bases might also be able to use soda ash
as a flux.  Soda ash is water-soluble, even cheaper than lye, less
annoying to handle, and melts at only 851°.  My experience melting it
with a butane torch suggests that it has an alarming tendency to
bubble, perhaps because it is slowly converting into lye.  This
produces only carbon dioxide gas rather than muriatic acid.

### Iron as flux ###

If iron silicates are crucial to the fluxing effect in the
salt-glazing of pottery, perhaps metallic iron or some iron salt could
form these iron silicates directly with soda-lime glass at lower
temperatures than those necessary for salt-glazing.  Ferric chloride
melts at only 308° but has a very narrow liquid range, while green
vitriol starts to decompose into high-melting hematite at 680°.

### Wood ash ###

If transparency of the glass produced is not a concern, wood ash might
be a possibility; it would surely be the cheapest flux for powdered
glass, if it works.  It is mostly carbonates, oxides, and hydroxides
of alkali and alkaline earth metals, including lye; leaching out the
water-soluble components will tend to eliminate the counterproductive
polyvalent cations.  [Traditionally][3] this was done by washing the
ash on top of linen cloth, then boiling down the results to reasonably
pure potassium hydroxide.

[3]: https://en.wikipedia.org/wiki/Ash_burner

Crude sand experiment
---------------------

I did a crude and deadly kitchen experiment the other day which seems
to have successfully made a little waterglass from quartz and lye.  I
placed a layer of damp construction sand in a thin stainless (or
nickel-plated?) metal bowl, sprinkled a layer of lye flakes liberally
on top of the center of the layer of sand, then pressed down another
layer of damp construction sand on top.  I covered the bowl with
aluminum foil, placed a paper towel over the aluminum foil, added an
aluminum-foil skirt around the edge to reduce the loss of radiant heat
from the bowl’s sides, gently heated it on a gas stove burner (maybe
500 W) until the lye flakes stopped crackling from the release of
water.  Then I turned the burner up to max (maybe 1500 W) for an hour;
halfway through I moved the bowl over a bit to ensure that there were
no cold spots that never got heated.  I left the sliding-glass door
open so that the draft would carry any fumes from the bowl away from
me.

Unfortunately I don’t have a thermometer.  Some of the aluminum foil
skirt around the sides of the bowl strayed into the gas flame and
melted, but on the various occasions during the hour when I inspected
the crude apparatus, no part of the bottom of the steel bowl itself
was ever glowing visibly, so it had not reached the 525° Draper point.
When I turned the flame off, tore open the aluminum foil, and poked
the sand with a chopstick, the end of the chopstick charred and
smoked, but didn’t burst into flames, so the top of the sand was
probably somewhere between 250°-350° at that point.  The sand had
formed a hard mass, infiltrated by the molten lye, although not, as it
turned out, around the edges of the bowl; only in the middle.
Presumably the sand in the bowl was hottest on the bottom where it was
separated from the flame only by a thin layer of steel, with a net
heat flow in at the bottom and out at the top producing a thermal
gradient through the sand.

Upon cooling I was able to use the chopsticks to lift up a large
monolithic aggregate of sand that extended all the way to the bottom
of the bowl; at its bottom and top surfaces its color was the beige of
the sand, but in between, where the lye flakes had been, it was much
more white.  No intact lye flakes were in evidence; they had all
completely melted, so that part of the sand had exceeded 320°.

I broke off a small piece of the aggregated sand with the chopsticks
and dropped it into a polypropylene bottlecap to which I added a few
drops of water; it disintegrated immediately, indicating that the
binder was probably mostly lye, not mostly waterglass.  A couple of
flakes of aluminum foil added to the bottlecap fizzed
enthusiastically, confirming the presence of free lye.  So at this
point I had no indication that any waterglass had been formed.

I neutralized the rest of the sand by soaking it with kitchen vinegar;
after letting it stand a while, I added a pinch of baking soda, which
fizzed, confirming that the pH had been brought down below neutral.
This ensured that any lye had been not only dissolved in water but
converted to highly soluble sodium acetate; at the same time, the
lower pH would make any waterglass present almost entirely insoluble
in water.

Stirring around the sand with my fingers, I found that most of the
aggregated chunks had disintegrated immediately upon wetting or were
easily broken up.  However, one irregular chunk of aggregated sand of
a centimeter or three in every dimension remained intact, indicating
that it was completely bound together with something other than frozen
lye, almost certainly waterglass.  Handling it wet did not leave my
fingers slippery, providing further confirmation that free lye was not
present.
