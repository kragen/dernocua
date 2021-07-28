What if we wanted a small dynamically-typed imperative language with
the flexibility of Lisp that admitted reasonably efficient
implementations, but not based on conses?  Like, something with an
implementation about the size of the ur-Lisp?  The power of
first-class hash tables (“dictionaries” or “tables” or “associative
arrays”) has been convincingly shown by JS, Perl5, PHP, Python, and
Lua, and they certainly produce much more readable code than Lisp.

Lua has shown that freeform syntax without statement terminators can
be reasonably usable (though it mostly prohibits you from using
juxtaposition as an operator, as ML does for function composition, and
it limits your flexibility in what expressions can start with), and
Python has shown that indentation-based syntax can be too, at least if
you don’t demand too much from anonymous lambdas.

Statement-level structure
-------------------------

We can start with variables.  Imperative languages probably need
variable updates, but most variables should be declared and
initialized and then not mutated, so it makes sense to privilege the
declaration form over mutation with brevity; and ideally the thing
being declared should be in the left margin, permitting easy scanning,
rather than preceded by a keyword or punctuation:

    decl ::= name "=" expr
    assi ::= "set" lvalue "=" expr

Multiple assignment (and multiple declaration) is convenient syntactic
sugar at times, especially with Lua-style or Perl-style multiple
return values, but it doesn’t add any fundamental power if we have
dicts.  And I think non-multiple assignment tends to push code toward
being “boring” rather than “clever”, which is worthwhile here.

So an lvalue is just a dictionary lookup chain from a name.  A
pathname, you might say.  I think it’s really important to be able to
say literally `p.x = 3` rather than the much noisier options like,
say, `p{x} = 3` or `p:x = 3` or `p.:x = 3` or `p['x'] = 3` or `x(p) =
3`, or a more implicit option like `p x = 3`.  But it’s also important
to be able to index with expressions rather than literal symbols like
`:x`.  One approach to this would be to distinguish literal symbols by
case: perhaps `X` would be a literal symbol and `x` a variable, so
`p.X = 3` would index by the literal symbol, but `p.x = 3` would use
whatever the current value of `x` was.  But I think maybe a better
approach is to use a parenthesized expression, so `p.x = 3` assigns to
the property `x`, while `p.(x) = 3` reads the variable `x` and assigns
to the property it names.  Thus `.()` takes the place of `[]` in most
conventional languages.

    lvalue ::= name ("." arc)*
    arc ::= name | "(" expr ")"

Now we need conditionals, functions, and (if this is really
imperative) iteration.  My Lisp sense tells me that conditionals and
iteration should be expressions rather than statements; my Lua and
Python sense tells me that this might make parsing errors unusable
(Lua's parsing can reliably distinguish a function call from a
trailing expression followed by a new statement beginning wih `(` or
`[` because Lua statements can’t begin with those because Lua doesn’t
have expression statements) but in any case they should use
conventional words; my C sense tells me that I should use curly
braces.  So, conditionals:

    if ::= "if" expr "{" expr+ "}"
            ("elif" expr "{" expr+ "}")*
            ("else" expr "{" expr+ "}")?

Since we don’t have multiple value returns, the value returned by the
conditional is the value of the last expression in the chosen branch.

Function calls are similarly syntactically simple, although they
involve the expression-juxtaposition danger that shows up in JS, since
presumably we will allow expression parenthesization:

    call ::= expr "(" (expr ("," expr)*)? ","? ")"

The arrow syntax from current JS is the lowest-hassle way to define an
anonymous function.  Semantics are that it is a closure with arguments
are passed by value.

    lambda ::= "(" (name ("," name)*)? ","? ")" "=>" "{" expr* "}"

Tentatively I’m using Sam Atman’s `->` syntax from Lun for function
return values:

    return ::= "->" expr

This allows us to write `add1 = (x) => { -> x + 1 }`, which is
lightweight enough to not wish for a sugared `function add1(x) { -> x
+ 1 }` form.

Minimally iteration needs a while loop, but most loops are better
expressed as iteration over a sequence:

    while ::= "while" expr "{" expr* "}"
    for ::= "for" name "in" expr "{" expr* "}"

List comprehensions in Python are extremely useful, so these ought to
return sequences, but what should they contain?  The conventional
answer would be the last expression invoked in the loop body, and that
seems adequate.

The Lisp approach to sequences is to use cons lists, in which case the
“for” structure would desugar somewhat as follows:

    for x in y { z }
    
    yi = y
    while !yi.null {
        x = yi.car
        z
        set yi = yi.cdr
    }

A different approach would use arrays and perhaps slices:

    yi = 0
    while yi < y.len {
        x = y.at(yi)
        z
        set yi = yi + 1
    }

The remaining fundamental means of combination is explicit aggregate
variable construction.  Unlike in JS, it’s syntactically unambiguous
to use `{}` here because all our previous uses of `{` were
semantically obligatory and thus cannot occur where an expression is
expected.

    dict ::= "{" (arc ":" expr ("," arc ":" expr)* ","?)? "}"
    list ::= "[" (expr ("," expr)* ","?)? "]"

So, the basic expression language then is

    expr ::= decl | assi | if | call | lambda | return | while | for
           | dict | list | infix

Infix expressions
-----------------

Pop infix syntax is fairly straightforward; basic arithmetic is:

    atom ::= "(" expr ")" | string | int | real | symb | lvalue
    unary ::= atom | "-" atom | "!" atom
    expo ::= atom ("**" exp)*
    term ::= expo (("/" | "//" | "*" | "%") expo)*
    terms ::= term (("+" | "-" | "..") term)*

Here `..` is Lua’s string concatenation operator.  I think it’s safe
to relegate bitwise arithmetic to named functions.

There’s an unfortunate precedence ordering thing in C where booleans
have precedence close to the bitwise operators, tighter than
comparisons, rather than the more desirable looser-than-comparisons
thing.  Another problem is that chained comparisons (`x == y == z`)
have unintuitive results in most languages.  A simple solution is to
restrict the syntactic composability of these elements, requiring the
use of parentheses to disambiguate:

    infix ::= terms (( "==" | "!=" | "<"  | ">"
                     | "<=" | ">=" | "&&" | "||") terms)?

A slightly better solution is to provide a separate case for the
associative short-circuiting Boolean operators that does allow them to
be individually chained:

    infix ::= terms (( "==" | "!=" | "<"  | ">" | "<=" | ">=") terms)?
            | terms ("&&" terms)+
            | terms ("||" terms)+

Tokens
------

Strings, numbers, names, and symbols are simple enough.  The {} around
these productions indicate that whitespace should not be skipped
within them.

    string ::= {"\"" ([^\\"] | "\" byte)* "\""}
    int ::= {"-"? [0-9]+}
    real ::= {"-"? ("." [0-9]+ | [0-9]+ "." [0-9]*)}
    name ::= {[A-Za-z_$] [^] \t\r\n(){}[.=!<>+-*/%&|#]*}
    symb ::= {":" name}

Whitespace itself, implicitly ignored elsewhere, includes comments to
end of line, which are marked with Unix `#` rather than Ada/Lua `--`.

    whitespace ::= ([ \t\r\n] | "#" [^\r\n]* (\r\n | \n | \r))*

Modules and scoping
-------------------

There’s no need to put an import statement into the program grammar;
the “.” syntax will work perfectly well for reaching into modules if
there’s an ordinary function that imports a module and returns it,
like JS’s `require`.  We can simply declare, Python-like, that global
variables in a file are the properties of the corresponding module.

So then we simply have

    module ::= expr*

I’m convinced that lexical scoping is adequate and the right default.

The whole Smolsay grammar (Smolbutswol?)
----------------------------------------

    module ::= expr*
    expr ::= decl | assi | if | call | lambda | return | while | for
           | dict | list | infix
    decl ::= name "=" expr
    assi ::= "set" lvalue "=" expr
    lvalue ::= name ("." arc)*
    arc ::= name | "(" expr ")"
    if ::= "if" expr "{" expr+ "}"
            ("elif" expr "{" expr+ "}")*
            ("else" expr "{" expr+ "}")?
    call ::= expr "(" (expr ("," expr)*)? ","? ")"
    lambda ::= "(" (name ("," name)*)? ","? ")" "=>" "{" expr* "}"
    return ::= "->" expr
    while ::= "while" expr "{" expr* "}"
    for ::= "for" name "in" expr "{" expr* "}"
    dict ::= "{" (arc ":" expr ("," arc ":" expr)* ","?)? "}"
    list ::= "[" (expr ("," expr)* ","?)? "]"
    atom ::= "(" expr ")" | string | int | real | symb | lvalue
    unary ::= atom | "-" atom | "!" atom
    expo ::= atom ("**" exp)*
    term ::= expo (("/" | "//" | "*" | "%") expo)*
    terms ::= term (("+" | "-" | "..") term)*
    infix ::= terms (( "==" | "!=" | "<"  | ">" | "<=" | ">=") terms)?
            | terms ("&&" terms)+
            | terms ("||" terms)+
    string ::= {"\"" ([^\\"] | "\" byte)* "\""}
    int ::= {"-"? [0-9]+}
    real ::= {"-"? ("." [0-9]+ | [0-9]+ "." [0-9]*)}
    name ::= {[A-Za-z_$] [^] \t\r\n(){}[.=!<>+-*/%&|#]*}
    symb ::= {":" name}
    whitespace ::= {([ \t\r\n] | "#" [^\r\n]* (\r\n | \n | \r))*}

This still contains the frustrating ambiguity where an expression
immediately followed by `(` is a call, but expressions can also begin
with `(`.  The alternative of replacing `sin(x)` with something like
`sin:(x)` or `sin[x]` is unappealing.  It’s possible to disambiguate
in these cases by assigning to a dummy variable: `_ = (foo)`.
Requiring no whitespace or at least no line breaks before the paren
would pretty much solve the problem, but it sort of requires that the
parsing of `expr` not consume following whitespace.

Because conditional blocks are always wrapped in braces, the if-else
ambiguity doesn’t occur.

Resulting design at other levels of abstraction
-----------------------------------------------

This suggests the following set of 23 basic “bytecode” operations:
getlocal, setlocal, get, put; jumpfalse, jump, call, return; makedict,
makelist; constant; negative, not, exponent, truediv, floordiv, mul,
mod, add, sub, cat, eq, lt.

Of course, the proper order of implementation would be something like:

1. Implement bytecode interpreter with textual bytecode syntax and
   program in it a bit.
2. Implement S-expression syntax, compiling to the bytecode, and
   program in it a bit.
3. Implement debugger stuff, maybe native-code compiler, etc.
4. Implement pop infix syntax above.

The S-expression syntax can get by with six special forms:

- `(lambda args body...)`
- `(return x)`
- `(cond xy...)`
- `(while p body...)`
- `(for x y body...)`
- `(setlocal n v)`

The other bytecode operations are either implicit (getlocal, call,
constant), folded into the three control structures, or ordinary
functions (get, put, makedict, makelist, negative, not, exponent,
truediv, floordiv, mul, mod, add, sub, cat, eq, lt), along with the
other ordinary functions (require, print, length, etc.).

From the point of view of the pure ur-Lisp, if we strip away the
imperative and arithmetic frippery, we’re replacing ATOM, CONS, CAR,
and CDR with get, put, makedict, and makelist, and makelist is
unnecessary.

Of course, other alternatives to S-expressions exist.  RPN, for
example (which is on my mind lately because I’ve been hacking on PDF
and PostScript) or Prolog notation, or REBOL-style non-R PN, or
APL-style precedence-free infix.

Alternative debugging-first semantics
-------------------------------------

What if functions returned their internal namespaces instead of an
explicit return value?  You wouldn’t need a return statement or a dict
type, and in most cases debugging would get a lot easier.

A hairier approach to this would be to associate the internal
namespace with the value thus produced, and provide a function
`why(x)` that returns the activation record of the function call that
returned `x`.  This implies that returning a value sort of makes a
copy of it to potentially associate it with a different activation
record, but accessing it as a property does not; we want `why(p.x)` to
work.  Other internal operations can be treated as functions.

That is, a variable/property has a *value* aspect, the usual
reference; but it also has a *why* aspect, which is the activation
record of some function, accessible via the `why` built-in function.
Both of these aspects are returned when a function returns and stored
in the variable/property.  It might as well also have other aspects
useful for debugging, like `prev`, which gives you the variable as it
was before being overwritten, and `where`, which tells you what
statement did the overwriting (or initializing), and in what
activation record.  An activation record might also have a `caller`;
often `caller(why(v))` will be `where(v).call`.  You might also want
to know the control-flow context of the `where`, with something like
`where(v).context.condition` to find out why the if or while statement
was continuing.

If all this data is always available, no activation record and indeed
no value ever becomes garbage, so only very short programs can run
fast.  (We’re in an imperative world here, so we can’t just recompute
the activation record on demand like Bicicleta.)  We could maybe store
it in some kind of a ring buffer, like Cheney on the MTA.

The no-return-statement variation doesn’t have this problem; `sin(x)`
is a whole activation record, but `sin(x).val` is just the return
value, so you only retain activation records when you want them.  In
Bicicleta I had syntactic sugar for this: `sin{x}` and `sin(x)`
respectively, the second of which extracted a variable annoyingly
called `()`.

Efficient implementation
------------------------

A standard pointer-bumping generational GC should work pretty well
here, though maybe not quite as well as in a strictly immutable
language.  If we use a standard sort of stack structure rather than
heap-allocating activation records, we need to scan the stack for
roots on nursery collections anyway, so we don’t need a write barrier
for writes to the stack, which are statically apparent, nor for
property initializations.  Only property mutations and module-variable
mutations need a write barrier.

To statically resolve callees, we’d like to be able to treat the
module variables in which “global” functions live as constant.  Static
analysis can’t show that module variables are never mutated, but we
could maybe trigger a recompile after mutating such a cell.  This
makes the property-mutation write barrier more expensive, and it might
require on-stack replacement (with a recompilation of the same code,
not a compilation of the new function), which is easier if our
stack-frame structures aren’t too optimized.  Debugging is also
easier if those structures are ordinary dictionaries.

Statically compiling local-variable accesses into indexing off a stack
frame that is also an ordinary dictionary would be easier if we could
ensure that dictionaries never changed shape, as local-variable
vectors normally don’t.  If you can delete values from a dictionary,
which is probably important, there’s the question of what happens when
you try to read the deleted value.  If getting nil as in Lua is an
acceptable answer, then you can ensure that dictionaries never change
shape.  But, if you want that to raise an exception, you either need
to check for existence every time you read a local variable, as Python
does, or you need to recompile the function to crash (and potentially
do on-stack replacement) when you delete the variable from its stack
frame.

Or you could just raise an error when you try to delete a variable
from a stack frame, which is probably the most sensible thing to do
--- changing their values is reasonable but deleting them is not.
That would require that the deletion operation do a special check for
such protection --- which is fine, because key deletion is so rare
that it doesn’t need to be especially fast.

The space-efficient way to make such early-bound accesses fast would
be to put dictionaries’ keys in one vector (or set of vectors, but
probably just one in this case, though maybe it would be worthwhile to
use the set-of-vectors approach to handle lexical scopes) and the
corresponding values in another one, which would be in the stack
frame.  For large key sets, a canary hash table for the key set would
enable fast access by key.  Newly added keys would go into a new
key vector.

This kind of design, where the stack frame structure is a regular
first-class data value that happens to be efficient enough to use for
local variables, seems like it might be an appealing alternative to
dynamic deoptimization.

(It might be useful to expose the inheriting-dictionary approach used
to handle nested scopes as first-class in the language itself, so that
you could, for example, put a class’s methods in one dictionary and
then create objects that inherit from it, or efficiently override a
few things in a large dictionary.)

This structure would also make the common makedict case, where the set
of keys is constant, fast and space-efficient.  And it might ease the
task of “hidden class” compilers.

Initialization can be statically guaranteed for all local variables if
variable declarations are block-local rather than function-local.

What about dynamically dispatched methods?
------------------------------------------

We can use closures as methods, of course, or we could supply
syntactic sugar like Lua’s `obj:method(args)`, which translates to
`obj.method(obj, args)`, although both `:` and `->` are already taken
in the syntax above.  `obj.method[args]`, `obj << method(args)`, `obj
<- method(args)`, `^method(obj, args)`, `@method(obj, args), and
`method = generic(:method) ... method(obj, args)` come to mind.  But
we’d like to be able to do this in a way that can be compiled
efficiently in a dynamically-typed system, which means we need some
way to quickly verify that the method to invoke is the same as last
time.  So we’d like the memory representation of `obj` to be possessed
of some easily readable register-sized value that can be efficiently
compared against the one for the method we think we ought to call.

One approach is to attack the problem entirely at the desugared level:
if we’re first fetching a property from the object, then invoking the
resulting closure, we could try to speed up the property fetch, and/or
we could compare the resulting property against the last closure we
invoked at this callsite (or a PIC of them).  This would be fine for a
tracing JIT but it seems unlikely to provide much benefit for a
simpler compiler.  If your objects are made out of a delegation chain
of dictionaries as described earlier, you can store the chain in a
counted vector in the dictionary object, and you can copy the chain
item in which you found the method to your inline cache, along with a
number that says what index it was at.  Then you can compare the
cache-key dictionary pointer to the dictionary pointer in the
delegation chain at the appropriate position, if it’s within bounds.
But then you need to worry that a later (more superficial) dictionary
in the chain might be hiding the method, so you can also maybe store
an index in the object that tells which is the last dictionary in the
chain none of whose keys are hidden, and use *that* instead of the
dictionary where you actually found the keys.  Hopefully this will
allow you to have cache hits for “objects” in the same “class”, since
instance data doesn’t normally hide methods.

Another approach is the Perl/Python `bless` approach, where the
instance data of an object is in one dictionary, and its methods are
in another, providing a totally separate namespace and enabling you to
use dicts with much greater security than in JS.  Lua does this with
`setmetatable`: the things that tell Lua how to index a table or
convert to strings are stored in a separate table, the metatable,
which may be shared among many objects.  So maybe `obj <<
method(args)` should desugar to what we’d write in Lua as
`getmetatable(obj).method(obj, args)`.

This is somewhat less conceptually simple (a dict isn’t just a set of
key-value pairs; instead it has become merely the puppet of a shadowy
class) but much easier to compile efficiently and much safer.  You
don’t need to grovel over a delegation chain to figure out what the
best cache key is; it’s just the class, which doesn’t need to support
inheritance.  It would be better to put regular user methods in the
class too, unlike Lua, which is at this intermediate point where
methods like __index and __tostring are in the metatable as in Perl
and Ruby, but you’re expected to put ordinary user methods in the same
namespace as your instance variables or dictionary items, as in JS.

I think this is slightly less simple than the current Lua approach,
since in Lua, you don't need to add a metatable to a table in order to
put methods on it.  but the metatables are already in the picture and
it's already common to `return setmetatable(...)` in object
constructors, and in those cases it seems like it would just simplify
user code, as well as having the above advantages.

One of the things I really enjoyed about LuaJIT's FFI (by contrast to
Python's cffi) is that I can just add Lua methods to C structs with
`ffi.metatype(ctype, { __index = { methods } })` instead of having to
do the whole song and dance of the membrane pattern where I wrap each
C type in a separate porcelain object, everywhere it's returned
through the looking glass (and possibly going to some effort to keep
that relationship 1:1).  But the standard Lua way of defining ordinary
methods means that if I want to do the same thing for an ordinary
table that's used as a dictionary, I do have to create a separate
porcelain façade to hold its methods.

Some notes on COLA-like object models are in file `faygoo.md`.

