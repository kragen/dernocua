I’ve previously written a bit about a hypothetical new hypertext
medium displaying several “cards” or “scraps” at once.  I think “leaf”
is maybe better terminology.

The idea is that your memex consists of some collection of “leaves”
and dynamically lays out as many as will fit on the screen, something
like TiddlyWiki or Ward’s Simplest Federated Wiki; but the leaves are
a bit smaller, like a line of text rather than a paragraph.  Each leaf
is identified by a globally unique leaf ID which can be used to link
to it, and those links may be activated explicitly (for example by
clicking) or implicitly in order to display some other leaf.
Typically these implicit links include previous and next links, which
permit reading through a linear document in a more or less
straightforward fashion by shifting the focus to earlier or later
leaves --- if necessary by clicking or tapping them, but usually just
by centering them in the display.  (This implies that the potentially
infinite graph of implicit links cannot simply be fully traversed to
decide what to display at any given time.)

In addition to this subatomic conception of hypertext, we have
*parameters* in the links, like #fragment identifiers on the WWW.  The
rendering of a leaf for display is done by some arbitrary
Turing-complete code, contained in the leaf or linked from it, which
is supplied some arbitrary blob of parameters from the link that was
followed to display it.  By interacting with the display (clicking on
it, typing characters into it, etc.) you can change these parameters
under the control of that code.

In this way, it becomes straightforward to write a leaf that, for
example, contains data and buttons to plot the data in different ways
by invoking other leaves with the data as parameters, or that invokes
an “infobox template” leaf with some parameters in order to present
that data visually in a consistent way.

I’d like to do some kind of infinite regress thing where the leaf
contents are themselves produced by invoking some piece of code with
some parameters, and the leaf ID likewise consists of the ID of that
piece of code and its parameters, so that ultimately we ground
ourselves in a single “primitive leaf” that provides some kind of
fundamental virtual machine.  But I don’t quite see how to do that
yet.

In the stuff you have on the screen you can thus have a mix of stuff
you wrote, stuff you’re taking notes on, and code.