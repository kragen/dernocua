I was thinking that, for examining data in PDF files, it would be nice
to have Python objects that basically represent chunks of bytes; for
example, the contents of a file, some substring of the contents of a
file, or the output of decompressing them.  You ought to be able to
slice these objects to create new ones on subranges of them, without
copying the underlying data.  And these objects ought to have default
displays that are useful for debugging, but not only one such display,
like the ordinary repr(); rather, several:

- A default text display that represents, in UTF-8 text, the contents
  of the chunk of bytes, treated as UTF-8 text, up to some limited
  number of lines, like 8.  Like, the first four lines, an ellipsis,
  and the last three lines.  Plus magic symbols to indicate things
  like control characters, malformed UTF-8, and trailing whitespace.
- A hex dump display, again by default limited to a small number of
  lines.
- An annotated display that also indicates their provenance.
- Jupyter displays that somehow use Jupyter facilities to display them
  more richly.  For example, Jupyter apparently invokes `_repr_svg_`
  if present (which the `graphviz.Graph` class uses).  Or you can
  return an `IPython.display.Image(filename)` or
  `IPython.display.Image(data=somebytes, format='png')`.

Also, I want to have parse-node objects, which are the same kind of
objects but with child nodes, trailing context, and computed values,
and the computed values are their default display --- but the other
forms of presentation are still available.  To get one of these, you
invoke a .parse() method on one of the raw buffer objects with a
grammar argument, and you get back a version of the same object, but
with the parse-node stuff associated.

Even the computed values ought to be able to have multiple kinds of
displays.

Ideally I’d like to enable clicking around the graph in an
object-inspector sort of way, and clicking on Jupyter output to select
different views and follow links to child nodes.

IPython facilities
------------------

Aha, and I see [IPython also supports customizing tab-completion][0]
by defining a `__dir__` method, which is also what the builtin dir()
uses, and for tab-completion of mapping keys or sequence indices
foo[key], there’s an `_ipython_key_completions_` method.

[0]: https://ipython.readthedocs.io/en/stable/config/integrating.html

[For customizing display, there’s not only `_repr_svg_` but also png
and jpeg representations, and in the HTML notebook, html, javascript,
markdown, and latex][5].  If you define more than one of these I don’t
know how IPython determines which one to use, but there is a
`_repr_mimebundle_` that supersedes them, and an `_ipython_display_`
function which I guess can call whatever IPython methods it wants to
draw stuff.

[5]: https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html

For interactivity, there’s [IPywidgets][1], which is simple enough to
use for simple cases (sliders, dropdown selections) and will use the
above means for output.  For example:

    from ipywidgets import interact
	class Circle:
		def __init__(self, r):
			self.r = r

		def _repr_svg_(self):
			return """<svg width="256"><circle cx="128" cy="128" r="%s" stroke="#339" fill="#c6c" /></svg>""" % self.r

	@interact(r=(0, 181))
	def circle(r):
		return Circle(r)

[1]: https://ipywidgets.readthedocs.io/en/stable/examples/Using%20Interact.html

It’s no ObservableHQ, but hey, it gives you a form-based GUI to any
function.  There’s an `interactive` which creates the widget that
`interact` displays, but lets you maybe display it later with
IPython.core.display.display, which is imported into notebooks by
default.  The dropdown facility is enough to select among different
output facets; this very minimal prototype works, for example:

	from ipywidgets import interactive

	class DataView:
		def __init__(self, data):
			self.data = data

		def widget(self):
			def show(format='text', size=64):
				if format == 'text':
					print(self.data[:size])
				elif format == 'hex':
					print(' '.join("%02x" % ord(c) for c in self.data[:size]))

			return interactive(show, format=['text', 'hex'], size=(0, len(self.data)))

	DataView(open('README.md').read()).widget()

There’s a submit-button version of `interact` called
`interact_manual`, and there’s [widgets.Button][2] which has an
[on_click method][4].  Setting .value on an existing widgets.Text from
another cell causes it to update its value on the screen.  There are
HBox and VBox widgets for layout (not sure if their .children is
mutable), and various kinds of output widgets: widgets.Label,
widgets.HTML, widgets.HTMLMath, widgets.Image (whose .value is the
binary data of the image file, and also takes format, width, and
height parameters).  And there’s widgets.Tab and widgets.Accordion for
selectively hiding things, but not, I think, for computing them
lazily.

I’m able to spawn widgets with a button `on_click`.

Also, suitable for nesting inspectors, there’s a [widgets.Output to
display anything IPython can display][3], which can be used as a
context manager:

[2]: https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html#Button
[3]: https://ipywidgets.readthedocs.io/en/latest/examples/Output%20Widget.html
[4]: https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20Events.html

    out = widgets.Output(layout={'border': '1px solid black'})
	with out:
		display(YouTubeVideo('eWzY2nGfkXk'))

widgets.Output also has a `.clear_output()` method and (maybe in newer
versions?) an `.append_display_data()` method which avoids problems
with multithreading.  However, `display()` with a widget doesn’t get
nested into the output as it should, so I guess my best bet is
mutating a VBox; the following code is a bit awkward but does work:

	def nestable():
		i = 0
		out = widgets.Output()
		inc = widgets.Button(description='inc')
		def inc_click(ev):
			nonlocal i
			i += 1
			with out:
				display(i)

		inc.on_click(inc_click)

		spawn = widgets.Button(description='spawn')
		vbox = widgets.VBox([widgets.HBox([inc, spawn]), out])
		def spawn_click(ev):
			nonlocal out
			out = widgets.Output()
			vbox.children += nestable(), out

		spawn.on_click(spawn_click)

		return widgets.HBox([widgets.Label('-'), vbox])

	nestable()

Finally, non-button widgets have an `.observe()` method.

It’s possible to insert things with a `_repr_svg_` for instance into
these Output widgets, using `display()`.
