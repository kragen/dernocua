I was reading about PLATO a lot yesterday (see file
`beyond-overstrike.md`); the PLATO IV terminal designed in 01970 had a
relatively simple control system, executing a series of 21-bit words
received over a 1200-baud serial line from the computer center.  It
included line-drawing and character-painting hardware, but because its
gas-plasma panel display screen had inherent memory, it didn’t need a
framebuffer; the screen could be painted as slowly as necessary.  And
the terminal wasn’t programmable at all; it was just a puppet of the
supercomputer in the computer center.  If it detected a parity error,
it would stop processing and signal the error back to the
supercomputer, which would then retransmit the operation stream from
the point of the error.  Keystroke handling was all done on the
supercomputer.

Although such terminals were replaced by personal computers in the
late 01970s and early 01980s, as I understand it, a similar sort of
instruction-stream-executing setup is applied by modern cellphone LCD
panels, is used by the “threads” in a GPU “warp” or “wavefront”, and
was used by the processors in early Connection Machines, which had
predication but no separate control.  The LCD panels do function as
puppets of the CPU (or perhaps GPU), bringing about a predetermined
result like the PLATO terminals, but in the other cases there is local
data that computes a different result on each processor.

An interesting question to me is this: what’s the smallest amount of
additional local control you could add to such a system to make it
more powerful?

Often such a system needs a current-instruction register, into which
it periodically clocks another instruction from the incoming
instruction stream.  The simplest form of control would be to
conditionally not do that, instead remaining with the already-received
instruction, executing it a second time.  But this needs some kind of
termination bit computed somehow, or entering such a repetition mode
would be permanent.  A repetition-count field of 3–7 bits in the
instruction word is one approach, perhaps coupled with some kind of
chip-select line that allows you to load a repeated instruction into
one such executor, and then while it is running, into another, and so
on.

In other cases, the execution unit needs to buffer a sequence of
recently received instructions, such as 8 or 16, in a small
dual-ported FIFO, which it maintains an execution index into, perhaps
lagging behind the incoming instruction stream.  A backward-jump
instruction can then set up a loop.  In such a case, the looping and
overwriting need not be conditional, as in the previous case; the
looping can simply continue until the loop gets overwritten, though
reliably synchronizing this with the loop execution could be tricky.
