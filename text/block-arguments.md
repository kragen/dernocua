What would a calling convention optimized for block arguments look
like?

Block arguments
---------------

Smalltalk and PostScript use block arguments for all their control
structures, though Smalltalk cheats a bit on this.  This makes
user-defined control structures first-class.  Ruby method calls can
include a “block argument” after the other arguments, to which you can
“yield” once or many times within the method, for example to
automatically clean up after running some code, or to provide
iteration over a data structure, echoing CLU’s iterator construct:

    irb(main):012:1* def xs(y)
    irb(main):013:1*   yield y + 1
    irb(main):014:1*   yield y + 2
    irb(main):015:0> end
    => :xs
    irb(main):016:0> xs(3) { |z| puts(z) }
    4
    5
    => nil

This sort of makes the caller and callee into coroutines rather than
subroutines.  Python’s generator construct, adapted from a more
general construct in Icon and now adopted by JS as well, provides a
similar iteration facility.

Tcl procedures can evaluate an argument in the context of the caller,
which is how Tcl control structures work, making user-defined control
structures first class in Tcl as well.

ALGOL-60 provided call-by-name parameters allowing the callee to
assign to an arbitrary expression in the caller; this, it turned out,
required thunks to implement correctly and with reasonable efficiency.

Pascal permits passing nested subroutines as parameters, and these
nested subroutines had access to the variables of the subroutine they
were nested within.  Though more awkward, this has the same sort of
power as block arguments in Smalltalk, PostScript, Ruby, and Tcl.  To
preserve stack discipline in memory management, subroutines cannot be
returned or stored in variables or fields, only passed.  Such
“downward funargs”, rather than unrestricted closures, were also the
only kind of closures implemented in old dynamically-scoped Lisps;
dynamic scoping did not provide real closures.  They provide much of
the power of real closures.

Aside from the well-known use of this for iteration, my notes on IMGUI
languages suggests that there is great utility in block arguments and
at least pass-by-reference parameters, which cannot be implemented in
Lisp-family languages like Python, PostScript, Smalltalk, and Ruby:

    text_field("First name", &firstname, &firstname_len);
    button("Submit") { send_form(); }

And of course it’s common for control structures to want to assign to
local variables in the caller, which in Ruby and Smalltalk is usually
handled with block arguments:

    mydict.each(&k, &v) { print "$k: $v"; }

So, how efficiently can we implement this kind of thing?

Calling conventions
-------------------

The usual calling convention establishes where arguments are passed
and divides registers into “caller-saved” and callee-saved.  When a
callee returns, it’s entitled to have clobbered all the caller-saved
registers it pleases, generally including all the arguments, but must
have restored the callee-saved registers (on amd64, that’s %rbx, %rsp,
%rbp, %r12, %r13, %r14, and %r15; on RISC-V, according to both the
user-level ISA manual and the ELF psABI, that’s x2 (sp), x3 (gp), x4
(tp), x8 (s0/fp), x9 (s1), x18-x27 (s2-s11), f8-f9 (fs0-fs1), and
f18-f27 (fs2-11)) to their values on entry.

On RISC-V, interestingly, tp and gp are supposed to be preserved even
for signal handlers, so the callee can’t even temporarily use them for
something else unless it’s willing to disable signals.

There are tradeoffs in how many registers you preserve across calls.

Generally, if you’re going to support recursive functions, you need to
at least preserve a stack pointer or a frame pointer; otherwise the
function you’re returning to has no way to find its return address or
other local variables.  And making very rarely changed registers like
a thread pointer or global pointer callee-saved is basically free:
since callees won’t normally change them, preserving them incurs no
cost.

Generally the caller doesn’t really save the caller-saved registers.
A better term might be “scratch registers”: any result you compute in
them must be consumed or stored somewhere stable before any call.
That might be, as the “caller-saved” term suggests, by pushing it on
the stack or storing it into the stack frame, but there’s no
particular reason to restore it to the same register again afterwards,
or indeed any register; you might also have stored it into a data
structure or used it as a pointer or an arithmetic operand.

You could argue about whether argument registers are copy-in-copy-out
or pass-by-reference, but at any rate the caller is able to see
whatever changes the callee made to them.  Sometimes this may be true
of arguments passed on the stack (at least if the callee isn’t
responsible for popping them) and aggregate return values are commonly
provided by allocating space for them on the stack.

I don’t have a great handle on the performance tradeoffs involved.  If
a function uses a callee-saved register, it must save it whether or
not its caller was actually using it; if it uses a scratch register
for a value it wants to preserve across a call, it must save it
whether or not its callee was actually going to clobber it.  Having
only a few callee-saved registers makes context switching (including
function calls) faster, because context switching is precisely a
question of saving and restoring the callee-saved registers in a way
that violates stack discipline.  Having many callee-saved registers
makes leaf functions slower, because they have to save and restore
however many callee-saved registers they use, but never have to save
and restore scratch registers.

On the other hand, having enough callee-saved registers makes
higher-level functions more convenient to write, and possibly faster,
since it doesn’t have to pay the cost of saving those registers unless
it calls a callee that uses them.

Jeremiah Orians tells me that he finds it much less cognitive overhead
to make all the registers, except of course return-value registers,
callee-saved.

Different ways to represent closures or blocks
----------------------------------------------

Indirect-threaded (ITC) Forth normally does a function call [as
explained in Moving Forth][0] by the following sequence (my syntax,
not his):

    w := *pc  -- load virtual machine instruction (xt) into W
    pc++      -- increment program counter
    x := *w   -- load address of machine code from where xt pointed
    goto x    -- invoke code

[0]: https://www.bradrodriguez.com/papers/moving1.htm

Note that this leaves the execution token in the W register.  So, for
example, all colon definitions share the same machine code (their
first cell is a pointer to DOCOL) but have different data, and by
incrementing W they can access that data.  So this double indirection
gives you a sort of automatic closure: the invocation sequence passes
the code an address from which its code pointer was loaded, where it
can find whatever other data it’s interested in.  Rodriguez explains,
“CODE words [primitives] don’t need this information, but all other
kinds of Forth words do.”

He points out that direct threading, where instead of putting a
pointer to DOCOL you put a call or jump to DOCOL at the beginning of
each word, is a better option on most machines:

    w := *pc
    pc++
    goto w

Note that the execution token is still in W, so the instruction being
jumped to can be simply a jump; it doesn’t have to be a call.
(Rodriguez attributes this discovery to Frank Sergeant’s Pygmy Forth.)
This is a faster way to invoke primitives (“CODE words”) and generally
no worse for other cases, though it involves a mixing of executable
code and writable data that is difficult in many contexts (Harvard
machines, operating systems hardened with W^X).

But suppose you want to pass CLU-style iterators, Ruby-like block
arguments, or ALGOL-60-style call-by-name thunks to a subroutine.
These are also closures, but normally the data they want access to is
in the lexically enclosing stack frame.  GCC handles this by building
a trampoline on the stack which sets the context pointer register
before jumping to the implementation code.  If you wanted to use the
Forth approaches to this, you could imagine representing an ITC
closure as a two-word struct:

    struct closure { void (*c)(); void *d; };
    
If this struct is passed by reference, invoking `c` from it involves
assembly code something like this:

    mov -24(%rbp), %rax    # load struct pointer into %rax
    mov (%rax), %rcx       # load code pointer into %rcx
    call *%rcx

Then, *if* this struct were passed in memory (rather than in two
registers), and *if* the pointer to it can be guaranteed to always be
in a known register (in this case %rax), then the callee can access
`d` as something like `8(%rax)`, just like DOCOL in an
indirect-threaded Forth.

The direct-threading thing would amount to dynamically generating a
jump instruction instead of a code pointer, and as with GCC’s
trampolines, would allow the invoker of the block argument to not
indulge in an extra level of indirection in case it’s invoking a
closure.

However, this requires the caller to build a closure structure in
memory for each thunk argument or block argument.  This requires
storing a code pointer in memory, which is a huge pain on amd64.  If
you have three such arguments, that might be something like this (in
the ITC-like case; the DTC-like case is just slightly messier):

        movabsq $foo, %rdi      # build first closure
        mov %rdi, -24(%rbp)
        mov %rbp, -16(%rbp)
        movabsq $bar, %rdi      # build second closure
        mov %rdi, -40(%rbp)
        mov %rbp, -32(%rbp)
        movabsq $baz, %rdi      # build third closure
        mov %rdi, -56(%rbp)
        mov %rbp, -48(%rbp)
        lea -24(%rbp), %rdi     # pass first closure argument
        lea -40(%rbp), %rsi
        lea -56(%rbp), %rdx
        call quux

It’s not *too* terribad how the callee invokes one of these (remember
that this is a non-standard calling convention that guarantees the
closure pointer to be in %rax):

        mov %rsi, %rax          # invoke second closure argument; realistically this would probably be in the stack frame
        mov (%rax), %rcx
        call *%rcx

If we were to use the standard C calling convention and the usual
userdata `(*k->c)(k->d)` approach, closure invocation is instead
something like:

        mov %rsi, %rcx
        mov 8(%rcx), %rdi    # first parameter to closure
        mov (%rcx), %rcx
        call *%rcx

Despite all this hassle, the code for each of these closures needs an
additional instruction to load its context pointer:

        mov 8(%rax), %rcx

Or three, if it wants to use %rbp as its context pointer.

A calling convention that makes block arguments efficient
---------------------------------------------------------

For the specific case of thunks and block arguments, where the context
pointer is the parent’s call frame, it would be much nicer to be able
to just pass the code pointers and have the caller’s frame pointer
just implicitly flow through to the block arguments.  Then the initial
call sequence would look like this:

        movabsq $foo, %rdi
        movabsq $bar, %rsi
        movabsq $baz, %rdx
        call quux

The block/thunk invocation would just look like this, at least if no
registers need to be saved or restored first:

        call *%rsi

Then, within the block or thunk, %rbp is just available as a frame
pointer as normal.

In the case where registers do need saving/restoring, for example
because the callee `quux` was also using %rbp, it might look like
this:

        push %rbp
        mov -8(%rbp), %rbp
        call *%rsi
        pop %rbp

Normally you might expect this to index off the stack pointer or the
frame pointer instead of using push/pop instructions, but the whole
point of block arguments is to allow the stack pointer to be
arbitrarily far away from the stack frame of the current lexical
context, by allowing callees to yield back into callers.  (Probably
this whole thing would be totally impossible on something like a
SPARC.)

This suggests dividing “callee-saved” registers into thunk-preserved
registers, %rbp in the above example, which the callee is obligated to
restore to their caller’s values upon entry to any caller-provided
thunk, and return-restored registers, which are guaranteed to be
restored to their original value when the callee returns but may have
different values when thunks are being run (notably, %rsp).

This kind of thing makes it practical to implement control structures
as library functions.  To take an extreme example that will obviously
frustrate desirable optimizations:

    while (*s) { *t++ = *s++; }

This might be compiled, using a library `while` function, as something
like the following:

            movabsq $thunk_1, %rdi
            movabsq $thunk_2, %rsi
            call while
            ret
    thunk_1:
            mov -8(%rbp), %rax      # s
            mov (%rax), %cl
            xor %rax, %rax
            test %cl, %cl
            setnz %al
            ret
    thunk_2:
            mov -8(%rbp), %rax      # s
            mov -16(%rbp), %rcx     # t
            mov (%rax), %rdx
            mov %rdx, (%rcx)
            incq -8(%rbp)
            incq -16(%rbp)
            ret

I mean, this is obviously not a good way to compile
non-NUL-terminating-strcpy, but at least so far the overhead is not
ridiculous.  `while` itself might be implemented as follows:

    while:  push %rsi               # thunks can hork %rsi
            push %rdi               # and %rdi
            push %rbx               # but not %rbx
            mov %rsp, %rbx
    1:      mov 16(%rbx), %rsi      # load first thunk
            call *%rsi
            test %rax, %rax
            jz 2f
            mov 8(%rbx), %rdi
            call *%rdi
            jmp 1b
    2:      pop %rbx
            retq $16

We could improve this a bit by guaranteeing %r12, %r13, %r14, and %r15
to the thunks as well as %rbp.  This would require no changes to our
`while` but would allow us to rewrite our thunks:

    thunk_1:
            mov (%r12), %cl         # s
            xor %rax, %rax
            test %cl, %cl
            setnz %al
            ret
    thunk_2:
            mov (%r12), %rdx
            mov %rdx, (%r13)        # t
            inc %r12
            inc %r13
            ret

Suppose we decide to guarantee that thunks preserve %r8 and %r9
(normally caller-saved argument registers, which is to say, the callee
owns them; here we’re extending the callee’s ownership over them to
require blocks in the caller to preserve them while the callee is
yielded).  Then we can improve `while`, rearranging it a bit as well:

    while:  mov %rsi, %r8           # save first thunk
            mov %rdi, %r9           # save second thunk
            jmp 1f
    2:      call *%r9
    1:      call *%r8
            test %rax, %rax
            jnz 2b
            retq

This amounts to 14 instructions per loop.  GCC -O is emitting this
code for me for the real C version:

        endbr64
        movq	%rsi, %rax
        movzbl	(%rdi), %edx     # s
        testb	%dl, %dl
        je	.L2
    .L3:
        addq	$1, %rdi
        addq	$1, %rax
    	movb	%dl, -1(%rax)    # t
        movzbl	(%rdi), %edx
        testb	%dl, %dl
        jne	.L3
    .L2:
        ret

This is 6 instructions per loop, so we can crudely guess that the
overhead introduced by this coroutine mechanism is around a factor of
2-3 in this sort of worst-case scenario.

So instead of dividing registers into caller-saved and callee-saved,
we divide registers into four groups: caller-saved that thunks must
preserve, caller-saved that thunks can clobber, callee-saved that
thunks can rely on, and callee-saved that thunks must preserve (but
cannot rely on).

You can simplify this by eliminating the “callee-saved that thunks
must preserve” category.  Or complexify it by by having registers,
like sp and RISC-V’s tp and gp, which thunks can rely on, but must
preserve.

One upside of just using ordinary closures for this kind of thing is
that, even though it takes four instructions to construct and pass the
closure, three or four instructions to invoke it, and an extra
context-pointer instruction within the closure, you can pass it down
through any number of levels of calls with just the usual single
instruction needed to pass on an argument to a callee, and invocations
from however deep down the stack are always equally efficient.  With
this coroutine mechanism, by contrast, if you want to pass on a thunk
you received to a callee, you can’t; the best you can do is make a
thunk of your own that invokes your thunk.

Bounding stack depth
--------------------

This kind of mechanism is useful in cases where you want to avoid
garbage collection, either for micro-efficiency or to avoid possible
failures.  In the cases where you care about possible failures, it’s
important to be able to statically bound the stack depth.  In the
normal kind of C programming, which doesn’t have block arguments, you
would do this by just making a call graph, which would need to be
acyclic, and computing the highest-weight path from the root to a
leaf, where the weight of each node is the size of its stack frame.

Actually, a better way to do this is to compute the maximum stack size
of each function as its stack frame size plus the maximum of the
maximum stack sizes of its callees, rather than explicitly
constructing the graph, but conceptually it’s the same thing.

That runs into difficulties with function pointers, where you have to
conservatively approximate the set of functions that can actually be
called from a given callsite, for example using the function type.
This can very easily give you unwanted recursion.

I think this block-argument thing is more tractable to make fairly
precise, because when a function invokes a block argument, you know it
can only be one of the block arguments it was actually passed.

Now each subroutine S has not only a maximum stack size of its own
M[S], but also a maximum stack size M[S, P] with respect to each of
its block formal parameters P, which expresses the maximum size of the
stack of that function and its callees when that block formal
parameter is invoked.  If it only invokes the block formal parameter
directly (not from a block nested inside it and passed to some other
function) its stack size for that parameter is just its own stack
frame size F[S].  But if it invokes block formal parameter P inside
some block that it passes to subroutine T as the actual parameter for
block formal parameter Q, then its maximum stack size M[S, P] for that
parameter is at least M[T, Q] + F[S].  So M[S, P] = F[S] + max(i,
M[Ti, Qi]) for all the callsites (Ti, Qi) for the block formal
parameter P.  And M[S], which will be at least at large as any of the
M[S, Pi] for subroutine S, is F[S] + some other maximum stack size.
