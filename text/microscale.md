Watched a Nominal Semidestructor advertising video recently about
weighing an eyebrow hair with an analog meter movement.  Paul Groke
built his scale as follows: he oriented the needle horizontally,
connected up an optointerruptor to an opamp that drove the current
through the meter movement so as to maintain the optointerruptor half
interupted, then dropped his eyelash on the end of the needle.  Then
the current required to restore the zero position gave a measurement
of the weight.  Result: 75 micrograms or something.  I guess he
calibrated it previously.

(The circuit is very simple: the opamp has a resistor from its output
to its inverting input, which is connected to the photodiode, and its
noninverting input is held at a fixed bias voltage.  Then the output
is just connected to the meter movement, which is then connected to a
resistor to ground.  So the current flowing through the resistor keeps
the inverting input equal to the bias voltage, and that current is
just the photocurrent, so the output is maintained at a voltage above
the bias voltage proportional to the photocurrent by the factor of the
resistance.)

The nice thing about this kind of Kibble balance is that, except for
elastic deformation, the movement is in the same position when it’s
balanced as when it’s empty.  The magnetic field can be wildly
nonuniform over the range of the meter’s movement, but you don’t care
because once you’re taking a reading you’re back at the same position;
all that’s changed is the strength of the magnetic field (which is
hopefully linear in the current) and the bending of the balance beam.

(This version of the ampere balance used to be called a “watt balance”
because the power needed to restore the position is what’s
proportional to the weight.  Kibble proposed it in 01975, and after he
died in 02019 they renamed the instrument after him.  The full-fledged
Kibble balance includes some other refinements and can measure mass by
reference to voltage, current, gravity, and speed.)

It occurred to me that a simpler and higher-resolution version of the
instrument would use electrical contacts instead of an
optointerruptor, ideally gold-plated spherical ball bearings to ensure
a well-defined point of contact.  Then you include a small ac or noise
component in the coil current in order to get intermittent contact and
thus a continuously varying feedback signal (“stochastic resonance”).
Such electrical contacts can detect movements of nanometers rather
than the microns you get from an optointerruptor.  At this point
thermal deformation and creep of the balance apparatus become more
significant sources of error than the sensor.

