I learned last night that vanadium oxide transitions from
IR-transparent to highly IR-reflective at 68° (or a lower temperature
if doped with tungsten) in 100 picoseconds.  If you wanted to project
an IR image onto something, say for an IR camera, what kind of image
quality could you manage with that?

Well, suppose you have a line of 64 vanadium oxide pixels illuminated
by an IR laser, and you can individually turn them on and off using
individual heating elements, and you’ve arranged the time constant of
cooling to be on the order of the thermochromic response time, so
maybe you can turn a pixel on or off in 200 picoseconds.  This allows
you to modulate the laser beam through each such pixel at 5 gigabaud,
5 gigapixels per second, up to 2.5 GHz; the overall system is 320
gigapixels per second.  Each pulse of light in the air is 60 mm long.

If you shine light through your modulator strip onto a 30krpm spinning
mirror whose axis is more or less parallel to the strip --- say
they’re both vertical --- then the mirror spins by 630 nanoradians
(0.13 arcseconds) per pixel column.  If you can manage such a tiny
beam divergence, then at 10 meters’ projection distance, your pixel
columns are 6.3 *microns* wide.

If your beam waist is 200 mm and your wavelength is 0.1 mm (near IR),
the usual Airy-disk formula approximate formula sin⁡ *θ* ≈ 1.22 *λ*/*d*
gives us 1.22(.1/200) = 0.61 milliradians, three orders of magnitude
blurrier.  And a 200-mm-wide mirror facet spinning at 30krpm would be
something to behold --- ideally from a great distance.

So trying to use such a spatial light modulator in such a way would
probably greatly exceed the capabilities of your electronics, your
optics, and your mechanics.  But it’s something to keep in mind if
those each improve by an order of magnitude or so.

For LIDAR, you could imagine sending out periodic 200-picosecond
pulses by modulating such a mirror to briefly pass light (perhaps in a
direction determined by mechanically moving conventional optics) and
then modulating a second mirror to briefly pass light some time later;
by using analog electronics to vary the phase delay between the two
pulses, you should be able to measure the time delay of the reflection
to within about 20 ps (6 mm).

I don’t know if such fast thermochromic materials exist in visible or
shorter light wavelengths, which would be convenient for
super-high-speed displays.  If you wanted 4000 horizontal pixels
spread across half a radian with a 30krpm spinning mirror, 40
nanoseconds would be plenty fast enough, and there are lots of LEDs
that can do that.

Real-time holography would be another potentially interesting use.  In
particular, if you illuminated a grid of such thermochromic pixels
with a single laser, you could use it as an infrared phased-array
communications transmitter, modulating an arbitrarily large number of
separate beams, each at 2.5 GHz.  (The divergence of each beam, and
thus the number of beams that you could actually separate in practice,
would depend on the number of pixels and on the total aperture and
thus diffraction-limited divergence.)  The pattern imposed on the
thermochromic pixels would merely be an approximate linear sum of
waveplates, one waveplate pattern for each outgoing beam.

Such a system can be used for multicast communication in an even
faster mode.  Suppose your laser source can be modulated at 20 GHz, 25
ps per bit.  By setting the phased array to direct its light to five
specific destinations, after a wait of 200 ps (8 bit times), you can
then talk to those five destinations at the full 20 GHz bandwidth.

A perhaps more interesting use of the phased-array approach for
optical communication is reception, in which you simply reverse the
flow of time; incoming light from a particular chosen source is
focused onto your photodiode (or other detector) with a waveplate on
the phased-array modulator.  You can superimpose several waveplates at
once to enable reception from any of several possible sources (each
with high “antenna gain”, though necessarily lower than you’d have for
listening to a single source).  Similarly you can have several
photodetectors, perhaps at different focal lengths behind the
waveplate; their holographic beamforming patterns on the shared
phased-array spatial light modulator will add noise to one another,
but only mildly so.

Such bidirectional phased-array optics with small arrays of high-speed
photodetectors can also be used as “lensless” cameras, whether by
physically scanning them over a scene or by changing the holographic
beamforming pattern to scan.  And of course these also work in
reverse, illuminating scenes from a distance.

Alternative means of rapid light modulation, other than thermochromic
effects, include Kerr (10 GHz, 30 kV) and Pockels (slower, 10 kV)
electro-optic cells.  I think these can be used not only to set the
phase delay (and polarization rotation) through a material, but also
to turn off and on total internal reflection as fast as you can
modulate the electro-optic cell.  If so, near the critical refractive
index that is the threshold for total internal reflection threshold,
the transmitted wavefront is still potentially planar (it depends on
the phase delay of the electric field over the cell) but has a very
large derivative of refraction angle with respect to the applied
field, and, thus, potentially with respect to time.  If this works, it
is a faster alternative to a spinning mirror for scanning a light
beam, and perhaps a better alternative to a phased-array transmitter
as well.

Liquid crystal pixel arrays, of course, if stripped of their
conventional second polarizer, can also produce a spatially modulated
optical phase delay, and can thus also be used for such holographic
beamforming, especially if the pixel size is not too much larger than
the light wavelength.

If the pixel size of any of these spatial light modulators cannot be
kept small, blacking out all but a small window in the center of each
pixel may help.  A microlens array between the SLM and the focal plane
should be able to reduce the resulting loss of gain, for example by
focusing all the light that arrives from the laser source onto the
small window, or directing all the light that makes it through the
small window toward the single photodetector.  A microlens array
between the SLM and the rest of the world would limit the device’s
field of view but add “antenna gain”.

Whether using liquid crystals, direct electro-optic effects, or
thermochromic effects, if great speed in changing the image is not
required (because the speed is taken care of by the light source or
detector rather than the modulator, which only sends it in an
occasionally-varying direction), it may make sense to use a “passive
matrix” or “active matrix” like a common LCD display to multiplex a
large number of pixels onto a smaller number of control lines.
