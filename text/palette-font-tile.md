The problem of a CRTC is, in some sense, to compute a function from
screen coordinates to color, where the function is largely given by a
pipeline of some lookup tables.  In the bitmap or TrueColor case, you
have just a single lookup table, the framebuffer, which directly
converts from screen coordinates to color.  In paletted modes, aka
pseudocolor, there are two lookups: first from screen coordinates to
palette index, then from palette index to color.  In a character
generator, there are also two lookups, but they are slightly
different: first from *truncated* screen coordinates to glyph index,
then from glyph index combined with differently truncated screen
coordinates to color.  Or, sometimes, to a foreground/background
selector, which is then used in combination with the truncated screen
coordinates to index a table of character colors.  In a tiled video
game console like the NES, the situation is fairly similar to the
colored-character-generator case, but there’s also a palette for each
tile, an offset added to the screen coordinates for scrolling, and
some sprite compositing as well.

Nowadays there is less call for this sort of elaborate stuff for 2-D
graphics, because human eyes are still the same resolution they were
in the 01960s, while computer memories have gotten much larger and
CPUs faster, and by storing the scene to be drawn in a framebuffer,
you can draw whatever you want in the framebuffer.  For 3-D stuff it’s
much more elaborate still, with shader programs doing arbitrary GPU
computations that might take an arbitrary length of time.

I was thinking that an interesting sort of intermediate level of
complexity would be a sort of reconfigurable systolic array (maybe the
kind sometimes called a “diastolic array”, though I’m not sure of the
distinction).  Essentially the idea is that you set up an APL-style
array computation on the whole vector of screen coordinates to produce
the desired colors, and then the CRTC executes this computation in a
pipelined fashion, producing each pixel value as it is needed.  Each
node in the abstract syntax tree is assigned to some computing
resource, such as a memory, an adder, or a FIFO, and they all
communicate through some sort of routing fabric.  In the most general
case, this could be a sort of crossbar scheme, but even a simple
fixed-function pipeline where each stage has the option to pass
through its input would be useful in many cases.  More flexible
routing fabrics and data processing units permit more efficient
assignments of operations to nodes, but a limited degree of
flexibility might be sufficient for many uses.

I was thinking that a particularly interesting kind of node for this
might be a round-robin memory, for example for fonts and colors.  It
might appear as, for example, eight LUT resources in the computational
fabric, consisting in fact of a counter, eight output latch registers,
and an input multiplexer multiplexing the address bus among eight
inputs, controlled by a counter.  On each cycle, the counter latches
the current memory word into the current output register and advances
to the next input.  In this way, a single memory could be dynamically
divided among different functions, such as tile palette and glyph
atlas, which vary less often than once per pixel.  Thinking further,
though, I’m not sure this kind of processing element is actually
useful at all, unless more than one of the functions can usefully use
the same data in memory (for example, for compositing multiple layers
of text); eight memories that each contained about one eighth the
amount of data would occupy almost exactly the same amount of chip
space, and they wouldn’t be limited to changing their value every
eighth cycle (or fifth, or whatever, if you set the counter to reset
more frequently).  You’d have eight address buses and eight data
buses, but they’d each be connected to one eighth as much memory, so
that’s not actually worse.  The only drawback is really the static
partitioning.

Even static partitioning could be overcome to some degree.  Suppose
you have an incoming 11-bit index and your memories only have 512
words.  You can feed the low 9 bits of the index to four different
memories, and then in a subsequent processing stage or two use the
other two bits of the index to demultiplex one of the four memory
outputs.  This is energy-inefficient and adds a cycle of latency, but
it doesn’t reduce throughput over the case where you had a single
2048-word memory.

Unlike in the strict array-processing paradigm, the system could
easily accommodate stateful processing.  The simplest example might be
generating pixel indices modulo 5 for a 5-pixel font; this can be done
with a counter whose low three bits cycle to 0 and generate a carry
after reaching 5, and which is synchronously reset to all 0 at the
beginning of each scan line.  A perhaps more interesting example is a
boxcar filter using a prefix-sum node, a FIFO, and a subtractor.
Doing the same thing vertically requires a buffer of the size of a
scan line.
