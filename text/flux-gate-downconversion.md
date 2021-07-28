Lower radio frequencies like AM radio are typically received with
ferrite loopstick antennas rather than half-wave dipoles or similar,
because the dimensions of an efficient dipole are totally impractical
for a human-scale system.  It occurred to me that if you saturate the
loopstick with a magnetic field at a different frequency, you could
use it as a magamp that does downconversion, either for downconversion
to IF or baseband — in a sense, using the ferrite as a flux-gate
magnetometer to measure the magnetic component of the radio waves at
submicrosecond intervals.

Mediumwave AM broadcasting is 530 kHz to 1700 kHz, so you couldn't
just use a single fixed frequency to downconvert to IF — you could
imagine using a 400 kHz LO to get 130–1200 kHz, say, but that's
useless.  If you tried saturating the ferrite with a square wave at
the frequency of the desired station, you might get half-wave
synchronous rectification of the frequency without so much as a diode,
or you might get nothing if you were in quadrature.  So you'd probably
need some kind of second-order PLL or something to keep your phase in
sync, and it would have to tolerate the intermittent nature of AM.
This is probably more complexity than the usual tuning circuits, so
there may be no real advantage to this design at all.

There are magnetic core materials that work well up to about 10 MHz.