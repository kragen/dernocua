Consider the statement:

    y := x * x;
    
One way to think of this is as a partial function from states of the
world to states of the world.  The prior state (the one in the domain)
needs to have some variable `x` defined in it, and the posterior state
has that variable `x` and also a variable `y`.  We could maybe write
that function as {x: x0, ...} -> {x: x0, y: x0², ...}, with the
understanding that the two `...` tokens denote the same set of other
variable assignments.

This is a partial function in the sense that it isn’t defined on
states of the world that don’t have an `x` in them.  We could
additionally argue that maybe it requires an `x` for which
multiplication to be defined in some way, and describe this as a
*type*.

Similarly, we can consider the statement

    z := y + 1;

to mean {y: y0, ...} -> {y: y0, z: y0 + 1, ...}.  Instead of being
undefined for environments that lack an `x`, this is undefined for
environments that lack a `y`.

If we *compose* these two partial functions, the result corresponds to
a sequence or progn of two statements:

    y := x * x;
    z := y + 1;

which denotes {x: x0, ...} -> {x: x0, y: x0², z: x0² + 1, ...}.  The
second statement’s requirement for `y` in the environment has vanished
because the first statement satisfied it directly.

(I’ve been thinking about a program-calculating environment where you
manipulate scraps of program like these, constructing them bottom-up
and combining them with elementary operations like sequencing,
alternation, and iteration (and their inverses), seeing not only the
procedures but the resulting extensional functions visualized as you
manipulate them.  It would be useful to also have additional
non-elementary operations like specialization, loop unrolling,
subroutine extraction, and conditional hoisting.)

This sort of inheritance of non-overridden variables is precisely the
semantics of indexing I have been thinking about for my “principled
APL” project.

Some interesting avenues for further investigation:

1. Conditionals (alternation) are straightforward to add to this way
   of thinking about statements, but what about while-loops?  Do they
   drive us to Dijkstra’s weakest-precondition function?  Or do they
   just denote the least fixpoint of a conditional function?
   
2. What do conditionals and while-loops correspond to in APL-land?

3. Is subroutine call just a slightly different form of composition in
   which most of the variable bindings from the called subroutine are
   discarded?

4. We can think of expressions as being functions from these
   environments to non-environment values.  The expression `45`, for
   example, denotes {...} -> 45, while a more interesting expression
   like `x * x` denotes the more interesting function {x: x0, ...} ->
   x0².
