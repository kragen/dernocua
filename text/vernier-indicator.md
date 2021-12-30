I was thinking of [SunShine’s flexure indicator][0] 3-D printed from
PLA, just using a couple of “blade flexures” that converge on an
indicator needle, nearly at the same point, perhaps 0.1 mm apart; the
needle is about 20 mm long.  Although he doesn’t have the thing
calibrated, he was able to use it to detect the thickness of a
50-micron-thick sheet of paper, which produced about a millimeter of
movement.

(I’ve put quotes around “blade flexures” because each “blade” is made
up of a set of parallel wiggle bars in order to allow them to connect
to the same bar at almost the same point without interfering; “we
stagger the layers”, as he says.)

In SunShine’s mechanism, most of the actual flexing takes place far
away from the indicator itself, which unfortunately greatly reduces
the amplification factor to only about 20:1; this could be remedied
with a more rigid flexure design, at the cost of increasing plunger
force, but a better flexure design is also possible.  He also has
sinned against flexures by making the plunger shaft a sliding contact
with the 8mm indicator stem rather than using parallel blades or some
similar prismatic flexure joint.

[0]: https://youtu.be/RFkn6gMkz78

The total range of motion of his indicator needle is about 10 mm,
which reduces the precision of readings available, even if you
calibrate the device.  It occurred to me that using the vernier
principle it should be possible to make much smaller rotations easily
visible.  By printing a disc that rotates relative to a fixed disc
with graduations at a slightly different frequency, you can visually
see quite small rotations.  Better still, I think, would be to print
each disc with a series of holes or slits in it, rather than merely
graduations on the surface, and place the two in sliding contact with
one another, or a flexural approximation thereof, so that the place
where the holes coincide moves around the dial much more rapidly than
the holes themselves.

It ought to be possible to get 200-micron holes with conventional 3-D
printing and laser-cutting processes, which ought to afford about
20-micron visible precision on the outer edge of the dial.  If the
mechanical advantage can be set to 50:1, this would provide
400-nanometer resolution.

As with a ruler or caliper, thermal expansion or contraction will
introduce error in the measurement.  However, uniform expansion either
of the dials or of the plunger and stem poses no such risk, because
such expansion doesn’t change the angles; it’s specifically the part
of the plunger outside the stem, and to a much greater extent, the
lever arm over which the plunger’s translation is transformed into
rotation, which determines the calibration.  Thus it should be
possible to incorporate a small piece of wood, invar, glass, sapphire,
carbon fiber, or fused quartz into that part of the movement, or build
it like a gridiron pendulum, to get a measurement tool that is immune
to such problems, differential though it is.

A simpler way to cancel thermal expansion in one dimension than a
gridiron pendulum is with the following structure:

       0      1       2      3
       #######         #######
    A  #########     ######### A
               #     #
              ##     ##
    B         ##@@@@@##        B
              ## @@@ ##
              ##     ##
              ##     ##
              ##     ##
              ## ### ##
    C         #########        C
       0      1       2      3

Here the # represents a material with a large thermal coefficient of
expansion, and the @ represents a (normally more of a pain in the ass)
material with a smaller but still positive TCE.  There are six
flexural joints in this setup: A1, A2, B1, B2, C1, and C2; let’s
suppose that essentially all the flexion happens there, while the rest
of the structure remains rigid.  Consider the ratio of distances
AB:AC.  If this is the same as the ratio of TCEs between the two
materials, then uniform heating will not change the distance A1A2.  By
putting B a little bit further down, we can get a *negative*
coefficient of expansion for A1A2, which could be chosen, for example,
to cancel the coefficient of expansion for A0A1 and A2A3, so that the
distance A0A3 is invariant with uniform heating.

In this literal form the structure would not be very stable; in
practice you would want to stiffen it.  Making just B1 and/or C1
perfectly rigid would probably answer for many purposes, and even if
C2 were rigid the structure might work adequately with the right
corrections.  If it could be arranged to be under constant
compression, the low-expansion B1B2 member could possibly be a ball
bearing ([steel: 12 ppm/K][22]), or a glass marble (8.5 ppm/K),
perhaps held in two lengthwise V-grooves in the A1C1 and A2C2 members,
so that any necessary rotation can happen by rolling, without
stick-slip movement.  Constant stress, whether compression or not,
would probably rule out the use of low-melting and therefore
high-creep materials like PLA.

Many materials might serve.  Radial expansion for Douglas fir is given
as 27 ppm/K, while parallel to the grain it is 3.5, but it is also
sensitive to humidity.  Brass is 19, aluminum 23, fused quartz 0.59.

[22]: https://en.wikipedia.org/wiki/Thermal_expansion#Thermal_expansion_coefficients_for_various_materials

Getting back to the indicator, a simple expedient might be to
laser-cut the whole thing from one to three sheets of steel.  Steel
has significant thermal expansion and contraction, but it’s much
smaller than that of many alternative materials; polypropylene’s TCE
is given as 150, 12 times higher, and even PLA is about 40 ppm/K.
And, unlike them, steel isn’t hygroscopic and doesn’t creep
significantly at ambient temperature.
