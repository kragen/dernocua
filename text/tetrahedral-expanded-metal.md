To make a three-dimensional honeycomb with the open-cell structure of
the diamond crystal lattice, you make many sheet-metal strips of the
same width, and you make a stack of two of these layers of strips,
running at right angles, either with or without spacing between the
strips.  This gives you a grille of intersections between the strips.
Color these intersections chessboard-style and spot-weld the black
ones.  Add a third layer at right angles to the second, each of its
strips in the same position as a corresponding strip in the first
layer (except displaced in Z by twice the sheet metal thickness), and
spot-weld the white squares.  (This may require a spot-welder with
both electrodes on the same side of the workpiece, like those used for
welding nickel strips to lithium batteries.)  Now at every
intersection the second layer is welded to either the first layer or
the third layer.  Add a fourth layer parallel to the second, and
spot-weld it to the third layer at the intersections where the third
layer isn’t welded to the second (but the second *is* welded to the
first).  And so on.

Once you have added enough metal, pull the layers apart, permanently
bending the strips so that each welded intersection becomes a
tetrahedral lattice point.

If you have two-dimensional square mesh available for free, you can do
this with half as many spot welds.  Place a second layer of mesh on
top of the first layer, with its X and Y axes parallel, but offset in
both X and Y by half a cell, so that each wire in one layer of the
mesh crosses a wire in the next layer exactly halfway between the two
nearest intersections in each of their respective meshes.  Spot-weld
all these crossing points; repeat.

This isn’t a very rigid structure, which is why it’s possible to bend
it into shape by pulling on it once it’s welded up.  If impact energy
absorption is the goal, then that’s fine; it should work great for
that.  However, if higher rigidity is desired, it’s possible to take
advantage of metals’ work-hardening tendencies to get it.  Say that
two intersections are “metamours” if they are directly connected to a
single common intersection.  The trick is to add additional members to
the structure connecting each pair of metamours which get further
apart during the pulling process, of which I think each intersection
has 8; these extra members are initially not straight, but the initial
expansion of the matrix straightens them, which work-hardens them.  If
the expansion is done rapidly enough, the mass of the centers of these
members comes into play, makng them straighter than the same amount of
pulling force could have made them under quasistatic conditions.

This may be enough to get an ideal omnitriangulated mesh like an octet
truss.  There are still 4-cycles in the structure that have no
diagonals, one between each pair of metamours in the same layer, but
that's true of the standard octet truss as well.

