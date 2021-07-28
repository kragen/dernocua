:fq0zl, a normal-order text macro language
==========================================

Textual macro replacement languages like m4 are famous for being easy
to implement and eliminating artificial barriers to factoring out
duplication.  They also have a very low barrier to entry for new
programmers.  However, they also have a lot of problems.

m4 is notoriously hard to use, although it’s often effective.  Part of
the problem is that data is re-executed both on its way into and on
its way out of macro invocations, so you often need
quoting — confusingly, multiple levels thereof.  Worse, if you are
missing a level of quoting, your code will often appear to work until
some previously inert data happens to have a macro invocation in it.

m4’s design has a number of other avoidable defects.  It’s
whitespace-sensitive in a way that impairs readability.  Often m4
macros collide with ordinary words, resulting in accidental macro
invocations that corrupt the text.  Since it was defined, the ASCII
apostrophe has been redefined as a terrible symmetrical typewriter
glyph, depriving m4’s default quote characters of their symmetry.  And
m4’s parameter-passing mechanism is so purely positional that, as in
Forth, you can’t even name your arguments.

Can we define a text macro language that retains the basic processing
paradigm of m4, m6, and cpp, but has a better balance of power and
usability?

Existing macro languages
------------------------

TeX is a pure macro-expansion system, perhaps the most successful
attempt, but I suspect we can do better.  Tcl is semantically mostly a
macro-expansion language, and although it’s somewhat limited it’s at
least usable.  Mooers’s TRAC is hard to find information about.
MediaWiki templates, sh, make, PHP, ES6, Perl, cpp, macro assemblers,
and many other languages implement string interpolation in more or
less central ways.

Normal-order macro expansion
----------------------------

If macro *output* is not subject to macro expansion, we have
“applicative-order macro expansion”, and m4 loses its
Turing-completeness, making it much more comprehensible (all the macro
invocations that will be expanded are explicitly present in the input
file) but also much less useful.  (m4’s predecessor m6†, which was
included with early versions of Unix, offered the call-time option to
expand a macro in this fashion by terminating the call with a
semicolon.)

On the other hand, if macro *input* is not subject to macro expansion,
much of the need for quoting disappears, but Turing-completeness
remains.  This is “normal-order macro expansion”.  Done naïvely, there
are cases where it will take exponentially longer than m4’s strategy,
but I think these can be mostly avoided in practice, and a more
sophisticated implementation can optimize them away.  Make's standard
`$(variable)` mechanism works this way, though without the ability to
define parameterized macros.

Tcl, instead, doesn’t rely on macro expansion for computational power;
its `proc` mechanism is not defined in terms of macro expansion
producing an enormous string, just the construction of the arguments
to a Tcl command.

______  
† “the program contains about 25 subroutines, totaling about 600
executable statements,” according to the Bell Labs Computing Science
Technical Report #2 about m6 in 01971.

Lexical syntax for :fq0zl
-------------------------

m6† used “warning characters” to delimit macro invocations, a feature
that is present in a certain sense in cpp and has been added again in
GNU m4.  In standard m4 we can write this and get 6:

    define(`mylen',`ifelse($1,,0,`eval(1+mylen(substr($1,1)))')')dnl
    mylen(kanawa)

But, in m6, where the quote characters were `<>` and the default
warning characters were `#:`, I think you would have written:

    #def,mysize,<#if,#seq,$1,:,0,1,<#add,1,#mysize,#substr,$1,1:::>:>:
    #mysize,kanawa:

(As mentioned above, replacing `:` with `;` yielded applicative-order
expansion, in which the macro’s output would not be expanded further.)

Here `#seq,$1,:` tests whether the first argument to mylen was
string-equal to the empty string, in which case the invocation of the
builtin `#if` macro returns 0; otherwise it invokes `#eval` to
recurse.  I think the inner `<>` are necessary to prevent the
recursion from being evaluated infinitely before invoking `#if`.

In GNU m4, if `changeword` is enabled, I think we can get a similar
effect like this, but I don’t have m4 compiled with that at the
moment to test:

    changequote(<,>)changeword(<#\([_a-zA-Z0-9]*\)>)
    #define(<mylen>,<#ifelse($1,,0,<#eval(1+#mylen(#substr($1,1)))>)>)#dnl
    #mylen(kanawa)

Overall this is all pretty nasty and unreadable to my eyes.  I'd
rather separate arguments with arbitrary amounts of whitespace and use
an explicit, nestable, and visually symmetrical circumfix syntax for
macro invocation.  Single ASCII characters only offer a few choices:

    <mylen kanawa>
    [mylen kanawa]
    (mylen kanawa)
    {mylen kanawa}
    ‘mylen kanawa’  # formerly ASCII, now sabotaged by aping MS-DOS

Of these, I like `<mylen kanawa>` best — it most strongly implies that
it's a placeholder — but that would run into a lot of trouble if you
started trying to macro-expand C programs that say things like
`#include <string.h>` and `for (size_t i=0; i<result->len; ++i)` all
over the place, not to mention PDF files with hex strings like
`<668531e8e73e8ee1503359167219ef43>`, and of course SGML, HTML, and
XML — unless you pass undefined macro invocations through unchanged.
But I want undefined macro invocations to crash.

So, to avoid these problems, with SGML, HTML, and XML, you must
precede the macro name with `:`, as in `<:mylen kanawa>`.

Just as in m4 and m6, there’s the problem of how to embed the argument
separator within an argument, which is more urgent when the separator
is whitespace.  You *could* use the same delimiters in such a case, or
something like `<:q this text is a single argument>`, but I think it’s
best to expropriate more delimiters in a way analogous to m6’s use of
`<>` — but *only in the context of macro arguments*.  And I think the
best delimiters to use here are braces `{}`, backslashing } and
backslash inside them if you need unbalanced braces.

And I think named arguments are pretty important.  So instead of

    define(`mylen',`ifelse($1,,0,`eval(1+mylen(substr($1,1)))')')

we might write

    <:def <:mylen s>
        <:ifelse %s {} 0 <:eval 1+<:mylen <:substr %s 1>>> >
    >

No quoting is needed here because we’re using normal-order
macro-expansion; the `<:mylen s>` and `<:ifelse ...>` calls are parsed
so we can see where they end, avoiding the need for extra `{}`, but
they aren’t macro-expanded until and unless they end up in a strict
context, such as a top-level output stream or the argument of `<:eval
...>`.  And `%s` expands to the parameter `s`, as in MS-DOS batch
files or in SGML parameter entities:

    <!ENTITY crap "#PCDATA | %font | %phrase | %special | %formctrl"> 

However, in :fq0zl, the substitution is only carried out on the text
of a macro definition, and only using the parameters that are
lexically within scope — it’s not done throughout the rest of the
file, as in an SGML DTD (the above SGML defines `&crap;` to expand to
all that crap, with `%font` and the like additionally expanded,
anywhere in any document ruled by this DTD).

As in SGML, you can optionally terminate the parameter name with a
`;`, which is useful for contexts that would otherwise be a problem:

    <:def <:mylen %s>
        <:ifelse %s; {} 0 <:eval 1+<:mylen <:substr %s; 1>>> >
    >

Consider, for example, this definition from the Hammer parsing library:

    #define HAMMER_FN_DECL_NOARG(rtype_t, name)             \
      rtype_t name(void);                                   \
      rtype_t name##__m(HAllocator* mm__)

We can define the equivalent in :fq0zl as follows:

    <:def <:hammer_fn_decl_noarg rtype_t name> {
        %rtype_t %name(void);
        %rtype_t %name;__m(HAllocator* mm_);
    }>

Without the disambiguating `;` we would have `%name__m`, which would
abort with an error, since there is no parameter in scope named
`name__m`.

Named parameters can have defaults, and you can pass parameters by
name.  So, for example, corresponding to this MediaWiki markup with
its named parameters:

    {{Infobox laboratory equipment
    |name         = Holter monitor
    |image        = HolterAFT1000.jpg
    |caption      = Holter monitor
    |inventor     = [[Norman Holter]] and Bill Glasscock at Holter Research Laboratory
    }}

we might have

    <:infobox-laboratory-equipment
        name = {Holter monitor}
        image = {HolterAFT1000.jpg}
        caption = {Holter monitor}
        inventor = {[[Norman Holter]] and Bill Glasscock at Holter Research Laboratory}
    >

The spaces around the `=` are optional, so parsing this from left to
right requires retconning `name` from being a parameter *value* “name”
to being a parameter *name*.  When we define the macro we can provide
it with default parameter values:

    <:def <:infobox-laboratory-equipment
                name caption inventor image={} model={}>
    ...>

It’s reasonable to question having two separate replacement
mechanisms, one for macros `<:s>` and the other for parameters `%s`.
You could of course provide parameters as locally-defined macros, but
my intuition is that bloating references to what are really just local
variables to a minimum of four characters is excessive and would make
:fq0zl clumsy to use.

Static function arguments
-------------------------

By defining a macro that expands to a `<:def ...>` we can do
imperative programming, but what about higher-order functional
programming?

In m4 we can pass function arguments by name:

    define(parenthesize,`($1)')dnl
    define(bracize,`{$1}')dnl
    define(hello,`$1(h)$1(e)$1(l)$1(l)$1(o)')dnl
    hello(`bracize')
    hello(`parenthesize')

The `hello` macro invokes the macro whose name is passed in as an
argument, so we get:

    {h}{e}{l}{l}{o}
    (h)(e)(l)(l)(o)

It took me about half an hour, and rereading much of the GNU m4
manual, to figure out that the reason this wasn’t working was that I
had forgotten to quote the argument to `hello`.  In :fq0zl we can do
precisely the same thing, but quoting is unnecessary:

    <:def <:parenthesize x> (%x)
    ><:def <:bracize x> {{%x}}
    ><:def <:hello f> <:%f h><:%f e><:%f l><:%f l><:%f o>
    ><:hello parenthesize>
    <:hello bracize>

If we change the definition in m4, we can pass in a curried function
instead; this produces the same output:

    define(wrap, `$1$3$2')dnl
    define(hello, `$1,h)$1,e)$1,l)$1,l)$1,o)')dnl
    hello(`wrap(`(',`)'')
    hello(`wrap({,}')

However, though this works in this case, it is clearly monstrous; it's
incompatible with the previous `hello` definition, and not only is the
definition of `hello` unreadable (you can’t even see the nesting
structure), it’s buggy when you pass it alphanumerics:

    define(wrap, `$1$3$2')dnl
    define(hello, `$1,h)$1,e)$1,l)$1,l)$1,o)')dnl
    hello(`wrap(_,_')

This produces the output

    _h_wrap(_,_,e)_l_wrap(_,_,l)_o_

Two of the five calls to the callback argument got cabbaged because
when the scanner got to them they’d undergone token pasting.  The
m6/:fq0zl design is somewhat safer here, but this is far from the only
such problem with macro expansion.

It’s not impossible to fix this bug within m4:

    define(wrap, `$1$3$2')dnl
    define(hello, `$1,h)`'$1,e)`'$1,l)`'$1,l)`'$1,o)')dnl
    hello(`wrap(_,_')

This produces the desired output:

    _h__e__l__l__o_

But the definition is, if possible, even uglier than before.

The straightforward equivalent definition in :fq0zl would use the same
definition of `:hello` as above:

    <:def <:wrap l r m> %l;%m;%r;
    ><:def <:hello f> <:%f h><:%f e><:%f l><:%f l><:%f o>
    ><:hello {wrap ( )}>
    <:hello {wrap \{ \}}>

But first we should explore the question of expansion semantics in
more detail.

Expansion semantics
-------------------

A big problem with make, sh, and m4 is that they tend to have subtle
bugs when handling “special characters”: make totally fails on
filenames with spaces.  sh by default re-splits the results of
$variable and `` `command` `` expansion to “help” you use shell
variables and command output as arrays of filenames instead of
individual filenames.  The m4 behavior I exploited above to pass in a
curried function as an argument is not only pretty unreadable in this
context, it’s also an abundant source of bugs.

Another problem with the m4 semantics is that they’re slow: the macro
output must be rescanned character by character in case the token
boundaries have moved.

We have to scan the macro arguments when we first encounter them in
order to figure out where they end.  The right solution is to store
the resulting list structure and treat *that* as primary, rather than
the character-by-character syntax.  This need not diminish the
abstraction power of the language.

Consider a macro invocation like this:

    <:foo %a b %c>

It is desirable that we can statically know that this invocation
invokes `foo` with three arguments, the second of which is the string
`b`, which is a positional parameter.  It is not desirable for `b` to
be the second or third argument depending on the value of `a`.

I’ll handwave over actually establishing semantics here for now,
though.

Lambda-lifting to construct data structures out of curried functions
--------------------------------------------------------------------

With this ability to construct and invoke curried functions, we can
define naturals, booleans, and Lisp-style lists in the λ-calculus
fashion, even though we don’t have anonymous functions.  To examine a
natural, we invoke it with two continuations, one to return if the
natural is zero, and another to invoke with the number's predecessor
if it is nonzero:

    <:def <:zero ifzero ifsucc> %ifzero>
    <:def <:succ n> {succ2 %n}>
    <:def <:succ2 n ifzero ifsucc> <:%ifsucc %n>>

Given this definition, we can define addition recursively: 0+y is just
y, and succ(n)+y is succ(n+y):

    <:def <:add x y> <:%x ifzero=%y ifsucc={add2 %y}>>
    <:def <:add2 y n> <:succ <:add %n %y>>>

Comparing a number to zero is fairly trivial:

    <:def <:eq0 x> <:%x ifzero=true ifsucc=eq01>>
    <:def <:eq01 _> false>

However, what are `true` and `false`?  We can define them in the same
way, as functions that invoke different continuations:

    <:def <:true iftrue iffalse> %iftrue>
    <:def <:false iftrue iffalse> %iffalse>

Now we can compare two naturals with the same recursive approach we
used for addition.  If the left argument is zero, then we get the
result by checking to see if the right argument is zero:

    <:def <:eq x y> <:%x ifzero=<:eq0 %y> ifsucc={eq2 %y}>>

Otherwise,

    <:def <:eq2 y x1> <:%y ifzero=false ifsucc={eq %x1}>>

    <:def <:nil ifnil ifpair> %ifnil>
    <:def <:pair car cdr ifnil ifpair> <:%ifpair %car %cdr>>
    <:def <:mapcar f list> <:%list nil {mapcar2 %f}>
    <:def <:mapcar2 f car cdr> <:pair <:%f %car> <:mapcar %f %cdr>>>
    <:def <:append xs ys> <:%xs %ys {append2 %ys}>>
    <:def <:append2 ys car cdr> <:pair %car <:append %cdr %ys>>>

