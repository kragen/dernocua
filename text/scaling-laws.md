[Galileo’s square-cube
law](http://galileoandeinstein.physics.virginia.edu/tns_draft/tns_109to152.html)
explains that a cylinder over a given dimension will collapse under
its own weight:

> From what has already been demonstrated, you can plainly see the
> impossibility of increasing the size of structures to vast
> dimensions either in art or in nature; likewise the impossibility of
> building ships, palaces, or temples of enormous size in such a way
> that their oars, yards, beams, iron-bolts, and, in short, all their
> other parts will hold together; nor can nature produce trees of
> extraordinary size because the branches would break down under their
> own weight; so also it would be impossible to build up the bony
> structures of men, horses, or other animals so as to hold together
> and perform their normal functions if these animals were to be
> increased enormously in height; for this increase in height can be
> accomplished only by employing a material which is harder and
> stronger than usual, or by enlarging the size of the bones, thus
> changing their shape until the form and appearance of the animals
> suggest a monstrosity.

Different properties
--------------------

Suppose we scale some physical system up by some factor *f*, or down
if *f* < 1.  Not only will some of its static properties change, as
Galileo points out above, but also some of its other behaviors will
speed up or slow down.  But by how much?

### Mass ###

The mass and thus weight of a body will tend to scale as *f*³.

### Tensile failure ###

The tensile strength of a member will tend to scale as *f*², so by
smallifying an object we make it stronger (1/*f* times) relative to
its own weight.  If we consider stress from accelerations, well, this
means we can accelerate it faster (1/*f* times) before it fails in the
tensile mode; relative to its own dimension, this is an advantage of a
factor of 1/*f*² in acceleration, but this only works out to a factor
of 1/*f* in frequency.

That is, suppose we have some sort of machine in which a weight is
being jerked back and forth along a course inside the machine by a
rope, and if we run the machine too fast, the rope will break.  We
smallify the machine, say by a factor of 1/*f* = 3.  Now the weight is
being moved a 3 times shorter distance, it has 27 times less mass, and
the rope can withstand 9 times less tension.  So the rope can
withstand 27/9 = 3 times greater acceleration, but at a given jerking
frequency, 3 times less acceleration would be needed to jerk the
weight the same distance.  But the length of the weight’s course
within the machine has also diminished by a factor of 3, so at the
same operational frequency, the stress on the rope has actually
diminished by a factor of 9.

However, if we run the machine 3 times as fast, so that it jerks the
weight 3 times as often, the velocity increases by a factor of 3, but
the acceleration increases by a factor of 9.  So, in the mode of
tensile failure, smallifying does increase the maximum frequency, but
only proportionally, not quadratically as one might hope.

### Buckling failure ###

XXX Euler columns

### Shear failure ###

XXX

### Compressive failure ###

XXX

### Elastic beam bending ###

The usual expression for rectangular beam bending stiffness is *k* =
*Ebh*³/4*L*³, where *E* is the material’s modulus, *h* is the
thickness of the beam along the direction of bending, *L* is its
length, and *b* is its width transverse to the direction of bending.
If we scale the beam uniformly up or down by some factor, then the
changes in *bh*³ and *L*³ leave the stiffness varying directly with
the scale.

### Resonant tines ###

The general expression for the resonant angular frequency of a
sprung-mass system is *ω* = (*k*/*m*)<sup>½</sup>.  So, if a mass is
at the end of an elastically bending beam, the mass *m* changes by a
factor of *f*³ while the stiffness *k* changes by a factor of *f*, so
its resonant angular frequency changes by a factor of 1/*f*.

tensile-mass oscillation

shear-mass oscillation

### Dennard scaling ###

XXX

### Resistors ###

A resistor’s resistance is *ρL*/*bh*, where *ρ* is the resistivity.
If it becomes *f* times longer and *f* times wider and deeper, it will
thus diminish in resistance by that same factor *f*.  Smallifying
resistors thus makes them proportionally higher in resistance; we
might say that *conductance*, rather than resistance, is proportional
to scale.

A thin resistive film whose thickness does not change is well known to
have a characteristic “resistance per square”: its resistance over 1
mm × 1 mm is the same as its resistance over 1 cm × 1 cm or 1 μm × 1
μm.

At ordinary (macroscopic) sizes it is easy to achieve an enormous
range of resistances at any scale, because in a given volume you can
either make a long, thin conductor or a short, thick one, and moreover
available resistive materials themselves cover several orders of
magnitude of resistivity; resistors from 0.001Ω to 1GΩ are all staple
articles of commerce, and resistors from 1Ω to 1MΩ are common, and all
of those common ones are available at any size from 0402 up to many
watts.  At the lower end these resistances are limited by the
resistances of the commonly employed wires (i.e., not superconductors,
but materials like copper) and at the upper end by the leakage
currents of materials such as glass, polypropylene, and Teflon, used
as insulators.

On chip, the story is different, because although low resistances are
easily accessible (just use a metal layer) high resistances such as
100kΩ are not; they occupy an inordinate amount of space and are a
nuisance.

### Capacitors ###

A (planar) capacitor’s capacitance is *εA*/*d*, where *ε* is the
permittivity of the dielectric.  This is proportional to *f*, so
smallifying capacitors thus makes them proportionally smaller in
capacitance.

Common macroscopic capacitors cover an even wider range than
resistors, from 10 pF to 50 F, or 10000 μF if we exclude
supercapacitors.

### RC time constant ###

Perhaps the most common way to mark time in an electrical circuit is
with an RC circuit with an exponential decay time constant *τ* = *RC*;
this is how RC filters and 555 timer circuits work, for example, and
how the internal oscillators in microcontrollers work.  Since *R* is
inversely proportional to *f* while *C* is proportional to it,
smallifying an *RC* circuit will not change its frequency response.

This is an astonishingly different result from Dennard scaling.

### Inductors ###

A cylindrical air-core coil has an inductance of roughly *μN*²*A*/*L*.
Scaling it by *f* increases *A* by *f*² and *L* by *f*, so inductance
scales with *f*.  So inductance, like capacitance and conductance, is
proportional to scale.

### LC frequency ###

The resonant angular frequency of an LC circuit is *ω* =
(*LC*)<sup>-½</sup>.  So multiplying both *L* and *C* by a factor *f*
will multiply *ω* by 1/*f*; larger LC circuits oscillate
proportionally slower.

### RL time constant ###

### etc. ###

electromagnetic relays

electrostatic relays

crystalline structure

heat transfer characteristic time

turbulent vs. laminar flow

matter diffusion

composite materials

aerostats

heat exchanger design

mass transfer design

liquid friction
