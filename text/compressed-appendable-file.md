PDF is a mess because it tries to support incremental updates by way
of appending, random access, and compression, in a way that’s deeply
intermeshed with the application-layer data structures it uses and
unnecessarily inefficient as a result.  Each indirect object has an
identifying number that can be used to make references to it.
Indirect objects include independently compressed streams for the
contents of each page, and you have an xrefs table at the end of the
file that tells you the byte offset at which to find each indirect
object.

In PDF 1.5, they added compressed object streams containing a bunch of
non-stream indirect objects that all get compressed together, preceded
by a variable-length free-form header that gives the byte offset of
each indirect object in the decompressed stream, but of course the
objects don’t have byte offsets in the top-level file that could be
listed in the traditional xrefs table; instead they added a new xref
stream format which has type-1 xrefs (the traditional kind) and type-2
xrefs that give the object number of an object stream and an index
into it.

Despite all this, you still can’t compress the contents of multiple
pages together, so even with all the bells and whistles, PDF files are
still significantly bigger than the corresponding gzipped PostScript
files.

I think the right solution is a layer separation: generic data
compression should be provided by a layer underneath the application
data structures.  For example, a filesystem supporting transparent
compression would allow PDF files to just forget about compression
entirely, just using text and byte offsets and relying on the
filesystem to map byte offsets to the proper place in the
transparently decompressed data; and the files would occupy less space
than using the current PDF Rube Goldberg scheme.

Filesystem compression doesn’t help with network transmission, though.
For that you need a file format, implemented by a library.  But
efficient traversal of graph structure as in PDF requires random
seeks, and traditional compression libraries like gzip don’t support
random seeks.

This is pretty much the same problem the dictzip program from Rik
Faith’s dictd solves: it resynchronizes the gzip compression algorithm
every sub-64-K “chunk”, and provides a gzip-compatible format that
stores an “Extra Field” in the gzip header that tells how many bytes
each chunk compressed to, and how many bytes the chunks were
originally.  The man page reports that with 64kB chunks, the file is
only 4% larger than with unchunked gzip.

However, PDF files, like many other candidate uses for such a file
format (such as debug logs and database journals), need to be able to
append data to the end of the file.  I think dictzip can’t provide
this, because it would have to expand its header field with data about
the newly added chunks, which I think would involve shifting the data
in the rest of the file a few bytes to the right to make room.

PDF and PKZip both take the approach of appending a file “directory”
or “xrefs” trailer or footer that permits you to efficiently find
everything else in the file; in the case of a compressed bytestream
format, the only thing to find are the seekable compressed byte
offsets most closely corresponding to particular uncompressed byte
offsets.  The [.xz file format][0] also does this, including an
“Index” just before the “stream footer” which gives the compressed and
uncompressed size of each of the data blocks in the stream.  This
allows you to parse an .xz file backwards from the end to seek
randomly in it.

[0]: https://tukaani.org/xz/xz-file-format-1.0.4.txt

Moreover, an .xz file can consist of multiple concatenated streams:

    $ (echo hi | xz -9c; echo bye | xz -9c) | xz -dc
    hi
    bye
    $ 

So in theory you could use .xz as a compression format that supports
appending and random reads.  However, your reads (or opens) are going
to eventually take time proportional to the total number of appends
that have been done, rather than constant time, as is desirable.  And
if an append operation is interrupted, for example by a process being
killed or a server going down, it’s likely that the file will no
longer end with a stream trailer, eliminating the ability to read it
safely from the end.

If we add a single fixed-size field in the file *header* (like dictzip
does) that points at the latest trailer (unlike dictzip), we can
atomically update that field after appending a new commit to the file.
And all the stuff we append in a single commit can be compressed
together.