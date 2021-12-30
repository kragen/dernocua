Duct tape or electrical tape is a great way to make things; for
example, wallets, pipes, connections between pipes, handles, hammocks,
shoes, masks, baskets, purses, canoes.  It’s really easy to make and
remake a variety of surface shapes, either with an underlying form or
without one, or to seal connections; and the result remains open to
revision.  But when the tape is only sticky because it uses a
constant-tack adhesive, the resulting object never fully solidifies,
is subject to creep, and can’t handle high loads.  There’s something
called “self-amalgamating tape” which avoids this problem to some
extent by bonding to itself and solidifying once it’s in place, but I
think this is generally a potentially much wider-ranging family of
materials.

There’s a thing called “[UD tape][0]” or “unidirectional endless fiber
reinforced tape” which is an existing higher-end version:
thermoplastic tape, 50-500 microns thick and 3-165 mm wide, reinforced
with lengthwise carbon, glass, or UHMWPE fibers.  Typically an
automatic tape layup machine (“ATL”) automatically laminates together
several layers of the UD tape on a flat surface, and then the
resulting flat sheet of composite is pressed and heated to fuse the
thermoplastic together.  Then it can be cut to final 2-D shape, for
example with a waterjet, and thermoformed in a hot press.  Or,
instead, it can be wound around a form to form wound shapes like
wound-fiber tanks.  The matrices/binders are thermoplastics; common
thermoplastics include polyethylene, polypropylene, PET, nylon 6,
polycarbonate, PMMA, or, for stronger results, [PEEK or nylon 12][1].

[0]: https://www.sciencedirect.com/science/article/pii/S2212827117307102 "From UD-tape to final part – a comprehensive approach towards thermoplastic composites"
[1]: https://composites.evonik.com/en/products-services/Tapes

And of course prepreg sheets for fabricating carbon-fiber reinforced
plastics or similar materials are pretty much the same thing: a
flexible woven fibrous sheet of carbon fiber is pre-impregnated with
resin, stored at low temperature to prevent full curing, and activated
by bringing it up to room temperature after it’s incorporated into a
laminate.

There is a very wide spectrum of composites following the general
pattern of some sort of flexible sheet (woven or otherwise) combined
with some sort of adhesive.  As I pointed out in file
`globoflexia.md`, it includes the balloon-covering kind of
pâpier-maché, as well as most carbon-fiber and fiberglass
construction, and it’s especially effective if used to add rigid
shells to easily-shaped foam cores, forming a sort of sandwich panel
which can gain extra strength from surface curvature.  If you can
somehow cut the sheet into a strip and precombine the adhesive with
it, maybe you can use it in the same convenient way as duct tape, but
with much more permanent results.

If you’re precombining the adhesive for convenience, though, you need
the roll of precombined tape to not self-amalgamate into a solid
cylinder before you use it.  There are different ways you could
potentially achieve this.  The adhesive could be activated by contact
with air, if you store the tape in an airtight box.  It could be
activated by spraying it with some kind of chemical.  It could be
activated by the process of peeling it or stretching it as you unroll
it.  It could be activated by the humidity cycling of the air.  It
could be activated by externally applied temperature, as by a heat gun
or sunlight.  It could be activated by pressure, as scratch-and-sniff
books are, for example by breaking open micro-encapsulated reagents in
the tape by burnishing it with a burnisher.  It could be activated by
ultraviolet light, as by sunlight.  And (for me the most exciting
possibility) it could undergo self-propagating high-temperature
synthesis, where once the object is in the shape you want, you light
it (for example, with a match, a blowtorch, or a magnesium strip) and
a hot chemical reaction propagates through the material, converting it
into a different material.

You can use a lot of different possible flexible sheets as bases for
the tape: ordinary cotton cloth, cotton duck (as in duck tape!),
paper, glass-fiber cloth, fiberglass window screening, aluminum window
screening, steel window screening, carbon fiber, basalt fiber, woven
or laminated music wire, ceramic fibers like alumina and zirconia,
woven polyester, sheet polyester like Tyvek, woven glass rovings as in
printed circuit boards, Kevlar or other aramids, UHMWPE fibers,
carborundum fibers, aluminum foil, gold leaf, boron fibers, quartz
fibers, polyimide film, boPET, burlap, hemp cloth, cotton-candy sugar
fiber, flax, silk, glass foil, or foil or cloth made from the common
thermoplastics mentioned earlier, for example.  For any of these that
are fibers, it may be useful to make the fibers unidirectional or
nearly so, rather than evenly distributed in two or three directions,
as in the case of thermoplastic UD tape mentioned above.

If the permanent binder isn’t active until after the tape has been
applied, you may need some sort of “sizing” to hold the binder onto
the base sheet, or in the case of a base sheet made of unidirectional
fibers, just to hold the fibers of the base sheet together.  (Often in
“unidirectional” fibers for composite panel layups, there is
“stitching” or “weaving” of either polyester or the same fiber
material for this purpose, so they are only, say, 90% unidirectional.)
Such sizings might also be useful for holding layers of the tape in
place before the permanent binder is activated, especially if the
sizing is intermittently placed, permitting direct layer-to-layer
contact, unlike the continuous adhesive layers in duct tape and
electrical tape.  Sizings might include conventional
pressure-sensitive or constant-tack adhesives like those used in duct
tape; PVA; other water-soluble polymers such as gelatin, carrageenans,
sodium polyacrylate; the common thermoplastics mentioned earlier;
soluble silicates; “drying oils” such as linseed or poppyseed oil;
soluble polymers such as celluloid and shellac; pine pitch; clays;
soluble salts such as the chlorides of sodium, calcium, or magnesium;
sugar; gelatinized starch; or thermosets such as epoxies, phenolic
resins, or polyurethanes.  In some cases only very light bonding might
be needed, so even very gentle bonds like sublimed ammonium chloride
might work as a “sizing”; this has the advantage that it can be
rapidly infused into a great volume of tape at a reasonable
temperature without introducing any water, which is advantageous if
water would prematurely activate the permanent binder.

Candidate permanent binders include all of those listed above as
sizing candidates, and also geopolymers, plaster of Paris, portland
cement, silicones, phosphates, and brass.

Comments on some candidate tape systems of those described above
----------------------------------------------------------------

I wrote this program; it blindly generates random selections from
4,744,806 possible tape systems.

### Program to generate random combinations ###

	#!/usr/bin/python3
	import random

	thermoplastics = '''
	polyethylene
	polypropylene
	PET
	nylon 6
	polycarbonate
	PMMA
	PEEK
	nylon 12
	'''.strip().split('\n')

	fibers = '''
	cotton
	glass fiber
	carbon fiber
	basalt fiber
	music wire
	ceramic fiber
	polyester
	Kevlar
	UHMWPE
	carborundum fiber
	boron fiber
	quartz fiber
	hemp
	cotton-candy sugar fiber
	silk
	'''.strip().split('\n')

	fibers.extend(x + ' fiber' for x in thermoplastics)

	films = '''
	paper
	fiberglass window screening
	aluminum window screening
	steel window screening
	sheet polyester like Tyvek
	woven glass rovings as in printed circuit boards
	aluminum foil
	gold leaf
	polyimide film
	boPET
	burlap
	glass foil
	'''.strip().split('\n')

	films.extend('woven ' + x for x in fibers)
	films.extend('unidirectional ' + x for x in fibers)
	films.extend(x + ' film' for x in thermoplastics)

	sizings = '''
	common pressure-sensitive adhesives
	PVA
	gelatin
	carrageenans
	sodium polyacrylate
	waterglass
	linseed oil
	poppyseed oil
	celluloid
	shellac
	pine pitch
	clays
	sodium chloride
	calcium chloride
	sugar
	gelatinized starch
	epoxy
	phenolic resin
	polyurethane
	ammonium chloride
	'''.strip().split('\n')

	sizings.extend(thermoplastics)

	binders = '''
	geopolymers
	plaster of Paris
	portland cement
	silicone
	calcium phosphate
	brass
	lead-tin solder
	silver solder
	latex paint
	'''.strip().split('\n')

	binders.extend(sizings)

	def imagine_a_tape():
		tape = random.choice(films)
		if not random.randrange(3):
			tape += ' and ' + random.choice(films)

		if not random.randrange(2):
			tape += ', sized with ' + random.choice(sizings)

		tape += ', with a permanent binder of ' + random.choice(binders) + '.'
		return tape[0].capitalize() + tape[1:]

	if __name__ == '__main__':
		print("A random selection from the %d possible tapes:" % (len(films) * (1+len(films)) * (1 + len(sizings)) * len(binders)))
		for i in range(16):
			print(imagine_a_tape() + '  ')


### Commentaries on some combinations ###

I ran the program to see if it would come up with anything reasonable.

#### Unidirectional nylon 6 fiber, with a permanent binder of silver solder. ####

This would not work in its raw form, both because you need some kind
of sizing to keep the fiber together and keep the solder on the fiber,
and because activating the silver solder requires heating it up far
beyond the melting point of the nylon.  If you added some kind of
refractory sizing, like potassium silicate, then probably you could
get the sizing to both stick the powdered silver solder to the tape
and roughly hold its shape as the nylon burned out, perhaps even up to
the melting point of the silver solder (some 741°), though that’s kind
of pushing it.  Using potassium silicate rather than sodium silicate
would allow you to re-wet the tape if it dried out.

The benefit of this sort of thing is that you could make free-form
jewelry out of it, then solder it into final shape once you were
satisfied; or, you could stick it onto things that you wanted to
silver-solder together that were in positions where loose bits of
silver solder would just fall off.  But I can’t help but think that
unidirectional nylon 6 is nearly the worst base material for these
purposes.

#### Aluminum window screening, sized with linseed oil, with a permanent binder of clays. ####

You can definitely get clay to stick to a strip of window screening
with linseed oil, and as long as this is kept in an airtight
container.  If there’s a bit of grog in the clay to add porosity, you
might even be able to get the linseed oil to solidify all the way
through the shape.  Then you have an “all-natural” free-form thin clay
surface shape which doesn’t need to be fired to cure, at least if
aluminum is natural enough for you.  You might be able to burnish it
to a nice finish after it cured.

If you did try to fire it, the aluminum would burn out, but the
resulting thin eggshell of fired clay would probably still have enough
strength to stand up, at least if it didn’t slump too much in the
kiln.  But if you were going to do that, you’d probably want to leave
out the linseed oil and use water instead.

#### Woven cotton and aluminum foil, with a permanent binder of polyurethane. ####

The cotton layer would bear the mechanical load of the tape, while the
aluminum foil would make it reflective on one side, especially to
infrared.  You’d probably have to use a thermoplastic polyurethane and
“cure” it with heat somehow, rather than using one of those
polyurethanes that polymerizes when it’s exposed to air.

#### Unidirectional music wire and woven hemp, sized with gelatinized starch, with a permanent binder of phenolic resin. ####

This is probably not a good mix.  Unidirectional music wire tape is
probably a useful thing to make, and I guess if you wove hemp through
it you could keep it from coming apart?  The starch would probably
interfere with the resin curing, phenolic resin probably would be too
brittle for anything you’d want music wire for, and the thermoset
curing process for the phenolic would probably soften the music wire.

#### Woven polypropylene fiber, with a permanent binder of clays. ####

You could probably use an oil to get the clay to stick to the
polypropylene cloth, especially if it was loosely woven, and this
could maybe give you a “plasticine tape” that you could make things
with, sealing the different layers together with some pressure.  It
might be hard to unroll from its totally-stuck-together state without
ripping all the clay off the fabric.  Getting water-based clay to
stick to polypropylene would be more difficult, but if you could do
it, you could build fairly free-form thin structures that could then
be either dried or dried and fired.  Normally I’d suggest that you
could keep layers of claycloth from sticking together on the roll by
putting a thin smooth plastic sheet between them, but also normally
that plastic would ideally be polypropylene.

#### Unidirectional glass fiber, with a permanent binder of latex paint. ####

No, I don’t think that would be a useful combination.  You’d need some
kind of sizing to keep the glass fiber together, and generally you’d
want either a fairly beefy permanent binder like geopolymer cement or
epoxy, or a more accessible and convenient fiber like nylon.

#### BoPET, sized with gelatin, with a permanent binder of PEEK. ####

Maybe you can get gelatin will stick to PET if you activate the
surface with a corona-discharge plasma first?  The way you’d activate
PEEK would be by blasting it with heat, which would shrink the boPET
by making its orientation less biaxial, so this would be sort of like
a shrink-wrap tape kind of thing.  I guess that would squish the
(presumably granular) PEEK around whatever the tape was wrapped
around, so that when the PEEK melted it would be in contact with
itself.  Except that I think the PET and gelatin would just totally
melt away, and maybe burn, long before the PEEK started to soften.

Maybe you could activate it with some kind of solvent that softens the
PEEK but doesn’t attack the boPET?  Nothing attacks boPET.

#### Woven PEEK fiber, sized with clays, with a permanent binder of PEEK. ####

I guess you could draw PEEK into fiber, though I haven’t heard of
anybody doing it, and if so you could wrap a tape of PEEK cloth around
something tightly a bunch of times and then turn a heat gun on it.
Maybe if the cloth was impregnated with clay, maybe like glossy
magazine paper, that would increase its viscosity enough to keep it
from melting onto the floor before you’d finished melting it together.
But probably a better way to thus hold it in place would be to mix the
PEEK fiber with some other fiber that was totally unharmed by
PEEK-melting levels of heat, like glass fiber.  Or nylon?  Does nylon
stay solid at PEEK-melting temperatures?  Polyimide would definitely
work but would be expensive.  Maybe you could use an oven-bag-style
*layer* of nylon (or polyimide) on the back of the tape, but make it
full of small holes to permit the layers of PEEK to melt together.

#### Unidirectional glass fiber, sized with polyethylene, with a permanent binder of lead-tin solder. ####

This is definitely a thing you could make.  In fact, glass-fiber UD
tape in a polyethylene matrix is available from multiple vendors right
now; all that’s lacking is granulated lead-tin solder as a filler in
the polyethylene.  Although I haven’t tried it, I think the solder
won’t bond to the glass fiber, no matter what the temperature, and
heating it up enough to flow the solder onto whatever copper pipes or
electronic connections you’re interested in will burn up the
polyethylene, leaving the glass fibers embedded in this solder mass
but not strongly bonded to it.  But the glass fibers would still be
undamaged.

So maybe you could use this combination to coat an entire vertical
surface with solder, or the outside of a copper tank, or something.

#### Woven PET fiber and unidirectional carborundum fiber, with a permanent binder of carrageenans. ####

Well, this would certainly be very strong, and the carrageenan could
probably stick the carborundum to the polyester cloth well enough to
keep the tape intact.  You could store the tape in dry form, then
spritz it with water to activate the carrageenans once you’d wound it
around whatever tank you had.  But you’d probably be better off with a
stronger binder, and maybe a more refractory one, too, because the
virtues of the carborundum are probably going to be wasted with such a
weak binder.

#### Unidirectional polycarbonate fiber, with a permanent binder of nylon 6. ####

I don’t think you can do this because I think polycarbonate melts
lower than nylon 6, and I can’t think of any solvents that will
dissolve the nylon but not the polycarbonate.  The other way around
would work, though, especially with a little adhesive of some kind to
stick layers of the tape together, and it might be a good way to make
free-form shatterproof plastic surfaces.

#### Woven carbon fiber and unidirectional quartz fiber, with a permanent binder of pine pitch. ####

This is silly: two exotic refractory high-strength low-creep
health-hazard fibers and a “permanent binder” of high-creep
low-temperature low-strength colophony, whose principal advantages are
its low toxicity and wide accessibility.

#### Woven polyester, with a permanent binder of silicone. ####

This could work.  The commonplace single-component silicone caulk
cures by absorbing moisture from the air, so if you keep this in a
hermetically sealed container, the tape you pull out will always be
fresh and sticky.  The polyester cloth (I now realize I have a
duplicate in the above list) allows you to wrap a thin layer of
silicone around just about anything, and it compensates significantly
for silicone’s low strength.

Still, I’m not sure what I’d use it for where I wouldn’t just use the
silicone.

#### Aluminum window screening and unidirectional carborundum fiber, with a permanent binder of sugar. ####

Haha, no.

#### Unidirectional PMMA fiber, with a permanent binder of polyethylene. ####

This would almost definitely work; you’d hot-press a UD tape layup to
get a strong, shatterproof sheet that could absorb an enormous amount
of impact energy and wouldn’t suffer even in highly reactive
environments.  Or you could wind it around a form and then heat it up
with a heat gun to fuse the layers together.  I’ve never heard of PMMA
fiber though, just acrylonitrile.

#### Woven cotton-candy sugar fiber, sized with common pressure-sensitive adhesives, with a permanent binder of silver solder. ####

Yeah, no.

#### Polycarbonate film, with a permanent binder of linseed oil. ####

How would you cure the linseed oil through the polycarbonate film?

#### Woven glass rovings as in printed circuit boards, sized with polypropylene, with a permanent binder of sodium chloride. ####

This wouldn’t work; you could spray it with water and dissolve the
salt, but neither the water drops nor the recrystallized grains would
interact with the polypropylene-coated glass fibers.  Without the
salt, it would be glass-fiber-reinforced polypropylene sheet, but in a
form that was hard to thermoform.

#### Unidirectional polypropylene fiber, with a permanent binder of lead-tin solder. ####

Nope, the PP melts too low.

#### Unidirectional UHMWPE, sized with waterglass, with a permanent binder of linseed oil. ####

I don’t think the waterglass will stick to the UHMWPE, because nothing
does.  And the linseed oil is too weak to be useful here.  This won’t
work.

#### Polypropylene film, sized with common pressure-sensitive adhesives, with a permanent binder of sugar. ####

So it’s tape that you wet to make syrup?  No.

#### Woven carbon fiber, sized with nylon 6, with a permanent binder of shellac. ####

You could activate it by spritzing it with alcohol, dissolving the
shellac out of the nylon, I guess.  So it would be a relatively easy
way to do a carbon-fiber layup, and squirting alcohol on it is a
pretty easy way to “amalgamate” it.  The shellac isn’t very strong at
all, but in some situations it wouldn’t have to be.

#### Unidirectional basalt fiber, sized with sodium chloride, with a permanent binder of gelatinized starch. ####

Basalt starch tape with salt in it to keep it from growing mold, I
guess.  All natural!  I guess you activate it by getting it wet?  And
remove it the same way?  At a very small scale this might be a good
way to repair damaged old books, but maybe with copper sulfate instead
of the sodium chloride.

#### BoPET, with a permanent binder of PMMA. ####

I’m pretty sure you can activate this by spraying it with DCM if there
are holes in the BoPET, which you would want so that the PMMA can weld
abundantly from layer to layer of tape.  You could probably just
deposit a film of PMMA on one or both sides of the boPET.

#### Paper, sized with sugar, with a permanent binder of linseed oil. ####

This sounds like decoupage, although I don’t know what the benefit of
the sugar would be.  Maybe it facilitates wet-folding origami?

#### Nylon 12 film, sized with clays, with a permanent binder of celluloid. ####

I guess the film would be heavily perforated, maybe in a honeycomb
pattern of 1-mm holes spaced 2 mm apart.  So you’d get a nice strong
biaxial bond, and then you’d wet it down with something to dissolve
the celluloid (I forget what dissolves celluloid but I bet it doesn’t
hurt nylon) and let it redeposit as a very stiff, rigid, lightweight
plastic sheet.  Which explodes if you get a spark on it.  I like it
except for the clays.

#### Woven nylon 12 fiber and glass foil, sized with PMMA, with a permanent binder of pine pitch. ####

No, that makes no sense.

#### Unidirectional nylon 12 fiber, with a permanent binder of common pressure-sensitive adhesives. ####

That sounds like strapping tape, minus the plastic backing.

#### Unidirectional Kevlar, with a permanent binder of linseed oil. ####

No, that’s ridiculous.

#### Woven Kevlar, with a permanent binder of sodium chloride. ####

That’s even more ridiculous.  You can build furniture and shields with
it that withstand bullets, but they fall apart if you spill your Coke.

#### Woven glass rovings as in printed circuit boards, sized with linseed oil, with a permanent binder of PVA. ####

None of these three materials are usefully compatible with any of the
other two.

#### Woven polycarbonate fiber, sized with linseed oil, with a permanent binder of carrageenans. ####

This sounds like expensive and smelly pâpier-maché.

Less random thoughts
--------------------

In tape systems where you need to apply heat to join the layers
together permanently, as in the various kinds of thermoplastic-matrix
UD fiber-reinforced tapes, it can be extremely inconvenient to do so
externally.  A possible solution is to “print” a grid of a
self-propagating high-temperature synthesis system on one surface of
the tape, a grid of little squares or hexagons whose edges are printed
with, for example, a stoichiometric mixture of iron powder and sulfur,
or a stoichiometric balance of aluminum foil and nickel foil separated
by, for example, a layer of zinc.  These systems, once ignited, will
burn rapidly, producing a high temperature but no gas.  Where they’re
sandwiched between two layers of tape, each with a thermoplastic
surface, they will melt together the thermoplastics in their vicinity.
Although the tapes along the grid line itself will be separated by the
waste products of the reaction and thus will not form a bond, on both
sides of the weld line they will be quite firmly welded together.

Deliquescent substances like calcium chloride may have a useful role
in activating water-activated binder systems like calcium sulfate, by
absorbing water from the air and making it available to the binder in
their vicinity.  I’m not sure that will work in that form; it might
run into the same kinds of difficulties perpetual-motion machines do.
In cases where the lack of a suitable solvent was preventing a
reaction, though, deliquescence can definitely bridge that gap.  This
might work, for example, for producing calcium phosphates from
diammonium phosphate and calcium chloride, initially mixed together as
dry powders, but gradually, after deliquescing, irreversibly reacting
to form calcium phosphates, which can serve as binders under some
circumstances.

Water-activated permanent binders like slaked lime, portland cement,
and plaster of paris can’t be coated onto the backing with water-based
“sizings”.  You need to use some kind of anhydrous or almost-anhydrous
approach.  Maybe a polymer like polystyrene dissolved in a nonpolar
solvent like acetone, for example, or shellac in ethanol, would work
for this sort of “sizing”, as long as there isn’t so much present that
it will waterproof the permanent binder particles or keep them from
being able to interact.  Above I also suggested subliming ammonium
chloride into the tape to deposit some relatively inert salt crystals
to stick things together.
