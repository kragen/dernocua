I just noticed that FreeCAD sometimes seems to be using “backwards
perspective”: the side of a part that is obscured by being on the
opposite side from the camera is projected as *larger* rather than
smaller.  This is easy enough to achieve mathematically (you just
reverse the test for distinguishing visible surfaces from invisible
ones) and I understand that there are actually some physical lenses
that achieve this in real life as well, sometimes used for
machine-vision automted inspection systems.

It occurred to me that this is actually a potentially powerful UI
technique for increasing the visibility of parts in CAD, since, with a
wide enough viewing angle, you can see the part from nearly all sides
at once.  FreeCAD in particular is using a rather moderate viewing
angle, so the effect is somewhat subtle, and it doesn’t seem to be
happening all the time.
