If you have some slips of paper on a table, you can translate and
rotate them around the table with two fingers.  But you can’t move the
fingers further apart without tearing the paper or slipping on it, and
if you move them closer together, the paper buckles and maybe
wrinkles.

In typical early multitouch demos, this two-finger drag gesture was
used to arrange photos or other objects on a surface, resizing them in
the process.  I’ve also seen people use it in SnapChat to place text
on a photo while resizing it.  Mostly it seems to have fallen out of
favor, though.

What if you had an infinite canvas on which you could rotate and move
objects, like these slips of paper, but also interact with them by
moving your fingers nearer and further?  For many objects it isn’t
that useful to expand and contract them, or even to rotate them.  You
could use these extra degrees of freedom in the two-finger touch to
control one or two continuously variable parameters of the object or
to invoke actions on it.

The single-finger drag has become an idiomatic way to scroll in
multitouch environments, and single-finger taps either select an
object or invoke a button.  So a two-finger drag as a universal way to
move movable objects seems like a promising interaction paradigm.  It
potentially conflicts with the idiomatic pinch-zoom interaction, but I
think that you can still support zooming by pinching on the
background.

What these objects should be or do depends on the application, but one
of the most appealing features of a potentially universal UI paradigm
like this one is that it permits the modeless coexistence of objects
from different applications.

Container objects can do a few different things.  The simplest thing
they can do is to move the objects they contain when they are
themselves moved, maybe rotation too.  If they support a copy
operation, they can copy the objects they contain in the process;
similarly for a hide operation, perhaps provided by a tabbed view
widget.  They can do layout for the objects they contain, for example
radial or table layout.  They can also publish and subscribe to
communicate with the objects they contain; those inner objects can
then be used as tools to alter the outer object, or vice versa.

Tool objects that can alter other objects are a major way to extend
this approach, since without interaction between objects, each object
is limited to only two parameters or some sort of menu system.  But if
you can target a tool object at it, for example bringing it under some
sort of magnifying glass or selecting it to bring up its attributes as
separate on-canvas objects, you have arbitrary freedom.

