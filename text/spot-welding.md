In theory you should be able to do spot welds with arbitrarily small
energies if you do them fast enough and can somehow get the energy to
deposit at the place you want it.

But suppose you want to melt a spherical nugget of steel of radius
1mm, which should be a practical thing to do with a carbon arc.  Iron
is 7.8 g/cc and 55.845 g/mol, holds 25.10 J/mol/K, and sucks up 13.81
kJ/mol in melting, which it does when pure at 1538° but as steels
perhaps more typically at 1400° or so, which can be reasonably
approximated as 1400° above room temperature.  This should require
about 30J:

    You have: (1400 K * (25.10 J/mol/K) + 13.81 kJ/mol) / (55.845 g/mol)
    You want: J/g
        * 876.53326
        / 0.001140858
    You have: (1400 K * (25.10 J/mol/K) + 13.81 kJ/mol) / (55.845 g/mol) * spherevol(1mm) * 7.8 g/cc
    You want: J
        * 28.638589
        / 0.034917922

Maybe make it 100 J to be safe.

You could maybe preheat the workpiece to 200° to make this a little
cheaper, but the effect on the required energy is surprisingly small.
Preheating it more would rapidly oxidize the surface.

    You have: (1200 K * (25.10 J/mol/K) + 13.81 kJ/mol) / (55.845 g/mol) * spherevol(1mm) * 7.8 g/cc
    You want: J
        * 25.701598
        / 0.038908087

If we very roughly approximate that the temperature gradient is
1400°/mm over the surface of a 1mm-radius sphere, and use pure iron’s
thermal conductivity of 80.4 W/m/°, we can derive a power for how fast
this little weld puddle will be quenched, about 1500 watts:

    You have: 4 pi (1 mm)**2 1400 K/mm * 80.4 W/m/K
    You want: W
        * 1414.4707
        / 0.00070697825

That means we have to deliver all of our 30 or 100 or 200 joules
within about 20-100 ms, or the steel will suck the heat away faster
than we’re pouring it in, and we’ll never get a melt.  But 20-100 ms
is really not a very demanding specification at all.

If, like a handheld point-and-shoot camera with an on-camera strobe,
we build up the energy over a period of time before releasing it in a
sudden burst to make the weld, thus avoiding the need for a high-power
power source, we need to store it in some kind of energy storage
element that can release it very rapidly, probably an inductor or
capacitor, although a flywheel attached to a motor-generator that can
briefly handle multi-kilowatt pulses is an amusing idea too.  You
might reasonably be able to build up the energy over 100 ms or 1000ms.

The energy of an ideal inductor is ½LI², so if you want 100 J in a
1-henry inductor, like those used in old 120V fluorescent-light
ballasts, you need to be running 14 amps through it.  Actually, let’s
derive this.  WP says, “A general lighting service 48-inch (1,219 mm)
T12[30] lamp operates at 430 mA, with 100 volts drop. High output
lamps operate at 800 mA, and some types operate up to 1.5 A. The power
level varies from 33 to 82 watts per meter of tube length (10 to 25
W/ft) for T12 lamps.”  To drop 20 V at 430 mA the ballast needs a
reactance of 47Ω, which is 2πfL, so we need about 120 mH:

    You have: 20V/430mA
    You want: ohms
        * 46.511628
        / 0.0215
    You have: 47 ohms / 2 pi 60 Hz
    You want: H
        * 0.12467137
        / 8.0210876

So maybe it’s common to use inductors of less inductance than that.
Regardless, it’s going to be a pretty annoying energy storage device,
the weight of my fist.

The energy stored in a capacitor is analogously ½CV².  A 1μF 2100V
microwave oven capacitor is also about the weight of my fist but is
only rated to hold a couple of joules:

    You have: half (2100V)**2 1 microfarad
    You want: J
        * 2.205
        / 0.45351474

Electrolytic capacitors might be a better option.  A 400V 1000μF
capacitor from a switching power supply is rated to hold 80J and is
actually smaller:

    You have: half 1000μF (400V)**2
    You want: J
        * 80
        / 0.0125

Electrolytics don’t have spectacular ESR and ESL ratings, so they’re
not useful for fast pulses, but 20ms is not a fast pulse at all.  [The
Cornell Dubilier 1200μF 380LX122M400A082 costs US$6][1] and is
supposed to have 0.152Ω, though that is of course at 120Hz, but
unexpectedly it’s supposed to be only 0.053Ω at 20 kHz; it’s 82 mm
tall and 35 mm in diameter, dramatically smaller than a microwave oven
capacitor.  Discharging it from 400V in 20ms would take about 24 A,
dropping an insignificant 4V across the ESR.

[1]: https://www.digikey.com/en/products/detail/cornell-dubilier-electronics-cde/380LX122M400A082/1699352

    You have: 400 V 1200 μF / 20 ms
    You want: 
            Definition: 24 A
    You have: 24 A .152 ohms
    You want: V
        * 3.648
        / 0.27412281

You’d also need some kind of switch that could turn on the capacitor
rapidly, handle 24 amps, and not drop much more than 100 volts itself
(so under 4Ω, ideally under 0.4Ω).  A US$2 IRF540N MOSFET could almost
do the job, but its voltage rating is a little low at only 100V.
Something like the [US$8 STB45N65M5][5] would probably be vast
overkill; it’s rated for 650 V, 0.078Ω, 210 W (!), and 35 A
continuous, 140 A pulsed.  Something like the [US$1.70 STU6N62K3][6]
would work if we ease up a little: 22 amps pulsed drain current, 620
V, 90 watts, 0.95Ω.  And the [US$1.40 TK650A60F-S4X][7] would be
ample: 44 A pulsed current (11 A continuous), 600 V, 45 W, 0.54Ω.

[5]: https://www.digikey.com/en/products/detail/stmicroelectronics/STB45N65M5/3088024
[6]: https://www.digikey.com/en/products/detail/stmicroelectronics/STU6N62K3/2035551
[7]: https://www.digikey.com/en/products/detail/toshiba-semiconductor-and-storage/TK650A60F-S4X/8570619

(You could probably even use a bipolar power transistor for this, but
MOSFETs seem to have higher pulse currents relative to their
continuous currents.)

I suspect that the correct circuit for this is actually fairly similar
to a traditional fluorescent-light setup: the storage capacitor has an
inductor on its output, and the switching transistor shorts the
inductor to the other end of the storage capacitor, allowing current
to build up.  When the current has risen to the correct level, the
transistor is turned off, and the resulting high voltage strikes the
arc to the workpiece, which then converts the small amount of energy
stored in the inductor and the large amount stored in the capacitor
into heat, while the inductor prevents the negative-resistance
characteristic of the arc from creating oscillations (although, would
it matter if it did?).  Because [DC-electrode-negative delivers about
two thirds of the power to the positively charged workpiece][8],
perhaps because [electrons evaporating from the cathode cool it][9],
you probably don’t want to be shorting the inductor *to ground* with
the transistor, assuming your workpiece is grounded.

[8]: https://en.wikipedia.org/wiki/Gas_tungsten_arc_welding#Power_supply
[9]: http://web.archive.org/web/20140824085415/https://eagar.mit.edu/EagarPapers/Eagar109.pdf "The Physics of Arc Welding Processes, by T.W. Eagar, 01990"

That last reference, though, brings the alarming news that “the actual
melting efficiency of the arc welding process is relatively low (i.e.,
on the order of 20 percent or less).”  So maybe delivering 30 joules
to the metal would involve dissipating 150 or 200 joules, which eats
up most of the safety factors in my notes above.  However, if you can
deliver the same energy in much less than 20 milliseconds, or deliver
several kilowatts for a longer time, you should still get a molten
nugget.

Perhaps resistance welding would have higher efficiency; it would
certainly simplify the circuitry.
