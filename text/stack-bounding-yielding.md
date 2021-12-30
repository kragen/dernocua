C is simple and efficient, doesn’t require GC, and potentially allows
you to handle failures, but it can take a lot of code to get things
done, and you tend to bake in a lot of inflexibility.  Things like
Smalltalk are less efficient and can run out of heap, but require less
code to get stuff done, and allow more flexibility.  I’ve been
thinking about how to get a Pareto improvement over C: something that
allows you to handle failures, but still supports failure-free GC-less
computing, and is simpler.  Seven key features I’ve identified are
coercions, dynamic dispatch, call-by-name, block arguments, pattern
matching on sum types, uninitialized data, and list comprehensions.

C tries to help you by implicitly converting between data types, but
the rules for this are extremely complex and bug-prone.  I think it’s
better to require explicit coercions but, as in Golang, make constants
sort of typeless.  This makes the language safer and much simpler in
exchange for, generally, a tiny increment of brevity.

C++ can do dynamic dispatch with virtual functions, but the design is
all wrong.  The Golang design for virtual functions by indirection
through an interface is the correct design; whether a method call is
statically dispatched or dynamically dispatched is a property of the
callsite, not the function being called.  This is achieved by
(implicitly, in Golang) creating an “interface object” containing a
pointer to the object and the relevant function pointers.  In the case
where you’re creating an interface object for a concrete type, or for
a more restricted facet of a broader interface, this can be done
statically.  Golang also, using dynamic checks, implements a
broadening type conversion; I think this is basically just a kludge to
fake dynamic typing, and can be dispensed with.

The Golang interface construct doesn’t create a subtyping relation.
The interface is a separate object from the concrete object that it
provides access to; they are separate types, although Golang does
unfortunately have implicit coercions.  The absence of subtyping
relations dramatically simplifies the task of type inference.

Call-by-name was a much-maligned feature of the original Algol 60,
omitted from both C and Pascal.  It allowed you to write a function
like the following:

    double sum(double &fi, int &mut i, int start, int stop) {
      double total = 0.0;
      i = start;
      while (i != stop) { total += fi; i++; }
      return total;
    }

This could be invoked, for example, as `sum(&a[i], &mut i, 0, 10)` or
as `sum(&i**2, &mut i, -5, 6)`, assuming `**` is exponentiation.  As
with C preprocessor macros, each evaluation of the name of a
call-by-name parameter would re-evaluate the expression that had been
passed as an argument, and this even worked in lvalue context, so `i =
start;` here would change the value *in the caller*.  In these cases,
changing `i` also changed `fi`.

This is clearly somewhat bug-prone (though I think some kind of
marking at the callsite like the `&` in the above might help to
clarify what’s going on) and its implementation is slow (it involves
creating one or more closures per parameter; they are not
garbage-collected, but invoking them involves all the usual
call/return overhead); but it is not without its merits.  One is that,
unlike C pointer parameters, it can be passed down the stack, but
cannot be stored in a data structure or returned up the stack, so they
do not pose a risk of pointer lifetime bugs.  The other, in
combination with CLU iterators, is subtler and more powerful.

The block arguments I have in mind are similar to CLU iterators; they
are a restricted form of the block arguments you see in Smalltalk or
Ruby.  You can use them as iterators:

    each_line(&mut line, somefile) { print(line); }

Or as resource managers:

    with_file(&mut f, filename, "r") { results = read(f, fstat(f).st_size); }

Or as conditionals:

    button("Invert") { invert(&mut image); }

The block is passed in to the function being invoked as a closure,
just like a name parameter.  That function can invoke the block (in
CLU or Ruby, `yield`) zero or more times, including with arguments.
But the block does not have its own stack frame; instead, it stores
all its state in the subroutine it’s lexically nested inside of.  And
the subroutine they’re passed to cannot return them or save them in a
data structure.

Together with call-by-name, this facility allows you to implement
control structures as library functions:

    forto(&mut x, 0, 10) { printf("%d² = %d\n", x, x**2); }
    while (&x < 10) { x++; }

You *could* implement `while` something like this, at least as a
prototype, assuming proper tail-call elimination is at play:

    void while(&b) {
        if (!b) return;
        yield;
        while(&b) { yield; }
    }
        
Syntactically you probably need facilities to handle multiple block
arguments, though; in particular you want to be able to do things like
map and filter as such iterators, which take one block to describe the
mapping or filtering and a second block to send the result to.

Null pointers are the bane of C, and ML-family languages avoid them by
instantiating their data structures fully populated and by using
variant tags.  If you define a string-search-result type in OCaml:

    type loc = Found of int | Not_found

then if you have a value of type `loc` you cannot get any data out of
it without a pattern-match:

    match p with Found x -> x * 2 | Not_found -> 1

The variable `x` is only in scope in the part of the conditional where
it has matched something.  This eliminates the need for NULL.

(I’m not sure how this fits into C’s nested-data model, but I don’t
think there’s a clash.)

Uninitialized data in C is almost invariably a result of the
traditional Algol block structure with declarations at the top of the
block, followed by statements.  C at least allows you to initialize
things in the declarations.  But there’s very little reason, even in
modern C, to declare a variable before giving it a value; you can
delay declaring it until you have the value ready.  This eliminates
another source of null data.

In Python, list comprehensions are just a ridiculously useful way to
write code.  The translation to imperative code is straightforward, so
why should we do it by hand?  (This might involve some tricky
questions about allocation.)

The thing I was really trying to figure out here, though, is how to
put a static stack size bound on code that uses these features, in
particular block arguments and dynamic dispatch.  Dynamic dispatch
with method names is potentially less troublesome than arbitrary
function pointers, since a function pointer could take you to any
function whose address has been taken, while method dispatch can only
take you to one of the 6 functions named toTuple or whatever.  Block
arguments are a little tricky because any calls from within the block
get stacked on top of the activation record of the “iterator” that’s
calling it --- but not at the same time as the iterator’s own callees.

There are two different reasons for wanting a static stack size bound.
One is to statically guarantee that the program won’t crash.  Another
is to insert a minimal number of stack overflow checks which, if they
fail, do something like invoke the Cheney-on-the-MTA trampoline, or
allocate a new segment to expand the stack into.
