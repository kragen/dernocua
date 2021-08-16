I was talking about flashlights and mentioned that I’d tried designing
a constant-current buck converter without success.  But now I don’t
see what was so hard about it.  Maybe when I submit this design to
simulation I’ll find out.

The basic constant-voltage buck converter is
GND->|-a-R1-b-L1-c-C1-GND.  The input power waveform is applied
between GND and a; the output voltage appears across the output
capacitor C1.  Subject to enough output load to keep it in continuous
conduction mode (CCM), the output voltage is the average input
voltage, so if the input voltage is a fixed voltage with a fixed duty
cycle, then the output voltage is inherently regulated and will change
very little with load.  The current shunt resistor R1 allows you to
measure the average load current, filtered through the LC low-pass
filter that forms the output; when this is not necessary it can be 0Ω.

To drive this circuit, though, you need some kind of square-wave
oscillator that switches point a between between a constant input
voltage and open circuit (or, in CCM, between the voltage rails, in
which case you don’t need the freewheel diode ->|-.).  You can use an
opamp configured as a relaxation oscillator, for example, or a
comparator between a sawtooth or triangle oscillator and a reference
voltage level which determines its duty cycle.

My thought was that you should be able to use a single opamp as a
differential amplifier across points a and b to set the reference
voltage level for that comparator; for example, hook up point b to its
noninverting input and point a through a 10k resistor to its inverting
input, then a 100k resistor between its inverting input and its
output.  So then if point a swings up 0.1V relative to point b, the
output must swing down by 1V to compensate.

I think you can probably make it simpler, though: by adding an
error-integrating capacitor and positive feedback for a
Schmitt-trigger effect, you should be able to integrate the
square-wave generation into the same opamp rather than needing a
separate ramp generator and comparator.  I’m kind of fuzzy on how to
actually do this, so I'm not sure you can do it all with a single
opamp, but I suspect you can.

The capacitor across the output of the buck converter low-pass filters
the current signal you’re measuring and can briefly source or sink
immense amounts of current itself, so if you want a *really*
constant-current supply (perhaps because overshooting your current
limit will burn up your expensive laser diode) you might want to make
it very small or remove it entirely.  Such extreme measures would
probably require clamping the output with a TVS or at least a regular
zener.

This feedback circuit is pretty close to being a class-D amplifier — I
think you can use the same approach of modulating a square-wave duty
cycle with the integrated difference between a reference signal and
the variable-duty-cycle square wave itself to get a class D audio
amplifier.  The only difference is that the “audio” amplifier input
here is tied to the low end of the current sensing shunt resistor.  It
would be pretty cool if you could make a class D amplifier out of a
single op-amp.