You can serialize a data structure in a compact way that can be
efficiently interpreted by building it up on a stack, with pointers
into older parts of the stack, minimizing parsing and permitting the
fixup of pointers on input so that the final structure can be safely
traversed with no overhead.  This is a potentially interesting middle
ground between slow serialization formats like JSON and protobufs and
zero-parsing formats like FlatBuffers.

Now, the most basic thing you could do would be to have a big block of
literal binary data, then a “linkage table” that just lists all the
pointers in it, so that you can iterate through and offset each of
these pointers by adding a base pointer to it in place, and maybe
verify that it doesn’t point outside the block afterwards.
(Alternatively, you could do the offsetting when you follow the
pointers rather than when you load them.)  Import and export tables
are a simple addition to such a scheme.  This isn’t all that compact,
it’s not self-describing, and it's likely to have
backward-compatibility problems, but it sure is fast to load.

A somewhat less basic approach would use nested delimiters like JSON
or PDF for dictionaries and heterogeneous tuples, but counted
bytestrings for text or numerical arrays.  By using both opening and
closing delimiters for dictionaries and tuples, arbitrary nested
structures can be built in place, without fragmentation.  A linked
list of delimiter contexts can be interspersed with the actual data on
the stack to avoid any further allocation; and processing the closing
delimiter of a dictionary can create, for example, an
appropriately-sized hash table.

Referring to the same object more than once cannot be done with a pure
stack discipline.  The simplest way to handle this is probably with a
symbol table: a way to define a unique name or ID number as pertaining
to the next or previous object, and a way to insert a reference to
another object.  If this name-binding step is done at the end of
deserialization, or lazily when following references, rather than
during deserialization, it permits cyclic references as well as
multiple references.

In cases where data is being received byte by byte over a network or
serial port, it makes sense to allocate all the memory on the stack.
But if the data is mapped in from a memory-mapped file, it makes more
sense to build only an ‘index’ structure on the stack, with pointers
pointing to raw binary data in the mapping.

This still requires parsing work for each text string, though, as well
as each object.  A faster approach is to have a single bolus of all
the text and numerical data, followed by a list of offsets into it
defining where each blob starts, and then the graph structure of
arrays, dictionaries, and records represented with lists of object
IDs.  A final _coup de grace_ is to include the typing information
needed to decode the graph structure itself as a graph-structure item,
thus making the entire structure self-describing without inflating it
with redundant type tags, length fields, and field names.  The decoder
must traverse the type graph in sync with the object graph in order to
know how to interpret the bytes of each item.

But traversing such a file requires not only parallel type-graph
traversal, but also an extra indirection through the object ID table
on every reference traversal.  If the object IDs in the graph
structure are allocated x