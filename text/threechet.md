Truchet tiles are squares divided into a black right isosceles
triangle and a white one, and by tiling a surface with them at various
orientations you can achieve a wide variety of interesting patterns,
as [observed by Truchet in
1722](https://archive.org/details/methodepourfaire00doua) (and earlier
in briefer papers published in 1704 and 1707, it seems).

A variant of the Truchet tile introduced by Cyril Stanley Smith in
1987 has two quarter-circles connecting the centers of its square
sides, and can occur in two orientations; Smith comments early on:

> Truchet's patterns are superficially similar to those used in the
> construction of the mosaic tiles so prominent in Islamic
> architecture, the construction and philosophy of which, based on the
> intersection of circles of differing radii, has been so well treated
> by Keith Critchlow, but the principles are more fundamental.

Then later, introducing his variant:

> Of course, there are many other tile shapes with interesting
> properties, for example the non-periodic tilings described by Martin
> Gardner.  Then, more Truchet-like, are hexagons divided into two
> tetragons which assemble to give vertices of average valence 4 if
> uncolored or 5 if colored with a single internal line, and the
> square tiles of Fig. 19 with eight vertices and three internal
> polygons the boundaries of which on assembly in any orientation
> generate nothing but quadrivalent vertices and form continuous lines
> extending or closing on any desired scale.  As with any net of
> quadrivalent vertices, the first selection of one of two colors for
> one polygon determines the pattern of contrast throughout.

(This is, I think, very poorly explained, like the entire paper.)

These Fig. 19 “polygons” made of arcs are the patterns shown in Adrian
Likins’s 1998 xscreensaver hack “Truchet”, along with a variant that
replaces the quarter-circle arcs with straight diagonal lines.

(The Gardner reference is evidently to “Extraordinary non-periodic
tilings that enrich the understanding of tiles,” SciAm 236, No. 1,
110–221 (01977), which [seems to have been about Penrose
tilings](https://blogs.scientificamerican.com/guest-blog/the-top-10-martin-gardner-scientific-american-articles/),
(certainly [the cover depicts a Penrose
tiling](https://www.scientificamerican.com/magazine/sa/1977/01-01/))
but I don’t have the article.)

It occurred to me that, instead of dividing each side of the square
tile into two equal parts with an arc, you could divide each divide
them into *three* parts with two points of division, perhaps with the
center part being smaller or larger than the other two.  If we letter
the sides clockwise A, B, C, D and number the two points of division
clockwise as 0 and 1, then we have eight points of division (in
clockwise order: A0, A1, B0, B1, C0, C1, D0, D1), which we can connect
with arcs, or not.  One obvious possibility is A1-B0, B1-C0, C1-D0,
D1-A0, and another is A0-A1, B0-B1, C0-C1, D0-D1.  More interesting,
perhaps, is A1-B0, A0-B1, which (unless we allow intersections or
unconnected points) forces the connections C0-C1, D0-D1, and even that
is only possible if the center interval isn’t too long.  This tile has
four rotations.  Allowing straight lines as well as arcs gives us
another pair of tiles: A0-C1, A1-C0, B0-B1, D0-D1, and its 90°
rotation.  The lines on all of these (if, unlike Smith, we omit the
tile boundaries) join to form closed curves with no sharp angles and
no intersection or branching.

Using two points of division per side enables us to also use a regular
triangular tile, with division points A0, A1, B0, B1, C0, C1, and
tiles including A0-A1, B0-B1, C0-C1; A1-B0, B1-C0, C1-A0; and possibly
A1-B0, A0-B1, C0-C1 and its other two rotations.  But this last tile
is only free of intersections if the middle interval is fairly small.

A regular hexagonal tile with only a single point of division per side
has only one obvious base tile: A-B, C-D, E-F, with two rotations.  If
we permit straight lines we also have A-B, C-F, D-E and its other two
rotations.

