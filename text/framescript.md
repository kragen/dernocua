Suppose you want to run some arbitrary scripts in an interactive
display system, like a game, using a flexible programming language
like Lisp, but you want to ensure that those scripts don’t cause it to
use more memory or become unresponsive.  One possible way to handle
this is to run the scripts once per frame, allocating only from a
per-frame arena heap which gets nuked before the next frame, similar
to the nursery of a generational garbage collector.  The difference is
that any permanent effects need to go through some kind of
“interprocess communication” eye of the needle which will not pass
references into the per-frame heap — so you can pass, say, byte
strings, or maybe JSON-serializable objects, but not, say, mutable
data structures.  There is no automatic copying out of retained
objects when the nursery is full.

An advantage of doing things this way is that, to the extent that you
can contain any side effects from script execution inside a
“transaction” of some kind, you have the option of fearlessly aborting
a script at any point, either because it’s run out of time, because it
ran out of *memory*, or because it detected an error.  Changes within
the per-frame heap are entirely exempted from this because they will
get vaporized when the script ends, whether succeeding or failing.

If you run the pending event handlers in a frame starting from the
highest-priority ones, you can ensure that if anything fails to run
because you ran out of time, it’s the lowest-priority scripts.  Often,
in interactive systems, the handling of an event can be separated into
several parts which can to some extent fail independently:

1. **Bottom-half handlers**.  Some kind of minimal state update that
   provides feedback that the event has happened; for example, a
   bullet hitting a player might make the screen go red, or a
   keystroke might put a letter on the screen.
2. **Background tasks**.  Some kind of cascading state changes that
   happen as a result; for example, a keystroke might update an editor
   buffer, which might cause a lot of text to get
   re-syntax-highlighted, or a player entering a new region might
h   spawn a bunch of mobs, which then begin pathfinding to attack the
   player.
3. **Isochronous tasks**.  Some kind of logic to generate a screen
   image from the current internal state.

Normally you would like #3 to run *after* #1 and #2, so that it takes
into account the latest events, but generally #3 has a hard deadline
to generate some pixels, and if it doesn’t complete in time, the
program will miss a frame, which is not ok.  So if something has to
get aborted it should be a background task, #2.  But there isn’t a
clearly obvious time at which that should happen; if the frame is due
at 8.3 milliseconds, say, and the current time is 5.2 milliseconds,
should we abort scripts from #2 or not?  And the answer depends on
whether #3 needs more or less than 3.1 milliseconds to reliably run to
completion.

One plausible way to handle this is to analyze the isochronous code in
#3 for its worst-case execution time (WCET) and use that to compute
the deadline, so the deadline will always be hit.  A different
alternative is to measure how long it takes, and how variable that
timing usually is, and use something like the mean of the last 30
execution times, plus, say, three standard deviations.  This will
sometimes miss frames, but perhaps rarely enough to be acceptable for
interactive applications.

Computing WCET is harder when there are interrupts, because interrupts
can happen during the isochronous code.  You need some kind of bound
on how frequently they can happen and how long the (top-half) handler
can take to run.

Any time left over at the end of the frame can be used to run
(bottom-half) handlers and background tasks.

In general it is totally okay for the script’s ephemeral heap to
contain pointers to things outside of it, just not the other way
around.  But, if writing within the ephemeral heap is supported, the
system needs to be able to distinguish these potentially-external
pointers from heap-internal pointers.

When a new event comes in, it would be undesirable for any
currently-running background script to yield the CPU to the
bottom-half handler.  This can be achieved by aborting it and
resetting the allocation pointer or by running the handler on a
different heap.  If you have multiple cores you presumably want to try
to run background tasks on all of them, so you’ll probably have to
suspend or abort one of them.

Pointer-bumping allocators can be very quick.
