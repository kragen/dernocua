Heapsort’s initial heapification phase is linear time, while its
sorting phase is linearithmic.  One common reason for sorting things
is to see the first N items; heapsort, unlike quicksort, mergesort, or
library sort, can produce those top N items much sooner than it can
produce the rest of the sorted results.

Heapsort’s laziness
-------------------

I wrote a simple heapsort program that generates random integers and
heapsorts them.  For ten items, it takes 4-7 swaps to initially
heapify them, then 21-25 swaps to finish sorting; for a hundred, 64-74
swaps and 500-520 swaps respectively; for a thousand, 700-740 and
8300-8400; for ten thousand, 7400 and 120 thousand; for a hundred
thousand, 74 thousand and 1.5 million; for a million, 740 thousand and
18 million; for ten million, 7.4 million and 220 million; for a
hundred million, 74 million and 2.5 billion.  The heapifying phase
does about 4.7 record compares per swap, so about 3.5 per input
record.

So, even with very small input sets, heapsort can generate the first
output value in only 20% of the time required to generate the whole
output set (though admittedly at this scale insertion sort is probably
faster), and for reasonable-sized results, the difference is more than
an order of magnitude, with the heapifying phase going as low as 3% of
the total.  Moreover, it takes only about 3.5 comparisons per input
record, plus a logarithmic number per output record.

This is relevant if you’re writing a sort utility that generates
output lazily, as when the shell `sort` command is piped to some other
command.  This laziness-friendliness seems like a relevant attribute
for a generic standard-library sorting routine or toolkit: by
heapifying a data array into a max-heap and then performing a few
extract-max operations, we have a top-N algorithm.

If you know at the outset how many output values you’re going to need,
you can do better than this by iterating over the input values,
conditionally adding them to a “shortlist” heap of the right size,
from which future values may possibly evict them.  In the case where
most values never make it onto the shortlist, it’s easy to keep the
number of comparisons per input record below 1.2, but of course it
cannot go below 1.

Can we improve heapsort’s locality of reference?  An idea that fails
--------------------------------------------------------------------

Normally heapsort has relatively poor locality of reference, making it
unusable for external sorting.  This has probably already been
investigated, but I think this can be cured by dividing the heap into
smaller heaps connected by queues.

Suppose you have 256 GiB of 16-byte records (16 gibirecords) to sort
in 16 GiB of RAM (1 gibirecord).  Your auxiliary storage is a tebibyte
SSD, which takes 100 μs to do a 4096-byte read or write, potentially
containing 256 records.

One way to approach this problem is to build a bunch of 255-record
min-heaps, each associated with a 255-record queue containing records
that precede its top (minimal) record.

First, consider the output phase: we repeatedly consume a record from
the root queue.  When a queue goes empty, we refill it from the heap
dangling off of it by repeatedly removing minimal items from that heap
and appending them to the queue.  This usually involves sifting up
items that we would normally find in child heaps, but in this case the
child heaps are at the other end of their own queues, so unless one of
those queues goes empty, we only need the root queue, the root heap,
and its 255 (?) child queues in RAM, a total of 2056 kibibytes.

However, every item added to the output queue shifts an item into the
root heap from one of those child queues, which has a 1/255 chance of
going empty.  At that point, we need to refill that queue, so we
temporarily switch to refilling that queue by draining 255 items from
its heap, each of which has a 1/255 chance of emptying one of *its*
child queues, unless it’s a leaf node.  So on average we will recurse
all the way down to the leaves when we empty the root’s output queue,
but only once; sometimes we’ll get lucky and end the recursion early,
and sometimes we’ll get unlucky and have to recurse down to the leaves
two or three times.

Draining a leaf node in this way only requires 4 KiB of RAM buffer
instead of 2056 KiB.  (Its empty queue was already in RAM because its
parent node was draining it.)

Each heap+queue node holds 512 records, so we need 32 mebinodes; with
255-way branching, these are about 3e-6% the root node, 0.0008% its
children, 0.2% the third level, 49.4% the fourth level, and 50.4% the
fifth level.  The first three levels (and 6% of the fourth level) fit
in RAM, so every time we drain the root queue and recurse down to our
on-average-one-leaf, we’re paging in 50.4% of the time a fourth-level
2052-kibibyte node with all its child queues, plus one of the
fifth-level leaf nodes.  So we need, I think, 515 iops, 51.5
milliseconds, every other time we drain the root queue, which is about
1 iops per record, which is... still unusably slow.  If I’ve
calculated this correctly, it’ll take us 20 days to sort our data file
this way.

By contrast, we can trivially mergesort the data file in two passes:
one to divide it into (worst-case) 16 16-gibibyte internally-sorted
hunks, and a second pass doing a 16-way merge.  That’s a little less
than 4 hours.
