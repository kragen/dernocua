Programming by example ought to be easily applicable to regular
expressions, and by extending that with computations and assertions,
it should be possible to make a usable nondeterministic programming
system.

By typing the string “bye” I am writing a program that generates the
string “bye”, and if I’m doing it in Emacs’s incremental-search, all
the instances of “bye” will be highlighted.  If I then back up back to
the “b”, maybe by twisting a time-turner or hitting shift-backspace,
and type “ad”, I have programmed the regexp “b(ye|ad)”, which is a
nondeterministic program that can generate the strings “bye” and
“bad”.  I might then want to hit some other key to cross the two
streams back together and then type “law”, so I have the regexp
“b(ye|ad)law”.  A third key could progressively cast a spell of Kleene
closure over a gradually-increasing number of the last few nodes in
the graph, giving the following progression:

    b(ye|ad)law
    b(ye|ad)law*
    b(ye|ad)l(aw)*
    b(ye|ad)(law)*
    b((ye|ad)law)*

As I’m doing this, it’s reasonable to concurrently display random
strings generated from the program, the shortest strings generated
from it, a FSM diagram of it, a derivation tree of the regexp itself,
the matches it finds in searching some corpus of text, and/or
derivation trees for those matches as well.

It is, I think, straightforward to add zero-width negative lookahead
assertions and positive lookahead assertions to the UI in the same
way.  Providing a UI for tagging some subexpression of the regexp for
reuse, then reusing it elsewhere, is straightforward from the UI
perspective, but of course increases the expressiveness of the system
to the point where it can no longer be parsed precisely with a finite
state machine.

If, instead of typing a string of characters, I type a sequence of
assignment statements, then my program, instead of producing a
sequence of characters from nothing, produces an output set of
variable assignments from a (usually smaller) input set.  In the same
way, I can move around my program and add alternatives or iteration to
parts of it, making it nondeterministic; if I then add assertions to
parts of it, which fail if some condition is not met, I may be able to
make it deterministic again.

Such a program can have arguments, which are variables that it may
read from before assigning to them.  If all my operators are
monomorphic, it can infer some sort of types for all of these
variables, and inject some example values.  And extracting an
expression or sequence of statements into another subroutine is, if
not trivial, at least a straightforward thing to do.  All of this can
be displayed as I’m typing.

The traditional and terser alternative to this sort of
assertion-pruned nondeterministic control flow is Boehm-Jacopini
control flow, consisting of sequencing, conditional repetition, and
if-else conditionals.  You could imagine a key to extend an if-block
backwards from your cursor, whose condition was initially just `true`
and whose else-block was initially empty (or inserted assignments to
any variables needed to keep the following parts of the program
happy), and perhaps a while-block could initially use the condition
`false`, with the selection left on the condition in either case.

A different approach is Dijkstra’s guarded-command language, in which
I suppose you could do the analogous thing.

The approach I’m most interested in at the moment, though, is Baker’s
COMFY approach.  While the Boehm-Jacopini constructs, like Kleene’s
constructs, have a single entry and a single exit, Baker’s forms of
combination have one entry and *two* exits: a success exit (“win”) and
a failure exit (“lose”).  His conditionals and loops are ruled not by
a *value* computed by their conditionals, but, as in Icon and Unicon,
by whether those “conditionals” succeed or fail.  IIRC you can reduce
Baker’s combinations to three, like those of Kleene and those of Boehm
and Jacopini, consisting of the following connections:

    do x y:
        entry = x.entry
        x.win = y.entry
        y.win = win
        x.lose = y.lose = lose
        
    if x y z:
        entry = x.entry
        x.win = y.entry
        x.lose = z.entry
        y.win = z.win = win
        y.lose = z.lose = lose
        
    while x y:
        entry = x.entry = y.win
        x.win = y.entry
        x.lose = win
        y.lose = lose

This straightforwardly permits the construction of early exits from
loops or from subroutines, error handling, and short-circuit Booleans,
and it is easy to compile with a recursive strategy starting from the
end of a subroutine.

