How do we bring the goodness of RPN and command-line history into a
multitouch world?

I’ve been thinking about this problem for a few years, and I think my
thinking has evolved to the point where it’s probably reasonable to
implement it.  I think it will make it easy to implement a lot of
really cool and versatile exploratory computation user interfaces.

Basic interaction paradigm
--------------------------

I’m imagining some data values scattered around a two-dimensional
workspace, maybe zoomable, each one represented by some kind of
graphical display, which I’ll call a “port”.

Maybe the data are numbers, or formulas, or programs, or images, or
files, or data tables, or locations in memory in a program being
debugged.  One of them is the “focused port” (this has some
similarities to the WIMP concepts of “current selection”, “current
window”, “current tab”, and “focused widget”) and is highlighted to
indicate this, and there are some operation buttons and knobs
displayed for it, maybe outside of its actual display area, as well as
some generic operations applicable to all objects.  If you click or
tap on another port, the focus shifts to that other port, and the
previously focused port becomes the “background port”, which is also
highlighted in a secondary way.

The ports do not contain other ports; there is no hierarchy of ports.
Data values can certainly contain other data values.

I am agnostic as to whether these ports are rectangular, round, or
some other shape (although I keep imagining them as being round, with
round buttons scattered around them), or whether they are overlapped
or tiled or flowed together like sentences in a paragraph, or whether
they are all composited together on a single canvas, as in KSeg or
Flash.  But it does need to be possible to tap or click on individual
ports.

The data values themselves are conceptually immutable; at any given
time, each port is associated with a single data value, but at
different times that value will be different.  So ports are stateful
but data is not.

Generic user interface operations applicable to all ports include
resizing, moving, cloning, closing, and undo/redo.  These might be
accessible from a menu in a fixed location on the display and/or with
fixed reserved keys.  Each port has associated with it an undo/redo
tree, which you can navigate to restore it to values that it has had
at some time in the past.  Cloning a port creates a new port with the
same data value and a copy of the undo/redo tree, which is then
focused, but from then on the two ports evolve independently.  Closing
a port adds it to a list of recently closed ports, from which it can
be reopened in case of regret.

So ports have state, but it is entirely under user control: ports
cannot change state irreversibly or destroy information, because you
can always undo a state change, and you can copy a port, go back in
time, and see what would have happened if you hadn’t taken the road
less traveled by.

Unary rators
------------

Some of the buttons for the focused port compute a function of the
port’s current value and change the port’s value to the new value,
adding a node to its undo/redo tree, and these normally include some
kind of preview of this new state in their display.  Examples include
incrementing or negating a number, deleting a column from a data table
or sorting it by a column, navigating to a child or parent node in a
filesystem or JSON hierarchy, and perhaps appending a letter to a
string (if we consider each of the letters on the keyboard to be a
separate “button for the focused port”).  If you invoke one of these
and regret it, you can go back in the undo tree; sometimes you will
then want to clone the port and redo the undone operation, so that you
have both the old and the new value visible.  Some other buttons
similarly compute such a function but open a new port to display the
result in; you might have both kinds of button for the same function.
These are best thought of as conveniences for common cases, especially
where you might want to invoke several such operations in a row
starting from the same state; the user can always get the same effect
by manually cloning the port before invoking the operation.

(Maybe it would be fun to call these buttons’ operators “rators” or
“rations”.)

Sometimes a rator might return *both* a new data value for its own
port *and* a data value to display in a new port — a random number
generator, for example.

Rators with continuous parameters
---------------------------------

Some other rators interactively adjust one or more continuous
parameters of the current port, like a slider widget does.  That is,
they compute a new value that is a function of the port’s current
value and some set of continuous quantities.  This might be
implemented by dragging from a button in one or two dimensions while
watching the live preview of the result.  Examples include changing a
numerical value, changing the brightness or contrast of an image (or
cropping it), changing the width of a column in a data table, or
rotating a 3-D object.  Once the user finishes adjusting the value, a
new state is added to the port’s undo tree.

It might be better to use a second finger to drag to adjust the
parameters while the button is being held, which both permits
continuous parameters with more components and reduces the clash with
the one-finger scroll idiom in touchscreen interfaces.

Convergent data flow with binary rators combining two ports
-----------------------------------------------------------

All the data flow described so far is divergent: you can make lots of
“copies” of a value and “modify” each of them in different ways, but
there’s no way to combine multiple values displayed in different ports
into a single value.  But some rators take a parameter that is another
port.  For example, the addition or division rator on a number or
formula might take another number or formula as a parameter, the
differentiation rator on a formula might take a variable as a
parameter, the move-to rator on a file might take a directory as a
parameter (or alternatively the move-into rator on a directory might
take a file as a parameter), the concatenation rator on a program
might take another program as a parameter, and on data tables the
union and intersection rators take another table.

This requires some kind of data value typing to give the user feedback
about which ports are plausible parameters.  It might be best to
display a preview of the rator’s result on each of the possible
visible operand ports, graying out those that are not possible, so the
user can tap the one they want.  If they tap a grayed-out port, they
should see an explanation of *why* it is not compatible; in this form,
such compatibility checking doesn’t require static typing, only
dynamic.  Normally the whole operand-selection thing should be
quasimodal, only active as long as the user is holding down the
operation button.

(WIMP interfaces sometimes use drag-and-drop for this kind of
two-operand operation, but I think that’s clumsy, and it’s profoundly
incompatible with one-finger scroll on touchscreens.)

### Lifecycle behaviors ###

There are at least five different plausible user interface “lifecycle
behaviors” for invoking such a binary operation:

1. The focused port transitions to display the result, and the operand
   port is closed.  This adds a special node to the undo/redo tree of
   the focused port so that undoing will reopen it, and the user need
   not manually restore it from the list of recently closed ports.
2. Similarly, but the operand port remains unchanged.
3. The operand port transitions to display the result, but the focused
   port remains unchanged.  This is sort of like the HP-9100A
   behavior.
4. Similarly, but the focused port is closed, although it’s hard to
   imagine when that would be useful.
5. The result is displayed in a new port, which becomes the new
   focused port when the button is released.  Both of the original
   ports remain open and unchanged.

I think in most cases #1 should be the default, beause that’s what RPN
does, but it seems likely that different options will be best for
different cases.

The “background port” mentioned earlier now comes into play; if you
press and release the operation button without explicitly tapping an
operand, the background port is taken to be the operand if it is
compatible.  (You can always undo if that wasn’t what you wanted.)
There’s a whole invisible focus history maintained so that, when the
background port is closed, the most-recently-focused still-visible
port becomes the new background port; this is just the RPN stack.
This is also used to set the new focused port when the focused port
closes.

Which of the 5 lifecycle behaviors mentioned above is the right
default likely depends on what kind of repetition you’re most likely
to want when you’re invoking the operation.  It’s very useful to be
able to invoke the same operation repeatedly on the same or different
operands while still holding down the operation button, but there are
lots of possible meanings of “invoke the same operation”.  Suppose you
have the number 1.21 focused and you are selecting its multiplication
button.  Here are the kinds of repetition you get if you select the
operands 2.50, 4, and 2.10:

1. All four numbers are collapsed into a single product, 1.21 × 2.50 ×
   4 × 2.10 = 25.41.
2. Same, but the other three numbers remain visible.
3. Each of the other three numbers is replaced by its product with
   1.21, handy if you’re computing a 21% VAT.
4. If the operation somehow remains active while the focused port goes
   away, all four numbers are collapsed into the same single product
   as in #1, but in a different order.
5. Similar to #3, but both the original price and the price with VAT
   are visible.

In cases #2 and #3, it even makes sense to repeat the same operation
with the “same” operands, since one of them now has the result of the
previous repetition.
   
It probably makes sense to offer #5 as an user option with a gesture
of dragging from the selected operand off into empty space,
particularly in cases where #3 is the default.  That is, if you just
tap on an operand port, that port transitions, but if you drag from
it, the new data value appears in a new port where you dragged it.

Part of the question here is how common various kinds of “linearity”
are, linearity in the sense of Girard’s linear logic or linear type
systems.  If a particular kind of value, like a number, tends to be
used only once, it is most convenient for operations on it to remove
it from the canvas, leaving only the operation result, rather than
requiring you to manually remove each intermediate value.  On the
other hand, perhaps joining two data tables through a one-to-many
relationship normally leaves the table on the “many” side of the join
intact, waiting for further joins to be applied to it.

(Henry Baker noted the connection between linearity in this sense and
the life cycle of values on an RPN stack.)

The gulf-of-execution problem for binary rators
-----------------------------------------------

The operand feedback suggested above may not be particularly useful if
no compatible ports are visible on your canvas, creating a large gulf
of execution.  Say you have a formula focused and you try to
differentiate it, but the differentiation operation takes a variable
as its operand, and there aren’t any variable ports visible.  So you
press the differentiate button, all your formulas go gray for a
moment, and then you release it and nothing happens.  How are you
supposed to know how to open a port of the right type?  This is the
kind of problem VB-style forms UIs excel at.

In this particular case, maybe you could fix the problem by opening a
menu of the formula’s free variables, although note that the UI idioms
discussed so far offer no way to open such a menu.

Currying
--------

Computations with more than two inputs can be handled by currying:
providing each of the extra inputs in sequence.  This potentially
worsens the gulf-of-execution problem, because when you provide the
first input you don’t have any way to see what the type of the second
input will be, or that there even is a second input.  This is sort of
like a “wizard” or a “dark pattern”.

So, for example, to equijoin two data tables, you might tap an unary
equijoin rator that one of the two tables displays on one of its
column headers, which opens a new port for the next step in the join.
The new port might display the same data table, maybe with the column
in question highlighted and some information about the column’s data
type and typical values; a binary rator on the join port allows you to
select a table to join with, which transitions the join port to
displaying data from the columns of the second table, each with an
unary rator to select each of them as the join column, and maybe some
outer join options.  Tapping one of those unary rators transitions the
join port to displaying the join result.  At any point, even long
after completing the join, you can “undo” to go back to a previous
step and change the options.

This kind of program-controlled sequencing is anathema to event-driven
GUI thinking, according to which the user should be in control of what
order they provide the information to complete an operation.

Programming by example with rator names
---------------------------------------

Suppose that each rator has a consistent name, though perhaps not one
that is displayed prominently in the UI.  Then we can imagine writing
a transcript of a part of a session, automatically assigning a hidden
variable name to each port involved:

    v0 := Number new.   “Create a number for the VAT.”
	v0 set: 1.21.       “Adjust its value with a slider.”
	clone(v0, v1).      “Clone the port so we can use it twice.”
	v2 := v2 * v0.      “Multiply the first price by VAT.”
	v3 := v3 * v1.      “Multiply the second price by VAT.”
	v2 := v2 + v3.      “Add them together.”

This slighly silly transcript contains three free variables ---
`Number`, `v2`, and `v3` — which are in some sense inputs; and it
ends with one unconsumed result in `v2`.  So, when you are interacting
with concrete values in this way, you are also “programming by
example” or “programming by demonstration”, building up a script that
could be later applied to different input data, in a way similar to
John W. Cowan’s system “Mung”.

(Maybe `Number` is really a constant rather than an input.)

You could imagine converting such a single-output transcript into a
new rator (keyboard macro recording), or automatically snipping it
into separate rators at the boundaries where new inputs appear.  The
standard facilities for output preview and operand compatibility
scanning can apply automatically to these new rators just as they
apply to built-in rators.

This may run into some difficulty with the idea that the applicable
rators might be derived from the data; for example, a data table view
might have a unary rator to sort by the Rating column and another to
sort by the Price column, but the same data-table-viewing code will
have a different, arbitrarily large number of applicable rators when
it’s looking at a table with a different number of columns.  I think
we can solve this by allowing the “rator selector” to include
arbitrary immutable data rather than just being a symbol in the way my
Smalltalk-syntax example above suggests.

How do you know in what ports a new binary rator thus defined is
applicable?  At first, I thought this might require static typing, but
as long as we can run code peremptorily without harm, I don’t think it
does.  The above script requires inputs `v2` and `v3`.  Suppose we
should offer it on a port’s menu whenever the current state is
suitable for use as `v2`, which is to say, it has a `*` rator that can
accept our `v1`, which is the Number 1.21; we can determine this by
trying to run it, and checking to see where it crapped out.  If it
croaked trying to read the not-yet-defined `v3`, then we’re probably
good, but it shouldn’t be a menu option if it didn’t even get to
trying to read `v3` and instead died on a previous line because `v2`
doesn’t have a `*` (or someone hacked Number and its instances no
longer support `set:`).

If you want conditionals in pure programming-by-example form, you can
get them with assertions and fallbacks, but I’m not sure how to do
loops.  So it might be best to reify the macros in the interface so
you can apply operations like “if” and “while” to them.

Dependencies and external state via paint functions
---------------------------------------------------

Each data value provides not only the transition functions invoked by
rators, but also functions that the user interface shell uses to paint
its port and rators.  So far most of my examples have concerned only
painting data pulled from the data values themselves, like the column
widths of a table view, or column names and data cells from the
underlying immutable table it refers to.  But we could imagine that
the paint functions can also read mutable state that lives outside the
rator-port system, like the list of running processes on the system,
or the contents of the filesystem, or the history of IRC messages on a
channel.  So the rator-port system can give you undo and cloning and
stuff for everything inside it, but you might only be using it as a
cyberdeck through which you interact with the stubborn and refractory
traditional world.  (Even the set of available rators on a port might
depend on the state of the external world; consider navigating to a
filesystem subdirectory.)

If we allow paint functions, or some of them, to read the mutable
state of the outside world, then we might as well allow them to read
the mutable state of the ports as well, and thus data values to
contain pointers to ports.  In this case, we could imagine, for
example, having some data values representing formulas in which the
variables are pointers to ports, and having the
increasingly-poorly-named paint function evaluate those formulas
recursively.  Then, if we change the formula in one of the ports, all
the ports whose formula refers to it will also update their display on
the next repaint.  (Which we ought to be able to arrange to happen
quickly.)

Note also that the rator functions are themselves just pure functions,
so it ought to be feasible to incorporate them, or even a PBE script
invoking a sequence of them as described above, into a paint function
in that way.  (Of course that’s essentially how the system’s results
previews work.)

At this point it becomes necessary to cache the evaluation of parts of
a paint function that depend on mutable state (“nested transactions”),
so that you don’t re-evaluate the same formulas exponential numbers of
times for each repaint.  And this brings us to the question of
background computations, progress, cancelation, and futures.

Background processes
--------------------

Everything above has supposed that all the computation is fast enough
that it’s always effectively instant, but of course that is a bad
assumption for a user interface, especially in latency-sensitive
environments like touch and especially VR/AR.  In practice we can’t
miss video frame deadlines simply because a formula is slow to
recalculate!  But everything described so far is purely
side-effect-free, except for consuming input events, port transitions,
and updates to the cache; so it’s always safe to discard and/or
restart a computation in progress, as long as we don’t consume
whatever input events inspired it.  So probably we can keep painting
responsive by just having the display of some ports update after
several frames, and maybe giving them a “fast paint” function whose
results can be used when the slow paint function is slow.

However, we also might want to run background computations that take a
while, like solving a large system of equations, maybe even in
separate OS processes or on separate machines.  I think the simplest
way to handle that is to treat the *output history* of such a
background computation as “mutable external state”, so a port can
display that history in whatever way it chooses: scrolling text,
progress bars, progressive image enhancement, whatever.  And if the
background processing happens internal to the rator-port system, well,
aborting the computation is just another event to add to the log.
It’s guaranteed not to corrupt anything else.

Not Actors
----------

These ports are very similar to Hewitt’s Actors, but there are some
significant differences.  Like Actors, ports have a current state,
which can include references to other Actors, and a state transition
function that specifies how their state should change in response to
external events.

But ports cannot send messages, either to other ports within the
system or globally, and they cannot create new ports.  And they have a
fixed set of methods, rather than a single “invoke” operation or an
arbitarily large set of methods: one to paint, and one to return a
list of currently valid rator selectors and their corresponding
closures.  (Or maybe there’s a third method to invoke a given rator
selector.)

Moreover, ports don’t manage their own state; their rators return a
new data value and some kind of indication of where to stick it, but
that new data value might end up being the new state of a *different*
port, and at any rate you can time-travel the ports independently to
any previous or later state.  They can’t count on other ports being in
a state that is in some way mutually consistent.

(This suggests that maybe another reason that the default lifecycle
behavior should be #1 or #2 is that it’s maybe kind of bad to set that
data value as the new state of a different port, since it will wreck
whatever display preferences the user had set up.  But how else will
we arrange to set the same background color on three different drawing
objects conveniently?)

Modality-agnosticism and graceful degradation
---------------------------------------------

This doesn’t have to be limited to multitouch; the abstraction level
of invoking rators with operands on a bunch of ports to get them to
transition to new states means that most of your code would be fine on
a terminal.

If you’re writing a paint function for something that’s basically some
text, what you really want is to call a library function with either
the literal text or a lazy stream of the text, and have it produce the
painted window and maybe some scrollbar interaction stuff, and then
just return it.  Then you could run that same paint function in a
terminal interface by passing in a different library of paint-function
building blocks.

It’s important to structure the user interface libraries such that
most of your code doesn’t care about pixels and touches.

Taming external processes with snapshots
----------------------------------------

If we can take snapshots of external process state and record and
rewind and replay it, then we can apply the whole undo/redo/clone
thing to computations carried out by external processes as well, as
long as we confine their I/O well enough; we can treat their behavior
from one input to the next as a “pure function”.  Batch-mode external
processes don’t even need snapshots; we only need to “snapshot” the
filesystem before they start and after they stop, potentially using
something like Docker.
