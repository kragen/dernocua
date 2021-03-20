Darius Bacon’s Parson parsing library includes a beautiful little
example compiler in 11 lines of code, “eg_calc_to_rpn.py”; quoted in
full:

    from parson import Grammar, alter

    g = Grammar(r"""  stmt* :end.

    stmt   :  ident '=' exp0 ';'  :assign.

    exp0   :  exp1 ('+' exp1      :'add')*.
    exp1   :  exp2 ('*' exp2      :'mul')*.

    exp2   :  '(' exp0 ')'
           |  /(\d+)/
           |  ident               :'fetch'.

    ident  :  /([A-Za-z]+)/.

    FNORD ~:  /\s*/.
    """)(assign=alter(lambda name, *rpn: rpn + (name, 'store')))

    ## print ' '.join(g('v = 42 * (5+3) + 2*2; v = v + 1;'))
    #. 42 5 3 add mul 2 2 mul add v store v fetch 1 add v store

As can be seen from the Halp test at the bottom, this is all that’s
needed for Parson to compile an infix grammar to a sequence of
stack-machine operations, although it will go wrong if you use “add”,
“mul”, “fetch”, or “store” as variable names.

XXX

Review of standard properties of Kleene algebras
------------------------------------------------

A “Kleene algebra” is an [idempotent semiring][0] augmented with an
unary “closure” operator “★” with certain properties.  In the concrete
case of regular languages, the + and · operators of the semiring are
alternation and concatenation; that is, if *a* and *b* are two
languages, *a* + *b* is their union (and equal to *b* + *a*, because
set union is commutative), and *a*·*b* is sort of their Cartesian
product: the set of strings that can be produced by concatenating a
string *α* ∈ *a* with a string *β* ∈ *b* to form *a* || *b*.  (This is
only *sort of* their Cartesian product because the string boundary is
lost, and as a result this product operator is associative:
(*a*·*b*)·*c* = *a*·(*b*·*c*), which is not true with most
formulations of the Cartesian product.)  In general *b*·*a* is a
different language.  We can observe that there is a language 0
containing no sentences that is the identity for +, and the language 1
containing only the empty sentence that is the (left and right)
identity for ·.  Multiplication by 0 produces 0: 0·*a* and *a*·0
contains no sentences for any *a* because there are no sentences to
draw from 0 for the left substring (respectively the right substring)
of the product.

[0]: https://en.wikipedia.org/wiki/Semiring

We can also observe that multiplication distributes over addition:
*a*·*b* + *a*·*c* = *a*·(*b* + *c*), because iff you have a string *α*
∈ *a* and a string *γ* ∈ *b* + *c*, then by definition (*α* || *γ*) ∈
*a*·(*b* + *c*).  Let *δ* be *α* || *γ*.  Also by definition, *γ* ∈
*b* ∨ *γ* ∈ *c*.  In the first case *δ* ∈ *a*·*b* by the definition of
·, and therefore *δ* ∈ *a*·*b* + *a*·*c*.  In the second case *δ* ∈
*a*·*c* and so again *δ* ∈ *a*·*b* + *a*·*c*.  The same chain of
reasoning works in reverse and *mutatis mutandis* to show *b*·*a* +
*c*·*a* = (*b* + *c*)·*a*.

These are the semiring properties (+ a commutative monoid operation, ·
a monoid operation, distributivity, and annihilation) so we can
conclude that languages are a semiring under such concatenation and
alternation.  Importantly, this conclusion is not limited to, for
example, regular languages.

It happens that, with the union interpretation of addition, *a* + *a*
= *a*, so languages form a so-called “idempotent semiring”, which
induces a partial ordering relation: *a* ≤ *b* iff *a* + *b* = *b*.
In this case, this is simply the subset relation ⊆.  (I’m not sure
what happens in non-idempotent semirings.)

(Henceforth I will write multiplication simply as juxtaposition.)

The usual Kleene closure operation ★ from regular expressions can be
defined in terms of an equation:

    x★ = 1 + x x★ (or equivalently 1 + x★ x)

[But the definition used for Kleene algebras][1], invented not by
Kleene but by Kozen in 1994, is axiomatic rather than equational:

* 1 + *aa*★ ≤ *a*★
* 1 + *a*★*a* ≤ *a*★
* *ax* ≤ *x* ⇒ *a*★*x* ≤ *x*
* *xa* ≤ *x* ⇒ *xa*★ ≤ *x*

[1]: https://en.wikipedia.org/wiki/Kleene_algebra

A BNF grammar as a set of equations in a Kleene algebra
-------------------------------------------------------

Let’s consider the expression grammar above as a grammar over tokens,
with the semantic actions and tokens stripped out:

    g      : stmt*.

    stmt   :  ident '=' exp0 ';'.

    exp0   :  exp1 ('+' exp1)*.
    exp1   :  exp2 ('*' exp2)*.

    exp2   :  '(' exp0 ')'
           |  number
           |  ident.

Parson parses PEGs, but we can safely regard this as a CFG because it
doesn’t use any of the extra-CFG features of PEGs; for example, it
doesn’t use negation, and it has no ambiguity of the sort that PEGs
resolve in a non-CFG way.  So we can rewrite this as a system of
equations in a Kleene algebra:

> *g* = *s*★  
> *s* = *i* '=' *e*₀ ';'  
> *e*₀ = *e*₁ ('+' *e*₁)★  
> *e*₁ = *e*₂ ('*' *e*₂)★  
> *e*₂ = '(' *e*₀ ')' + *n* + *i* 

We could think of the problem of constructing a parser as the problem
of finding the solution, or at least a least fixpoint, of these
equations.  What (infinite, non-regular) language *g* satisfies this
system of equations?  And a mostly satisfactory answer is “The
language recognized by such-and-such a pushdown automaton,” in general
a nondeterministic one.  We can always compute such an answer, and
it’s reasonable to think of the parser generation problem as the
problem of solving such sets of equations to compute such an answer.

It’s not an entirely satisfactory answer, though, because if the PDA
in question isn’t deterministic, its equivalence to another PDA is
undecidable.  (The 1997 proof that [the problem *is* decidable in the
deterministic case][2] won Sénizergues the 2002 Gödel Prize,
suggesting that it may be difficult in practice.)

[2]: https://en.wikipedia.org/wiki/Deterministic_pushdown_automaton#Equivalence_problem

We don’t need the whole Kleene algebra to express the system of
equations, though; its semiring operations are enough, and we don’t
even need parentheses in the notation, except as literal strings:

> *g* = *s* + *g s*  
> *s* = *i* '=' *e*₀ ';'  
> *e*₀ = *e*₁ + *e*₁ '+' *e*₀  
> *e*₁ = *e*₂ + *e*₂ '*' *e*₂  
> *e*₂ = '(' *e*₀ ')' + *n* + *i* 

Note that there are three “nonlinear” terms in here, where two
nonterminals (that is, from the equation-solving point of view,
unknowns) are part of a single product.  A CFG that cannot do this,
where each concatenation is restricted to at most one nonterminal,
cannot express arbitrarily branching derivations — each parse tree
node can only have a single non-leaf child — but it can still describe
some non-regular languages, for example:

> *p* = '<' *p* '>' + '⚜'

But it can’t match parentheses in more than one place, so it can't
express, for example:

> *q* = '{' *q* '}' + *q q* + '☮'

So these “linear” context-free grammars are a class of languages
strictly larger than regular languages, but strictly smaller than
CFGs.  There’s probably a well-known name for them.

Notational alternatives
-----------------------

Consider the original grammar again:

    stmt* :end.

    stmt   :  ident '=' exp0 ';'  :assign.

    exp0   :  exp1 ('+' exp1      :'add')*.
    exp1   :  exp2 ('*' exp2      :'mul')*.

    exp2   :  '(' exp0 ')'
           |  /(\d+)/
           |  ident               :'fetch'.

    ident  :  /([A-Za-z]+)/.

    FNORD ~:  /\s*/.

Or the semantics-free version:

    stmt*.

    stmt   :  ident '=' exp0 ';'.

    exp0   :  exp1 ('+' exp1)*.
    exp1   :  exp2 ('*' exp2)*.

    exp2   :  '(' exp0 ')'
           |  /(\d+)/
           |  ident.

    ident  :  /([A-Za-z]+)/.

    FNORD ~:  /\s*/.

If we were driven by a mad Tuftean urge to minimize ink on the page,
we could start by shortening the identifiers as I did before:

    s*.

    s   :  i '=' e ';'.

    e   :  f ('+' f)*.
    f   :  g ('*' g)*.

    g   :  '(' e ')'
        |  /(\d+)/
        |  i.

    i  :  /([A-Za-z]+)/.

    FNORD ~:  /\s*/.

Then we could omit the (strictly speaking, redundant) colons, and
replace the `|` with something lighter, such as `,`, even though `;`
would have a more accurate connotation from Prolog:

    s*.

    s  i '=' e ';'.

    e  f ('+' f)*.
    f  g ('*' g)*.

    g  '(' e ')',
       /(\d+)/,
       i.

    i  /([A-Za-z]+)/.

    FNORD ~  /\s*/.

If we switch to `;` for rule terminators, we could use `.` to tag
nonterminals, thus eliminating the need for *most* quotes:


    .s*;
    s  .i = .e ';';
    e  .f (+ .f)*;
    f  .g ('*' .g)*;
    g  '(' .e ')', /(\d+)/, .i;
    i  /([A-Za-z]+)/;
    FNORD ~  /\s*/;

Hmm, that didn’t pay off quite as well as I was hoping; I could
instead tag the literal tokens with a lighter-weight `:`, perhaps,
unless they contain whitespace:

    s*.
    s  i := e :; .
    e  f (:+ f)*.
    f  g (:* g)*.
    g  :( e :) , /(\d+)/, i.
    i  /([A-Za-z]+)/.
    FNORD ~  /\s*/.

We can replace Kleene’s `*` with a “join” operator, for which we can
use `;`, vaguely connected to Perl’s `$;`; ( number; :, ) would mean
“one or more numbers separated by commas”, for example, equivalent to
the current (number (:, number)\*) construct.  Parson spells this
`number ** ','` or, in the Python interface, `star(number,
separator=',')`.  The idea of `;` is that it's lower-noise than `**`
and it binds *less* tightly than concatenation, or `,` alternation.
This gives us:

    , s ; .
    s  i := e :; .
    e  f ; :+ .
    f  g ; :* .
    g  :( e :) , /(\d+)/, i.
    i  /([A-Za-z]+)/.
    FNORD ~  /\s*/.

This eliminates the multiple references that gave rise to the
necessity for naming f and g, so we can reduce this to:

    , s ; .
    s  i := e :; .
    e  ((:( e :) , /(\d+)/, i) ; :*) ; :+ .
    i  /([A-Za-z]+)/.
    FNORD ~  /\s*/.

This is kind of unreadable but it’s also 97 characters.  To crunch it
*further* we can try defining nonterminals inline; instead of saying
`i := e :; .` and then only later defining `i`, we can define it right
then and there by saying `<i /([A-Za-z]+)/> := e :; .` If we want to
refer to `i` again, and we do, it's probably more readable to refer to
it as `<i>`, although that obviously does cost some strokes if we’re
playing golf.  This also means that the whole grammar can be inlined
into one giant unreadable expression, so we no longer need any
terminating periods.  Meanwhile we can rename FNORD to `_`, as in a
variable you’re ignoring in Prolog, ML, Python, or Erlang.  Then we
have *this*:

    , <_ /\s*/> <i /([A-Za-z]+)/> := <e ((:( <e> :) , /(\d+)/, <i>); :* ); :+ > :; ;

That's 80 characters: an infix precedence partner for possibly-empty
sequences of assignment statements in one line of code.

I don’t like the colon-delimited tokens, though.  It’s too easy to
remove the whitespace following them.  So I'm going to add some noise
back in:

    ,<_ /\s*/> <i /([A-Za-z]+)/> "=" <e (( "(" <e> ")", /(\d+)/, <i>); "*"); "+"> ";";

It’s 83 characters now, but I think enormously more readable.

So those are our means of *composition* or combination of grammars to
make richer grammars.  But it would also be useful to have a lot of
canned *primitives* with common meanings, not just regular expressions
and constant strings, for common kinds of tokens with common
semantics.  For example:

* $a one or more upper and lowercase letters
* $A one or more uppercase letters
* $w one or more digits, upper and lowercase ASCII letters, and
  underscores, starting with a non-digit
* $s zero or more spaces, tabs, carriage returns, or newlines (but not
  vertical tabs!)
* $S zero or more Unicode whitespace characters, including $s
* $u a single Unicode codepoint encoded in UTF-8
* $U one or more non-ASCII characters
* $d possibly signed decimal integer
* $n decimal integer with no sign
* $r either carriage return, linefeed, or carriage return and then linefeed
* $R the rest of the line: /.*/ $r
* $x hexadecimal digit
* $f possibly signed decimal floating-point number
* $c C-style double-quoted string with \-escaping of doublequotes and \\
* $e Elisp-style double-quoted string with \-escaping and possible
  embedded newlines
* $q SQL-style apostrophe-quoted string with doubling of embedded apostrophes
* $# comment to end of line introduced with #
* $^ ASCII control characters in general, including carriage returns,
  linefees, tab, and delete, but not including the ISO-8859-1 control
  characters after delete, the other Unicode control characters like
  ZWNJ, or space (ASCII 32)

Such an arsenal of preloaded ammunition allows us to reduce the above
expression grammar to 62 characters, about 25%:

    ,<_ $s> $a "=" <e (( "(" <e> ")", $n, $a); "*"); "+"> ";";

We could even make some reasonable extensions:

    ,<_ $s, $#> $w "=" <e (( "(" <e> ")", $n, $w); "*", "/"); "+", "-"> ";";

An accommodation especially for precedence parsers would be to declare
that the `;` operator associates to the left, allowing us to flatten
the grammar considerably at, perhaps, some cost to readability:

    ,<_ $s, $#> $w "=" <e "(" <e> ")", $n, $w; "*", "/"; "+", "-"> ";";

As written, this can accidentally match the empty string an infinite
number of times, which may or may not be a problem depending on your
matching technology.  If so, parens help:

    ,(<_ $s, $#> $w "=" <e "(" <e> ")", $n, $w; "*", "/"; "+", "-"> ";";)

Because `;x` matches zero or more `x`es, we can rewrite this without
any parens at all:

    ; <_ $s, $#> $w "=" <e "(" <e> ")", $n, $w; "*", "/"; "+", "-"> ";"

If we define a lowest-precedence `@@` operator which discards its
right argument, we could write this perhaps more readably as

    ,($w "=" <e> ";";)
    @@
        <_ $s, $#>
        <e "(" <e> ")", $n, $w; "*", "/"; "+", "-">

Using apostrophes instead of doublequotes:

    ,($w '=' <e> ';';)
    @@
        <_ $s, $#>
        <e '(' <e> ')', $n, $w; '*', '/'; '+', '-'>

JSON might be (from memory) something like

    <v "[" <_ $s> (,(v; ",")) "]"
     , "{" (,(<s $c> ":" <v>; ",")) "}"
     , ("true", "false", "null") !!$s
     , $f
     >

Hmm, I just checked, and JSON has a slightly more complex string
syntax, and doesn’t actually require whitespace after the keywords as
I claimed above.  And my definition above of $s happens to be perfect
for JSON.

    <v '[' <_ $s> (,(<v>; ',')) ']'
     , 'true', 'false', 'null'
     , <s '"' 
        (;
            !'"' !'\\' !$^ $u,
            '\\' ('"', '\\', '/', 'b', 'f', 'n', 'r', 't', 'u' $x $x $x $x)
        ) '"'>
     , '{' (,(<s> ':' <v>; ',')) '}'
     , $f
     >

You might want to add more tags and regex captures to help with
semantic actions:

    ,(<_ $s, $#> <s $w> "=" <e <t "(" <e> ")", <k $n>, <f $w>;
                               <m /([*/])/>; <a /([-+])/>>";";)

An alternative to `;` might be `|`, as in Haskell list comprehensions,
though that looks awkward without extra whitespace:

    ,(<_ $s, $#> $w "=" <e "(" <e> ")", $n, $w | "*", "/" | "+", "-"> ";" | )

Or `:`, since we aren't using that for anything else and it's less
jarring than `|` in the absence of whitespace:

    ,(<_ $s, $#> $w "=" <e "(" <e> ")", $n, $w: "*", "/": "+", "-"> ";":)

Or `*` of course, although that visually binds more tightly than ",":

    ,(<_ $s, $#> $w "=" <e "(" <e> ")", $n, $w * "*", "/" * "+", "-"> ";" *)

An alternative to <x y> would be x: y.  This would reduce the `;`
version to

    ,(<_ $s, $#> $w "=" e: "(" e ")", $n, $w; "*", "/"; "+", "-". ";";)

An alternative use of `.` would be for canned primitives:

    ,(<_ .s, .#> .w "=" e: "(" e ")", .n, .w; "*", "/"; "+", "-". ";";)
