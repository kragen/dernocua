Suppose you charlieplex blue LEDs on four pins ABCD of a
microcontroller.  So you have 6 pairs of lines AB, AC, AD, BC, BD, and
CD.  To light a forward LED you bring an earlier line high and a later
line low, and the voltage is below twice the threshold voltage, so
when you bring A high and C low, LED AC lights, but the LEDs AB and BC
(which you might suppose would supply a secondary current path) do not
exceed their threshold voltage and so do not light.

You can get 12 LEDs on 4 pins by charlieplexing by adding reverse LEDs
BA, CA, DA, CB, DB, and DC.

Consider LVDTs.  At the most basic level, an LVDT creates or destroys
an inductive coupling between two coils depending on the location of a
sensed element, typically a magnetic core.  The “L” means that the
coupling is linear in the position of the core, and the “D” means that
the way it is destroyed is by precisely balancing couplings in two
opposite directions.

Between these 12 current paths there can exist 66 pairwise inductive
couplings; in series with the AB LED we can have inductive elements
that couple that current path to current paths BA, AC, CA, AD, DA,
etc.  We can literally create these couplings by putting 11 LVDT
windings in series with each of the 12 LEDs.  But can we sense them
independently?

I think the answer is “not quite”.  If we bring A high and B low, then
we cannot sense voltages on those pins (unless we are using weak
pullups and pulldowns like those in the STM32).  But maybe if flowing
20 mA from A to B causes C to be pulled up or down from either A or B,
we can detect this, and likewise for D.  Moreover if the induced
voltage is at some point predictably less than the voltage being
applied across A and B, as it surely will be if the AB current tends
toward an asymptote, we can distinguish C being pulled up from A
(which will be limited by the input protection diodes to 3.9 volts or
so) from C being pulled up from B (which might be, say, 1.5 volts).
So that gives us 12 keys: two for each of our 12 current paths, but
each key appears twice, since the coupling between an AB winding and
an AD winding will appear both as an AD voltage on an AB current pulse
and an AB voltage on an AD current pulse.  Maybe you can increase this
further with different polarities and coupling strengths, although
that would seem to eliminate the possibility of using continuously
varying coupling strengths to, in effect, charlieplex analog sensors.

If C is being pulled up or down from D, this may be more difficult to
distinguish if both C and D are floating.  We might have 1.5 volts of
difference between the two, but does that mean C is at 0 and D is at
1.5 volts, or that C is at 1.8 and D is at 3.3?  This is maybe
complicated by diode blocking.  But maybe twiddling weak pullups and
pulldowns at C and/or D can distinguish.

Unlike just charlieplexing a switch in series with each LED, this
approach allows you to use the LEDs independently for output.

With five pins the picture is rosier still: instead of 12 current
paths we have 20, and each of those 20 can be sensed on any of 3 other
pins, for a total of 30 keys.  Or maybe each of those 20 current paths
can be usefully coupled to any of 18 others, and we can distinguish
all of them, in which case you have 180 keys.
