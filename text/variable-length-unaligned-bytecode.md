Instruction set design for hardware has a different value system from
instruction set design for software emulation; sometimes the tradeoffs
that improve an instruction set for hardware implementation worsen it
for software.

For example, for software emulation, instructions trailed with
variable-length operands, like the 8086, are no problem, and
inconsistency from one instruction encoding to the next is no problem,
but bitfields are a terrible problem.  For hardware, bitfields are
just wires, but layout inconsistency adds layers of multiplexor delay;
for software, bitfields require bit shifting, which requires a loop if
your CPU lacks a barrel shifter or has registers too short for the
numbers you’re shifting.

I was prototyping a virtual machine in C today on my phone, using an
unsigned byte array as the VM’s memory.  I was pleased to see that
clang supports GCC’s pointers-to-labels extension and generates decent
code for it; my `goto dispatch;` at the end of each case even resulted
in duplicating the code `dispatch: goto *tbl[mem[pc++]];` in every
case, which is one or another variant of

    ldrb r2, [r4, r6]
    add r1, r6, #1
    ldr r3, [r5, r2, lsl #1]
    bx r3

Duplicating this code allows each case to have its own BTB entry,
which is helpful for branch prediction, and saves a wasteful
unconditional jump.  So, the virtual machine bytecode dispatch
overhead is only about a factor of 5, and all seemed good in the
world.  But then I looked at unaligned memory access.

My code to store a 32-bit value in the memory was:

    #define byt(x) ((x) & 255)
    #define store_tet(val, p) do { \
            mem[p] = byt(val); \
            mem[(p)+1] = byt((val) >> 8); \
            mem[(p)+2] = byt((val) >> 16); \
            mem[(p)+3] = byt((val) >> 24); \
    } while (0)

I figured that this was a portable, #ifdef-free way of marshalling a
little-endian 32-bit value, but the phone’s ARM processor (a Qualcomm
MSM8939 ARMv7l) is running in little-endian mode, so Clang would
recognize this and convert it to a simple store.  Imagine my surprise
at seeing the assembly:

    strb r7, [r4, #3]
    strb r7, [r4, #2]
    strb r7, [r4, #1]
    strb r7, [r4]

[ARMv7 supports unaligned access][0] but possibly the compiler is not
generating ARMv7 code; it’s not using Thumb, for example, although
/proc/cpuinfo says it’s supported.  (`-march=armv7` doesn’t help.)
(Older ARM versions mostly ignored the low-order bits, but had strange
behavior in `ldr` and unpredictable behavior in `ldrh` and `ldrd`.
[ARMv11 has an even larger set of possibilities][1].)  But there’s an
option in ARMv7 to trap on unaligned accesses!  So you can’t rely on
it.  Also, as a side note, it doesn’t seem to be doing the specified
bit shifts; in other cases it says things like

    lsr r0, r3, #24
    ...
    strb r0, [r1, #-1]
    lsr r0, r3, #16
    strb r0, [r1, #-2]
    lsr r0, r3, #8
    strb r0, [r1, #-3]

[0]: https://archive.fo/aWFc7
[1]: https://archive.fo/kDlnI

which is sort of reasonable, although I’m not sure what happened to
r3’s least significant byte.  Except it’s *not* reasonable: a single
virtual machine instruction to store a 32-bit value in RAM is going to
take 7 instructions on the underlying machine this way, plus dispatch
overhead.

So I was happily replacing my byte array with an array of `uint32_t`
(it’s a prototype!  I can do things like that!) and started using
`mem[p/4]` and `byt(mem[p/4] >> (p & 3))` before I realized that I’d
just replicated the whole unaligned-memory-access problem.  If an
instruction contains an unaligned 4-byte immediate operand, rounding
down `p/4` is not going to fetch that immediate successfully!

So, unless I’m going to require the instructions to be aligned, which
probably means mostly not using variable-length instructions, the
multiple shifts and loads are going to be happening.  Even if you have
“hardware support” for unaligned accesses, that doesn’t mean you
aren’t paying a speed penalty, or that it’s less than the above
code — it might be implemented by trapping to the kernel, making it
hundreds of times slower.

So this is a case where I thought hardware and software were more
different than they actually are.
