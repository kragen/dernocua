What if we use the Fortran memory model in Forth?  With bounds
checking?  No more free access to memory.  Like, a segmented kind of
thing.

Create a scalar variable x with value 3:

    3 value x

Set it to 4:

    4 to x

Create an array a containing the values 0, 1, 4, 9, 16:

    create a 0 , 1 , 4 , 9 , 16 ,

Load 9 from its position 3, with bounds checking:

    a 3 @

Store -4 in its position 2, overwriting 4:

    -4 a 2 !

Define a word “cons” that allocates two cells and stores values on the
stack in them:

    : cons create , , ;

Use it:

    3 4 cons mycon

Define a word “cdr” that loads the second field, and use it:

    : cdr 1 @ ;
    mycon cdr

Define a different word “cons” that defines words that push the two
values on the stack when run:

    : cons create , , does> dup 0 @ swap 1 @ ;

Define a word that creates a one-dimensional array of cells of a given
size:

    : array create cells allot ;

Use it:

    10 array xs  500 xs 3 !  xs 3 @   \ retrieves the 500

For multi-dimensional arrays and for things like dynamically
allocating conses, we probably need pointer arithmetic.  But we can
bounds-check the pointer arithmetic with fat pointers.  That allows us
to say, for example:

    0 value this
    : 2darray create dup , * cells allot  \ save Y-dimension
       does> to this  this 0 @ * cells this + 1+ ;

This lets us get a pointer to the Nth row of the 2darray, and we can
then use that row as a normal 1-D array, but with weaker
bounds-checking:

    32 64 2darray tile  5 tile  \ get pointer to row 5 of 32
    100 @    \ will work even though the row is smaller than that

Similarly, this allows us to allocate cons cells from an arena that we
can later garbage-collect.  Address arithmetic within the arena is
fine; trying to index out of your arena will fail.

You can also have `allocate` if you want to be able to create new
“segments” at run-time.

One problem I’ve run into with the similar semantics in C is that it’s
impossible to write memmove.