(Based on Jamie Brandon’s [Imp][0] and some unpublished work of Dave
Long’s based on Hehner’s _Practical Theory of Programming_.)

[0]: https://scattered-thoughts.net/writing/imp-sets-and-funs/

Consider N-ary relations like those of the relational algebra, treated
as sets of equal-arity tuples.  (Maybe they could be bags instead of
sets; I’m not sure.)  It’s convenient to assume some set of atomic
items to make these tuples out of, such as words, symbols, or numbers.
We can treat an atom as a degenerate relation: `a` is taken to be the
relation consisting of a single tuple containing the atom `a`.

From these atoms we can build nonempty single-column relations with a
union operator `+`: `a+b+d` is a single-column relation consisting of
three one-item tuples `a`, `b`, and `d`, in no particular order, so
it’s equal to `a+d+b` or `d+b+a`.  (If we rule out multisets, it’s
also idempotent, so `a+b+d+a+b+d` is also equal.)

By adding a cartesian-product operator with higher precedence, written
simply with juxtaposition, we can build multiple-column relations: `x
y z` is a three-column relation consisting of a single tuple with the
atoms `x`, `y`, and `z`, in that order.  This operator is associative,
so `(x y) z` is equal to `x (y z)`, but not commutative; the order of
columns matters, so, for example, `y z` ≠ `z y`, and `x y z` ≠ `x z
y`.

We give the implied operator of juxtaposition cartesian-product
semantics simply by declaring that it distributes over `+`, so `(a +
b) (c + d)` = `a (c + d) + b (c + d)` = `a c + a d + b c + b d`.  This
also gives us a normalization procedure for relations built up in this
way, which makes equivalence decidable.

Now we can introduce identity elements for these two operations;
capitalizing the names from Imp, we can declare that None is a
relation with no rows, and Some is a relation containing only the
empty tuple.  (A different choice of notation might use {} for None
and () for Some, or α for Some and ω for None.)  For any relation X,
`None + X` = `X`, and `Some X` = `X Some` = `X`.  I think it’s
provable from this that `None X` = `X None` = `None`, but if not,
let’s postulate it — it’s obviously necessary for juxtaposition to
give us the usual kind of cartesian product.

We’ve said that we’re interested in sets of *equal-arity* tuples, but
there’s nothing stopping us from writing `a + b c`, though that has a
straightforward interpretation as a set containing a 1-tuple and a
2-tuple.  For the time being we’ll just consider such expressions as
being uninteresting due to being “ill-typed”, but clearly enough if we
leave them in with that interpretation, we have the
Kleene-closure-free regular expressions.

This is nearly a Boolean algebra, with juxtaposition for ∧, `+` for ∨,
None for 0, and Some for 1; but the ∧ of a Boolean algebra must be
commutative, and it’s not clear to me how to define ¬ such that *a* ∨
¬*a* = 1 and *a* ∧ ¬*a* = 0 (`X + !X = Some` and `X !X = None`).

It *is* a semiring, though, at least if we sweep the “typing” problem
under the rug; we have associativity of both operators, commutativity
of `+`, distributivity, identity elements, and annihilation.  In fact,
it’s pretty much just the free semiring on whatever our atoms are.  If
we rule out multisets, it’s the free idempotent semiring, which
induces a partial order on the operations.

The two operators above are two of the five primitive operators of
Codd’s relational algebra; the other three are selection, projection,
and set difference (set intersection being derived from union and
difference).