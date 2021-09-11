Today Andrius Štikonas got the `hex0_riscv64` bootstrap seed program
down to 392 bytes; it translates from hexadecimal into binary, though
much of the bulk of the program is opening and closing files.  This
led me to thinking about the question of kefitzat haderech, shortening
the path: can we teleport directly from a few hundred bytes of machine
code to something much more amenable to writing compilers?

Term rewriting languages like Q, Pure, Mathematica, Maude, or
Aardappel seem more amenable to writing compilers not only than
imperative languages like C but also more so than traditional Lisps;
it implicitly provides conditionals, pattern-matching for arguments,
ad-hoc polymorphism with multiple dispatch, and parametric
polymorphism.  As Oortmerssen’s dissertation on Aardappel points out
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

An interesting thing about this is that, despite the vastly increased
expressive power (especially for things like writing compilers), the
code to implement a term-rewriting interpreter is roughly as simple as
the code to implement an ur-Lisp interpreter, just much slower.
However, I don’t think it’s actually any *simpler* than the ur-Lisp,
and it’s surely a bit larger than `hex0_riscv64`.

A Scheme strawman interpreter for term rewriting
------------------------------------------------

The interpreter is pretty simple.  Basically, to evaluate a non-atomic
expression, you first evaluate its components, and then you loop over
the rewrite rules, trying to match each one against the expression,
and when one of them succeeds you instantiate its replacement with the
match values, then evaluate the instantiated replacement.  Something
like this in Scheme (untested):

    (define (ev t)                                 ; eval, for tree rewriting
      (if (pair? t) (ap (args (cdr t)) rules) t))  ; atoms don’t get rewritten

    (define (args xs)    ; evlis, for tree rewriting; applied to the head too
      (if (null? t) '() (cons (ev (car xs)) (args (cdr xs)))))

    (define (ap t rules) ; apply, for tree rewriting, but with different arguments
      (if (null? rules) t               ; no rewrite rules left? don’t rewrite
        (let ((m (match t (caar rules) emptyenv)))
          (if m (ev (subst (cdar rules) m)) ; if rule matched, substitute & eval
                (ap t (cdr rules))))))      ; otherwise, try the other rules

That depends on definitions of `match`, `emptyenv`, and `subst`.  `subst`
is easy enough:

    (define (subst t env)
      (if (pair? t) (cons (subst (car t) env) (subst (cdr t) env))
        (let ((v (lookup t env)))
          (if v (cdr v) t))))

Then `match` needs to compute whether there’s a match, which requires
it to distinguish variables from other things.  In its simplest form
we can consider variables that occur more than once an error, but an
error we don’t try to detect; then it might look like this:

    (define lookup assoc)

    (define emptyenv '())

    (define (match t pat env)
      (if (var? pat) (cons (cons pat t) env)  ; vars match anything
        (if (pair? pat)  ; pairs match if the cars match and the cdrs match
          (if (pair? t)  ; a non-var pair pattern can’t match an atom
            (let ((a (match (car t) (car pat) env)))  ; try matching the car
              (and a (match (cdr t) (cdr pat) a)))    ; then, try the cdr
            #f)
          (and (equal? pat t) env))))  ; non-var atoms match only the same atom

Then you just need some kind of convention for marking variables.  The
simplest thing in Scheme would be to use `,x`, which is syntax sugar
for `(unquote x)`:

    (define (var? pat) (and (pair? pat) (eq? (car pat) 'unquote)))

And that’s it.  Unless I've forgotten something, 23 lines of Scheme in
terms of `define`, `if`, `'()`, `cons`, `pair?`, `let`, `car`, `cdr`,
`caar`, `cdar`, `#f`, `and`, `equal?`, `assoc`, and `null?` gives you
a bottom-up, source-order-precedence term-rewriting interpreter.  If
we want to include implicit equality testing in patterns when a
variable occurs more than once, it’s a couple more lines of code, but
that’s about a 10% total complexity increase.

(Hmm, now I realize that `subst` presupposes that variables aren’t
pairs, but that bug probably doesn’t actually translate to assembly,
so I’ll leave it for now; avoiding it would involve calling `var?`
before `pair?` and perhaps instead of using the return value of
`lookup`.)

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
`pair?`, `car`, `cdr`, `equal?`, `assoc`, and `null?`.  Most of these
are not very difficult.

(None of the assembly code below is tested.)

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

But the SBCL approach of tagging the pointer would be shorter:

    sbcons: mov %eax, 0(%ebx)       # car was arg 1
            mov %ecx, 2(%ebx)
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

If we instead use two low-order 0 bits to tag cons pointers, list
operations get smaller still, to the point where almost all of them
are so small that they need to be open-coded:

    00000036 <altcons>:  # 11 bytes
      36:	89 03                	mov    %eax,(%ebx)
      38:	89 4b 02             	mov    %ecx,0x2(%ebx)
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

Here’s what `subst` might look like with that setup:

            # subst t env returns a version of t with atom substitutions from env.
    subst:  push %ebp               # callee-saved variable used here
            push %eax               # %eax has t, %ecx has env
            push %ecx
            test $3, %al
            jnz 1f                  # jump if not a pair
            mov 4(%eax), %eax       # get cdr t for (subst (cdr t) env)
            call subst              # inherits our env
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

That’s 60 bytes of machine code, and although I’m sure I missed a few
tricks, I don’t think it’s going to get more than about 30% smaller.
That’s 15 bytes per line of Scheme, which I think is pretty good, but
it puts the estimate of the whole 23-line Scheme program at 345 bytes,
which doesn’t include the non-open-coded primitives like `cons` (and
`assoc`/`lookup`), the parser, or I/O.  I/O is actually almost all of
`hex0_riscv64`.

Trying to do this in RV64 without the C compressed-instruction
extension, like `hex0_riscv64`, would surely have much worse code
density; *with* the C extension it might be slightly more compact.

Dynamic dispatch
----------------

Because patterns can dispatch on more than just the function being
called, you can define “methods” on “classes”; one of the examples in
the Aardappel dissertation is defining a hash method for a point class:

    hash(point(x,y)) = x*y

Or, in S-expression syntax using unquote:

    (hash (point ,x ,y)) => (* ,x ,y)

Elsewhere you might define how to rewrite `hash` expressions applied
to other types of values; then a hashtable implementation can invoke
`hash` without worrying about the types of its arguments.  The
compiler transformation described above would gather all the `hash`
rules togther into a subroutine, which then performs a sequence of
conditional tests to dispatch to one of them.

This also permits CLOS-style multiple dispatch:

    (* (scalar ,s) (vec ,x ,y ,z)) => (vec (* ,s ,x) (* ,s ,y) (* ,s ,z))
    (* (scalar ,s) (scalar ,t)) => (scalar (* ,s ,t))
    (* (m ,r1 ,r2 ,r3) ,vec) => (vec (dot ,r1 ,vec) (dot ,r2 ,vec) (dot ,r3 ,vec))

Higher-order programming
------------------------

In languages like C or Lisp, the atom-head requirement Aardappel has
would prevent you from doing any higher-order programming, but not in
term-rewriting languages, because you can use the same
dynamic-dispatch trick.  You can define a higher-order mapcar function
as follows:

    (map ,f nil) => ()
    (map ,f (cons ,car ,cdr)) => (cons (apply ,f ,car) (map ,f ,cdr))

Then you can define patterns like this:

    (apply (cover ,material) ,base) => (some ,material covered ,base)

so that `(apply (cover chocolate) raisins)` rewrites to `(some
chocolate covered raisins)`.  I learned about this on p. 35 of the
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
