Watching [an Abom79 video][0] I saw an interesting way of fastening
parts together with friction: one part has a slot in it that’s too
small for the other part, but round holes on both sides of the slot.
By using a simple hand tool with two round pins that fit in the holes,
one of which is mounted on an eccentric with a handle on it, you can
exert a very large force to elastically bend the slot open, allowing
the other part (in this case, a ceramic cutting insert for a lathe
parting blade) to freely move in and out of the slot.

[0]: https://youtu.be/PbFLW0_HIAU

This is a fascinating idea to me.  Bolts and other screws also fasten
parts together with friction, but they add weight and tend to vibrate
free if they aren’t secured with lockwire.  (Loctite isn’t considered
adequate in aviation.)  Screws are inherently very three-dimensional,
while this bending-open-jaws approach can I think be arbitrarily close
to planar; you can fabricate it with 2-D cutting approaches.  And
screws take a long time to insert and remove, while this eccentric
approach is a quarter-turn of a handle, like a camlock.

Screws get a pretty good mechanical advantage, but eccentrics can in
theory have arbitrarily high mechanical advantage, because the
relevant output lever arm is at most the eccentric axis displacement
distance and diminishes toward zero like a toggle mechanism when the
eccentric approaches top dead center; additionally, you could drive
the eccentric rotation through a separate toggle mechanism if need be.

I’d previously seen the [MTM Snap][27] mill by Jonathan Ward and Nadya
Peek, which uses snaplock connectors milled out of HDPE instead of
screws, because Neal Gershenfeld loves snaplock connectors.  And
they’re sort of the same thing as the flexing-jaw connector in the
video, or anyway there’s a continuum between them.

[27]: http://mtm.cba.mit.edu/2011/2011_mtm-snap/mtm_snap-lock/index.html

Exploring the design possibilities, I think this is a potentially very
exciting mechanism offering many possibilities:

1. Snap-jaw joints potentially offer a repeatedly-assemblable
   alternative to screw fasteners with several advantages:

    1. It could be integrated into the parts to be assembled at the
       cost of a few cuts and holes, rather than being manufactured
       separately.
    2. It could require dramatically less effort, whether measured in
       maximum force, in energy, or in time, to assemble and
       disassemble than screws do.
	3. It is usually enormously more vibration-resistant than screws
       are.
	4. On one of the two parts being connected, it’s possible to make
       the connection anywhere in a continuous region, as with a screw
       slot, but without the reduction in holding force and part
       strength that a screw slot implies.
    5. The cost may be comparable, but is probably lower, by at least
       a factor of 2 or 3, in part because snap-jaw joints can easily
       be made with XY cutting processes.

2. You could build a reusable, very inexpensive, very rapid
   construction kit using high-strength snap-jaw fasteners, which
   would allow you to rapidly assemble and disassemble a variety of
   shapes.

A basic snap-jaw connection
---------------------------

Consider a mating pair of such parts, made of mild steel with 250 MPa
yield strength and a 200 GPa Young’s modulus, giving 0.125% yield
strain.  They’re made from 3 mm steel plate (23.7 kg/m²); the first is
2-D cut with a 20-mm-long slot in its edge that tapers from 2.5 mm
wide at the edge up to 3 mm at the base of the slot.  The second has a
corresponding backwards taper ground or rolled into its edge, so that
its edge is the full 3 mm thick, while 20 mm from the edge, it’s been
thinned down to 2.6 mm.  The slot must thus be elastically opened by
0.5 mm or more, 0.25 mm per jaw, to assemble the parts.  Then these
jaws can be clamped onto the edge anywhere along its length, not just
at predefined locations.

Although there is a stop at the base of the slot, it consists of a
tongue; the jaws do not join onto the main body of the second piece
for another 20 mm, so the total bend in each jaw is 0.25 mm over 40
mm.

The Von Mises yield criterion says the shear yield stress should be
about 0.58 of the tensile yield stress (3<sup>-½</sup>), or 145 MPa,
and the shear modulus G = ½E/(1 + nu), where nu is the Poisson ratio
(about 0.26 for mild steels) and E is Young’s modulus, which works out
to about 79 GPa, so the shear yield strain is about 0.18%.  0.18% of
40 mm is 0.07 mm, which is a lot less than 0.25 mm.  This means that
if the jaws are so thick and solid that they are deforming in shear
instead of flexure when we open them, we have lost the game; we need
them to deform almost entirely in flexure.  (I need to learn how to
calculate that.)

0.25 mm over 40 mm amounts to a radius of curvature of 3200 mm and a
diameter of curvature of 40²/0.25 = 6400 mm.

So suppose we make them 5 mm thick.  Assuming pure bending, the jaw’s
inner edge is 40/3200 radians of a circle of radius 3200+2.5 mm; its
outer edge is the same number of radians of a circle of radius
3200-2.5 mm.  This amounts to 0.031 mm of compressive or tensile
strain, 0.08% strain, which is comfortably less than the 0.125% yield
strain limit of the mild-steel material.

But how much force is this biting down on the other plate with if it
tries to pull out?  Well, that 0.08% strain gives us 160 MPa stress in
the material at the extremes, where it’s applying a 2.5 mm lever arm.
But as the strain diminishes toward the neutral axis of the beam, so
does the lever arm.  We need the integral from -1 to 1 of x² (which is
2/3), times 160 MPa, times (2.5 mm)², times the 3 mm thickness of the
material, and we get a torque of 2 N m, which is like 800 N applied at
a 2.5 mm lever arm.  Dividing this by 40 mm we get 50 N, which is a
pretty modest force.  You wouldn’t even need a special tool.

But that’s when it’s almost all the way pulled out; it increases from
20% of that (10 N) up to that value as the taper pulls the blades
apart, for an average bite force of 30 N.  The interesting thing,
though, is the size of the energy barrier: steel on steel has a
kinetic friction coefficient of about 0.6, so it’s an average of 18 N
of friction resisting the pull-out force (plus 30 N × 0.5 mm / 20 mm =
0.75 N).  But because that’s over 20 mm, the energy barrier is a very
significant 0.36 J.  If you don’t manage to pull it all the way out,
it will tend to move back into place when there is vibration.

Shape variations
----------------

A purely-2D-cuttable version is to use a sort of triangle-wave pattern
of teeth on the jaws of one plate and a series of slots in the other
plate to accommodate the crests of the triangles.

This conformation of the connector type is not very proof against
being twisted, without further support; if we turn it inside out so we
have two tapered prongs that stick through a slot against the inside
of which they are pressing, we obtain a much better purely-2D-cuttable
connector which resists more degrees of freedom.  The slot can be, for
example, 3.1 mm × 40 mm to locate the connector in all dimensions to a
reasonable degree of precision (and if it’s not perfectly rectangular,
thinning out to 3.0 mm at the edges, that will improve the precision];
or it could be 40 mm × 40 mm to permit positioning the connector
anywhere within it at either of two angles; or it could be longer, say
150 mm × 40 mm, to permit further positioning freedom.

To increase the force without vastly increasing the required
cantilevered jaw length, we can use rigid jaws mounted on many
parallel flexible thin strips (a section of metal with many parallel
cuts through it, perpendicular to the edge but not reaching it), which
bend into parallel S-curves to allow the jaw section to move.  Since
the strips would be bending twice, they’d need to be half as thick to
reach the same strain, so 2.5 mm, which also halves the torque (and
thus, I think, the force) applied by each one.  So to reach a 20 J
energy barrier for sliding out of place, we would need about 60
strips, occupying about 150 mm of lateral space and providing about
1500 N of peak bite force, for which you would definitely want a
special tool.  The energy for opening the jaws would be 0.75 J.

What people normally do in practice in such cases is to use a much
steeper slope than the 1:40 slope I’m talking about above, using
something closer to 1:1 or even 2:1 or 10:1, creating something more
like a hook than an inverted wedge, and a much larger displacement
than 0.5 mm.  This makes the snap connector self-locking (like a screw
or the most common kinds of worm drive) without requiring excessive
forces to open it, when the opening forces are applied directly to the
snap jaws rather than to the joint they secure.  Because rounding over
or breaking off the snap hook is an alternate means of failure,
typically only one side of the snap fastener moves.

(Providing multiple hook tips, like interlocking sawtooths, is another
possibility for reducing the failure risk from the snap hook.)

If the snap jaws are grabbing onto the edge of something or into a
slot, rather than poking through a hole or grabbing a small object,
having *two* connected sets of jaws in parallel planes positioned some
distance apart along the edge would strongly resist two axes of
twisting that a single edge-jaw connection is vulnerable to.  And if
you want an edge that can be reliably grasped with such an edge-jaw
connector, a 2-D-cutting way to get one is, rather than trying to roll
a reverse taper into the edge, to assemble something like one side of
an I-beam, where a narrow strip of material runs along the edge of a
plate of material, perhaps held there by snap connectors protruding
through it.  If the edge is perfectly straight and there are no jaws
clamped onto it, the strip can be twisted around its intersection
line, but if the strip is curved or there are jaws grabbing it, it
should be held firmly in place.

Compound mechanical advantage and smooth jaws
---------------------------------------------

An exciting thing about hook tips with steep slopes is that they
provide further mechanical advantage that’s available to press
multiple things together.  Suppose your hook tips have a 10:1 slope,
so 0.4 mm of bite-down movement is permitted by 0.04 mm of snugging
up, and you have 1500 N of bite-down force.  That multiplies whatever
part of the bite-down force isn’t stymied by static friction,
potentially all of it if you vibrate the joint enough, so you might be
able to get 15 kN of snugging force.  (But, with a 250 MPa yield
strength, you need 60 mm² of cross-sectional area in tension to
withstand 15 kN, so you’d probably want to make such a thing out of
6mm mild steel sheet instead of 3mm.)

An interesting thing about this is that the numbers for the forces
needed to fasten and unfasten, or the costs of fabrication, don’t
really depend at all on how wide the actual jaw is (and thus its
tensile strength), just the flexure that supports it.  This might seem
like a distinction without a difference, though: if the flexure breaks
under tension, what does it matter that the jaw didn’t?

But I think there is a very clever way around this.  The movable jaw
always has to work against some kind of fixed jaw (whether pressing
toward it or pulling away), and the fixed jaw is rigid and not
supported on the flexure.  Therefore, why not put the hook on the
fixed jaw, which can be arbitrarily robust, and make the movable jaw
totally smooth so it isn’t subject to tensile forces?  This is
backwards from the usual snap-connector design, but I think it has a
really killer advantage in terms of strength.

In the case where we’re joining the edge of one plate to the face of
another, we can’t do the sawtooth thing to prevent the hook from
rounding over or breaking off.  Instead, we can use *multiple rigid
hooks* that poke through multiple slots in the mating plate, all
preloaded with the same flexure-mounted smooth movable jaw.

There are some disadvantages to the hooked-fixed-jaw approach.  It
means that the parts being joined have some play in the join,
depending on exactly how far down the hook ramp the flexure has
managed to force the mating parts, so they aren’t precisely locate
relative to one another.  And an impact could apply the mass of either
of the two parts to the purpose of disconnecting the smooth movable
jaw.  I think these can be mostly eliminated by using a chain of
wedges, like those in a tusk-tenon joint, those used to assemble
reusable concrete forms, or those in a cotter pin, with only the last
“keystone” wedge in the chain using a compliant snap joint to wedge
the whole chain tighter and tighter when there’s vibration.  The small
masses of the keystone wedge and its immediate wedgee prevent impacts
from breaching the energy barrier to disassembly.

Being able to make each connection extremely strong means that you can
use fewer of them, which lowers both costs and time for assembly and
disassembly.

Of course, if you *were* to apply 1500 N, you need a fastening and
unfastening tool.

Design of a 91%-efficient snap-jaw-loading tool
-----------------------------------------------

At 0.5 mm displacement, a simple eccentric lever tool like the one in
the Abom79 video would have an 0.25 mm eccentric offset and thus
maximum lever arm.  A comfortable handle length of 250 mm would thus
have a M.A. at worst of 1000:1, halfway through the movement, when the
bite force is only 750 N, and the handle force thus 0.75 N plus
friction.  The peak handle force is just a little past that, and then
the M.A. starts to increase togglewise.  With a force budget of 10 N,
you’d only need a peak M.A. of 75:1, and thus a handle length of 19
mm.  (A pullstring might still be a better way to apply the force,
though.)

With the snap-fit fastener, though, there’s almost no friction inside
the workpiece, just elastic hysteresis, which is insignificant for
most common materials at these speeds.  The friction is all inside the
tool used to force the snap open, where it’s practical to reduce it
with material choice and rolling-element bearings, instead of within
the part as with a screw.  Consider these scenarios:

1. The force is applied to a movable snap jaw by inserting a round
   steel pin from the tool into a dry round steel hole in the snap
   jaw, and the pin rotates as an integral part of the eccentric as
   the handle is turned, thus rubbing against the jaw hole while the
   normal force increases from 300 N to 1500 N.  Suppose the pin is 3
   mm in diameter; then in a half turn it moves 4.7 mm with an average
   of 900 N normal force, which with a friction coefficient of 0.7,
   gives us 630 N of average friction force, consuming an extra 2.96 J
   every time you opened *or closed* the jaws, in addition to the 0.75
   J that gets elastically stored.  This is most similar to the
   situation with ordinary screws.
2. Same, but now the pin is bronze or zinc, so the coefficient is
   reduced to 0.22, and instead of 2.96 J it’s 0.93 J.  A big
   improvement already, and one you can’t get with screws unless you
   either put bronze sleeves in all your screw holes or make all your
   screws out of bronze.
3. Same, but now the pin has a teflon sleeve.  This drops your
   coefficient of friction to [about 0.04 to 0.10][4], but teflon has
   a [compressive strength of only around 10-15 MPa][3] so
   withstanding 1500 N requires a 150 mm² contact area, so now you
   might need to make the “pin” and its hole 50 mm wide to not wear
   out, which would make this less efficient instead of more, not to
   mention less convenient.
4. Same, but now instead of rotating as an integral part of the
   eccentric, the pin runs through a pair of ball bearings pressed
   into the eccentric, giving an effective frictional coefficient
   around [0.0008][22] to [0.0015][1].  At this point, though, we need
   to worry about the bearings on which the eccentric shaft as a whole
   rotates, because they become a more significant source of friction;
   suppose the pin is on 608 roller-skate bearings with an 8mm bore
   and 22mm outer diameter.  Then the eccentric needs to be at least
   22.5 mm in diameter and probably more like 24mm, so at the business
   end its 24-mm-bore bearing is resisting that same 750 N average
   force with the same 0.0015 effective frictional coefficient, but
   over 38 mm of rotation instead of 4.7 mm.  So that bearing consumes
   50 mJ, while the pin’s 608 bearing consumes 17 mJ, for a total of
   about 67 mJ.  [SKF rates their 608 deep-groove bearings for 3450 N
   dynamic, 1370 N static][2], so this is sort of marginal, but that’s
   for a million revolutions before fatigue.
5. Same, but now the eccentric isn’t a constant diameter, but has a
   sort of dogbone shape; its two ends are 25 mm in diameter with an
   eccentric 22mm bored out of them (0.25 mm off center) to press the
   3 mm pin’s bearings into, but those two ends are connected by an
   8-mm OD pipe which is itself pressed into two more 608 bearings.
   The 3mm pin runs through the ID of the pipe, which is, say, 4mm.
   Now the eccentric’s bearing also consumes only 17 mJ for a total of
   34 mJ, and as a bonus, the bearings cost 50¢ each instead of 600¢
   each, like a 24-mm-bore 6802 would.

[1]: https://www.smbbearings.com/technical/bearing-frictional-torque.html
[2]: https://www.skf.com/ph/products/rolling-bearings/ball-bearings/deep-groove-ball-bearings/productid-608
[3]: https://www.bearingworks.com/uploaded-assets/pdfs/retainers/ptfe-datasheet.pdf
[4]: https://wisconsindot.gov/documents2/research/WisDOT-WHRP-project-0092-08-13-final-report.pdf
[22]: https://koyo.jtekt.co.jp/en/support/bearing-knowledge/8-4000.html

These 34 mJ are 4.5% of the 750 mJ needed to activate the mechanism,
but we pay them twice: once to load the snap jaw, once to unload it.
So it’s only 91% efficient.

Consider the mechanical advantage of the screw.  A coarse M6 screw has
1mm thread pitch and might be driven by a screwdriver with a
25mm-diameter handle, so each 79 mm of screwdriver motion produces 1
mm of axial screw motion.  This is a 79:1 mechanical advantage.  To
get 15 kN of snugging force you would need to apply 200 N of force at
the surface of the screwdriver; you might need a T-handled screwdriver
or something.  But with an appropriate safety factor [an M6 screw can
handle a snugging load of only about 2090 N][5] in strength class
12.9, because its effective cross-sectional area is only 20.1 mm².  To
handle 15 kN you would need a larger screw --- the 60 mm²
cross-sectional area I suggested above would be a little bigger than
an M10, but Misumi recommends a safety factor of 3-15 depending on the
situation, and so a at least an M24.  And these larger screws have
coarser thread pitch, further decreasing the mechanical advantage.

[5]: https://de.misumi-ec.com/pdf/press/us_12e_pr1271.pdf

How inexpensive?
----------------

[McHone][6] says laser cutting steel costs US$13-$20 per hour, and 70”
per minute is a common cutting speed, which works out to 12¢-19¢ per
meter of cut, but [sometimes as slow as 20” per minute][7], which
would bring the cost to 66¢ per meter.  (Also they suggest 0.005”
precision, which is 127 microns in modern units.)  [AST Manufacturing
says plasma is 0.020” precision (500 microns)][8] on materials thicker
than 1”, but laser can hit 0.003” (76 microns) and up to 1575 (!)
inches per minute.

[OSHCut says the nominal 1200-ipm speeds for the laser they bought are
misleading][9] because *acceleration* is the limiting factor, not
cutting speed.  So curvy contours, angles, traversing between
contours, and especially piercing are slower than cutting the contours
themselves, but also they say that on their 3kW Trumpf 1030 fiber
laser ¾”-thick steel (19mm) cuts at a maximum of 47 inches per minute
(20 mm/s), while 0.04”-thick steel (1mm) cuts nominally at 1160 inches
per minute (490 mm/s).  They measure curviness in radians per inch,
and their plot seems to show that at 5 radians per inch (200
radians/m) the 1160 drops by a factor of 8, I guess to about 150
inches/minute (61 mm/s).  Even at 1 radian/inch (39 radians/m) it was
down to ¼ of max (I guess 290 inches/minute, 120 mm/s).  Still higher
curvatures added less penalty; even at 30 radians/in. (1200 radians/m)
the penalty for 1-mm steel was only about 17×, so I guess 68 in/min or
29 mm/s.  For thicker metal the curviness penalty was less, basically
no measurable penalty for the 19-mm stuff.  Their plot isn’t super
well labeled but one of the thicknesses is supposed to cut at 335 ipm
(141 mm/s) and I’m guessing that might be 3mm; at 5 radians/in. (200
radians/m) it was only 2× as slow (70 mm/s?) and even at 30
radians/in. (1200 radians/m) the penalty was only 4× (35 mm/s?).

[6]: https://blog.mchoneind.com/blog/how-much-does-laser-cutting-steel-cost
[7]: https://blog.mchoneind.com/blog/cost-laser-vs-waterjet-cutting
[8]: https://astmanufacturing.com/cutting-processes-compared/
[9]: https://www.oshcut.com/post/laser-cutting-speeds

Another way to look at these curvature numbers is as the
characteristic feature size, although especially good CAM software can
avoid this sometimes for some designs; a closed convex polygon of any
shape is 2 pi radians, so a curvature of 200 radians/m means that your
closed polygons are about 31.4 mm in perimeter, while 39 radians/m
means they’re about 160 mm in perimeter, and 1200 radians/m means
they’re 5.2 millimeters in perimeter, which is pretty impressive if
your kerf is close to the typical 0.2 mm.  Except that it doesn’t
include pierce times, so maybe they weren’t really cutting 6 polygons
per second, maybe more like 24 radius-0.8-mm 90° corners per second.

[Higher-powered 12-kW lasers can cut 12mm steel at 150 ipm, 64
mm/s][10], but even for straight cuts, laser cutters from 6 kW to 12
kW on 0.5-mm steel all topped out at 3150 ipm (1.3 m/s).  [JMT has a
cutting speed chart][11] cutting 1-mm steel with 4kW from 280 to 2362
ipm (120-1000 mm/s) and 3-mm steel at 120-380 ipm.  Interestingly they
needed to use either O2 or N2 gas for such thick steel; air was
insufficient.  Air could cut thin steel faster, and nitrogen faster
still, but oxygen was needed for steel over 6.4 mm.

[10]: https://info.paramountmachinery.ca/blog/how-fiber-laser-power-impacts-cut-speeds
[11]: http://jmtusa.com/laser-comparison-cutting-speed-and-rate-of-feed/

[Plasma is cheaper and faster than laser][12] as of 02018 anyway.
This article also gives me the term “XY cutting processes” to cover
plasma, laser, and waterjet, and mentions the acceleration limitation.
[Laser vendor Trumpf disagrees, saying plasma is more expensive per
hour][20], while laser is only US$3/hour in operating costs, and also
cuts faster (114 ipm (48 mm/s) in ¼” (6.4mm) mild steel rather than
“typical plasma”’s 70 ipm, which commenters say is much slower than
typical).

[12]: https://www.engineering.com/story/an-engineers-guide-to-laser-cutting
[20]: https://www.fabricatingandmetalworking.com/2017/09/the-king-of-cutting-sheet-metal-up-to-one-inch-thick/

[A company in Monte Castro called ZYX Mecanizados][18] (4674-6826,
zyxmec...@gmail.com) is one possible vendor of the service; they offer
plasma, CNC router, laser, and hot-knife cutting, for up to 1000 ×
1300 mm.  Their [website is down but dates from 02014][22] and it says
they cut [lots of things but not ferrous metals][24].  There seem to
be [some other vaguely relevant companies listed in its category on
MercadoLibre][19], but that is probably not really true.  Near here
Google Maps lists [Plasmacenter][21] (Perón 1898, Lomas de Zamora,
4282-3855 or maybe now 6233-5443), but they just sell CNC plasma, oxy,
and laser machines.  And in Palermo there’s [S.A.D.I. Metales][23],
whose web site says they do CNC plasma (1.6 mm to 12.7 mm) and
oxy-fuel (4.7 mm to 300 mm) cutting, but who said they just do laser
last time I asked.  They sell sheet metal from 1 mm to 6.4 mm in
thickness.

[18]: https://servicio.mercadolibre.com.ar/MLA-927216734-servicio-corte-router-cnc-pantografomecanizado-mdf-otros-_JM
[19]: https://servicios.mercadolibre.com.ar/imprenta/impresiones-laser/
[21]: https://plasmacenter.com.ar/index.php/servicios/
[22]: http://web.archive.org/web/20190812011332/http://www.zyxmecanizados.com.ar/
[23]: https://www.sadimetal.com.ar/index.php
[24]: http://web.archive.org/web/20190803100231/http://www.zyxmecanizados.com.ar/materiales

[Sheet steel is sold here as construction material][16] in a weird mix
of medieval and modern units: [1500 mm × 3000 mm × 3.2 mm (0.125”) for
AR$28650][13], which at today’s rate of AR$163/US$ is US$176, or
US$39/m²; [1220 mm (4 feet) × 2440 mm (8 feet) × 1.25 mm (18-gauge),
20 kg, for AR$9100][14], US$56, US$19/m², but it also can’t possibly
be those dimensions or it would be 29 kg; [1 m × 2 m × 1.25 mm
(18-gauge), 20.5 kg, SAE 1010, for AR$7458][15], US$46, US$23/m²,
which ought to be 19.75 kg, which is close enough; [1.22 m × 2.44 nm ×
2.0 mm (14-gauge) for AR$15043, 49 kg, SAE 1010 from Hierros
Torrent][17], US$92, US$31/m².  These are all in the range
US$1.43-US$2.80/kg, with the thinnest gauges costing nearly as much
per square meter and thus far more per kg.

[13]: https://articulo.mercadolibre.com.ar/MLA-924439735-chapa-lisa-de-18-lac-1500-x-3000-32mm-1500x3000--_JM
[14]: https://articulo.mercadolibre.com.ar/MLA-906262811-chapa-lisa-n18-de-122x244-mts-125mm-laf-_JM
[15]: https://articulo.mercadolibre.com.ar/MLA-828878948-chapa-lisa-laf-n-18-125-mm-de-100-x-200-mts-_JM
[16]: https://listado.mercadolibre.com.ar/materiales-construccion-obra-chapas/lisa/material-acero/
[17]: https://articulo.mercadolibre.com.ar/MLA-796327344-chapa-lisa-lac-n-14-200-mm-de-122-x-244-mts-_JM

So, to get a cost estimate, let’s try scaling down the hook thing a
little.  Say we’re satisfied with the 2kN snugging load a
strength-class-12.9 M6 screw can handle, and we get a 10:1 M.A. from
the angle of the hook (so we only need 200 N of bite), and 500 microns
*is* enough.  And to get 200 N over 500 microns, let’s say my
calculations above are okay and each additional 2.5-mm-wide 40-mm-long
strip in 3-mm mild steel would give you 25 N of bite, so you need 8 of
them; a 20-mm-wide strip cut lengthwise into 8 straight 40-mm strips
with 7-9 cuts (although where do we pierce?).  And let’s say the
US$15/hour number is about right, and 70 mm/s (one of what I think are
OSHCut’s numbers) is about right for these cuts.  That works out to 6¢
per meter of cut, or 1.9¢ to cut the springs for each such snap
connector.  The connector itself might occupy more like 1000 mm²
(0.001 m²), so the steel thus used costs about 3.9¢, but it can also
be serving other roles as structural support.

(At 200 N we don’t need a special tool with eccentrics and bearings
and stuff.  We can comfortably use snap-ring pliers with an M.A. of
3:1.)

A [box of 50 15mm M6 screws costs AR$540][25] or US$3.31, or 6.6¢ per
screw, but those aren’t strength class 12.9 or actually any declared
strength class.  A [box of 25 20 mm class-12.9 M6 screws costs
AR$656][26], 8¢ per screw.  Drilling and tapping the holes for a screw
costs extra, probably a comparable amount.

[25]: https://articulo.mercadolibre.com.ar/MLA-767623283-tornillos-fresada-philips-m6-x-15mm-caja-x-50-unidades-_JM
[26]: https://articulo.mercadolibre.com.ar/MLA-883120009-tornillo-allen-boton-m6-x-20-pack-x-25-unidades-calidad-129-_JM
