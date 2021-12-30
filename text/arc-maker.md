Stick welding is a pain partly because of the necessity to strike the
arc and the danger of sticking the electrode; with a traditional
buzzbox it takes some skill to learn to avoid these.  And an arc
furnace is clearly the easiest way to reach temperatures over 1000° or
so.

Basic circuit parameters
------------------------

In theory, though, an intelligent control circuit could make this a
lot easier.  A high-frequency start mode, as found on some TIG
welders, could activate when open circuit is detected, initiating a
plasma; and when you stick the electrode and a short circuit is
detected, the high-power circuit can be turned off entirely until a
low current detects that the short is cleared.  Perhaps by monitoring
the arc voltage it could even warn you you’re getting too close.

I think about the lowest an arc can go usefully is about 50 volts and
10 milliamps, but for welding as such you need much higher currents:
10 amps at least, 100 more typically.  But the initial high-frequency
start, according to conventional wisdom anyway, requires something on
the order of a kilovolt per millimeter, so, say, 3kV at 100kHz, but
then probably only up to a few microamps.

The normal welding current can run at a much lower frequency than the
high-frequency start; 100-120 Hz is traditional, but even 500 Hz would
be reasonable.

[A table of values from Deringer-Ney][11] cites minimal voltage and
current conditions for maintaining an arc, however short, for
different electrode materials; silver is said to require 400-900 mA
and 11-12.5 volts, while carbon only 10-30 mA, but 15-22 volts.
Sadly, no values are given for the materials I’m most interested in,
like copper, steel, brass, and tungsten carbide.  Still, these values
are much lower than I had expected!

[11]: https://www.deringerney.com/assets/1/7/1.9.2_Arcing_Systems.pdf "p. 6"

Can you just use a single flyback?  No!
---------------------------------------

In theory a flyback converter can smoothly switch between any output
voltage and frequency, but in practice I feel like this factor of 60
in voltage and 200 in frequency is probably pushing it pretty far.
Like, suppose your flyback transformer has a turns ratio of 80:1, so
one volt on the input produces 80 volts on the output.  So in theory
you can get 50 volts output with 5-volt input pulses at a duty cycle
of 1:8 or 1/9, so the pulses are on for 11% of each 2-ms cycle (thus
220 μs) and off for the other 89%.  And to get 3000 V out, the pulses
use a duty cycle of 8:1 or 8/9, giving 3200 V.  But now we’re talking
about 8.9 μs on and 1.1 μs off.

So what’s the magnetizing inductance of our flyback core?  10 amps on
the output is 800 A (oof! car jumper cables!) on the input, but that’s
divided by our duty cycle to get 7200 A, which is the average value
our current must reach in its 220 μs, so a current slew rate of 7200 A
/ 220 μs = 32 MA/s, under an influence of only 5 V.  So the
magnetizing inductance must be 153 nH, and our switching MOSFET bank
needs to handle ten thousand amps.  ½LI² at 14400 A is 15.9 J, which
is going to be a pretty huge inductor.

Is that inductance a minimum or a maximum?  If the magnetizing
inductance is higher, the current will rise lower, and less energy
will be stored in the core, thus producing lower output and limiting
our welding power to a too-low value.  If the inductance is lower,
then instead we will produce more output power, if we can, unless we
saturate the core.  (Hmm, what does “if we can” look like?)

Then what happens with the high-frequency case?  With 153 nΗ, in 8.9μs
our 5 V can “only” raise the primary current from 0 to 291 A, which
limits out output high-frequency start current to 3.6 A, which is
grossly overkill.

Using two supplies should work
------------------------------

It would surely be better to use two separate flyback converters to
produce the high-voltage, high-frequency, low-current starter signal
and the low-voltage, low-frequency, high-current arc sustaining
supply.  They can be usefully separated by passive means to take
different circuit paths.  An inductor reaching 100 ohms (=ωL) at
100kHz would be 160 μH, and a capacitor reaching 100 ohms (=1/(ωC)) at
500 Hz would be 3.2 μF, so a “bias tee” that routed low-frequency “DC”
stuff to one flyback and high-frequency stuff to the other would be
very easy to build.  160 μH at 500 Hz is only 0.503 ohms, and 3.2 μF
at 100 kHz is similarly 0.497 ohms.

The low-voltage, high-current system probably ought to be powered from
mains power rather than from a 5-volt supply, using a voltage
step*down* flyback transformer.  50 volts at 10 amps is necessarily
500 watts, and delivering 500 watts from a 5-volt power supply is just
gonna suck.  Delivering 500 watts from a 240-VAC power supply is a
little tricky but highly doable.  Stepping it down to 50 volts or less
could be done simply with a stepdown transformer, but 50Hz
transformers are heavy; I think an H-bridge from the mains wires
across the primary of a high-frequency transformer would be a more
elegant approach that would easily permit the kinds of power and
polarity control I’m talking about here.

This can be done without the kinds of large energy-storage capacitors
needed by conventional switching power supplies, because it doesn’t
need to produce a constant ripple-free voltage; the H-bridge can also
operate at frequencies of around 100 kHz, with a fuse and a little bit
of filtering on the inputs and outputs, at just the cost of having an
annoying 100-Hz buzz in the arc.  A 500-watt power supply that has to
store 10 milliseconds’ worth of energy needs 5 joules of energy
storage; one that only has to store 10 microseconds’ worth needs 5
millijoules.

The high-voltage high-frequency starter supply could use a stepup
flyback as usual, or maybe a chain of two 16:1 stepups.  The flyback
part of it would operate at a 7:3 duty cycle: 7 μs on at 5 V, 3 μs off
at 0 V, which would produce 11.7 volts referred to the input, or 187 V
on the output.  The second stage 16:1 stepup transformer would then
raise this to 2995 V.  If this output is to be capable of delivering
10 mA, which may be rather a lot but is surely adequate, the first
input winding needs to handle 2.56 A average, 3.66 A average during
the 7 us, 7.3 A peak, which is an eminently straightforward thing to
achieve.  Magnetizing inductance can’t be more than 5 V 7 μs / 7.3 A =
4.79 μH.  ½LI² is 0.13 μJ.

### Microcontrollers ###

This seems like a waveform that would be easy to generate with an
Arduino or an ATTiny9.  3 μs is 48 cycles or 24-48 instructions at
16MHz even if you’re doing it in software; the ATTiny9 runs at 10MHz
and has a 16-bit PWM counter.  (Also the 61¢ [ATTiny4][0]: and the
40¢ [ATTiny5][1]: 12MHz, 256 instructions of Flash, 32 bytes of RAM.
The difference is that the ATTiny5 has an ADC and the ATTiny9 has 512
instructions of Flash.)  The transformers seem like they’d be easy to
wind; 2 or 3 turns on each primary, 32 or 48 turns on the secondary.
Putting an ac-coupling cap in between the MCU’s GPIO (or rather its
external buffer transistor or transistors) and the transformer would
keep the transformer from saturating.

Looking at AVRs, there’s a new (from 02018) “0-series” 46¢
[ATTiny202][5] with 20MHz, 1024 instructions of Flash, 128 bytes of
RAM, and a bunch of onboard peripherals including I²C (“TWI”),
master/slave SPI, two PWM channels, a 10-bit 115-ksps 6-input ADC, 6
GPIOs, and an FPGA-style 3-LUT logic cell (or two?).  Also it maps the
Flash into the data address space so you don’t need the special aptly
named LPM instruction to read it.

[0]: https://www.digikey.com/en/products/detail/microchip-technology/ATTINY4-MAHR/2271064
[1]: https://www.digikey.com/en/products/detail/microchip-technology/ATTINY5-TSHR/2238294
[5]: https://www.digikey.com/en/products/detail/microchip-technology/ATTINY202-SSN/9947534

### Winding transformers ###

[This coil inductance calculator][2] suggests that this low inductance
should be easily reachable with an air-core coil; for example, 3 turns
packed into 2 mm with a radius of 16 mm and a relative permeability of
1 should be about 4.55 μH.  But I think this may be inaptly using a
long-coil approximation formula μN²A/l which assumes Nagaoka’s
coefficient is 1.  [WP says][3] that for cases like this `L\approx
{\frac {\mu _{0}}{2\pi}}N^{2}\pi D\left[\ln \left({\frac
{D}{d}}\right)+\left(\ln 8-2\right)\right]+{\sqrt {\frac {\mu
_{0}}{2\pi }}}\;{\frac {ND}{d}}{\sqrt {\frac {\mu
_{\text{r}}}{2f\sigma }}}` but I have no idea what to make of that.
Low-frequency ferrites [have permeabilities in the 350-20000 range][4]
so any ferrite would instantly rocket us out of the microhenry range.
But without a core, how can we guide the flux through 48 windings of a
secondary?

[2]: https://www.allaboutcircuits.com/tools/coil-inductance-calculator/
[3]: https://en.wikipedia.org/wiki/Inductor#Inductance_formulas
[4]: https://en.wikipedia.org/wiki/Permeability_(electromagnetism)#Values_for_some_common_materials

10 amps in a transformer winding or something like that requires at
least 12-gauge wire, 2.1 mm in diameter, even though 16-gauge (1.3 mm)
would be fine for single conductors.

### Switching elements ###

Our peak wall voltages here are 340 volts.  If we’re H-bridging that
across the primary of our transformer, our switching elements need to
be able to handle that much voltage, and in either direction.  Common
high-voltage signal MOSFETs like the [57¢ BSS131][12] won’t cut it,
and not just because of the body diode; we need much larger switches
like the 82¢ [STS1NK60Z][13] (600V 0.25A), the obsolete 185¢
[STF5N52K3][14] (525V 4.4A), the 89¢ [STD2LN60K3][15] (600V 2A), the
63¢ [AOD1N60][16] (600V 1.3A), the obsolete 116¢ [STGB14NC60KT4][17]
(600V 25A), the obsolete RoHS-non-compliant 122¢ [STGD3NB60FT4][18]
(600V 6A), or the 847¢ [C3M0120065K][19] (650V 22A, SiC).  I think I
need 8 of these for a full H-bridge to deal with the body diodes,
which suddenly makes this seem a lot less appealing... maybe a
center-tapped winding with diodes down to both live and neutral, and
then I can get by with just two MOSFETs on the ends?  Or I could just
bridge-rectify the input, of course.

[12]: https://www.digikey.com/en/products/detail/infineon-technologies/BSS131H6327XTSA1/2783458
[13]: https://www.digikey.com/en/products/detail/stmicroelectronics/STS1NK60Z/1039725
[14]: https://www.digikey.com/en/products/detail/stmicroelectronics/STF5N52K3/2682995
[15]: https://www.digikey.com/en/products/detail/stmicroelectronics/STD2LN60K3/3711342
[16]: https://www.digikey.com/en/products/detail/alpha-omega-semiconductor-inc/AOD1N60/2353844
[17]: https://www.digikey.com/en/products/detail/stmicroelectronics/STGB14NC60KT4/1299900
[18]: https://www.digikey.com/en/products/detail/stmicroelectronics/STGD3NB60FT4/603475
[19]: https://www.digikey.com/en/products/detail/cree-wolfspeed/C3M0120065K/13906976

To get 500 watts out of 240 Vrms, I need only slightly over 2 A, and
that’s spread across two transistors.

Hmm, I wonder if this is some version of the “totem-pole PFC
topology”, though I’m not using it for PFC.  Or maybe the “phase-shift
full-bridge and LLC circuit”?
