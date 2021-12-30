If you have a probe pressing against a material, its force and
position are functions of time.  If you’re using a spring attached to
an actuator, you can try to jam it in harder or less hard, which will
tend to increase or decrease the force, respectively; but the material
can then yield.  Viscoelastic materials will yield to different
degrees at different time scales, and every material is somewhat
viscoelastic; this gives us a complex spectrum in which the real part
at a given frequency is the elasticity (or resonance) and the complex
part is a frictional loss.

If you apply a Heaviside step function to the probe, in theory this
contains all frequencies and so you can determine the material’s
entire viscoelasticity spectrum from its response to the step
function.  In fact, though, your step function is going to be
bandlimited, and the material’s response at low frequencies may be
lost in the noise.  By applying a *sequence* of such step functions,
sometimes in opposite directions, at random times, you can get more
data points, which will allow you to estimate not only the
viscoelastic spectrum of the object but also the frequency and Q of
its vibrational modes.

A piezoelectric actuator can straightforwardly produce frequency
components up to a megahertz or so, and a strain gauge or
piezoelectric force sensor can measure its special mix of force and
displacement at similar speeds.

You can use the same approach for dielectric spectroscopy of
time-dependent permittivity and magnetic spectroscopy of
time-dependent permeability.
