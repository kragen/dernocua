I read [Henry Baker’s columns about COMFY-65 and COMFY-80][0] and
found them very interesting.  He credits the approach to Pratt in the
early 01970s, which is pretty interesting; combined with [top-down
operator precedence][1] — not PEG or TDPL, but a different linear-time
top-down parsing algorithm with better space and time bounds — it
seems like Pratt totally reinvented compilers in a different way in
the 01970s and nobody noticed!

[0]: https://josephoswald.nfshost.com/comfy/summary.html
[1]: http://crockford.com/javascript/tdop/tdop.html

The COMFY-65 approach is “structured control flow” in the sense that
larger pieces of code are built up from smaller pieces of code using a
fixed set of forms of composition, but they aren’t the same forms as
the Kleene set of sequence, alternation, and closure used in the
Böhm-Jacopini theorem.  The key difference is that Pratt’s/Baker’s
pieces of code have one entry and two exits (“win” and “lose”) instead
of one, so they can directly represent arbitrary control-flow graphs.
In COMFY-65 his forms of composition are `seq`, `alt`, `if`, `while`,
`not`, and `loop`, which are similar to the usual constructs but not
the same.

Re-expressing the COMFY approach with constraint satisfaction
-------------------------------------------------------------

I suspect that constraint satisfaction is a productive way to
formulate compilation problems in general, so here’s an attempt to
formulate Baker’s constructs logically as sets of constraints in a
hypothetical hierarchical constraint language supporting the
definition of infix operators, using `yes` and `no` rather than `win`
and `lose`.  Starting with `loop`:

    (loop X):
        entry = X.entry = X.yes
        no = X.no

This is an abbreviation for

    (loop X).entry = X.entry = X.yes
    (loop X).no = X.no

The remaining constructs can be defined as follows:

    (A; B):                # sequence
        entry = A.entry
        A.yes = B.entry
        yes = B.yes
        no = A.no = B.no

    (A || B) = !(!A; !B)   # alternation

    (!X):                  # negation
        entry = X.entry
        yes = X.no
        no = X.yes

    (A ? B : C):           # general conditional
        entry = A.entry
        A.yes = B.entry
        A.no = C.entry
        no = B.no = C.no

    (while A: B):
        entry = A.entry
        A.yes = B.entry
        B.yes = A.entry
        yes = A.no
        no = B.no

Baker’s compiler compiles these constructs recursively, providing
`yes` and `no` (`win` and `lose`) as concrete numbers when `compile`
is invoked.  It does this by filling memory with instructions starting
from the end, such that each of these exit points (the `yes` and `no`
items) generally refer to things that have previously been compiled
and will follow them in memory — possibly immediately, in which case
manifesting the required control flow doesn’t require a jump
instruction.  In that context, though, I’m not totally sure how he
handles loops, which necessarily need a jump back to the beginning of
the loop, which is at a location unknown when the loop body is being
compiled.  I need to look at his code.

But not right now!

An alternate definition of `alt`:

    (A || B):
        entry = A.entry
        A.no = B.entry
        no = B.no
        yes = A.yes = B.yes

Given a program `pass` which does nothing and just passes control to
its `yes`, we could define `loop` as:

    loop X = (while pass: X)

We could define `fail`, which does nothing and just passes control to
its `no`, as `!pass`, we could define sequencing as a conditional:

    (A; B) = (A ? B : fail)

Here's a totally revised, terser version, using some symbols from
Baker’s 1976 note, the above constructions, a Python-like respelling
of the conditional, and C-like blocks instead of Python indentation.
I’m also changing “entry” to “go” (on your mark, get set,...) and
defining ¬X in terms of the conditional, as Darius did in his
“Language of Choice”.  Actually, it occurs to me that COMFY is very
closely related to binary decision diagrams, but its control graph
isn’t constrained to be acyclic...

    pass            { go = yes }
    fail            { go = no }    # do not pass go
    (B if A else C) { go = A.go, A.yes = B.go, A.no = C.go, no = B.no = C.no }
    (while A: B)    { go = A.go, A.yes = B.go, B.yes = A.go, yes = A.no, no = B.no }

    (¬X)      = (fail if X else pass)
    (A; B)    = (B    if A else fail)
    (A / B)   = (pass if A else B)
    (X∞)      = (while pass: X)

I was going to try to unpack a small program in this notation into a
flat pile of constraints, but I’m getting confused about the
class/instance distinction when I try.

A particular instruction might fit into this framework in a form like
the following:

    pushq_rbp { mem[go] = 0x55, yes = go + 1 }

(Since `pushq %rbp` doesn’t use its `no` exit, it imposes no
constraints on `no`.)

More generally, I think straight-line code as cons-lists of bytes can
be emitted as follows:

    straight([])   = pass
    straight(A::B) { mem[go] = A, T = straight(B), T.go = go + 1, yes = T.yes }

There’s a semantic lacuna in the above, though; something like
`pushq_rbp / pushq_rbp` will fail, because there’s no place to insert
the necessary jumps.  (Also, because `pushq_rbp` can’t fail, the
second alternative could be entirely optimized out.)

Dissection of Baker’s Elisp
---------------------------

Here’s the part of Baker’s Elisp code concerned with compiling loops.
It turns out to work more or less the way you’d expect if you know it
compiles things recursively, starting from the end of memory:

    (defun compile (e win lose)
      (cond ((eq (car e) 'loop)
             (let* ((l (genbr 0)) (r (compile (cadr e) l lose)))
               (ra l r)
               r))
            ((eq (car e) 'while)             ; do-while.
             (let* ((l (genbr 0))
                    (r (compile (cadr e)
                                 (compile (caddr e) l lose)
                                 win)))
               (ra l r)
               r))))

So, it begins by generating a branch to 0 at the end of the loop,
saving the address of the jump instruction in `l`; then it compiles
the contents of the loop (possibly including jumps to `lose` and, in
the `while` case, `win`).  It saves the address of the beginning of
the loop in `r`, and then it runs `(ra l r)`:

    (defun ra (b a)
      ;;; replace the absolute address at the instruction "b"
      ;;; by the address "a".
      (let* ((ha (lsh a -8)) (la (logand a 255)))
         (aset mem (1+ b) la)
         (aset mem (+ b 2) ha))
      b)

So this just backpatches the jump; `ha` and `la` are the high and low
bytes of the address, and it stores them two bytes after and one byte
after the address of the jump instruction, which is generated as
follows:

    (defun genbr (win)
      ;;; generate an unconditional jump to "win".
      (gen 0) (gen 0) (gen jmp) (ra f win))

And that’s in terms of `gen`, which is:

    (defun gen (obj)
      ;;; place one byte "obj" into the stream.
      (setq f (1- f))
      (aset mem f obj)
      f)

Modifying `mem` and `f`:

    (defvar mem (make-vector 10 0)
      "Vector where the compiled code is placed.")

    (setq mem (make-vector 100 0))

    (defvar f (length mem)
      "Compiled code array pointer; it works its way down from the top.")

The semantic lacuna mentioned above is filled in this case with an
explicit `genbr` call followed by the backpatching.  But the `win` and
`lose` addresses (which Baker calls continuations) are passed in to
compile the snippets of code within the loop, which in many cases
bottom out in `emit`, which begins by inserting a call to the `genbr`
above if necessary:

    (defun emit (i win)
      ;;; place the unconditional instruction "i" into the stream with
      ;;; success continuation "win".
      (cond ((not (= win f)) (emit i (genbr win)))
             ...))

That is, if the next address to execute is not the address immediately
following where we’re going to be compiling, then first we `genbr` a
jump so that it is.

Naming
------

What should you call something derived from Baker’s system, but
different?  Antonyms for “comfy” include cold, cool, disagreeable,
dissatisfied, hard, strict, troubled, uncomfortable, unfriendly,
unhappy, unpleasant, unsuited, destitute, poor, discontented, needy,
hopeless, miserable, neglected, pitiable, upset, and wretched,
according to Roget’s.  Synonyms include snug, cozy, cushy, homey, and
soft.  Lojban has “kufra” for “foo is comfortable with bar”.
