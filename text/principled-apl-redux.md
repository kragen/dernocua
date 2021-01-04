Writing [rpneact](http://canonical.org/~kragen/sw/dev3/rpneact.py) I
realized that there are some straightforward ways to extend such a
system toward Bicicleta and the principled variant of APL I was
thinking about, as well as to do performance work.

One is that inheritance is relatively straightforward:

    class Var(namedtuple('Var', ('name',)), Expr):
        def eval(self, vars):
            return vars[self.name].eval(vars)

If the second `vars` were a different object, we’d have the equivalent
of invoking an inherited method — any vars referred to by the formula
would come from the different object.  (And this is exactly how
inheritance works in Bicicleta and in the ς-calculus it’s based on.)
And of course in Python such inheritance is straightforward to
implement in the `vars` object by having its `__getattr__` delegate to
one or more different mappings.

There’s code in rpneact for the solver that evaluates a loss formula
at various points along a design variable; it works as follows:

    var = design_var.name
    original = vars[var]
    ...

    try:
        ...
                vars[var] = Const(b)
                b_obj = objective.eval(vars)
        ...
    finally:
        vars[var] = original

This could be done in a purely functional way instead by the
inheritance mechanism described above.

Let’s call these “vars” namespace objects that might inherit from one
another “worlds”.

Bitmask caching
---------------

For caching property values in such a system, you’d like to carry over
the cached value of a property to any child worlds that hadn’t
overridden any other property used during its computation.  Moreover,
if that value didn’t get cached in the parent but did get computed in
the child entirely from properties unchanged from the parent, you’d
like to propagate those values back to the parent, so that other
children can use them.

I’m not sure what’s an actually scalable way to implement this, but an
approach that’s reasonable up to a certain extent, with single
inheritance, is to maintain a bitmask of overridden fields in each
world.  Each field is assigned an index, starting from the number of
fields in the base class.  Each cached result is stored at that index
in a cached result vector associated with each world; each field
definition is stored at that index in a definition vector; and in the
bitmask of overridden fields for an world, the bit is set if the world
has its own private definition of a field, rather than using the
parent world’s.  And each cached result is associated with a bitmask
of all the fields consulted during its computation.

(For the moment I’m going to ignore dependencies on things outside of
the world itself, which were common in Bicicleta but sort of
impossible in the principled-APL approach.)

These bitmasks can be 64 bits for worlds with 64 fields or less, so we
can operate bitwise on them in a single instruction on a 64-bit CPU,
or 128 bits for worlds with 128 fields or less.  In the limit of a
large number of fields, of course, such explicit sets will tend to
incur a large space and time cost.

To know whether the parent world’s value of a variable can be safely
reused, we can AND the current world’s overridden-field bitmask with
the dependency bitmask for the parent world’s variable; if the
intersection is null, we can just reuse the parent’s value (and
perhaps also cache it locally).  Similarly, if we compute a field
value locally, we also compute its dependency bitmask, so we can check
in the same way to see whether it involved any locally overridden
values (although you could imagine that maybe it would be more
efficient to just set a flag during the computation, you have to
compute the dependency bitmask anyway) and then do the same check.
This lets you see how far up the inheritance hierarchy you can push
the cached value.

When a cached field is consulted during the computation of a field
value, we must OR its dependency bitmask into the dependency bitmask
of the computation, as well as set its bit.

Compilation and duplicate suppression
-------------------------------------

In a system compiled without runtime reflection, all of this bitmap
consultation can happen at compile time; only the consultation to see
if a field is already computed, and if so where, and what its value
is, must be deferred to runtime.  This in some sense involves
compiling a separate version of each world for each callsite,
depending on the particular overrides provided at that callsite, but
in many cases these worlds will use precisely the same code and can
thus be merged, as with C++ templates.  (And runtime reflection can be
supported in such a system by invoking the compiler at runtime.)

If an override method doesn’t use any other fields of the object it’s
being stuck onto, it could be implemented as a simple delegation to a
thunk.  Then all the worlds that differ only by the contents of that
thunk can be merged.  For example, in Bicicleta:

    prog.if(foo, then={all kinds of stuff}, else={more stuff})

can be merged with all the other invocations of `prog.if` that
override only `arg0`, `then`, and `else`.

### Field order ###

The fields within a world can be topologically sorted to emit a single
sequence of code that computes all of them in dependency order.  In
cases where no cached results are possible, for example when a program
starts, if there’s no risk to termination behavior, we can run all the
fields peremptorily in sequence, one after the other.  In other cases,
it may be sensible to do a slightly modified version of the same
thing: concatenate the code, put a conditional jump past the
computation of each field, based on, for example, a bitmap of fields
whose computation is desired: the abjunction of the dependencies of a
desired-fields bitmap and an already-computed-fields bitmap.  In many
cases, we can jump directly to the first not-yet-computed field, and
run straight-line code from there, perhaps even without such
conditional skips.

Inlining the computations of other worlds’ fields may be worthwhile,
particularly when no references to those other worlds themselves
escape from the computation.  The `if` case above is paradigmatic: no
reference to `if` world survives, just its output.

General inlining in a system as late-bound as the original Bicicleta
design would require type specialization using hidden classes.  Maybe
a “Triciclo” design could omit the ability to override standard
operators like arithetic, but you could probably get to better
performance than CPython or similar systems by the Ur-Scheme approach
of inlining the implementation of native operators (integer addition,
etc.) with a conditional jump to an exception handler for cases where
an operator is overridden.  But this is to some extent orthogonal to
the question of the caching strategy!
