I was looking at power transistors to use to control a load of some
tens of watts (a tiny arc furnace) from a microcontroller, driving a
couple of flybacks with something like 10 amps at 5 volts at a few
kHz.  But obviously the microcontroller can’t drive 10 amps, so you
need a high-power buffer, and it should probably be a transistor.

What buffer transistors would you want to use?

MOSFETs
-------

In MOSFET-land, a pricey power MOSFET like an IRF540N is one option
when you need low on-resistance; (0.044 ohms, 33 A, Vds up to 100,
145¢); another would be a parallel pair of IRLML6344s (0.029 ohms, 5 A
each, 30 V, 36¢).

An interesting figure here is the expected load impedance.  An IRF540N
can control a 3300-watt load, but if it’s resistive, that load has to
be 3 ohms.  If the load is 10 ohms, at 100 volts it can only draw 10
A, and so it’s only 1000 watts.  Similarly, if the load is 1 ohm, we
can only use voltages up to 33 V, and so it can only be 1089 watts.
So even though the actual impedance of the IRF540N is only 0.044 ohms,
from the point of view of efficient power transfer, it’s kind of like
a power supply with a 3-ohm internal impedance.  I’ll call this the
“virtual impedance”.

In general if the virtual impedance is too low, you can stack up
multiple switches in series to get the voltage you want.  It may be
inconvenient but it’s probably not that bad.  But if it’s too *high*
you may be in for trouble; BJTs need a lot of ballast to avoid current
hogging.

Because you can parallel MOSFETs, too high a virtual impedance figure
is less of a concern; paralleling them drops your virtual impedance
just like it drops real impedance.  So one IRLML6344 has “6 ohms” of
virtual impedance, but two in parallel have “1.5 ohms”, and four have
“0.75 ohms”.

The modern choice would probably be a GaN FET like the EPC2036.  Damn,
those things are sweet.  100 V, 1 A, 0.065 ohms, and only 0.91
nanocoulombs of Qg, compared to the IRF540N’s 71 nC and the
IRLML6344’s 6.8.  And its threshold voltage is lower, too.  So you can
switch it on or off much faster and with less energy.  The
245¢ [EPC2016C][25] is 100 V, 18 A.

[25]: https://www.digikey.com/en/products/detail/epc/EPC2016C/5031689

TIP120s are too voltage-greedy 
------------------------------

You can’t use a TIP120 darlington for this kind of thing; though it
can deal with 60 V, 5 A continuous, 8 A peak, its saturation Vce is 4
volts at 5 amps, so it would eat basically all the power you were
trying to feed the transformer.

60 V / 5 A is a virtual impedance of 12 ohms.

Other bipolars
--------------

So are there bipolars that would work better?

Digi-Key suggests the 55¢ [2STN1550][6], the 141¢ [MJB41CT4G][7], the
232¢ [MD2001FX][8], the obsolete 21¢ [2SD23210RA][9], or the obsolete
32¢ [2SD250400A][10].

[6]: https://www.digikey.com/en/products/detail/stmicroelectronics/2STN1550/2122365
[7]: https://www.digikey.com/en/products/detail/onsemi/MJB41CT4G/1481723
[8]: https://www.digikey.com/en/products/detail/stmicroelectronics/MD2001FX/2043597
[9]: https://www.digikey.com/en/products/detail/panasonic-electronic-components/2SD23210RA/972467
[10]: https://www.digikey.com/en/products/detail/panasonic-electronic-components/2SD250400A/972471

### 21¢ 2SD2321 ###

Starting with the cheapest, the 21¢ Panasonic 2SD2321 can switch 5 A
(8 A peak) at up to 20 V with a beta of at least 150 at 2 A and a
typical saturation Vce of 0.28 V when you’re running it at 3 A,
zooming up to 1 V at 8 A or so.  It has a 150MHz “transition
frequency”, which I think means its beta is guaranteed to be not more
than 15 if you’re running it at 10 MHz.

20 V / 5 A is a virtual impedance of 4 ohms.

So, you could feed it 40 mA through a 120-ohm base resistor from a
microcontroller GPIO pin, grounding the emitter, and running the
flyback primary winding through it from 5V.  The current through the
coil starts to climb, and keeps climbing until we turn off the
transistor, at which point the current leaps to the secondary and
energizes the arc.  If we don’t buffer it further we probably won’t
get more than 6 amps out of it.  But then it’s dropping a whole volt,
so it’s dissipating 6 watts, briefly exceeding its 0.4 watt rating 15
times over.  And it probably spends a fair bit of time dissipating
more than half that.  So it’s probably going to overheat in its little
bitty NS-B1 TO-92-like package.

But, even before that, quite likely at 5 V 2 A we drive the poor
little transistor into second breakdown.

The max you could theoretically switch with this transistor, if second
breakdown wasn’t a consideration, is 100 W.  In a flyback setup you
won’t get more than 40 W; the flyback waveform is an interrupted
sawtooth, so its RMS value is half of its mean value, a quarter of its
peak value of 160 W.  With a 5 V supply, though, you’ll be lucky to
control 10 W with it.  And because of its lousy power dissipation you
can only control a tiny fraction of that continuously.

### 32¢ 2SD2504 ###

This is slightly more promising, specced to switch 5 A (9 A peak) at
up to 10 volts, and dissipate 750 mW from its TO-92-B1.  But its
saturated Vce crosses 1 V at only 4 A; at 8 A it’s up to 2 V (and thus
16 W).  So it’s just going to dissipate way too much power for this,
even if it doesn’t hit second breakdown (Panasonic forgot to include
the safe-operating-region plot in the datasheet this time).

10 V / 5 A is a virtual impedance of 2 ohms.

### 55¢ 2STN1550 ###

This is a little bitty surface-mount SOT-223, which entitles it to
dissipate 1.6 watts, and it’s rated to switch up to 5 A (10 A peak) at
up to 50 V; at 5 A 5 V it says its (non-small-signal) beta is
typically 95, so you’d need 53 mA to avoid saturating, which is a bit
much to ask from a microcontroller.  It turns on in 90 ns and off in
700 ns, so you can switch efficiently at near-MHz rates.

50 V / 5 A is a virtual impedance of 10 ohms.

ST omits the performance curve plots entirely, as it turns out, only
specifying a 0.26 V saturated Vce at 3 A.

I feel like this transistor would probably work in a 12V system!  But
in a 5V system we’re just asking too much current from it.  Say we can
drive its base with another transistor so we don’t have to worry about
the 40 mA limit on AVR pins.  5 amps at 5 volts is a peak of 25 watts;
in a flyback setup we can never get more than half of that, since if
the *mean* current of the sawtooth is 5 amps, its *RMS* current is
only half of that.  So we’re talking about 12.5 watts, which is not
much of an arc furnace.  If we were using 12 volts, though, we could
do 30 watts with a switch like this.

I don’t know, I think we’d need to go for something a lot beefier to
get hundreds of watts of power into our stepdown flyback arc power
supply.

### 141¢ MJB41CT4G ###

This is a TO-263-3 surface-mount version of the TIP41 power
transistor, specced to switch 6 A (10 A peak) at *100* volts, but with
a beta of only 15 and a transition frequency of only 3 MHz (which the
onsemi datasheet helpfully explains *is* the gain-bandwidth product),
which limitations would be fine for this application.  You’d have to
use some kind of a driver circuit to drive its base: another
transistor, a step-down pulse transformer, something.

100 V / 6 A is a virtual impedance of 17 ohms.

It’s rated both for 2 watts and 65 watts dissipation, depending on
whether you’re holding the case or the ambient air at 25°.  The
junction temperature max is 150°, junction-to-case thermal resistance
is 1.92°/W, and junction-to-ambient thermal resistance of 62.5°/W (or
50°/W “when surface-mounted to an FR-4 board using the minimum
recommended pad size”).  If you divide 150°-25° by 1.92°/W you get the
65-watt number, while 62.5°/W gives you the 2-watt number.  So if you
heatsink this guy well enough, you could dissipate tens of watts.

It says its saturated Vce is 1.5 V at 6 A, which would be 9 watts, so
that’s really all the heatsinking it needs if you’re using it as a
switch.  At 5 volts it would be grossly inefficient, controlling a 3.5
V 6 A (21 watt) load at a cost of 9 watts.  But if it were
controlling, say, a 70-volt load, it might be fine.

### 232¢ MD2001FX ###

This is a monster 700-volt bipolar 12-amp (18-amp peak) 58-watt NPN
BJT, marketed as “High voltage NPN power transistor for standard
definition CRT display”!  It’s a transistor specifically designed for
the horizontal deflection output for a CRT, but astonishingly it’s not
marked as “obsolete” and it was only introduced in 02007.  Its beta is
only 4.5, and it’s sloow, 2.6 microseconds storage time.

700 V / 12 A is a virtual impedance of 58 ohms.

Triacs
------

Suppose you connect the flyback primary between the positive power
rail and a capacitor to ground and put a triac (or just an SCR) across
the capacitor.  Initially when you plug it in there will be a flyback
pulse as the capacitor charges up, to twice the input power rail, I
think, but then when the cap starts to discharge, the flyback
secondary’s diode will go forward-biased and rapidly drain most of the
energy out of the circuit, so fairly rapidly the cap will be charged
to the power rail voltage, and everything will be quiescent.  But if
you tickle the SCR gate, the cap dumps to ground and the whole cycle
starts again.  You can control the amount of power delivered to the
output by doing this more or less often.  A triggered spark gap could
maybe substitute for the triac in a pinch.  I mean basically this is
just a Tesla coil.

This doesn’t seem like it is going to be very efficient, but it would
definitely work.

I am going to assume that the 46¢ Ween (formerly NXP, formerly
Philips) [Z0109MN0][11] is a typical triac.  It’s an SOT223
four-quadrant triac that starts passing 1 A at 600 V (dropping 1.3 V)
if you tickle its gate with 1 V and 10 mA, until the current drops
below 10 mA (or maybe 30 mA?).

[11]: https://www.digikey.com/en/products/detail/ween-semiconductors/Z0109MN0-135/2780441

600 V / 1 A is a virtual impedance of 600 ohms.
