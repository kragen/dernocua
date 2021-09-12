Today Andrius Štikonas got the `hex0_riscv64` bootstrap seed program
down to 392 bytes; it translates from hexadecimal into binary, though
much of the bulk of the program is opening and closing files.  This
led me to thinking about the question of Kefitzat haDerekh, shortening
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

    (define (ev t)                                 ; eval, for tree rewriting
      (if (pair? t) (ap (map ev t) rules) t))      ; atoms don’t get rewritten

    ;; apply, for tree rewriting, but the arguments are the top-level tree
    ;; to rewrite, after all its children have been rewritten as above, and
    ;; the remaining set of rules to attempt rewriting with
    (define (ap t rules)
      (if (null? rules) t               ; no rewrite rules left? don’t rewrite
          (let ((m (match t (caar rules) '()))) ; initially no vars () match
            (if m (ev (subst (cdar rules) m))  ; rule matched? substitute & eval
                (ap t (cdr rules))))))         ; otherwise, try the other rules

That depends on definitions of `match`, `emptyenv`, and `subst`.
`subst` is easy enough (though I got it wrong at first, and it might
be nicer to handle the case where the variable is undefined):

    (define (subst t env)
      (if (var? t) (cdr (assoc t env))
          (if (pair? t) (cons (subst (car t) env) (subst (cdr t) env))
              t)))

Then `match` needs to compute whether there’s a match, which requires
it to distinguish variables from other things.  In its simplest form
we can consider variables that occur more than once an error, but an
error we don’t try to detect; then it might look like this:

    (define (match t pat env)
      (if (var? pat) (cons (cons pat t) env)  ; vars match anything
          (if (pair? pat)  ; pairs match if the cars match and the cdrs match
              (and (pair? t)  ; a non-var pair pattern can’t match an atom
                  (let ((a (match (car t) (car pat) env)))  ; try to match car
                    (and a (match (cdr t) (cdr pat) a))))   ; then, try the cdr
              (and (equal? pat t) env))))  ; non-var atoms match only themselves

Then you just need some kind of convention for marking variables.  The
simplest thing in Scheme would be to use `,x`, which is syntax sugar
for `(unquote x)`:

    (define (var? pat) (and (pair? pat) (eq? (car pat) 'unquote)))

(This has the unfortunate effect that you can’t use the atom `unquote`
in head position in either a pattern or a replacement template.  You
could fix this by quoting all the atoms in patterns and replacements,
but probably a better idea is to use `#(varname)`.)

And that’s it.  19 lines of Scheme in
terms of `define`, `if`, `'()`, `cons`, `pair?`, `let`, `car`, `cdr`,
`caar`, `cdar`, `#f`, `and`, `equal?`, `assoc`, `map`, and `null?`
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

Here’s what `subst` might look like with that setup.  I was working
from this earlier version of `subst`:

    (define (subst t env)
      (if (pair? t) (cons (subst (car t) env) (subst (cdr t) env))
          (let ((v (lookup t env)))
            (if v (cdr v) t))))

In i386 assembly:

            # subst t env returns a version of t with atom substitutions from env.
    subst:  push %ebp               # callee-saved variable used here
            push %eax               # %eax has t, %ecx has env
            push %ecx
            test $3, %al
            jnz 1f                  # jump if not a pair
            mov 4(%eax), %eax       # get cdr t for (subst (cdr t) env)
            call subst              # inherits our env.  calls are 5 bytes
            mov %eax, %ebp          # save subst result
            mov 4(%esp), %eax       # load saved t
            mov (%eax), %eax        # car t
            mov (%esp), %ecx        # second argument is saved env
            call subst
            mov %ebp, %ecx          # second cons argument is (subst (cdr t) env)
            call cons
    2:      pop %ecx                # discard saved arguments; labeled for
            pop %ecx                # epilogue sharing
            pop %ebp
            ret

    1:      call lookup             # inherits both arguments; sets CF if not found
            jc 1f
            mov 4(%eax), %eax       # return value is cdr of lookup return value
            jmp 2b                  # returns via shared epilogue

    1:      mov 8(%esp), %eax       # return original t
            jmp 2b

That’s 24 instructions and 60 bytes of machine code,
and, although I’m sure I missed a few
tricks, I don’t think it’s going to get more than about 30% smaller.
That’s 15 bytes per line of Scheme, which I think is pretty good, but
it puts the estimate of the whole 19-line Scheme program at 285 bytes,
which doesn’t include the non-open-coded primitives like `cons` (and
`assoc` and `map`), the parser, or I/O.  I/O is actually almost all of
`hex0_riscv64`.

Trying to do this in RV64 without the C compressed-instruction
extension, like `hex0_riscv64`, would surely have much worse code
density; *with* the C extension it might be slightly more compact.

### A sketch of `subst` in a stack bytecode ###

XXX this is also the old version of the Scheme code

In one of the bytecodes suggested in file `c-stack-bytecode.md` this
might look like this:

    PROCEDURE subst argwords=2
        loadword 0  ; t
        call pair?
        jztos 1f    ; if not a pair, skip
        loadword 0
        call car
        loadword 1  ; env
        call subst
        loadword 0
        call cdr
        loadword 1
        call subst
        call cons
        ret
    1:  loadword 0
        loadword 1
        call lookup
        dup
        jztos 1f     ; jump if top of stack is 0, i.e., nil
        call cdr
        ret
    1:  drop
        loadword 0
        ret

According to the hypotheses in that note, this might compile to 2
bytes of procedure header, 23 opcode bytes, 8 operand bytes for call
instructions, 2 operand bytes for jump targets, and a 2-byte entry in
a global subroutine table, for a total of 37 bytes.  At this rate, the
whole Scheme program irresponsibly extrapolates to 175¾ bytes, but of
course you’d have to add the bytecode interpreter on top of that.  On
the other hand, if the bytecode interpreter is customized specifically
to run the term-rewriting interpreter, none of the call instructions
will need an operand byte, because there’s plenty of opcode space to
allocate each subroutine in this program a single-byte opcode.  That
would bring it down to 29 bytes, less than half the size of the i386
machine code, irresponsibly extrapolating the whole Scheme program to
137¾ bytes of machine code.

Dynamic dispatch
----------------

XXX move this or another section of examples to the beginning?

Because patterns can dispatch on more than just the function being
called, you can define “methods” on “classes”; one of the examples in
the Aardappel dissertation is defining a hash method for a point class:

    hash(point(x,y)) = x*y

Or, in S-expression syntax using unquote:

    (hash (point ,x ,y)) => (* ,x ,y)

Which you could feed into the Scheme strawman interpreter above as
follows:

    (define rules '(((hash (point ,x ,y)) (* ,x ,y))))

Elsewhere you might define how to rewrite `hash` expressions applied
to other types of values; then a hashtable implementation can invoke
`hash` without worrying about the types of its arguments.  The
compiler transformation described above would gather all the `hash`
rules togther into a subroutine, which then performs a sequence of
conditional tests to dispatch to one of them.

This also permits CLOS-style multiple dispatch:

    (* (scalar ,s) (vec ,x ,y ,z)) => (vec (* ,s ,x) (* ,s ,y) (* ,s ,z))
    (* (scalar ,s) (scalar ,t)) => (scalar (* ,s ,t))
    (* (m ,r1 ,r2 ,r3) ,vec) => (vec (dot (vec . ,r1) ,vec)
                                     (dot (vec . ,r2) ,vec)
                                     (dot (vec . ,r3) ,vec))
    (dot (vec ,a ,b ,c) (vec ,d ,e ,f)) => (+ (* ,a ,d) (* ,b ,e) (* ,c ,f))

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

    (map ,f nil) => ()
    (map ,f (cons ,car ,cdr)) => (cons (call ,f ,car) (map ,f ,cdr))

Then you can define patterns like this:

    (call (cover ,material) ,base) => (some ,material covered ,base)

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

    (apply (qsortcompare ,x) ,y) => (< ,y ,x)
    (filter nil ,_) => (pair nil nil)
    (filter ((cons ,h ,t) ,f)) => (filter2 (filter ,t ,f) ,h ,f (apply ,f ,h))
    (filter2 (pair ,a ,b) ,h ,f true) => (pair (cons ,h ,a) ,b)
    (filter2 (pair ,a ,b) ,h ,f false) => (pair ,a (cons ,h ,b))

(This also demonstrates how the term-rewriting paradigm implicitly
provides conditionals.)

Oortmerssen discusses this further in pp. 48–50 (§4.1.2).

In the language implemented by the interpreter above, you could just
as well define things this way:

    (map ,f (cons ,car ,cdr)) => (cons (,f ,car) (map ,f ,cdr))
    ((cover ,material) ,base) => (some ,material covered ,base)
    ((qsortcompare ,x) ,y) => (< ,y ,x)
    (filter ((cons ,h ,t) ,f)) => (filter2 (filter ,t ,f) ,h ,f (,f ,h))

This would have the advantage that you could pass in the name of any
existing function.  But compiling this efficiently might be
nontrivial.

It might be worthwhile to implement lambda-lifting to get closures.
Aardappel experimented with this but ultimately rejected it.

A metacircular term-rewriting interpreter
-----------------------------------------

If you love term rewriting so much, why don’t you marry it, huh?
Why’dja write that “strawman” above in *Scheme*?  Are you *chicken*?

XXX the below lacks some bugfixes from the Scheme

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
