Some ideas about tile-based media for constructing systems.

Historical background
---------------------

After writing file `unicode-graphics.md` I remembered a graphics
program called SYMED on the Zenith Z-100, capable of drawing, for
example, extensive circuit schematics, despite the machine only
possessing 128KiB of RAM, a sub-MIPS processor, sub-megabyte floppies,
and totally unaccelerated graphics.  (I suspect that this program is
totally unrelated to the Mentor Graphics program of the same name;
although they are used for related purposes, there is no similarity in
how the programs work.)  In SYMED you defined a tileset, as with
Nintendo games, and placed tiles from the tileset to form your
drawing.  SYMED arranged these into the machine’s framebuffer for
display ([8 colors at
640×225](http://www.computinghistory.org.uk/det/44090/Zenith-Z-100/),
which works out to a hefty 54KB of video RAM) but stored the tile
definitions and tile indices.

I forget how big the tiles were, but if we suppose they were 8×8 (a
common size for such things) you might be able to get a creditable
representation of a diode or capacitor, or half a resistor or
inductor, into one — you could repeat the “symbol” for the other half
of the resistor.  Vertical and horizontal wires, four corners, four
junctions, four diodes, two resistor sections, two inductor sections,
two capacitors, a four-way intersection, a crossover, and a battery
might add up to 23 symbols; you could probably do a real circuit with
around 64 symbols.  The definitions of those 64 symbols, if
monochrome, would occupy 512 bytes, and each screenful of 80×28 tiles
would occupy 2240 bytes at one byte per tile, so a screenful might be
a 3-KB file, quite a lot of compression compared to the 54K of a raw
framebuffer dump, and still smaller than a 6K monochrome dump.  If the
tiles were full color, 64 of them would be 1.5 KiB, so a full-color
screen-sized drawing would be almost 4K.  (You could do bit-packing
tricks with such a small number of tiles, packing 8 tile indices every
6 bytes, but I don’t know if SYMED did.)

In theory it would be easy to do PLATO-like or APL-like overstrike
with such tiles, or Nintendo-like sprites composited in at arbitrary
places, although I don’t think SYMED could do this.  I don’t remember
if it even supported text annotations.

For things like schematics you wouldn’t need to separately draw and
store the four orientations of diodes; you could generate them
algorithmically with rotations.  This would cut the 23 separate
symbols above to 10 and additionally let you reorient the battery as
you wished.  Nowadays this is interesting not to save space on
400-kibibyte floppy disks but to make the system a more fluent medium
for creation, because you don’t have to make parallel modifications to
various copies of your sprites.

Here’s a somewhat similar set of symbols from the Unicode box drawing
set, although this does not represent a coherent schematic for
anything and lacks the circles indicating wire joins:

            ┌╫───┐
       ┌───┬┘╭┤├─┤
       └─▶├┼─╯   │
           └╮    ▼
            ╰╮   ┬
             ╰┄┄┈┘

Still, it would be nice to have a more parsimonious set of tiles.
Perhaps this Commodore BASIC program from the *Commodore 64 User’s
Guide* is relevant:

    10 PRINT CHR$(205.5+RND(1)); : GOTO 10

This outputs a “maze” like the following:

    ╲╲╱╲╲╲╱╱╲╲╱╲╱╱╲╲╱╲╲╱╲╲╱╲╱╱╲╲╲╲╱╲╲╲╲╱╱╲╱╲
    ╲╱╲╲╱╱╲╲╲╱╲╲╲╱╱╲╱╱╱╲╲╱╱╱╲╲╲╱╲╲╲╲╱╲╲╱╱╲╱╱
    ╲╲╱╲╲╱╲╱╱╱╱╱╲╱╲╲╱╲╱╱╲╱╲╱╲╱╱╱╲╲╲╲╱╱╱╲╱╲╱╱
    ╱╲╲╲╲╲╲╱╲╱╲╱╲╱╱╲╲╲╲╱╱╱╲╲╲╱╱╲╱╱╱╱╱╱╲╲╱╲╱╱
    ╱╲╲╲╱╱╱╱╱╱╲╲╱╲╱╲╱╱╲╱╲╱╲╱╲╱╱╲╱╲╱╱╱╲╲╲╱╲╲╱
    ╲╱╱╲╲╱╱╱╱╲╱╱╱╲╱╲╲╲╲╲╲╱╲╲╱╱╱╲╱╱╱╲╲╱╱╲╲╲╱╱
    ╱╱╲╱╲╱╲╲╲╲╱╱╱╱╲╱╱╱╱╲╱╲╲╲╲╱╱╱╲╲╱╲╲╱╱╱╲╱╲╲
    ╲╲╲╱╱╲╱╲╲╲╱╱╲╲╱╲╱╲╱╲╲╲╲╱╲╲╱╲╱╲╱╲╱╲╲╱╲╱╲╲
    ╱╲╱╱╲╱╲╲╲╱╲╲╲╱╲╱╲╱╱╱╲╱╱╱╱╲╱╲╲╱╱╲╲╲╱╲╱╲╱╲
    ╱╲╲╱╲╱╲╱╱╲╱╲╱╲╱╲╱╲╲╱╱╲╲╲╲╲╱╱╲╲╱╱╲╲╲╱╲╱╱╱
    ╱╱╱╲╲╲╱╱╲╲╲╱╲╱╲╲╲╲╱╲╲╱╲╲╲╱╲╱╱╱╱╲╱╱╲╱╲╲╱╲
    ╲╱╲╱╱╲╲╲╱╱╱╲╲╱╱╱╱╲╲╱╲╲╲╲╲╱╲╲╱╲╲╱╱╱╲╱╱╲╲╲
    ╲╲╱╱╲╱╲╱╱╱╲╲╱╲╱╲╲╲╲╱╱╱╲╲╱╲╲╱╲╲╱╱╱╱╲╱╲╲╲╲
    ╲╲╲╲╱╲╱╲╱╲╲╱╱╱╲╱╲╲╲╱╱╱╲╱╱╱╲╲╲╱╱╱╲╱╱╲╱╱╲╱
    ╲╱╲╲╲╱╲╱╲╱╲╱╲╱╱╱╲╲╲╱╲╲╱╲╱╲╲╱╲╲╱╲╱╲╲╲╱╱╱╱
    ╲╲╲╲╱╲╱╱╱╱╱╱╱╲╲╱╱╱╲╱╲╱╲╱╲╲╲╲╲╲╱╱╲╱╱╱╱╲╲╲
    ╲╱╲╱╲╱╲╱╱╱╲╱╲╲╲╲╱╱╲╱╲╲╱╲╱╲╲╲╱╱╲╲╲╱╱╲╲╲╲╱
    ╱╲╱╱╱╲╲╱╱╲╱╲╱╱╲╲╲╲╱╲╲╱╱╱╱╲╱╲╲╱╱╱╲╲╱╲╲╲╱╱
    ╱╱╲╲╲╲╱╱╲╱╱╱╱╲╱╱╲╱╱╲╲╱╲╲╱╲╲╱╲╲╱╲╱╱╱╲╲╱╱╲
    ╲╱╱╱╲╱╱╲╱╲╱╱╲╲╱╲╱╲╱╲╲╱╱╲╱╲╱╱╱╲╲╱╲╲╱╲╲╲╱╲

(I generated the above in Python 3:

    for _ in range(20):
        print(''.join(chr(random.randrange(0x2571, 0x2573))
                      for _ in range(40)))

)

This uses a smaller tileset, only two tiles, to produce an interesting
range of topologies, though the passages don’t branch.  On the
Commodore, with its square character cells, the lines were
perpendicular to each other, just not to the edges of the display.  In
addition to the diagonal-line characters 205 and 206 above, it also
had a crossed-diagonal-lines character 214 (`╳` in Unicode, U+2573,
`BOX DRAWINGS LIGHT DIAGONAL CROSS`), and of course a space character.

By adding these additional tiles, we can get branching passageways,
which is most interesting when the amount of branching is close to the
critical percolation threshold:

    for _ in range(20):
        print(''.join(' ' if random.random() < .2 else
                      '╳' if random.random() < .1 else
                      '╲' if random.random() < .5 else
                      '╱' for _ in range(80)))
 
     ╲╱╱ ╱ ╲╱ ╱╱╱╲ ╳╱ ╲╲ ╱╲╲╲╲╱╱╱╱╱╲  ╳╱╱ ╱╱ ╲╲  ╱╲╲╲╳╲╲╲╲╱╱╲╲╱╲╲ ╲╱╱╲╱╱╱╲╳╳╱╳ ╲╱╲╳╱
    ╲╱╳╱╲╱╱╱╲ ╱╲╲╱  ╲╱╲╲╲╱╱╲╲╲╳╲╲╳╲╱ ╲╱╲╲╱╲ ╲╱╱ ╱╱╲╱╱╲╳╳╳╲╱ ╱╳╲╱╱╱╱╲╱╱  ╱╱╱╱╲╱╲╱╱╱╲╲
    ╳ ╲╱╲╱╱ ╲ ╱╱╱╱╲╱╲╱╲╳╱╳╳╱╲ ╲ ╳╲╱╱╱ ╲╱╱╲╱╲  ╲╲╱╲╲╱ ╲╱╲╲ ╱  ╱ ╲╲ ╲╲ ╱ ╲ ╲╲╱╲ ╱ ╱╱╲╱
    ╱╱╳╲╱╳╲╲╲╲ ╱╲╱╲╲ ╲╲╳ ╲╲╱╲╲╳╱╲╲╱ ╱ ╲╱ ╱╲╲╲ ╲╲ ╲╲ ╱╲╲ ╱╲╱╲ ╱ ╱╱   ╱╱ ╲╱ ╲╲╲╲ ╱╱ ╲╲
    ╱╱  ╲╱╱╲╱╱╲╲╳╱╲ ╱╳╲╳╲╱╲╲╳╲╲╱╳╱  ╲╲╱╱╳ ╳╱╳╱ ╲╳╱    ╲╲╲╱╱╱╲╱╳╱ ╲ ╲╲╲ ╲╱╲╱╱╱╱╲╲ ╲╲╲
    ╲╱ ╲ ╱╳╲╲╲╱╱╲╱╲╱ ╲ ╲╲╲╲╱╳╱ ╱╲╱╱╱╱  ╱╲ ╲╲╲╱╲╳ ╱╱╲╲ ╳╲ ╱╲ ╱ ╲╳ ╱╱╲╲╲╱╱╲╱╲╱╱╱╱╱╱╲╳╱
    ╲ ╱╱ ╲╲╲ ╲╲ ╲╱╲ ╲╱╲ ╱╲ ╱╲╲╱╱╱╲╲╲╲╱╱╳╳  ╱╲╳╱ ╳╱╲ ╱ ╱╱╱ ╱╱╱╲╲╲╲ ╲╲╱╲╲ ╲╲╳╲  ╱ ╲╱╱ 
    ╱╲╱ ╱╱ ╲╱╲╱╱  ╱╱╲╱╱╲╲ ╱╱╲╲╱╱╱╲╲╲╳╱╲╳╱╱ ╲╲╱╳╲╲╱ ╱╲╱╱╲  ╱ ╱╱╲╲╲╲╳ ╱╳╱╱ ╲╱╲╲╳╲╲╱ ╱╲
    ╱ ╱╲╱╱╳╲╲╲╱╲╲ ╱╱╲ ╱  ╳╱╲╱╲ ╲ ╳ ╲ ╱╲╱╳╲╲╳ ╱╲╲╱╳ ╲╱ ╱╱╳╱╲ ╲╱╱╱╲╲ ╲╳ ╱ ╱╱╳  ╱ ╲╳╱╲╲
    ╱ ╳╲ ╱╱╱ ╲ ╲╳╳ ╲  ╲╱╱╳╲╲╳╳ ╲╱╲ ╱╳╳╲  ╲ ╲╳╳╱╲╱╲╱╱╲╱╲╱╱╱╱╲╱╱   ╱╳╲╲╲ ╱╱╱╱╱╲╱ ╳╲╱  
     ╲╱╱ ╲╱╱    ╱╲╱╲ ╲╱╲╱╲╲ ╱╲╲╳╱ ╲ ╱ ╱╱╱╱╱  ╱╲╲╲╲╲╱╲╲╲ ╲╱╱╱╳╱╱╲╱╱╲╲╱ ╲╳╳╱╱╱╲╳╱╲╲ ╱╱
    ╲╱   ╲  ╲╱╲ ╲ ╲ ╱╲╱ ╱ ╱╲ ╲╲ ╲╲╱╲╱╲╱ ╲╳╲╳╲ ╲╱╱╲ ╲╱╲ ╱ ╲╱╲╱╲  ╱  ╱╱╲ ╳╲╲╱╱╲╱ ╲ ╱╲╱
    ╲╲╲╱  ╱╱╱╲╱ ╲╱╲╱╱ ╲╱╲╱╱╲ ╲╲╱╱╲╲╱╲   ╲   ╳╲╱  ╱ ╲ ╱╲╱╱╲╱╳╲╲╱╲╲ ╲╱ ╲ ╲╲╱╳╱ ╱╲╱╲╱ ╱
    ╱╱ ╱╱╲╲╲╱╲    ╱╲╱╲ ╱ ╲╱╱╳╱╲╱╱ ╳ ╳ ╲   ╱   ╱╱╲╲╱╱╲╲╲╱ ╲╱╱╲╲╱╲╳╲╱╱╲╲╲╲╲ ╳╲╲╱ ╱╲╱╱╲
    ╳╱╲╲╱  ╱ ╱ ╱╳╲╲╱  ╲╲ ╱╲ ╲╲╲ ╱  ╱╲╲╲╲ ╱ ╲  ╲╱╲ ╳╱╱╲╱╲╱ ╲╲  ╲ ╲╲╱╲ ╱ ╱ ╳╲╱ ╱╳╱╲╱╲╱
     ╲╳ ╲ ╱╲ ╳╲ ╱ ╱   ╱╲╱╲╱╱╱╲╱╱ ╳ ╱ ╱╲╲ ╲╳╱╲╱  ╱╱ ╱  ╲ ╱ ╱╲╲╱ ╲ ╲  ╲╲╱ ╲╲╲╲╱╲╲  ╲╲╲
    ╲╱╳╲ ╲╱╳╱╳╱╳╲╲╲╱╲╲╲╱╲ ╱╱╲ ╲╳╲ ╱   ╳╲╲╲╲╱╱ ╲ ╱╱╲ ╲  ╲╱ ╲ ╲╳╱╳╱╱╲╱╱╱ ╲╲╱╱╲╱╱╱╲ ╱  
    ╱╲ ╲╱╱╲  ╲╲╳╳╲╱╱ ╱╲╲╲╱╱╱╲╳╲╲╲╳╱ ╲╲╲╱╱╲╱ ╱╱╲ ╲╱  ╱╲ ╳╱╲╱╲ ╳ ╱ ╲╲ ╲╱ ╲ ╲╲╲╲╲╲╱ ╲╱╲
    ╲╲╲╱╱╲╱╲╱╱╲╲ ╲╳╲  ╳ ╱╱╱╲ ╲╲╲ ╲╲╱  ╲╲ ╱╱╲╳╱╱ ╲╲╱╲╲╲╱╲╲╲╳╳╲ ╲╱╱╱╲╱╱ ╲╲╱ ╲ ╱╲╲╳ ╱╳╱
    ╱ ╳ ╱╲ ╳╱╲╲╲  ╱╱╲╱╱╱╲╱╲╱╲╲   ╳╲╱╱╱ ╱╲  ╱ ╳╱╱╲╱╱ ╲╲╲ ╲╲╱ ╱╲╱╲╱╱╲╱ ╲╲╲╱╱╲╱╱ ╱╱╱╲ ╲


If you make the tiles square and rotate 45°, boxes like this:

    ╱╲
    ╲╱

become boxes like this:

    ┌─┐
    │ │
    └─┘

Correspondingly this

    ╳╳
    ╳╳

becomes this:

      ╷
     ┌┼┐
    ╶┼┼┼╴
     └┼┘
      ╵

What you give up is the ability for the lines to begin or end on any
grid point; now they can only begin and end on half of the grid
points, the ones corresponding to the black squares on a chessboard.
In exchange, for line drawings, you only need one bit per grid point
instead of 4, and you only need to draw four tiles including space, or
three if rotation is automatic, instead of 16 (or six if rotation is
automatic: `─ ┐ ┤ ╷ ┼` plus space).

Paraxial parallelograms
-----------------------

Now, suppose we divide our board into square or parallellogram tiles
whose diagonals are vertical and horizontal:

    ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲
    ╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱
    ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲
    ╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱
    ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲
    ╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱
    ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲
    ╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱
    ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲
    ╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱
    ╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲
    ╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲╱

In each of these tiles we can place a horizontal line, a vertical
line, both, or neither, or some other component, such as a resistor or
diode.  If they’re square, you can automatically generate multiple
rotated tiles from a single master, so you only need to draw, for
example, one diode instead of four.

This skew-tile approach reduces the number of tiles, but with some
drawbacks.  Unless supplemented with sprites, if you *do* want to, for
example, render three-way intersections differently (for example with
a dot), you need not just one new tile but two or more, containing the
different parts of the dot.  In the simplest approach, this also
requires the user to replace four tiles when they want to place such
an intersection, but there are various possible approaches to avoiding
this, including Wang-tile-like approaches.  And inserting or deleting
rows or columns of tiles is no longer so simple.

Isometric grids
---------------

A uniform grid of equilateral triangles can tile the plane, and the
isometric projection measures along just such a grid.  QBert and
Zaxxon (from 01982) take place on such an isometric grid.  Marble
Madness (01984, by Mark Cerny, running on a 68010) used an isometric
projection, but included lines that deviated from the grid for things
like sloped surfaces.

One approach to creating a tileset for such a grid is to pick one of
the three isometric planes and draw tiles for the parallelograms in
that plane.  This can display integer displacements perpendicular to
that plane as long as the displacements are quantized.

Ugh, I guess I should implement these things to see how well they
work.
