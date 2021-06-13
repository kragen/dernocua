Darius mentioned [DOPE][0], Kemeny’s predecessor to BASIC, and it
occurred to me that you could simplify it further by unifying
destination variables with line labels.

[0]: https://en.wikipedia.org/wiki/DOPE_%28Dartmouth_Oversimplified_Programming_Experiment%29

In DOPE each line of the program was similar to a line of assembly,
with implicit variable declarations and explicit line numbers and
inputs and outputs.  So to calculate -b+√(b²-4ac) you might say:

    10 * 4 a d    # d := 4 * a
    20 * d c d    # d := c * d
    30 * b b q    # q := b * b
    40 - q d d    # d := q - d
    50 sqr d d    # d := √d
    60 - d b d    # d := b - d

The line numbers permit gotos.  If we require destination variables to
be unique, we could have just as much goto messiness with less
verbosity, and you could also shift the operand one position to the
right to improve readability slightly:

    d:  4 * a      # d  := 4 * a
    d2: d * c      # d₂ := d * c
    q:  b * b
    d3: q - d2
    d4: d3 sqr
    s:  d4 - b

Labels can be omitted for statements executed for side effects.
Conditionals and loops would require some equivalent of SSA φ
functions.  DOPE used FORTRAN-style arithmetic IF (an opcode named “C”
with 4 operands), but we can avoid such abominations with conditional
jump or conditional skip; for absolute value, for example:

    pos:  x > 0
          pos → r       # jump to r if x is positive
    xn:   0 - x         # negate x into xn
    r:    x \/ xn       # set r to either x or xn, whichever is most recent

A different approach, though it doesn’t subsume the need for jumps, is
a conditional operator:

    pos:  x > 0
    xn:   0 - x
    r:    pos ? x xn

Here’s a dot-product routine for nonzero-length vectors without a
high-level FOR construct:

    init: 0
    i0:   0
    i:    i0 \/ i'
    s:    init \/ t
    ai:   a @ i
    bi:   b @ i
    p:    ai * bi
    t:    s + p
    i':   i + 1
    cont: i < n
          cont → i

Changing it to handle zero-length vectors makes it two lines longer:

    init: 0
    i0:   0
    i:    i0 \/ i'
    s:    init \/ t
    stop: i = n
          stop → end
    ai:   a @ i
    bi:   b @ i
    p:    ai * bi
    t:    s + p
    i':   i + 1
          → i
    end:  nop

For *writing* to arrays, you’d probably need some kind of
side-effecting indexed-store operator, like `a ! i x` or something.

However, all of this is pretty shitty compared to Forth — harder to
write and harder to read — and Forth is probably just as easy to
implement, if not to optimize.  These versions are 2–10× smaller,
depending on how you count, and I think more readable, though still
worse than infix:

    0 b - b b * 4 a * c * - sqrt +
    x 0 < if 0 x - else x then
    0 s !  n 0 do  i a @ i b @ *  s +! loop  s @
