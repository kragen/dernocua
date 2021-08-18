What would a compact stack bytecode for C look like?  I think you
could usually manage to compile to about 3 bytes per line of C code,
which would enable you to run C programs of about 10kloc on an Arduino
or about 300kloc on an Ambiq Apollo3.

Why?
----

There are lots of microcontrollers around now, but for traditional
personal computing purposes they have more speed than needed and less
memory.  The 3¢ Padauk microcontrollers (the PMS150 family) as
described in file `minimal-cost-computer.md` in Derctuo has “512-4096
words of program memory and 64-256 bytes of RAM, all running at up to
16 MHz (normally 8 MIPS) ... running on 2.2–5 volts at 750 μA/MHz,”
though they’re out of stock everywhere last I saw.  As mentioned in
file `wearable-ekg.md`, the ATTiny1614 costs 82¢ from Digi-Key; it has
16KiB of program memory (8192 words) and 2048 bytes of RAM and runs at
20 MHz (≈20 MIPS).  (The formerly cheaper ATTiny25V-15MT is now out of
stock due to the Chipocalypse and its price has shot up enormously to
US$1.82 in quantity 1000.)  The [STM32F051C8T6 is still out of stock
at Digi-Key with a standard lead time of 52 weeks][0], and now the
[CKS32F051C8T6 is out of stock at LCSC too][1], but at least they have
the [GD32F130C8T6][2]: 64KiB program memory, 8KiB RAM, 72 MHz
Cortex-M3 (80 DMIPS?), US$3.25.  And the Ambiq Apollo3 mentioned in
file `energy-autonomous-computing.md` has 1MB Flash and 384KiB SRAM
and is a 48MHz Cortex-M4F, running at about 10 μA/MHz at 3.3 volts.

[0]: https://www.digikey.com/en/products/detail/stmicroelectronics/STM32F051C8T6/3064610
[1]: https://lcsc.com/product-detail/Other-Processors-and-Microcontrollers-MCUs_CKS-CKS32F051C8T6_C556574.html
[2]: https://lcsc.com/product-detail/GigaDevice_GigaDevice-Semicon-Beijing-GD32F130C8T6_C80735.html

In file `microlisp.md` and file `energy-autonomous-computing.md` I’ve
written about how to effectively use off-chip memory in order to kind
of bridge this gap somewhat.  Swapping in code or data from off-chip
Flash is a great deal faster than swapping from a spinning-rust disk
drive or loading overlays from a floppy, so it can be a lot more
transparent.

However, an alternative approach is to make more frugal use of the
internal memory, and in file `microlisp.md` (and in file
`tiny-interpreters-for-microcontrollers` in Dercuano) I explored
compact bytecode formats a bit.

The Microsoft Excel team wrote their own C compiler in the 01980s for
this purpose; as I understand it, to fit more functionality into PCs
of the time, such as the Macintosh, their compiler allowed them to
choose for each function whether to compile it to bytecode or to
native code.

[The MakeCode VM][3] reportedly consists of about 500 bytes of AVR
machine code:

> MicroPython and similar environments cannot run on the [Arduino] Uno
> due to flash [32 KiB] and RAM [2 KiB] size limitations.  We also ran
> into these limitations, and as a result, developed two compilation
> modes for AVR.  One compiles STS [Static TypeScript, a JS-like
> language] to AVR machine code, and the other (MakeCode VM) generates
> density-optimized byte code for a tiny (~500 bytes of code)
> interpreter.  The native strategy achieves code density of about
> 60.8 bytes per statement, which translates into space for 150 lines
> of STS user code.  The VM achieves 12.3 bytes per statement allowing
> for about 800 lines.  For comparison, the ARM Thumb code generator
> used in other targets achieves 37.5 bytes per statement, but due to
> the larger flash sizes we did not run into space issues.

[3]: https://www.microsoft.com/en-us/research/uploads/prod/2018/07/lctes18main-p12-p.pdf

In exchange for this 4.9× code compression, they accepted about a 6.4×
interpretive slowdown.

Chuck McManis [famously reverse-engineered the Parallax BASIC
Stamp][4], based on a PIC16C56, and found that it used a
variable-bit-length “bytecode” system to take maximum advantage of the
2048 bytes of its serial EEPROM.  Most of the “tokens” in the
“bytecode” corresponded straightforwardly to BASIC tokens, but some of
them were significantly swizzled around; `NEXT B0` compiles to `10111
CCCVVV VVVVVV F CCCVVV CCCVVV AAAAAAAAAAA` where CCCVVV encodes the
increment 1, VVVVVV encodes B0, F encodes +, the second CCCVVV encodes
the ending counter value (255, say), the third CCCVVV encodes the
starting counter value (0, say), and the final AAAAAAAAAAA encodes the
address of the statement to jump to (the first statement inside the
loop).

[4]: http://www.mcmanis.com/chuck/robotics/stamp-decode.html

How big is functionality?  The original [MacOS Finder was 46KiB][5]
and fit on a 400KiB floppy with MacOS (“System”) and an application
and a few documents, making it possible to use the Macintosh with a
single floppy, though drawing on the [128KiB of ROM including
LisaGraf/QuickDraw][6]; MacPaint was under 50 KB and consisted of
[5804 lines of Pascal and 2738 lines of assembly][7], but that
includes blank lines and comments and excludes MyHeapAsm.a and
MyTools.a.  A more reliable figure is 4688 lines of Pascal and 2176
lines of assembly, which is according to David A. Wheeler’s
“SLOCCount”.  If we figure that a line of Pascal is about 5 lines of
assembly, according to the folklore.org figures, that’s the equivalent
of 6351 lines of Pascal, and under 7.9 bytes of compiled code per
line; or, using SLOCCount figures, 5123 Pascal-equivalent lines and
under 9.8 bytes of compiled code per line.

If you could get 4 bytecode bytes per Pascal-level line of code, which
seems plausible but difficult, you could fit MacPaint into about
20 KB.

[5]: https://www.folklore.org/StoryView.py?project=Macintosh&story=The_Grand_Unified_Model_The_Finder.txt "The Grand Unified Model.  CC-BY-NC"
[6]: https://www.folklore.org/StoryView.py?project=Macintosh&story=MacPaint_Evolution.txt&sortOrder=Sort+by+Date&topic=QuickDraw "MacPaint Evolution.  CC-BY-NC"
[7]: https://computerhistory.org/blog/macpaint-and-quickdraw-source-code/ "MacPaint and QuickDraw source code, licensed for non-commercial use."

There’s a nonlinear benefit to this kind of thing, too: the
functionality of software comes more from interactions among the
components than from individual components.  If you can fit 6000 lines
of code into your Arduino, there are four times as many potential
interactions as if you can only fit 3000 lines of code in.

So, the primary objective is to fit more functionality into less
memory.  But a secondary objective is to add in-application
programmability to one-time-programmable devices like the PMS150C, and
make in-application programmability easier for Harvard-architecture
devices like the AVR and the GD32VF, which can’t execute native code
from RAM.

How?
----

Probably the right thing to do, to be able to run existing
microcontroller-friendly code, which is mostly written in C, C++, or
the Arduino dialect of C++, is to write a C compiler to some kind of
very compact bytecode, along with a bytecode interpreter for it.

A virtual machine designed for C probably needs a frame-pointer
register, but otherwise a registerless stack architecture will
probably result in more compact code.  A lot of the usual C compiler
optimizations aren’t useful on a stack machine, though dead-code
elimination, constant folding, and common subexpression elimination
may be valuable.

There’s a tradeoff between interpreter size and code size.  In the
MakeCode case, they evidently had about 9–10 KiB left for STS user
code, and by using 500 bytes of it for the interpreter they were
effectively able to increase the functionality that fit in memory by
almost a factor of 5.  But this is probably far from the optimum; if
by doubling the size of the interpreter they were able to increase the
code density from 12.3 to 10 bytes per statement, then instead of 800
statements, they would be able to fit 930 statements into the same
space.  How much further could you take that approach?

So it’s quite plausible that the right tradeoff for minimum space is
to use the *majority* of program memory for a really elaborate
interpreter.  But we can’t do this simply by adding common subroutines
as built-in interpreter instructions written in native code; we can
certainly vector some built-in interpreter instructions to common
subroutines, but if we want to use minimum space, we should still
encode that common subroutine in bytecode, not native code.  (For the
most part, anyway — for example, while you could implement
multiplication in terms of addition and bit tests, for example,
invoking a multiply instruction is going to be a lot simpler, and
similarly for most functionality commonly provided as part of the CPU
instruction set.)  So what should we put in the interpreter proper?
Other than optimizations, of course.

Probably a big part of the answer is “weird addressing modes”.

For really tiny chips like the PMS150C with its 1024 instructions of
ROM, probably only 512-768 instructions or so of interpreter are
affordable; obviously 1024 instructions would not be.  So I think it’s
worthwhile to think about what kind of kernel bytecode interpreter you
could fit inside that kind of constraint, even on an 8-bit machine,
before decorating it with richer functionality for machines with
larger memory.

Elisp and Smalltalk bytecodes commonly have an operand field within
the byte, 3–5 bits of operand.  Often these operands are indexes into
tables (of constants, selectors, or functions) that are associated
with the method or function, and which can contain more data than the
bytecode itself.

I tend to think that variable-bit-length instructions like the BASIC
Stamp are hard to justify, particularly on machines like the AVR where
you apparently need to write a 5-iteration loop to shift a 16-bit word
by 5 bits.  But variable-byte-length instructions are probably easy to
justify, where perhaps you have 3 bits of operand within the
instruction byte, perhaps another operand byte following, and perhaps,
with a different opcode, two operand bytes following.

Making a global table of all subroutines is probably a win.  Talking
to solrize about the subject, they made the observation that if a
subroutine is called zero times, it can be omitted from the compiled
program; if it is called once, it can be inlined; and if it is called
twice or more, then it is quite plausibly a savings to put its address
into a global table of subroutines, and refer to it elsewhere only
with an index into this subroutine table.  For example, on the
ATMega328 in the Arduino Uno, a word-aligned address anywhere in the
32-KiB program memory requires 14 bits, but if you can only fit 800
lines of user code in there, you can’t plausibly have more than 160
user subroutines, so you only need 8 bits for a subroutine-table
index.  Or 7.32 bits, really.  So by putting a 16-bit address into the
subroutine table, you can invoke the subroutine with an 8-bit operand
instead of a 14-bit operand, which probably saves you the 2 bytes that
it cost to put it into the subroutine table.  If there are more than 2
calls to it, you’re in the black.

Exceptions might include where there was one reference to the
subroutine, but you were passing its address rather than invoking it,
so it can’t be inlined; or where the alternative to a global table of
subroutines is a local table (like the ones Smalltalk and Elisp use)
that can be indexed with fewer bits, like 3–5 instead of 7.32.

If a subroutine table is too large for a compact operand field to
index into it, the subroutines can be sorted so that the ones with the
most callsites come first, and the losers who drew the long addresses
can’t be invoked without a 2-byte calling sequence.

We can improve in density over Elisp bytecode to the extent that we
can exclude K&R C’s generic variadic calling convention, where the
caller knows how many parameters are passed but the callee doesn’t,
and every function returns a value — because we don’t have to encode
the number of arguments at the callsite, and we don’t have to
explicitly discard void return values.  A function header can specify
how many arguments there are, automatically moving them from the
operand stack into the function’s stack frame.

C is pretty thorough about having byte-oriented memory.  IIRC you can
do pointer arithmetic between nested struct members.  You’re not
supposed to do pointer arithmetic between different things in the same
stack frame.  On the other hand, you could very reasonably allocate
word-sized local variables in a separate area, even if you take their
addresses.

Sketches
--------

Let’s look at some examples of what bytecode-compiled subroutines
might look like.  My examples so far, with a strawman bytecode I made
up as I went along, are respectively 3.4, 3.1, 7.5, and 3.4 bytes per
source line of code.  I think this is a compelling argument that 4
bytes per line of code is usually achievable and 3 bytes might be.

### DrawTxScrap ###

Here’s a Pascal subroutine from MacPaint; C and this Pascal are almost
identical.

    {$S        }
    PROCEDURE DrawTxScrap(dstRect: Rect);
    VAR i:          INTEGER;
        myProcs:    QDProcs;
    BEGIN
      KillMask;   { not enough room in heap for mask and font }
      ClipRect(dstRect);
      EraseRect(dstRect);
      InsetRect(dstRect,2,0);
      dstRect.right := Max(dstRect.right,dstRect.left + txMinWidth);
      dstRect.bottom := Max(dstRect.bottom,dstRect.top + txMinHeight);
      SetStdProcs(myProcs);
      thePort^.grafProcs := @myProcs;
      myProcs.textProc := @PatchText;
      i := CharWidth('A');  { swap in font }
      HLock(txScrapHndl);
      TextBox(txScrapHndl^,txScrapSize,dstRect,textJust);
      HUnlock(txScrapHndl);
      ClipRect(pageRect);
      thePort^.grafProcs := Nil;   { restore to normal }
    END;

What would this ideally look like in bytecode?

This only has three local variables, but two of them are structs
(records in Pascal).  `dstRect` evidently has `.top`, `.bottom`,
`.left`, and `.right` members, which are probably integers, and it’s
evidently being modified by `InsetRect`, which I guess must take it as
a var parameter.  The `@` operator, an Apple extension, takes the
address of a variable like `&` in C, just as passing a var parameter
does implicitly.  `thePort` is a global variable imported from
elsewhere; `txMinHeight`, `txMinWidth`, `txScrapHndl`, `textJust`, and
`pageRect` are five of the 128 global variables in this file; and
`PatchText` is a procedure defined just above.

The repeated use of the same `txScrapHndl` and `thePort` globals makes
me think that maybe a function could have an associated vector of
referenced global variable indices so that such repeated references
only cost one byte.

Maybe in idealized bytecode assembly this would look something like this:

    ; This next line compiles to a procedure header structure with bit
    ; fields.  This procedure takes 8 bytes of “blob arguments” and
    ; has another 18 bytes of local blobs immediately after them; both
    ; of these are in the blob part of the activation record.  It also
    ; takes 1 word of word (register-sized) arguments, which go into
    ; the word part of the activation record.
    PROCEDURE DrawTxScrap argblob=8 localblob=18 localwords=1
    globals txScrapHndl, thePort
        call KillMask
        lea_blob 0       ; load address of offset 0 into stack frame blobs
        call ClipRect
        lea_blob 0
        call EraseRect
        ;      InsetRect(dstRect,2,0);
        lea_blob 0
        tinylit 2        ; push constant 2 (coded in a 3-bit field in the bytecode)
        tinylit 0
        call InsetRect
        ;       dstRect.right := Max(dstRect.right,dstRect.left + txMinWidth);
        loadword_blob 1  ; load word from stack frame blobs at offset 1 word (.right)
        loadword_blob 0  ; load .left
        loadglobal txMinWidth
        add
        max
        storeword_blob 1 ; store max result into .right
        ;       dstRect.bottom := Max(dstRect.bottom,dstRect.top + txMinHeight);
        loadword_blob 3  ; load .bottom
        loadword_blob 2  ; load .top
        loadglobal txMinHeight
        add
        max
        storeword_blob 3
        lea_blob 8          ; load @myProcs (@myProcs)
        call SetStdProcs
        lea_blob 8          ; load @myProcs (@myProcs)
        loadglobal thePort
        storeword_offset 5  ; using thePort value from top of stack, offset 5 words and store result
        ;      i := CharWidth('A');  { swap in font } (oddly this return value i is not used, but let’s compile it anyway)
        lit8 65             ; 'A'
        call CharWidth
        storeword 0         ; store into i, in the stack frame word-sized variables (rather than blobs)
        loadglobal txScrapHndl
        call HLock
        ;      TextBox(txScrapHndl^,txScrapSize,dstRect,textJust);
        loadglobal txScrapHndl  ; not sure if this is a var parameter, I’ll assume so
        loadglobal_long txScrapSize  ; this variable is 32 bits
        lea_blob 0
        loadglobal textJust
        call TextBox
        loadglobal txScrapHndl
        call HUnlock
        lea_global pageRect     ; again, assuming this is a var parameter; if not we must memcpy
        call ClipRect
        ;      thePort^.grafProcs := Nil;   { restore to normal }
        tinylit 0
        loadglobal thePort
        storeword_offset 0
        ret

That’s 44 bytecode instructions, so 44 opcode bytes; how many operand
bytes?  All but 5 of them have immediate operands, but probably none
of those operands need to be more than 1 byte, so we have at most 39
operand bytes.  10 of them are call instructions (or 12 if we count
the `max` instances); there are 211 functions and procedures declared
in this file, including EXTERNAL procedures, and each of them is only
called once in this function, so plausibly those 10 call operations do
need an operand byte to index into a global table of subroutines.
Another 10 operands are global variables; of these half (thePort twice
and and txScrapHndl three times) are referenced more than once and
could thus be usefully listed in the function’s global-references
vector so they could be referenced in a single byte; the other 5 would
require a separate operand byte.  Of the other 19 operands, most are
small integers between -3 and 3 or between 0 and 6, so they could be
packed into a 3-bit immediate field; the only exceptions are 8, 8, and
65, so there would be 3 more bytes of operands, and 16 bytecodes with
embedded operands.

So that’s 3 numeric operand bytes, 5 global-index operand bytes, and
10 function-call operand bytes, for 18 operand bytes, and 44+18 = 62
bytes of bytecode.  The procedure header is probably 2 bytes, the
procedure's address in the global subroutine table is another 2 bytes,
and then you have two global-variable offset bytes, so all in all the
subroutine is probably about 68 bytes.  This corresponds to 20
non-comment non-blank source lines of Pascal code, or 3.4 bytes per
line, which is about 2.9 times the density of the original MacOS
compiled program.

(All this is assuming that there are few enough bytecode operations to
fit into a single byte.  The above code already uses `call`,
`lea_blob`, `tinylit`, `loadword_blob`, `loadglobal`, `add`, `max`,
`storeword_blob`, `lit8`, `storeword`, `storeword_offset`, and `ret`,
which is 12, to 9 of which we are imputing this 3-bit operand field;
furthermore supersymmetry implies the existence of such undiscovered
massive particles as `storeglobal`, `loadbyte_blob`, `storebyte_blob`,
`loadword_offset`, `storebyte_offset`, and `loadbyte_offset`, which
bring us to 15 of the 32 major-opcode slots filled, plus leptons such
as `subtract`, `multiply`, `divide`, `mod`, `bitand`, `bitor`, `xor`.
So I think it’s pretty plausible that we’ll have plenty of opcode
space, but it’s something to watch.)

It’s a little bit unclear how blob parameters are supposed to get
passed here.  Do we pass them in word-sized chunks on the operand
stack, or is there a separate blob stack or something?  If we assume
that the bytecode interpreter is equipped to go look at the function
header in memory when it’s interpreting a call, it might be reasonable
to put the `call` bytecode *before* the arguments so that the
interpreter can allocate the callee’s stack frame, allowing arguments
to be poked directly into it in the appropriate places instead of
needing to be copied there on subroutine entry.

### strlcpy ###

Here’s `strlcpy`, originally from OpenBSD, but this version is the
copy from avr-libc, for which SLOCCount reports 26 lines of code,
condensed down to 14 lines for ease of reading:

    size_t strlcpy (char *dst, const char *src, size_t siz) {
            register char *d = dst;
            register const char *s = src;
            register size_t n = siz;

            if (n != 0 && --n != 0) {
                    do { if ((*d++ = *s++) == 0) break; } while (--n != 0);
            }

            if (n == 0) {
                    if (siz != 0) *d = '\0';
                    while (*s++)
                            ;
            }

            return(s - src - 1);
    }

Unlike the straight-line Pascal code above, this has a bunch of
control flow, seven conditional jumps.  (Normally a `while` would also
involve an unconditional jump, but in this case the body is empty.)

This has six local variables, all word-sized, but only five of them
are live at once; `dst` passes the torch to `d` early on, which can be
eliminated by the compiler.

If we try encoding it in the same bytecode as before with a fairly
traditional compilation strategy, I think it looks like this:

    PROCEDURE strlcpy argwords=3 localwords=2
        loadword 1       ; load argument 1, src
        storeword 3      ; store into word variable 3, s
        loadword 2       ; load siz (argument 2)
        storeword 5      ; n
        jz 5, 1f         ; jump to label 1 if word variable 5 is 0
        decrword 5       ; decrement word variable 5
        jz 5, 1f
    2:  loadword 0       ; d, preparation for *d++
        incrword 0       ; d++
        loadbyte_offset 0 ; dereference pre-incremented pointer
        dup              ; this will be used in an assignment whose result value is used
        loadword 3       ; s
        incrword 3
        storebyte_offset 0
        jztos 1f
        decrword 5       ; --n
        jnz 5, 2b        ; repeat do loop if word variable 5 still isn’t 0
    1:  jnz 5, 1f        ; if (n == 0)
        jz 2, 3f         ; if (siz != 0) using word variable 2
        tinylit 0        ; '\0'
        loadword 0       ; d
        storebyte_offset 0 ; *d =
    3:  loadword 3       ; s
        incrword 3       ; ++
        loadbyte_offset 0
        jnztos 3b
    1:  loadword 3       ; s
        loadword 1       ; src
        subtract
        tinylit 1
        subtract
        ret

That’s 32 bytecode instructions.  4 of these are zero-operand leptons
(dup, subtract, subtract, ret), 7 are conditional jumps (6 with 2
arguments), and the other 21 are the same kind of one-operand one-byte
operations that dominated DrawTxScrap.  Maybe `jnz 5, 2b` gets encoded
with 5 in the 3-bit immediate field, indicating that it’s looking at
local register-sized variable 5, and jumping to label 2, looking
backwards, if it is Not Zero.  The byte offset to label 2 is encoded
in a following operand byte, within the range ±127; if it’s -128 then
two more operand bytes follow giving the real jump offset.  `jnztos`
jumps if the top of stack is 0 instead of if a local variable is zero;
I think the way to do this is that if the 3-bit immediate field is 0
through 6, it tests that variable, but if it’s 7, it tests the top of
stack (and pops it).  By contrast, in the other baryonic operations, I
was thinking 7 would indicate that the immediate parameter is in the
following byte, but if you want to test a local variable that’s higher
than 6, then you could just `loadword` it and then `jztos`.

So, in addition to demonstrating the previously speculative
`loadbyte_offset` and `storebyte_offset` operations, this imposes new
baryonic opcodes on us: `incrword`, `decrword`, `jz`, `jnz`, and
probably `js`, `jns`, and `jmp`, bringing the total from 15 to 22 out
of 32.

So with the above-suggested encodings, we have 7 jump-offset argument
bytes, 2 bytes of procedure header, and 2 bytes of global subroutine
table entry, for a total of 32+7+2+2 = 43 bytes.  That’s 1.7 bytes of
bytecode per SLOCCount line or 3.1 bytes per physical non-blank line
in the above.

You could very plausibly squeeze this down a bit more.  The 8086’s
LOOP instruction provides the decrword/jnz functionality, its LODSB
instruction provides the `loadword/incrword/loadbyte_offset`
functionality, and its STOSB instruction provides
`loadword/incrword/storebyte_offset`.  And of course the final
expression being returned admits all sorts of optimizations, including
a decrement-top-of-stack operation or an increment or decrement to one
of the variables being subtracted.

In an alternative direction, note that this code has 7 jump
instructions, comprising 14 bytes, but only 4 labels; following Henry
Baker’s COMFY-65, if we could use a 1-byte instruction to set the
destination to jump to on failure or success, maybe we’d only need 4
bytes of jump destinations instead of 7.

### `proc_get_cam_register_3` ###

Let’s look at something a little less nice and pretty:
`proc_get_cam_register_3` from
`linux-2.6/drivers/staging/rtl8192e/rtl_debug.c`:

    static int proc_get_cam_register_3(char *page, char **start,
                              off_t offset, int count,
                              int *eof, void *data)
    {
            struct net_device *dev = data;
            u32 target_command = 0;
            u32 target_content = 0;
            u8 entry_i = 0;
            u32 ulStatus;
            int len = 0;
            int i = 100, j = 0;

            /* This dump the current register page */
            len += snprintf(page + len, count - len,
                            "\n#################### SECURITY CAM (22-31) ######"
                            "############\n ");
            for (j = 22; j < TOTAL_CAM_ENTRY; j++) {
                    len += snprintf(page + len, count - len, "\nD:  %2x > ", j);
                    for (entry_i = 0; entry_i < CAM_CONTENT_COUNT; entry_i++) {
                            target_command = entry_i + CAM_CONTENT_COUNT * j;
                            target_command = target_command | BIT31;

                            while ((i--) >= 0) {
                                    ulStatus = read_nic_dword(dev, RWCAM);
                                    if (ulStatus & BIT31)
                                            continue;
                                    else
                                            break;
                            }
                            write_nic_dword(dev, RWCAM, target_command);
                            target_content = read_nic_dword(dev, RCAMO);
                            len += snprintf(page + len, count - len, "%8.8x ",
                                            target_content);
                    }
            }

            len += snprintf(page + len, count - len, "\n");
            *eof = 1;
            return len;
    }

This is 36 lines of code, which I think is maybe a little too much for
a sketch, so I’ll try just the first half of it, plus enough cleanup
to get it to compile, which brings it to 22 lines:

    static int proc_get_cam_register_3(char *page, char **start,
                              off_t offset, int count,
                              int *eof, void *data)
    {
            struct net_device *dev = data;
            u32 target_command = 0;
            u32 target_content = 0;
            u8 entry_i = 0;
            u32 ulStatus;
            int len = 0;
            int i = 100, j = 0;
            len += snprintf(page + len, count - len,
                            "\n#################### SECURITY CAM (22-31) ######"
                            "############\n ");
            for (j = 22; j < TOTAL_CAM_ENTRY; j++) {
                    len += snprintf(page + len, count - len, "\nD:  %2x > ", j);
                    for (entry_i = 0; entry_i < CAM_CONTENT_COUNT; entry_i++) {
                            target_command = entry_i + CAM_CONTENT_COUNT * j;
                    }
            }
            return len;
    }

Let’s say our C is a 16-bit-pointer platform, like Arduino, so the
`u32` items all go into blobland instead of wordland.  As before, I’ll
elide the copy from `data` to `dev`.  And I’ll assume that the
interpreter by default initializes all local variables to zero, which
is a reasonable thing for a C implementation to do.

    PROCEDURE proc_get_cam_register_3 argwords=6 localwords=4 localblob=16
    const "\n#################### SECURITY CAM (22-31) ##################\n "
    const "\nD:  %2x > "
        lit8 100
        storeword 8  ; i.  note that this implies a separate operand byte with 3-bit immediate fields
        loadword 0   ; page *
        loadword 7   ; len
        add
        loadword 3   ; count *
        loadword 7
        subtract
        loadconst 0  ; the string *
        call snprintf
        loadword 7
        add          ; len +=
        storeword 7
        ; for (j = 22; j < TOTAL_CAM_ENTRY; j++) {
        lit8 22
        storeword 9
    1:  loadword 9
        lit8 32      ; TOTAL_CAM_ENTRY
        subtract
        jstos 1f     ; if result negative, skip loop
        incrword 9
        loadword 0   ; *
        loadword 7
        add
        loadword 3   ; *
        loadword 7
        subtract
        loadconst 1  ; the other string *
        call snprintf
        loadword 7
        add
        storeword 7
        tinylit 0    ; *
        storebyte_blob 0  ; entry_i = 0.  In the blob because u8 *
    2:  loadbyte_blob 0   ; *
        lit8 8            ; CAM_CONTENT_COUNT
        subtract
        jstos 1f
        loadbyte_blob 0   ; *
        tinylit 1         ; *
        add
        storebyte_blob 0  ; *
        ; target_command = entry_i + CAM_CONTENT_COUNT * j;        
        loadbyte_blob 0   ; *
        lit8 8            ; CAM_CONTENT_COUNT
        loadword 9        ; j
        multiply
        storelong_blob 0  ; target_command = *
        jmp 2b
    1:  loadword 7
        ret

This is a mess!  But a workable mess.  49 bytecode instructions.  Of
these, 11 have no operands at all; another 14, marked with `*` above,
have operands that can be packed into a 3-bit field; the remaining 24
each need an operand byte.  73 bytes of bytecode!  But by itself that
would be pretty okay for 21 lines of code (3.8 bytes per line).  What
really kills us here is the 64-byte literal string and the other
12-byte literal string, plus a constant vector (probably two 16-bit
pointers).  All that, plus the 2-byte procedure header and 2-byte
entry in the global subroutine table, adds up to 73 + 64 + 12 + 4 + 2
+ 2 = 157 bytes.  That’s 7.5 bytes per line of code!  Those two string
literals *doubled* the space this truncated subroutine needs.

I think that if I were to add in the missing 15 lines of code, this
would get slightly less ugly, maybe another 64 bytes, which would get
the total down to about 4.4 bytes per line of code.  But it would be
easy for someone to write code that really does have that many quoted
`#` signs in it.

Of course, this *particular* code probably has no business running on
a microcontroller, even if I hadn’t snipped out the `read_nic_dword`
call that does the real work; it’s part of a Linux device driver for a
Wi-Fi card that I think requires a PCI bus to operate at all.  But I
think it’s a good representative of workaday C code.

### `File_pipe2file` ###

This is from `php5-5.4.4/ext/fileinfo/libmagic/compress.c`:

    protected int
    file_pipe2file(struct magic_set *ms, int fd, const void *startbuf,
        size_t nbytes)
    {
            char buf[4096];
            ssize_t r;
            int tfd;
    #ifdef HAVE_MKSTEMP
            int te;
    #endif

            (void)strlcpy(buf, "/tmp/file.XXXXXX", sizeof buf);
    #ifndef HAVE_MKSTEMP
            {
                    char *ptr = mktemp(buf);
                    tfd = open(ptr, O_RDWR|O_TRUNC|O_EXCL|O_CREAT, 0600);
                    r = errno;
                    (void)unlink(ptr);
                    errno = r;
            }
    #else
            tfd = mkstemp(buf);
            te = errno;
            (void)unlink(buf);
            errno = te;
    #endif
            if (tfd == -1) {
                    file_error(ms, errno,
                        "cannot create temporary file for pipe copy");
                    return -1;
            }

It... goes on for another 36 lines from there; that’s 30 lines.  It’s
not super plausible that we could fit the PHP interpreter into an
Arduino, but we could surely fit it into an Ambiq Apollo3.  The
`protected` suggests that this is not actually C at all but C++, but
it’s pretty close.  Let’s see what this would look like in the
strawman bytecode assembly.  Let’s imagine we *do* `HAVE_MKSTEMP`.

    PROCEDURE file_pipe2file argwords=4 localwords=3 localblob=4096
    const "/tmp/file.XXXXXX"
    const "cannot create temporary file for pipe copy"
    const 4096
    globals errno
        lea_blob 0     ; buf
        loadconst 0    ; filename template
        loadconst 2    ; 4096, sizeof buf
        call strlcpy
        drop           ; discard result, because of course that makes sense when calling strlcpy
        ; #ifndef HAVE_MKSTEMP drops the next N lines
        lea_blob 0     ; tfd = mkstemp(buf); 
        call mkstemp
        storeword 6
        loadglobal errno ; te = errno
        storeword 7
        lea_blob 0
        call unlink
        drop
        loadword 7       ; errno = te
        storeglobal errno
        loadword 6
        tinylit -1
        subtract
        jnz 1f
        loadword 1
        loadglobal errno
        loadconst 1
        call file_error
        tinylit -1
        ret
    1:

So that’s 25 bytecodes, of which the four `call`s and the two
references to `te` require an operand byte.  The others can all
reasonably be 1 byte each, so we have 31 bytes of bytecode, plus 43 +
17 = 60 bytes of literal strings, 6 bytes of constant table, 1 byte of
global vector, 2 bytes of procedure header, and 2 bytes of global
subroutine table entry, 31 + 60 + 6 + 1 + 2 + 2 = 102 bytes, nearly ⅔
in those two stupid strings.  Still, that’s 102 bytes for 30 lines of
code: 3.4 bytes per line.  But only because 12 of those 30 lines were
discarded by the preprocessor!

Like most of the PHP interpreter, this is a good example of really
pretty shitty C code that people nevertheless want to run, and run
correctly.

### Insertion sort ###

Here’s an excerpt from the latest .c file I wrote in my dev3
directory, which does an insertion sort on an array of ints (obviously
a programming exercise):

    static inline void
    swap (int *x, int *y)
    {
      int tmp = *x;
      *x = *y;
      *y = tmp;
    }

    void
    isort(int *a, size_t n)
    {
      for (size_t i = 1; i < n; i++) {
        for (size_t j = i; j > 0; j--) {
          if (a[j-1] > a[j]) swap(&a[j], &a[j-1]);
        }
      }
    }

This counts as 16 lines of source code, although that’s pretty
generous!  Let’s suppose our compiler does in fact inline `swap` and
cancel out the resulting `*&`:

    void
    isort(int *a, size_t n)
    {
      for (size_t i = 1; i < n; i++) {
        for (size_t j = i; j > 0; j--) {
          if (a[j-1] > a[j]) {
             int tmp = a[j];
             a[j] = a[j-1];
             a[j-1] = tmp;
          }
        }
      }
    }

This is the first example we’ve seen that does real pointer
arithmetic, the kind where you have to multiply by the size of the
pointer.  Using just the strawman bytecode above and no CSE I think it
looks something like this:

    PROCEDURE isort argwords=2 localwords=3
        tinylit 1
        storeword 2    ; i
    1:  loadword 2
        loadword 1     ; n
        subtract
        jstop 2f
        loadword 2
        storeword 3    ; j
    3:  jz 3, 4f       ; if j == 0, exit loop
        loadword 0     ; a for a[j-1]
        loadword 3     ; j-1
        tinylit 1
        subtract
        tinylit 2      ; sizeof int
        multiply
        add
        loadword_offset 0
        loadword 0      ; a[j]
        loadword 3
        tinylit 2
        multiply
        add
        loadword_offset 0
        subtract          ; if >
        js 5f
        loadword 0        ; tmp = a[j]
        loadword 3
        tinylit 2
        multiply
        add
        loadword_offset 0
        storeword 4       ; tmp
        loadword 0        ; a[j] = a[j-1]
        loadword 3
        tinylit 1
        subtract
        tinylit 2
        multiply
        add
        loadword_offset 0
        loadword 0
        loadword 3
        tinylit 2
        multiply
        add
        storeword_offset 0
        loadword 4        ; a[j-1] = tmp
        loadword 0
        loadword 3
        tinylit 1
        subtract
        tinylit 2
        multiply
        add
        storeword_offset 0
    5:  decrword 3     ; j--
        jmp 3b
    4:  incrword 2
        jmp 1b
    2:  ret

This is 61 bytecode instructions, which I think is pretty horrific.  5
of them are jumps which take an operand byte, so 66 bytecode bytes in
all, plus the usual 4 bytes of per-subroutine overhead, for 70 bytes.
That’s 4.4 bytes per line of code.

However, there are a couple of directions to go to improve this.  One
is that, despite the examples above, neither `a[j-1]` nor `for (...; i
< expr; i++)` is actually at all unusual in C.  We could support the
first one with leptonic bytecodes to decrement top of stack and to do
base+index addressing:

        loadword 0       ; a[
        loadword 4       ; j
        decrtos          ; -1
        loadword_indexed ; ]

And we could support the loop with a baryonic bytecode similar to the
8086 LOOP instruction mentioned earlier, but for up-counting loops; if
at the bottom of the loop:

        loadword 1       ; n
        countup 2, 1b    ; i < n? if so increment and jump back to label 1

For the full C semantics, which loops zero times when n is 0, you’d
need to initialize the counter to one *less than* the initial value
and then unconditionally jump to that loop trailer.  Alternatively you
could reverse the sense of the conditional jump, put it at the top of
the loop, and put the unconditional jump at the end of the loop.

The Forth way to handle counting loops is different; it stores the
loop counters, limits, and increments on the return stack instead.
This would require more analysis from the compiler (it has to verify
that the loop limit is a constant expression and that the loop counter
is only read from, insert an UNLOOP instruction at breaks) but it
would allow you to write the outer loop with two new leptonic
instructions as follows:

        tinylit 1        ; start value
        loadword 1       ; n, loop limit
        fortoloop        ; stash loop counters and loop address on the loop stack
        ...
        continue         ; update loop counter, maybe jump to address after fortoloop

And the inner loop as follows:

        i                ; get outer loop counter as start value
        0                ; loop limit
        tinylit -1       ; step
        fortosteploop
        ...
        continue

Instead of having Forth-like i, j, and k instructions, you could maybe
stick the loop counter in a regular word-sized local variable, using a
baryonic for-loop instruction.

XXX

Finally, you could actually do common subexpression elimnation XXX