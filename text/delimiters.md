Suppose you’re parsing a token stream containing nested delimiters,
like (a b (c (d) e ((f g))) h), storing the tokens as you go, and
you’d like to store information about the nesting structure in the
stored tokens themselves, which are of some fixed size.

You can clearly get by with a previous-sibling pointer and a
previous-parent pointer, populated online as you parse the string, if
you’re going to traverse the string backwards; on close delimiters,
you could repurpose the previous-parent pointer as a last-child
pointer, since if you want the parent you could just follow the
previous-sibling pointer to the matching open delimiter and use *its*
parent pointer.  When adding a close delimiter and thus ending a
level, to find the matching open delimiter, simply leap to the last
delimiter or delimiter pair within the level now ending and ask them
for their parent; when adding a new open delimiter, look at the
previous delimiter, and if it was a close delimiter, it is your
sibling and tells you your parent; if it was an open delimiter, it is
your parent and you have no siblings yet.  This permits building the
structure in linear time with only a single pointer to leap over the
trailing non-delimiter tokens with.
