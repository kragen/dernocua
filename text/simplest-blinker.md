There are lots of LED blinker circuits around, most driven by a 555 or
a transistor-based astable multivibrator.  But there are enormously
simpler options.

In some sense the simplest LED blinker is two red LEDs in antiseries,
in parallel with a capacitor and resistor, in series with another
resistor, powered by a voltage around 9–48 V.  That is, 
9V-R1-(->|-|<- || R2-C)-GND.  When the reverse-biased LED goes into
[avalanche discharge][0] at *Vbr*, around 5 V, the capacitor discharges
down to the minimal voltage necessary to sustain avalanche conduction
in the backward-biased LED, after subtracting the forward voltage drop
of the forward-biased LED, and with time constant *R*₂*C*, with a
pulse energy ½*Vbr*²*C*, lighting the forward-biased LED.  When the
current drops too low to sustain avalanche conduction, the
reverse-biased LED begins to block again, and the capacitor recharges
toward the power supply voltage with time constant (*R*₁ + *R*₂)*C*.

[0]: https://www.infineon.com/dgdl/Infineon-ApplicationNote_Some_key_facts_about_avalanche-AN-v01_00-EN.pdf?fileId=5546d462584d1d4a0158ba0210977cde

(*Most* reverse-biased PN junctions have that kind of bistable
avalanche behavior, and it’s an annoying source of noise when using
avalanche diodes as voltage references, but not all.  Note that the
plots in Infineon’s appnote linked above do not exhibit this
bistability; it is the source of MOS latchup.  You could probably
force such recalcitrant circuits into oscillation with sufficient
series inductance: 9V-R1-L-(->|-|<- || R2-C)-GND.)

This is very similar to the basic neon lamp flasher, except for the R2
current-limiting resistor (which may not be necessary!), the lower
voltage, the potentially much higher speed, and the complication that
the LED that provides the circuit’s bistability doesn’t light
(avalanche-mode LEDs do emit, but at two orders of magnitude lower
radiative efficiency), so a second LED is needed.

In theory you could make R1 small enough that the LED would just stay
lit until the avalanching LED burned out, but that seems unlikely in
practice.  And in theory you could leave out R2 and allow the LED to
set its own current, since the energy of the pulse will be limited to
the energy stored in the capacitor, but even arbitrarily short high
currents can damage semiconductors through non-thermal damage
mechanisms, so it might be better to leave it in.

Let’s calculate some values so that this circuit is likely to flash
visibly.  The current through the LEDs should probably be around 20 mA
to be brightly visible without much risk of damage, and I think the
reverse voltage drop of an avalanching LED is pretty small, maybe
around 1 volt.  The forward voltage drop of the illuminated LED should
be around 1.6 V, so we have about 5 - 1 - 1.6 = 2.4 volts across R2,
which means something like 100Ω is appropriate, which would give us
24 mA.  Let’s shoot for about 1 Hz overall repetition rate.  I suspect
that even 1% duty cycle (10 ms) would be bright enough to be visible,
but let’s shoot for 50 ms (5%) to be safe.

At this point I realize I don’t have any idea how much current is
necessary to maintain avalanche conduction.  If I pretend that the
avalanche sustaining voltage and the LED forward voltage drop are
constant with respect to current, and any amount of current is
sufficient to sustain the avalanche, the result is that the capacitor
voltage asymptotically approaches the 1 + 1.6 = 2.6 V and never
reaches it, and the circuit never turns off, so this is not a useful
approximation.  I’m sadder but no wiser after reading a couple of
application notes about avalanche breakdown.

So, just guessing, maybe you need four RC time constants (54× lower
current) to turn off.  50 ms ÷ 100Ω = 500 μF, so a 470 μF electrolytic
ought to work.  Then we just need to set R₁ to get an off-time of
around a second.

The off-time is determined by the time to charge from the avalanche
cutoff voltage (plus the forward-biased LED’s voltage drop) up to the
breakdown voltage on its way up to the source voltage: from 2.6 V up
to 5.0 V out of 9.0 V, which is to say, the remaining voltage should
drop from 6.4 V to 4.0 V, a factor of 0.625, about √*e*, so half a
time constant.  Thus a time constant of about two seconds would be
right, which works out to about 4.3 kΩ, so a 4.7kΩ resistor ought to
work.

The visual brightness of the LED should mostly depend on how much
charge goes through it, not how long it takes.  If we were going to
discharge 2.4 volts out of a 470 μF electrolytic at a constant 20 mA,
it would take about 56 ms, which is plenty long enough to see the LED
flash.  So I think probably the LED flashing will be visible.  The
energy of each flash is about 2.3 mJ, about half dissipated in the
resistor, with the other half split almost equally between the two
LEDs, so it’s unlikely that the LEDs will be damaged by heating.

The reverse-biased capacitance of the LED is down in the picofarads,
so the stored energy is in the dozens of picojoules, insufficient to
damage it much.

So the final circuit is:

    9V-4k7-(->|[red LED]-|<[red LED]-||100Ω-470μF)-GND

*****

Such a circuit is sensitive to every electronically relevant aspect of
its environment: temperature, voltage, light, EMI, and radioactivity.
Its off-time is inversely proportional to the difference between the
input voltage and the turn-off voltage, though its on-time varies
little with that.  The avalanche breakdown voltage increases with
temperature (Infineon’s appnote above says that in silicon MOS it
varies about 5% per 100°), so its both its off-time and its on-time
would increase with temperature; but the threshold voltage of the
forward-biased diode also changes with temperature, and I think that
voltage *decreases*, which may have a larger effect on the on-time
(though it isn’t immediately obvious to me which way).  Both diodes
are photosensitive, so the circuit can be triggered with a flash of
light, and its frequency will vary with the ambient light level.  EMI
can also advance the timing of the oscillator, so under some
circumstances it can phase-lock to weak signals coupled in
capacitively or inductively; but even in the absence of EMI, avalanche
breakdown is somewhat random, perhaps because it detects radioactive
decay as well.

An interesting question is whether this sort of behavior is useful for
anything.  Of course, if you can mostly isolate the circuit from
variations in voltage, light, EMI, and radioactivity, you can use it
to measure temperature; if you can mostly isolate it from variations
in temperature, voltage, EMI, and radioactivity, you can use it to
measure light; etc.  But digital logic seems potentially more
interesting.

In file `micro-marx.md` I’ve argued that such triggerable oscillators
can be used as clocked logic elements.  With ordinary LEDs you ought
to be able to get up into the MHz, but with avalanche diodes built on
an IC, tens of GHz ought to be attainable.  Large resistances or
capacitances on chip require large areas, but by running with a supply
rail closer to the breakdown voltage and increasing the duty cycle
from 5% up to maybe 20%, you ought to be able to use equal or nearly
equal resistances for R1 and R2, so neither needs to be particularly
large.  On chip it might be reasonable to use C ≈ 20 fF, R1 ≈ R2 ≈
2kΩ, with a frequency around 10 GHz.

Why would you use this kind of dynamic logic instead of regular CMOS?
As I understand it, a regular CMOS flip-flop needs 6 (or 8)
transistors, and a CMOS NAND gate requires 4.  Such an oscillator
requires a capacitor, two diode-connected transistors, and two
resistors, so it might permit higher density than regular CMOS, but be
less power-hungry than four-phase logic (see file `snap-logic-ii.md`).
(But really that's not attacking the crucial aspect of CMOS density,
which is routing.)
