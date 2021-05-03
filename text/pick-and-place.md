JiaLiChuang PCB will fab ten tiny prototype boards for you for US$2.
They also offer a service where they will stuff the board for you with
certain components, ones from LCSC’s “LCSC assembled” list, which has
about 30k components.  I have a couple of questions about this:

1. How much does it cost?
2. What are the parts most suitable for building a CPU?
3. How big would such a CPU be?

[Electronoobs reports][0] on his experience.  He was paying €0.0035
and €0.0097 for precision 0805 resistors, €0.0559 for large bright
blue LEDs, €0.0530 for his WS2811 LED drivers, etc., *all* of which
were “extended” parts; and €0.0031 for some 0805 180Ω 1% resistors,
€0.0670 for some SOT-23 P-MOSFETs (AO3401A), and €0.0155 for some
0.1μF X7R 50V 0805 caps, which were selected from among their 689
“basic” components that don’t require a US$3 per-component-type fee.
However, I guess JLCPCB was paying him to pay them.  He was building
30 7-segment displays with 57 LEDs on them, 80 components total, for
about US$2.90 each (€79.30 or US$85 for 30 PCBs is US$2.83⅓ each),
controlled by some WS2811 8-SOICs.  They were 2-layer boards with
plated-through vias.

He reports that the stuffing service only supports SMD, and only on
one side, and only for 2-layer and 4-layer green boards.  Apparently
since then [JLCPCB has added][1] 6-layer and some other colors of
solder mask.

[0]: https://electronoobs.com/eng_circuitos_tut41.php
[1]: https://jlcpcb.com/smt-assembly

Roughly estimating, 10,000 SOT23 transistors would be enough for a
CPU, which would be 100×100 transistors.  You could maybe bit-slice a
CPU across multiple boards, since I think JLC has a minimum of 5 or 10
boards per prototype order.

[There’s a third-party parametric search engine][2] for the parts
library, which has a [cached zip file of JSON][3] listing the parts,
which is 260 mebibytes.

[3]: https://yaqwsx.github.io/jlcparts/data/cache.zip

[2]: https://github.com/yaqwsx/jlcparts

So, what do the 689 “basic” parts include?
------------------------------------------

Most of the parts are not in stock at any given time, a common source
of frustration among forum posters.

Roughly half the “basic” parts are resistors.  Some of these are very
small; the 0.34¢ Uniroyal 4D02WGJ0102TCE is an array of four 1kΩ 5%
resistors in a 1 mm × 2 mm package, which I guess is twice the size of
an 0402.  That brings the cost per resistor down to 0.085¢, plus 0.3¢
for soldering.  10kΩ, 4.7kΩ, 470Ω, and 33Ω are also available in this
form, or 4 in an 0603 (0.43¢ or maybe 0.38¢).  Other denominations
included in small form factors include 4.7MΩ, 2.2MΩ, 1.5MΩ, 1.2MΩ,
1MΩ, 620kΩ, 300kΩ, 270kΩ, 100kΩ, 75kΩ, 49.9kΩ, 40.2kΩ, 24kΩ, 22kΩ,
8.2kΩ, 6.8kΩ, 6.2kΩ, 5.6kΩ, 5.1kΩ, 4.3kΩ, 3.9kΩ, 2.2kΩ, 1.2kΩ, 1kΩ,
750Ω, 680Ω, 360Ω, 330Ω, 300Ω, 240Ω, 120Ω, 100Ω, 75Ω, 56Ω, 33Ω, 22Ω,
10Ω, 2.2Ω, 1Ω, etc.; these are about 0.3¢ for (rare) 1206s (¼W!), 0.2¢
for 0805s, 0.1¢ for (rare) 0603s, or 0.05¢ for 0402s, and ±1% is
typical tolerance.  This means the discrete 0402s are actually
*cheaper* than the resistors in the arrays (usually) but take up twice
as much space.

Much of the remainder is MLCCs: roughly 1.3¢ for a 1206, whether C0G,
Y5V, or X7R, 0.4¢ for an 0603, or 0.1¢ for an 0402.  With MLCCs
there's a tradeoff between size, voltage, capacitance, and precision.

In logic and quasi-logic, we have the 555 timer (7.58¢); the 74HC244
octal tristate buffer (12.87¢); the 74HC14 hex inverting Schmitt
trigger (7.64¢); the 74HC04 hex inverter (9.11¢); the 8-bit 74HC164
serial-to-parallel (9.04¢) and 74HC165 parallel-to-serial (10.1¢)
shift registers, as well as the 8-bit (?) 74HC595 serial-to-parallel
latched-output shift register (10.84¢); the 74HC08 quad AND gate
(9.85¢); the 74HC138 3-to-8 decoder (9.15¢); the 8-channel analog
mux/demuxers CD4051 (15.01¢), CD4052 (14.56¢), and CD4053 (14.35¢);
the 74HC573 tristate octal transparent latch (22.14¢); the 74LVC4245
tristating bidi 3–5 volt octal level shifter (32.46¢); and the 74HC245
tristating bidi octal buffer (18.13¢).

I think the combination of a 74164 and a CD4051 gives you an async
3-LUT for 24.05¢ plus 4.5¢ for assembly (14 74164 pins and 16 CD4051
pins), 28.55¢ total: you shift your LUT bits into the 74164 and feed
them into the CD4051’s 8 inputs, then drive its channel-select inputs
from the logic signals you actually want to compute on.  If one of
your logic signals is available in inverted form as well, you can gang
together two such combos (wiring the CD4051 outputs together and
connecting the fourth logic input to INH on one CD4051 and inverted to
INH on the other) to get a 4-input LUT.

Even with a decoder, the 74244 would not work for this because it only
has two output enable pins, controlling four bits each; the 74573 only
has one.

There’s also the 7-darlington 16-pin ULN2003 (13.64¢ + 2.4¢ assembly =
16.04¢) and the 18-pin 8-darlington ULN2803 (50.32¢), so the ULN2003
costs 2.29¢ per transistor as long as you don’t mind all the emitters
being tied together.  Discrete transistors cost less, though: a
SOT-23-3 P-MOSFET like the Leshan Radio Company LBSS84LT1G is 1.34¢
(+0.45¢ assembly), and the Changjiang Electronics Tech SOT-23-3 2N7002
(a N-MOSFET, of course) is 1.23¢ (+0.45¢).  Bipolar transistors are
even cheaper — the SOT-89-3 PNP B772 from Changjiang is 5.38¢
(+0.45¢), but the SOT-23-3 Changjiang NPN S9013 is only 1.13¢ (+0.45¢)
or possibly 0.929¢?, and its complementary PNP S9012 is 1.16¢ or maybe
0.891¢, and their PNP S9015 is only 0.98¢ (+0.45¢) or 0.909¢, and the
CJ MMBT3904 NPN is 0.87¢ (+0.45¢) or 0.682¢.

SOT-23 seems to be the smallest discrete transistor they have in
“basic”.  SOT-89 is a bit larger, 4.5 mm × 4.1 mm.

The ULN2003 is packaged in an SOIC-16, which is 10 mm × 6 mm, which
works out to 8.57 mm² per transistor, very nearly the same as an
SOT-23 per transistor.

No connectors at all are included among “basic” parts.

They do have LEDs among “basic” parts: 1.63¢ for yellow 0603s, 1.54¢
(or maybe 0.909¢?) for red 0805s, 1.82¢ for green, 1.1¢ for blue
0603s, 0.75¢ or 0.57¢ for blue 0805s, and 0.78¢ or 0.56¢ for white
0805s.  This suggests a price of around US$20 per kilopixel if you’re
into that kind of thing.

10ppm SMD 8MHz crystals are 22.78¢ or maybe 18.27¢ in quantity 1 in an
“SMD-5032_2P” package.

Power diodes cost 0.5¢, Schottkys 2.15¢ (or maybe 1.32¢), zeners 1.35¢
(or maybe 0.96¢) (5.6V and 3.3V only), fast recovery rectifiers 0.74¢
or maybe 0.6¢, 1N4148Ws 0.78¢ (or maybe 0.77¢), and 5.8V TVSs 2.91¢
(or maybe 2.94¢).

CPU size estimation
-------------------

If we estimate a basic CPU as being 1000 gates, evenly split between
AND and NOT, that would be 84 74HC14s in and 125 74HC08s, all in
SOIC-14s.  An SOIC-14 is 6 mm × 8.6 mm, so these chip packages alone
would be 10784 mm², about 100 mm × 100 mm, or 1078 mm² on each of 10
boards, 33 mm square.  I think the parts would cost US$8.82 for the
74HC14s, US$9.00 for the 74HC08s, plus US$4.39 to solder the 2926
joints, for a total of US$22.21.  In practice you’d need about twice
that much space, and of course you’d have registers and things in
there too.

If we estimate a basic CPU as being 500 3-LUTs, that’s 500 74164s (in
SOIC-14) and 500 CD4051s (in SOIC-16), which would be US$142.75.  An
SOIC-16 is 60 mm² so this is (51.6 + 60) × 500 = 55800 mm².  If
divided into 10 square boards, each would be 75 mm square, or more
realistically a bit bigger than that.

If we estimate a basic CPU as being 10,000 transistors, each with two
resistors, each SOT-23 transistor is about 3 mm × 3 mm, and each 0402
resistor is 1.0 mm × 0.5 mm, for a total of 10 mm² per
transistor-plus-resistors.  This would give us a total of 100000 mm²
or 10 100 mm × 100 mm boards.  If the transistors are half 2N7002s
(1.23¢) and half LBSS84LT1Gs (1.34¢) and the resistors all cost 0.05¢,
then we have US$10 for 20,000 resistors, US$61.50 for 5000 2N7002s,
US$67 for 5000 LBSS84LT1Gs, and US$105 for all the SMD soldering, for
a total of US$243.50.

All of the above omits the costs of things like voltage regulation and
bypass capacitors, but I think those would probably be a minority;
also it omits the cost of the PCB fabrication itself.

Conclusions
-----------

SSI random logic chips are probably the most suitable way to build
such a CPU, which would probably cost under US$50 through JLCPCB’s
service and be less than 150 mm square; if it’s 16 layers thick, it
should fit into a 40 mm cube.  Some hand-soldering will be needed to
connect multiple boards together.
