I was watching a [video about the Open Source Ecology large 3-D
printer][0] and the problems they’re having with bushing misalignment.
Basically the problem is that they have this big 3-D-printed block
with spaces in it for bronze bushings, so that it will ride smoothly
and with low friction on a pair of steel rods, but it doesn’t.

[0]: https://youtu.be/BnMIJprpCIA

The problem is diagnosed to be misalignment: the bushings are
12-micron tolerance, so a 12-micron deviation in the shape of the
cavity they fit into is enough to get them out of tolerance, and
possibly kick the two bushings for a single rod out of parallel enough
that the rod can’t slide through the easily.

It occurred to me that this is another case of needing to worry about
not only geometry but the derivative of geometry with respect to
force, which is to say, compliance.  If there’s enough space around
the ends of the bearings for them to rotate a little bit in their
seats to comply with the rod, this wouldn’t be a problem, as long as
the solid ring around the middle of the bearing can support the
necessary load.  (The idea of leaving some play to avoid binding is
mentioned around minute 39 of the OSE video, but I don’t really
understand if they’re talking about leaving play in the same place I’m
talking about leaving play here.)

More generally you can leave space in the “solid” plastic *around* the
cavity which allows the cavity as a whole to rotate but not translate,
using established flexure designs to provide selective compliance
(whether using FACT or another design approach).  Even just using a
softer plastic would diminish the binding problem, but that might
create undesired compliance in other degrees of freedom; spaces for
compliance, like a 3-D version of the Snijlab living hinge, can permit
large compliances in selected degrees of freedom with minimal
compromise on strength and the stiffnesses in other degrees of
freedom.  Leaving such spaces can be done even with conventional
molding and subtractive manufacturing processes, but it’s much easier
with 3-D printing or digital 2-D cutting processes.

Another aspect of the problem is that they’re building a gantry with
lots of prismatic joints (built, in turn, out of cylindrical joints),
which pose a lot of problems like binding under side loads, and
revolute joints would have been a better choice.
