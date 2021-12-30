Consider measuring four values x0, x1, x2, and x3 (for any value of
“four”).  One way to do this is to take a separate measurement of each
value, but often this is difficult to do, for example because your
measuring tools have unknown offsets.  So sometimes you might prefer
to measure four linear combinations of x0, x1, x2, and x3; then, any
fifth measurement will allow you to determine such an unknown offset.

Popular bases for this include the Fourier basis, in which you measure
the average value and the dot products with three sine waves.  But
that has the awkward problem that in many cases the coefficients are
transcendental; it also has the property that some of the coefficients
may be 0, as in the case of four values, where I think the Fourier
basis is x0 + x1 + x2 + x3, x0 - x2, x1 - x3, and x0 - x1 + x2 - x3.
The Hadamard-Walsh basis is another alternative, in which all the
coefficients are either 0 or 1, but these are also sparse, in the
sense that they don’t depend on all the values; or, alternatively, you
can use -1 and +1.

In some sense the simplest kind of number that could give you an
orthonormal basis for this kind of thing is rational numbers.  It
occurred to me that with one or more Pythagorean triples, you can
construct an arbitrary number of orthonormal bases with rational
coefficients.  Consider the triple 3-4-5.  This gives us the
orthonormal basis [[3/5, 4/5], [4/5, -3/5]].  We can use this to
rotate an arbitrary rational orthonormal basis into another rational
orthonormal basis; for example, starting with the identity-matrix
basis:

    [ 1  0  0  0 ]   [ 3/5  0  4/5  0 ]   [ 3/5  0  4/5  0 ]
    [ 0  1  0  0 ]   [  0   1   0   0 ]   [  0   1   0   0 ]
    [ 0  0  1  0 ]   [ 4/5  0 -3/5  0 ] = [ 4/5  0 -3/5  0 ]
    [ 0  0  0  1 ]   [  0   0   0   1 ]   [  0   0   0   1 ]

By iterating this sort of rotation we can get an infinite number of
orthonormal bases, and after a few such rotations our matrix is dense.
For example,

    [[ -900, -1200,  2500, -1125],
     [ 1293,  -776,  1200,  2460],
     [-2376, -1293,  -900,  1280],
     [ 1280, -2460, -1125,  -900]]/3125

or equivalently

    ⎡ -36     -48                ⎤
    ⎢ ────    ────    4/5   -9/25⎥
    ⎢ 125     125                ⎥
    ⎢                            ⎥
    ⎢ 1293   -776      48    492 ⎥
    ⎢ ────   ─────    ───    ─── ⎥
    ⎢ 3125    3125    125    625 ⎥
    ⎢                            ⎥
    ⎢-2376   -1293   -36     256 ⎥
    ⎢──────  ──────  ────    ─── ⎥
    ⎢ 3125    3125   125     625 ⎥
    ⎢                            ⎥
    ⎢ 256    -492           -36  ⎥
    ⎢ ───    ─────   -9/25  ──── ⎥
    ⎣ 625     625           125  ⎦

is a dense rational orthonormal matrix representing five such
rotations.  So, returning to our original measurement problem, we
could measure -900 x0 - 1200 x1 + 2500 x2 - 1125 x3, 1293 x0 - 776
x1 + 1200 x2 + 2460 x3, and so on, and by multiplying by the transpose
of this matrix and dividing by 9765625 (3125 squared), we should get
the original values of x0, x1, etc.  For example, for [11, 5, 8, -2]
we get [254/125, 15023/3125, -42361/3125, -1084/625] when we divide by
3125 once, and multiplying back through the transposed original matrix
does indeed give us back [11, 5, 8, -2].

Even though I don’t know how to define norms in a prime field, you can
convert a rational matrix like this into its equivalent in some prime
field, and do the same thing in that field, and you’ll still get back
the original numbers.

A thing that’s bothering me is that it seems like you ought to be able
to do something like this that gives you back *more* values than you
put in, and somehow use that for erasure coding, or N-of-M secret
sharing, or for noise reduction in noisy measurements.  But this
requires giving up orthogonality; you can’t have five orthogonal
vectors in a four-dimensional space, so you can’t just transpose the
matrix, you have to use some other approach to solving it, like
calculating the pseudoinverse.
