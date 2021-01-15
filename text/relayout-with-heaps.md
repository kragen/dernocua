I was just writing a table editor in Python.  Modern machines are
fast, so simple brute force was sufficient to instantly recalculate
the typewriter width of each column in the redraw:

    def redraw(self, output):
        widths = [max(1, max(len(s) for s in col)) for col in self.contents]
        output.write('\033[2J\033[0H') # clear screen, home
        ...

Until I loaded a two-megabyte file with 100k rows and 400k cells into
it, anyway, and redraw started taking a noticeable fraction of a
second.

There are a lot of ways you can change the problem to make it easier.
You can divide your table into pages with independently varying column
widths.  You can compute column widths with a 512-row window around
the cursor that moves in big jumps with a little hysteresis.  You can
require the user to set the column widths manually.  You can render
the display immediately with the outdated column width, recomputing
the correct column width in the background, and update the display
again when you’re done.  You can cache the column widths, only
recomputing them after a change.

But most changes — the vast majority, in fact — don’t change a column
width, so you can do better than just recomputing the column width
after a change.  If you make a cell narrower, it only changes the
column width if it was previously of the maximal width in the column,
and no other cell is still that maximal width.  If you make it wider,
it only changes the column width if it becomes wider than the previous
column width, and then its new width is the new column width.

So, even though the column width depends on every cell in the column
(100k cells in this example) a custom cache invalidation strategy can
eliminate most column-width recomputations and make many others
trivial: the new column width is the cell’s new width.  But there’s
still a case where you need to do a potentially expensive computation:
where you’re making the cell so narrow that it’s narrower than the
column.  You need to figure out what the new narrow cell is.

Previously I’ve written about computing such semilattice reductions
incrementally using the standard parallel or incremental prefix-sum
algorithm, which gives you a logarithmic-time way of finding the new
maximum.  In this case, for example, you could have a 17-level perfect
binary tree of maximal cell widths, each node annotated with the
larger cell width from its two children, with the overall maximal
width at the base; whenever you increase or reduce a cell width, you
propagate that reduction up the tree, potentially all the way to the
root, requiring only 17 pairwise max operations in the worst case, but
only about two in the average case.

But it occurred to me that a possibly different approach is to build a
max-heap over the cell widths.  If a binary heap (rather than, for
example, a Fibonacci heap), this is also a perfect binary tree, but
because it the widths it keeps in internal nodes are not duplicated in
leaves, it’s half as big, and is thus only 16 levels deep.  It also
requires about two operations in the average case, this time
comparisons and conditional swaps.

One tricky bit is that it isn’t sufficient to just keep the widths
themselves in the heap; we need a bit more metadata in order to be
able to update them.  There are a couple of different approaches.
First, we can make the heap items into (width, cellindex) pairs,
inserting a new one every time a cell changes width; and, when we
consult the one at the top of the heap, we we check to see if its
width is still up to date, and if not, we discard it and check the
next one.  Second, we can mutate the items within the heap,
maintaining an index into the heap in the cell structure itself, with
which to find its corresponding heap item and sift it up or down as
appropriate; this index must be updated whenever the heap item is
shouldered aside by a larger cell sifting up, or promoted by a smaller
cell sifting down, so the heap item also needs a pointer back to the
cell structure in this case, so it still needs to contain the
cellindex, though it no longer needs to contain the width itself.

Note that, unless the cellindex is smaller to store than the width,
this eliminates the apparent twofold size advantage of the bin-heap!

The heap approach also requires a total ordering on its keys, so it’s
*less general* than the reduction prefix-sum tree, which can work on
more general semilattices as well as other monoids and even I think
semigroups.

Reasoning in the opposite direction, the semilattice-reduction
prefix-sum tree would seem to provide a viable logarithmic-time
implementation of a priority queue, which will be cheaper if the items
in the priority queue need to be addressable by something other than
priority — process ID, for example, or table cell index.  If you have
a hash table of scheduled events, for example, you should be able to
maintain a perfect binary tree of earliest scheduled events in various
2*ⁿ*-sized subsets of the hash buckets.  This will obviously be costly
if most of the hash buckets are empty, but with modern hashing
techniques like cuckoo hashing, the number of empty buckets can be
kept very low.

So, is there ever a reason to use a binary heap?  Heapsort is an
in-place worst-case linearithmic comparison sort, and I don’t think
you can do that with this prefix-sum tree thing.  But I think the
usual priority-queue problems can be solved just as well with the
prefix-sum-tree approach.