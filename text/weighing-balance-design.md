You can get these US$6 scales that use a load cell to measure weights
of up to 500 g with 0.1 g precision, and they work surprisingly well.
Similar scales with 0.01 g precision are available, but everyone seems
to be out of stock.  But for things like food coloring or agar, 0.1 g
precision is really not good enough even for making things; and for
evaluating the results of things like my waterglass foam tests, it
requires unreasonably large samples to get good precision.

A simple balance design to solve this problem is an unequal beam.  You
put a weight of, say, 400 g on the pan of the balance, and you tie a
heavy wire or chain to the top of the weight and loop it over a notch
in a horizontal beam.  A centimeter away on the bottom side of the
beam, there’s a fulcrum notch that rests on a knife edge; ten
centimeters past that, there’s another notch in the top, from which a
sample pan is hung.  Each gram added to the sample pan pulls up on the
400 g weight with a force of the weight of 10 g, so now you can weigh
50 g with 0.01 g precision.

The principle here is similar to the principle of a bismar balance, in
that the balance arms are unequal, but instead of measuring the point
along the beam where the center of gravity is located, we’re directly
measuring the force induced on one end of the lever by an unknown
force on the other end.  It’s more similar to the Roman-steelyard type
of balance commonly used in doctors’ offices.  Since we are not moving
the fulcrum, the moments exerted by the unknown mass distribution of
the beam remain constant and are tared out automatically; and the
inaccuracy of the position of the fulcrum can be calibrated out by
calibrating the apparatus with known weights, and it will not move
thereafter.  Moreover, the movement of the apparatus during weighing
is very small (perhaps 100 microns), greatly reducing the the
importance of factors like the shifting distribution of the weight of
the balance arm itself, the imperfect sharpness of the fulcrum
inducing a change in effective fulcrum due to changing beam
orientation, or static friction from bearings at pivot points.  [None
of these advantages are shared by the steelyard in practice][1].

[1]: http://www.topoi.org/wp-content/uploads/2017/06/etopoi_sp6_bu%CC%88ttner-renn-1.pdf "The Early History of Weighing Technology from the Perspective of a Theory of Innovation, Jochen Büttner and Jürgen Renn, 2016, eTopoi Journal for Ancient Studies, Special Volume 6 (2016): Space and Knowledge, pp.757–776, CC-BY"

This design inherently limits the force on the delicate load cell;
once the force applied is large enough to lift the 400-gram
counterweight entirely off the electronic scale’s weighing pan, the
system goes nonlinear and no further force is applied to the load
cell.

Of course after you build the thing you have to measure the leverage
multiplier; calibrating to a given multiplier is easy to do in
software if you have a way of getting the scale readings digitally.

A second stage of leverage could add another factor of 10 or so,
allowing you to, say, measure weighs up to 5 g with 1-milligram
precision.xs

Varying local gravitational fields can still introduce errors of
±0.5%, as with any load-cell weighing scale.

It occurred to me that maybe strain-gauge load cells are not the best
way to measure mass, not only for that reason, but also because
ultimately your measurement of the load cell is an analog voltage, and
those are hard to measure with any precision.  [Microchip app note
AN3183][0] goes into some of the issues involved, using a differential
amplifier to cancel things like unknown errors in the power supply
voltage; it mentions additional sources of error including
manufacturing imperfections, aging, ambient temperature, heating by
the excitation voltage, nonlinearity in the resistance change,
hysteresis, creep, and noise on the low-level output signal.  The
cheap scales I mentioned earlier cancel some of these sources of error
in part by powering off at random times and retaring when you turn
them back on, which is extremely inconvenient if you had tared
something like a sample boat.  Microchip’s appnote strongly recommends
using multiple different temperature sensors (which, conveniently,
they sell) and correcting temperature-induced errors in software.

[0]: http://ww1.microchip.com/downloads/en/Appnotes/DS00003183A.pdf

Nonlinearity and hysteresis in their sample load cell are ±0.05% of
full scale, but creep is ±0.05% per five minutes, and the temperature
effect on the zero point is ±2%/°, which means that if the scale
changes temperature by 20° during operation, its zero could drift by
40% of full scale; you wouldn’t even get one significant figure of
precision, much less the 3½ sig figs the other sources of error
suggest (and that the cheap scales mentioned earlier seem to deliver).

It occurred to me that if you could convert the mass into a time
measurement rather than a voltage, maybe you could avoid some of these
problems; quartz crystal oscillators for wristwatches are commonly
accurate to 4½ significant figures.  In simple harmonic motion the
angular frequency is sqrt(k/m), where k is the spring constant, so if
you calibrate to a fixed k, then you can square the measured period to
get a measurement of the mass.  A small error in the period will
result in an error twice as large in the estimated mass; so if the
period is wrong by 0.001%, the mass will be wrong by 0.002%.

This approach has the advantage of being immune to variation in local
gravitational force (unlike ordinary types of spring scales), although
it might suffer from creep and aging in your spring.  I think common
spring steels are pretty stable, though, and their spring constant
isn’t temperature-dependent by anything close to 2%/°.

The physical size of the oscillations in question could be very small
indeed.  Ideally you’d like them to be fast enough that you can
measure them quickly, and you’d like to maintain a high Q for the
physical sprung-mass oscillation.  If the whole sample pan with the
sample weighs 60 g, for sqrt(k/m) to be 10 kiloradians/s, the spring
constant must be 6 MN/m, which is 6 N/micron, about 10 times the
weight of the 60 g per micron; so to maintain the acceleration below
that of gravity (probably necessary to treat the sample mass as a lump
rather than separate particles interacting nonlinearly) we would need
to maintain the displacement below 100 nm.

Such small displacements are challenging to detect accurately, even
though we don’t have to measure their amplitude; but a few microns
would be fairly easy.  If the spring constant is only 600 N/m, then
sqrt(k/m) is 100 radians/second, and the displacement under the 60 g
weight is only 0.98 mm.

I suspect that suspending the whole resonating mechanical system with
high compliance (or even locally zero rigidity by canceling negative
rigidity with positive rigidity) would be adequate to get high Q.
Without high Q your measured frequency will be subject to a lot of
error.

You might have to measure six degrees of freedom between the two
masses in the resonating part of the scale; trying to restrain
unwanted vibrational modes with sliding-contact mechanisms would
surely introduce far too much friction to get good Q.  Modern flexure
design techniques might allow you to restrain them in a friction-free
fashion and with adequate linearity.

If, instead of getting the restoring force for resonance from a
spring, you got it from gravity, you’d have a sort of pendulum-clock
scale.  (Reversing the usual situation, this kind of pendulum scale
would be subject to errors from local gravitational acceleration,
while its spring-based sibling described above is not.)  By adding
mass to the pendulum, you can increase or decrease its effective
length.  However, pendulum frequency is inversely proportional to the
square root of length (and directly proportional to the square root of
gravity), and a meter-long pendulum has a period of close to two
seconds (about 2.006 seconds), so a 100-Hz pendulum would have to have
an effective length of 25 microns, a scale at which gravity and even
mass are comparatively unimportant compared to effects like air
resistance and surface adhesion.  So I think probably that is not a
good design direction.
