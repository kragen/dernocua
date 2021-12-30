2-D cutting (laser cutting, waterjet cutting, CNC plasma table, 2-D
wire EDM, the electrolytic method described in file
`electrolytic-2d-cutting.md`, etc.) is a highly efficient way to make
things, especially at large scales and when you have high precision.
It occurred to me that by combining it with electroforming and anodic
dissolution (ECM) it can be substantially more powerful.

Sheet lamination
----------------

If you want to 3-D print a 100-mm prolate spheroid that is 50 mm in
its minor diameters, you need to 3-D print 131 milliliters of volume.
With a typical 30% infill, this works out to 39 milliliters of actual
plastic for the interior.  If you use an 0.8-millimeter line width to
print 3 perimeters around each layer, you have about 2.4 mm of
thickness on the shell, which is 38 of those 131 milliliters, leaving
only 93 mℓ for the infill, using 28 mℓ of plastic, for a total of
66 mℓ.  At a typical layer height of 0.2 mm this is 138 meters of
extrusion; at a typical 50 mm/s, this is 46 minutes of printing.

XXX recalculate that, it’s calculated with a shell thickness of 2.4 mm
which is wrong on the bottom and top

By contrast, if you instead print out the same object by sheet
lamination (“laminated object manufacturing”), you only need to cut
the perimeters.  If you were to use the same 200-μm layer height, you
would only need to make 78.5 meters of cuts, which at the same
movement speed of 50 mm/s would only take 26 minutes.  The resulting
object is normally fully dense, which is an advantage in some
contexts, since it makes it stronger and stiffer.  In cases where it
is not, if the inside contour of the object (where infill would have
been placed) is not strictly defined, you can often hollow it out by
nesting multiple layers one inside the other, avoiding the need for
extra cutting time.

Often the movement speed is *not* the same; many 2-D cutting processes
can run at much higher speeds than additive processes can usually
manage.

This advantage increases for larger objects and decreases for smaller
ones; for a meter-scale object instead of a factor of 1.8 it’s a
factor of 18.  Larger objects tend to benefit more from being fully
dense, because they need proportionally more cross-sectional area to
support their own weight, or their own mass under the same
accelerations.

Electrolytic welding
--------------------

By electrodepositing a thin layer of metal on a metal object made by
metal sheet lamination as described above, we can get several
important advantages:

- The layers are connected together by the deposited metal.  Although
  it won’t *penetrate* the layers, under some circumstances it can
  have sufficient adhesion to them to form a solid object.  This
  depends crucially on their surface condition, which is more
  controllable in this situation (sheets freshly cut out, produced by
  a controlled process) than under some other circumstances.

- The alternative to connecting the lasers is to run slots or holes
  through many layers and put a sliding fastener through them; such
  fastener-based or sliding-joint construction can also be fixed
  “permanently” by such electrodeposition.  (If the glue metal being
  deposited can be anodically dissolved at a more moderate voltage
  than the base metal, the glue metal can be selectively removed later
  by electrolysis, permitting disassembly.)

- The electrodeposited metal can smooth out layer lines which could
  otherwise interfere with appearances, fluid flow, optical
  performance, smooth sliding, human comfort, etc.

- The electrodeposited metal (or composite) can be a material that
  can’t be processed by the original sheet-cutting process, or with
  more difficulty.  For example, copper and nickel cannot be cut with
  oxy-acetylene torches, but you can very rapidly cut out a form from
  cheap mild steel on a CNC oxy cutting table, then electrodeposit
  them on its surface.  This is especially true of nanolaminates,
  whose properties can be tuned to the application.

- If the originally deposited sheets can be anodically dissolved at a
  more moderate voltage than the newly electrodeposited metal,
  contrary to the anodic ungluing process described above, they can be
  selectively removed after the electroforming process is complete.

Subtractive 3-D printing with ECM
---------------------------------

Electrodeposition suffers from a positive feedback process of dendrite
growth, in which protuberances on the surface are exposed to greater
electric fields; as a secondary, much weaker, effect, they physically
obstruct ion transport (“mass transport control”) to nearby parts of
the surface.  Consequently small protuberances grow into larger
protuberances, potentially bridging all the way to the cathode while
most of the material is only thinly plated.  This is exacerbated by
the anisotropic nature of crystal growth; as I understand it, many
“brighteners” used in electroplating work by introducing grain
boundaries to prevent the creation of large crystals.  Others work by
reducing ionic flow so that deposition rate is limited by ionic
concentration rather than electric field.

Electrolytic cutting or electropolishing suffers no such effect (on
the workpiece); instead of causing small irregularities in the surface
to *grow* faster, it causes them to *shrink* faster, making the
feedback *negative*.  This permits the usage of much larger currents
and correspondingly larger material removal rate.

So you can get faster free-form fabrication by alternating electroless
plating with anodic removal of the unwanted part of the deposited
layer, for example using a movable array of separately controlled
cathode electrodes, each removing a controlled amount of material in a
particular area of the workpiece.  By limiting the degree to which the
workpiece is dipped into the electroless plating bath, you can prevent
material from depositing elsewhere on the workpiece than the current
layer, enabling a layer-by-layer printing process.  With electroless
codeposition you can even print in a metal-matrix composite, and with
the right choice of baths you can switch between two or more different
baths to produce a nanolaminated material.

This procedure, as described, requires moving the workpiece back and
forth between an electroless plating bath and a second bath where it
is electrolytically cut by cathodes in precise positions relative to
it (which may be moved in the process).  You probably cannot use a
single bath because the electroless plating solution will probably all
plate out on your cathodes; you might be able to find a cathode
material that doesn’t do this, but it may be difficult.  An
alternative using a single bath is to alternate between selective
electrodeposition (at higher current densities than are normal for
electroplating) and selective electropolishing (to smooth out any
irregularities in the surface that are unwanted).  This permits much
finer layers and eliminates the dead time and material loss between
the two baths.

Unfortunately, both the [negative feedback in electropolishing][0] and
the positive feedback in electrodeposition increase with the
resistivity of the electrolyte.

[0]: https://www.pfonline.com/articles/a-pulsepulse-reverse-electrolytic-approach-to-electropolishing-and-through-mask-electroetching