The number of coefficients of a general polynomial of a given degree
in a given number of independent variables is a binomial coefficient,
*n*C*m*.  This is surely well known, but it was surprising to me.

The general quadratic polynomial in two variables is *ax*² + *bxy* +
*cy*² + *dx* + *ey* + *f*; it has six coefficients.  Each of its terms
has degree 2 *or less*.

(By introducing a third variable *z*=1 we can make them each have
degree 2 *exactly*: *ax*² + *bxy* + *cy*² + *dxz* + *eyz* + *fz*².  So
6, the number of coefficients, is also the number of ways to get 2 by
adding up three natural numbers (including 0): 2+0+0, 1+1+0, 0+2+0,
1+0+1, 0+1+1, 0+0+2.)

In one variable, the number is 3: *ax*² + *bx* + *c*.  In general, in
one variable, the number of coefficients for degree *d* is *d*+1.

In no variables or in degree 0 for any number of variables, the number
is 1: *k*.

One way to factor *ax*² + *bxy* + *cy*² + *dx* + *ey* + *f* is as a
quadratic in *x*, *ax*² + *dx* + *f*, plus *y* times a linear in *x*, *y*(*bx*
+ *e*), plus *y*² times a constant in *x*, *cy*².  In matrix form:

    [ f   e  c ] [ y⁰ ]
    [ dx bx  0 ] [ y¹ ]
    [ ax² 0  0 ] [ y² ]

So it seems like the number of coefficients in a two-variable
polynomial will be a triangular number; to extend this to cubics, for
example, we’d add a new leftmost column that’s a general cubic in *x*,
some zeroes to fill out the bottom row, and *y*³ to the bottom of the
vector.

This is a general property: the general degree-*d* polynomial in *n*
variables is a sum of the general polynomials of all degrees up to and
including *d* in *n*-1 variables, each multiplied by the appropriate
power of the newly introduced variable to bring it up to the correct
degree.

If we instead try the same trick to go to a quadratic in three
independent variables, introducing, say, *w*, we can take this general
two-variable quadratic and multiply it by *w*⁰, take a general
two-variable linear polynomial (3 coefficients) and multiply it by
*w*¹, take a general two-variable constant polynomial (1 coefficient)
and multiply it by *w*².  So we have 1 + 3 + 6 = 10, but not because
it’s the fourth triangular number; rather, because it’s the third
tetrahedral number.

Without formally proving it, it seems like this is a matter for
Pascal’s triangle of binomial coefficients, (*a*+*b*)!/(*a*! *b*!):

     1      0      0      0      0      0      0      0      0      0      0
     1      1      0      0      0      0      0      0      0      0      0
     1      2      1      0      0      0      0      0      0      0      0
     1      3      3      1      0      0      0      0      0      0      0
     1      4      6      4      1      0      0      0      0      0      0
     1      5     10     10      5      1      0      0      0      0      0
     1      6     15     20     15      6      1      0      0      0      0
     1      7     21     35     35     21      7      1      0      0      0
     1      8     28     56     70     56     28      8      1      0      0
     1      9     36     84    126    126     84     36      9      1      0
     1     10     45    120    210    252    210    120     45     10      1

The number of coefficients for polynomials in zero variables are in
the first column; for polynomials in one variable in the second
column; for polynomials in two variables in the third column; and so
on.

The fourth column says that in three variables, a degree-0 polynomial
has one coefficient; a degree-1 polynomial, 4; a degree-two
polynomial, as explained above, 10; and a degree-three polynomial, 20.

This also means that the number of coefficients in a polynomial in
three variables grows as O(*d*³); specifically, it's
(*d*+1)(*d*+2)(*d*+3)/6.