I’m looking at [the RISC-V instruction set][0].  It seems kind of
boring, on purpose, in a good way, kind of like C and Golang.  There’s
intentionally very little that’s clever.

[0]: https://riscv.org/wp-content/uploads/2017/05/riscv-spec-v2.2.pdf

Overall it looks very pleasant, much simpler to learn than amd64, and
maybe not even more verbose.  You have 32 int registers (though x0 is
a hardwired zero) and 32 float registers and a load-store
architecture.  There’s a [nascent assembly programmer’s manual][11].
You can [run it at 400+ MHz in 809 LUTs on a Xilinx 7-series FPGA][6]
or [even run it on a Lattice iCE40-HX8K][8] ([multiple different
designs even][9])or [in even fewer LUTs with a slower design][7], or
even with Linux support, and there’s a [1.4 GHz full-custom quad-core
dev board][10], [a software emulator on amd64 with only a 3×
slowdown][19], and a [108MHz GigaDevice GD32VF103 microcontroller][12]
with a US$6 Seeed Studios devboard.

[6]: https://github.com/cliffordwolf/picorv32 "PicoRV32 (small): 761 slice LUTs, 48 LUTs as memory, 442 slice registers"
[7]: https://github.com/jens-na/VexRiscv "VexRiscv smallest: Artix 7 372 Mhz 568 LUT 603 FF"
[8]: https://pingu98.wordpress.com/2019/04/08/how-to-build-your-own-cpu-from-scratch-inside-an-fpga/
[9]: https://github.com/grahamedgecombe/icicle
[10]: https://abopen.com/news/a-look-at-the-risc-v-pc-from-sifive/ "HiFive Unmatched"
[11]: https://github.com/riscv/riscv-asm-manual/blob/master/riscv-asm.md
[12]: https://github.com/SeeedDocument/Sipeed-Longan-Nano/blob/master/res/GD32VF103_Datasheet_Rev1.0.pdf
[19]: https://github.com/rv8-io/rv8-io.github.io/blob/master/index.md#benchmarks

The 145 pages of the user-level instruction set manual plus the 91
pages of the [privileged ISA manual, Volume II][15] compare quite
favorably to the 262 pages of the [MOSTek MCS6500 family programming
manual][16] or [the 332 pages of the Z80 User Manual][17].

[16]: https://archive.org/details/6500-50a_mcs6500pgmmanjan76
[17]: https://www.zilog.com/docs/z80/um0080.pdf

There are some surprises, though.  There’s hardware threading
(“harts”, suggesting that perhaps a memory space should be called a
“forest”), with a concurrency mechanism called “LR/SC” that’s new to
me, and no condition flags.  (The opcode listing is not, as I first
thought, omitted from the instruction set manual, but consigned to the
six-page Chapter 19, plus seven privileged instructions in chapter 5
of Volume II.)  The `lui` load-upper-immediate instruction has a
20-bit immediate, so the other immediate-load instructions have only
12-bit immediates.  Some of the bit fields in the instruction encoding
are scrambled.  And it uses NaN-boxing to support multiple
floating-point formats on the same chip.

ABI
---

RISC-V defines [a standard ABI][1] as well as the instruction set,
because of their experience that more than just an ISA was needed to
get the benefits of a large software ecosystem.  The calling
convention is that the return address is passed in x1, the stack
pointer is x2, x3 and x4 are gp “global pointer” and tp “thread
pointer” respectively, x5 to x7 are caller-saved temporary registers
t0 to t2, x8 is the (callee-saved) frame pointer fp aka s0, x9 is
callee-saved s1, x10 to x17 are argument/return registers a0 to a7,
x18 to x27 are callee-saved registers s2 to s11, and x28 to x31 are
caller-saved t3 to t6.

The weird split putting s2–11 after a0–7 is apparently to map the
arguments into the 8 registers most broadly accessible from RVC
compressed instructions (p. 70).

There are alternative conventions for processors with and without
floating-point registers.

It’s mostly what you’d expect: C on RV64 is LP64, eight arguments in
registers a0 to a7, everything else pushed on the stack, with the
earliest non-register argument pushed last to facilitate C varargs.
There are a few surprises: C `char` is unsigned.  32-bit unsigned ints
are sign-extended to 64 bits on RV64.  Alignment padding for stack
arguments affects assignment of arguments to registers.  Return values
of more than two registers are returned in memory, with a pointer to
the memory passed as an extra argument prepended to the list.  The
stack pointer must always be 16-byte aligned even on RV32 and RV64.

[1]: https://riscv.org/wp-content/uploads/2015/01/riscv-calling.pdf

Flags and condition codes
-------------------------

I’m surprised that it has no condition-code flags.  The authors
explain that this was one of their reasons for not using the OpenRISC
1000 instruction set (p. 15, 24 of 145 of the instruction set spec):

> OpenRISC has condition codes and branch delay slots, which
> complicate higher performance implementations.

Instead there are `beq`, `bne`, `blt`, `bltu`, `bge`, and `bgeu`
instructions, which compare two registers and conditionally jump by an
immediate ±4KiB offset (p. 17), as done in PA-RISC and the ESP32’s
Xtensa (p. 18, where the alternatives are discussed).

This seems like it might complicate multi-precision arithmetic; the
authors explain a workaround (p. 13, 25 of 145):

> We did not include special instruction set support for overflow
> checks on integer arithmetic operations in the base instruction set,
> as many overflow checks can be cheaply implemented using RISC-V
> branches. Overflow checking for unsigned addition requires only a
> single additional branch instruction after the addition: `add t0,
> t1, t2; bltu t0, t1, overflow`.
> 
> For signed addition, if one operand’s sign is known, overflow
> checking requires only a single branch after the addition: `addi t0,
> t1, +imm; blt t0, t1, overflow`. This covers the common case of
> addition with an immediate operand.
> 
> For general signed addition, three additional instructions after the
> addition are required, leveraging the observation that the sum
> should be less than one of the operands if and only if the other
> operand is negative.
> 
>            add t0, t1, t2
>            slti t3, t2, 0
>            slt t4, t0, t1
>            bne t3, t4, overflow

This would seem to imply that, on a straightforward in-order machine,
addition and subtraction of multi-precision two’s-complement numbers
is almost an order of magnitude slower than on a conventional machine
with condition codes.  The MuP21’s approach of having an extra carry
bit in its internal CPU registers (21 bits in the MuP21 case, 33 or 65
bits in the RV32I or RV64I case) seems perhaps more reasonable; it
would eliminate the concern about complicating higher-performance
implementations.

Instruction word format
-----------------------

There are only a small number of instruction layouts (named with
letters: **R**egister/register, **I**mmediate/register, **S**tore,
**U**pper immediate, **B**ranch, and **J**ump), which is refreshing,
and the choice to reserve two bits in the fixed-width 32-bit format to
indicate instruction length brilliantly avoids the complications of
ARM Thumb “interworking” between Thumb code and non-Thumb code.  I
haven’t yet tried to compare the code density of the variable-length
RV64IC or RV32IC instruction formats, but I’m optimistic that they
will provide Thumb-2-like code density, which would be a unique
advantage in the 64-bit world, now that Aarch64 has abandoned Thumb.

The S-type, B-type, and J-type instructions include immediate fields
in a slightly weird permutation.  In response to the observation that
sign-extension was often a critical-path logic-design problem in
modern CPUs, they always put the immediate sign bit in the MSB of the
instruction word, so you can do sign-extension before instruction
decoding is done, but this leads to the J-type format imm[20] ||
imm[10:1] || imm[11] || imm[19:12] || rd || opcode, with a ±1MiB
PC-relative range, and an only slightly-less-surprising B-type format,
with a ±4KiB range.

They justify this by saying (p. 13):

> By rotating bits in the instruction encoding of B and J immediates
> instead of using dynamic hardware muxes to multiply the immediate by
> 2, we reduce instruction signal fanout and immediate mux costs by
> around a factor of 2. The scrambled immediate encoding will add
> negligible time to static or ahead-of-time compilation. For dynamic
> generation of instructions, there is some small additional overhead,
> but the most common short forward branches have straightforward
> immediate encodings.

U-type instructions, of which there are only two (`lui` and `auipc`),
have a 20-bit immediate field, but I-type and S-type instructions
(used for things like `addi` and `slti` and, notably, memory loads and
stores) have only a 12-bit immediate field.

ALU instructions
----------------

Surprisingly, there are no bit rotates (they suggest on p. 85 that
these might be added in the “B” extension) and no abjunction, and
multiplication and division are optional extensions.

It supports floating-point, and it spends 22 pages on this, which I am
going to comprehensively ignore.

Prologues and epilogues
-----------------------

The hardware calling convention stores the return address in a link
register instead of on the stack, and the standard ABI defines quite a
lot of callee-saved registers, and there’s no ARM-like store-multiple
instruction (p. 72 explains how they considered and rejected this), so
a typical prologue is relatively long, for example:

    addi sp, sp, -12
    sw ra, 0(sp)
    sw a0, 4(sp)
    sw s0, 8(sp)

And the epilogue is similar.

There’s an intriguing suggestion on p. 16 about factoring this out
with “millicode”:

> The alternate link register supports calling millicode routines
> (e.g., those to save and restore registers in compressed code) while
> preserving the regular return address register. The register x5 was
> chosen as the alternate link register as it maps to a temporary in
> the standard calling convention, and has an encoding that is only
> one bit different than the regular link register.

This suggests you could replace the above with something like `jal
prologue_a0_s0, x5` or `li t2, 1; li t3, 1; jal prologue_variadic,
x5`, which would indeed reduce code size.  You could implement
ARM-like bitmap-driven “load multiple” and “store multiple”
instructions that way.

The S-type encoding used for stores has the same number of bits of
each type as the I-type encoding used for instructions such as `addi`
and loads, but they are in different places, so that if there’s a
destination register, it’s always indicated in bits 11 to 7, and if
there are source registers, they are always indicated in bits 24 to 20
and 19 to 15.  I guess the idea is to avoid a possible additional
level of muxing.

The “RVC” or “C” extension described later also has a couple of
instruction formats specifically designed to cut the size of these
prologues and epilogues in half.

OS stuff
--------

There’s a [page on the OSDev Wiki][4] with an introduction.

[4]: https://wiki.osdev.org/RISC-V

There’s a `scall` instruction (now `ecall`) for trapping into the
kernel, and three privilege modes: **U**ser mode, **S**upervisor mode,
and **M**achine mode.  There are correspondingly three versions of
`iret`: `uret` from any mode if you have the “N-extension” (not yet
finished, p. 101) to enable user-mode trap handlers, `sret` from
S-mode (or M-mode), and `mret` only from M-mode.

There are 4096 “CSR”s, control/status registers, 1024 per mode
(including 1024 reserved for hypervisors, I guess?  There used to be
an “H” mode that has now been removed), and accessing one you aren’t
allowed to will trap.  These include things like floating-point
rounding mode and exception state, the trap vector (I guess for
setting up interrupt handlers and other trap handlers?), and cycle
counters.  The [minimal set of CSRs is like 12 or 16 bits][2].

[2]: https://youtu.be/fxLXvrLN5j "Privileged ISA, Esperanto Technologies"

The virtual memory setup seems super simple.

The smallest protection unit is 4-KiB pages, though there’s some kind
of large page support; there’s an `addr_space_id` field in the “SATP”
CSR (“supervisor address translation and protection”) that specifies
which address space you’re in so you can context-switch without
flushing your TLB I guess.  RV32 has 2 levels of page tables and
32-bit physical addresses, so I guess that’s 1024-way branching at
each level (Vol. II, p. 68, §4.3.1); RV64 has 3 or 4 levels of 512-way
branching and respectively 39 or 48 virtual address bits (“Sv39” and
“Sv48”), and then there’s something called “RSVD” which may or may not
be another name for RV128.

An Sv32 (Vol. II, p. 67, §4.3) page table entry is 32 bits; bits 31:20
(12 bits) are “PPN[1]” (“physical page number”), bits 19:10 (10 bits)
are “PPN[0]”, there are two bits reserved, and then 8 bits DAGUXWRV.
XWR are permissions; if all are 0, the PTE is a non-leaf PTE.  G is 1
if the PTE is global to all address spaces, and U is 1 if the PTE is
accessible in U-mode.  D and A are Dirty and Accessed bits, and “V” is
a “valid” bit.  The bottom N bits of the “SATP” CSR are the “page
table root physical page number” for the current task (whose
`addr_space_id` is more of those bits).  This is documented in
Vol. II, p. 63, §4.1.12.

Interestingly, U-mode pages are normally not readable or executable in
supervisor mode, although there’s an override bit to make them
readable.

There’s also a “physical memory attributes” thing (Vol. II, p. 43,
§3.5) that sounds like MTRRs, and a “physical memory protection” thing
that lets you irreversibly lock some memory regions at boot.

Trap handlers, including interrupts, page faults, and other
exceptions, are set up with the “xtvec” CSR (for x in U, S, or M, I
guess; vol. II, p. 27, §3.1.7; `stvec` in particular is documented in
vol. II, p. 57, §4.1.4) pointing to the trap handler address, or
optionally to a table of instructions (if the bottom 2 bits of `xtvec`
are set to 01).  There is an “xcause” CSR that tells you which
interrupt it was, even without the table.  And four more related “x\*”
CSRs.  There are currently nine interrupts defined and 12 exceptions:
misaligned instruction (0), instruction access fault (1), illegal
instruction, (2), breakpoint (`ebreak`, previously `sbreak`) (3), load
address misaligned (4), load access fault (5), store address
misaligned (6), store access fault (7), environment call (8),
instruction page fault (12), load page fault (13), and store page
fault (15).  The misaligned-address faults are present because,
although misaligned fetches are architecturally allowed, you’re also
allowed to implement them with a trap handler instead of in hardware
☺.  (And the same is true of page table traversal.)  All the “store”
faults may also be “AMO” faults, which I think is “atomic memory
operation”.

All this is, I think, specified in the [RISC-V privileged-instructions
spec, which is Volume II][15].

[15]: https://github.com/riscv/riscv-isa-manual/releases/download/Ratified-IMFDQC-and-Priv-v1.11/riscv-privileged-20190608.pdf

There’s an S-mode `sfence.vma` instruction for, I guess, flushing
TLBs — for the current “hart”.

### Counters, timing, and nondeterminism ###

There’s a 64-bit timer counter (the `time` CSR, I think, 0xC01,
p. 108) that can provide an interrupt at a predetermined wall-clock
time; each hart has its own comparator, configured in M-mode.
*Reading* the timer CSR is *privileged* and traps to M-mode (at least
in U-mode), which means you can remove it as a source of
nondeterminism from user processes.  I’m not sure if the same is true
of the performance counters like `instret`, the instructions-retired
counter (0xC02), and `cycle` (0xC00); they say (p. 36):

> We mandate these basic counters be provided in all implementations
> as they are essential for basic performance analysis, adaptive and
> dynamic optimization, and to allow an application to work with
> real-time streams. Additional counters should be provided to help
> diagnose performance problems and these should be made accessible
> from user-level application code with low overhead.

However, on p. iv of “Volume II: RISC-V Privileged Architectures”,
they explain that one of the changes from version 1.9.1 to version
1.10 was so that “S-mode can control availability of counters to
U-mode”.

(I don’t know how you can both have a 64-bit timer CSR *and* have only
12 or 16 bits of total CSRs...  maybe the dude meant RV32E.)

Hmm, the timer in question actually seems to be the memory-mapped
`mtime` register (vol. II, p. 32), coupled with `mtimecmp` which posts
a timer interrupt when `mtime` exceeds it.

Aha, here’s the poop on the counter enabling (vol. II, p. 34):

> The counter-enable registers `mcounteren` and scounteren are 32-bit
> registers that control the availability of the hardware
> performance-monitoring counters to the next-lowest privileged mode. ...
> 
> When the CY, TM, IR, or HPMn bit in the `mcounteren` register is
> clear, attempts to read the `cycle`, `time`, `instret`, or
> `hpmcountern` register while executing in S-mode or U-mode will
> cause an illegal instruction exception. When one of these bits is
> set, access to the corresponding register is permitted in the next
> implemented privilege mode (S-mode if implemented, otherwise
> U-mode).
> 
> [analogously for `scounteren`]
> 
> Registers `mcounteren` and `scounteren` are WARL registers that must
> be implemented if U-mode and S-mode are implemented. ...
> 
> The `cycle`, `instret`, and `hpmcountern` CSRs are read-only shadows
> of `mcycle`, `minstret`, and `mhpmcountern`, respectively. The
> `time` CSR is a read-only shadow of the memory-mapped `mtime`
> register.

So *yes*, the OS (or M-mode code) can hide timers from user code to
deny it nondeterministic behavior.

### Booting ###

Julian Stecklina says [QEMU boots RISC-V with OpenSBI firmware][5] and
can load an ELF kernel with `qemu-system-riscv64 -M virt -bios default
-device loader,file=kernel.elf`.

[5]: https://x86.lol/generic/2020/01/01/riscv-intro.html

Hardware threading
------------------

I don’t know what’s going on here but there is a `fence` instruction
for synchronization betweent threads, a `fence.i` instruction for JIT,
but apparently no instructions to spawn or terminate “harts”.  There’s
some kind of “IPI” interprocess interrupt mechanism for nonconsensual
IPC: you set the USIP bit (or maybe SSIP or MSIP) in another hart with
memory-mapped I/O in M-mode, although this is tricky when an OS might
be concurrently descheduling a hart.

I never did find anywhere that it says how to start or stop a hart.
There’s a CSR `mhartid` that tells you what the current hart ID is, so
maybe all the harts are running all the time?

RV32E embedded
--------------

For embedded systems, like maybe soldering irons, 1024 bits of integer
architectural registers might be a lot (??) so they defined a smaller
profile with only 16 registers and no counters.  I guess that means
you don’t get a6 and a7, nor s2–11 and t3–6.

The whole chapter about this is only a page and a half long.

RV64I
-----

The 64-bit extension is similar to amd64 in that the normal
instructions now work on 64-bit registers, and there are new
instructions like `addiw` or `sltiw` which work on only the low 32
bits, and a `lwu` instruction that loads a 32-bit value and
zero-extends it.  `addiw rd, rs, 0`, to sign-extend a 32-bit value to
64 bits, has an alias `sext.w`.

I suspect that loading a 64-bit non-PC-relative constant will require
using an ARM-style “constant pool” rather than the `lui`/`addi` pair
needed for 32-bit constants.

This is reasonably compatible, but not totally; it might not be
feasible to generate machine code that can do the same thing on either
RV64I or RV32I, aside from having some sort of conditional jump.  But
with the exception of `slli` and `sari` and the like, most of the
instructions can just ignore the upper 32 bits if you don’t care about
them.

Multiplication and division
---------------------------

The standard `mul` operation is only 32×32 → 32, but then there are
`mulh`, `mulhu`, and `mulhsu` operations for various ways of computing
the high 32 bits of the result.  RV64 has a `mulw` as well.
Analogously `div` has `rem`, `divu`, `remu`, `divw`, `divuw`, `remw`,
and `remuw`, but it does not take a double-precision dividend.

Division by zero or divide overflow does not raise an exception.

Atomics
-------

The atomic instruction set doesn’t provide compare-and-swap, or even
LL/SC, but rather something called “load-reserved/store-conditional”
and an “atomic fetch-and-op” facility.  This part seems to be in flux,
related to something called “RCsc” or “release consistency”.

LR “registers a reservation” on a memory address and reads a word from
it; SC writes a word to a memory address, “provided a valid
reservation still exists on that address” (p. 40, 52 of 145).  I guess
if someone else writes to the address, that demolishes your
reservation, so your later SC will fail; this is an alternative to CAS
that avoids A–B–A bugs, though they say it’s more vulnerable to
livelock in other designs that aren’t RISC-V.

It’s not clear whether *read* accesses from another hart to the
reservation will cause it to fail.

They give the following implementation of CAS in terms of LR/SC
(p. 42):

        # a0 holds address of memory location
        # a1 holds expected value
        # a2 holds desired value
        # a0 holds return value, 0 if successful, !0 otherwise
    cas:
        lr.w t0, (a0)        # Load original value.
        bne t0, a1, fail     # Doesn’t match, so fail.
        sc.w a0, a2, (a0)    # Try to update.
        jr ra                # Return.
    fail:
        li a0, 1             # Set return to failure.
        jr ra                # Return.

(`jr rs` here is “jump register” (p. 110): `jalr x0, rs, 0`.)

The atomic “fetch-and-ops” are atomic swap, add, and, or, xor, max,
maxu, min, and minu (p. 43), which points out the curious fact that
min and max are not provided as standard ALU operations.

They give a three-instruction example of a critical section using
`amoswap.w.aq`, `bnez`, and `amoswap.w.rl`.

“RVC” compressed instructions
-----------------------------

Chapter 12, p. 67 (79 of 145), explains a Thumb-2-like scheme,
providing a 16-bit version of the instruction when:

> * the immediate or address offset is small, or
> * one of the registers is the zero register (x0), the ABI link register (x1),
>   or the ABI stack pointer (x2), or
> * the destination register and the first source register are identical, or
> * the registers used are the 8 most popular ones.

It turns out, though, that the last two are actually an “and” rather
than an “or”, and the conditions are actually considerably more
restrictive than the above implies.

There’s an opcode map on pp. 81–83.

They point out that the Cray-1 also had 16-bit and 32-bit instruction
lengths, following Stretch, the 360, the CDC 6600, and followed by not
only ARM but also MIPS (“MIPS16” and “microMIPS”) and PowerPC “VLE”,
and that RVC “fetches 25%-30% fewer instruction bits, which reduces
instruction cache misses by 20%-25%, or roughly the same performance
impact as doubling the instruction cache size.”  I’m not sure how
that’s possible.

There are eight compressed instruction formats.

Much to my surprise, the eight registers accessible by the three-bit
register fields in the CIW (immediate wide), CL (load), CS (store),
and CB (branch) formats are *not* the *first* eight registers, but the
*second* eight registers, x8–15!  These are callee-saved s0–1 and the
first argument registers a0–5.  The CR (register–register), CI
(immediate), and CSS (stack store) formats have full-width five-bit
register fields.  (The CJ format doesn’t refer to any registers.)

Complementing the stack-store format are stack-load instructions
(p. 71) using the CI format with a 6-bit immediate offset, which is
prescaled by the data size (4, 8, or 16 bits).  These index only
upward from the stack pointer, institutionalizing the
otherwise-only-conventional downward stack growth.  The
immediate-offset field in the stack-store format is also 6 bits and
treated in the same way.  And there’s a thing called `c.addi16sp`
which adds a signed multiple of 16 to the stack pointer, that is,
allocates or deallocates stack space.

So in a 16-bit instruction you can load or store any of the 32 integer
registers to any of 64 stack slots (if you’ve allocated that many),
and you can do a two-operand operation with either two registers or a
register and an immediate.  It’s the more general load, store, and
branch formats (CL, CS, CB) that limit you to the 8 “popular”
registers and only permit 5-bit unsigned offsets (thus 32 slots
indexed by those “popular” registers).

These general CL and CS formats effectively require the register to
either be used as a base pointer to a struct or contain a memory
address computed in a previous instruction, although you could
reasonably argue that the 12-bit immediate field in the uncompressed
I-type and S-type instructions imposes a similar restriction — 2 KiB
is not very much space for all of your array base addresses!

Additionally, on RV32C and RV64C, the CIW-format `c.addi4spn` loads a
pointer to any of *256* 4-byte stack slots (specified in an immediate
argument) into one of the 8 popular registers, which you can then use
with a CL or CS instruction to access it.

Unconditional jumps and calls (to ±2KiB from PC) and branches on
zeroness (to ±256 bytes from PC) are also encodable in 16 bits, using
the CJ format.  These are also restricted to the 8 popular registers.
There’s also `c.jr` and `c.jalr` indirect unconditional jumps and
calls, which can use any of the 32 registers except, of course, x0.

There’s a couple of compressed load-immediate instructions with a
6-bit immediate operand, of which the second (`c.lui`) seems entirely
mysterious.

16-bit-encoded ALU instructions (subtract, `c.addw`, `c.subw`, copy,
and, or, xor, and shifts) are all limited to the 8 popular registers,
except for addition, which can use all 32 registers.

`ebreak` (into the debugger) is mapped into RVC, which is pretty
important, but `ecall`/`scall` isn’t.

There doesn’t seem to be a reasonable way to load immediate memory
addresses in 16-bit code except through the deprecated `c.jal .+2`
approach, which leaves the current PC in `ra`, at which point you can
add a signed 6-bit immediate to it with `c.addi`, thus generating an
address of some constant (or maybe a variable, if your page is mapped
XWR or you don’t have memory protection!) within 32 bytes of where you
are, but then it’s still in x1 and not a popular register.  There’s no
compressed version of the `auipc` instruction, for example.  This is
maybe not such a big deal like it would be in Thumb, since you can
freely intersperse 32-bit instructions like that into your 16-bit
code.

So in pure 16-bit instructions you can freely walk around pointer
graphs, index into arrays, jump around, jump up, jump up, and get
down, add, subtract, and do bitwise operations, but you can’t invoke
system calls or load addresses of global variables or constants.

So you could *almost* do a 16-bit-instruction RISC-V hardware core
that emulates other instructions with traps but executes at full speed
when running 16-bit instructions.  You’d need to add a few additional
16-bit instructions for accessing CSRs, loading addresses, and
handling traps.

MMX “P”
-------

On p. 91 they talk about packed SIMD (as in the TX-2 and MMX) which
they have decided to support by reusing the floating-point registers
for integer vectors (as in MMX) and not support for floating point in
favor of Cray-like variable-length vector registers (p. 93).  But
evidently the packed SIMD proposal is not ready.

2019 update of instruction set
------------------------------

All of the above was from looking at the 2017 2.2 spec.  The [current
version of the user-level ISA spec is 20191213][18] and is about
another hundred pages, 238 pp. in total.

[18]: https://github.com/riscv/riscv-isa-manual/releases/download/Ratified-IMAFDQC/riscv-spec-20191213.pdf "The RISC-V Instruction Set Manual, Volume I: User-Level ISA, Document Version
20191213, Editors Andrew Waterman and Krste Asanović, RISC-V Foundation, December 2019."

This answers a bunch of my questions above about hart initiation, why
the RV64I \*W instructions are the way they are, etc.
