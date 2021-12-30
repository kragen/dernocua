Suppose you divide a text into consecutive four-byte windows.  If the
text is not a multiple of four bytes long, one of the windows will not
be full; traditionally we pad at the end, but we can also pad at the
beginning.  There are four ways to do such sequence alignment.  If we
hash the text in each of these windows into some alphabet, perhaps one
large enough that hash collisions are improbable, each of these window
alignments converts the text into a text from a larger alphabet with
one fourth the length.

At this point we have converted the original N-byte text into four
N/4-letter texts; call them “first-level summaries”.  Suppose that we
choose only three of these, for a total of 3N/4 letters.  Repeating
the process on each of the 3 first-level summaries gives us 9
second-level summaries, each 1/16 the size of the original text
(though in a larger alphabet) by repeating this until we are reduced
to a single letter, we end up with (almost) 3N hashes for different
parts of the text, each computed over four letters, so this process
takes linear time.

Suppose the text consists of two copies of some motif concatenated.
Then the hashes in the first level will be mostly the same.  If the
original motif is a multiple of 4 bytes, *all* the hashes in the
first-level summaries will be the same, except those overlapping the
boundary; but if not, then the second copy of the motif will be
byte-misaligned.  Suppose that the misalignment is 1; then, the hashes
in first-level summary #1 of the first copy of the motif will be found
a second time in first-level summary #2 of the second copy, those of
first-level summary #2 of the first copy will be found in first-level
summary #3 of the second copy, while the hashes in first-level summary
#1 of the second copy and first-level summary #3 of the first copy
will not be found again.  The other possible misalignments, 2 and 3,
have similar properties: two thirds of the hashes in the first-level
summaries will occur twice.

In higher-level summaries we have the same sort of property, that a
repeated motif results in two or three repeated sequences of hashes in
the summaries of all levels small enough for the plaintext of the
motif to be entirely contained inside a single hash at the next level
up.

By starting at the topmost level summary and working down, we can
efficiently detect duplicate text of any length anywhere in a corpus
--- in linear time, if we treat hash-table probing as constant time,
or linearithmic time in a more realistic scenario.  This provides an
efficient solution to the basic version of the sequence alignment
problem, the rsync problem (without using sliding hashes), and, I
think, the diff-with-rearrangement problem.

A given 4-byte substring is not guaranteed to be covered by a hash in
the first-level summary, but of the two 4-byte substrings of a given
5-byte substring, one or both will be.  Similarly, in a 17-byte
substring, one or both of its two 16-byte substrings will be covered
by a 4-letter substring in the first-level summaries, which may or may
not have a hash in the second-level summary, but a 5-letter substring
in the first-level summaries is guaranteed to have one, and every
21-letter substring of the original string is thus guaranteed to
contain at least one second-level hash.  So the maximal size of an
unrepresented substring in a given summary level proceeds by this
logic of f(i) = 4f(i-1) + 1: 5, 21, 85, 341, 1365, 5461, 21845, 87381,
349525, 1398101, etc.

(There might be some way to stagger the skipping across summaries to
get this series to increase a little slower.)

I think that, by this scheme, you would add 15 level of summary to a
gibibyte of text, as follows:

* 1,073,741,824 bytes of text;
* 805,306,368 hashes, 6,442,450,944 bytes in 8-byte hashes, each
  covering 4 bytes;
* 603,979,776 hashes, 4,831,838,208 bytes in 8-byte hashes, each
  covering 16 bytes;
* 452,984,832 hashes, 3,623,878,656 bytes in 8-byte hashes, each
  covering 64 bytes;
* 339,738,624 hashes, 2,717,908,992 bytes in 8-byte hashes, each
  covering 256 bytes;
* 254,803,968 hashes, 2,038,431,744 bytes in 8-byte hashes, each
  covering 1024 bytes;
* 191,102,976 hashes, 1,528,823,808 bytes in 8-byte hashes, each
  covering 4096 bytes;
* 143,327,232 hashes, 1,146,617,856 bytes in 8-byte hashes, each
  covering 16384 bytes;
* 107,495,424 hashes, 859,963,392 bytes in 8-byte hashes, each
  covering 65536 bytes;
* 80,621,568 hashes, 644,972,544 bytes in 8-byte hashes, each covering
  262,144 bytes;
* 60,466,176 hashes, 483,729,408 bytes in 8-byte hashes, each covering
  1,048,576 bytes;
* 45,349,632 hashes, 362,797,056 bytes in 8-byte hashes, each covering
  4,194,304 bytes;
* 34,012,224 hashes, 272,097,792 bytes in 8-byte hashes, each covering
  16,777,216 bytes;
* 25,509,168 hashes, 204,073,344 bytes in 8-byte hashes, each covering
  67,108,864 bytes;
* 19,131,876 hashes, 153,055,008 bytes in 8-byte hashes, each covering
  268,435,456 bytes.

(Actually, I think I’m slightly overestimating the higher levels
because I’m omitting the hashes that would be hashing entirely missing
data off the end of the file.)

This is 26,809,069,296 bytes, about 25 gibibytes in all, the original
gibibyte plus almost 24 gibibytes of summaries.  If you are only
interested in finding large coincidences, more than 5, 21, 85, 341, or
1365 bytes, you can discard the first few levels of summaries, saving
you most of those gibibytes.

The hash function you use needs to be reasonably good to avoid false
positives.  If you’re willing to accept a small false positive rate,
you can use a smaller hash, such as 4 bytes.  Collisions only matter
within a summary level, so it might be reasonable to use smaller
hashes at higher levels.
