I was writing file `glass-powder-bed-printing.md` and came up with the
idea of “powder-bed” 3-D printing that is really more of a layered
paste bed, and I realized that that idea itself is maybe a lot more
broadly applicable than to the lye-fluxed glass-powder bed processes
with full-bed baking prior to depowdering I was exploring there.

In particular, I was exploring the idea of powder-bed 3-D printing
with two binders: a “sacrificial binder” that maintains the integrity
of the powder bed during the printing process but is later removed,
and a selectively deposited permanent “flux” binder which defines the
geometry ultimately produced by the process, and which perhaps is not
active until after all the layers are patterned.  My objective there
was to allow the flux to be blown in dry powder form onto the powder
bed without disturbing it, but now I see many other potential
advantages of this design approach.

One variant for printing in concrete is to trowel on plastic layers,
made of a thixotropic aqueous paste of sand; water; perhaps
reinforcers like chopped basalt fibers or straw; a water-soluble
temporary binder like sugar, carboxymethylcellulose, clay, or
gelatinized starch; and perhaps a plasticizer, which might be the same
as the temporary binder.  Then, on each layer, selectively deposit a
permanent cement such as waterglass, slaked lime, plaster of Paris,
magnesium oxychloride, calcium aluminate, or ordinary portland cement.
This requires the layers to be thin enough, relative to the mobility
of the cement molecules, that the cement can diffuse down to the
previous layer before it sets, or they require you to deposit the
cement vigorously enough to penetrate the whole layer.  In the case of
a slaked-lime binder, you’d have to perforate an array of air holes at
the end of the process to allow CO2 to diffuse to all the layers.
Such objects wouldn’t need to be baked; they’d just need the
uncemented material to be washed away with a water hose once the
cement was set.

Another variant is to pour layers of liquid into a vat or pit, one by
one, allowing hydrodynamics to level each layer rather than using a
mechanical recoater; after pouring each layer, you solidify it with
the sacrificial binder (for example, by allowing excess water to
depart into porous surroundings, or allowing a solvent to evaporate,
or by allowing enough time for thixotropic network formation to gel
it, or by spraying on a pH-changing agent to activate a pH-sensitive
gelling mechanism) and then selectively deposit the permanent binder,
which might be a construction cement like those mentioned above, or
might be a sintering aid like those discussed in the note mentioned
above and in Dercuano, or might be something else.

Another variant is to deposit the layers using spin-coating,
permitting extremely fine and precise layer thickness control.  In
this case, you could still pattern the layer by selectively depositing
a different material on it, such as a catalyst, but another
possibility is to pattern it by using light or particle beams to cause
some kind of change in it, like a multi-layer version of the standard
photolithography process, or stereolithography on a solid substrate
rather than a vat of liquid.  For example, you could draw a pattern on
the layer with a moving laser, move a bar of light sources across it
analogous to how a xerox machine or flatbed scanner scans an image or
how an LED printer prints one, press it up against an LCD that
selectively permits light to pass through, project a pattern onto it
optically with a lens from a projector, or press it up against a thin
mica window through which an electron beam is passing.  Once all the
layers have been patterned, maybe you need to bake it, and then you
can remove the undesired parts of the block, for example by immersing
it in a solvent.

If you were using, say, UV light to pattern the layers in this way,
most of the usual stereolithography resin concerns apply: you need a
component that reacts to the UV, a possibly different component that
does something like polymerize or depolymerize in response, and
something that blocks the UV from reaching the next level down, which
has already been patterned --- a UV-opaque pigment, but not so much of
it that the effect only reaches partway through the layer.  The mix
might include other components as well, for example to affect the
mechanical or electrical properties of the final product, and these
might vary from layer to layer.

In the case of patterning with electron beams, which might offer the
possibility of deep submicron 3-D printing, adjusting the electron
energy may be a more reasonable way to set the penetration depth to
the layer height than mixing in varying amounts of opaque pigment.

If you specifically spin-coat potassium silicate rather than
photopolymers, your “sacrificial binder” can be the dried potassium
silicate itself, while you can inkjet-print the pattern on each layer
with an aqueous solution of a polyvalent-cation salt such as calcium
acetate, which will cross-link the potassium silicate into insoluble
alkali-lime glass.  Once all the layers are printed, if it’s been
adequately protected from CO2, you can redissolve the dried but
uncrosslinked waterglass with hot water, leaving a 3-D-printed object
in alkali-lime glass.  This may be adequately precise and transparent
for fabricating optical lenses; 100-nm resolution in Z should be
easily attainable, and resolution in X and Y will depend on the
precision of positioning and inkjet deposition, easily reaching 30
microns.  Other things to selectively deposit might include aqueous
lead acetate, which will not only make the glass insoluble but
significantly alter its refractive index and dispersion; water-soluble
dyes to incorporate into the final piece; and various kinds of paint
that are intended merely to adhere to the final workpiece rather than
to react with it, such as conductive copper-filled paint.

For cases like that, where the permanent binder consists of polyvalent
cations, you might be able to do your patterning with an array of
transition-metal electrodes in contact with the layer being patterned,
rather than with actual ink jets.  By putting a positive charge on one
of the electrodes, you anodically dissolve some of it and pump the
resulting (generally polyvalent) cations into the workpiece.  This
requires that the workpiece have high enough ionic conductivity for
this to be acceptably fast.

Doing things exactly backwards, you could spin-coat layers of some
viscous solution of some salt with polyvalent cations, like calcium
acetate, and then print “inks” onto them containing water-soluble
compounds that abruptly stop being water-soluble once they see
polyvalent cations; waterglass is one example, but sodium alginate is
another, much gummier example, while e.g., ammonium phosphate is an
example that can form extremely strong and refractory minerals with
many polyvalent cations, and plain old sodium carbonate can form
carbonate minerals with many polyvalent cations.  So you could
imagine, for example, a single spin-coated layer of zinc sulfate
(maybe mixed with other water-soluble solids), on which one of your
inkjet nozzles can create the biocompatible mineral zinc phosphate,
another can create zinc carbonate (smithsonite), a third can create
fluorescent-green zinc silicate (willemite), and a fourth can create
the biocompatible antibacterial hydrogel zinc alginate, all with
submicron precision at least in Z.  After you’ve finished printing out
your array of multi-material objects in a block of mostly zinc
sulfate, you can wash away the unreacted zinc sulfate.  And maybe you
could have other layers that provide other polyvalent cations.

If you’re printing in a pH-sensitive gel like some of the carrageenans
(or, again, waterglass), you can maintain the pH at a level favorable
to gelation of the whole layer during the printing process, but then
pattern each layer by loading some places on it up with a bunch of
buffering agent to *keep* it favorable to gelation.  So, for example,
if your gel is stable at acidic pH but dissolves in basic
environments, you could dump a bunch of a citrate or acetate buffer
into the parts you want to keep; or, if it’s stable in basic
environments but dissolves in acidic ones, you could dump a bunch of
borate buffer in there.  Then, once you’re done printing all the
layers, you can immerse the block in a base (or, respectively, acid),
which will immediately dissolve all the unprotected parts, while
taking a much longer time to attack the printed object.

Returning to the powder-bed context, we could consider the problem of
iron powder metallurgy.  We can build up a powder bed of iron, layer
by layer, and deposit a binder in it that works as a sintering aid (in
Dercuano I suggested graphite, copper, or iron phosphide), and then
bake the result to sinter the iron; but iron is not very rigid at
sintering temperatures, and will tend to sag.  Suppose we mix some
dehydrated active alumina in with our iron powder, and repeatedly
compact the powder bed during printing enough to kind of squish the
iron particles together with the alumina particles, forming a friable
but solid block.  Now, when we bake this solid block, the iron gets
gummy and soft, but the alumina particles remain as firm as ever, and
have enough contact with each other to prevent any macroscopic
deformation.  When the loaf comes out of the oven, the fluxed part of
the block is no longer friable; it’s a solidly connected network of
welded-together iron particles with an interpenetrating network of
alumina particles.  Light wire brushing removes the unsintered volume,
leaving the metal part, and lye, muriatic acid, or oil of vitriol can
destroy the alumina within it, leaving the iron part with great
porosity.  (Infiltration may solve this, or it may be desirable.)

Alumina particles may not be the ideal “sacrificial binder” here;
they’re a very poor binder, so they have to occupy a lot of the volume
to work at all.  There are sol-gel processes for producing alumina
gels, and forming some kind of gel to encapsulate the base powder
particles could allow firmer holding with much lower volume; the most
common sol-gel processes are aqueous, which would be a disaster for
iron powder, but some take place in other solvents that won’t attack
the iron.  But there may be better binders available.

For example, silica gel deposited from tetraethyl orthosilicate might
do a better job of holding the iron particles in place.  In its crude
form its polymerization takes far too long, but perhaps if the iron
powder is mixed with dry glass fibers of length comparable to the
particle size, even slight polymerization would form a continuous
network.  Amorphous silica can handle iron’s sintering temperatures
for the little while that’s necessary, and then you can remove it with
molten lye or hydrofluoric acid without damaging the iron.

Shrinkage is [already a big problem in ordinary pressed powder
metallurgy][0], and the sacrificial-binder approach can solve it
almost completely, at the cost of increased porosity.

[0]: https://www.hoganas.com/globalassets/download-media/sharepoint/handbooks---all-documents/handbook-2_production_of_sintered_components_december_2013_0675hog_interactive.pdf

