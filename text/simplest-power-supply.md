Watching [BigClive’s air “freshener” teardown][0] I was surprised to
see an even simpler DC power supply for a microcontroller from the
powerline than I’d seen previously, but it turns out that it’s only
cheaper for microcontrollers dissipating less than about 25 mW.

In the air freshener it consists of two 15K resistors in series, fed
from the powerline by a fuse and a diode used as a half-wave rectifier
(two diodes in series actually), across a 5V zener and a 100
microfarad 16-volt electrolytic storage cap, bypassed with a ceramic
capacitor for high frequencies.  There is no galvanic isolation.

[0]: https://youtu.be/3cm9AO0qD7k

I think this is even cheaper and simpler than a capacitor dropper:
fuse (in the air-freshener case, shared with the line-voltage heating
elements), resistor, diode, zener, and the two caps, six components in
all, and you have your 5 volts out.  It’s extremely inefficient (maybe
2% efficient), but that’s nearly irrelevant at the power levels it’s
cheaper for; it isn’t very important if it’s wasting 0.1-1 W.

You could cut it to five components if you used a fusible resistor, of
which [Digi-Key has 140 in stock][1], like the US$0.05 [Vishay
NFR25H0001001JR500][2], a half-watt “flameproof” 1-kilohm jobbie.  But
how much resistance do we need, and how much power does the resistor
need to dissipate?

[1]: https://www.digikey.com/en/products/filter/through-hole-resistors/53?s=N4IgjCBcoKxaBjKAzAhgGwM4FMA0IB7KAbRAGYAWAdhiqpH0pqoA4HzraBOdpmLnowoCWAJl7CuLChJFlZUuAF18ABwAuUEAGV1AJwCWAOwDmIAL74AtD2ggkkfQFc8hEuBBLLIK%2BLsPnVyJIUmVzcKA
[2]: https://www.digikey.com/en/products/detail/vishay-beyschlag-draloric-bc-components/NFR25H0001001JR500/614119

Suppose the microcontroller draws no more than 10 mA (50 mW), and
you’re designing for a 240VAC environment.  Your rectum-fried DC will
peak at 340V, but what’s more important here is probably the RMS
voltage, which is actually only 120V with half-wave rectification, and
the mean voltage, since we want the mean charging current to be 10 mA.
The mean of an ideally half-wave rectified signal is about 0.318 of
its peak, about 108 V in this case, so we’d need no more than 10.8
kilohms of series charging resistance; lower resistance would be fine
but would produce more waste heat, so 4.7k might be better.  With 4.7k
you get 23 mA average current, 26 mA RMS current, and thus 3.2 watts
of power burned in the resistor.  That’s a curtain-burner!

So you need maybe a 5-watt resistor.  These are off-the-shelf parts
like the [Vishay AC05000004701JAC00][3], but they’re quite a bit more
costly; that one costs 71¢, while the 45¢ [TE RR03J5K6TB][4] would
almost work at 5.6kilohm and a 3-watt power rating.  And, perhaps
unsurprisingly, none of the resistors Digi-Key lists in that power
range claim to be “fusible”.

[3]: https://www.digikey.com/en/products/detail/vishay-beyschlag-draloric-bc-components/AC05000004701JAC00/596732
[4]: https://www.digikey.com/en/products/detail/te-connectivity-passive-product/RR03J5K6TB/9371876

Evidently this simplification is only economical for microcontrollers
using significantly less power than that, because using a capacitor to
drop that voltage instead would be cheaper.  The air-freshener circuit
being dissected used 30 kilohms instead of 4.7 or 10, so evidently its
microcontroller needs 3 mA or less.  Accordingly the resistor’s power
is only half a watt, and that’s distributed over two resistors, which
I think are sized for half a watt each, and are located a substantial
distance apart on the board, perhaps with the objective of avoiding a
concentration of heat.

The voltage across the dropper resistor is effectively the whole
half-wave rectified power supply voltage, so the power it dissipates
is linearly proportional to the current: 3.2 W at 23 mA (4.7 kilohms),
but 0.32 W at 2.3 mA (47 kilohms), and 0.03 W at 0.23 mA (470
kilohms).  There’s actually a lot you can do even at 0.23 mA.

At 10 mA the 100 microfarad capacitor would also be too small. Because
of the half-wave rectification, there’s a dead time of just over 10 ms
when there’s no current charging up the cap, and in that time, it
would drop from 4.9 V to 3.9 V.  So 100 microfarads is adequate for
maybe a 4 mA sustained current draw.  But at a lower power level, like
0.23 mA, 10 microfarads is likely enough.

So here’s a parts list for a 5V 0.23 mA power supply:

* Dropper resistor: 470 kilohms, >0.03 W: [Yageo CFR-12JR-52-470K][4]
  (0.97¢, 170 mW) or [TE CRGCQ0402F470K][5] (0.28¢, 63 mW, SMD 0402,
  would need potting for creepage because max working voltage is
  nominally only 50V because of the 0402 package).
* Diode: a 1N4004 or 1N4005 from, say, [Micro Commercial Co.][6]
  (2.2¢, 400V, 1A).
* Zener: something like the [Nexperia BZX84-C5V1-235][7] (1.96¢, 5.1V,
  250mW).
* Electrolytic: something like the [Würth 860020372001][8] (5.4¢, 16V,
  10 microfarads ±20%, 35 mA max ripple, 5mm diameter, 12.5mm long)
* Ceramic cap: maybe a [Samsung CL05A104KA5NNNC][9] (0.22¢, 25V, 100
  nF, X5R SMD 0402)
  
That gives us a total bill of materials of 10.75¢, almost exactly half
being the electrolytic.  At such low currents, it might be feasible to
replace both the electrolytic and the ceramic with a ceramic like the
[0805 Samsung CL21A106MQFNNNE][10], which is 10 microfarads, rated for
6.3 volts, and costs 1.9¢, which would drop the BOM cost to 7¢.

[4]: https://www.digikey.com/en/products/detail/yageo/CFR-12JR-52-470K/17719
[5]: https://www.digikey.com/en/products/detail/te-connectivity-passive-product/CRGCQ0402F470K/8576261
[6]: https://www.digikey.com/en/products/detail/micro-commercial-co/1N4004-TP/773641
[7]: https://www.digikey.com/en/products/detail/nexperia-usa-inc/BZX84-C5V1-235/1156102
[8]: https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/860020372001/5728733
[9]: https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL05A104KA5NNNC/3886701
[10]: https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL21A106MQFNNNE/3886956

The fuse is essential for safety in case the rest of the apparatus
fails short, but it’s potentially just a piece of wire that’s free to
melt without setting anything on fire.  The cheapest off-the-shelf
fuse is something like the [Eaton C310T-SC-4-R-TR1][11], which costs
14¢, twice the cost of the whole power supply.  PowerStream’s [fuse
wire chart][12] suggest that 40-gauge copper wire (79 microns
diameter) should fuse at 1.8 amps, and anything 28-gauge or smaller
(320 microns diameter) should fuse below 15 amps, which is low enough
to keep a house circuit breaker from blowing.

Using 58 megasiemens per meter as copper’s conductivity, 79-micron
diameter wire (0.0049 square mm) gives you 3.5 ohms per meter.  At 1.8
amps, that’s 11.4 W/m, or 11.4 mW/mm, and so at 0.0049 mm³/mm we have
2.3 W/mm³.  Copper is about 9 mg/mm³ so that’s about 2300 W/mg, which
does seem like the kind of power that tends to melt metal.

[11]: https://www.digikey.com/en/products/detail/eaton-electronics-division/C310T-SC-4-R-TR1/5420163
[12]: https://www.powerstream.com/wire-fusing-currents.htm

Because we have about a factor of 8000 between the fusing current and
the normal working current, it should be easy to provide enough
insulation to permit fusing without causing the fuse wire to go into
thermal runaway under normal loads.

A few millimeters of such thin wire (far enough for safe creepage
allowances at 240VAC RMS) in an environment that won’t catch on fire
if the wire melts would be a perfectly adequate fuse.
