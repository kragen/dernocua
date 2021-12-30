Before people started embedding a computer into every terminal, as was
done in the VT-100 (8085), Datapoint 2200 (discrete TTL), and PLATO V
(8080) terminals, the traditional way to make a character-cell CRT
terminal such as an ADM-3A was to build a hardware character
generator.  Even some terminals introduced after the Datapoint 2200,
and of course many personal computer display driver boards, used this
approach to lower costs.

Traditional character generators
--------------------------------

We map each character cell to a fixed† position in a random-access
screen-buffer memory, then control its memory address bus with a
counter during raster scanout.  A pixel counter overflows into the
column counter, which overflows into a scanline counter, which
overflows into a text-line counter.  The pixel counter and scanline
counters are used to drive some address lines on a font memory (often,
tragically, a mask ROM) while the column and text-line counters drive
the screen-buffer address lines, the data from which drives the other
address lines on the font memory, perhaps delayed by a clock cycle or
two of latches.

If the memory used for a screen buffer is fast enough, writes to it
can be interleaved with the character generator’s reads to avoid the
need for dual-ported RAM or the occurrence of CGA-clone snow.  One way
to make the screen buffer faster is to make it wider, so that it can
be read two or four glyphs at a time rather than one.  This generally
was not done at the time because video signal rates were so much
higher than baud rates that snow wasn’t a problem.  Writes can be
delayed until an HBI with a little buffering logic, and I think that’s
what was generally done.

This approach to driving the screen can produce a high pixel rate even
with relatively slow RAM.  Typical numbers from this epoch might be
60 Hz for vertical scan, 5 horizontal pixels per glyph, 80 glyphs per
line, 8 scanlines per text line, 24 text lines per screen, and about
10% horizontal blanking interval (HBI) and 10% vertical blanking
interval (VBI).  A glass terminal might talk to the host over an
asynchronous serial line at 1200–9600 baud, or rarely 300; at 9600
baud, each character took 1042 μs, 1.04 *million* ns.  Multiplying
this out, the visible part of the screen contains 192 scan lines, so
including the VBI it’s about 213, giving a horizontal scan frequency
of 12.8 kHz (78 μs per line).  In practice this is low enough to
produce an annoying whine audible to many people, so often higher
frequencies were used; suppose the horizontal scan is instead 20 kHz,
including 400 pixels and a 44-pixel HBI.  Then our pixel clock is
8.9 MHz; pixels come out 113 ns apart.  This is fast enough to require
significant attention to signal integrity and path-length issues.

One solution to this problem is to dump each character slice from an
N-bit-wide font memory into a shift register like a 74165.  The shift
register needs to run at the full dot clock speed, but the font memory
can run N times slower; in this case, where N=5, that’s 1.78 MHz,
560 ns per access, which is easily attainable with memory chips from
the 01970s, and maybe even with faster kinds of core memory.  The
screen-buffer memory runs at the same speed.

To be concrete about sizes, the font buffer might contain 96 5×8
glyphs, 480 bytes in all, while the screen buffer is just under 2000
bytes.  The VT50 or DECScope had only ROM for the font buffer and only
half that amount of RAM, 12 lines of 80 characters, 960 bytes, 7-bit
IIRC.  When even that amount of RAM was too expensive, you were stuck
with vector displays or printing terminals.

One drawback of this organization is that the ordinary text-editing
operations of inserting or deleting a character require updating
potentially a whole line of text in the screen-buffer memory.  Doing
this locally in the terminal was highly desirable, since
retransmitting all those characters from the host to the terminal at
1200 or 2400 baud introduces a delay of a significant fraction of a
second, and also likely imposes the cost of interrupt handling and
perhaps even context switching on the host; but copying a variable
number of glyph indices one item forward or back in the screen-buffer
memory, potentially as many as a whole line’s worth, is also
potentially slow, especially if the screen-buffer memory is multiple
glyph-indexes wide as suggested above.

† Scrolling the whole screen is usually necessary, and can be done in
a cheaper way than inserting or deleting text, by changing the
starting value the text-line counter has at the top of each frame.
But inserting or deleting lines is also expensive.

Traversing piece chains in hardware
-----------------------------------

There’s an alternative which I think *might* be simpler than embedding
an entire computer into the terminal, which is to traverse a piece
chain in hardware.  Instead of mapping each memory location in the
screen buffer to a fixed location on the screen (or one that is fixed
except for scrolling), we build linked lists.  Suppose we divide a
2048-byte screen buffer into 256 60-bit words, so addresses are only 8
bits, and store one variable-length *piece* of text in each word.  The
first byte of the word gives the address of the word holding the text
to its right.  The next three bits specify how many characters are in
this piece, a number from 1 to 7, which is used to initialize a
countdown timer in the character generator.  Then there are 1 to seven
7-bit glyph indices, which are loaded into 7 shift registers whose low
bits drive address lines of the font memory.  (There’s always at least
one glyph per piece to ensure that the pipeline doesn’t run dry.)

(There are 128 bytes out of the 2048 which are unaccounted for here,
and note that we only support 1792 distinct characters on the screen
at once, only 93% of the usual 1920.  This is probably still enough
for an 80×24 terminal screen almost all of the time, since most lines
have some blank space.  A blank-space trailer can be drawn with a
single-glyph piece that points to itself, shared among all lines.)

The video generation pipeline with this system is slightly longer than
that of a traditional character generator.  The pixel counter,
character-cell counter, scan-line counter, and text-line counter work
as usual, but the character-cell counter is only used to detect the
end of the scan line, and the character-cell and scan-line counters
are not directly connected to the screen-buffer memory.  There’s a
60-bit buffer for the next piece; when the countdown of glyphs in the
current piece ends, it’s used to reload the countdown timer and the
glyph-index shift registers, and its next-pointer field is used to
fetch the next piece from the screen buffer.  Before the HBI ends, the
buffer is instead loaded from a piece indexed by the text-line
counter.

If every piece on a line is one glyph long, then the character
generator will read a word from memory after every glyph, every
560 ns; if the memory is slow, this could reduce the bandwidth
available for processing of screen updates.  However, serial data
transmission is so slow that I think this is unlikely to matter.

Traditional vertical scrolling just involves changing the piece at
which each line starts.

An alternative to using linked lists would be to use a piece index
vector for each line; you need between 11 and 80 pieces for each line
on the screen, so you could use 11 to 80 bytes for piece indices,
maybe reasonably in the neighborhood of 20.  A disadvantage is that
sometimes an insertion would require moving a lot of piece indices
over by one to make room for the new piece, and if you were
dynamically allocating the piece index vectors in a piece index vector
memory, maybe you’d suffer from fragmentation.  The potential
advantage is that you could share common pieces between lines,
providing data compression.  Overall I think it’s not worth it.

An intermediate approach, sort of a wheel-of-reincarnation thing,
would be to have a “piece index stack” (of some limited depth like 4)
and a “call bit” in each piece.  If the call bit is 0, the behavior is
almost the same as described above — the pointed-to piece just
replaces the current piece.  If the call bit is 1, then the current
piece index is incremented and pushed onto the piece index stack; and
when the call bit is 0 and the next-pointer is also 0, then the new
piece index is popped off the piece index stack.  This allows the
reuse of common strings for data compression without making insertion
difficult.

Serial protocols
----------------

It’s clear that inserting or deleting a glyph can be done *efficiently*
in this representation, but it probably is not *simple*.  Deleting a
character may involve removing a piece from the piece chain and returning
it to a free list; inserting a character may involve allocating a piece
from a free list, inserting it into the current piece chain, and moving
some of the characters from the current piece into it.  While it would
be *possible* to do this kind of thing with microcode in the terminal, a
much more reasonable thing to do would be to do the logic on a computer,
then send to the terminal the commands to make the necessary changes:
set the next of (undisplayed) piece 167 to 81 and its glyph count to 7,
append the 3 glyphs “ges” to piece 167, set next(27) to 167 and its
glyph count to 4.

That’s maybe 11 bytes (set7 167 81, append3 167 g e s, set4 27 167) to
insert a character, which would be a noticeable 92-ms delay at 1200
baud.  You could maybe improve this by, when you might want to insert
into the middle of a piece, pre-copying the glyphs that follow the
cursor into a new not-yet-displayed piece, which you point at the
display list ahead of time: set7 167 81, append2 167 e s; then
actually inserting the glyph is just split4 27 167 g, four bytes that
sets both the size and next pointer as well as appending a glyph, or
possibly set3 27 167, append1 27 g, six bytes.  This is not as fast as
the one byte needed for insert mode on a VT100, of course, but it also
doesn’t need an entire computer embedded in your terminak.

Probably a better option than a byte-oriented update state machine is
to simply transmit 68-bit piece updates over the serial interface: an
8-bit piece index plus a 60-bit word to load into it.  Under some
circumstances this would impose a slight extra performance cost, but
it would be less significant at higher baud rates, and it would
simplify the terminal hardware significantly.  When drawing bulk text
this would require 68 bits per 7-glyph piece, compared to the 72 bits
required by the byte-oriented approach above (or 90 bits if we’re
using N81 asynchronous serial with start and stop bits), while the
11-byte sequence above would be two piece updates (17 bytes), and both
the 6-byte pre-copying sequence and the 4-byte or 6-byte splitting
sequence would be one update (8½ bytes).  Note that at 115200 baud,
the fastest standard RS-232 baud rate, a 70-bit sequence including a
start bit and a stop bit would be 608 μs, roughly 1100 times slower
than the fastest frequency at which the character generator might need
to read pieces.

This word-transmission approach might actually be faster overall if it
permits the use of higher baud rates; the [PLATO V terminal in
01977][0] ran its serial interface at only 1200 baud, perhaps in part
so its 5 MHz 8080 could keep up.

[0]: https://archives.library.illinois.edu/erec/University%20Archives/0713808/1977%20Aug%20X-50%20PLATO%20V%20Terminal%20Stifle.pdf "The PlatoⓇ V Terminal, J.E. Stifle, August 01977, University of Illinois CERL Report X-50"

The word-transmission approach has the additional merit that it’s
idempotent, so retransmission is safe, and it’s weakly convergent in
the sense that if you keep sending messages then probably eventually
the state will be correct, instead of persistently diverging.  Data
transmission errors are likely to induce psychedelic effects with any
of these data models, so this sort of convergence is important.

If there’s no special support for scrolling, then scrolling a 24-line
display would require setting 24 60-bit words, 180 bytes, which would
take a janky 188 ms at 9600 baud and a totally unusable 1500 ms at
1200 baud.  The easiest approach is to have an 8-bit screen-start
register S with the semantic that the first line on the screen starts
with piece S, the second line with piece S+1, and so on, and then you
can scroll just by creating a blank line and setting that register.
If you don’t do a modulo of the screen size, you can scroll a window
up and down over a larger area instantly, assuming you have enough
space for the text, but you’ll have to occasionally relocate live data
the scrolling is about to steamroll.

Overstrike
----------

If you fetch an average of 20 pieces for each scan line at 20 kHz,
that’s an average of one every 2500 ns.  That’s pretty slow, so even
with 01970s hardware, you could imagine generating a couple of pixel
streams in parallel and ORing them together.  That would allow you to
generate, for example, accented or struck-through characters.  But the
second pixel stream would cost a similar amount of hardware to the
driver for the first pixel stream, so this might not really be
worthwhile.

Writable and proportional fonts
-------------------------------

A softfont, even one with only a few writable positions, extends the
graphical capabilities of such a device enormously.  A transparent
pixel-granularity mouse pointer or other sprite can be emulated with
only four writable glyphs and unused glyph indices, and a few more
writable glyph positions is sufficient to enable applications like
schematic capture, dataflow diagrams, math, and limited foreign
language support.

Of course, any kind of softfont capability requires some extra logic
to distinguish glyph-update requests from screen-update requests
(perhaps a 69th bit), and updating four 5×8 glyphs necessarily
involves at least 20 bytes of data if uncompressed; that’s only 21 ms
at 9600 baud, but a janky 167 ms at 1200 baud.

This setup can even be extended to support proportional fonts in an
analogous way: instead of initializing the pixel-within-glyph counter
always to 5, you initialize it to a value taken from a font-metrics
memory that’s indexed by the same glyph index used to index the
font-pixels memory.  As before, you shift the glyph-index registers
when this counter hits 0.  This would enable proportional fonts
without a framebuffer.

Variable line heights could be done in a similar way but much more
easily, since they just involve conditionally resetting the scan-line
counter and incrementing the text-line counter during the HBI.  But
once you have variable line heights you may start wanting the ability
to have non-aligned baselines on different parts of the screen.  And
at that point you’ve just about moved to a scan-line rasterizer kind
of model.

Graphical effects
-----------------

The VT100 supported inverse video and, I think, some other graphical
effects, maybe including double-width, double-height, bright, dim, and
blinking characters.  I think it had some line-widening logic that
extended each bright pixel horizontally by a second pixel in order to
reduce the size of the font ROM.  Some successor terminals supported
smooth scrolling, where scrolling happened a pixel at a time instead
of a line at a time.  The PLATO V terminal supported “character
magnification” to get different font sizes.

In addition to this sort of thing, you could imagine using an LFSR to
get “snowy” characters, either as foreground or background, or
adjusting the letter spacing or line weight; this could all be done
with a dedicated effects bitfield in each piece, avoiding any
potential need for blank spaces on the screen.  If the frame rate were
high enough, or the display hardware possessed of sufficient
persistence, you could also use PDM to get various brightnesses, but
probably this is usually better done in other ways.

Alternatively, a display list
-----------------------------

Compositing from a display list into a single-scan-line “framebuffer”
is probably a better way to get things like overstrike, and it would
also allow you to do pixel-perfect positioning of text, so variable
line height is an easy thing to do.  This “line buffer” would cost 50
bytes with the figures described above, but double-buffered, making
100 bytes.

The idea is that, while one part of the hardware is spitting out your
pixels at 8.9 MHz from a 50-byte FIFO, another part of the hardware is
writing to another 50-byte “back-buffer” register.  It’s driven by the
kind of piece-chain structure described above, but instead of having a
rigid grid of lines on the screen, you have a “display list”, in which
each item is a (y, x, height, piecenum) tuple, which is sorted by y.
As we iterate over the scan lines in a frame, the display-list
processor maintains two indices into this display list: the earliest
item that’s still visible, and the earliest item that’s not yet
visible; and it just draws all the piece chains in between those two
indices into the back buffer, one after another, using OR or AND or
whatever.

And then, when it’s time to move on to the next scan line, the back
buffer is loaded into the FIFO, and then the back buffer is cleared.
Hopefully the display-list processor finished traversing the display
list first, but at any rate it now starts rendering the new line.

This is basically just standard scanline rendering like you might use
for a 3-D image rasterizer, but you need a barrel shifter or something
in the middle, unless you want to have a second shift register running
at 8.9 MHz in the middle of your otherwise relaxed sub-2-MHz system.

Alternatively, if you’re using a fixed-width font, and you’re willing
to snap your horizontal pixel positions to character cells or half
character cells or whatever, you can reduce the number of shifts you
need between your font memory and your back buffer.  If the back
buffer is divided into 6-bit chunks, say, and the font is 6 pixels
wide, you can AND aligned 6-bit chunks from the font buffer into the
back buffer.  If you allow 3-pixel shifts, then you need a 3-bit
shifter that you can write 6-bit pixel slices into and copy
3-bit-shifted 6-bit pixel slices out of into the back buffer.

This level of control complexity may be high enough that it’s
justifiable to use a real CPU to draw into your line buffer, even if
you have special-purpose hardware driving the actual video signal.  At
that point it no longer makes sense to think of it as a “terminal”;
you want to run your entire program on that CPU as much as possible so
that it can be instantly responsive and have as high bandwidth as
possible to the display.

This might even be a reasonable way to do PAL video out of a working
monochrome GUI on an ATMega328 Arduino: running at 16 MHz I think the
TVout library can output pixels at 8 MHz, which leaves enough space
for 320,000 pixels in a 25-Hz PAL frame.  PAL (except for Brazil’s
PAL-M) is a 625-line standard with 576 visible lines (92.2% visible)
with 51.95 μs of active video per 64 μs line.  In theory this means
415.6 horizontal pixels, which is actually enough for 80 columns of
5×8 text (400 pixels).  You absolutely can’t do it with an in-RAM
framebuffer, because the ATMega328 doesn’t have enough RAM, but you
could maybe do it with a per-line framebuffer.

On the AVR the situation is a lot worse than in hardware, though:
because you don’t have the hardware parallelism, you can only render
into your line buffer during the horizontal blanking interval.  That
gives you only about 200 clock cycles, which is not a lot of time,
maybe 60–100 instructions.

I suspect it might be possible to steal part of the horizontal visible
part of the screen for computation — leave it black (or white) and
arrange for a timer interrupt at the right time to generate the back
porch and sync pulses.  In fact, I think TVout already does this,
since it supports any output resolution (as long as you have enough
memory) but can only output pixels on integer clocks: every 2, every
3, every 4, or every 5 clocks, but not every 2.5 clocks.  Every line
is still only 1024 clock cycles but you still ought to be able to do a
few hundred instructions that way.
