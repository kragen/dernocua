Suppose you want to make a minimal number of gage blocks (Joe blocks)
out of Zerodur or something similar, with precision of 0.1 microns and
a range from 2 mm up to 200 mm in increments of 0.5 microns.
Conventionally this is done with combinations of 1 to 7 gage blocks
from a set of some 80 or 90 pieces.  (Also, conventionally, the blocks
are made of hardened steel rather than a ceramic, despite steel’s
inferior thermal stability, chemical stability in air, and tendency to
raise burrs when scratched.  Zirconia gage blocks are coming into use,
but they are no more thermally stable than steel; a zirconia coating
on a Zerodur base would probably be better still.  Tungsten carbide is
an intermediate ceramic that is seeing some use with a lower TCE.)

Well, in theory you could try doing it in binary, with sizes in
microns 0.5, 1, 2, 4, 8, 16, and so on, 18 sizes in all to get to 200
mm.

But a gage block that’s less than 10 microns thick will be destroyed
when you touch it, probably 100 microns if it’s a fragile material
like Zerodur.  If instead you start at 200 microns and go up with
these binary increments, you could start with 200.5 microns, 201, 202,
204, 208, 216, 232, 264, 328, and 456, plus ten 200-micron blocks,
then you can wring together ten items from this set to get from 2 mm
to 2.5115 mm in 0.5-micron increments; at this point you can add
blocks of 0.512 mm, 1.024, 2.048, 4.096, 8.192, 16.384, 32.768,
65.536, and 131.072 to get any number up to 200 mm.  Up to 264.1435
mm, in fact.  But that’s 29 blocks instead of 18.

Suppose that instead we use balanced ternary and add an offset of 250
microns.  Our first few blocks would be of sizes 249.5 microns, 250.5,
248.5, 251.5, 245.5, 254.5, 236.5, 263.5, 209.5, 290.5, plus 5 blocks
of 200 microns.  Combinations of 5 of these 15 blocks give us any size
from 1.1895 mm up to 1.3105 mm in increments of 0.5 mm, 243
measurements covering a total range of 121 microns.  If we offset our
next power of 3 around 321.5 microns instead of 250, we have three
more blocks of 200, 321.5, and 443 microns, and now we can cover the
range from 1389.5 microns to 1753.5 at 0.5-micron intervals by
wringing together 6 of these 18 blocks, a 364-micron range.  A single
additional block of 364 microns doubles our range, and now we have a
728-micron range in combinations of 6 or 7 blocks out of 19.  By
increasing the offsets mentioned above we can relocate that range to
cover 2.000 to 2.728 mm; this is clearly a small improvement over the
previous system, which needed 20 blocks to cover 2.000 to 2.5115 at
the same resolution.  Adding 9 more binary blocks as before gets us to
our objective in 28 blocks.

Still, I can’t help but feel that this is not optimal.  There are
524288 combinations of our 19 initial blocks, but these are only
giving us 1457 different lengths within their intended range; many
combinations are outside the bounds (including all the combinations
with less than 6 or more than 7 blocks), and 5 of the initial blocks
are 250 microns in size and thus interchangeable, so there are many
equivalent ways to achieve most of our 1457 lengths by using one or
another 250-micron block.  Ideally if we wanted to be able to
construct 1001 evenly spaced lengths from 2.0000 mm to 2.5000 mm, we
could do it with only 10 blocks (from which there are 1024
combinations), or maybe only a little bit more, rather than needing as
many as 19.

So, it seems that this solution can be easily improved (it’s only
about 0.3% efficient) but it’s not clear to me what the optimal
solution is or how to calculate it.

Making the gage blocks circular rather than rectangular might make it
more difficult to wring them together, but it would also reduce their
vulnerability to chipping.

If these blocks are themselves microscopic in size and intended to be
handled by microscopic manipulators, the problem of very thin blocks
may become less severe, as breakage is less of a problem at small
scales; the forces needed to lift and manipulate objects are smaller
relative to their strengths than at macroscopic scales.  But surface
effects like adhesion and wear may become more troublesome.
