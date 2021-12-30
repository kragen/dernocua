I’d previously made some notes somewhere on using mechanical vibration
to counter stiction when driving or removing screws, thus preventing
screwdriver camout; this would be less annoying if it was above the
threshold of human hearing, although that might not be practical,
because the energy of each vibrational pulse needs to exceed the
stiction energy.  It occurs to me that it would also be useful for
driving nails, where stiction is pretty much the name of the game.

The ideal graph of force against time of such a sonic-screwdriver
system would be the derivative of a sawtooth: a Dirac delta in the
desired direction large enough to make progress on the fastener, which
necessarily creates momentum within the sonic screwdriver in the
opposite direction, followed by a recovery time during which a
constant small force is applied to arrest and eventually reverse that
momentum, all the while maintaining contact with the fastener.  The
recovery force is applied against, say, the hand of the person using
the device.

A control system can pause if contact is lost, and detect whether
progress is being made and increase the impact energy (lengthening the
recovery time and lowering the frequency) if not, or decreasing the
energy if so, moving the frequency into the ultrasonic; and some
degree of randomness in the interval would seem to be desirable to
spread acoustic annoyance across the spectrum, also avoiding the
danger of dumping a damaging amount of energy into a single resonance
mode of the system.

(For screw installation, it would be very useful to be able to set a
torque.)

This is all very similar, actually, to the action a hammer drill or
rotary hammer uses for drilling holes in masonry.  [Bosch’s 5.7 kg
1500-watt “Titan 5 kg SDS Plus” hammer drill advertises 5 J][0]
maximum impact energy and is rated for drilling 32-mm holes in
masonry, and other hammer drills from the same “Farmers Weekly” seller
advertise impact energy in the 1.7 to 5 J range.  [Makita advertises
their “23 lb. AVTDemolition Hammer” HM1213C rotary hammer as
“delivering 18.8 ft.lbs. of impact energy][1], which is 25 J; it runs
on 14 amps, which is presumably 1.7 kW.  [One shill site advertises
the DeWalt DCH773Y2 rotary hammer (US$1099, 21 pounds) at 19.4 J of
impact 1000-2000 times a second][2] and marvels at how it “just
pulverizes concrete”.

[0]: https://www.fwi.co.uk/machinery/tips-for-choosing-the-right-sds-drill
[1]: https://www.makitatools.com/company/press-releases/2020/makita-introduces-two-powerful-demolition-hammers-with-exclusive-anti-vibration-technology
[2]: https://www.protoolreviews.com/tools/power/cordless/rotary-hammers/dewalt-flexvolt-2-inch-sds-max-combination-hammer-hands-on-review/52694/

For no particularly good reason, there doesn’t seem to be a tool that
applies the same sawtooth force profile to pulling an actual flat saw
blade or wire saw through stone or concrete.

Some of these hammer drills and rotary hammers have a new
anti-vibration feature which creates *two* simultaneous impacts with
each hammer blow: one on the tool bit to make the hole, and the other
on an internal counterweight, so that what rebounds from the impact is
only the counterweight rather than the tool you’re struggling to hold
in your hands.  A different way to accomplish the same thing would be
to just impact the counterweight directly against the toolbit: apply
the tool’s motor to gradually accelerating the counterweight away from
the toolbit against the counterweight’s spring, then toward the
toolbit once the spring wins and the counterweight starts accelerating
it back toward the toolbit.  Either version of this same feature can
be applied to the helical motion of an impact screwdriver (like those
I’m discussing here) just as well as to the linear motion of a rotary
hammer.

How hard is it to drive screws?  Well, how hard can I twist a
screwdriver?  In a simple test just now with a water bottle and a
metal pipe, I was able to rotate my wrist in a T-handle sort of
configuration hard enough to lift 5.5 kg with a lever arm of 330 mm
(the water bottle) and 430 g at 500 mm (the metal pipe itself), which
is a torque of about 20 N m.  This is probably about as hard as I can
twist a T-handle screwdriver to unscrew a screw, but smaller amounts
of torque usually suffice.  About a tenth of a turn is pretty much
always enough for a screw to make progress rather than springing back
to its old position, and that would work out to about 13 J at that
torque.  (This explains the quasi-unit-compatibility of torque and
energy: 20 N m of torque is really 20 N m of energy per radian!)

Normally, of course, screws don’t have to turn nearly that far to not
spring back, and I don’t need a T-handle screwdriver to remove them.

[Engineering Toolbox gives withdrawal forces for some nails][3] in
spruce ranging from 17.6 pounds to 348 pounds (79-1550 N), with a
common 16-penny nail of length 3½” (89 mm) requiring 141 pounds (630
N).  Driving such a nail 1 mm would probably be far enough that it
wouldn’t spring back out, and that would be 0.6 J.  Framing carpenters
drive them all the way in in three hammer blows, which is about 20 J
per blow, disregarding the mass of the nail and the vibrations of the
structure, as you should.

[3]: https://www.engineeringtoolbox.com/nails-spikes-withdrawal-load-d_1814.html

So a simple sonic screwdriver would probably need to be able to ramp
up to on the order of 1-10 J per impact to make progress in difficult
cases, and then it would be able not only to remove screws and drive
framing nails, but also drill and saw concrete, wood, and stone, and
engrave or center-punch steel.  But most of the time 0.1 J would be
enough.  If it were running at 1000 W, the average impulse frequency
would be in the range 100 Hz to 10 kHz, unfortunately all well within
the audible range.  1000 W would also drive one of those 60 J nails in
60 ms.

You could power it off Li-ion batteries in the now-conventional way,
but it really only needs to contain on the order of 128-256 J at any
given time, so it might often be more convenient to charge it with the
necessary energy just before use.  Even a clockwork spring sort of
arrangement might be adequate with a pullstring; I can do two pushups
to about 600 mm, lifting half my 110-kg weight, which is about 320 J.
So normal people should be able to repeatedly pull a pullstring out to
about a meter under a tension of about 50 N, like starting a
lawnmower.  Easy jobs might need a single pull occasionally, while
hard jobs might need five or six pulls before every fastener or
whatever, although at some point you just want to plug the thing in.

The pullstring need not be visible in normal operation; you could
split the tool into two parts joined by the pullstring when charging
it, then reassemble them once charged.

Clockwork springs have the advantage of having almost arbitrarily high
power density, unlike batteries, both for charging and for
discharging.  Rechargeable lithium batteries typically have a “fast
charge rate” of “1 C”, meaning 1/1 hour, or less, perhaps 0.5 C,
meaning 1/.5 = 2 hours.  If you were going to charge them up with a
pullstring, you would have to pull the string continuously over the
course of that hour or two.

The modulus of resilience of a material is the amount of energy it can
store per unit volume as elastic deformation.  For tensile elastic
deformation of ductile linear materials, the relevant figures are
[Young’s modulus E][5] and the [yield stress][4] σ<sub>y</sub>, and
the integral of deformation from 0 to the yield strain σ<sub>y</sub>/E
gives us ½σ<sub>y</sub>²/E.  Most types of steel have the same Young’s
modulus regardless of their hardness, about 200 GPa.  Soft steels have
[yield stresses as low as 300 MPa][6], but normally we make springs
from [music wire][7], which is more like 2800 MPa.  This gives us a
*tensile* modulus of resilience for music wire of some 20 MJ/m³, or 20
J/cc.  256 J then would require 13 cc of spring steel, or 100 g.

Conventional clock mainsprings do in fact deform in tension and
compression, but the mainspring is only stressed to its limit at its
inner and outer surfaces; on its neutral axis it isn’t strained at
all.  So the situation is actually even worse: you only get ¼ of the
possible tensile energy storage that way, and you’d need 400 g of
mainspring.  This is getting to be a rather heavy screwdriver!

Coil springs instead deform the spring material in torsion, which is
to say, in shear, and much more of the material is closer to the
maximum shear strain.  For *shear* deformation we’re interested in the
[shear modulus G][8], about 79 GPa for steels, and the yield [shear
strength][9] τ<sub>y</sub>, which for steels is about [0.58 of
σ<sub>y</sub>][10], or say 1600 MPa; the factor 0.58 comes from
3<sup>-½</sup>.  So if we just calculate the shear modulus of
resilience as ½τ<sub>y</sub>/G, which I’m not sure is the right thing
to do, we get 16 MJ/m³ or 16 J/cc, about 15% lower than the tensile
modulus.  I guess I should do the integral to see how much the
distribution of the shear strain in the circular coil spring
cross-section affects the situation, but it seems clear that using
shear rather than tension (and compression) doesn’t make a huge
difference.

By twisting a *tube* rather than a solid bar, the way a lot of torsion
bars in car suspensions do nowadays, you can get the full shear
modulus of resilience of your metal, but that doesn’t get you more
energy per volume, just more per mass.

So what about carbon fiber?  I hear truck suspensions nowadays are
starting to use carbon-fiber-reinforced plastic rather than steel.

sawtooth components

[4]: https://en.wikipedia.org/wiki/Yield_(engineering)
[5]: https://en.wikipedia.org/wiki/Young%27s_modulus
[6]: https://www.engineeringtoolbox.com/young-modulus-d_417.html
[7]: https://en.wikipedia.org/wiki/Piano_wire
[8]: https://en.wikipedia.org/wiki/Shear_modulus
[9]: https://en.wikipedia.org/wiki/Shear_strength
