What’s the simplest way to support the basic Unix filesystem
interface?  open, close, read, write, mkdir, chdir, lseek, and fstat,
supporting append, random-read, random-write, and random-readwrite
modes.  If you were willing to sacrifice efficiency for simplicity.

You need file-descriptor objects with offsets and modes, and then the
actual directories, and a CWD for your filesystem cursor.

Probably the simplest solution in a garbage-collected language is to
make a mutable tree of strings in memory with associated metadata.
fstat sort of requires that you keep track of the modification date.
Then you might want to be able to serialize this in-memory filesystem,
or maybe an incremental update to it.  inode numbers are potentially a
bit tricky, but they don’t have to be assigned sequentially.

One alternative is to use an *immutable* tree and update it
functionally, which potentially simplifies the incremental-update
logic.

This feels like it ought to be doable in about 200 lines of code in a
garbage-collected language.