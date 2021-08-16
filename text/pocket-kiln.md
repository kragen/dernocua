As mentioned in file `material-observations.md`, my experiments on
materials are limited by needing a kiln that can maintain a
reproducible temperature somewhere in the 500°–1500° range for
probably considerably longer than 20 minutes.

The thermal aspect of this seems like an eminently feasible thing to
do with the intumescent refractory recipes explored above: I can mix
up some intumescent mix, maybe with a bunch of vermiculite filler,
mold it to a rough shape, and heat it with the torch enough to get it
to bubble up; then I can cut and grind it to shape with saws, knives,
bricks, bits of granite, and so on.  Maybe a little hardfacing with
waterglass-bonded sand or alumina would be useful to improve
durability, or maybe a bed of vermiculite would be adequate.  That
would already be a significant improvement over just an open bowl of
vermiculite or even the Monster-can forge I’ve been using.

(If I didn't have a butane torch, a stove burner with a metal bowl, or
a wood fire, would probably work too.  We’re getting into serious
bootstrapping territory here!  Also worth mentioning is using a pile
of loose particulate, supported by the thing being heated up and
possibly fuel, instead of a solid refractory.)

Temperature control involves at a minimum some kind of electrical
circuit, probably a temperature sensor, and probably one or both of
airflow control (say, with muffin fans well upstream of any heating)
and electrical heating, say with a resistive heating element.  Without
electrical heating, blowing a variable amount of air through ignited
charcoal, ignited yerba mate, or some other burner (maybe an oil
burner like the one I made with the porous magnesium silicate) could
add a variable amount of heat to the chamber; mixing that air with a
second airstream could control the temperature of the air being
introduced to the kiln as well as reducing unburnt fuel contamination
and making the atmosphere oxidizing again if desired.

Once I can do that, making further components from fired-clay ceramics
should be easy!

Although this involves contaminating the kiln atmosphere with the
fuel, and it has a relatively low maximum temperature, this sort of
thing has the advantage that very high powers can be easily attained
without imposing a significant load on the electrical system.  A
typical US$10 computer case fan might use 200 mA at 12 V and be able
to provide 30 “cfm”, cubic feet per minute, which is 14 liters per
second, which works out to 3.6 grams per second of oxygen (21% of
1.2 g/ℓ).  (Maybe that’s too pessimistic; [the first fan I checked on
Amazon claims 56.3 cfm at 0.96 W][0], but [a US$2 40mm fan claims 6.7
cfm at 1.2W][1].) Suppose you’re burning charcoal, and that it’s
basically the same as graphite; one mole of O₂ (31.998 g/mol) produces
one mole of CO₂ (44.009 g/mol), which has a standard enthalpy of
formation of -393.5 kJ/mol.  So crudely you get about 12.30 kJ/gO₂, so
at 3.6 g/s you get **44 kilowatts** of heating power, while the fan
motor is only using 2.4 watts.  The charcoal amplifies the fan’s heat
output by a factor of 18000.  Or 86000 if we believe the Amazon large
fan number, or only 8200 if we believe the Amazon small fan number.

[0]: https://www.amazon.com/ARCTIC-ACFAN00120A-Pressure-Optimized-Sharing-Technology/dp/B07GJGF56L/ref=sr_1_3 "US$9.82 ‘ARCTIC P12 PWM PST’ 120 mm case fan, 200–1800 rpm, 56.3 cfm, 12 V, 145 g, static pressure ‘2.2 H2O’ whatever the fuck that’s supposed to mean (2.2mm H₂O?), 80 mA at full speed"
[1]: https://www.amazon.com/Adda-40mm-10mm-Speed-2-Pin/dp/B07NKLKKP4/ref=sr_1_8 "US$1.99 Adda AD0412HS-G70 2-pin fan, 40 x 40 x 10mm, 12VDC, 0.10A, 1.2W, 6.7 CFM, 32 dBA, 6000 RPM"

(In a sense this design involves two combustion chambers: one with
fuel in it, which will increase the rate of fuel volatilization when
airflow through it increases, and a second one downstream from it,
which serves to ensure complete fuel combustion and perhaps restore
oxidizing conditions by adding enough oxygen to the exhaust from the
first combustion chamber, and which does not transmit heat to the
still-unburned fuel.)

Fuel burning is of course much more difficult to control.

Using a resistive heating element upstream from the kiln chamber
itself would enable me to maintain a reducing atmosphere in the kiln
(with a little sacrificial carbon or something, similar to the
ignited-charcoal-heater approach) without needing exotic heating
elements (graphite, carborundum, zirconia, platinum,
fused-quartz-encapsulated tungsten) that can withstand reducing
atmospheres at high temperatures.

Running the flue gases through a scrubber would be pretty useful to
avoid poisoning the neighborhood, creating noxious smells, and setting
things on fire with hot gases.  A bubbler, a spray-nozzle column, or a
sewage-treatment-style trickling-filter sort of arrangement (see file
`liquid-packed-beds.md`)would enable a large contact surface area
between the flue gases and the water.  Driving the whole thing with a
suction pump at the output of the scrubber would keep the pump itself
from being exposed to hot gases and melting, as long as the scrubber
itself is cooling the gases adequately.

Even if the kiln isn’t heated by combustion, flue gases are a concern,
because reactions inside the kiln can produce gases which can be
stinky, poisonous, or both, and of course the output will be hot.  But
it may be possible to have less of them!

Carbon monoxide (perhaps from incomplete combustion of organics inside
the kiln) is a particular concern because it’s hard to remove; you
pretty much just have to burn it.

Alternatives to combustion for heating include direct resistive joule
heating, indirect resistive heating by way of an induction coil,
dielectric heating, microwave heating (which provides indirect
resistive and dielectric heating), direct arc heating with consumable
electrodes (typically graphite), indirect arc heating with microwaves,
self-propagating high-temperature synthesis, and solar furnaces like
Lavoisier’s.  Of these, the last two have natural temperature limits,
and the others basically don’t.

Once I have a refractory ceramic automated fabrication capability
working, it should be possible to make fan blades and even Parsons
turbines out of refractory ceramics, which straightforwardly would
seem to make it relatively easy to pump hot gases directly.  But I’m
not sure how to transmit the rotation to the blades: through a long
shaft that traverses refractory gland packing?  (This is a “bifurcated
fan” in industrial fan lingo.)
