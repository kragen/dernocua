Milling machines need a lot of rigidity to avoid not only imprecision
but even oscillation, or even grabbing in the case of climb milling,
under the heavy side forces created by their cutters.  Their
workholding setups also must withstand these side forces.

The cutters are most commonly end mills doing side cutting.  It occurs
to me that, when doing a straight cut while side cutting, if you have
two counter-rotating end mills close to one another, so that one is
climb-milling while the other is conventional-milling, then only the
spacing between the cutters needs to be rigid to resist the cutting
forces, because the forward force by one cutter can be balanced
against the reverse force by the other cutter.  By adjusting the two
cutters’ engagement depths and spindle speeds, you can use a
controlled imbalance in these side loads to feed the machine through
the material, eliminating the need for a high-power feed motor driving
the X and/or Y axis; the feed motor only needs to oppose the side
loads *perpendicular* to the toolpath, which will be only partly
canceled by this setup but do not require any power, just holding.

The two spindles might be mounted a fixed distance apart on a small
turntable rotating around a C axis, for example.

Of course you need active feedback to monitor the resulting positions
and feedrates and adjust the angles and spindle speeds between the two
cutters to compensate.

Doing this for more complex surfaces might require rotating the
carrier for the two cutters around two axes, not just one.  If the
cutters are not ball-nose endmills, it might then be necessary to
rotate the spindles back to verticality.

In face milling, it should be possible to do something similar most of
the time while cutting almost twice the width of a single face-milling
cutter in a single pass, by overlapping the paths of the cutters
slightly, while overlapping the path of the leading cutter with a
corresponding amount that was cut in the previous pass. That same
overlap will create an imbalance between forward and backward forces
which can enable the cutting forces to feed the cutter into the
material.

To do the same kind of thing for single-point cutting on a lathe, you
could use two cutters on opposite sides of the workpiece, perhaps with
a negative rake angle on them so that if one strays a bit closer to
the center of the material than the other, the cutting force will push
it back out, so that the cut is the same depth on both sides.  Using
three cutting points instead of two eliminates an undesired degree of
freedom in movement.

This is pretty much the same way that dies, taps, and countersinks
center themselves on existing round features, and drills follow
existing holes, so it could lead to cutting non-concentric features.
If the cutters’ rake angle can be varied dynamically during each
revolution, you could use position feedback to cut deeper on the high
side and thus recenter the cutting; a system of levers referenced to
the desired cutting axis can achieve this.  The same approach can be
used in place of a boring bar: a sort of hole-expanding drill or
boring head that self-centers on the desired cutting axis by changing
the rake angles of its cutting points.

These drilling-like approaches surely eliminate most of the usual side
forces and workholding forces: if you’re cutting a vertical cylinder,
inside or outside, then all the horizontal cutting forces cancel
between the three cutting teeth.  It’s like a drill press: you still
need potentially a vertical force to feed into the stock (and to hold
the stock in place as you do that), which maybe you can avoid by
tilting the teeth forward or back to pull it into the stock at an
appropriate speed.

But the bigger remaining issue is that the *moment* from rotating the
teeth relative to the workpiece is still present; this is what
potentially causes a poorly held workpiece in a drill press to spin
around on the drillbit and break your hand.  If you’re cutting on a
large radius, this moment is potentially very large, and it needs to
be resisted (probably quite rigidly) across the whole
workpiece-workholding-frame-spindle chain.  If instead of using three
rotating *teeth* you use four rotating *endmills* with steep enough
helices to ensure continuous contact, then this problem can be
eliminated; two of the endmills can rotate in one direction while the
others rotate opposite them, with the relative depths of engagement
determining the overall revolution of the assembly.  It might be
possible to reduce this to two endmills and a roller.

Using ordinary endmills would give up the ability to control the rake
angle, but a more elaborate endmill design with movable inserts could
retain that degree of control as well.

For face milling, the equivalent of concentricity is tramming.  You
could imagine a sort of three-pointed fly cutter which dynamically
adjusts the rake angles of its three teeth as it moves over the
surface so as to cut deeper on one side than the other, in order to
bring the surface into parallelism with the desired plane.  If we
suppose the surface is horizontal, the cutter’s yaw axis is driven by
a spindle, while its pitch and roll axes are controlled by its
engagement with the surface.  Some kind of force is needed in Z to get
the teeth to dig into the stock (unless a steep rake can provide that
force on its own).  The varying degrees of engagement produce side
forces in X and Y, which will not in general correspond with the
desired direction of motion across the workpiece, so X and Y feed
motors are also needed.

If instead of one three-pointed fly cutter we have three, the X and Y
side forces from the nine points can be controlled to provide the
desired X and Y feed.
