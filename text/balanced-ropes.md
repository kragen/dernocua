Is there a really simple way to balance ropes?

Basic ropes
-----------

I wrote [a simple implementation of ropes last night in 45
minutes][0]:

    #!/usr/bin/python3
    from collections import namedtuple
    from functools import cached_property  # 3.8 or later


    def as_rope(obj):
        return obj if isinstance(obj, Rope) else Leaf(obj)


    class Rope:
        def __add__(self, other):
            return Concat(self, as_rope(other))

        def __radd__(self, other):
            return as_rope(other) + self

        def __str__(self):
            return ''.join(self.walk())


    class Leaf(Rope, namedtuple("Leaf", ('s',))):
        def __getitem__(self, slice):
            return Leaf(self.s[slice])

        def __len__(self):
            return len(self.s)

        def walk(self):
            yield self.s


    class Concat(Rope, namedtuple("Concat", ('a', 'b'))):
        def __len__(self):
            return self.len

        @cached_property
        def len(self):
            return len(self.a) + len(self.b)

        def walk(self):
            yield from self.a.walk()
            yield from self.b.walk()

        def __getitem__(self, sl):
            if sl.start is None:
                sl = slice(0, sl.stop)

            if sl.stop is None:
                sl = slice(sl.start, len(self))

            if sl.start < 0:
                sl = slice(len(self) + sl.start, sl.stop)
            if sl.stop < 0:
                sl = slice(sl.start, len(self) + sl.stop)

            # Important special case to stop recursion:
            if sl.start == 0 and sl.stop == len(self):
                return self

            a_len = len(self.a)
            if sl.start >= a_len:
                return self.b[sl.start - a_len : sl.stop - a_len]

            if sl.stop <= a_len:
                return self.a[sl]

            # At this point we know we need part of a and part of b.
            # Since slicing a leaf creates a Rope, we can blithely just do this:
            result = self.a[sl.start:] + self.b[:sl.stop - a_len]
            # Avoid making Concat nodes for lots of tiny leaves:
            return Leaf(str(result)) if len(result) < 32 else result

[0]: https://news.ycombinator.com/item?id=28885929

Improvements
------------

The main critical flaw here is the problem of unbalance: if you append
a byte to something in a loop, you end up with a radically unbalanced
tree, so you will run out of recursion space trying to traverse it,
and also some operations that ought to be logarithmic-time become
linear-time.

It occurred to me that the code would be better if we put most of the
hairy logic down in the concatenation code instead of the slicing
code.  Empty string plus X?  X.  X plus empty string?  Also X.  X + Y
when the result is short?  A new leaf.  This would also avoid the
construction of suboptimal trees by non-slicing means.

### Weight-balanced trees ###

Can we solve the unbalance problem the same way?  In a concatenation
node X + Y, if we want to concatenate Z, we can improve balance by
choosing whether to parenthesize (X + Y) + Z or X + (Y + Z).  It seems
that we should perhaps choose whichever split will be more even: the
former if len(X) + len(Y) ≤ len(Z), the latter otherwise.  It might be
better to have a bias toward the former, which doesn’t involve
visiting the child nodes of X + Y, so maybe the criterion should be
something like len(X) + len(Y) ≤ 2×len(Z).  And of course we have the
symmetrical procedure for concatenating some X onto concatenation node
Y + Z.  This amounts to balancing a binary tree with single rotations.

(In an OO language like Python, implementing this by overriding
concatenation for Concat nodes is appealing, since the children are
readily accessible and no explicit check for leaves is needed; but
then you need some kind of double dispatch to handle the case of
prepending a byte onto a giant tree.)

Constructing all our concatenation nodes in this way would seem to
ensure that the depth of the tree is logarithmic, because descending
one level in a tree thus constructed always rules out at least ⅓ of
the bytes that were left over, so at most you have to descend
log(N)/-log(⅔) levels: at most 12 levels for 128 bytes (assuming at
least one leafnode per byte), at most 27 levels for 65536 bytes, at
most 55 levels for 4 gibibytes, etc.

But the very simplicity of the solution makes me suspicious of it: if
maintaining a balanced binary tree were that simple, surely someone
noticed this before 02021?  Because I think it’s applicable to binary
search trees, too, not just ropes.  This approach must have some
killer disadvantage for people to have invented AVL trees, B-trees,
2-3-4 trees, red-black trees, splay trees, treaps, and so on.  What’s
the catch?

This structure, or a slight variation on it, seems to be known as a
[weight-balanced tree][1], and normally it also requires double
rotations.  (See below about this.)

[1]: https://en.wikipedia.org/wiki/Weight-balanced_tree

It seems straightforward that we can assure the weight-balance
property whenever we do a concatenation in the way I described above,
and that this will ensure that slicing is logarithmic time.  (Possibly
slicing would be simpler if decomposed into a prefix-removal operation
and a suffix-removal operation, or perhaps a single split-at-point
operation, but almost certainly slower.)  That eliminates the
possibility of a fatal flaw in traversal and slicing, leaving only the
possibility that concatenation itself according to this algorithm is
fatally flawed by taking more than logarithmic time.

But that won’t be the case either.  When we’re appending two trees A +
B, we only recurse down the right edge of A and the left edge of B,
and we only do an O(1) amount of work at each node, so we also have a
logarithmic bound on concatenation.

### Splitting middle concatenees ###

Aha!  I think I found the fatal flaw with this simple approach: in (X
+ Y) + Z, Y might be 1048576 bytes while X and Z are one byte.  So
moving Y to one side or the other doesn’t help; you might have to
split it.  Of course that presupposes that (X + Y) already violates
the balance condition, but if #X = 32, #Y = 64, and #Z = 32, you have
a transition from the balanced state into the unbalanced state.  So
sometimes you need to split Y, which takes logarithmic time rather
than constant time.  (And this reinforces the suggestion of building
slicing out of splitting rather than vice versa.)

Can you use *only* such splitting?  That is, if a concatenation would
violate the balance condition, can you just split the larger
concatenee in half, instead of rotating?  I think the answer is yes,
but the cost might be O(lg² N) concatenation, because you could
potentially end up splitting a whole bunch of right-edge nodes in
half for a single concatenation.

The standard approach here is to use double rotations, where instead
of considering three concatenees X + Y + Z you consider four W + X + Y
+ Z, which can be concatenated as ((W + X) + Y) + Z, (W + X) + (Y +
Z), (W + (X + Y)) + Z, W + ((X + Y) + Z), or W + (X + (Y + Z)).
WX+Y+Z+, WX+YZ++, WXY++Z+, WXY+Z++, WXYZ+++.