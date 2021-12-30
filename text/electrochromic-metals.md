Tungsten oxide, Prussian blue, and some other metal compounds can go
through a reversible electrolytic redox reaction that changes their
color or transparency; commonly this involves intercalating lithium
ions into them.  But of course you can also electrolytically oxidize
silver to black silver oxide or, if sulfur ions are available, to
sulfide, and then reduce it again by reversing the current; this sort
of thing is also done by artisans to add contrast to copper objects,
typically using liver of sulfur rather than electrolysis.

Display design
--------------

This suggests that by running, say, silver or copper “electrochromic”
strips in one direction and thin wire counter electrodes over them in
the other direction, filling the space between with a thin electrolyte
(maybe a hydrogel), you could get a very simple electrochromic
display.  It might not be fast or last through many switching cycles
but it should still be interesting.  Like other electrochromic
displays it would be fairly bistable and thus potentially very energy
efficient for passive reading.

If you apply higher voltages to speed up the reactions, unless you use
a per-pixel diode or transistor, you might get some bleedover into
other pixels in the same row and column, as well as the rest of the
display.  If you’re applying +2.1 V to a pixel, then any pixel not in
the same row or column is in series with a pixel in the same row and a
pixel in the same column with +0.7 V, -0.7 V, +0.7 V respectively.  By
a similar route, unless there are per-pixel diodes, different pixels
will tend to drive currents through one another even when the driver
is open-circuit, which will tend to equalize the charge and therefore
the colors along each row and column.

With either per-pixel diodes or per-pixel transistors, the idea is
that one of the two electrodes (let’s say the counter electrode,
though the electrochromic electrode would work too) is divided into
one section per pixel.  In the diode case, there are two insulated
wires for that row or column, one with a diode from it to the
electrode, which can thus make the electrode an anode, and the other
with a diode from the electrode to it, which can thus make the
electrode a cathode.  Ideally these would be germanium diodes,
Schottky diodes, or both, to reduce the voltage error.

In the transistor case, the channel of a FET switchably connects the
electrode to a power-supply line, which itself can be brought low or
high, so you still have two insulated wires but you no longer have a
voltage error.  We’re using low enough voltages that the FET body
diode probably doesn’t matter; if it does, you might be able to use a
silicon carbide MOSFET (which has a larger body diode forward voltage
because of carborundum’s [3.3
V](https://www.mouser.com/pdfDocs/infineon-CoolSiC-MOSFET-Revolution.pdf)
bandgap, triple silicon’s; [the MSC040SMA120B4 is rated for -4.0
V](http://ww1.microchip.com/downloads/en/DeviceDoc/Microsemi_MSC040SMA120B4_SiC_MOSFET_Datasheet_A.PDF)
but the plot shows appreciable body-diode current at only -1.5 V,
depending on Vgs) or I think you can get MOSFETs where the body
terminal is brought out as a fourth pin, in which case you could tie
that to a third power supply wire.  (However, the 4-pin discrete
MOSFETs I’ve been able to find use the fourth pin as a
Kelvin-connection probe for sensing the voltage at the source on
chip.)

The electrolytic reactions at the wire counter electrodes must also be
taken into account; if they produce gas, for example, it will deplete
the electrolyte, mechanically stress the device with gas bubbles, and
may create an explosion risk.  If the “wires” are, for example,
transparent ITO strips, anything that forms on their surface will also
be in the optical path; alternatively they could be the same metal as
the electrochromic electrode, though they will probably have different
overpotentials due to smaller surface area and thus higher current
density.

You need the electrolyte to be on the same order of thickness as the
pixel width in order to change the color of the whole pixel, though if
the reaction passivates or “polarizes” the electrochromic electrode it
might just be a question of how soon the color changes in each part of
the pixel.  That effect could be used to get, in effect, multiple
pixels per intersection: whatever part of the electrochromic electrode
is closest to the counter electrode would react first.

It may be useful to have reference electrodes that run along either
rows or columns in order to control the voltage on the electrochromic
electrode more precisely.

Such a device could presumably be used as short-term nonvolatile
memory as well, using the thickness of the passivation layer thus
formed to record a bit, measured by the ratio of resistive impedance
to capacitive impedance by probing it at two frequencies.

Some materials have different extinction coefficients (opacities) for
different wavelengths, so the color of their films depends on their
thickness, quite aside from iridescence.  For oxide layers that are
not very opaque at any wavelength, the iridescence effect will tend to
be stronger than the inherent color of the oxide formed, though it
will be weaker in contact with water than with air, since the
[index](https://en.wikipedia.org/wiki/Refractive_index) of water is
1.33, close to common glasses.  However, [zinc oxide is
2.4](https://en.wikipedia.org/wiki/List_of_refractive_indices),
[hematite is close to
2.9](https://refractiveindex.info/?shelf=main&book=Fe2O3&page=Querry-e),
[tenorite is
2.9-3.1](https://www.sciencedirect.com/science/article/abs/pii/092702489390027Z),
titania is 2.6, and [the strength of the reflection at the interface
is roughly proportional to the square of the difference of the
indices](https://en.wikipedia.org/wiki/Fresnel_equations#Power_(intensity)_reflection_and_transmission_coefficients),
so such materials would still have great potential for iridescence.

In general these devices will act faster at higher temperatures.

Copper oxides
-------------

The Pourbaix diagram for copper shows that above about pH 7 and above
about +0.3 volts the equilibrium favors black cupric tenorite, CuO; as
pH increases to about 12.5 the critical voltage decreases to about
-0.2 volts.  But there’s a small region, for example from about -0.1 V
to about +0.2 V at pH 8, where instead red cuprite, Cu2O, is favored.
(Different sources disagree on exactly how big this window is.)  At
more negative voltages, the equilibrium favors the reduction back to
copper metal.

In this case the electrolyte would need to be slightly alkaline, and
maybe you could get three colors: copper yellow, red, and black.
Possibly turning a pixel red might take weeks.

There also exists an unstable olive-green copper peroxide, but I don’t
think you can make it in this way; you need pre-existing peroxide
groups.

If the copper forms dissolved copper salts, they will of course be
green, and when it redeposits as metallic copper it will often be
yellow rather than shiny.  Oxides of copper are very insoluble,
though, so this presumes some other materials in the electrolyte.

[Copper oxide itself is an electrochromic
material](https://www.sciencedirect.com/science/article/abs/pii/092702489390027Z)
and when it contains some cuprite it is reported to be somewhat
reddish-gray even when only 60-500 nm thick.

Iron oxides and hydroxides
--------------------------

Iron oxides can have many different colors, especially with water
hydroxylating them: [in pottery commonly red, green, grey, or
brown](https://digitalfire.com/material/iron+oxide+red); there are
[sixteen known oxides](https://en.wikipedia.org/wiki/Iron_oxide),
including [black Fe3O4
magnetite](https://en.wikipedia.org/wiki/Iron(II,III)_oxide), [black
FeO wüstite](https://en.wikipedia.org/wiki/Iron(II)_oxide), [red Fe2O3
hematite](https://en.wikipedia.org/wiki/Iron(III)_oxide),
[orange/brown FeOOH goethite](https://en.wikipedia.org/wiki/Goethite)
[which can be yellow to black depending on
things](https://en.wikipedia.org/wiki/Iron(III)_oxide-hydroxide#Properties)
including [limonite at the yellow
end](https://en.wikipedia.org/wiki/Limonite), and
[green](https://en.wikipedia.org/wiki/Foug%C3%A8rite).  This is
another possible multicolored pixel, although you probably can’t get
*all* of those colors; [the Pourbaix diagram for iron in water at
25°](https://www.substech.com/dokuwiki/doku.php?id=pourbaix_diagrams)
says that starting about pH 8.1, you get iron up to about -0.5 V,
(green?) fougèrite up to about -0.3 V, black magnetite up to about 0
V, red hematite up to about 1.2 V, and then [aqueous ferrate
solution](https://en.wikipedia.org/wiki/Ferrate(VI)), “pale
violet... one of the strongest water-stable oxidizing species known”
(!).  However, I suspect that most of these reactions are very slow.

Nickel oxides
-------------

Nickel is pretty passive most of the time, but [nickel
oxide](https://digitalfire.com/material/nickel+oxide+black) is used in
pottery to produce blue, grey, yellow, and black, and [its usual NiO
form](https://en.wikipedia.org/wiki/Nickel(II)_oxide) is green, while
[the trivalent
oxide-hydroxide](https://en.wikipedia.org/wiki/Nickel_oxide_hydroxide)
is black.  I’m not sure if you can form the divalent green compound in
water; the Pourbaix diagrams I’m finding are contradictory.
