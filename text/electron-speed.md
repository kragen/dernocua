Electrons move fast because they are very light and very strongly
charged.

A classroom Van de Graaff generator might charge its sphere to 100
kilovolts.  The capacitance to infinite space of a sphere of radius
*r* is 4*πε*₀*r*, about 11 pF for a 10-cm-radius sphere, so this
voltage would be about 1.1 μC of charge, about 6.9 trillion electrons.
Because an electron weighs about 5.5 × 10⁻⁴ atomic mass units, which
is 9.1 × 10⁻³¹ kg, this quantity of electrons weighs 6.3 × 10⁻¹⁸ kg,
6.3 femtograms.  If such a mass were to fall a meter off the Van de
Graaff generator onto the table under the force of gravity, it would
gain 62 attojoules by falling, dissipating it in the impact (or, more
likely, from air resistance).  But if these electrons instead “fall”
through this 100-kilovolt potential, they gain 111 **milli**joules,
111 quintillion attojoules, about 2 quintillion (2 × 10¹⁸) times as
much.  So, in the absence of air resistance, they would tend to impact
going about a billion times as fast.

The acceleration due to gravity is a pretty normal acceleration in our
world, although there are stronger accelerations like hitting things
with hammers (100 gees or more) and weaker ones like things rolling
down slopes.  And 100 kilovolts is a pretty reasonable kind of voltage
for electostatic machines, though a bit on the high side for
electromagnetic machines and especially for semiconductor devices.
So, in general, electrons tend to move around a few thousand times to
a billion times faster than macroscopic objects.

This is why electronics are so useful for computing.

The advantage becomes smaller when we’re only limited by energy.  With
a joule, you can accelerate 10 trillion carbon atoms (200 picograms)
up to about 0.01 of *c*, 3200 km/s.  If you apply that joule over a
micron, then you will move them over that micron in 0.6 picoseconds.
But if you’re accelerating just their electrons, well, those are only
0.11 picograms (110 femtograms), so classically you’d expect to be
able to accelerate them to 0.45 of *c*, 135’000 km/s, so classically
you could cross that micron in 0.0074 picoseconds, 7.4 femtoseconds.
(Relativistic effects increase this by a few femtoseconds.)

Of course you can’t normally apply a joule to 200 picograms of
anything, much less 110 femtograms — not without the thing ceasing to
be a *thing*.  4.184 joules per gram, a calorie per gram, heats up
water by a kelvin.  So a joule per 200 picograms ends up being 1.2
gigakelvins, about six orders of magnitude hotter than temperatures at
which solid matter exists, even solid matter with a somewhat higher
specific heat than water.  Duly derating the above numbers by six
orders of magnitude of energy and thus three of velocity, it seems
that you can move groups of atoms micron-scale distances at nanosecond
timescales, or you can move groups of electrons micron-scale distances
at picosecond timescales.  If you must remain near room temperature,
it takes several nanoseconds or several picoseconds.

However, Drexler has suggested that if you’re computing with solids,
you may not need to move them as far, because Heisenberg’s uncertainty
principle *σₓσₚ* ≥ ½*ħ* means that their location can be defined to
higher resolution.  Here *p* is the momentum, *x* is the position, and
*σ* is the standard deviation; so increasing the mass 2000× with a
given uncertainty of velocity would increase the uncertainty of
momentum by the same 2000×, so decreasing the (possible) uncertainty
of position by the same 2000×.  So perhaps you have to move some
electrons by 1 nm to resolve the result with a given certainty, which
seems to be what chip manufacturers do these days, but if you were
moving some atoms to encode the same result with the same certainty,
you could move them 2000 times less distance, 500 fm.

This seems rather challenging since, for example, the lattice spacing
of silicon atoms is around 200 picometers, so you’d be deforming the
lattice by about 0.3% of a single atom spacing.  LIGO successfully
measures such small displacements every day, but it still seems
daunting.

Still, if that approach works out, then instead of comparing moving
some atoms by a micron, to moving some electrons by a micron 45 times
as fast, we’d be comparing moving some atoms by 0.5 picometers, to
moving some electrons 2000 times as far, 1000 picometers, 45 times as
fast.  This suggests that in fact computing by moving around atoms
should be about 45 (= 2000 ÷ 45) times as fast at a given level of
uncertainty, at least if you can bring similar energies to bear rather
than similar electric field strengths.
