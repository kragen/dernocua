The Fibonacci sequence is F(0) = 1, F(1) = 1, F(*n*>1) = F(*n*-1) +
F(*n*-2), giving 1 1 2 3 5 8 13 21 34 55 89... and a property I just
noticed is that Σ*ₙ*F(*n*) for 0 ≤ *n* ≤ *m* is just F(*m* + 2) - 1.

We can observe that this property is true for *m* = 0: the sum is 1,
*m* + 2 = 2, F(2) = 2, so F(2) - 1 = 1.  When we advance the sum from
*m*₀ to *m*₀ + 1, we are adding F(*m*₀ + 1) to it.  F(*m*₀ + 3) =
F(*m*₀ + 2) + F(*m*₀ + 1), by definition, so if this property is true
for some *m*₀, it is also true for *m*₀ + 1.  So by induction it is
always true.

In some sense we should expect something like this to be true, since
the Fibonacci sequence grows exponentially, but it was still a bit of
a surprise to me to observe that 1+1+2+3+5+8+13+21+34 = 89-1.