Writing about Veskeno, it occurred to me that the nearest equivalent
might not be Chifir, the Universal Machine of the Cult of the Bound
Variable, Lorie’s UVM, or even Brainfuck, but rather [TIC-80] and
[CHIP-8], or in general video game consoles:

> TIC-80 is a **FREE** and **OPEN SOURCE** fantasy computer for
> making, playing and sharing tiny games.

[TIC-80]: https://github.com/nesbox/TIC-80

> CHIP-8 programs are run on a CHIP-8 virtual
> machine. It was made to allow video games to be more easily
> programmed for [01970s 8-bit RCA 1802] computers. ... In 1990, a
> CHIP-8 interpreter called CHIP-48 was made for HP-48 graphing
> calculators so games could be programmed more easily.

[CHIP-8]: https://en.wikipedia.org/wiki/CHIP-8

And [Cowgod say]:

> Chip-8 is a simple, interpreted, programming language which was
> first used on some do-it-yourself computer systems in the late 1970s
> and early 1980s.

[Cowgod say]: http://devernay.free.fr/hacks/chip8/C8TECH10.HTM#1.0

[PICO-8], [2]:

> PICO-8 is a fantasy console for making, sharing and playing tiny
> games and other computer programs. ...  A fantasy console is like a
> regular console, but without the inconvenience of actual
> hardware. PICO-8 has everything else that makes a console a console:
> machine specifications and display format, development tools, design
> culture, distribution platform, community and playership. It is
> similar to a retro game emulator, but for a machine that never
> existed.

[PICO-8]: https://www.lexaloffle.com/pico-8.php?page=faq
[2]: https://www.lexaloffle.com/pico-8.php

The most crucial thing here is the “cartridge format”, an image file
format that includes everything a game needs to run, and that the
peripherals are fully specified, which is the case for Chifir but not
for the UM or Brainfuck.  This is true of consoles like the Nintendo,
too: you can write a game and, if it works on one Nintendo, you can be
reasonably sure it will work on other Nintendos too.  You don’t have
to worry that maybe some Nintendo can’t handle as many sprites, or
runs some instructions faster and screws up the game’s timing, or has
less RAM, or has a TSR installed that’s stealing cycles, or has a
garbage collection that’s too conservative and causes your game to run
out of memory and crash halfway through, or doesn’t interpret the
cartridge format in the same way.

The challenge for Veskeno is achieving this, for a “console emulator”
written by someone born after this body dies, who doesn’t have access
to a working Veskeno implementation, while enabling the format to
support applications that are sufficiently powerful to do things like
run Linux and Windows at a speed sufficient for artifact preservation,
if not everyday use.

To do this, it needs to specify the behavior of the peripherals used
for the user interface at a level of detail sufficient to permit real
usage; CHIP-8, for example, specifies the keyboard layout used by the
COSMAC VIP, designed by CHIP-8’s author, and Norbert Landsteiner
explains that the most difficult part of getting the [PDP-1 emulation
for Spacewar!][3] usable was emulating the afterglow of the P7
phosphor used on the CRT, an aspect Steve Russell specifically called
out for praise in his comments.

[3]: https://www.masswerk.at/spacewar/
