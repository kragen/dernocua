Avery Pennarun’s bupsplit and Silentbicycle’s Jumprope, used in his
[Tangram][1] filesystem, are something like a hash-consed
general-purpose rope structure.

[1]: https://github.com/silentbicycle/tangram/

It occurred to me that by extending this approach, you can build a
string type that supports in-practice-constant-time concatenation and
comparison operations, at least in the absence of adversarial input.
Traversal is linear time; extracting substrings by numeric byte
position is logarithmic.

Hash consing
------------

Hash consing is an interesting technique: it allows you to reduce all
equality comparisons to pointer comparisons, extending the magic of
garbage collection, which lets you reduce all copying of (immutable)
values to copying of pointers, to equality comparison.  This is
clearly very desirable for hashing and associative storage: you can
hash the pointer, for example by interpreting it as an integer, rather
than the data structure, thus obtaining constant-time indexing of
properties by arbitrarily complex data structures.

Recent advances in hashing, such as cuckoo hashing and [Robin Hood
hashing][0], reduce some of the historical downsides of hashing.

[0]: https://www.sebastiansylvan.com/post/robin-hood-hashing-should-be-your-default-hash-table-implementation/

Hash consing is not called that because it’s useful for hashing,
though, but because you have to hash the values you’re consing in
order to find out whether the cons already exists.  If it does, you
just return it, rather than allocating a duplicate.

Ropes
-----

Ropes represent strings as, basically, the fringe of an arbitrary cons
tree structure, typically with the size of each subtree cached at each
node.  This permits linear-time traversal, logarithmic-time indexing
by byte offsets, and constant-time concatenation.  However, if we want
to use hash consing for ropes, we have a problem; string concatenation
is supposed to be associative: "a" || ("b" || "c") == ("a" || "b") ||
"c".  If we just use regular hash consing with ropes, we may end up
with lots of duplicate ropes that represent the same string.

Lua hashes a new string in constant time: at least in Lua 5.2,
`luaS_hash` examines at most 32 bytes of the string in order to
compute its hash value.  But it can’t *construct* the new string in
constant time, or usually constant time, because it has to copy all of
its bytes.  Similarly, it can’t test strings for equality in constant
time, or even usually constant time—even if their hash values are
equal, it has to iterate over all their bytes.

The Jumprope approach is to use a rolling hash to split the string
into chunks in a consistent way, so that strings that contain common
substrings will usually split into the same chunks.  But Jumprope does
not aspire to support string concatenation or, I think, constant-time
string comparison.

Monoidal hash functions
-----------------------

Here’s one way you could get *usually* constant-time string
concatenation and always-constant-time string equality tests.  You
compute the hash used for cons hashing in such a way that equivalent
ropes will always have the same hash value, even if their internal
structure is different.  This is done by choosing the hash to be a
monoid under a constant-time operation applied at concatenation time.

A particularly appealing kind of monoid for this purpose is functional
composition of linear forms *mx* + *b*; the hash of the concatenation
of string *s*₀ with hash *m*₀*x* + *b*₀ and string *s*₁ with hash
*m*₁*x* + *b*₁ is then *m*₁(*m*₀*x* + *b*₀) + *b*₁ = (*m*₁*m*₀)*x* +
(*m*₁*b*₀ + *b*₁).  So to compute the hash of the concatenation of the
tuples (*m*₀, *b*₀) and (*m*₁, *b*₁), we just compute (*m*₁*m*₀,
*m*₁*b*₀ + *b*₁).  Since the empty string is the identity element of
the string-concatenation monoid (which is the free monoid on the
characters) the hash of the empty string must be (1, 0), while the
hashes of the characters can be chosen to be anything convenient, such
as (3, c).

It isn’t necessary for the multiplication and addition operations here
to be integer multiplication and addition, and in fact it’s
undesirable, because integers can be arbitrarily large, and we want
our hash values to be of constant size, and the computation of their
composition to be constant-time.  We only need the addition and
multiplication operators to be associative, the multiplication to
left-distribute over the addition, and for them both to have identity
elements (written 1 and 0 above); that is, they each need to be a
monoid, with one left-distributing over the other.  The usual approach
in such cases is to use “machine integers”, say multiplication and
addition mod 2⁶⁴, and that would work fine here.  Reducing modulo a
large prime, such as 2⁶⁴ - 59, might be advantageous, in order to keep
bits well mixed.  Vectors or matrices would work too.

But any semiring with identity (and in particular any ring and any
field) would work; we don’t even need the addition operation to be
commutative, as semirings guarantee.  Rings in general will tend to
work better, because the addition operation of a ring is
information-preserving, so you can’t end up in a trap where all
strings with a given prefix have the same hash.  (Idempotent semirings
and especially tropical semirings would probably be bad choices.)
Multiplication in a ring isn’t information-preserving, so with the
above it’s possible to get into a trap where all the strings with a
given *suffix* have the same hash, or where a lot of information is
lost, but this should generally be easy to avoid; when the
multiplicative inverse exists for nonzero elements, for example, you
just need to prevent the hash of any primitive rope from containing a
0 multiplier.

It might be desirable to prevent an adversary from choosing strings to
produce a high collision rate, and the linearity of this simple family
of monoids might pose a problem for that.

In some sense you could use a much more general function, such as
secure hash functions using the Merkle-Damgård construction, but it’s
really desirable to use sets that have some kind of constant-size
representation that can be efficiently composed.  The whole idea of
the Merkle-Damgård construction is to limit that kind of thing.
[Infogulch suggests that random invertible matrices over finite
fields][3] ([Julia notebook][2]) might provide an answer, but others
suggest that it would probably be easy to break:

> Consider an ordered sequence of elements *aₙ*, a function *h* that
> derives an invertible matrix over finite field 𝔽₂₅₆ from a single
> element’s cryptographic hash, and a function 𝐻 that finds the
> product of all such matrices from a sequence:
> 
> 𝐻(*a*)=∏*ⁿᵢ*₌₁*h*(*aᵢ*)
> 
> Define 𝐻(*a*) to be the hash of the sequence *aₙ*.

[3]: https://math.stackexchange.com/questions/4200988/using-random-invertible-matrices-over-finite-fields-to-define-the-hash-of-a-list
[2]: https://archive.fo/lpgal

Rope append algorithm
---------------------

So, to concatenate two ropes in this scheme, you first compute the
hash of the concatenation, then check to see if a rope with that hash
already exists.  If so, you must check to see if it is actually equal;
in most cases, this will be rapid, because you won’t have to descend
very far down the respective trees to decompose them into nodes of the
same size, which can simply be compared by pointer.  If it is actually
equal, you can simply return the existing rope; otherwise, you must
allocate the new concatenation.

An alternative approach to checking for equality in such a
candidate-equality case is to slice the candidate new rope into new
candidate ropes.  If the existing rope is (A || B) and the new
candidate rope is (C || D), then either #A == #C, #A < #C, or #A > #C.
If #A == #C it is sufficient to compare the identities of A and C, and
B and D.  If #A < #C, then we can continue by constructing C[:#A] and
comparing its identity to A’s; if they are equal, then we construct
C[#A:] || D and compare it in the same way to D.  Analogously,
when #A > #C, we can check whether C || D[:#A-#C] would be equal to A,
and if so, check whether D[#A-#C:] would be equal to B.

This would seem to pose a troubling problem of infinite regress: to
construct a new rope, we must apparently construct three more new
ropes, and, worse, these extra new ropes might sit around in the hash
cache and waste space until they get garbage collected.  I think
that’s one way to solve the problem, but maybe a better way is to
“proto-construct” these ropes but not stick them into the table; I
think this reduces to the approach of traversing both trees in
parallel.

In the usual case, if we approximate the hashes as random, the
probability of a hash collision is on the order of 2⁻¹⁰⁰ or lower, so,
with a reasonably good hash function, such double-checking deep
comparisons will almost always return true; new strings will almost
always have new hashes.  Even if the root has an equal hash, its
children almost certainly won’t (except in the case of an intentional
attack).  So maybe it isn’t worth worrying too much about how many
ropes get allocated in those cases, except to bound the cost to
logarithmic.

Here, I’m supposing that each concatenation node includes a left
pointer, a right pointer, two 64-bit words of hash, and a length
field, so about 5 words, 40 bytes.  On a 32-bit machine maybe it would
be 20 bytes.  You might need another word if you can’t steal a bit for
a type field somewhere, either in the node pointer or from one of the
words.

Input splitting and leafnode coalescing
---------------------------------------

When importing bytestrings into the hash-consed-rope system, you can’t
get any storage sharing if you just import them as single leafnodes.
You could imagine, for example, importing two versions of this
Markdown file into the system as two strings, one before and one after
inserting a blank line at the beginning.  Ideally you would like these
two versions to share most of their storage.

Now, if you construct the second version within the system, by
appending the old version to a newline character, then you get storage
sharing automatically, like the Ent of Xanadu.  But what if you don’t?
What if someone sends you the second version over a network?

Jumprope and bupsplit have an answer here: run a rolling hash over the
file (a hash like the CRC, that’s not just monoidal but has an
inverse), and use some criterion on the rolling hash to pick out a
hierarchy of special cut points determined by their surroundings.

If you have working hash consing of ropes, though, I don’t think
that’s necessary; you just need some way of splitting big input blobs
into leafnode chunks of about 64–512 bytes that tends to reproduce the
same cut points when it encounters the same data in different
contexts.  After that, the size of the rope tree internal nodes is
going to be relatively small, maybe 20% of the size of the leaf nodes,
and if you build it in a relatively random and balanced way, you’ll
probably be able to share a fair bit of that, too.

One simple approach is to start with a counter at 576 and decrement it
every byte, then split and reset the counter when encountering a byte
whose value is more than half of the counter value.  So the byte ‘a’,
whose value is 97, will start a new block if the counter is less than
194, setting the counter back to 576.  This clearly guarantees chunks
of 64–576 bytes, and it will clearly stay resynchronized if it ever
manages to split in the same place (which is likely), but the average
block size will depend on the data — if it’s all zero bytes, it’ll be
576 bytes per block, and if it’s all 0xff bytes, it’ll be 64.  In
Python:

    def split(infile, maxsize=576):
        i = maxsize
        buf = []
        while True:
            c = infile.read(1)
            if not c:
                yield ''.join(buf)
                break

            i -= 1
            if ord(c) * 2 > i:
                i = maxsize
                yield ''.join(buf)
                buf = []

            buf.append(c)

You could take some steps to whiten the distribution a bit; for
example, you could use the sum of all the bytes in the block so far
mod 256, which will still have a much higher probability of creating a
break at a ‘y’ than at a ‘!’, or you could use the sums or bitwise
ANDs of pairs of adjacent bytes.  All such measures are necessarily
trading off consistency of split location against consistency of split
frequency.

On similar economic considerations, when you’re concatenating small
ropes, say less than 64 bytes, it’s probably worth it to just copy the
bytes into a new leafnode.  This means that if you’re typing into a
hash-consing-rope editor, you’ll be allocating a new leafnode of 16-72
bytes on every keystroke (averaging 44 bytes), which is clearly 44
times slower than it needs to be, but still better than allocating a
16-byte leafnode *and* a 40-byte concatenation node.  (Of course you
also need to allocate another couple of concatenation nodes that join
the new character to the previous and following parts of the editor
buffer, but that’s true whether the keystroke is in a leafnode of its
own or not.)

Along the same lines, it’s probably good to coalesce concatenation
nodes into a B-tree to some degree; a 4-child concatenation node would
have a length, two words of hash, and 4 child pointers, 7 words.  If
you built it out of binary concatenation nodes, you’d need three
5-word concatenation nodes, 15 words, more than twice as much space.