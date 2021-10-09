Some notes on perusing [the Udanax Green codebase][4], with particular
attention to how it thinks about version tracking.

[4]: http://udanax.xanadu.com/green/download/udanax-1999-09-29.tar.gz

There’s a slightly updated version at
<https://github.com/dotmpe/udanax-mpe>.

Conceptual guides I’ve found
----------------------------

A conceptual overview is in `olddemo/demo_docs/Bizplan4`.

The place to start for nuts and bolts is quite likely green/man, which
contains man pages that GNU man can format with, e.g., `man
green/man/fex.L`, which documents the frontend UI.  I suspect the
“Xanadu FeBe Protocol 88.1x” document might be more informative if I
could find it.  `man green/man/xumain.L` offers an illuminating
glimpse into how Xanadu thought of documents at the time.

Each document is evidently identified by a “docid”, a dot-separated
sequence of numbers called a “tumbler”; the numbers constituting the
tumbler are sometimes called “digits” or “tdigits”.  (Sometimes a
tumbler is also called an “isa” in the source.)  Tumblers, like
tilde-bearing WWW URLs, can contain in sequence a network node
identifier, a user account (/~kragen/, represented as a number in a
tumbler), a document ID within that account, and a region identifier
within that document; so they can identify finer-grained or
coarser-grained things than individual documents.  A “span” is
specified in terms of character counts.  I think?  Bizplan4 says:

> by combining a document's unique identifier with a character
> position within that document, we can uniquely address any character
> stored in the entire system.
> 
> By designating a particular (starting) character and a length we can
> address any contiguous string of characters in the system.  Such a
> string is called a “span.”  By clever use of tumblers instead of
> plain integers to represent character positions and span lengths, it
> is possible to have spans which contain whole documents and cross
> document boundaries.

There doesn’t seem to be any thought given (in
`green/olddemo/demodocs/ReplacingD`, anyway) to the problem of
updating documents while retaining links.  They do conceive of
multiple versions of a document, and in `green/olddemo/demo_docs/Suespaper`
it says, “Xanadu hypertext can maintain multiple versions of any given
document, efficiently storing the common portions in common, ...  All
such editing wil [sic] be logged by Xanadu's historical trace
function. Xanadu can provide historical traceback information in dated
chronological order about any and all changes to a given document.”;
but in [the status page on the WWW][0] “Historical Trace” is in the
“Needs Implementation” column.

[0]: http://udanax.xanadu.com/green/status.html

The concern for the space required for multiple versions seems very
quaint now; it’s easy to forget that even when Subversion was
introduced in October 02000 the fact that it kept a separate
“pristine” copy of whatever source code you were editing was
considered a major concern, and in 02001 crazy old Tom Lord’s arch’s
policy of keeping the entire version history on your development
workstation was, for many, considered a showstopper.  (Today almost
everybody uses Git, except for people working with large binary
assets, who often use Subversion.)

The source base itself
----------------------

It’s surprising they chose C as an implementation language so early.
It’s archaic K&R C formatted with 2-space tab stops (in `less`, use
`-x2`), but it’s C.  Before 01984 it doesn’t seem like it would have
been an obvious choice; it seems like at some point they decided to
restart from scratch on a 68000-based Sun.
`green/olddemo/demo_docs/Datamation`, which seems to be from 01982,
says “running under Unix on a Motorola 68000-based Onyx desktop
computer,” but [I think Onyx’s Unix machines were
Z8000/Z8002-based][1], [running the first microcomputer Unix in
01980][3], but [even in 01981 people had a hard time finding the
company][2].  Evidently the team was foresightful enough to recognize
the importance of Unix.  The choice of C is a pleasant surprise; it
makes the codebase a lot more readable than, say, EUMEL.

[1]: https://web.archive.org/web/20020810193147/http://www.dmsd.com/Onyx.history.html "More about Onyx Systems, by John L. Bass"
[2]: https://web.archive.org/web/20040414024027/http://rlab.cs.nyu.edu/ultra/reports/proton/01 "[Courant] UltraComputer Prototype Note #1, Microprocessor System Survey, by Jim Lipkis, October, 01981"
[3]: https://web.archive.org/web/20020614113953/http://www.heuse.com/1980.htm

In the context of the space concerns mentioned above, it’s sort of
surprising that the source base *per se* is 39,000 lines of C weighing
1.07 megabytes (16000 unique lines weighing 650 KB), in significant
part because they named their functions things like
`klugefindisatoinsertnonmolecule`.

In the backend types are mostly named with the prefix “type”, as in
“typecuc” or “typetask”; in the frontend that is more typically a
suffix, as in “spectype” and “cutseqtype”.

The source base seems to be fairly consistent in putting the names of
functions being defined (and *only* functions being defined) at the
left margin without indentation.  I think this is an accommodation for
archaic versions of `ctags`, but it’s handy as a way to navigate the
source base without `ctags`.

I’m inferring that maybe documents, at least in the frontend
(`fe_source/vm.c`) are referred to by “specs” (type `spectype`) and
consist of “charspans” (`charspantype`).  The spec contains a
`specspanptr` (which I guess is a charspan?), which contains a
`sizeofspan`, and a `docid`, which is a “tumbler” and can be sent to
the backend.  Destroying a spec is done with `specfree(&specptr)`.

They’ve implemented their own virtual memory system made of objects of
type `vmthingtype`.  There’s a subtyping graph:

    spectype* -> vmthingtype*
    charspan* -> vmthingtype*

The frontend evidently contemplates editing documents; there’s a
`sendrearrange` function in `fe_source/sendtop.c` which sends a
“cutseq”, I guess like an EDL for text?, to the backend.  There’s also
`sendinsert`, which makes it seem like the granularity of edits is
very small.

A “link” is from a spec, to a spec, three a spec (“threesets are used
to describe the intended meaning of the link, such as if it is a jump
link or a footnote link”, the other possibilities evidently being
“quote” and “marginal note”).  But when the frontend does
`sendcreatelink` to the backend, it also includes an additional docid,
apart from those in the three specs; this is explained in
`olddemo/demo_docs/Bizplan4`:

> Links themselves are said to reside inside documents, located in a
> separate logical address space from the text. A link may reside in
> one document and link from a second document to yet a third.  The
> location of residence of a link is entirely independent of the
> contents of the link's end-sets.  The fact that links are among the
> potential contents of documents means that links themselves may be
> linked from or to, just as characters may.  Thus very general sorts
> of indirect structures may be assembled.

For the frontend they seem to have used curses, including its
windowing system (well, `newwin`, `delwin`, and `wrefresh`, anyway),
and also some kind of Sun GUI (it’s trying to `#include
<suntool/tool_hs.h>`, call `win_setcursor`, etc.)  This seems to be
the “sunwindow” system sometimes called “SunWindows” and the “Sun
Graphical User Interface,” and later called SunView, mentioned in
<http://homepages.rpi.edu/home/56/frankwr/afs/rpi.edu/campus/sun/lang/2.01/SC2.0.1/include/CC_413/sunwindow/win_struct.h>,
(which seems to be part of a huge repository of old Sun stuff that was
shipped to customers, up to Solaris 2.5) and documented in
<http://bitsavers.trailing-edge.com/pdf/sun/sunos/4.1/800-1784-11A_SunView_System_Programmers_Guide_199003.pdf>;
this window system had a file descriptor per window.

The backend refers to something called a “granfilade”, which I think
is one of the three possible types of enfilade: GRAN, SPAN, and POOM.

### Creating new versions ###

The protocol documented in `green/olddemo/demo_docs/Feidoc` includes a
`CREATENEWVERSION` function:

> A version is a document, the only distinction being that a version
> is descended from a previously existing document.  A new version
> inherits all of its immediate ancestor's information, both textual
> and topological.

Its tumbler is to be nested under the document it was created from:

> For example, if there is only one version of document 23.0.17.0.256,
> this request will create a document with the id 23.0.17.0.256.1.

However, this isn’t always possible, because sometimes you create a
new version of a document that somebody else owns, and you don’t get
to inject it into their namespace like that.  So, is there some way to
trace the history back to the original?

The `CREATENEWVERSION` request type is defined in
`green/fe_source/requests.h` and `green/be_source/requests.h` as
`#define CREATENEWVERSION 13`; the backend vectors it to a
`createnewversion` function in `green/be_source/fns.c`, which calls
`docreatenewversion` in `green/be_source/do1.c`, which eventually
calls `docopyinternal` with a new “isa” pointer (allocated, I think,
by `doopen`) and vspans and vspecs it got from the old document.  As
mentioned above, “isa” is another name for “tumbler”, or maybe a
certain kind of tumbler.

There’s a conditional at the top of `docreatenewversion` which checks
to see if the `wheretoputit` argument identifies a tumbler that
belongs to the user, invoking `makehint` differently; makehint invokes
`movetumbler`, which is just a struct assignment macro which copies
its left argument over its right argument.

Within `docreatenewversion`, in the case where the document does not
belong to the user, there is no evident dataflow from `isaptr` (the
tumbler of the document being copied) to `createorglingranf` (in
`green/be_source/granf1.c`, delegating to `createorglgr` in
`green/be_source/granf2.c`), which I guess allocates the new tumbler
with `findisatoinsertgr` (just below) and inserts it somewhere with
`insertseq`.

I’m not sure what an “orgl” or a “sporgl” is but evidently it’s some
kind of thing that gets stored on disk, an orgl being some sort of
cuc, and maybe a granfilade consists of null, texts, and orgls.  In
one place ORGLRANGE and SPANRANGE are explained as “wid and dsp
indexes for sp”, which is pretty significant; widative and dspative
are the two major dimensions of enfilade theory.  A diagram, however,
seems to suggest that this is not respective but orthogonal: both wid
and dsp have both ORGLRANGE and SPANRANGE.

After `createorglingranf`, `docreatenewversion` builds a vspec and
apparently copies the original `isaptr` into it, and then invokes
`doopen` with `newisaptr` and without the vspec or the original
`isaptr`, and then uses `docopyinternal` to copy the old document to
the new document, using the vspec.  Also, the thing that it’s copying
is the stream of a vspan obtained from `doretrievedocvspanfoo`, which
delegates to `retrievedocumentpartofvspanpm`, which sets the stream
and width of the vspan from two tumblers found in the orgl:
`cdsp->dsas[V]` and `cwid->dsas[V]`.  I’m not quite sure what these
are for; do they offer a way to navigate back to the original version?

The vspec passed to `docopyinternal` (containing the original
`isaptr`) is a “specset” to `docopyinternal`; it gets converted to a
“spanset” named `ispanset`.  This is passed to `insertpm` and
`insertspanf`.  `specset2ispanset` loops over the linked list of
`spanset` objects (they have a `->next`) and specifically looks at the
`docisa` copied into the vspec by `docreatenewversion`, passing it as
the third argument to `findorgl`, so it can use it to fetch the orgl
with `fetchorglgr`.  But that's all it does with the `docisa` that
`docreatenewversion` copied from the `isaptr`.

However, when `docreatenewversion` is being invoked from
`createnewversion`, it *also* gets the original document tumbler as
its `wheretoputit` argument!  So actually there is data flow from the
original tumbler into *both* of the `makehint` cases, so the `hintisa`
of the hint will have the original document tumbler in it.

