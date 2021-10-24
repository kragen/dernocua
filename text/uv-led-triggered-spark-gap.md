The Akhilleus-heel of the spark-gap closing switch is its high jitter,
due to the stochastic nature of streamer formation and cosmic-ray
bombardment in the working gas.  By stimulating the emission of
photoelectrons from a surface with a low work function, you can lower
the breakdown voltage of a spark gap significantly, enough to get it
to trigger reliably with low jitter; if you can drop the breakdown
voltage by more than about 25%, you should be able to reliably trigger
a discharge with little risk of prefires (and, in addition to dropping
the breakdown voltage, this photoemission also significantly reduces
the variability).  But, historically, the only reliable way to get the
short-wavelength light necessary to stimulate such photoelectron
emission was either an incandescent object or another electrical
discharge, leading to a chicken-or-egg problem.

LEDs in the 365–400-nm range are now widely available, including US$10
high-power 3-watt jobbies, and [for US$4.56 Digi-Key will sell you a
278nm 1-milliwatt Everlight ELUC3535NUB-P7085Q05075020-S21Q UVC
LED][0] designed for UV sterilization.  LEDs normally have no jitter
and can have rise times measured in nanoseconds, though the larger
ones have enough junction capacitance to slow this down, and the time
lag of photoemission is typically also around a nanosecond.

[0]: https://www.digikey.com/en/products/detail/everlight-electronics-co-ltd/ELUC3535NUB-P7085Q05075020-S21Q/12177237

To reduce the threshold frequency of light necessary to provoke
photoemission from the spark-gap cathode, we can coat it with a
low-work-function surface; I think barium oxide is the traditional
choice for this in vacuum tubes.  In a spark gap you would need to
ensure that the air within was dry enough not to allow the barium
oxide to become wet.  Zinc might be a friendlier metal, but it still
must be protected from oxidation — or nitridation!  This suggests you
might need a controlled atmosphere in the spark gap.

I think *hν* is the energy of a photon, where *h* is Planck’s constant
6.63 × 10⁻³⁴ J/Hz, and *ν* is the frequency; and the threshold
frequency is that at which this energy is the work function of the
surface.  This gives 3.1 eV at 400 nm, 3.4 eV at 365 nm, and 4.5 eV at
278 nm.

Barium metal’s work function varies from 2.52–2.70 electron volts on
different crystal faces, putting it within the grasp of even the
400-nm “debatably ultraviolet” LEDs, though its enthusiastic
reactivity is problematic; also thus reachable are sodium at 2.36 and
lithium at 2.9, cerium at 2.9, and maybe yttrium at 3.1.  The more
sedate cerium and yttrium are perhaps more promising, though they are
pyrophoric and quickly oxidize in air, the oxides are passivating.

The 365-nm LEDs might additionally be able to spall photoelectrons off
manganese at 4.1 eV and neodymium at 3.2, and the 278-nm ones could
bring within reach zinc at 3.63–4.9, lanthanum at 3.5, molybdenum at
4.36–4.95, and even tin at 4.42 and lead at 4.25.  Unfortunately all
the metals whose oxides are less stable in air than the metals
themselves (gold and some of the platinum group) have work functions
that are still out of reach.

[Barium oxide formed in a certain way on a silver substrate has a work
function around 3.2 eV][1], and the barium peroxide (which BaO tends
to turn into at room temperature, given the chance) is up around 3.6.
[On tungsten, barium oxide mixed with oxides of strontium and calcium
lowers the work function below 2 eV, and baria alone is calculated to
be 2.7 eV][2].  Magnesia, much more chemically stable than baria, has
apparently also been used to good effect; although by itself its work
function is 4.22–5.07 eV, a thin film of it on a metal surface
apparently reduces the work function?  I don’t know.

[1]: https://www.sciencedirect.com/science/article/abs/pii/S0039602814002027
[2]: https://aip.scitation.org/doi/10.1063/1.1646451 "Model of work function of tungsten cathodes with barium oxide coating, by K. C. Mishra, R. Garner, and P. C. Schmidt"

So, this suggests a setup with a hermetically sealed gas-filled spark
gap where the anode has one or more holes in it through which an
ultraviolet LED can shine onto the cathode; the cathode has a partial
coating of one of the above systems, such as a thin film of barium
oxide on top of a coating of titanium, or a coating of cerium, a
coating of lead, a coating of zinc, a coating of lead-tin solder, or a
coating of tin.  When the spark gap is held a little below its
breakdown voltage, a pulse of current through the LED can initiate
abundant photoemission into the interelectrode gap, lowering the
breakdown voltage enough that the spark gap triggers without any
voltage change, and with a jitter measured in nanoseconds.

The advantage of having many holes is that a larger area of anode is
exposed to the photoelectron-enriched region of the gas, potentially
permitting higher current.  The advantage of not having many holes is
that lower arc inductance can be achieved by having many parallel arcs
around the edges of a single round hole, and it’s easier to fabricate.

All of these same techniques can also be applied to a pseudospark
switch, and of course any other low-work-function material can also be
used.  Pseudospark switches normally have jitter down in the tens of
ns.

Although UV irradiation drops the breakdown voltage, I’m not sure it
drops it *below* the lowest safe non-UV-irradiated breakdown voltage.
If that is the case, this approach will always have a significant
chance of prefires.  (I don’t know why free electrons in the gap don’t
drop the lowest breakdown voltage, but apparently free ions in the gap
from a previous firing do.)

A hybrid approach, however, should work extremely well: use an UV LED
to illuminate a conventional electrically-triggered spark gap, using a
third triggering electrode (whether insulated with quartz or not).
This should give jitter that’s as low as could be hoped for with the
LED, while eliminating the risk of prefire.  You still need a
low-work-function electrode surface to keep the work function low
enough to overcome with a mere LED.  (Hofstra sells a UV-illuminated
spark gap using this principle, but I think it uses conventional a
mercury-discharge-lamp UV source rather than LED illumination; it
appears to be hand-sized.)

There are reports that in the twilight zone below the Paschen minimum,
where pseudospark switches operate, electron injection *is* adequate
to reliably trigger a discharge, and “UV flash” is an existing
triggering approach.  Perhaps electron injection via UV-LED-induced
photoelectrons would be sufficient.  Normally pseudospark switches
operate at neon-sign-style vacuums (10–50 Pa) in order to get past the
Paschen minimum, but you could instead simply make them very small
(micron-sized gaps), reducing the distance factor rather than the
pressure factor.

To avoid arcing *to* the low-work-function “seed” surface — for
example, if it’s delicate, has annoyingly high resistivity, or would
contaminate the dielectric gas undesirably — it can be placed closer
to the anode than the main cathode is, connected to the rest of the
cathode with a heavy high-value resistor.  As long as only the
photocurrent is flowing in the gap, the voltage across the high-value
resistor is effectively zero, but once the spark initiates to the
seed, the seed quickly reaches the potential of the anode, so the
spark will rapidly propagate to the rest of the cathode through the
gas, since now the entire gap’s breakdown voltage is across the much
shorter distance between the two parts of the cathode, and across the
resistor.
