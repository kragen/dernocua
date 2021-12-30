A clay wire cutter makes curved cuts.  If it enters a planar surface
of a clay block all at once while it is pulled taut, the cut starts
out straight, but if it enters incrementally, the cut can start out
curved; and of course the path on which it is pulled through the clay
can also be curved.

The cut path has a tendency to have negative Gaussian curvature as
initial wiggles in the wire tend to straighten out; I am not sure if
it the cut surface through homogeneous clay is necessarily a minimal
surface.

By moving the wire ends under automatic control it should be possible
to make preprogrammed cuts, and by using a mathematical optimization
algorithm such as Nelder-Mead or gradient descent on either a
simulation or experimental data, it should be possible to design those
preprogrammed cuts to produce a wide variety of geometries in the
clay.  Simulation parameters can be tuned from experimental results,
for example using a mathematical optimization algorithm such as
gradient descent.

The same thing is true of hot-wire foam cutters that contact the foam,
but the process has an additional degree of freedom, the speed.  The
trajectory of the wire through clay is almost insensitive to speed
because the clay is almost purely plastic, but that is clearly not the
case for hot-wire cutters, which encounter not only viscous resistance
but time-varying viscous resistance as the molten plastic around them
heats up.  By adjusting the wire current up and down, they can even
vary this variation with time.

Feedback from the wire cutting process can come in different forms:
tension, electric resistance, and electric impedance tomography
through the clay, for example.  This can improve the quality of the
control algorithm by improving the picture of what is going on during
the cut, permitting incremental replanning to improve the quality of
the final result.
