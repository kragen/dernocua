I was rereading [Piumarta and Warth’s paper on open and extensible
object models][oeom] today ([implementation][oopsla07]), and I was
thinking about how to extend it, which sadly seems not to have been
done much, though Piumarta did build his [COLA][COLA]/[Idst][idst] on
it.

[COLA]: https://www.piumarta.com/software/cola/colas-whitepaper.pdf
[oeom]: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.121.6603&rep=rep1&type=pdf
[oopsla07]: https://www.piumarta.com/oopsla07/
[idst]: https://www.piumarta.com/software/cola/

Piumarta & Warth
----------------

The paper describes a relentlessly simple metaobject protocol, with
three core object types (object, symbol, and vtable) and five core
methods (symbol.intern, vtable.lookup, vtable.addMethod,
vtable.allocate, and vtable.delegated).  The system starts with a
symbol table, five symbols, and two vtables, one for vtables
themselves and one for non-vtable objects.  The fundamental operation
it provides is send(anObject, aSymbol, args...).  This is implemented
by invoking bind(anObject, aSymbol), which in the usual case fetches
the vtable pointer v from the word preceding anObject and then
recursively invokes m = send(v, :lookup) on it to get the pointer to
the method code.  This having been done, the method code pointer m is
then socked away in various caches for performances, and then invoked
m(anObject, args...).  To bottom out the recursion, bind() has a
special case such that bind(vtablevtable, :lookup) returns a hardcoded
constant function pointer.

If I’m reading the numbers right, they report that the usual C
function call mechanism on their 2.16GHz Core 2 Duo takes about 8 ns,
while this dynamic send mechanism takes about 15 ns in the fast path
for monomorphic sends found on the fast path.  This is a pretty
reasonable cost; I think it replaces the single-instruction call found
on most modern CPUs with 5-7 instructions.  [Deutsch &
Schiffman][popl84] report that in their measurements such a
single-item inline cache was effective 95% of the time, though it is
well known that the Self researchers got significant system speedups
out of a polymorphic inline cache, since many of the remaining 5% of
calls are not “megamorphic”.

[popl84]: http://web.cs.ucla.edu/~palsberg/course/cs232/papers/DeutschSchiffman-popl84.pdf

The other four core methods provide a runtime mechanism for
constructing other object classes.  intern creates new symbols that
can be used as method selectors; x.addMethod(selector, code) mutates
vtable x by overwriting or adding a method; x.allocate(size)
instantiates a new object with vtable x; and x.delegated() creates a
new vtable whose lookup method delegates to x when it doesn’t find a
method internally.

In more conventional terminology, vtables are called classes, allocate
is called new, and delegates is called subclass.

The objective is that you should be able to extend the system with new
kinds of vtables that use a different lookup algorithm than the
built-in version.  They are only constrained in that whatever method
pointer they return will be cached, both in an inline cache and in a
system-wide cache indexed by (class, selector) tuples, forever.

The particular mechanism chosen for the inline cache allocates two
words of writable memory for each callsite, one for the class and one
for the method.  Upon visiting the callsite a second time, if the
receiver’s class is equal to the class last time around, the chosen
method is invoked without invoking bind(); otherwise, bind() is
invoked for the new class, and the result is duly cached before
invoking it.  In pseudo-assembly:

        ;; callsite 4310
        ld.8 r1(-8), r2        ; r1 is the receiver, word size is 8
        ld.8 icclass.4310, r3  ; icclass.4310 is a statically allocated word
        bne r2, r3, 1f         ; if this is the wrong class, jump to slow path
        ld.8 icmeth.4310, r4   ; load method pointer
        b 2f
    1:  st.8 r2, icclass.4310  ; update the IC key so we’ll have a hit next time
        call bind              ; bind expects class in r2, method selector in r5
        st.8 r4, icmeth.4310   ; bind’s return is in r4; r1 and r2 are preserved
    2:  call *r4               ; method expects receiver in r1, class in r2

The fast path here is 6 of these 9 instructions, but it’s common for
absolute loads to require multiple machine instructions (auipc, loads
from PC-relative constant pools, that kind of thing).  Also, though,
note that 9 instructions per callsite occupies quite a bit of code
space.  The slow path is mostly inside of bind, which may recursively
invoke send() with lookup, and maintains the system-wide cache.

But what if we want to invalidate these caches to accommodate new
methods, changes in the inheritance hierarchy, recompiled methods with
new code, and so on?  It’s okay for the invalidation to be relatively
expensive, since code changes happen much less often than message
sends; but, with the above pseudocode, unless we want to add
additional memory accesses and comparisons on the fast path, there are
only two paths open to us:

1. To *change the class of every affected object*, which would seem to
   involve scanning the entire heap and mutating potentially every
   live object, and probably also tripping the GC’s write barrier on
   all those objects, possibly resulting in a second scan of the
   entire heap.  This might actually be slower than just saving the
   whole system image and restoring it.
   
2. To *scan through the entire IC space*, clearing the pointer in
   icclass.N for every N whose callsite might need to be relinked.
   This is surely less expensive; it might amount to a few million
   instructions for a large program.

Trampolines or yantras
----------------------

In the original Deutsch & Schiffman JIT for Smalltalk-80, each method
body was preceded by a header that validated that the receiver was of
the correct class, failing over to a generic dispatch procedure if
not:

> The entry code [prologue] of an n-code [compiled] method checks the
> stored receiver class from the point of call against the actual
> receiver class.  If they do not match, relinking must occur, just as
> if the call had not yet been linked.

This suggests the following alternative compilation of send():

        ld.8 icmeth.4310, r4
        call *r4
    callsite.4310:

This transfers control to a trampoline, which has access to the
receiver in r1 and the callsite in the link register.  We’ll call
these trampolines “yantras”, because they are a sort of apparatus the
object system sets up to efficiently achieve the desired result.  In
the happy path, this yantra verifies that it is being invoked for the
correct class, then transfers control to the method body:
        
        ld.8 r1(-8), r2
        li r3, $foobarclass            ; load immediate
        beq r2, r3, foobar::ogonkify
        b bind

There might be several such yantras for the same method, one for each
class that inherits it, but the total number of yantras in the system
is relatively small, perhaps tens of thousands.  In the case that the
inheritance hierarchy changes, or the method is replaced with a new
version at a different address, or a subclass starts to override the
method with its own version, we can simply smash the yantra by
overwriting the first instruction or two with a `b bind` instruction.

The world is a little less rosy for `bind`.  It has the receiver in r1
and the receiver’s class in r2, but to finish its job it needs two
more pieces of information: the selector of the method that was being
invoked, and the address of the inline-cache variable `icmeth.4310`
into which it must store the address of the correct yantra, which it
may additionally need to synthesize.  For these, it must look at the
link register to find the callsite `callsite.4310`; then it can look
up the callsite in a table of all callsites like the following:

    callsites:
        .8byte callsite.0
        ; ...
        .8byte callsite.4308
        .8byte callsite.4309
        .8byte callsite.4310
        .8byte callsite.4311
        ; ...

Binary search on this table provides the index 4310 in about 12 memory
accesses and about 60 instructions.  (However, if code is not emitted
in strictly increasing memory-address order, it might be necessary to
use a segmented table, so maybe we should be using a 256-way trie
instead.)

This index allows `bind` to look up the selector at index 4310 in a
table of callsite selectors, so it can perform the correct lookup, and
also to store the yantra pointer into `icmeth.4310` for the next time
around.

At system startup, the `icmeth.N` values for every callsite simply
point directly at `bind`, which gradually materializes yantras for
frequently-called methods and populates the global cache and the IC
with pointers to them.

Ideally the yantras are allocated *after* the method bodies that they
jump to so that their conditional branch will be correctly predicted
the first time (and most of the times they fall out of the branch
prediction buffer).

Let’s call this inline-cache mechanism “faygoo”, for “fast abstract
yantra generic object orientation”.  Its primary benefit over Piumarta
& Warth’s implementation is that it provides a reliable, efficient,
and fine-grained way of invalidating elements in the inline caches.
But it might also be more efficient; on the fast path, faygoo runs 5
of these pseudo-assembly instructions instead of the 6 used by the
Piumarta & Warth mechanism, and performs one data memory read instead
of two.  It uses much less space per callsite (two pseudo-assembly
instructions, a read-only word, and a read-write word, rather than
nine pseudo-assembly instructions and two read-write words) at the
expense of allocating a megabyte or so of yantras, and perhaps having
somewhat worse locality of reference.

Yantra size
-----------

Why a megabyte or so?  In “bytecode interpreters for tiny computers” I
dissected the Squeak 3.8-6665 image a little and found 49775 methods;
presumably the majority of these are in leaf classes, while a few are
inherited by thousands of classes, so perhaps in a system as large as
Squeak, there would eventually be 65536-131072 yantras.  Each of these
consists of the four pseudo-instructions listed above; ld.8/li/beq/b.

I think that in the RISC-V C extension, the ld.8 would be C.LD if we
store the class pointer at index 0 instead of index -1, the li is
probably an uncompressed LUI/SLLI/LUI/ADDI sequence (14 bytes), the
beq is probably an uncompressed BEQ (to avoid a separate subtract
instruction and to be able to put the yantra within 4 KiB of the
method start rather than 256 bytes like C.BEQZ), and the b is probably
a compressed C.J to an uncompressed JAL instruction that’s shared
between many yantras.  That’s 20 bytes in all.

The amd64 realization might be something like this, 25 bytes per
yantra if we don’t do any alignment and don’t use a shared fast-path
second-level trampoline to allow the use of the shorter jump format,
or 21 bytes if we do:

    0000000000000000 <bind_shared_trampoline>:
       0:	e9 00 00 00 00       	jmpq   5 <yantra1>

    0000000000000005 <yantra1>:
       5:	48 8b 43 f8          	mov    -0x8(%rbx),%rax
       9:	48 b9 ef cd ab 89 67 	movabs $0x123456789abcdef,%rcx
      10:	45 23 01 
      13:	48 39 c1             	cmp    %rax,%rcx
      16:	0f 84 00 00 00 00    	je     1c <foobar::ogonkify>
      1c:	eb e2                	jmp    0 <bind_shared_trampoline>

This also gets a byte shorter if we put the class pointer at offset 0
instead of offset -1:

    000000000000001e <yantra2>:
      1e:	48 8b 03             	mov    (%rbx),%rax
      21:	48 b9 67 45 23 01 ef 	movabs $0x89abcdef01234567,%rcx
      28:	cd ab 89 
      2b:	48 39 c1             	cmp    %rax,%rcx
      2e:	0f 84 00 00 00 00    	je     34 <foobar::ogonkify>
      34:	eb ca                	jmp    0 <bind_shared_trampoline>

In the i386 instruction encoding, conditional jumps could only use the
short format, which would have required the extra shared unconditional
jump.

If class identifiers were HotSpot-style 32-bit “compressed oops”, or
indices into some kind of object table or class table, instead of
64-bit memory addresses, these numbers would probably shrink a little.
But probably each yantra costs about 20 bytes, so 65536-131072 of them
will cost 1310720-2621440 bytes.

When to smash yantras?
----------------------

One of the interesting items in Deutsch & Schiffman, carried over to
most modern JITs, is the notion of a restricted-size cache for
JIT-compiled code.  Because they were using machines with small memory
by current standards (typically using 16-bit address spaces, and
usually less than a megabyte) and slow disks, and the Smalltalk
bytecode (“v-code”) was something like 5× more compact than the native
machine code (“n-code”), they considered it more practical to discard
the least-recently-used native code rather than swapping it out to
disk.  Nowadays, rather than main memory, the objective might be to
fit the n-code into L1 or at least L2 cache (4096 KiB on this [AMD
A10-5745M][amd]).  If a compiled method is to be thus discarded,
smashing its yantras is a cheap way to ensure that control will not
flow into it again.

[amd]: https://www.amd.com/en/support/apu/amd-series-processors/amd-a10-series-apu-for-laptops/a10-5745m-radeon-hd-8610g

But that’s just an optimization.  The main reason to smash yantras is
because the method they jump to is no longer the correct method for
the class; in this case the yantra must be smashed and its
corresponding global lookup cache entry must be removed.  If your only
metaclass (vtable vtable) is the primitive metaclass, and you only
modify classes through Piumarta & Warth’s methods, this happens only
when you call `addMethod`, at which point we must smash that method’s
yantras in that class and all its subclasses.  This should be
straightforward.

However, the great appeal of the OEOM metaobject protocol is that it
makes it straightforward to extend the system with other metaclasses.
Piumarta & Warth give the example of implementing Traits, but other
possibilities include RPC remote stub objects, the proxy-membrane
pattern more generally (which is also useful for auditing or
debugging), record-reply-style creation of mock objects for unit
tests, and the creation of data classes from, for example, Proto3
files.

Some of these cases, like dynamic data-class creation, don’t actually
need custom metaclasses; being able to subclass existing classes and
add methods to them under program control is quite sufficient.  Other
cases require the creation of new methods on demand, but never
subclass the classes they create or change those methods once they
exist, so never need to smash any yantras.  However, in theory, the
ability for the lookup method to examine arbitrary mutable data means
that any change in the system state, or even outside of it (such as on
a network server with which the lookup method communicates) might
necessitate smashing yantras.

The most significant missing facility from the methods in the
primitive metaclass is the ability to mutate the inheritance graph by
changing a class’s parent, which would necessitate smashing some or
all of the yantras of that class and all its transitive subclasses,
depending on whether the methods they inherited had changed.

For *interactive* changes to the system, such efficient and
fine-grained cache invalidation is probably not necessary.  If there
are 65536 methods with 131072 yantras and 1048576 callsites, flushing
the entire cache can be done by brute force by overwriting only 8
mebibytes of RAM, which takes on the order of a millisecond;
repopulating the cache as callsites get rebound will slow down the
system over a longer period but still possibly be a tolerable
slowdown.  But you wouldn’t want the system to hang for a millisecond
every time a new method got invoked on a debugging membrane proxy
object.

Eliminating inheritance
-----------------------

I think the OEOM system becomes simpler if you eliminate inheritance
entirely.  There’s no need to propagate invalidation through
subclasses and no need for class.subclass() (called vtable.delegated()
by Piumarta & Warth).  There would still be the possibility that a
changed lookup() method might return different results, and the only
way to be sure to avoid this is to flush the cache completely.
