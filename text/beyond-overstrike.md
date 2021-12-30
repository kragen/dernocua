In my childhood, I used a mechanical typewriter with no exclamation
mark “!”.  It did have a vertical apostrophe “'” which was nearly
right, lacking only the dot at the bottom.  The solution was to type a
“'”, press the backspace key, and then type “.”, thus creating an
exclamation mark on the paper.  (The vertical nature of the apostrophe
allowed it to do double duty as a single-quote as well, much as the
letters “l” and “O” did double duty as digits on many typewriters; I
think that’s why typewriters with a separate “!” often put it on the
“1” key.)  If memory serves, it also had an underscore key (shift-6)
used in the same way to produce underlined text.

Typewriters for other languages, for which diacritics were important,
commonly had “dead keys” for accents.  These would place an accent
mark on the paper without advancing the carriage, so you can type â
simply by typing ^a, without typing a backspace in the middle.

Overstrike and glass ttys
-------------------------

Traditional printers (including the ASR-33) are equipped with this
ability to “overstrike”, typically using backspace or a carriage
return without an accompanying line feed, which permitted them to do
boldface, accented letters, and underlining, without any dedicated
electronics or mechanics for those purposes.  This is the reason ASCII
includes the characters “~”, “^”, and “`”, characters which don’t
exist in pre-ASCII English text.  APL used this overstrike capability
to create an unlimited variety of new operator symbols; for example,
by overstriking Δ with |, you could get ⍋, the ascending-sort-order
operator. Some printers also implemented superscript and subscript
with a half-linefeed feature, so you could write x² or xᵢ in a more or
less readable way — although these were the same font size due to
mechanical limitations.

Glass terminals like the “DECScope” VT-50 did not implement these
feature, because taking an arbitrarily long period of time to compose
a glyph was not very compatible with scanning out pixels in real time
to a CRT electron beam.  Instead, “printing” a new character at the
location of an existing character simply replaced it.  While this
removed the ability to overstrike, it made it possible to do real-time
screen editing, updating any part of the screen to contain arbitrary
new contents.

### PLATO ###

One very notable exception was [the terminals developed for the
University of Illinois PLATO project][4]; after spending the 01960s
using Raytheon storage tubes, starting with PLATO IV, PLATO terminals
used Owens-Illinois Digivue gas-plasma screens with [(in the 01977
PLATO V incarnation) 8080 processors][0], and they *did* support
overstrike, potentially doing a bitwise OR of the various characters
in a character cell, an ability PLATO users used to compose a variety
of creative cartoons.  The terminals’ protocol was [wildly
nonstandard, involving 11-bit words from terminal to host and 20-bit
words (21 including parity) from host to terminal][1], and they could
handle overstrike because [their quarter-megapixel screens were
*bistable*][2], like Tektronix 4014 DVBST.  For output they used a
non-ASCII-related 6-bit character code with mode shifts, packed three
to an instruction word, and for input they used an unrelated 7-bit
modeless character code embedded in that 11-bit word.

Probably unsurprisingly, 5 of the built-in 128 characters in the PLATO
terminal’s ROM character set were accent characters apparently
designed to be overstruck with letters: ̃, ̈, ̂, ́, and ̀, at positions 033
(octal) to 037 of the M1 font memory.  (The character bitmaps can be
seen in Figure 2.8.2 on p. 25 of the 01977 PLATO V terminal report.)
There were also superscript and subscript control codes to move the
baseline up and down by 5 pixels.

David Liddle explained the bistable nature of the panel:

> The plasma panel was invented, or discovered, if you want to think
> of it that way, that... if you, you probably remember this, though:
> it, of course, produced those orange dots.  But it also had memory,
> automatically!  As you wrote something on that screen, it stayed!
> You didn’t have to refresh it, rescan it, or anything.

He explained that when they started the plasma-panel project in 01968,
memory cost 1¢ a bit, so the 262144 bits in a flat-screen PLATO
display of the resolution of 512×512 they eventually settled on would
have cost US$2621.44, the price of a house; but by the time they
finished the project, memory prices had fallen by more than an order
of magnitude, greatly decreasing the advantage.

The [original 01970 PLATO IV terminal paper explains][4] (pp. 2–3,
7–8/30):

> The terminal should cost less than $5000 ...
> 
> Direct viewing storage tubes may be used to overcome the flicker
> problem but these devices suffer from low brightness and the
> inability to perform selective erase operations on the displayed
> data.
> 
> The use of a plasma panel, on the other hand, with its inherent
> memory, eliminates the refresh memory while preserving the selective
> erase function.  Because each point is stored on the panel as it is
> displayed, the terminal electronics need operate only fast enough to
> stay ahead of the incoming data.  A panel writing rate of 30 KHz is
> adequate for this [graphical computer-based instruction]
> application. The digital nature of the plasma panel also eliminates
> the need for any DA converters.

Brian Dear’s “The Friendly Orange Glow” chapter 6 describes the
history and principles of operation of these bistable plasma displays
in more detail, starting with the January 01963 article “Large
Displays: Military Market Now, Civilian Next” in _Electronics_
Magazine, incidentally fingering Lear Siegler, later the maker of the
ADM-3A, as the first manufacturer of non-bistable plasma displays, and
mentions that Doug Engelbart had filed some patents in the 01950s.  It
credits Gene Slottow at UIUC with the key insight of moving the
electrodes to the *outside* of the glass in 01964 or 01965, and said,
“By 1967 Alpert and Bitzer had chosen the Owens-Illinois (OI) company,
wizards of glassmaking, to be the manufacturer of the displays.”

(In Chapter 10 Dear explains that PLATO IV finally established ‘formal
“prime-time” hours of service’ in 01974, despite getting “hundreds of
PLATO IV terminals” in 01972, so evidently it took a while to get
those plasma terminals rolled out in volume.)

The rest of the terminal seems to have contained about 70 bits of
registers and 128 8×16 glyphs’ worth of softfont RAM, which are
programmed as 1024 16-bit words in “Mode 2” (§2.5) after a LDA (“load
address”) operation, each 16-bit word being a column of 16 pixels.  So
the display panel contained 262144/16384 = 16 times as much memory as
the entire rest of the terminak.  The 64×32 character resolution of
the terminal was slightly larger than the 80×25 VT-100.

[0]: https://archives.library.illinois.edu/erec/University%20Archives/0713808/1977%20Aug%20X-50%20PLATO%20V%20Terminal%20Stifle.pdf "The PlatoⓇ V Terminal, J.E. Stifle, August 01977, University of Illinois CERL Report X-50"
[1]: https://www.ietf.org/rfc/rfc600.html
[2]: https://youtu.be/k79rIfcNDfg "Oral history of David Liddle, interviewed by Hansen Hsu and Marc Weber, 02020-02-04, at 20 minutes 37 seconds"
[4]: https://archives.library.illinois.edu/erec/University%20Archives/0713808/1974%20Nov%20X-15%20Plato%20IV%20Student%20Terminal%20Stifle.pdf "The PLATO IV Student Terminal, by Jack Stifle, November 01974, University of Illinois Computer-based Education Research Laboratory CERL Report X-15, originally titled ‘A Plasma Display Terminal’ and published in March 01970 and March 01971"

In 01977, although the PLATO V terminal expanded the Memory Address
Register set by a LDA request from 10 to 15 bits, but the only
increased the terminal’s RAM from from 2048 bytes of RAM to 8192 bytes
of RAM, plus 8192 bytes of ROM.  So, Liddle’s interview aside, I think
the memory plasma panel was still a killer advantage even in 01977,
though perhaps the cost was set too high for it to go mainstream.

These 8192 bytes of RAM were used in part to expand from 128 softfont
glyphs to 384 glyphs, and the base addresses of the softfonts could be
changed, allowing you to use *all* of the RAM for softfonts, but you
could also load 8080 code into it and run it on the terminal.  There
seems to have been no way to read pixels from the display, which would
have quintupled the total storage available to the program.

Inserting
---------

Anyway, back from the evolutionary dead end of PLATO to the
DECScope-style glass ttys and replaceable characters that modern
terminal emulators are emulating.

Replacing characters in this way was not ergonomically optimal for
human editing of text, since although we do occasionally replace some
text with other text consisting of the same number of characters, it’s
much more common to insert text, delete text, or replace text with
text of some other length.  So insertion became the standard response
to typing a key in text editors, thanks in part to Macintosh, though
in some sense Emacs and vi worked this way pre-Macintosh, and I think
Smalltalk as well.  (See file `pipelined-piece-chain-painting.md` for
some notes on how random-logic terminal hardware could have been
designed to handle this better.)

A torrent of pixels; why text?
------------------------------

Framebuffer-driven displays like the Alto on which Smalltalk was built
and like the Macintosh (“bitmap displays”, early on) have now become
so ubiquitous that other kinds of displays have mostly been forgotten;
and GPUs are now fast enough to do many mathematical operations per
pixel per frame, so you can recompute all the pixels every frame if
you want.  So now we can do whatever we want, and the critical
question is no longer what the hardware to do but what would be most
useful to do.

Given the ease with which we can sling around pixels nowadays, many
people are surprised at the continuing primacy of textual programming
languages, and even textual formatting languages like Markdown and
HTML.  My thought is that plain ASCII text has several big advantages;
two of them are:

1. A tiny gulf of execution: you may not know what your code needs to
   say, but once you do know what it needs to say, it isn’t difficult
   to figure out how to type it in.  If you want the code to say `if x
   == 3 {` then you press the “i” key, followed by the “f” key,
   followed by the space bar, etc.  You don't have to try to figure
   out which menu the "if" or the "==" is hidden inside of.

2. A tiny gulf of evaluation: similarly, you can tell what your code
   says, as long as none of the characters are confusingly
   homoglyphic.

However, there are some drawbacks: ASCII text is not very
information-dense, and it's hard to get a lot of
preattentively-processable information into it.  Consequently, we rely
rather heavily on mechanized refactoring tools and indentation.

One approach to solving this is keyboard bucky bits, printing more
characters on more sides of your keyboard keys.  In the early days of
APL this was an easy thing to do, and with the move to mass-market
keyboards and ASCII standardization in the 01970s it became
impractical.  Now, with the profusion of input method editors on
cellphones and cheap custom keyboards, it would be feasible again.

APL-style overstrike is another potential way to improve the
situation; by overstriking two or more characters into a bindrune like
⍞, ⍝, or ⍣, you can expand your symbolic vocabulary to some degree
without expanding the gulfs of execution and evaluation.

Unicode combining characters are a potential way to get similar
benefits, though you must always beware of h̴̢̧̢̩͉͕̥͍̼̭̣́ͥ̾ͥ̏͆̆ͯ́̕͡͞ë̶̴̷̡̯̗̳̫̗̭̖͓́̉͐̒̊̏ͤ͋́͠͝͝ ̸̵̧̡̧̣̤̯̬͚̻̯͖͌̓̄͂̌̋̾ͮ͢͟͠w̵̶̷̢̻͙͍̪̪̪͚̫ͩ̐̈́̋̂̏ͩ̃́͠͠͞h̷̡ͣ̀̆ͣ͌ͫ̇̆͏̷̶̢̯̻̬͉̜͖̩̠͞͠o̴̵̡͋ͭͦ̎ͬ̽̑͐̕͘͝͝͏͇͕͖̱̠̞͈̫ ̂́̌̈́͛̐ͣ̓͏̷̴̴̛̹̻͙͚̞͎̝̹̀̕͡ẅ̶̢̨̛̝̬̟̦͇͉̩̈́̑̉ͤ̏̓̾̀̕͜͞ͅaͧ̅̈́ͭ́̂ͧ̚͏̛͏̷̢̨̨͉̟̭͉͚̪̘̘͝ḯ̷̴̵̺̜͇̱̻̟̘̀͑ͤ͌̏ͨͧ́̕͘͟͜ͅt̐ͨ̿̃̔͗͛̄͏̵́͝҉̶͏̱̙͖͖̠̠̘̰͠s̬̭̖̩͎̯̮̒̐̿ͩ́̿̎̓̀̕͘͢͜͡͝͞ͅ ̶̿ͭ̑̈̓̃̓ͦ́҉̢̛͜͏̛͖̱͙̲͔̝͕͖b̢͌̔̿̓͊̉̌̈́͏̢̕҉̧̢̙̘̙͕̙̝͓̥͞e̴̡̢̢̝̣̼͕͓̟̱̫ͭͦ͂͛̊̆̐͐́̕͢͠h̴̷̡̢̗̹͇͙̯̜̮̱͑̔̓͑́͛̆̃͟͢͝͞i̶̸̶̡̧̲͓̙̗̯̤͕̭ͮ̃̆̆̑ͮ̓̀̚͜͜n͛̔ͫͭ͑̊ͪ̀͜͏̵̨̢̟̳̫̲͈̗̟͈̕͢͝d̸̢̧̨̡̛̐̅ͭ͛̈̊͑̂̕҉̘̲̘̮̬̬̦͚ ̷̶̷̴̶̢̪̞̟͉̰̮̱͙͑̾͐ͮ̿͛́̓́͢t̿̐͊ͤͯ̌ͨ͋͏̶̛̕͝҉̡̛̤͉̣͈̺̫̣̪hͭ̒ͮ̈́̇ͮ̔̐͘͏̵̴̢̠̲̪͈̝̟͚̩͘͟͡e̴̸̡̮̲̪̳̩̣̲̖̽̄̂̾͑̄̄́͜͡͠͝͠
̨̖̬͕̜̣̰͖̱̔̃ͫ̋̈͂̒ͧ̀́́͟͞͞͝w̸̷̵̛̜͇̟̜̭̩͙̲͛͊͐͂ͨ̄̏ͫ́͜͠͞a̷̢̡ͩ͋́̽͆ͪ̓͛͜͜͜͡҉̼̗̖͈͚̰̹̙l̈͒ͬ̊ͮ͑ͣ͛҉͝͏̕͘͜͞҉̠̜͉͚̻͚̭̠l̛̆̒ͨͪͧ͊́́҉̶̷̲̖̭͙̙̫͇̮̕͘͢͠.  They don’t extend all that far, they aren’t very orthogonal,
and they can be hard to read and hard to figure out how to type.

What if we go beyond overstrike?  There are more ways to combine and
modify existing characters?  Superscript and subscript, for example.
How about changing colors or fonts?  Stacking characters vertically?
Squishing or stretching characters vertically or horizontally?  You’d
have to learn where to find the “stack vertically” or “bold font”
command on your keyboard, or the toolbar, but once you did, you could
apply it to any character at all.
