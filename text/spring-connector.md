[Watched an Abom79 video I’d seen before][2] tonight which featured a
parting blade with replaceable inserts.  A parting blade doesn’t have
a lot of space for holding down an insert; you can’t put a big screw
in there, for example.  So the insert was wedged into a sort of
two-tine fork, which flexes elastically to admit it.

[2]: https://youtu.be/PbFLW0_HIAU

The parting-blade setup
-----------------------

This means the force clamping the insert into the blade, perpendicular
to the friction surface, is the same force you need to apply to force
the tines apart to insert or remove the insert.  To supply this force,
there are round holes in the two tines, and an opening tool is
supplied, consisting of a spacer between two parallel dowel pins that
fit into the holes.  One of the dowel pins is machined on an eccentric
with a handle to rotate it relative to the spacer, moving it nearer to
and farther from the other dowel pin, thus forcing the tines open.
It’s sort of similar to circlip pliers in how it engages with the
fork, and in the fact that it consists of three revolute joints on
parallel axes (one between the two links of the tool, the other two
connecting the tool to the workpiece), but it has much greater
mechanical advantage.

Why this is awesome
-------------------

This is a really appealing concept for a couple of reasons.

First, if we disregard friction and the compliance of the tool, the
mechanical advantage is unlimited; the ratio between the length of the
handle and the center-to-center distance of the eccentric provides the
mechanical advantage, and the center-to-center distance (eccentric
axis offset distance) can be any value down to zero.  With an ordinary
lever, to get a very short lever arm, you also have to make the lever
arm thin, which limits the load it can take; no such limit exists with
this eccentric lever, because the eccentric pin can be as large as it
needs to be to resist the shear load (and, in the case where the hole
is deep, bending loads).

Friction is still an issue: the surface of the dowel pin rotating half
a turn in the hole creates a frictional moment opposing the action of
the tool, whose lever arm is the radius of the pin, which must grow
according to the square root of the fork-opening force in order for
the pin not to shear off.  So you have an opposing moment of
*F*<sup>3/2</sup>, which in the usual case will be about as big as the
work you’re actually doing, since the radius of the pin is typically a
bit larger than the eccentric axis offset distance, and the
coefficient of friction is typically a few times smaller than 1.
Friction inside the tool may or may not be reduced with ball bearings
or similar, but if not, it’s an additional comparable loss.  Such
losses may be desirable in this context to prevent back-drivability,
but they limit its applicability.

Second, when the fork opens and closes, assuming parallel planar
clamping surfaces, it doesn’t have any tendency to screw with the
position of the insert it’s clamping down on, except in the direction
of clamping and the two directions of rotation whose axes aren’t
parallel to the direction of clamping.  So it restrains the insert in
six degrees of freedom, but purely with friction in three of those
degrees, permitting any position in those three degrees.  This is a
nice improvement over things like jam nuts, which have a tendency to
put slightly askew the position you were intending to hold steady.

Third, the mechanical advantage becomes infinite as the eccentric
rotates to the position where the dowel pins are farthest apart, in
the usual toggle-mechanism way, because the lever arm becomes zero.

We can ask, what is the maximum clamping force we can apply with this
mechanism?  There’s no inherent limit coming from the applied force
(we can make the lever you rotate arbitrarily long, so given a fixed
point, you can move the Earth with an arbitrarily small force) but
there might be a limit coming from the energy, once friction is taken
into account.

Also, the compliance of the thing you are clamping may itself provide
a minimal energy cost: if under 10kN it elastically compresses 0.1 mm,
you need to open the jaws by more than 0.1 mm in order to insert it in
its uncompressed state, applying something more than 10kN in the
process, probably only a little bit more if the spring clamp (which
you are expanding) is more compliant than the thing being clamped.  So
that would require about a joule, plus frictional losses.

(Many cheap digital fabrication processes have imprecision on the
order of 0.1 mm: laser-cutting MDF, laser-cutting acrylic,
laser-cutting steel, CNC plasma tables, CNC oxy cutting tables, RepRap
FDM, etc.  You need to be able to flex the spring by more than the
fabrication error or in some cases you’ll get no clamping and in other
cases you won’t be able to insert the thing to be clamped.)

The compliance of the elastic part of the setup (the workpiece, in
this case the clamp) can be reduced almost arbitrarily, as long as the
compliance of the tool is smaller or at least not too much greater.
Given a nominal Young’s modulus of 200 GPa for steel, and considering
a 10 mm distance between the points where force is being applied, we
can get a compliance of 5 microns per newton stretching a
100-micron-square steel wire, or 50 nm/N stretching (or compressing) a
1-mm-square steel rod, or 500 pm/N stretching (or compressing)
something that averages out to a 10 mm block of steel.  At this last
compliance, 10kN would result in a 5 micron elongation, which is still
plenty to switch between contact and non-contact regimes for things
like electrical conductivity and so might be enough to clamp and
unclamp something.  As with brakes and clutches, the smaller the
compliance, the smaller the energy that is needed to reach a given
clamping force and thus a given stiction force.  In this example,
reaching 10kN of clamping force would only require 50 mJ plus
frictional losses.

(Of course in the geometry described earlier the tension path between
the prongs was not straight, increasing compliance, but there are
rivet-like clamping geometries where the tension path *is* straight.)

Larger compliance may be desirable for resistance to shock loads: if
the energy barrier to unclamping is 100 joules, shocks are much less
likely to result in slippage than if it is 0.05 joules.

In cases where the elastic piece doesn’t have to be planar, the tool
can be simplified to a single rigid body consisting of a handle
perpendicular to a shaft consisting of two cylindrical sections with
parallel axes.  The shaft is inserted through a slot in the elastic
piece into a round hole in another part of the elastic piece, and
rotating the shaft with the handle then moves the round hole
perpendicular to the length of the slot and to the shaft’s axis of
rotation.  This could reasonably be used for things like fasteners,
though in the case of one tool to operate many fasteners, it might be
cheaper to make the fasteners as simple as possible (like circlips)
and put any extra complexity in the tool.

To reduce frictional losses, the actual holes can be mounted in
rotating flexures, or the eccentric pin in the tool can be held in a
pair of bearings to reduce friction.  These bearings are mounted
eccentrically inside a larger shaft mounted on its own bearings which
is rotated by the handle.  It’s possible but maybe not practical to
avoid the use of large bearings in this case: the larger shaft can
neck down to fit into two small bearings at the non-workpiece end,
which are spaced far enough apart to handle the resulting moment.

Another way to reduce frictional losses is to provide some leverage
within the flexing workpiece itself.  In the case of a fork, you might
clamp the workpiece half as far from the bifurcation as the distance
from the bifurcation to the holes for the tool.  Then the tool only
has to apply half as much force as is applied to the thing being
clamped, and the tool rotation experiences about half as much
friction.

How big *are* those frictional losses?
--------------------------------------

Suppose that we are applying, again, 10kN of force with the tool, over
a whole half turn, using a handle which cannot be more than 1 m long
(the example in the video was about 150 mm long) and to which we can
only apply 200 N of force.  Perhaps the eccentric pin is made of a
bearing bronze such as [SAE 660 tin bronze][0].  Its yield tensile
strength is given as 125 MPa; its shear strength might be 0.6 of that,
75 MPa.  To fail under 10kN of load, then, it needs to be 13 mm in
diameter, giving a cross-sectional area of 132 mm<sup>2</sup>; 20 mm
diameter would give a good safety factor.  The eccentric axis distance
could be as large as 20 mm, or actually even greater since when the
lever arm is at its largest, the clip isn’t fully extended yet, so the
force is not at its largest.  If it’s 20 mm, we can use it to deform
the clip by 40 mm, for a total useful work of 200 J.

[0]: http://www.matweb.com/search/datasheet.aspx?matguid=b673f55f412f40ae9ee03e9986747016 "High-Leaded Tin Bronze, UNS C93200, Copper Casting Alloy, Bearing Bronze SAE 660,  ASTM B584; formerly ASTM B144-3B, 6.3-7.5% tin, 2.0-4.0% zinc, 6.0-8.0% lead, remainder copper"

That bronze is rated as having a frictional coefficient of 0.10,
presumably on steel (though [in 02001 Purcek et al. measured 0.68 when
dry][1], so maybe 0.10 is with an oil film), so the pin rotating in
the workpiece hole ramps up to 1 kN of friction.  Half a turn is
62 mm, so we have 31 J of frictional losses rotating in the workpiece,
and probably another 31 J of frictional losses where the shaft rotates
inside the tool, for a total of 62 J losses, 76% efficiency.  Ball
bearings or similar could reduce these losses by about an order of
magnitude, so they are more like 2% instead of 24%.

[1]: https://www.researchgate.net/publication/222064578_Dry_sliding_friction_and_wear_properties_of_zinc-based_alloys

Note that this means you have to apply more force to the handle than
the 200 N I was calculating with.  More like 262 N.  Except that the
force is going up as the lever arm goes down; at 45 degrees you have
70.7% of the force, 7 kN, and also 70.7% of the lever arm, 14 mm, so
only half that 200 N, 100 N, plus 70.7% of the frictional force,
another 44 N at the handle, for a total of 144 N.  A little lower, at
30 degrees, you have half the force, 5 kN, and 87% of the lever arm,
so 43% of the 200 N plus 50% of the frictional force.  I should plot
this I guess.

This bronze is also rated as having 315 MPa compressive strength, so
the hole in which that pin is turning would need to be at least 1.6 mm
deep to avoid damaging the surface, maybe more like 3 mm deep.

This is a fairly terrifying tool configuration, though, sort of like
garage-door-spring winding but at lower energy and much higher force.
If you lose your grip on the handle, it is going to acquire 138 J of
kinetic energy.

Suppose we are stretching a less compliant workpiece, so we only need
to deform it 4 mm.  If we use the same tool, we get about the same
efficiency (a little better, actually, since much of the frictional
loss is in parts of the circle that do very little real work) but we
could alternatively redesign the tool to have an eccentric axis offset
of only, say, 2 mm.  This would reduce the moment from the workpiece
from 200 N m to only 20 N m, but we still have 20 N m of frictional
loads because the pin is still 20 mm in diameter.  This enables us to
reduce the handle length to 200 mm, to which we apply the same 200 N,
but now at only 50% efficiency.  This tool is no longer backdrivable
by the workpiece’s elasticity, since the moment from the workpiece is
equal to the moment from friction.  (Even the larger configuration
wasn’t backdrivable when fully toggled, because the frictional forces
are at maximum and the lever arm is zero.)

We could maybe reduce the frictional losses further by using a mostly
hardened steel pin with just a surface of bronze on it, enabling us to
reduce the pin diameter by a factor of 2 or more without losing shear
strength.  Tool steels normally have (tensile yield) strengths of 1
GPa or higher.

In the case where we start almost “toggled” — in the sense that the
eccentric pin is nearly at its furthest distance from the other pin
when you insert the tool into the holes — the mechanical advantage is
very much greater, being limited only by the compliance of the tool.

Variations
----------

A couple of slight variations on the tool configuration are worth
mentioning.  Shear and flexural loading on the pins can be eliminated
if they are only *half* cylinders, with the pivoting bushing inside of
the eccentric pin, which can be longer than the workpiece; this makes
the loading on the pins entirely compressive, but requires the “holes”
in the workpiece to be two circular notches facing each other, between
which the tool is inserted.  This permits a much smaller hole radius
and thus dramatically reduces frictional moments and thus losses.  In
this configuration it is advisable for the handle to be roughly
perpendicular to the line between the two notches in the workpiece,
and to collide with the other pin when rotated just past the toggled
position in order to lock the pins *ε* less than their furthest
distance apart.

Such a tool can be cut out of a thick sheet in a single piece with 2-D
cutting processes; it consists of two quasi-rigid parts (the handle
and eccentric pin being one part, the other being either the Minkowski
sum of a circle and a line, or a rhombus with rounded corners) which
meet in a cylindrical sliding contact, held in roughly the right
position during insertion by a compliant spring that runs along the
handle, but which exerts forces that are insignificant compared to the
forces encountered during use.

The sheet needs to be thick to prevent it from twisting out of plane.

This pivoting bushing can be split in two to allow the workpiece (or
what it is clamping) to protrude past the notches, reintroducing half
the shear loading but not the flexural load.

If such a tool is used to push apart jaws on one side of a flexural
pivot, those jaws can pivot to come closer together on the other side,
with potentially some additional mechanical advantage; when the tool
is removed, they will spring back apart, at which point they can bear
on the inside of one or more holes, forming a fastener.  (However, you
need some way to hold the fastener in place as you’re applying the
tool, or it will just rotate along with the tool instead of flexing;
see below.)  Such a fastener can also be fabricated by 2-D cutting, in
which case the hole or holes can be just a slot.  If the hole is
tapered to widen away from the surface, withdrawing the fastener from
the hole will require adding energy to the flexural pivot, so
vibration will tend to seat the fastener deeper in the hole, similar
to flexural clips and very much contrary to the situation with screw
fasteners.

A fastener containing a double flexural pivot can be used in the same
way to convert the opening of jaws, on the side where the tool is
inserted, into compression in the middle of the piece, into the
opening of another set of jaws on the opposite side, with potentially
another layer of mechanical advantage, permitting clamping with truly
enormous forces.

(And, of course, the full range of clip-connector techniques is
available for these jaws: they can be smooth, serrated, or hooked,
potentially mating with matching features on the part they grasp.)

These pivoting-flexure connectors allow the same tool to be used for a
variety of sizes of fastener, because the jaw spacing on the tool side
of the fastener need not be the same as the jaw spacing on the
clamping or expanding side.

In cases where both locating and friction are desired, because the
fastener does not have to rotate, it can have a second tab that slips
into a second hole or slot in the workpieces to locate them relative
to one another, thus unifying in a single part functions similar to
those of a screw and a dowel pin.  If this second tab is longer than
the flexural parts, it can be inserted before applying force to the
tool, thus holding the fastener in place while force is being applied.

If the eccentric pin on the tool is replaced by a concave partial
cylindrical bearing surface, in which a convex cylindrical part of the
flexible workpiece can slide to form a revolute joint (or, really, a
cylindrical joint) then the tool can be used to compress the workpiece
rather than to expand it.  The effective lever arm is still the
distance between the center of this cylindrical surface and that of
the cylindrical bearing surface on which the other part of the tool
pivots.

If the fastener includes a parallel-movement flexure, a single tool
action can engage many hooks, inserted into many slots, in a single
motion.  This is probably not useful for clamping as such (the
clamping load would be distributed among the slots, and in an
unpredictable way unless the fabrication tolerances are much smaller
than the parts’ compliance), but with hook fasteners it allows you to
“stitch” two or more parts together along a whole line in a single
action.  Such a long fastener allows you the leverage to prevent the
fastener from rotating along with the tool just by holding it in your
other hand.

Contrast with bolts
-------------------

You need to rotate the bolt through the nut through some 6 turns
against the thread friction, which ought to be negligible but usually
is on the order of a tenth of the tightening load.  Then you crank
down on the bolt to preload it in tension; for a 10-mm-head bolt that
torque might be 25 foot-pounds or 30 newton meters, applied over maybe
a third of a turn, or about 30 J (would be 60 J but the torque goes up
almost linearly as you snug it up).  Maybe ⅓ of that energy goes into
the elastic clamping energy, 10 J; the other ⅔ is lost in friction,
20 J, on top of the ≈3 N m times six turns you lost in just getting
the bolt into the nut, which is another 110 J.  So you had to spend
140 J and six turns of the wrench to get 10 J of elastic clamping
energy, which might be the same 10 kN we were calculating with above.
Six turns of the wrench is a real PITA in a confined space, because
you have to slip the wrench on and off of the head between 12 times
and 72 times.

And then only stiction stabilizes the connection; enough vibration
will loosen it unless you apply loctite or lockwire or something.  And
manufacturing the threads requires a lathe, taps and dies, or a
thread-rolling machine, rather than a simple digital 2-D cutting
setup.