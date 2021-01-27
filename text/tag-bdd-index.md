Suppose you have some tags and want to index them.  My URLs file is
only about 4500 URLs, so for an interactive query sequential search
would be fine, but what if it wasn’t, because you had a much larger
database?

Each item has some set of tags.  A tag query consists of some set of
required tags and some set of forbidden tags, and the desired result
is the set of items that have all the required tags and none of the
forbidden tags; usually we want to be able to start iterating over the
result set as soon as possible.

So far this sounds trivial.  What makes it difficult is the Zipf
distribution and non-independence of tags.

I have about 2200 tags in my 5000-item URLs file, 1100 of which are
used only once; for example:

      1 #3D-XPoint
      1 #Alex-Jones
      1 #random-forest
      1 #dimensional-analysis
      1 #QR-codes
      1 #Data-General
      1 #CCC
      1 #digital
      1 #aurora
      1 #Steven-Universe

These are easy to handle: if they’re in the required set, a simple
inverted index directs you from the tag directly to its single hit,
and if they’re in the forbidden set, it’s adequately efficient to
check each tag in candidate items against a hash table of forbidden
tags.

But there are some tags that are used frequently:

    345 #hardware
    254 #paper
    217 #politics
    174 #history
    154 #USA
    144 #materials
    136 #PDF
    133 #pdf
    120 #security
    118 #toread
    112 #video
    103 #algorithms
    100 #ebook
     91 #human-rights
     91 #energy
     83 #performance

So, for example, #hardware has about 7% selectivity, and #paper about
5%.  Worse, these tags aren’t independent: only about 5% of all URLs
are tagged #paper, but 72 of the 133 #pdf URLs are, over 50%, according to

    grep '#pdf' urls | perl -lne 'print $1 while /\s(#[-\w]+)/g' |
        sort | uniq -c | sort -n

The set of all tags commonly grows almost linearly with corpus size,
but my intuition is that the set of *popular* tags like #politics
grows much more slowly.  The first 2200 URLs contain 1366 distinct
tags (4613 total), 0.62 per URL, while all 4578 URLs contain 2175
distinct tags (10269 total), 0.48 per URL.

Whether this is true depends on how you define “popular”.  If we take
an arbitrary cutoff point of 100, the full set had the 13 “popular”
tags above, while the first 2200 had only one “popular” tag (#paper).
If instead we say that a “popular” tag is one with 1% selectivity or
worse, then in the smaller set there were 25 “popular” tags, and in
the larger set there were 30.  If we draw the line at 0.5%, it’s 86
and 79.

We can build a tree over just the “popular” tags that enables
efficient enumeration of query results by a subdivision process.  Each
internal node has an associated tag, with one child for a subtree of
items containing that tag, and another child for all other items.
Several nodes may be associated with the same tag.  Leaf nodes are
associated with small sets of items.

The greedy approach
-------------------

We build the tree as follows.  First, if the set of items is too large
for sequential search to be desirable, take the tag that produces the
most even split between hits and misses, the one whose selectivity is
closest to 50%, #hardware above, and split the items.  Then repeat the
process recursively on the resulting two subsets.  So, for example,
within #hardware we have the following popular tags:

    345 #hardware
     26 #simulation
     22 #Arduino
     19 #PDF
     18 #reverse-engineering
     18 #history
     16 #display
     16 #cellphone
     16 #AVR
     15 #RISC-V

Here, #hardware no longer has useful selectivity (it’s 100%) but now
we have #simulation with 7.5% selectivity, so (if for the sake of
argument 345 is not small enough yet) we subdivide according to
whether #simulation is present or absent.

In the non-#hardware group, the ordering is pretty much unchanged,
except that the spuriously separate #PDF and #pdf tags have switched
places, #video has moved down the list, and #Trump has moved up:

    242 #paper
    217 #politics
    156 #history
    154 #USA
    141 #materials
    124 #pdf
    117 #PDF
    111 #security
    107 #toread
    103 #algorithms
    101 #video
     99 #ebook
     91 #human-rights
     89 #energy
     79 #Trump
     76 #performance

So we would subdivide with #paper; -hardware +paper is divided into
-pdf and +pdf, while -hardware -paper is divided into -politics and
+politics.  -hardware -paper -politics is unsurprisingly divided into
-history and +history, while +hardware +simulation is unsurprisingly
divided into -SPICE and +SPICE.  And so on.

The same tag can occur in more than one place; for example, both
-hardware +paper +pdf and -hardware +paper -pdf +PDF are divided by
the tag #toread.

To evaluate a query, we begin by querying the inverted index for all
the required tags; if any of them have an adequately small result set
for sequential search to be practical, we iterate over that result
set.  If not, then all of our required tags are “popular”, so we begin
to traverse the tree top-down.  When the tag associated with a tree
node is in the query, either as a required or a forbidden tag, we only
visit one of its children; otherwise, we visit both.

Ultimately each of the leaf nodes of this tree contains individually a
reasonable number of items to search, although this doesn’t
necessarily imply that the aggregate total of all the leafnodes to
search will necessarily be reasonable.  

Why the greedy approach fails
-----------------------------

A difficulty with this approach is that in some cases we will end up
reading through an entire subtree because a tag, though globally
popular, is unpopular within that subtree.  For example, the
intersection of #hardware and the lamentable #Trump tag is empty,
since Trump doesn’t know about hardware, so for the simple query
+Trump, the algorithm will have to sequentially examine all
345 #hardware items.  Even if there were one or two #Trump items in
there in a much larger set, it would never be a popular tag within
that context.

A non-greedy approach: BDD-like consistent choice order
-------------------------------------------------------

An alternative is to use a consistent order of tags throughout the
tree: divide the root by #hardware, its two children (if neither is
small enough to be a leafnode) by #paper, their four children (except
small ones) by #politics, and so on.  This avoids the catastrophic
worst case described above, but it probably means that the mechanism
can't handle more than about 4–8 popular tags.