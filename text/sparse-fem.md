Normally finite elements are constant, linear, quadratic, or cubic, so
you have a relatively limited number of trial functions per element,
and a relatively large number of elements.  In a three-dimensional
element, an arbitrary scalar cubic polynomial has 20 degrees of
freedom (coefficients).  In three dimensions, the number of
coefficients ((*d*+1)(*d*+2)(*d*+3)/6, see file
`polynomial-pascal.md`) grows as the cube of the degree, which gets
annoying quickly, so normally instead of adding more coefficients you
just use smaller elements.  (Also, as I understand it, normally you
impose continuity conditions which reduce this dimensionality greatly,
as with cubic splines in one dimension.)

(There are lots of sets of 20 polynomials you can use as a basis for
this 20-dimensional space, even a convenient orthogonal basis.)

But suppose that, instead of using low-degree piecewise polynomials,
we use a smaller number of larger elements, each with a
much-higher-dimensionality function space, and then try to keep things
computationally tractable by seeking a *sparse* approximation in that
larger space, or at least, a sparse state evolution rule over time?

In a sense this is the farthest thing from a new idea; it’s how
Fourier solved the heat equation and Wiener solved everything, by
lumping the entire system into a single element and picking basis
functions that were eigenfunctions of temporal evolution, so the
system evolves independently in each of these “vibrational modes”,
making computation enormously easier.

Fourier space is of course a useful space to seek a sparse
approximation of lots of things, but there are numerous other
alternatives, including chirplets and all kinds of wavelets.
