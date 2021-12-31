Qfitzah: a minimal term-rewriting language
==========================================

Today Andrius Štikonas got the `hex0_riscv64` bootstrap seed program
down to 392 bytes; it translates from hexadecimal into binary, though
much of the bulk of the program is opening and closing files.  This
led me to thinking about the question of Qfitzat haDerekh, shortening
the path: can we teleport directly from a few hundred bytes of machine
code to something much more amenable to writing compilers?

Term rewriting languages like Q, Pure, Mathematica, Maude, or
Aardappel seem more amenable to writing compilers not only than
imperative languages like C but also more so than traditional Lisps;
it implicitly provides conditionals, pattern-matching for arguments,
ad-hoc polymorphism with multiple dispatch, and parametric
polymorphism.  As [Oortmerssen’s dissertation on Aardappel][1] points out
(p. 9), term rewriting can be top-down (normal-order, leftmost
outermost) or bottom-up (applicative-order, eager, innermost),
nondeterministic, as well as other variants; and it can select rule
precedence according to source order, uniqueness, according to some
kind of specificity, nondeterministically, or in some other way.  I
think the easiest thing to implement is probably bottom-up
source-order rewriting; though top-down evaluation could give you
laziness, you don’t need laziness or special forms to get conditionals
with term rewriting, the way you do with the λ-calculus or the
ur-Lisp.

[1]: https://strlen.com/files/lang/aardappel/thesis.pdf "Concurrent Tree Space Transformation in the Aardappel Programming Language, by Wouter van Oortmerssen, 02000"

An interesting thing about this is that, despite the vastly increased
expressive power (especially for things like writing compilers), the
code to implement a term-rewriting interpreter is roughly as simple as
the code to implement an ur-Lisp interpreter, just much slower.
However, I don’t think it’s actually any *simpler* than the ur-Lisp,
and it’s surely a bit larger than `hex0_riscv64`.  The surprising
thing is that the difference may not be that much.

Still, the unfinished draft Qfitzah interpreter I wrote in assembly is
almost 1000 bytes, and for RISC-V (without the C extension) it would
probably be even bigger.

A Scheme strawman interpreter for term rewriting
------------------------------------------------

The interpreter is pretty simple.  Basically, to evaluate a non-atomic
expression, you first evaluate its components, and then you loop over
the rewrite rules, trying to match each one against the expression,
and when one of them succeeds you instantiate its replacement with the
match values, then evaluate the instantiated replacement.  Something
like this in Scheme:

    (define (ev t)                                 ; eval, for term rewriting
      (if (pair? t) (ap (map ev t) rules) t))      ; atoms don’t get rewritten

    ;; apply, for term rewriting, but the arguments are the top-level term
    ;; to rewrite, after all its children have been rewritten as above, and
    ;; the remaining set of rules to attempt rewriting with
    (define (ap t rules)
      (if (null? rules) t               ; no rewrite rules left? don’t rewrite
          (let ((m (match t (caar rules) '()))) ; initially no vars () match
            (if m (ev (subst (cadar rules) m)) ; rule matched? substitute & eval
                (ap t (cdr rules))))))         ; otherwise, try the other rules

That depends on definitions of `match`, `emptyenv`, and `subst`.
`subst` is easy enough (though I got it wrong at first, and it might
be nicer to handle the case where the variable is undefined):

    (define (subst t env)
      (if (var? t) (cdr (assoc t env))
          (if (pair? t) (cons (subst (car t) env) (subst (cdr t) env))
              t)))

So, for example, `(subst '(You #(vt) my #(np)) '((#(np)
. wombat) (#(vt) . rot)))` evaluates to `(You rot my wombat)`, as
you’d expect.

Then `match` needs to compute whether there’s a match, which requires
it to distinguish variables from other things.  In its simplest form
we can consider variables that occur more than once an error, but an
error we don’t try to detect; then it might look like this:

    (define (match t pat env)
      (if (var? pat) (cons (cons pat t) env)  ; vars match anything
          (if (pair? pat)  ; pairs match if the cars match and the cdrs match
              (and (pair? t)  ; a pair pattern can’t match an atom
                  (let ((a (match (car t) (car pat) env)))  ; try to match car
                    (and a (match (cdr t) (cdr pat) a))))   ; then, try the cdr
              (and (equal? pat t) env))))  ; atoms match only themselves

Then you just need some kind of convention for marking variables.  The
simplest thing in Scheme would be to use `,x`, which is syntax sugar
for `(unquote x)`, but that would have the unfortunate effect that you
can’t use the atom `unquote` in head position in either a pattern or a
replacement template.  Instead I am using `#(x)`:

    (define var? vector?)

(In other environments, you might use a different data type.)

And that’s it.  19 lines of Scheme in
terms of `define`, `if`, `'()`, `cons`, `pair?`, `let`, `car`, `cdr`,
`caar`, `cadar`, `#f`, `and`, `equal?`, `assoc`, `map`, and `null?`
gives you a bottom-up, source-order-precedence term-rewriting
interpreter.  If we want to include implicit equality testing in
patterns when a variable occurs more than once, it’s a couple more
lines of code, but that’s about a 10% total complexity increase.

Of course this approach to term-rewriting interpretation is very
inefficient, far more so than the standard Lisp tree-walker approach,
because every expression evaluation involves iterating over
potentially all the code in the entire program to see which ones
apply.  Aardappel (and, I think, Mathematica) requires the head of
each term to be an atom, and compiles the usually small number of
rules for each atom down into a subroutine, so that when attempting to
rewrite any term, you can start by doing a hash table lookup, and then
typically have a small number of conditionals after that.  So you’d
probably want to use this bootstrap interpreter only to run a
bootstrap compiler.

### Primitives and integers ###

Formally speaking we don’t need arithmetic primitives, since we can
define numbers in a variety of ways via term rewriting, but for
practical efficiency we probably want access to machine arithmetic.

I’m thinking that the way to handle things like arithmetic is to have
an additional class of constant atoms, the integers, and some built-in
rewrite rules that are implemented in machine code.  Darius Bacon
suggests that perhaps only the right-hand side should be implemented
in machine code, and the pattern-match itself maybe in a prelude.

The question is how to handle them for matching: can you pattern-match
on integerness, or do you just have a “function”?  In the first case,
you could allow an integer like 283 to match a pattern like `Int x`
and bind `x` to 283; or you could instead rewrite `Int? 283` and
similar to `Yes` and `Int? Qfitzat` to `No`.

If you were doing the pattern-match in the prelude, these alternatives
might look like:

    + (Int x) (Int y) :: 3
    - (Int x) (Int y) :: 4
    - x: - 0 x

where the `::` rather than `:` indicates that you’re supplying a
machine-code primitive index rather than a template, 3 being the index
of the addition routine and 4 that of subtraction; or, in the other
case:

    If Yes a b: Do a
    If No a b: Do b
    && x y: If x y x
    || x y: If x x y
    Not Yes: No
    Not No: Yes
    Do Yes: Yes
    Do No: No
    + x y: If (&& (Int? x) (Int? y)) (Int+ x y) (Add x y)
    Do (Int+ x y) :: 3
    - x: - 0 x
    - x y: If (&& (Int? x) (Int? y)) (Int- x y) (Sub x y)
    Do (Int- x y) :: 4

These If rules are convenient here but maybe not ideal, both because
it’s easy to forget the `Do` when you try to define the results, and
because it’s easy to forget that the *arguments within* the consequent
and alternate blocks *will* be evaluated eagerly.

You could define the usual arithmetic operations in terms of a single
machine-code primitive with multiple arguments, like Mulsubdiv a b c d
= (a*b - c)//d, with definitions in the standard prelude like these:

    + (Int x) (Int y): Mulsubdiv -1 x y -1
    - (Int x) (Int y): Mulsubdiv 1 x y 1
    * (Int x) (Int y): Mulsubdiv x y 0 1
    / (Int x) (Int y): Mulsubdiv 1 x 0 y

Alternatively you could have `Arithmetic x y` which evaluates to a
tuple containing all the results, like `Results <x+y> <x-y> <x*y>
<x//y> <x%y>`, and you could write

    + (Int x) (Int y): R15 (Arithmetic x y)
    - (Int x) (Int y): R25 (Arithmetic x y)
    * (Int x) (Int y): R35 (Arithmetic x y)
    / (Int x) (Int y): R45 (Arithmetic x y)
    % (Int x) (Int y): R55 (Arithmetic x y)
    R15 (a b c d e f): b
    R25 (a b c d e f): c
    R35 (a b c d e f): d
    R45 (a b c d e f): e
    R55 (a b c d e f): f

Either would avoid needing four or five
separate primitive subroutines, four or five
separate conditional cases to call them, four or five separate subroutine
table entries, etc.  Though maybe a single conditional case would be
sufficient, `Primop op x y`, with an op number, you’d still need a
table of subroutines.

For bitwise operations you could similarly use `Norshift a b c = ~(a |
b) >> c` and definitions like these:

    B~ (Int x): Norshift x 0 0
    Nor (Int x) (Int y): Norshift x y 0
    | (Int x) (Int y): B~ (Nor x y)
    & (Int x) (Int y): Nor (B~ x) (B~ y)
    &^ (Int x) (Int y): Nor (B~ x) y
    >> (Int x) (Int y): Norshift (B~ x) 0 y
    ^ (Int x) (Int y): Nor (Nor x y) (& x y)

Probably three arguments is the maximum that would be tolerated by
ordinary decency, but if not, you could of course incorporate
Mulsubdiv and Norshift into a single six-argument monster.

You’d also need some kind of comparison operation, minimally `>0`.

Left shifts are easy enough to implement as rewrite rules with
addition:

    << (Int x) 0: x
    << (Int x) (Int y): If (>0 y) (Shift (+ x x) (- y 1)) (Negative-left-shift x y)
    Do (Shift x y): << x y

Possibly a better way to implement that would be:

    << (Int x) 0: x
    << (Int x) (Int y): <<2 (>0 y) x y
    <<2 Yes x y: Shift (+ x x) (- y 1)

There’s a separate question of how to handle system calls, which I
think can be bodged in pretty easily since evaluation is eager.

Some sketches of assembly implementations
-----------------------------------------

But that’s Scheme!  In machine code it seems like it could be
significantly larger, even without garbage collection, which isn’t
necessary for a bootstrap interpreter on a modern machine, and
parsing, which is.  You also have to actually *implement* `cons`,
`pair?`, `car`, `cdr`, `equal?`, `assoc`, `map`, and `null?`.  Most of these
are not very difficult.

(None of the assembly code below is tested.)

Because I still know almost no RISC-V assembly, I’m going to sketch
this out in the i386 assembly of my childhood.

### Type tags in RAM ###

In i386 code, using the simple approach I took in Ur-Scheme, cons
might be 18 bytes:

    cons:   movl $0x2ce11ed, 0(%ebx)  # allocation pointer is in %ebx
            mov %eax, 4(%ebx)         # car was arg 1, in %eax
            mov %ecx, 8(%ebx)         # cdr
            mov %ebx, %eax            # return the old allocation pointer
            lea 12(%ebx), %ebx
            ret

Then `pair?`, leaving the predicate result in ZF, might be 7 bytes:

    pairp:  cmpl $0x2ce11ed, (%eax)
            ret

And an unsafe `cdr` might be 4 bytes:

    cdr:    mov 8(%eax), %eax       # probably better to open-code these 3 bytes
            ret

### Type tags in pointer low bits ###

But the SBCL approach of tagging the pointer would be shorter:

    sbcons: mov %eax, 0(%ebx)       # car was arg 1
            mov %ecx, 4(%ebx)
            lea 3(%ebx), %eax
            lea 8(%ebx), %ebx
            ret                     # 12 bytes, not 18

    sbpairp:
            and $3, %al             
            cmp $3, %al             
            ret                     # this reduces to 5 bytes

    sbcar:  mov -3(%eax), %eax
            ret                     # still 4 bytes

    sbcdr:  mov 1(%eax), %eax
            ret

### Type tags in pointer low bits where 00 denotes a pair ###

If we instead use two low-order 0 bits to tag cons pointers, list
operations get smaller still, to the point where almost all of them
are so small that they need to be open-coded:

    00000036 <altcons>:  # 11 bytes
      36:	89 03                	mov    %eax,(%ebx)
      38:	89 4b 04             	mov    %ecx,0x4(%ebx)
      3b:	89 d8                	mov    %ebx,%eax
      3d:	8d 5b 08             	lea    0x8(%ebx),%ebx
      40:	c3                   	ret    

    00000041 <altpairp>: # 3 bytes
      41:	a8 03                	test   $0x3,%al
      43:	c3                   	ret    

    00000044 <altcar>:   # 3 bytes
      44:	8b 00                	mov    (%eax),%eax
      46:	c3                   	ret    

    00000047 <altcdr>:   # 3 bytes
      47:	8b 40 04             	mov    0x4(%eax),%eax
      4a:	c3                   	ret    

    0000004b <altnullp>: # 3 bytes
      4b:	85 c0                	test   %eax,%eax
      4d:	c3                   	ret    

### A sketch of `subst` in i386 assembly ###

Here’s what `subst` might look like with that setup.

In i386 assembly:

            # subst t env returns a version of t with var substitutions from env.
    subst:  push %ebp               # callee-saved variable used here
            push %eax               # %eax has t, %ecx has env
            push %ecx
            test $2, %al            # ...10 is the pointer type tag for vars
            jz 1f

            call assoc              # calls are 5 bytes. inherits both t & env
            mov 4(%eax), %eax       # get the cdr
    2:      pop %ecx                # discard saved arguments; labeled for
            pop %ecx                # epilogue sharing
            pop %ebp
            ret

    1:      test $3, %al            # ...00 is the pointer type tag for pairs
            jz 1f                   # if this isn’t a pair:
            jmp 2b                  # %eax is already t; implicitly return it

    1:      mov 4(%eax), %eax       # get cdr t for (subst (cdr t) env)
            call subst              # inherits our env.
            mov %eax, %ebp          # save subst result
            mov 4(%esp), %eax       # load saved t
            mov (%eax), %eax        # car t
            mov (%esp), %ecx        # second argument is saved env
            call subst
            mov %ebp, %ecx          # second cons argument is (subst (cdr t) env)
            call cons
            jmp 2b                  # return cons result

That’s 24 instructions and 58 bytes of machine code,
and, although I’m sure I missed a few
tricks, I don’t think it’s going to get more than about 30% smaller.
That’s 14½ bytes per line of Scheme, which I think is pretty good, but
it puts the estimate of the whole 19-line Scheme program at 275½ bytes,
which doesn’t include the non-open-coded primitives like `cons` (and
`assoc` and `map`), the parser, or I/O.  I/O is actually almost all of
`hex0_riscv64`.

I went through and coded the whole thing in assembly language; after
trimming it down a bit, the
resulting (untested) program is 100 instructions and 237 bytes of
machine code (12.5 bytes per line of Scheme),
containing `cons`, `subst`, `assq`, `match`, `evlis`,
`ev`, `ap`, and no undefined symbols; so 275½ was actually a little
high.  I’m pretty sure I could squeeze it down a bit more, but
probably not below 200 bytes.  It’s still missing I/O, the reader, and
the printer.  In the process I trimmed down `subst` itself to 20
instructions and 55 bytes, then later 22 instructions and 49 bytes.

Adding an input reading loop cost 49 more bytes of code, plus 4 of
data; a printer (untested) cost another 81 bytes.  Now I’m at 370
bytes of code.  I think all it’s lacking now is a reader, so I’m
pretty sure it’ll be under 512 bytes of machine code and data, thus
under 1 KiB of executable.  I’m currently suffering 414 bytes of
executable-format overhead, mostly padding, but [Brian Raiter’s
work][2] suggests that it should be possible to get the
executable-format overhead down to about 45–52 bytes, but [with strict
ELF conformance he couldn’t get it below 76 bytes][3], and [with
dynamic linking he couldn’t get it below 297 bytes][2]; still, maybe I
can get the whole executable under 512 bytes.

P.S. a reader was 287 bytes.

[1]: https://www.muppetlabs.com/~breadbox/software/tiny/teensy.html
[2]: https://www.muppetlabs.com/~breadbox/software/tiny/somewhat.html
[3]: https://www.muppetlabs.com/~breadbox/software/tiny/revisit.html

However, it’ll still be missing library functions to do useful things
like I/O and arithmetic.

Trying to do this in RV64 without the C compressed-instruction
extension, like `hex0_riscv64`, would surely have much worse code
density; *with* the C extension it might be slightly more compact.

### A sketch of `subst` in a stack bytecode ###

In one of the bytecodes suggested in file `c-stack-bytecode.md` this
might look like this:

    PROCEDURE subst argwords=2
        loadword 0  ; t
        call var?
        jztos 1f    ; if not a var (top of stack is 0/nil/false), skip
        loadword 0
        loadword 1  ; env
        call assoc
        call cdr
        ret
    1:  loadword 0
        call pair?
        jnztos 1f   ; skip if it *is* a pair
        loadword 0  ; return t
        ret
    1:  loadword 0
        call car
        loadword 1
        call subst
        loadword 0
        call cdr
        loadword 1
        call subst
        call cons
        ret

According to the hypotheses in that note, this might compile to 2
bytes of procedure header, 23 opcode bytes, 9 operand bytes for call
instructions, 2 operand bytes for jump targets, and a 2-byte entry in
a global subroutine table, for a total of 38 bytes.  At this rate, the
whole Scheme program irresponsibly extrapolates to 180½ bytes, but of
course you’d have to add the bytecode interpreter on top of that.  On
the other hand, if the bytecode interpreter is customized specifically
to run the term-rewriting interpreter, none of the call instructions
will need an operand byte, because there’s plenty of opcode space to
allocate each subroutine in this program a single-byte opcode.  That
would bring it down to 29 bytes, half the size of the i386
machine code, irresponsibly extrapolating the whole Scheme program to
137¾ bytes of machine code.

A stack bytecode specifically designed for list processing might have
a `decons-or` instruction, which unpacks the pair on top of the stack
into a car and cdr, or if it’s not a pair, jumps to the given
destination, because usually `pair?` is associated with subsequent
calls to `car` and `cdr`.  We could represent that in Scheme as a
special binding form, here introducing variables called `a` and `d`:

    (define (subst t env)
      (if-pair t (a d) (cons (subst a env) (subst d env))
        (if (var? t) (cdr (assoc t env)) t)))

In such a bytecode:

    PROCEDURE subst argwords=2
        loadword 0  ; t
        decons-or 1f
        loadword 1  ; env
        call subst
        swap
        loadword 1
        call subst
        call cons
        ret
    1:  loadword 0
        call var?
        jztos 1f    ; if not a var (top of stack is 0/nil/false), skip
        loadword 0
        loadword 1
        call assoc
        call cdr
        ret
    1:  loadword 0
        ret

This reduces `subst` from 23 bytecode instructions to 19, and I think
it’s likely that a single omnibus pair?-and-jztos-and-car-and-cdr
procedure will also be smaller than three separate ones and their
opcode table entries.  The cost is that, in the relatively infrequent
case where only one of those three operations is called for, it costs
you an extra byte per unwanted result.

Dynamic dispatch
----------------

Because patterns can dispatch on more than just the function being
called, you can define “methods” on “classes”; one of the examples in
the Aardappel dissertation is defining a hash method for a point class:

    hash(point(x,y)) = x*y

Or, in S-expression syntax using vectors:

    (hash (point #(x) #(y))) => (* #(x) #(y))

Which you could feed into the Scheme strawman interpreter above as
follows:

    (define rules '(((hash (point #(x) #(y))) (* #(x) #(y)))))

Elsewhere you might define how to rewrite `hash` expressions applied
to other types of values; then a hashtable implementation can invoke
`hash` without worrying about the types of its arguments.  The
compiler transformation described above would gather all the `hash`
rules togther into a subroutine, which then performs a sequence of
conditional tests to dispatch to one of them.

This also permits CLOS-style multiple dispatch:

    (* (scalar #(s)) (vec #(x) #(y) #(z))) =>
        (vec (* #(s) #(x)) (* #(s) #(y)) (* #(s) #(z)))
    (* (scalar #(s)) (scalar #(t))) => (scalar (* #(s) #(t)))
    (* (m #(r1) #(r2) #(r3)) #(vec)) => (vec (dot (vec . #(r1)) #(vec))
                                             (dot (vec . #(r2)) #(vec))
                                             (dot (vec . #(r3)) #(vec)))
    (dot (vec #(a) #(b) #(c)) (vec #(d) #(e) #(f))) =>
        (+ (* #(a) #(d)) (* #(b) #(e)) (* #(c) #(f)))

Those rules, for example, will rewrite

    (* (m (1 2 3) (4 5 6) (7 8 9)) (vec x y z))

to

    (vec (+ (* 1 x) (* 2 y) (* 3 z))
         (+ (* 4 x) (* 5 y) (* 6 z))
         (+ (* 7 x) (* 8 y) (* 9 z)))

Higher-order programming
------------------------

In languages like C or Lisp, the atom-head requirement Aardappel has
would prevent you from doing any higher-order programming, but not in
term-rewriting languages, because you can use the same
dynamic-dispatch trick.  You can define a higher-order mapcar function
as follows:

    (map #(f) nil) => ()
    (map #(f) (cons #(car) #(cdr))) =>
        (cons (call #(f) #(car)) (map #(f) #(cdr)))

Then you can define patterns like this:

    (call (cover #(material)) #(base)) => (some #(material) covered #(base))

so that `(call (cover chocolate) raisins)` rewrites to `(some
chocolate covered raisins)`.  These rules compose so that

    (map (cover leather) (cons armchairs (cons bikers (cons goddesses nil))))

rewrites to

    (cons (some leather covered armchairs)
          (cons (some leather covered bikers)
                (cons (some leather covered goddesses) nil)))

I learned about this on p. 35 of the
Aardappel dissertation, which gives the example (in slightly different
syntax):

    apply(qsortcompare(x),y) = y<x
    filter([],_) = ([],[])
    filter([h|t],f) = 
      if apply(f,h) then ([h|a],b) else (a,[h|b])
        when (a,b) = filter(t,f)

In the syntax I used above, this would be written as

    (apply (qsortcompare #(x)) #(y)) => (< #(y) #(x))
    (filter nil #(_) => (pair) nil nil)
    (filter ((cons #(h) #(t)) #(f))) =>
        (filter2 (filter #(t) #(f)) #(h) #(f) (apply #(f) #(h)))
    (filter2 (pair #(a) #(b)) #(h) #(f) true) => (pair (cons #(h) #(a)) #(b))
    (filter2 (pair #(a) #(b)) #(h) #(f) false) => (pair #(a) (cons #(h) #(b)))

(This also demonstrates how the term-rewriting paradigm implicitly
provides conditionals.)

Oortmerssen discusses this further in pp. 48–50 (§4.1.2).

In the language implemented by the interpreter above, you could just
as well define things this way:

    (map #(f) (cons #(car) #(cdr))) => (cons (#(f) #(car)) (map #(f) #(cdr)))
    ((cover #(material)) #(base)) => (some #(material) covered #(base))
    ((qsortcompare #(x)) #(y)) => (< #(y) #(x))
    (filter ((cons #(h) #(t)) #(f))) =>
        (filter2 (filter #(t) #(f)) #(h) #(f) (#(f) #(h)))

This would have the advantage that you could pass in the name of any
existing function.  But compiling this efficiently might be
nontrivial.

It might be worthwhile to implement lambda-lifting to get closures.
Aardappel experimented with this but ultimately rejected it.

A metacircular term-rewriting interpreter
-----------------------------------------

If you love term rewriting so much, why don’t you marry it, huh?
Why’dja write that “strawman” above in *Scheme*?  Are you *chicken*?

XXX the below lacks some bugfixes from the Scheme.  Also I definitely
do not want to use the shitty Scheme syntax.

Well, part of it is that I think Scheme is a better pseudocode for assembly
language, but maybe it would look something like this, written in itself:

    (ev (cons ,f ,a) ,r) => (ap (args (cons ,f ,a) ,r) ,r ,r)
    (ev ,t ,_) => ,t
    (args nil ,_) => nil
    (args (cons ,a ,d) ,r) => (cons (ev ,a ,r) (args ,d ,r))

    (ap ,t norules ,_) => ,t            # no rules left to match
    (ap ,t (rule ,pat ,tem ,r) ,r0) =>  # try to match a rule
        (ap2 ,t ,r (match ,t ,pat emptyenv) ,tem ,r0)
    (ap2 ,t ,r nomatch ,_ ,r0) => (ap ,t ,r ,r0)  # on failure try others
    (ap2 ,t ,r ,env ,tem ,r0) => (ev (subst ,tem ,env) ,r0)  # or subst & eval

    (subst (cons ,a ,d) ,env) => (cons (subst ,a ,env) (subst ,d ,env))
    (subst ,t ,env) => (subst2 ,t (lookup ,t ,env))
    (subst2 ,t nomatch) => ,t
    (subst2 ,t ,v) => ,v

    (match ,_ ,_ nomatch) => nomatch               # match failures always win
    (match ,t (var ,v) ,env) => (bind ,v ,t ,env)  # otherwise vars always do
    (match (cons ,ta ,td) (cons ,pa ,pd) ,env) =>  # match cars and cdrs
        (match ,td ,pd (match ,ta ,pa ,env))
    (match ,t ,pat ,env) => (match2 (equal? ,pat ,t) ,env)
    (match2 true ,env) => ,env
    (match2 false ,env) => nomatch

So that’s 21 lines, about the same as Scheme, but I left out `lookup`,
which in Scheme is the standard procedure `assoc`:

    (lookup ,_ emptyenv) => nomatch
    (lookup ,v1 (bind ,v2 ,t ,env)) => (lookup2 ,v1 (equal? ,v1 ,v2) ,t ,env)
    (lookup2 ,_ true ,t ,_) => ,t
    (lookup2 ,v false ,_ ,env) => (lookup ,v ,env)

Tht brings the total to 25 lines.

I think I may have some unresolved confusion between `(var x)` and
`x`; which is supposed to occur in the template?  In Scheme, `(var
x)`.  Also, which is supposed to occur in the environment?  Also `(var
x)`.  Maybe instead of

    (subst ,t ,env) => (subst2 ,t (lookup ,t ,env))

I intended to write

    (subst (var ,t) ,env) => (subst2 ,t (lookup ,t ,env))

I should go back and review this.

Also, `equal?` needs to be provided by the system, at least for atoms,
which requires some sort of special case like this:

    (ap (equal? ,x ,y) ,_ ,_) => (equal? ,x ,y)

This points out how easy it is to add special cases like this in a
term-rewriting system, though we need to make sure the rule precedence
is such that adding the rule has an effect.  Of course, this
implementation doesn’t tell us anything about which definition of
equality is being used; this sort of thing is one of the common
objections to the use of metacircular interpreters to define
semantics.

If, instead of being a magic function name, it is provided through
multiple uses of the same variable name in a pattern, we could allow
this definition of equality to flow through the metacircular
interpreter in the same way; instead of

    (match ,t (var ,v) ,env) => (bind ,v ,t ,env)

we have

    (match ,t (var ,v) ,env) => (match3 ,v ,t (lookup ,v ,env) ,env)
    (match3 ,v ,t nomatch ,env) => (bind ,v ,t ,env)   # new var, not bound
    (match3 ,v ,t ,t ,env) => ,env   # already bound to the same value
    (match3 ,_ ,_ ,_ ,_) => nomatch  # all other cases are conflicting bindings

There’s an additional buglet: lookup should return its positive
results in a form that can’t be the symbol `nomatch`.  So maybe
instead of

    (lookup2 ,_ true ,t ,_) => ,t

we should say

    (lookup2 ,_ true ,t ,_) => (got ,t)

Also probably it’s confusing that `lookup` and `match` return the same
`nomatch` on failure.

At least playing with it mentally like this, I feel like this
term-rewriting paradigm is a much more pliant medium than Lisps are.

A note on syntax
----------------

Above I’ve been slavishly following Scheme syntax; but it would
probably be an improvement if instead of writing

    (args (cons ,a ,d) ,r) => (cons (ev ,a ,r) (args ,d ,r))

we wrote something more like [Darius Bacon’s syntax for
Pythological][0]:

    Args (Cons a d) r: Cons (Ev a r) (Args d r)

in part because that cuts down awkwardly verbose lines like

    (match (cons ,ta ,td) (cons ,pa ,pd) ,env) =>
        (match ,td ,pd (match ,ta ,pa ,env))

to more manageable things like

    Match (Cons ta td) (Cons pa pd) env: Match td pd (Match ta pa env)

[0]: https://github.com/darius/pythological/

The concrete syntax here is something like this:

    program: /\n/* definition* expression /[ \n\t]*/
    definition: expression _ ":" expression "\n"+
    expression: term /[ \t]+/ expression | term
    term: _ symbol | _ var | _ "(" expression _ ")"
    _: /[ \t]*/
    var: /[a-z_][a-z_0-9]*/
    symbol: /[A-Z][a-z_0-9]*/

A draft Qfitzah interpreter
---------------------------

Here’s my current test input for my draft interpreter:

    (NB x) x
    (NB (Simple Test File For Qfitzah))

    (Do (Cover x) it) (Some x Covered it)
    (Do (Cover Leather) Sofas)

    (NB (Higher Order Programming))
    (Map f Nil) Nil
    (Map f (Cons car cdr)) (Cons (Do f car) (Map f cdr))

    (Map (Cover Chocolate) (Cons Police (Cons Raisins (Cons Oreos Nil))))

    (NB (Boolean Definitions))
    (Not Yes) No
    (Not No) Yes
    (If Yes a b) (Do a)
    (If No a b) (Do b)
    (Do Yes) Yes
    (Do No) No
    (And a b) (If a b a)
    (Or a b) (If a a b)

    (NB (This Should Be A Built-in))
    (Eq Yes Yes) Yes
    (Eq No No) Yes
    (Eq Yes No) No
    (Eq No Yes) No

    (NB (Boolean Truth Tables))
    (Well (Not Yes) (Not No))
    (Well (And Yes Yes) (And Yes No) (And No Yes) (And No No))
    (Well (Or Yes Yes) (Or Yes No) (Or No Yes) (Or No No))

    (All Nil) Yes
    (All (Cons a b)) (And (Do a) (All b))
    (Any Nil) No
    (Any (Cons a b)) (Or (Do a) (Any b))

    (Test Yes) Ok
    (Test No) Fail

    (NB (Boolean Tests))
    (Test (All (Cons (And Yes Yes) Nil)))
    (Test (Not (Any (Cons (And Yes No) (Cons (And No Yes) (Cons (And No No) Nil))))))
    (Test (All (Cons (Or Yes Yes) (Cons (Or Yes No) (Cons (Or No Yes) Nil)))))
    (Test (Not (Or No No)))

    (NB (Peano Arithmetic))
    (= Z Z)         Yes
    (= (S x) Z)     No
    (= Z (S x))     No
    (= (S x) (S y)) (= x y)
    (+ Z x)         x
    (+ (S x) y)     (+ x (S y))
    (2)             (S (S Z))
    (3)             (S (2))
    (4)             (S (3))
    (7)             (S (S (S (4))))

    (Test      (= (+ (2) (2)) (4)))
    (Test (Not (= (+ (2) (2)) (2))))
    (Test (Not (= (2) (+ (2) (2)))))
    (Test      (= (+ (3) (4)) (7)))

    (Empty List Is ())

Upon being fed into my incomplete draft interpreter one line at a time
(the interpreter has a bug when it can read more than one line at a
time), it produces this output:

    ↪ ↪ (Simple Test File For Qfitzah)
    ↪ ↪ ↪ (Some Leather Covered Sofas)
    ↪ ↪ (Higher Order Programming)
    ↪ ↪ ↪ ↪ (Cons (Some Chocolate Covered Police) (Cons (Some Chocolate Covered Raisins) (Cons (Some Chocolate Covered Oreos) Nil)))
    ↪ ↪ (Boolean Definitions)
    ↪ ↪ ↪ ↪ ↪ ↪ ↪ ↪ ↪ ↪ (This Should Be A Built-in)
    ↪ ↪ ↪ ↪ ↪ ↪ (Boolean Truth Tables)
    ↪ (Well No Yes)
    ↪ (Well Yes No No No)
    ↪ (Well Yes Yes Yes No)
    ↪ ↪ ↪ ↪ ↪ ↪ ↪ ↪ ↪ ↪ (Boolean Tests)
    ↪ Ok
    ↪ Ok
    ↪ Ok
    ↪ Ok
    ↪ ↪ (Peano Arithmetic)
    ↪ ↪ ↪ ↪ ↪ ↪ ↪ ↪ ↪ ↪ ↪ ↪ Ok
    ↪ Ok
    ↪ Ok
    ↪ Ok
    ↪ ↪ (Empty List Is ())
    ↪ 

Here’s [the draft interpreter source
code](http://canonical.org/~kragen/sw/dev3/qfitzah.s) in amd64
assembly:

            ## Qfitzah, a leap or shortening: from a kilobyte
            ## or two of i386 machine code to a
            ## higher-order programming language with pattern matching,
            ## flexible parametrically-polymorphic data containers, and
            ## dynamically dispatched method calls with multiple dispatch.

            ## To build:
            ## $ gcc -Wl,-z,noseparate-code -static -m32 -nostdlib qfitzah.s -o qfitzah.bloated
            ## $ objcopy -S -R .note.gnu.build-id qfitzah.bloated qfitzah

            ## This version does *not* use bytecode.  But it should
            ## be a good estimate for how much
            ## code is needed for a Qfitzah (with some primitive operations
            ## such as addition).  358 instructions, 731 bytes of code, 40
            ## bytes of data, 1184 bytes of executable.

            ## (Brian Raiter’s sstrip utility reduced the 1056-byte
            ## version of the executable to 828 bytes, a 228-byte
            ## reduction, but I don’t yet have that built into the build
            ## process.)

            ## The m4 manual says, “An important precursor of m4 was GPM;
            ## see C. Strachey, ‘A general purpose macrogenerator’,
            ## Computer Journal 8, 3 (1965), 225–41,
            ## https://academic.oup.com/comjnl/article/8/3/225/336044. GPM
            ## is also succinctly described in David Gries’s book Compiler
            ## Construction for Digital Computers, Wiley (1971).
            ## ...GPM fit into 250 machine
            ## instructions!”  Well, Qfitzah isn’t quite that small yet,
            ## and it may not get there, but it’s a lot more agreeable to
            ## program in than GPM.

            ## Using variables in a template that are not matched in the
            ## pattern is a bug that the interpreter doesn’t detect,
            ## instead crashing:
            ## ↪ (Do Nothing) no
            ## ↪ (Do Nothing)
            ## Segmentation fault
            ##
            ## Using the same variable more than once is also an unchecked
            ## bug, but doesn’t crash:
            ## ↪ (Eq x x) (Yes x)
            ## ↪ (Eq 3 3)
            ## (Yes 3)
            ## ↪ (Eq 3 4)
            ## (Yes 4)

            ## On calling conventions:

            ## My initial thought was to use the standard i386 Linux ABI
            ## (stemming from Microsoft’s cdecl), where %ebx, %esi, %edi,
            ## %ebp, and of course %eip and %esp are preserved across
            ## calls, but %eax, %ecx, and %edx are not; but since my
            ## objective is to make things as small as possible, it was
            ## immediately obvious that passing all the parameters on the
            ## stack is unacceptably code-bloaty, so I was passing up to
            ## three parameters in %eax, %ecx, and %edx, and getting
            ## return values in %eax, and booleans in the flags.  So,
            ## within some limits, I was free to use %ebx, %esi, %edi, and
            ## %ebp as global variables.  I used %ebx as the allocation
            ## pointer, saving 12 bytes of code in the `cons` function,
            ## %esi as the parsing pointer, and %edi as the pointer to the
            ## global set of rewrite rules.

            ## However, I’ve come to the conclusion that this was a
            ## mistake, and callee-saved registers are generally not
            ## useful for i386 size optimization, especially not these.

            ## If you want to preserve a value across a call, you have two
            ## choices: you can push it on the stack (1 byte to push, one
            ## byte to pop) or you can allocate it in a callee-saved
            ## register.  But that means that you have to save and restore
            ## the callee-saved register at entry and exit, which costs
            ## the same 2 bytes; moreover, if you got the value by calling
            ## another function, you need an additional byte to xchg the
            ## value from %eax into the callee-saved register.  Also,
            ## pushing and popping lets you relocate it to a different
            ## register for free.  In theory using a callee-saved register
            ## could still be a win if you have multiple calls across
            ## which to preserve a value, but so far it never has been.
            ## And you have to weigh this dubious benefit against the
            ## benefit of having fewer registers available for
            ## temporaries: 3 temporaries, shared with arguments, is
            ## pretty cramped!

            ## Moreover, in the 8086, the only registers that could be
            ## used as pointers were %ebx, %ebp, %esi, and %edi; while the
            ## i386 removed this restriction, addressing with those
            ## registers still produces tighter code in some cases (like
            ## lodsb and I think base+index), though not in the simplest
            ## cases:

            ## 804816e:     89 48 04                mov    %ecx,0x4(%eax)
            ## 8048171:     89 4b 04                mov    %ecx,0x4(%ebx)
            ## 804812c:     8b 09                   mov    (%ecx),%ecx
            ## 804832a:     8b 13                   mov    (%ebx),%edx
            ## 804816c:     89 03                   mov    %eax,(%ebx)
            ## 8048358:     89 01                   mov    %eax,(%ecx)
            ## 8048358:     89 07                   mov    %eax,(%edi)

            ## Indexing off %esp instead of %ebp does cost an extra byte
            ## tho.

            ## Using a register like %ebx instead of a memory location for
            ## a global variable like the allocation pointer costs an
            ## extra byte of initialization, because the initialization
            ## has to be done with a MOV instruction.  Reserving %ebx in
            ## particular to be call-preserved also costs an extra
            ## push/pop pair around every system call, which is currently
            ## 4 bytes.

            ## So, for the time being, I’ve removed %ebx from the set of
            ## call-preserved registers, leaving only %ebp, %esi, %edi,
            ## and of course %esp and %eip.  Somewhat to my surprise, this
            ## initially made the code a byte *larger*, plus 4 bytes of
            ## data; but I quickly recovered the difference by using my
            ## shiny new temporary register.

            ## All three of these remaining registers have global usages:
            ## %esi is used during parsing as the parsing input pointer,
            ## %ebp is used as a base pointer to the global variables, and
            ## %edi is used as the text output pointer (so you can output
            ## a bytes with three bytes: `mov $'(, %al; stosb`.)

            ## Here’s how we’ll define procedures:
            .macro proc name
            .text 1                 # use subsection 1 for library code
    \name:
            .endm

            ## Global variables are in the data segment, but in order to
            ## use smaller instructions, we load a pointer to the data
            ## segment into %ebp at startup and then never change it.  So
            ## far I’m not using this everywhere.
            .data
    globals:
            .macro my name, initval
            .pushsection .data
    \name:  .long \initval
            .popsection
            .endm

            ## Let’s define a macro for things to do at startup.
            .macro init
            .text 0
            .endm

    init
            .globl _start
    _start: mov $globals, %ebp

            ## We can use this mechanism to reduce the byte weight of
            ## calls to frequently called functions.  The i386 lets you
            ## index into a function pointer table in an indirect-call
            ## instruction: call *4(%ebp), and that’s only 3 bytes, while
            ## a direct call would be 5 bytes, even though it’s
            ## PC-relative.  So with 3 calls, we can reduce 15 bytes of
            ## direct call instructions to 9 bytes of indirect call
            ## instructions and 4 bytes of address data, thus shaving 2
            ## bytes.
            .irp routine, cons, skip_whitespace, read_factor, subst, ev, match
            my \routine\()_address, \routine
            .endr

            ## By using a conditional macro for our calls, we can switch
            ## calls to a given routine between direct and indirect just
            ## by editing the list above:
            .macro do name
            .ifdef \name\()_address
            call *(\name\()_address-globals)(%ebp)
            .else
            call \name
            .endif
            .endm

            ## This interpreter is largely concerned with manipulating
            ## list structure.  Computers nowadays have large memories, so
            ## for any program that runs for a short time, perhaps under a
            ## second, we can get by without a garbage collector.  The
            ## fundamental procedure for constructing list structure is
            ## cons, which creates a pair.  It’s wrapped in a macro here
            ## to facilitate putting it physically after a later procedure
            ## that falls through into it.
            my allocation_pointer, arena
            .macro cons_here
    proc cons
            ## This is 11 bytes instead of 21 bytes thanks in part to
            ## replacing two giant 6-byte memory access instructions with
            ## 3-byte things that index off %ebp.
            push %edi
            mov allocation_pointer-globals(%ebp), %edi
            stosl                   # arg 1, the car, is already in %eax
            xchg %eax, %ecx         # arg 2, the cdr, is in %ecx
            stosl
            xchg %edi, allocation_pointer-globals(%ebp)
            xchg %edi, %eax         # return value (old allocation pointer) in %eax
            pop %edi
            ret
            .endm

            ## We’re going to use pointer alignment to distinguish pair
            ## pointers from other kinds of pointers, including the empty
            ## list (nil); specifically, the low 2 bits of a pair pointer
            ## should be 0.  For this, we define a couple of macros for
            ## jumping if a register does or does not point to a pair.  To
            ## avoid wasting bytes, the \reg here should be a low-byte
            ## register: %al, %bl, %cl, or %dl.  %al in particular makes
            ## the `test` instruction 2 bytes instead of 3.
            .macro jpair reg, dest
            test $3, \reg           # will set ZF if it's a pair
            jz \dest
            .endm
            .macro jnpair reg, dest
            test $3, \reg
            jnz \dest
            .endm

            ## Extracting the fields of a pair:
            .macro car src, dest=none
            .ifeqs "\dest", "none"
            mov (\src), \src        # this is only 2 bytes
            .else
            mov (\src), \dest       # 2 bytes
            .endif
            .endm

            .macro cdr src, dest=none
            .ifeqs "\dest", "none"
            mov 4(\src), \src       # 3 bytes
            .else
            mov 4(\src), \dest      # 3 bytes
            .endif
            .endm

            ## Finally, we need some representation for the empty list,
            ## which needs to test as not being a pair.  This is a little
            ## tricky; the chosen value (1) tests as a constant, but
            ## attempting to fetch its print name will crash.
            .macro setnil reg
            xor \reg, \reg
            inc \reg
            .endm

            ## For such a simple allocator to work, we need a large arena;
            ## and the allocation pointer needs to be aligned in it.  We
            ## do this by aligning the arena to a 4-byte boundary and
            ## then incrementing the allocator pointer by multiples of 4.
            .bss 1
            .balign 4
    arena:  .fill 512*1024*1024

            ## The other kinds of elements in our list structure are
            ## constants, such as uppercase symbols and numbers, which are
            ## represented by words ending in ...01, and variables, which
            ## are represented internally by words ending in ...10, and
            ## externally as lowercase identifiers.  So we have
            ## conditionals for these types corresponding to jpair and
            ## jnpair to test these tag fields:

            .macro jvar reg, dest
            test $2, \reg           # will clear ZF if it’s a var
            jnz \dest
            .endm
            .macro jnvar reg, dest
            test $2, \reg
            jz \dest
            .endm

            ## XXX these aren’t actually used:
            .macro jconst reg, dest
            test $1, \reg           # will clear ZF if it’s a const
            jnz \dest
            .endm
            .macro jnconst reg, dest
            test $1, \reg
            jz \dest
            .endm


            ## So, let’s define what it means to substitute some variables
            ## into a template:
            ## (define (subst t env)
            ##   (if (var? t) (cdr (assq t env))
            ##       (if (pair? t) (cons (subst (car t) env) (subst (cdr t) env))
            ##           t)))

            ## This is wrapped in a macro in order to enable us to
            ## physically put it further down, where `ap` can fall through
            ## into it.

            .macro subst_here
    proc subst
            jnvar %al, 1f           # if t is not a var, jump ahead; otherwise
            do assq                 # look it up with assq (inheriting args), then
            cdr %eax                # we take its cdr, then
            ret                     # return it
    1:      jpair %al, 2f           # if t is not a pair, we just return it
            ret                     # (it’s already in %eax)
    2:      push %eax               # we must preserve argument t across a call
            push %ecx               # and env too.
            cdr %eax                # get (cdr t) for that recursive call,
            do subst                # which inherits env, but might clobber args;
            xchg %eax, %edx         # socking away its return value in %edx,
            pop %ecx                # restoring env for the second recursive call,
            pop %eax                # and also t, before
            push %edx               # saving the first subst return value on the stack;
            car %eax                # what we want to subst now is (car t)
            do subst                # so now our substed car is in %eax,
            pop %ecx                # and our substed cdr in %ecx, so we can
            jmp cons                # tail-call cons and return the result


            ## `assq` is our function for doing a variable lookup in an
            ## environment.  To avoid an extra unconditional jump, I’ve
            ## relocated the tail end of the loop to before the loop entry
            ## point, which has the bizarre effect of putting it before
            ## the *procedure* entry point.  It happens to set ZF when it
            ## succeeds and clear ZF when it fails, but `subst` ignores
            ## that at the moment.  It might make things simpler if it
            ## returned its key argument when it fails, like `walk` from
            ## μKanren?

    2:      cdr %ecx                # go to the next item before falling into assq
    proc assq                       # look up an item %eax in a dictionary %ecx
    1:      jnpair %cl, 1f          # nil or another atom terminates the dict
            car %ecx, %edx          # get the item
            cmp %eax, 0(%edx)       # is our dictionary key this item?  CISC 4ever!1
            jne 2b                  # if not, restart the loop, or
            mov %edx, %ecx          # on success we return the item, or on failure
    1:      xchg %ecx, %eax         # return the non-pair we were examining
            ret
            ## Possibly it would be better to inline `assq` as a macro
            ## inside `subst`, since that’s the only thing that uses it so
            ## far.
            .endm                   # subst_here


            ## In a sense the inverse of `subst` is `match`.  If #(vt) is a var vt,
            ## `(subst '(You #(vt) my #(np)) '((#(np) . wombat) (#(vt) . rot)))`
            ## evaluates to `(You rot my wombat)`, as you'd expect if
            ## you're some kind of psycho stalker, while
            ## `(match '(You rot my wombat) '(You #(vt) my #(np)) '())`
            ## evaluates to `((#(np) . wombat) (#(vt) . rot))`.

            ## In Scheme:
            ## (define (match t pat env)
            ##   (if (var? pat) (cons (cons pat t) env)  ; vars match anything
            ##       (if (pair? pat)  ; pairs match if cars match and cdrs match
            ##           (and (pair? t)  ; a pair pattern can't match an atom
            ##               (let ((a (match (car t) (car pat) env)))  ; match car?
            ##                 (and a (match (cdr t) (cdr pat) a))))   ; then, cdr?
            ##           (and (equal? pat t) env))))  ; consts match only themselves

            ## In addition to returning an environment result in %eax,
            ## `match` also needs to indicate success or failure, which it
            ## does with ZF: ZF set indicates match (“equality”), ZF clear
            ## indicates match failure.  Switching from CF to ZF reduced
            ## the weight of this subroutine from 85 bytes to 76 bytes,
            ## and with further work it’s down to 55.

            ## This has a bug; it treats () the empty list as a var. So
            ## (Gallygoogle ()) matches the same patterns (Gallygoogle x)
            ## would.

    proc match
            ## Case for pattern being an unadorned var:
            jnvar %cl, 2f           # If the pattern is a var,
            xchg %eax, %ecx         # we want to (cons pat t), not (cons t pat)
            push %edx               # save env
            do cons
            pop %ecx                # now cons that pair onto the original env
            do cons
            xor %ecx, %ecx          # set ZF to indicate success
            ret

            ## Case for matching a non-pair against a pair pattern:
    2:      push %ecx               # for recursion, we must save pattern and
            push %eax               # t, the term being matched.
            jnpair %cl, 2f          # ensure pattern is a pair;
            jnpair %al, 1f          # if term is not a pair, fail (clearing ZF);

            ## To match two pairs:
            car %eax                # take car of both the term
            car %ecx                # and of the pattern
            do match                # and allow env to inherit in a recursive call;
            jne 1f                  # if that failed we bail out;
                                    # otherwise,
            xchg %eax, %edx         # put the resulting env in the third param
            pop %eax                # and get original term
            cdr %eax                # for second recursion with (cdr t), and likewise
            pop %ecx                # pat for
            cdr %ecx                # (cdr pat).
            jmp match               # tail-recursing; it’s my result, right (ZF) or wrong (!ZF)

            ## To match a constant pattern:
    2:      cmp %ecx, %eax          # Only succeed on exact equality,
            mov %edx, %eax          # returning the supplied env

            ## Shared epilogue (XXX maybe unshare it?)
    1:      pop %ecx                # discard 2 saved arguments
            pop %ecx
            ret


            ## ev evaluates a term by first evaluating all its children
            ## with evlis (which is just `(map ev t)`), then invoking
            ## ap(ply) on the result.
            ## (define (ev t)
            ##   (if (pair? t) (ap (evlis t) rules) t))
            ## (define (evlis t)
            ##   (if (pair? t) (cons (ev (car t)) (evlis (cdr t))) t))
    proc evlis
            jpair %al, 1f
            ret
    1:      push %eax               # save original t
            cdr %eax
            do evlis
            pop %ecx                # restore original t
            push %eax               # save return value
            xchg %ecx, %eax         # 1 byte — shorter than mov %ecx, %eax
            car %eax
            do ev
            pop %ecx                # pass evlis return value as cdr arg to cons
            # FALL THROUGH into cons (tail call)
            cons_here

            ## I’m thinking I’ll provide primitive procedures for
            ## arithmetic and file I/O by way of terms whose head is the
            ## integer “0”.  For example: integer subtraction.  Here we
            ## have the term in %eax.  This untested strawman evprim
            ## weighs 25 bytes, plus 7 bytes for the test and branch in
            ## ev.
    proc evprim
            cdr %eax
            car %eax, %ebx
            cdr %eax
            cmp $5, %ebx  # (0 0 x y) returns x - y assuming both are ints
            jnz 1f
            car %eax, %ebx
            cdr %eax
            car %eax
            sub %ecx, %eax      # XXX is this backwards?
            or $5, %al          # low-order bits got zeroed by subtraction
    1:      ret

            my rules, -1            # global set of rules, initially nil
    proc ev
            jpair %al, 1f
            ret                     # atoms always evaluate to themselves
    1:      do evlis
            car %eax, %ecx                # check for primitive invocation
            cmp $5, %ecx                  # is the car of the list (tagged) 0?
            jz evprim
            mov rules-globals(%ebp), %ecx # initial rules argument to ap: the global
            # FALL THROUGH to ap


            ## (define (ap t rules)
            ##   (if (not (pair? rules)) t   ; no rewrite rules left? don't rewrite
            ##       (let ((m (match t (caar rules) '()))) ; initially empty env
            ##         (if m (ev (subst (cdar rules) m)) ; matched? subst & eval
            ##             (ap t (cdr rules))))))         ; otherwise, try others
    proc ap
            jpair %cl, 1f
            ret                     # return input t

    1:      car %ecx, %edx          # get first rule
            push %eax               # save input t
            push %ecx               # save input rules
            car %edx, %ecx          # get pattern part of rule
            setnil %edx
            do match                # see if this rule matches inherited t in %eax
            je 1f                   # if that succeeded, go to the success case; or

            pop %ecx
            pop %eax

            cdr %ecx                # move on to next rule and tail-recurse
            jmp ap

            ## Now we have found a match, with the env in %eax; now we
            ## must invoke subst with the template, then return the
            ## instantiated template.
    1:      mov %eax, %ecx          # template is subst’s second argument
            pop %eax                # load saved rules
            car %eax
            cdr %eax
            pop %edx                # discard saved input t
            do subst
            jmp ev

            subst_here                      # XXX no longer necessary to be here

            ## Here are some macros from httpdito:
            .equiv __NR_exit, 1     # linux/arch/x86/include/asm/unistd_32.h:9
            .equiv __NR_read, 3
            .equiv __NR_write, 4

            ## System calls with different numbers of arguments.
            ## `be x, y` is a macro that does `mov x, y` or equivalent.
            .macro sys3 call_no, a, b, c
            be \c, %edx
            sys2 \call_no, \a, \b
            .endm

            .macro sys2 call_no, a, b
            be \b, %ecx
            sys1 \call_no, \a
            .endm

            .macro sys1 call_no, a
            be \a, %ebx
            sys0 \call_no
            .endm

            .macro sys0 call_no
            be \call_no, %eax
            int $0x80
            .endm

            ## Set dest = src.  Usually just `mov src, dest`, but sometimes
            ## there's a shorter way.
            .macro be src, dest
            .ifnc \src,\dest
            .ifc \src,$0
            xor \dest,\dest
            .else
            .ifc \src,$1
            xor \dest,\dest
            inc \dest
            .else
            .ifc \src,$2
            xor \dest,\dest
            inc \dest
            inc \dest
            .else
            mov \src, \dest
            .endif
            .endif
            .endif
            .endif
            .endm

            ## To read input, we need an input buffer; to intern atoms, we
            ## need someplace to put the atom base+length pairs.
            .bss
    input_buffer:
            .fill 65536
            .balign 8   # atoms need to be 8-byte aligned to free tag bits
    atoms:  .fill 8192
            my inptr, input_buffer
            ## Output is handled by setting %edi to point into this output
            ## buffer, then using stosb to add stuff to it.
            .bss
    outbuf: .fill 131072

    init
            mov $outbuf, %edi

            .data
    prompt: .ascii "↪ "
    prompt_end:
    init
    repl:   mov $prompt, %eax
            mov $(prompt_end - prompt), %ecx
            do emit
            do flush
            sys3 $__NR_read, $0, inptr, $255
            test %eax, %eax         # EOF on input?
            jz quit
            ## XXX missing loops for \n; could be multiple lines or partial lines
            mov inptr-globals(%ebp), %esi # copy old inptr to %esi for parsing
            add %esi, %eax  # NUL-termination unnecessary due to zero fill
            mov %eax, inptr-globals(%ebp)
            do handle_line
            jmp repl
    quit:   sys1 $__NR_exit, $0

            ## XXX this needs a lot of attention for reducing code space
    proc print
            cmp $1, %eax    # treat nil like pairs (cmp is only 3 bytes!)
            je 5f
            jnpair %al, 1f          # non-nil atoms treated otherwise
    5:      push %eax               # save S-expression to print
    4:      mov $'(, %al
            stosb
            pop %eax
            ## loop over list items:
    2:      jnpair %al, 3f          # XXX handle improper lists?
    6:      push %eax
            car %eax
            do print
            pop %eax
            cdr %eax
            jnpair %al, 3f
            push %eax
            mov $32, %al
            stosb
            pop %eax
            jmp 6b                  # XXX too many jumps?
    3:      mov $'), %al
            stosb
            ret
    1:      and $~3, %eax        # convert var/constant → base/len pointer
            cdr %eax, %ecx
            car %eax
            ## FALL THROUGH into a tail call to `emit`

    proc emit                       # output a string to output buffer
            push %esi
            mov %eax, %esi          # string base is arg 1, length is arg 2 (%ecx)
            rep movsb
            pop %esi
            ret

    proc flush                      # Send output buffer to actual stdout
            mov $outbuf, %ecx       # base address of bytes to output
            push %ecx
            mov %edi, %edx
            sub %ecx, %edx          # number of bytes to output
            sys1 $__NR_write, $1
            pop %edi                # reset output pointer
            ret

            ## Our grammar looks something like:
            ## prog ::= _ (factor (_ "\n" | _ factor _"\n"))*
            ## factor ::= constant | var | "(" (_ atom)* _ ")"
            ## _ ::= " "*
            ## constant ::= [*-^][*-~]*
            ## var ::= [_a-~][*-~]*
            ##
            ## Constants and vars chew up as many characters as they can.
            ##
            ## A line with two S-expressions (“factors”) defines a rule; a
            ## line with just one offers an expression to evaluate
            ## according to the rules so far.

            ## On inputting a rule, it is added
            ## to the front of the rules list (thus taking precedence over
            ## older rules).

            ## Here’s a crude parser.  Input pointer in %esi points
            ## into NUL-terminated input string.
    proc handle_line
            cld        # XXX not really necessary since DF is always clear
            do read_factor
            jz 1f                   # if blank line, ignore
            ret
    1:      push %eax
            do skip_whitespace
            lodsb    # lodsb;dec: 2 bytes, cmp $'\n, %al: 2; cmp $':, (%esi): 3
            dec %esi # so this approach saves bytes only because of second cmp
            cmp $'\n, %al # if there’s only one expression on the line, not a rule
            jnz 1f
            pop %eax
            do ev
            do print
            mov $'\n, %al
            stosb
            ret
    1:      do read_factor # read replacement template for rule being defined
            pop %ecx                # pop pattern
            jnz parse_error
            ## XXX ignoring the possibility of more than two things on the line
            xchg %ecx, %eax
            do cons
            ## FALL THROUGH into tail call to add_rule

    proc add_rule
            mov rules-globals(%ebp), %ecx # cons onto the existing set of rules
            do cons
            mov %eax, rules-globals(%ebp)
            ## debug print out rules:
            ## do print
            ## mov $'\n, %al
            ## stosb
            ## do flush
            ret

    proc parse_error
            mov $'!, %al
            stosb
            mov $'\n, %al
            stosb
            ret

    proc read_factor
            do skip_whitespace
            lodsb
            dec %esi                # peeking
            cmp $'(, %al            # Is there a nested list?
            jne 1f
            lodsb
            do read_term
            push %eax
            do skip_whitespace
            lodsb
            cmp $'), %al            # indicate success
            pop %eax
            ret
    1:      cmp $'*, %al            # [*-^] starts a constant
            ## <https://stackoverflow.com/a/29577037> explains that with
            ## cmp $2, %eax, jg jumps when %eax > 2, though this is
            ## confusing as
            ## <https://en.wikibooks.org/wiki/X86_Assembly/Control_Flow>
            ## explains; so this comparison has the correct sense:
            jb 3f
            cmp $'^, %al
            ja 2f
            jmp read_constant
    2:      cmp $'_, %al            # _ starts a variable
            je 2f
            cmp $'a , %al           # [a-~] also starts a variable
            jb 3f
            cmp $'~, %al
            ja 3f
    2:      jmp read_var
    3:      cmp $'_, %al # guaranteed to fail and clear ZF, indicating failure.
            ret

            ## Advance input pointer %esi into NUL-terminated input string
            ## to first non-whitespace character.
    proc skip_whitespace
            lodsb
            cmp $32, %al
            je skip_whitespace
            dec %esi
            ret

            ## Always succeeds (possibly returning nil), doesn’t set ZF.
    proc read_term
            do read_factor
            jnz 1f                  # if it failed, skip ahead
            push %eax               # save returned term
            do read_term            # recursive call for tail of term
            push %eax
            do skip_whitespace
            pop %ecx
            pop %eax
            do cons                 # XXX tail call
            ret
    1:      setnil %eax             # return nil if no factor found
            ret

            ## Always succeeds, sets ZF to indicate success.
    proc read_constant
            do read_atom
            ## xor $3, %al is also 2 bytes, same as or $1, %al
            ## So XXX maybe one of these two should fall through into
            ## intern and the other should xor the output of intern with 3
            or $1, %al
            cmp %eax, %eax          # set ZF
            ret

            ## Always succeeds, sets ZF to indicate success.
    proc read_var
            do read_atom
            or $2, %al
            cmp %eax, %eax
            ret

            ## Octal to tagged integer.  Digit count in %ecx, input starts
            ## at %esi.  19 bytes.  Not used yet.
    proc o2ti
            xor %eax, %eax
            xor %ebx, %ebx          # accumulate result in %ebx
    1:      lodsb
            sub $'0, %al            # convert digit from ASCII
            add %eax, %ebx
            shl $3, %ebx     # by shifting after the add instead of before,
            loop 1b
            xchg %eax, %ebx
            add $5, %eax            # we leave space for this type tag
            ret

            ## Decimal to tagged integer.  Digit count in %ecx, input
            ## starts at %esi.  22 bytes.  Not used yet.  If the
            ## difference is only like 6 bytes maybe I’ll just use
            ## decimal.
    proc d2ti
            xor %eax, %eax
            xor %ebx, %ebx          # accumulate result in %ebx
    1:      lodsb
            sub $'0, %al            # convert digit from ASCII
            imul $10, %ebx
            add %eax, %ebx
            loop 1b
            xchg %eax, %ebx
            shl $3, %eax
            add $5, %eax
            ret

            ## Tagged integer to octal, taking integer in %eax.  Outputs
            ## to buffer at %edi.  25 bytes.  Not used yet.
    proc ti2o
            xchg %eax, %ebx
            xor %eax, %eax          # clear high bytes of %eax for the loop
    1:      shr $3, %ebx            # shift first to remove type tag
            mov %bl, %al            # still only 2 bytes!
            and $7, %al             # 2 bytes, shorter than `and $7, %eax`
            add $'0, %al            # convert to ASCII
            test %ebx, %ebx         # don’t recurse if no digits remain
            jz 1f
            push %eax               # buffer up digit for later emission
            call 1b
            pop %eax
    1:      stosb
            ret

            ## I’m thinking about adding character string literals, in a
            ## form like this maybe.  This function would be called after
            ## the open-quote.  51 bytes.
    proc read_string
            xor %eax, %eax
            lodsb
            cmp $'", %al
            jne 1f
    2:      xor %eax, %eax          # tagged integer 0 as list terminator
            mov $5, %al # this is 4 bytes rather than the 5 of mov $5, %eax
            ret
    1:      cmp $'\n, %al
            je 2b                   # just treat this as end of string
            cmp $'\\, %al           # treat \" as embedded "
            jne 1f
            lodsb
            cmp $'\n, %al
            je 2b
    1:      push %eax
            do read_string          # read rest of string
            pop %ecx
            xchg %eax, %ecx         # get saved character back in %eax
            shl $3, %eax
            or $5, %al              # add integer tag
            do cons
            xchg %eax, %ecx
            xor %eax, %eax
            mov $13, %al            # tagged integer 1
            jmp cons # XXX probably place this closer to cons so this jump is short

            ## Always succeeds.
    proc read_atom
            mov %esi, %edx          # save address of start byte
    1:      lodsb
            cmp $'*, %al
            jb 1f
            cmp $'~, %al
            jbe 1b
    1:      dec %esi                # put back last character read
            mov %esi, %ecx          # save end address, then compute length:
            sub %edx, %ecx          # $ecx -= $edx, due to confusing AT&T syntax
            xchg %eax, %edx
            ## FALL THROUGH into intern

            ## (intern base-addr len) checks to see if a string is already
            ## in the atom table, returning it if so, or inserting it if
            ## not; either way it returns the (4-byte-aligned) address.
            ## Can’t fail.  Can’t use assq because it’s doing a string
            ## compare.
    proc intern
            push %esi
            push %edi
            mov $atoms-8, %ebx
            ## At the top of the following loop, %ebx points into (or just
            ## before) the atoms table, %eax points to the string we’re
            ## trying to intern, and %ecx has its length.
    1:      add $8, %ebx         # Advance to next table entry.
            mov (%ebx), %edi     # Load string pointer from table.
            test %edi, %edi      # null string pointer? indicates end of table
                                 # test %edi, %edi is one byte smaller than cmp $0.
            jz 2f                # reached end of table without finding it
            cmp %ecx, 4(%ebx)    # check to see if the lengths match
            jne 1b
            push %ecx            # repe will clobber %ecx
            mov %eax, %esi       # put pointer to needle string into %esi
            repe cmpsb
            pop %ecx
            jne 1b               # go on to next entry unless we found it
    1:      mov %ebx, %eax       # address of found entry (table pointer)
            pop %edi
            pop %esi
            ret
    2:                       # not found, must insert
            mov %eax, (%ebx) # non-null pointer here says this is no longer the end
            mov %ecx, 4(%ebx)
            jmp 1b               # now that we’ve inserted it, it’s “found”

Here’s the resulting 956-byte executable in base64:

    f0VMRgEBAQAAAAAAAAAAAAIAAwABAAAAuIAECDQAAAAAAAAAAAAAADQAIAADACgAAAAAAAEAAAAA
    AAAAAIAECACABAiTAwAAkwMAAAUAAAAAEAAAAQAAAJQDAACUkwQIlJMECCgAAAAsIAMgBgAAAAAQ
    AAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAL2UkwQIv8CzBQi4uJMECLkEAAAA6FYBAADoWAEAALr/AAAAiw20kwQIMdu4
    AwAAAM2AhcB0D4t1IAHwiUUg6EkBAADrxTHbuAEAAADNgPbBAnQMkVL/VQBZ/1UAMcnDUVD2wQN1
    GKgDdRiLAIsJ/1UUdQ+SWItABFmLSQTr0DnIidBZWcOoA3QBw1CLQATo8v///1lQkYsA/1UQWVeL
    fRirkauHfRiXX8OLQASLGItABIP7BXULixiLQASLACnIDAXDqAN0AcPouf///4sIg/kFdNaLTRz2
    wQN0AcOLEVBRiwox0kL/VRR0B1lYi0kE6+WJwViLAItABFr/VQzrw6gCdAnoIwAAAItABMOoA3QB
    w1BRi0AE/1UMkllYUosA/1UMWel0////i0kE9sEDdQiLETkCdfKJ0ZHDg/gBdASoA3UkULAoqlio
    A3UXUIsA6Ob///9Yi0AEqAN1B1CwIKpY6+mwKarDg+D8i0gEiwBWicbzpF7DucCzBQhRifopyjHb
    Q7gEAAAAzYBfw/z/VQh0AcNQ/1UErE48CnUNWP9VEOiU////sAqqw/9VCFl1DpH/VQCLTRz/VQCJ
    RRzDsCGqsAqqw/9VBKxOPCh1D6zoKwAAAFD/VQSsPClYwzwqchQ8XncC6zE8X3QIPGFyBjx+dwLr
    LTxfw6w8IHT7TsP/VQh1EFDo9f///1D/VQRZWP9VAMMxwEDD6IQAAAAMATnAw+h6AAAADAI5wMMx
    wDHbrCwwAcPB4wPi9pODwAXDMcAx26wsMGvbCgHD4vaTweADg8AFw5MxwMHrA4jYJAcEMIXbdAdQ
    6O3///9YqsMxwKw8InUFMcCwBcM8CnT3PFx1Baw8CnTuUOjh////WZHB4AMMBf9VAJExwLAN6fv9
    //+J8qw8KnIEPH52906J8SnRklZXu7iTBQiDwwiLO4X/dBI5SwR18lGJxvOmWXXqidhfXsOJA4lL
    BOv0AFSBBAiwggQIfYIECLeBBAh6gQQIBoEECMCzBwj/////wJMECOKGqiA=
