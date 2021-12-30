Let’s look at a binary search.

The binary-search problem
-------------------------

We have some array or slice A such that some predicate P is true for
some possibly empty prefix of A, and then false for all following
elements, and we want to define a procedure bsearch(A, P) that returns
the first index for which it is false — which may be an index off the
end of A, if the prefix is the whole thing.

The solution
------------

If A is empty, then the answer is simple: it’s 0.  In other cases we
can recurse.

We choose an element from within A, which we can do because we know
it’s nonempty.  We can choose M = #A // 2, rounding down; this is
always within the bounds of A.  We test P(A[M]).  If it’s false, we
know our return value is at most M, so we can recurse on an interval
that excludes it, returning bsearch(A[:M], P).  This is guaranteed to
make progress toward an empty array because #A // 2 < #A for #A > 0.

On the other hand, if it’s true, we know the return value is at least
M+1, so we can recurse, returning M+1 + bsearch(A[M+1:], P).  This
also reduces the interval, possibly to size 0, but never past 0.

In Python
---------

    def bsearch(a, p):
        if not a: return 0
        m = len(a) // 2
        if p(a[m]):
            return m+1 + bsearch(a[m+1:], p)
        else:
            return bsearch(a[:m], p)

Now, while this does work, it suffers from an efficiency problem in
Python: the recursive calls copy the relevant interval, which makes it
take linear time instead of logarithmic time.  We can solve this by
representing the slice as a triple (a, i, j) to mean a[i:j]:

    def bsearch(a, p):
        return bsearch2(a, p, 0, len(a))

    def bsearch2(a, p, i, j):
        if i == j: return i
        m = i + (j-i) // 2
        if p(a[m]):
            return bsearch2(a, p, m+1, j)
        else:
            return bsearch2(a, p, i, m)

This allows us to define the `bisect_left` and `bisect_right`
functions from Python’s bisect module:

    bisect_left = lambda a, x: bsearch(a, lambda n: n < x)
    bisect_right = lambda a, x: bsearch(a, lambda n: n <= x)

Which brings me to the [puzzle I was originally trying to solve][0],
which took me 3 minutes with those two functions:

> Given a sorted array arr[] and a number x, write a function that
> counts the occurrences of x in arr[]. (O(Log(N)))

[0]: https://github.com/twowaits/SDE-Interview-Questions/tree/master/Uber

    def count(arr, x):
        return bisect_right(arr, x) - bisect_left(arr, x)

Humblingly, though, without using the module, it took me another 30 to
get the binary-search code above right, because I was writing it at
the REPL instead of deriving it in the way I derived it above.

Term-rewriting
--------------

Here’s a description of the above `bsearch` procedure in terms of
rewrite rules with implicit equality testing:

    bsearch(A, P) = bsearch'(A, P, 0, #A)
    bsearch'(_, _, x, x) = x
    bsearch'(a, p, i, j) = bsearch''(a, p, i, j, i + (j-i) // 2)
    bsearch''(a, p, i, j, m) = bsearch'''(a, p, i, j, p(a[m]))
    bsearch'''(a, p, i, j, True) = bsearch'(a, p, m+1, j)
    bsearch'''(a, p, i, j, False) = bsearch'(a, p, i, m)

This is somewhat verbose, and it might contain errors (I haven’t
tested it) but I think it’s straightforward to see how to compile the
Python version to a representation like this.

Rigor
-----

What would it mean to make rigorous the above argument about
correctness?

First, we assume (have as a precondition) that the array is “sorted”,
which in this case means that if we step through its elements, if at
some point P becomes false, it stays false for all subsequent
elements.  I think I can write this as

> ∀*i* ∈ [0, #A): ∀*j* ∈ [i, #A): ¬P(A*ⱼ*) ∨ P(A*ᵢ*)

That is, if A*ᵢ* makes P false, then any A*ⱼ* after it within the
array must also make P false.  (I’m implicitly restricting *i* and *j*
to be integers.)

What we want to prove is that `bsearch` produces the right return
value: some value such that all elements before it make P true and all
other elements make P false; we also want it to be either a valid
array index or one past the end.  That is:

> bsearch(A, P) ∈ [0, #A]  
> ∀*i* ∈ [0, bsearch(A, P)): P(A*ᵢ*)  
> ∀*i* ∈ [bsearch(A, P), #A): ¬P(A*ᵢ*)

This would probably involve first proving that such a value exists,
using induction and the precondition above.  Such a value is
necessarily unique, which might or might not be necessary to prove.

We would also need to prove that bsearch terminates, which can be done
with induction on *j* - *i*: that difference is always nonnegative,
terminating the function when it reaches 0, and recursive calls always
strictly diminish it.  We also need to show that it doesn’t exceed the
array bounds of A:

> *i* ∈ [0, #A) ∧ *j* ∈ [0, #A] ⇒ *i* + (*j*-*i*) // 2 ∈ [0, #A)
