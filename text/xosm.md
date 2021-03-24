.xosm: experimental obvious stack machine
=========================================

This is an unfinished twigman outline of a simple computer — more
complex than its inspiration Calculus Vaporis, but perhaps more
practical.

> The foolish fill their coffee cups to the brim, in their greed
> unable to forgo a single drop unless the cup cannot hold it, and
> thus scald their hands when slightly jostled.  The wise use slightly
> bigger cups.

The .xosm is a virtual machine design with byte-addressable RAM, eight
32-bit architectural registers (X Y Z T PC CP S D), and 16-bit
instruction words.  It is intended to be nearly as minimal as possible,
but leave enough space at the top of the cup to avoid being penny-wise
and pound-foolish, to mix a metaphor.  Here are some of the pitfalls
I’m hoping to steer this ship between, to add two more incompatible
metaphors to this witch’s brew of too many cooks, with attempted
operationalizations:

- It should not be too hard to implement — it should take less than a day, or
  132 source lines of C, working from the spec and test suite, for
  which purpose it should have less than 100 instructions;
- It should not be too slow to interpret — not more than 16 clock cycles per
  bytecode instruction on a modern superscalar CPU;
- It should not be too slow if compiled — not more than 2 clock cycles per
  bytecode instruction on a modern superscalar CPU;
- It should not be too large if implemented in hardware — more than
  4096 logic gates;
- It should not be too awkward to program for by hand — not more than
  twice as much assembly code as for amd64, though probably more than
  twice as many instructions;
- It should not be too hard to compile C to, imposing neither an
  enormous performance penalty nor ridiculously complicated bytecode
  nor extremely complicated compilation tactics — no more than, say,
  four times worse than handwritten bytecode.
- It should not be too hard to debug programs for.

16-bit instruction words are a compromise.  They occupy about 50% more
space than 8-bit instructions (like Elisp or the 6502), but less than
32-bit instructions (like MIPS, SPARC, Lua, ARM, or RISC-V without the
C extension).  The instruction word consists of an opcode byte and an
operand byte, but most opcodes do not use operands.

Compared to 8-bit encoding, 16-bit encoding reduces the number of
cases where an instruction is followed by an immediate operand, and it
allows the use of 16-bit-wide memory without alignment efficiency
concerns; 32-bit immediates can be fetched in two memory operations
rather than the 4 that would be needed with 8-bit alignment.  The
opcode byte can use a simpler encoding that simplifies instruction
decode.

Compared to 32-bit encoding, 16-bit encoding uses a lot less space.

Operand registers
-----------------

The .xosm has a four-register operand stack, whose registers are called X,
Y, Z, and T (for time — introduced in the HP-35).  X can be usefully
thought of as the CPU’s accumulator.  Most instructions take implicit
arguments on this stack and return results there; for example, the `x +=
y` instruction (0x2b) adds Y to X, and the `x -= y` instruction
subtracts Y from X.  Each of these instructions also pops the stack.
Popping the stack consists of overwriting Y with Z and Z with T.  Oddly,
T, rather than retaining its value as you would expect, gets the old
value of X, as explained below in the section about reversibility.
There is a `;` instruction that just pops the stack without doing
anything else.

Some instructions push the stack instead before whatever other actions
they take.  Pushing the stack consists of overwriting T with Z (losing
the previous value of T), Z with Y, and Y with X.  For example, the `x
= *s` instruction (see below) pushes the stack before overwriting X
with a value loaded from memory at the address in index register S.
The `y = x` or `dup` instruction *only* pushes the stack
without doing anything else.  Immediate-load instructions like `x = 1`
push the stack before setting X to a
constant.  There are two immediate-load opcodes, one which sets X
to the operand byte, and one which is followed by a 32-bit immediate
argument to set X to.

Single-operand ALU instructions like `x = ~x`, `x++`,
and `x /= 2` neither push the stack nor pop it; they merely
overwrite the X register with their result.

The four-level operand stack permits the evaluation of even relatively
complex nested arithmetic expressions before having to fetch and store
temporaries in memory, as well as providing a more convenient way to
pass up to four parameters to subroutines than is common in assembly
languages.

Here’s a tentative full list of ALU/operand-stack instructions:

       x += y
       x -= y
       x &= ~y
       x &= y
       x ^= y
       x = ~x
       x = y  # ;
       y = x  # dup
       x = 0
       x++
       x--
       x += x  # x <<= 1
       x <<= 3
       x /= 2  # x >>= 1
       x /= 8  # x >>= 3
       x = k8  # 8-bit immediate
       x = k32 # 32-bit immediate

These are 17 ALU instructions, which seems like a reasonable set
compared to 16 in Wirth-the-RISC, 6 in Chifir, 21 in LuaJIT, 4 in
SWEET-16 if we categorize the comparisons as control-flow
instructions, and 7 in the MuP21 or F21.

XXX maybe provide rotates instead of shifts?

Pointer registers
-----------------

XXX from looking at the RTL this is still a
little muxier on the hardware side than having a single architectural
A register like the MuP21, and of course involves more instructions,
although maybe it’s better for software.  Maybe you could have a
“wielded pointer register” and an “alternate pointer register”.

The .xosm has two 32-bit pointer or index registers, S and D.  S
is used for reading from memory (loads), while D is used for writing
to memory (stores).  Normal load instructions push the stack and store
the result in operand register X, though there are two “leap”
instructions that store it instead in S or D; all the store
instructions write the contents of register X to memory before popping
the operand stack.  Commonplace address arithmetic can be done within
the S and D registers rather than requiring the use of the operand
stack; there are instructions for bumping them by small (8-bit)
immediate constants (“creep”), adding them to large (32-bit) immediate
constants, adding the program counter to them, shifting them left by 2
bits, and “leap”ping with the `d = *s` and `s = *s` instructions.

There are two instructions `x <=> d` and `x <=> s` to
transfer the index registers to and from the operand stack.  These
instructions exchange X with, respectively, D and S, without pushing
or popping the operand stack.

This segregation into fetch and store registers means that if you need
a call stack (as C does!) you need to allocate a memory address to
store your call stack pointer at.  So it might be worthwhile to add an
SP register and three instructions for it.

Tentatively here’s the index-register instruction set:

    *d = x
    x = *(u32*)s  # if we go to 16-bit words then this can have an offset field
    x = *(char*)s
    d = *s  # leap d
    s = *s  # leap s
    s += k8  # immediate constant; 8-bit and 32-bit formats
    s += k32
    d += k8
    d += k32
    s += pc
    d += pc
    s <<= 2
    d <<= 2
    x <=> d
    x <=> s

That’s 15 opcodes.

Control flow
------------

Like MIPS or RISC-V, there are no conditional flags, because the
conditional instructions work on the contents of the operand stack;
RISC-V chose this because it eases superscalar implementations, but
for my purposes the big advantage is that software implementations
don’t have to bend over backwards to compute lots of data that’s never
used, which is a really bug-prone thing to do.

The .xosm has two architectural registers for control flow, the program
counter PC and the continuation pointer CP, and a single control-flow
operation `yield`, which swaps them, and can thus function as either a
procedure call or return instruction.  There are three `yield`
instructions: unconditional (`else`), conditional on `x == 0`
(`if (x)`), and conditional on `x >= 0` (`if (x < 0)`).
The conditional instructions pop the operand stack.  To enable control
flow that goes beyond just two coroutines yielding back and forth,
there’s an `x <=> cp` instruction which exchanges CP and X,
which simultaneously loads in a new continuation pointer (for example,
pointing to another location within the same subroutine) and puts the
old one in a location where you can save it to memory.

XXX do conventional short jumps too?

This approach is inspired by Henry Baker’s COMFY-65 compiler and
the Warren Abstract Machine, although it’s also related to Calculus
Vaporis.  A very simple function like Forth’s `: triple dup dup +
+ ;` might be implemented as nothing more than `dup dup + + else`;
a nonrecursive function that calls other functions might save CP to a
static memory location on entry and restore it before yielding on exit.
I’d need more experience with the .xosm to really get a feel of what
prologues and epilogues to use.

Instruction 0x00 is the “halt” instruction, because if you’re
executing uninitialized memory that’s a bug.  I don’t know what it
should do exactly.

Tentative control-flow instruction set:

    if (x) ...
    if (x < 0) ...
    else
    halt

4 opcodes.

Reversibility
-------------

For debugging, backwards execution and efficient tracing and
checkpointing are obviously very desirable.  So many of the .xosm’s
operations are defined to erase as little information as possible,
reducing the volume of information that must be logged for a
reverse-executable trace.  The `yield` instructions erase only one bit
of information — whether the previous instruction execution was a
`yield` or not, and thus whether the previous program counter is in
PC-1 or in CP-1 — and because the two-operand ALU instructions save
both the result and one of the operands (the previous value of X,
which is saved in T) they are fully reversible as well if the
underlying ALU operation is.  The various register-swap instructions
are also fully reversible.  The non-reversible operations are:

- Everything that pushes the operand stack, including loads from
  memory and immediate-load instructions.  Immediate-load instructions
  not only erase the previous T value but also, when the immediate is
  not embedded in the opcode byte, the previous value of PC — some
  suffix of the immediate constant might also be a valid instruction.
- Store instructions.
- Irreversible ALU operations such as `x &= y`.
- `dup`, which you could consider an “irreversible ALU operation”.

This may also have implications for efficient hardware implementation,
as the tsunami in advance of the Landauer-limit earthquake seems to be
arriving already.

Twigman evaluation
------------------

This is 17+15+4 = 36 opcodes, which seems perhaps a bit more
oversimplified than I would like, but will probably grow to the size I
want when I get some experience with its deficiencies.

A couple of sample instruction implementations in an interpreter on a
64-bit machine might be:

    xor:
        tmp = y;
        y = z;
        z = t;
        t = x;
        x ^= tmp;
        goto *opcodes[mem[pc++] & 0xff];
    leap_d:
        d = mem[s];
        goto *opcodes[mem[pc++] & 0xff];

These probably work out to 9 and 6 instructions respectively,
including a jump with a failed prediction, so I think I’m within my
target performance zone for interpretation of 16 clock cycles per
bytecode.  It’s also 5 lines of C per opcode, but some of that can and
should be factored out into an inline function, and then it will
probably be within my lines-of-code complexity budget.

    xor:
        x ^= pop_operand_stack();
        goto dispath;

8 architectural registers is a good, practical, 8080ish size; we’d
also need a non-architectural instruction register I, a memory-address
register A, a memory-read register M, and some kind of microcycle
state machine.  32 bits may be a bit excessive for simple hardware
implementation; one flip-flop per bit means we need 256 flip-flops for
just the architectural registers.  If you implement it with an 8-bit
ALU and 8-bit data paths you can probably hit the 4096-gate target I
set at the top at the expense of a slowdown of 4× or so.

A rough sketch of the RTL:

    X <= ALU-output if ALU-instruction else
         operand-byte if load-immediate-8 else
         M if fetching-into-X else
         S if s-swapping else
         D if d-swapping else
         CP if cp-swapping else
         XXX if load-immediate-32 else
         X

    Y <= X if pushing else
         Z if popping else
         Y

    Z <= Y if pushing else
         T if popping else
         Z

    T <= Z if pushing else
         X if popping else
         T

    PC <= CP if yielding else
          PC+6 if immediate-32 else
          PC+2

    CP <= PC+2 if yielding else
          X if cp-swapping else
          CP

    S <= M if s-leaping else
         X if s-swapping else
         s-effective-address if s-creeping else
         S << 2 if s-shifting else
         S

    D <= M if d-leaping else
         X if d-swapping else
         d-effective-address if d-creeping else
         D << 2 if d-shifting else
         D

    A <= s-effective-address if loading else
         d-effective-address if storing else
         PC if fetching else
         0

    ALU-output = sum if adding else
                 diff if subtracting else
                 abj if abjuncting else
                 conj if anding else
                 xor if xoring else
                 negated if negating else
                 Y if discarding else
                 0 if zeroing else
                 incremented if incrementing else
                 decremented if decrementing else
                 double if doubling else
                 octuple if octupling else
                 half if halving else
                 eighth if eighthing else
                 tristate

    sum         = X + Y     # N - ½ full adders
    diff        = X - Y     # same
    abj         = X & ~Y    # N AND gates
    conj        = X & Y     # same
    xor         = X ^ Y     # N XOR gates
    negated     = ~X        # N NOT gates
    incremented = X + 1     # N half adders
    decremented = X - 1     # same
    double      = X << 1    # just wires
    octuple     = X << 3
    half        = X >> 1    # also just wires. unsigned
    eighth      = X >> 3

    yielding = unconditional-yield ∨ 
               zero-conditional ∧ X == 0 ∨
               sign-conditional ∧ X[31]

The “XXX if load-immediate-32” case and the A register point out that
sometimes extra cycles will be needed during which almost all of the
above will be paused, because it’s fetching an immediate
32-bit value (possibly unaligned).  If I want to build up an RTL
design incrementally I probably want to start with those troublesome
cases so the control state machine starts out as complicated as it’s
going to get.

But I think we can sort of reasonably estimate the above as about 27
N-wide 2-muxes or tristate buffers for control and another 14 for ALU
result selection, and another 9 or so for things I haven’t thought of
yet, 50 in all; here “N-wide” means whatever width the internal data
paths for 32-bit data are, which might be 32 bits for a fast
implementation or 4 or 8 bits for a small one.  The ALU needs about
16N gates, maybe a bit more for lookahead carry.  We can sort of
reasonably ballpark this at 400 gates of muxing for an 8-bit
implementation, plus 128 gates of ALU, which seems like an
unreasonably small ALU by comparison.  With 32-bit data paths these
would be 1600 gates of muxing and 512 gates of ALU.

There’s a separate N-wide AND for the `X == 0` condition and some more
muxes and adders for effective address computation, something like
this:

    s-effective-address = S + operand-byte if s-creeping else
                          S + PC if pc-relative else
                          S
    d-effective-address = D + operand-byte if d-creeping else
                          D + PC if pc-relative else
                          D

The instruction decode logic depends on the instruction encoding, but
the above strawman has it and the microcycle logic producing the
following control bits: `ALU-instruction`, `fetching-into-X`, `load-immediate-32`,
`load-immediate-8`, `s-swapping`, `d-swapping`, `cp-swapping`, `pushing`,
`popping`, `yielding`, `imm32`, `imm8`, `s-leaping`, `s-creeping`,
`s-shifting`, `d-creeping`, `d-shifting`, `loading`, `storing`,
`fetching`, `adding`, `subtracting`, `abjuncting`, `anding`, `xoring`,
`negating`, `discarding`, `zeroing`, `incrementing`, `decrementing`,
`doubling`, `octupling`, `halving`, `eighthing`,
`unconditional-yield`, `zero-conditional`, and `sign-conditional`.
That’s 38 control signals, and probably something like 9×38 = 342
two-input AND gates to compute them, if that’s how it’s done, or
possibly a much smaller number of wider AND gates.

So we’ve only accounted for about 1600+512+342 ≈ 2500 gates of an
internally-32-bit implementation, ten thousand transistors.  The 8
architectural registers and 3 non-architectural registers add 352
flip-flops, probably another 3000 transistors, for a total of 13000.
If that were the whole story, this design’s [transistor count] would
be between the 9000-transistor 8-bit 6809 and the 29000-transistor
16-bit 8086, both from 01978, nowhere near the 68000-transistor 68000,
which was 32-bit architecturally but 16-bit internally, much less the
190k-transistor 68020 (01984) or the 275k-transistor i386 (01985).
It’s even substantially smaller than the ARM 1 (25000 transistors,
01985), but it’s close to Chuck Moore’s 16-bit Novix NC4016 (16000
transistors, also 01985).  Most likely I just haven’t noticed the
majority of the transistors that are needed to make the .xosm actually
run.  Where are they?

[transistor count]: https://en.wikipedia.org/wiki/Transistor_count

(However, Moore’s later 21-bit MuP21 design (01994), one of the design
inspirations for for the .xosm, was only 7000 transistors, including an
NTSC-generation coprocessor.)

It probably isn’t extremely useful to keep a general-purpose CPU much
smaller than 16384 transistors, like 4096 2-input NAND gates, unless
your RAM is a drum or an acoustic delay line or something.  The COSMAC
VIP, the early personal computer where we get the CHIP-8 videogame
virtual machine design, shipped with 2 KiB of RAM, which was probably
6T SRAM: 16384 bits and 98304 transistors of RAM.  Now we’d use 16384
capacitors and 16384 transistors of DRAM, plus 128 6-transistor sense
amplifiers along the edge.  But Wozniak thought 4 KiB was the minimum
to run a usable BASIC on the Apple, and he was likely right, although
the x18 GreenArrays cores make do with 64 words of RAM (and 64 of ROM)
per core, forcing you to split all but the smallest programs across
multiple of the 144 cores on the chip.  If you already have 32768
components in your RAM, then whatever benefit you get from reducing
your CPU from 16384 components to 8192 is probably not worth the
sacrifices required.

File `risc-v.md` mentions that Claire Wolf’s PicoRV32 RISC-V design
can be configured to run in 761 slice LUTs on a Xilinx 7-series FPGA,
uses 48 LUTs as memory, and also 442 slice registers; I think those
are 4-LUTs, which can compute any arbitrary 4-input Boolean function,
so that’s roughly equivalent to 2300 2-input NAND gates and 500
flip-flops, which seems pretty comparable to the .xosm, actually, but
supporting interrupts and a wider range of operations and stuff.  I
should check out Wolf’s design.

picorv32.v is 1913 unique lines of Verilog so I’m not sure where to
start!  It’s enormous.  I think the interrupt controller is compiled
out in the small configuration I mentioned above, though.
