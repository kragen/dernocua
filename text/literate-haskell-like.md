Watching a demo of Keras in TensorFlow in IPython, I thought a Python
comment was a Markdown header.  And it occurred to me: why *not* have
formatted text comments in your code?  Or code in your text document?

Literate Haskell works like this: you write text like normal, but mark
your code with a leading `>`:

    > 3 + 4

You could imagine a sort of word processor that works this way,
automatically displaying the results of your code within the document,
like a spreadsheet or like Darius Bacon’s Halp.  You could even put
bits of code in the middle of a paragraph, displaying the code, its
result, or both at your whim.  This works best with non-procedural
programming paradigms like logic programming and pure functional
programming.

Programs normally contain a mix of commentary with executable code.
Traditional programming languages make the code primary, relegating
the commentary to a secondary role, while literate Haskell reverses
this.  Python doctest docstrings do something similar: the docstring
can contain code, but it is specially marked with `>>>` or `...`.
IPython and ObservableHQ notebooks follow a middle way, treating
either code or commentary as primary depending on which kind of cell
you’re in.  But I think that normally the commentary should be primary
and the code secondary.

Ideally when your cursor was near something easily identifiable as a
quantity, like `3`, `3.17 bits`, `23 AWG`, `45 psi`, or `2.4 GHz`, it
would become available for naming, referencing, and calculations;
maybe you’d have a sidebar that showed you the names, definitions, and
current values of nearby bits of code.  Maybe as part of this sidebar
you’d have a stack of active data, so that by typing alt-+, alt--,
alt-/ or alt-* you can apply arithmetic operations on the top item on
the stack, or by typing some other magic key like alt-X you can invoke
some named operation on it, such as getting some property.

So you might type “23 AWG wire has a cross-sectional area of ”, and
then, looking at the object in the sidebar which represents a cylinder
with a diameter of 0.57 mm and an unknown length, type alt-X and begin
typing the name of the “base area” property, releasing Alt when you’ve
typed enough to disambiguate; but on seeing that 2.58e-7 m² appears
in your document but is not a very useful way to display it, type
alt-A or something to get a menu of likely units, then select mm²
(rather than, say, `argentina_area` or 分地), thus changing the
display of the value to 0.258 mm².

Then you can type “ and, if copper, a resistance of ”.  Maybe the
system recognizes that “copper” is the name of an entity which has
properties, so it shows up in the sidebar, or maybe you have to open a
search box for it; either way, you get its resistivity of 16.78 nΩ⋅m
(at 20 °C) or, according to units(1), copperconductivity of 58 siemens
m / mm^2 (the Wikipedia value above works out to 59.59).  At this
point you can divide the resistivity by the surface area, or multiply
the conductivity and then take the reciprocal, with a couple of
keystrokes, to get the resistance: .0668 kg m / A^2 s^3, which is to
say, .0668 Ω/m.  (Ideally that would be the default way it was
presented.)

At this point you can go back and drag your mouse over the “23 AWG” to
change the wire gauge, or click on a dropdown arrow next to “copper”
to select other metals.

Of course, many wire resistance calculators already exist, and you can
do this problem in units(1) as well:

    $ units
    Currency exchange rates from FloatRates (USD base) on 2019-05-31 
    3460 units, 109 prefixes, 109 nonlinear units

    You have: 1/circlearea(awg(23)/2) copperconductivity
    You want: ohms/m
        * 0.066785595
        / 14.973289
    You have: 

But it typically requires a fair bit of blundering around to get
there, and in fact I solved the problem wrong the first time.

(Perhaps the “focused item” in the sidebar should have an expanded
view that tells you what the result of each property and possible
operation would be.)

A different approach to solving this would be to instantiate a
cylinder by binding the “material” property of the 23 AWG cylinder to
“copper” and its length to 1 meter; this defines its mass, volume,
surface area, electrical resistance, thermal resistance, etc.  Then
you could just pop in the electrical-resistance property.

Once you’ve reached this point, you can name the resistivity result,
the wire metal, and the wire size as properties of the current
document, and incorporate some more text: “If iron, ” and then
construct `this{metal=iron}.resistivity`, the resistivity property of
an instance of the current document with the metal changed to be iron.
This is just bog-standard Bicicleta.

You might also want to do things like plot the resistivity against AWG
or against, say, mass per meter, perhaps for different metals.  You
might want to include a table of the current calculations for, say, a
variety of different materials.  You might want to apply gradient
descent to maximize some property.
