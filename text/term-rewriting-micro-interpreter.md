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

XXX move this or another section of examples to the beginning?

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

XXX probably move this to the beginning before giving examples

Above I’ve been slavishly following Scheme syntax; but it would
probably be an improvement if instead of writing

    (args (cons ,a ,d) ,r) => (cons (ev ,a ,r) (args ,d ,r))

we wrote something more like [Darius Bacon's syntax for
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
