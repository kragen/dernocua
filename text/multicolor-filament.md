A YouTuber named [Sunshine][0] has demonstrated an interesting
technique for varying colors in an FDM 3-D print with a single hotend,
using the technique with PLA vaguely similar to knitting with
variegated yarn.  This also permits you to produce an unlimited
variety of colors within the color gamut spanned by two or more of
your filaments.

[0]: https://youtu.be/6kbjZobJtbM "3D-Print Your Own Filament! -  For Multi Colored Prints!"

He first prints out a spiral on his printer bed using two or more
filament colors in two or more printing passes; then he pops the
spiral off the bed and uses it as the filament for the final object.
Unless you do an additional filament-spiral-printing step, the
resulting color depends on the direction of movement during extrusion,
providing a color gradient.

At this point Sunshine is only printing a filament that remains
constant in composition from beginning to end, varying only laterally,
but it’s obviously easy to vary the composition as the filament
progresses, producing temporal variation during the print.

It occurs to me that your slicer knows within a few millimeters how
much filament will be extruded at various points in any given print.
So you could actually synchronize the color changes to different parts
of your print, so that instead of just the smooth color gradients
Sunshine demonstrates, you can perform arbitrary multicolor printing
in this way.  ([Marco Reps covers a multi-material filament splicer
called the Palette Plus from Mosaic Manufacturing][1] designed with
this purpose, but concurrent with the actual 3-D print itself, using
periodic pauses to fix desynchronization.)

[1]: https://youtu.be/7UVG9WLHMBQ

Doing this straightforwardly will suffer from some imprecision in the
color change, as the hotend’s melt chamber gradually changes from one
color to another, and also due to unavoidable imprecision in the
precise timing.  When this isn’t desired, you could insert G-code into
the print that moves the hotend off to the side of the print and
extrudes enough spaghetti to achieve the desired sharpness of color
change, wasting a little plastic, or you could choose to spend the
transition zone on inside perimeters or infill, where it won’t be
visible.  Typically you would have to do this two or more times per
layer.

By synchronizing the color changes to the amount extruded on a given
circumference of the print, you can achieve smooth gradients more
intense than those Sunshine achieved.

This filament-mixing process is not limited to color; you can use it
to achieve customized material properties, including gradient
properties.  For example, you could use filament with a metal filler
such as brass in areas of the print that need extra strength, density,
conductivity, rigidity, or shininess, or mix varying amounts of
thermoplastic elastomers into your ABS or PETG to give continuously
varying rigidity, or mix acetal into ABS, PETG, or PLA to improve
mechanical properties, or print polycarbonate or nylon fibers inside a
print to improve impact resistance, or polypropylene to provide a
chemically resistant surface, or include other fillers or additives to
make part of a print more malleable, translucent, electrically
permittive, phosphorescent, levorotary, permeable, hygroscopic,
flame-retardant, bacteriostatic, abrasive, hydrophobic,
abrasion-resistant, electronegative, ferromagnetic, high in refractive
index, ferrimagnetic, high in specific heat, diamagnetic, fragrant,
thermally expansive, flavorful, incompressible, acidic, porous or
otherwise permeable, optically dispersive, more dielectrically stable,
viscoelastic, high-melting, fluid when liquid, fluorescent, or
possessed of some other material property.  (Or less so: while flame
retardants will make a filament more flame-retardant, oxidizer fillers
will make it less so.)  And of course you can print water-soluble
supports with PVA.  This kind of processing has thermal limits, since
you can’t mix filaments that need incompatible hotend temperatures
(for example, PLA and nylon), but those can be extended somewhat with
additives such as plasticizers or antioxidants.

Even linear reinforcement like carbon fiber might survive this kind of
process.

Some kinds of additives might be harder to come by already mixed into
printer filament, but can be coated onto the surface of a filament
once it’s printed.  The geometry of the printed filament can be
adjusted to facilitate this kind of surface adhesion by having more
surface area.  It can also be adjusted to improve the grip of the
extruder, which is especially important for filaments that are highly
brittle or have high melt viscosities.

The filament in this process makes two trips through the hotend.  This
will have some good effects, such as boiling out any water it has
absorbed while in storage during the first trip; but it also increases
the strength loss from hydrolysis.  And of course it doubles the wear
on the hotend.
