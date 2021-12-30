3-D printing with a MIG welder (“WAAM”) suffers from a
positive-feedback problem which impairs geometrical precision: a
little bump on one layer tends to attract the arc of the next level
and consequently the droplets of metal, becoming a bigger bump on the
next level.  ([Marcin Jakubowicz says, “if you blast the power up,
that issue goes away,”][0] but apparently it’s an issue lots of WAAM
companies have, and Joshua Pearce reports in the same conference call
that he was scrubbing his prints with a wire brush between layers to
reduce this problem.)

Adam Blumhagen has proposed to Open Source Ecology that maybe if you
run a grinder over the surface after each layer, like the Ability 3D
and Big Metal, you could solve this problem (also potentially getting
better resolution than what MIG suffers from surface tension).
However, an alternative is to stabilize the system with negative
feedback: if you detect that the surface is slightly higher, you can
compensate by adding less metal to it.

[0]: https://youtu.be/ILw0MDsWhHQ "Open Source Wire Arc Additive Manufacturing, 11m37s"

There are a variety of ways you could detect this.  MIG welders in
particular are not really designed for this; they try to maintain a
constant arc length by maintaining a constant voltage across the arc,
but the amount of wire stickout is sort of uncontrolled, being the
integral of the difference between the meltoff rate (which is nearly
proportional to the current, which you can measure) and the wire
extrusion rate.  A small error in measuring either of these will work
out to a large error in estimating the stickout over time.

You could still use the wire as a conductive CMM probe by letting it
cool down first, then using a much smaller voltage and current to
probe the surface.  If you instead periodically probe a known surface
that isn’t changing significantly, ideally a piece of graphite or
something, you can find out what the current stickout is, correcting
the accumulated error in the stickout estimation.  Your stickout error
will still drift pretty fast, but maybe not fast enough for the
positive feedback problem to get out of control.

Using a much thicker electrode, as in stick welding, would largely
solve the problem by reducing the linear speed of meltoff; so would
using an electrode that isn’t constantly melting off, as in TIG
welding, although if you’re constantly crashing your tip into the work
it may not retain its nominal geometry for very long, even if you wait
for the work and the tip to cool first.
