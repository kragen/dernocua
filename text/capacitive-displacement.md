I was thinking about the kind of capacitive linear encoder sensor used
by digital calipers today.  It occurred to me that it’s a wonderful
way to increase the precision of machinery, stage by stage, and it
ought to be straightforward to manufacture a bootstrapping version by
hand.

The basic primitive is that you have a couple of “combs” with the same
spacing on two different circuit boards.  Each comb consists of a
sequence of parallel wide conductive lines with wide spaces between
them, which are all connected electrically together with some sort of
conductor elsewhere.  The boards are placed on top of one another,
with the lines parallel, with a thin dielectric between them.  When
the two combs on the different boards are in phase, which is to say
spatially aligned, there is a large capacitance between the two combs.
When they are out of phase, so that the lines of one are adjacent to
the spaces of the other rather than its lines, the capacitance is
instead very small.  By measuring the capacitance between such a pair
of combs, you can detect when they come in and out of phase.

To get a usable linear encoder, you put three interleaved combs on one
board instead of one.  When the comb on the other board is coming out
of phase with one of the three combs, it is coming into phase with a
second one, so the total capacitance is always the same, or nearly so.
You need only make a ratiometric measurement of the three capacitances
to uniquely identify the phase relationship of the two boards.

To be more concrete, suppose the combs are 10 mm wide, 100 mm long,
drawn on two fired-clay ceramic surfaces, and separated by a
50-micron-thick layer of paint with a relative permittivity of
about 5.  The area of each comb is about 300 mm², so we can calculate
the peak capacitance we see when two combs are in alignment at about
270 pF, while the parasitic capacitance between two out-of-alignment
combs is probably only about 1 pF.  If we assume the graphite itself
has a resistance on the order of a kilohm, then the circuit becomes
primarily resistive above about 600 kHz.  Above that frequency it
becomes harder to detect small changes in the capacitance because the
graphite’s resistance hides them.  (Measuring the time constant of a
step function response is probably a more practical measurement
method, whether with analog or digital circuits.)

If we can reliably measure an 0.1% ratiometric change between two of
these capacitances, for example with an ENOB-10 ADC, we should be able
to measure the phase to about a milliradian.  So if the lines on the
combs are 2 mm wide, separated by a 1 mm space, and thus have a full
cycle every 9 mm, a radian is 1.4 mm, and a milliradian is 1.4
microns, maybe 350 times more precise than the manufacturing precision
required for the original combs.  However, this is more precise than
is realistic, as will be seen below.

This setup is particularly appealing because of how many forms of
manufacturing error it tends to cancel out or average out.  It really
only cares about the surfaces being flat or cylindrical (so there’s a
constant separation), the right total length, and having the right
number of lines distributed over that length, so that the *average*
spacing of a comb is correct.  If all the teeth on one circuit board
or the other are too big or too small, that affects the absolute
capacitance but almost doesn’t affect the ratio in a given position at
all.

Random errors in the shape of a single comb tooth are averaged out
across all the comb teeth; in the above setup, there are 33 total
teeth on the interleaved plate, 11 in each of the three combs, so this
doesn’t help that much: an 0.5 mm standard deviation in edge location
averages out to an 0.15 mm standard deviation in average edge
location. However, with larger numbers of teeth, this is very
powerful.  Consider, for example, 30-micron-wide teeth separated by
15-micron gaps, presumably with a thinner dielectric.  In 100 mm,
there are 2220 total teeth, 740 per comb, so a 1-micron standard
deviation in edge position for each edge works out to 34 nm standard
deviation for the average.

So in practice it can only give errors on the order of 30 times
smaller than the average local manufacturing error, not 350 times
smaller; to get to 100 times smaller, you would need ten thousand
teeth per comb.  And the *global* manufacturing error is only slightly
diminished: if you make the nominally 100-mm-long combs 101 mm long
instead, or if thermal expansion makes them grow by that much, then
all your displacement measurements will be off by 1%.  Still, a 1%
error in a 1-mm displacement is only 10 microns.

(1% error in steel or concrete at 12 ppm/K is 830°.  In a 100 ppm/K
material like many plastics, it would be only 100°.)

By putting such a comb around the outside of a circle rather than on a
linear slide, you can get a pretty good relative angular measurement
rather than a displacement measurement (a rotary encoder rather than a
linear one), and you also avoid the variation in amplitude as more or
less of the boards overlap.  A 100-mm-diameter circle is 314 mm in
circumference.  If we have 314 teeth per comb, making each tooth about
300 microns wide, and the random error in each tooth edge has a
standard deviation around 50 microns, the resulting random error for
the whole dial will be about 2.8 microns, which is 56 microradians.
This is an error well under a micron for things near the center of the
dial, at which point the uncertainties in the bearings are a bigger
source of error than anything in the electronic realm or in the ruling
of the dial.

At a smaller scale, such sensors should provide even better precision.
If you have a 10-mm-long comb with 10-micron tooth spacing, 30 microns
per comb, then you have 999 total teeth, 333 per comb, and the
necessity to position the combs within a micron or two without
touching.  If the standard deviation per tooth is 1 micron, then the
standard deviation of the average should be 55 nanometers.  Capacitive
and micromagnetic feedback systems can measure smaller displacements
(for decades now) but over a much shorter total travel.

See also [tiltmeter].

[tiltmeter]: https://www.eevblog.com/forum/projects/suggestions-for-high-resolution-tiltmeter-(inclinometer)-sensor/msg1531160/#msg1531160
