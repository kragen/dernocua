Suppose you have some devices that send out periodic ultrasound
signals to each other.  If one sends a ping and another responds, the
two can measure the distance between them using the speed of sound.
If you have three, they can thus measure their pairwise distances and
thus angles, and if there are four or more, they can measure more or
less precise three-dimensional positions up to rotation and
reflection.

Multipath in this case should mostly just produce extra signals that
are delayed by more; it should usually be possible to distinguish the
shortest-path signal.

The array of devices can then coordinate to function as a phased array
for sonar imaging.

The speed of sound
------------------

In dry air at sea level, sound travels 343 m/s.  Wikipedia says this
is 20.05 \sqrt T m/s, so the temperature coefficient is about 0.6 m/s
per degree, ranging from 331.4 m/s at 0 degrees up to 354.8 m/s at 40
degrees:

    >>> C
    array([ 0,  1,  5, 10, 15, 20, 21, 30, 40])
    >>> 20.05 * (273.15 + C)**.5
    array([331.37136701, 331.97738684, 334.39048338, 337.38258383,
	   340.34838089, 343.28855628, 343.8735747 , 349.09462596,
	   354.80569735])

This means that every 1-degree error in temperature estimation of the
air will give rise to a scale error of about 0.17%.

There’s also an inverse-quadratic variation with the molar mass of the
air: dropping the molar mass of the air by 1% will increase the speed
of sound by 0.5%.  Humidity affects this: higher humidity means
lighter molecules and thus faster sounds, although this is partly
canceled by the higher adiabatic index of the non-collinear triatomic
water molecules, so the variation is only about 1.5 m/s for 0% to 100%
relative humidity at STP.  The temperature-induced error is probably
smaller.

Measurement precision
---------------------

A 40kHz wavepacket is hard to localize to better than about 25
microseconds, though probably with repetition and averaging we can get
down to around 2 microseconds.  This is an error of about 0.7 mm.  It
would be feasible for one or more of the devices to include a
meter-long constricted pipe which generates an echo a meter away; this
measures the round-trip time of the sound over a known distance of 2
meters.  0.7 mm over this distance would be an error of 0.035%, plus
whatever the error in the tube length is; this could then be used to
calibrate the scale factor of the overall mesh model, rather than
depending on temperature and humidity measurements.  (It also
*provides* a combination temperature/humidity measurement, where
unknown humidity works out to about ±4.4° temperature imprecision.)

By using a syn-synack-ack triplet it’s possible to measure a single
round trip according to two clocks at nearly simultaneous, overlapping
times, which allows you to measure the relative speeds of the two
clocks as long as they drift over a period of time that is large
compared to the round-trip time.

By using 2.4 GHz radio signals of known phase, it might be possible to
improve this, even in a system made of microcontrollers that are too
slow to respond in nanoseconds or even microseconds.  One
microcontroller starts by transmitting a “pilot wave” that the other
locks a second-order PLL onto, driving the phase error to zero, so the
second microcontroller’s local oscillator is perfectly in phase with
the signal it receives.

Then, the first microcontroller stops transmitting, and before the
phase has time to drift much, the second microcontroller patches the
still-oscillating LO through to an output amplifier hooked up to an
antenna.

Now, the first microcontroller can receive this signal and measure the
phase difference from its own local oscillator, down to, say, 0.2
radians.  This gives you the distance of the round trip (up to
multiples of the wavelength) precise to about 10 picoseconds, about 4
millimeters.

A single such measurement has an ambiguity of multiples of about 125
mm.  By repeating the measurement at a second frequency, you can
eliminate about 97% of the possible candidate distances; doing two
more measurements at two more frequencies should bring the number of
possibilities down to 1 if you know the distance is less than about 40
km.

This 4-mm precision for radio ranging is by itself worse than the
0.7-mm precision for the sonar approach, but it isn’t subject to the
0.17%/° thermal error and 1.5% humidity error of the sonar.  By
combining the two, you should be able to get the best of both worlds.
Suppose you have two nodes about 64 meters apart.  Through radio
ranging they know their distance to within 4 millimeters, an
uncertainty of 0.006%.  This allows them to compute the speed of sound
between them to that 0.006% uncertainty, which allows them to use
sonar to measure the distance to other nodes 10 m away and 20 m away
to that same 0.006% precision --- in the 10-meter case, they’re
limited to 0.7-mm precision, but in the 20-meter case, they get
1.25-mm precision.

This 0.006% precision for the speed of sound translates to measuring
the relative humidity to a precision of 0.4% if the temperature is
known, or measuring the temperature to a precision of 40 millikelvins
if the humidity is known.

(I’m handwaving a bit about things like the difference between
standard deviation, maximum error, and error interval size, because
these precision calculations aren’t that precise.  Hopefully they’re
within a factor of 3 or so.)

Spirometry
----------

By breathing through the tube, or perhaps two parallel tubes with
check valves going in opposite directions, you can do spirometry.  A
typical tidal volume of 500 ml in a 1 cm² tube at a normal breathing
rate of 15 breaths per minute amounts to an average exhalation breath
velocity of 1.25 m/s, with peaks up to perhaps 3 m/s.  This results in
a quadratic change in the round-trip time.  If outgoing sound travels
at 346 m/s and returning sound travels at 340 m/s, then instead of
taking 2.9155 ms on the way out and 2.9155 ms on the way back, the
ping will take 2.8902 ms on the way out and 2.9412 ms on the way back,
pushing the total round trip time up from 5.8309 ms to 5.8313 ms.
This 77 ppm change is easily within the precision of a quartz crystal
to measure, particularly since we’re only interested in cyclic changes
over less than a kilosecond.

However, the one-way trip time changes by almost 9000 ppm, so if you
can put a sensor node at each end of your spirometry tube and run
wires between them, you get 100× more precise spirometry, and an even
bigger advantage at lower flow rates.

Phased-array sonar
------------------

Having a bunch of nodes like this dispersed in a 3-D space allows you
to build a model of all of their locations relative to each other with
accuracy and precision of a few millimeters.  This ad-hoc phased array
of microphones allows you to do passive sonar imaging of sound sources
and sound reflectors in the surrounding environment down to a few
millimeters as well; also, you can emit pings from the devices
to sonically “illuminate” the scene for active sonar.

Orientation sensing
-------------------

The simplest way to sense the 3-dimensional orientation of an object
with such a system is to mount three nodes on it.  Polarization of two
or more antennas mounted on a node is another way.
