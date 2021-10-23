I just watched [Lars Brinkhoff’s demo of PDP-10 programming in the DDT
debugger under ITS][0], ([cheat sheet for mostly using it as a
shell][2], [newbie guide to using it for debugging][3]) which is truly
astounding.  Why couldn’t GDB be half this good?

[0]: https://youtu.be/7Ub36q03vkc
[2]: https://github.com/PDP-10/its/blob/master/doc/DDT.md
[3]: https://github.com/PDP-10/its/blob/master/doc/debugging.md

Summary of the video
--------------------

Brinkhoff, an enthusiastic PDP-10 novice, demonstrates “programming in
the debugger”, a technique Minsky was famous for, interactively
writing a hello-world program in PDP-10 assembly (I think 7
instructions), incrementally, then saving the resulting memory image
as an executable.  He works by repeatedly executing the partly written
program; when it tries to execute uninitialized (zeroed) memory, it
halts and disassembles the offending instruction, and then Brinkhoff
adds assembly instructions to it, then continues execution.  In that,
it’s fairly similar to its contemporary interactive environments for
BASIC, FORTH, or LISP in the 01970s, and MS-DOS’s DEBUG.COM and
[CP/M’s DDT.COM][1] were capable of similar feats, although I don’t
think they had an easy way to initialize memory to all illegal
instructions or debug breaks.

[1]: http://www.gaby.de/cpm/manuals/archive/cpm22htm/ch4.htm

The UI seems to be designed for a teletype printing terminal, though a
full-duplex one (ESC is echoed as $, as in TECO and CP/M ED.COM),
which is pretty limiting; it’s impossible to have a live display of
*anything*, even the current program counter or registers.  And I
don’t want to do all my programming in assembly language, and
interactively patching the machine code of a broken or incomplete
program is not something I spend a lot of time on, and it’s what
Brinkhoff spends most of the video on.  So, what’s so great about it?

The ways DDT is head and shoulders better than GDB
--------------------------------------------------

What’s amazing to me is the stuff Brinkhoff can do *instantly*, which
don’t take up much of the video, but which make up *most* of what I do
in GDB.

### Examining memory ###

To see what’s at location (octal) 100, he types `100/`; DDT
immediately responds with the disassembled instruction at that
location, or, failing that, its numeric value, leaving the cursor `∎`
at the end of the line to permit more operations on either the
location (like putting an instruction there) or the value (like
following it to where it points in memory with another `/`:

    $g
    ILOPR; 100>>0   0/   0   0/   0
    100/   0   ∎

### Numeric display and label definition ###

In this case, he types `.=` to ask for the value of `.`, the current
location, interpreted numerically, and then `. go:` to define a new
symbol GO with that value, all without ever hitting Enter:

    100/   0   .=100   . go:   ∎

In a sense, the three spaces are like FORTH's ` ok` prompt, but don’t
send you to a new line.  (But at this point Brinkhoff hits Enter to go
to a new line anyway, for reasons I do not know.)

### Disassembling memory in GDB ###

A similar command to `100/` in GDB, but using a longer address since
0x40 is in the zero page Linux never maps:

    (gdb) x/i0x80495c5
       0x80495c5 <addr>:	add    (%eax),%al

Instead of `/`, one keystroke, I had to type `x/i↵`, 4 keystrokes,
with the address in the middle.

### Numeric value display ###

GDB stores the address in the convenience variable `$_`, so instead of
typing `.=` to see it (perhaps superfluous in this case, since GDB
automatically displayed it as part of the `x` output) I can type:

    (gdb) p $_
    $6 = (int8_t *) 0x80495c5

That’s `p $_↵`, 5 keystrokes instead of 2.

### Convenience variable creation in GDB ###

Now, if I want to store that in a new variable called `go` (I haven’t
found a way to get GDB to create new labels at runtime) instead of
`. go:` (4 keystrokes) I can type `p $go=$↵` (8 keystrokes), where `$`
is GDB’s name for the last value output by `p`.  (`set $go=$↵` is
silent and doesn't clobber `$`, but is more awkward to type.)

    (gdb) p $go=$
    $8 = (int8_t *) 0x80495c5

### Intermission: GDB is 10 strokes over par and in the sand trap ###

So at this point the golf score is 7 (key)strokes for ITS DDT, 17 for
GDB, not counting typing the address.  *Programming* golf is not a
good metric on which to compare *programming* languages, but in this
case we’re counting *user interface actions* that must be taken to
reach a goal.

But we haven’t really reached the same goal, because DDT will use the
label GO to make future disassembly more readable, and GDB won’t.

### Easy or hard variable and memory access ###

Brinkhoff’s next move is to see the value of GO `go=` (superfluous in
both GDB and DDT) and then examine memory there, `↵go/` (which I think
could have just been `/`):

    go=100
    go/   0   ∎

To do the same in GDB is 10 keystrokes instead of 7:

    (gdb) p $go
    $10 = (int8_t *) 0x80495c5
    (gdb) x $
       0x80495c5 <addr>:	add    (%eax),%al

(As it happens, the data I have stored there is actually a
`sockaddr_in` struct, but GDB doesn’t know that; it’s disassembling
because the last time I told it how to examine memory it was with
`x/i`.)

### Switching between alternate display representations: SIXBIT and `sockaddr_in` ###

Later after Brinkhoff has added an instruction, he disassembles the
same place again with `go/` and then continues on to disassemble the
next word (the PDP-10 was a 36-bit word-addressed machine) with, I
think, ^J, which displays the address relative to the most recent
defined label:

    go/   OPEN TYOC,
    GO+1/   0   ∎

Typing ↵ in GDB (or ^J) will also continue to disassemble the next
instruction, because it repeats the last command (with slight tweaks),
but using my convenience variable `$go` to contextualize it:

    (gdb) 
       0x80495c7 <addr+2>:	pop    %ds

That also isn’t really an instruction; it's actually the first byte of
a TCP port number.  Brinkhoff encountered a similar problem with a
variable he called TTY.  It packed two variables into a 36-bit word;
one is an 18-bit I/O unit number (?), and the other is the
three-character SIXBIT string “TTY”.  But DDT tries to disassemble it
as an instruction when he types `tty/`, treating them as an opcode and
an operand:

    tty/   TYOC,,646471   ∎

So, to change his view of the memory, he types an apostrophe `'` to
see it as SIXBIT:

    tty/   TYOC,,646471   '$1'  !TTY'   ∎

The `$1'` syntax DDT outputs is the same input syntax it supports for
SIXBIT strings, but Brinkhoff had terminated his with altmode (ESC,
`$`) which I think is mandatory.

As far as I can tell, the shortest way to do the corresponding thing
in GDB is `x/h$_↵`, 6 characters:

    (gdb) x $go
       0x80495c5 <addr>:    add    (%eax),%al
    (gdb) x/h$_
    0x80495c5 <addr>:       0x0002
    (gdb) 
    0x80495c7 <addr+2>:     0x961f

Here `h` means “halfword”, 16 bits, which is appropriate because the
first two fields in a `sockaddr_in` are 16-bit fields, though
unfortunately the port number is in network byte order, and the i386’s
byte order is not network byte order.

### Switching between alternate display representations: floats and ASCII strings ###

Evidently the `;` key in DDT prints a value as floating-point instead
of SIXBIT or octal or machine instruction or whatever.

Sort of amusingly, DDT doesn’t remember the types of the values
Brinkhoff stores; for example, the words starting at his label HELLO
are actually strings (in a different encoding, I think ASCII, that
supports lowercase but only gets five bytes per word, using `$1"`
instead of `$1'` in the UI).  So he has to tell it again.  Here’s the
part of the session where he first enters the strings, then starts
looking at them, and it starts disassembling them as instructions:

    hello/   0   $1"hello$
    HELLO+1/   0   $1" worl$
    HELLO+2/   0   $1"d

    $
    hello/    TLCE B,@466337(15)   ∎

At this point he presses `"` and sees the right view, then presses (I
think) ↵ to go to the next word, repeating the process:

    hello/   TLCE B,@466337(15)   "$1"hello$
    HELLO+1/   MOVES 13,@771331(15)   "$1" worl$
    HELLO+2/   TRZ 6,@200001(A)   "$1"d^M^J$   ∎

So to see those three words of ASCII, given the start address, he had
to type `/"↵"↵"`, 6 bytes.  In some sense GDB is a little better about
this sort of thing, part of which is because character data is much
less of a pain on a byte-oriented computer; I only need `x/s$_↵`, also
6 bytes, to change my view to NUL-terminated text:

    (gdb) x &text_plain
    0x80496e3 <text_plain>: 25972
    (gdb) x/s$_
    0x80496e3 <text_plain>:  "text/plain; charset=utf-8text/css; charset=utf-8application/pdf\r\n\r\n"

(Let’s forget about the `&` here for the time being; it’s a thing that
I constantly mess up, because even though GAS demands `$` prefixing,
when I’m programming in assembly I think of `text_plain` as being *the
address* where I set that label (or the value I EQU it to), but GDB
thinks `text_plain` means “the contents of memory at address
`text_plain`”; this is particularly confusing because `x/i main↵` will
in fact treat the symbol for function `main` as the memory address to
examine, rather than a place to look for a pointer to it.  But it’s
not clear which interpretation actually imposes more keystrokes on the
debugger user.)

### GDB UI mode errors ###

GDB’s cleverness here can lead to subtle mode problems in the UI,
because `/s` isn’t quite a unit size specifier as strongly as it is a
format specifier:

    (gdb) x/h$_
    0x80496e3 <text_plain>:	 u"整瑸瀯慬湩※档牡敳㵴瑵\x2d66琸硥⽴獣㭳挠慨獲瑥甽晴㠭灡汰捩瑡潩⽮摰൦ഊ\n"

Getting back to seeing memory as two-byte integers requires an
explicit output format, thus `x/dh$_↵` (7 keystrokes) instead of DDT’s
`=`:

    (gdb) x/dh$_
    0x80496e3 <text_plain>:	25972

### Stepping backwards and changing memory ###

Above I mentioned that in both GDB and DDT you can move forward in
memory you’re examining by just hitting ↵.  But later on Brinkhoff
steps *backwards* in memory to get back to an instruction he wants to
change, using apparently the two-keystroke sequence `^↵`:

    LOOP+4/   0   . die:
    die/   0   .value
    ^
    LOOP+3/   JRST LOOP   ^
    LOOP+2/   .IOT A,B   ^
    LOOP+1/   JUMPE B,   ∎

Stepping backwards over i386 instructions is probably too much to ask
for, since in numerous cases there are i386 instructions that are
proper suffixes of other i386 instructions.  But what about halfwords?
The best approach I’ve found is `x $_-1↵` (7 keystrokes instead of 2).

    (gdb) x/xh&addr
    0x80495c5 <addr>:       0x0002
    (gdb) 
    0x80495c7 <addr+2>:     0x961f
    (gdb) x $_-1
    0x80495c5 <addr>:       0x0002

Surely, in many cases, the whole necessity to step backwards is
avoided by GDB’s facility at dumping vaast tracts of ... memory:

    (gdb) x/20xh &bind_args
    0x80495b9 <bind_args>:  0x0000  0x0000  0x95c5  0x0804  0x0010  0x0000  0x0002  0x961f
    0x80495c9 <addr+4>:     0x0000  0x0000  0x6962  0x646e  0x2928  0x0000  0x0000  0x0500
    0x80495d9 <listen_args+5>:      0x0000  0x6c00  0x7369  0x6574

(The egregious display misalignment of the DDT output was bothering
me, but here we’ve caught GDB at it too.  Also, those lines are 86
characters wide.)

[In recent GDB 7.12, negative repeat counts have been added to `x`][1]
to allow you to examine memory backwards.  So you can start stepping
backwards through memory with something like `x/-1↵↵↵`, returning to
stepping forward with `x/1↵`.

[1]: https://stackoverflow.com/questions/34257162/gdb-how-to-examine-memory-backwards

But, in the video, Brinkhoff was navigating backwards in order to find
where he wanted to *set* something, a pointer to a label in fact,
although the place he was poking it into was an instruction.  I feel
like this is a thing you might reasonably want to do with GDB too.
For example, I might want to change the port number the server binds
to to 1536, which byte-swaps to 6; DDT is *really* designed for this
kind of thing, allowing you to type numbers or assembly code whenever
you want and just poking it into memory wherever you are, so you could
set a variable to 6 just by typing “6↵”.  Here’s what the interaction
looks like in GDB:

    (gdb) x/xh&addr
    0x80495c5 <addr>:       0x0002
    (gdb) 
    0x80495c7 <addr+2>:     0x961f
    (gdb) 
    0x80495c9 <addr+4>:     0x0000
    (gdb) x $_-1
    0x80495c7 <addr+2>:     0x961f
    (gdb) p*$_=6
    $19 = 6
    (gdb) x/3 &addr
    0x80495c5 <addr>:       0x0002  0x0006  0x0000

To set the current memory location to 6, I typed `p*$_=6↵`, 7
keystrokes instead of 2.  Or 6 keystrokes instead of 1, if we leave
out the actual value I’m setting it to.

Of course I don’t want to switch to DDT, I’m not insane
-------------------------------------------------------

Well, I mean, I *am* insane, just not in that particular way.  GDB
supports the computer I actually have, high-level programming
languages, and operating systems I actually want to use like Linux.
It’s scriptable, including in Python (as well as in its own UI command
language, which is not only unreadable but also by far the slowest
interpreter I’ve ever used) and I can sort of remedy the annoying fact
that it defaults to not disassembling the instructions it’s stopped
at, even for programs with no debug info where it obviously can’t show
me the high-level source, by launching its TUI with `layout asm` or
just `display/i $pc`.  It has time-travel debugging, though it’s far
too slow to use for anything but very short runs, and watchpoints,
which are fast.  It remembers not just one printed-out expression but
all of them.

Moreover, modern debugger UIs like WinDbg, radare2, and the IntelliJ
IDEA debugger offer lots of improvements, like expression watch
windows and graphical control-flow graphs.

Here’s an edited session where I was using GDB a few months ago:

    (gdb) p *seq       
    $30 = {capacity = 0, used = 93824992367072, arena = 0x0, elements = 0x5555555c1728}
    (gdb) s
    262             uint8_t b = 0;
    (gdb) 
    263             HCountedArray *seq = H_CAST_SEQ(p->ast);
    (gdb) n
    264             size_t digits_processed = 0;
    (gdb) p *seq
    $31 = {capacity = 4, used = 2, arena = 0x5555555bfbd0, elements = 0x5555555c17a8}
    (gdb) p $.elements
    $32 = (struct HParsedToken_ **) 0x5555555c17a8
    (gdb) p *$@2
    $33 = {0x5555555c1da8, 0x5555555c2558}
    (gdb) p *$[0]
    $34 = {token_type = TT_UINT, {bytes = {token = 0x7 <error: Cannot access memory at address 0x7>, len = 0}, sint = 7, uint = 7, 
        dbl = 3.4584595208887258e-323, flt = 9.80908925e-45, seq = 0x7, user = 0x7}, index = 0, bit_length = 0, bit_offset = 0 '\000'}
    (gdb) p *$$[1]
    $35 = {token_type = TT_UINT, {bytes = {token = 0xd <error: Cannot access memory at address 0xd>, len = 0}, sint = 13, uint = 13, 
        dbl = 6.4228533959362051e-323, flt = 1.821688e-44, seq = 0xd, user = 0xd}, index = 0, bit_length = 0, bit_offset = 0 '\000'}

It’s really thought-provoking that the things I do *most of the time*
in GDB, which require awkward commands full of hard-to-type line noise
characters, like following chains of pointers or getting an alternate
display of the thing I just looked at, require *dramatically* less
typing in *the debugger Stallman maintained and used on a daily basis
before he wrote the first version of GDB*, because they’re bound to
single-keystroke commands.  And there’s apparently no way at all to
add a label to an address once you figure out what it means so that
GDB will use it in its output.  I have no idea how this could have
happened!  My best guess is that he thought a DDT-like user interface
would be too alien to Unix programmers accustomed to adb or dbx, so
they wouldn’t use it.

Lessons for debuggers and similar programs
------------------------------------------

I think there are a few principles to extract here.

One is the use of single-keystroke commands for the most common
things; the difference between 7 keystrokes and 10 is maybe marginal,
but the difference between 1 keystroke and 4, or even 1 keystroke and
2, is enormous, if it’s something you’re doing frequently,
*especially* repeatedly.  Unfortunately, this clashes pretty strongly
with modern modeless UI conventions; the `/` key should always insert
a `/`, not do something like follow a pointer.  Some possible
compromises here:

- Insert the `/`, and then react to the textual change, which is sort
  of what DDT is doing.

- Use control-/ or alt-/.

- Use an onscreen button, perhaps contextually available.

(Other uses of DDT also followed this approach; instead of `ls↵` you
would just type ^F, and instead of `bg↵` or `%&↵` you would type ^P.)

Another is the importance of immediate feedback.  Even if 7 characters
like `p*$_=6↵` is a reasonable length for a command to set a memory
location (given how much less important the debugger is nowadays as a
way of loading data into memory), it would be better to display the
current contents of the memory once you get to `p*$_`, and maybe to
use a postfix operator (like DDT’s `/` or Pascal’s `^`) instead of the
prefix `*` operator used in C and Rust.  Like recent versions of
Android’s calculator app, you should compute and display the value of
any expression being entered whenever this has no side effects.

A thing that barely reared its head here is the importance of
reversibility for user interfaces; this is really the main reason I
don’t use debuggers much.  Following a pointer or stepping forward
through memory might be reversible (though I didn’t see cases of
anything like a “back” button for unfollowing pointers in Brinkhoff’s
DDT demo) but single-stepping a program rarely is, so when I’m using a
debugger I often go very slowly to avoid having to restart my debugger
session from the beginning.

By contrast, when the program runs fast enough, I can debug it by
progressively adding tests, assertions, and logging, and running it a
very large number of times, without ever having to slow down to avoid
stepping just one step too far and losing minutes or hours of work.
As computers have gotten faster and faster, this monotonic approach
has become more and more appealing.  A debugger in which almost all
actions could be undone (and in which the irreversible actions were
easily distinguishable) would allow me to use it much more quickly.

A *lot* of DDT’s UI’s advantage over GDB’s is its implicit focus on
“the current location” and “the current value”, analogous to “the
selection” in many GUI systems or “the top of the stack” in systems
like HP RPN calculators, Forth, and PostScript; this avoids GDB’s
requirement to explicitly name `$` or `$$` or `$_` all the time.  It’s
not yet clear to me to what extent this transfers to touchscreen UI
design, but it seems pretty central to keyboard UIs.  In csh I would
frequently use `$!` to avoid having to name the same file repeatedly
in subsequent commands, and in bash I use M-. all the time for the
same reason.  The big difference is that, in a debugger, the values of
interest are not numbers or filenames, but regions of memory with
associated interpretation information — you might say “types”, but it
might also include things like how many digits of floating-point
precision you want to display or whether child nodes should be
collapsed or expanded.

Another aspect of this is the ease with which DDT switches between
different presentations of the current value, with keys like `'`, `"`,
`=`, and `;`.  In DDT’s case, these are a fixed, closed set, and
entirely insensitive to context, but even more useful would be an
extensible set of pretty-printers like GDB has — obviously posing the
difficulty of how to assign keys to them, for a keyboard
interface — and perhaps the possibility of backtracking as parsers do.
