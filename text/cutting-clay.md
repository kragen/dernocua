I’ve been interested in sheet-cutting automated fabrication for a
while as a more practical alternative to 3-D printing for many
purposes, and I just realized that there may be a considerably more
accessible variant of this technique right under my nose.

I was watching a video on “[clean cutting with polymer clay
cutters][0]”.  The author gets 3-D-printed cookie cutters to cut a
previously rolled sheet of “clay” cleanly by first sticking it to
something it will stick to, like glass or ceramic, then scraping it
off afterwards, a process which may distort it.  However, they also
point out that putting plastic wrap over the top of the “clay” will
keep the cutter from sticking to it, and then the wrap can be peeled
away; and then the bubbles trapped under the wrap produce little
shallow hollows in the surface.

[0]: https://youtu.be/ci7OY7H4I14

This wrap-layer approach provoked many thoughts about automated
fabrication.  This probably works with pastes such as real clay in its
plastic state too, and maybe even better in its leather-hard state,
I’m not sure.  In the leather-hard state adhesion is not much of a
problem.

Also, it probably works with molten thermoplastics (rather than
plasticizer-impregnated “polymer clay” plastics, as shown in the
video).  A thermoplastic of a higher melting point can serve as the
protective anti-adhesion wrap; for example, nylon oven bags for baking
chicken would work adequately for a lot of common plastics that won’t
dissolve them, or won’t dissolve them too fast.

Also, it probably works with soda-lime glass, although I’m not sure
what the backing plate needs to be.  The anti-adhesion layer in this
case might be aluminum foil, but probably a more effective approach is
to keep the surface of the glass cool, using forced air or water if
necessary.

You could probably use a rolling wheel to “cut” the plastic sheet
through the wrap, giving you a vinyl-cutting-plotter-like capability.
Certainly you can repeatedly push something like the end of a butter
knife or tongue depressor through it.  Making multiple trips along the
cutting contour at different heights should handle the cases where
this doesn’t work as well as you’d hope.  So this is an appealing
technique for sheet-cutting automated fabrication.

Also, you can push a thin rod into the material in many places, for
example a chopstick, to be able to cut arbitrary shapes without the
limits on sharp corners imposed by the wheel-cutter method.

You can use this approach with a rolling ball (like the spherical
casters sometimes seen on office chairs) to *form* the clay or other
plastic material instead of *cutting* it.  This requires good
simulation of the plastic deformation to plan the forming toolpath.
The wrap will reliably keep the plastic sheet or other plastic
workpiece from adhering to the forming tool.

Of course it also works with stamps pre-designed to form the surface
of the material rather than cutting all the way through like the
cookie cutters.  (Some cookie cutters have such stamps already
incorporated.)

For many sticky plastic materials, there exists some kind of powder
that can be dusted on the surface to prevent adhesion: talc,
cornstarch (suggested in the video, which claims it doesn’t prevent
sticking in this case), quartz flour, zirconia dust, whatever.  In
other cases a liquid coating will prevent sticking and may also serve
as a lubricant.  In some cases you would like this to be removed or
fuse with the workpiece after it has its shape, and with the
appropriate choice of powder this can be achieved by means such as
washing, raising the temperature further, solvent vapor smoothing, or
liquid solvent smoothing.

Instead of a film, powder, or nonplasticized part of the underlying
plastic slab, fibers may be a feasible alternative: woven, felted, or
especially knitted.  This is appealing because cloth can remain
flexible and resilient over a wider temperature range; even fairly
minor plastic or elastic deformations in the fiber material can permit
gross deformation of the cloth, protecting the “cutter” from adhesion
as it deeply penetrates the surface of the slab.  It can also provide
better thermal insulation than powders or films.  For example, knitted
fiber of silicon carbide or zirconia could permit pizza-cutter action
on glasses whose glass transition is at 1500° or more.

Other kinds of filled systems are appealing, too.  For example, filled
system consisting of 65 vol% stainless steel powder, 5% of a sintering
aid (such as borax, potassium bisulfate, boric acid, fluorspar,
sulfur, or brass), and 30% poly(lactic acid) or delrin would probably
become plastic at the usual temperatures for PLA (around 185°-230°) or
delrin, at which temperatures the sintering aids should be inactive.
Heating to a much higher temperature should activate the sintering aid
and bind the particles together, as well as burning off the organic
polymer; sufficient time at sintering temperature would result in a
porous sintered stainless steel body.  However, such a the
low-temperature plastic matrix will likely burn off long before the
sintering aids can activate, so you might need a small amount of a
fourth ingredient to add enough green strength by holding the
particles in place; candidates include soluble silicates, clays
(especially highly plastic clays like bentonites), carbohydrates such
as sugar, and organic thermosets.

Sulfur is a particularly interesting possible binder/matrix for such
filled systems because at one temperature it is very liquid, and then
at a higher temperature it polymerizes into a plastic form which can
be molded; if cooled quickly enough (traditionally by water
quenching), it then gradually hardens through further polymerization.
Moreover, it reacts with many possible metal fillers to form
low-melting sulfides, which can then be transmuted back to the
original metals by further heating to drive off the sulfur.

Water-soluble carbohydrates such as sugars, isomalt,
carboxymethylcellulose (a popular choice for pottery), or gelatinized
starch have the potential advantage that, like real clay, you can
plasticize them with a small amount of water so that they flow readily
at easily accessible temperatures (0°-100°), but upon being maintained
warm for a longer time in contact with air, they will lose water and
in some cases can be induced to crystallize by such dehydration.
(This is the principle behind making fruit leather, for example.)
Once their water content is low enough to avoid forming bubbles that
would disturb the form, they can be caramelized at somewhat higher
temperatures (150°-250°) to form a heat-stable green body that will
carbonize, and the carbon will survive for a substantial period of
time even at metal-sintering temperatures, before finally debinding
the sintered piece through oxidation.

Such carbon-containing binders/matrices or sintering aids may add
carbon to the final product, for example if the “filler” contains iron
or silicon.

What should you use as the backing sheet?  In the case of real clay or
similar preceramics which will be fired afterwards, one possibility is
to use sacrificial organic material or or sulfur, either of which
which will fully gasify during firing in an oxidizing atmosphere; this
will avoid distortion from the peeling process used in the video.
Sulfur or zinc will also simply boil away, even in a reducing
atmosphere, but the gases may cause problems for things other than the
workpiece, for example by forming metal sulfides.

In the case of molten thermoplastics, experience with RepRap-derived
3-D printers has shown that many thermoplastics will adhere nicely to
a sheet of warm glass, then delaminate from it without breaking due to
thermal contraction when allowed to cool.  This may work for soda-lime
glass on sheet steel too, I’m not sure.  Another popular option which
will also work here is to use an elastic flexible backplate made from
something like thin sheet steel; this can also be peeled off the
finished object once it is cool.

Another alternative may be backing sheets that can be destroyed, or
whose workpiece-contacting surface can be destroyed, by a reagent that
will spare the workpiece itself.  In semiconductor fabrication, for
example, hydrofluoric acid with a little nitric is routinely used to
remove exposed silicon dioxide without attacking the silicon,
aluminum, copper, and I think hafnia parts of the chip, while caustic
potash is routinely used to etch away silicon (along certain crystal
planes! and only if it doesn’t contain enough boron!) and aluminum
without affecting silicon dioxide or nitride; in jewelry, hot aqueous
alum solution is routinely used to dissolve broken steel taps from
workpieces made of other metals; and caustic soda will rapidly
dissolve aluminum and etch amorphous silica, and with sufficient heat
will dissolve crystalline silica, but leaves most metals untouched.

****

The air bubbles in the video suggest another fascinating possibility:
forming the surface of a sheet of material by injecting pressurized
gas or liquid between it and some kind of substrate, whether flexible
like the wrap or rigid like the glass.

And of course the overall process is not so far different from things
like hot-needle cutting of foam sheets, or hot-wire cutting.
