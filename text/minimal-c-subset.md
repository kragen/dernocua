What’s the smallest straightforward self-compiling compiler, targeting
a conventional assembly language, you could write in a subset of C?

That is, not the smallest subset of C; implementing a very small
subset of C means the compiler doesn’t have to do as much, but being
written in that same very small subset means that everything is more
difficult to do.  Also, though, I’m thinking of something I could
reimplement straightforwardly in assembly.

You need comments.

You surely need subroutines --- syntactically C needs them at least
for main(), and almost certainly there will be things you want to do
in more than one place.  There’s a question of whether or not to
implement recursion.  Without recursion you could statically allocate
all variables and only have a single way to compile lvalue variables
and a single way to compile rvalue variables, but you need `while`.
With recursion you can use a recursive-descent parser, which you
probably should, but you probably need to store some variables in
global space and others in stack frames.

Arguments and return values can be omitted by storing them in global
variables, but I think that will probably obscure the data flow a lot.
If there are arguments, you don’t need an arbitrarily large number of
them.

Alternatives to recursive-descent parsing with local backtracking (PEG
parsing) might be more compact but are unlikely to be as
straightforward.

You need some form of data structuring, either structs or arrays or
both, which means at least one additional kind of lvalue and rvalue.
You don’t need separate struct namespaces, and if you don’t have them
you can avoid having types for expressions at all, treating
characters, ints, and pointers interchangeably as words, as putchar()
and getchar() already do.  Structs might be a big improvement, but
they probably mean you need data of varying sizes.

You could reasonably support such composite data structures only at
global scope, so local variables are only scalars; and, if you do
that, shallow binding might be an alternative to using separate
indexing schemes for globals and locals.  Locals would just be globals
whose value is saved and later restored.

Structs are more appealing if you have dynamic allocation, so you can
build trees out of them using pointers.

In terms of arithmetic, you almost certainly need addition,
subtraction, and integer constants.  You don’t need pointer
arithmetic, and you probably don’t need bitwise operations,
multiplication, division, and modulo.  You surely do need ==, !=, and
at least one kind of ordering comparison.

Boolean operations `&&`, `||` might turn out to be painful to do
without.  Similarly for augmented assignment `+=`, `-=` and pre-
and/or post-increment `--`, `++`.

In terms of control flow, you surely need `if`, and if you don’t have
`else`, you probably need early `return` (and thus `return`).  I don’t
think there’s any advantage to not having nested blocks for `if`, and
little advantage for not requiring them.  Early `return` is more
complicated with shallow binding (you’d probably want to jump to a
shared epilogue to restore the proper set of variables).

I think that’s a sufficient set of statement types: either expression
statements or assignment statements and function calls; `if`; and
possibly `while`.  If we have return values, we need `return`.  Local
variable declarations are needed for local variables, and although C
doesn’t treat them as statements (in particular, you can’t precede
them with a label) I think that’s probably wrong.  Still, it might
turn out to be simpler to require them to all be declared at the top
of the function, as in Smalltalk.

Modern machines have enough registers that you could reasonably
statically allocate one register for a frame pointer, three or four
registers for arguments and returns, and, say, three or four other
registers as temporaries.  Nested function calls would still require
storing the temporary result in someplace that isn’t clobbered by
calls, either in the stack frame or a callee-saved register, so having
a few callee-saved registers would be handy.

All of that is far more complicated than just using a runtime stack
for expression evaluation and passing parameters and return values,
though.  Variadic C functions sort of require the caller to pop the
arguments, but the subset doesn’t have to include variadic functions.
Or, as I said, arguments at all.

At least ignoring `#include` is probably necessary in practice.
Lacking either `#define` or `enum` would be a pretty big impediment to
readability, though, comparable to lacking arguments.

Writing a C compiler without string literals would be pretty hard.
Doing it without data initializers, like basically every Wirth
compiler, wouldn’t be particularly hard, but I think you do need
string literals.  However, I think C-compatible string literals more
or less require some kind of pointer support; I don’t think we can
pass them off as offsets into a table of all constant strings, because
we need to be able to build up new strings at runtime.  I think this
pretty much forces on us the ability to take a pointer into the middle
of an array, and thus C’s equivalence of `a[b]` with `*(a+b)`, though,
and thus `*`.  Maybe we can still get away without expression types
(which we would need for the implicit multiplication by sizeof) by
shifting the pointers left by 2 or 3 bits before dereferencing them,
but of course that would break ABI compatibility with everything else.
I’d sure like to find a way to avoid this mess.

For writing the tokenizer you probably also need character literals.

If you didn’t need C compatibility, for many purposes, you could in
fact use indices into a global string table as your string type, with
maybe a couple of character buffers elsewhere used by other functions
to build up strings incrementally before interning them.
