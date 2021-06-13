Resistance welding with copper electrodes is the standard way to
spot-weld steel; for high duty cycles they are water-cooled, but low
duty cycles are often just solid copper.  You’d think this would
totally fail because [copper melts at 1084.62°][0] while steel
typically [melts around 1500°][1], so the copper would melt long
before the steel.  In fact, though, at room temperature, [copper has
an electrical resistivity of about 16.8 nΩ m,][2] while 1010 carbon
steel is more like 143 nΩ m, and [copper’s thermal conductivity of
400 W/m/K][3] is also greater than carbon steels’ of around
30–100 W/m/K.

So the same current density running through copper and steel generates
8.5 times as much heat per unit volume in the copper, and the copper
can conduct it away from the point of generation 4–12 times as fast,
so the temperature rise in the copper tends to be about 30–100 times
less.  These numbers change at higher temperatures but I think the
overall tendency remains the same.  In EDM, even with the ultra-high
temperatures of the arcs, copper electrodes are considered to be “free
of wear”.

[0]: https://en.wikipedia.org/wiki/Copper
[1]: https://en.wikipedia.org/wiki/Steel#Material_properties
[2]: https://en.wikipedia.org/wiki/Electrical_resistivity_and_conductivity#Resistivity_and_conductivity_of_various_materials
[3]: https://en.wikipedia.org/wiki/List_of_thermal_conductivities

Of course the heat equation tells us that the copper and steel in
contact immediately form a continuous temperature distribution, so
what you’re really doing is melting steel *under* the surface, while
the surface steel remains solid, chilled by the copper to under 1000°.

It occurs to me that you could use this same approach for *forming*
the steel instead of welding pieces of it together: by locally melting
it with a pulse of current, it can be formed by pressing even a soft
copper ball into it.  By doing this repeatedly while moving the copper
ball around to precise positions in three dimensions, you can achieve
arbitrarily complex surface geometry without the high side loads and
noise of a mill or lathe, and regardless of how hard the steel is.  If
it’s a high-carbon steel, the forming process will inherently
case-harden the product, as each melt is quenched by the mass of the
steel.  With proper planning of the toolpaths, especially the
finishing toolpath, it should be possible to keep heat-induced
distortion of the workpiece small by keeping the heating very
localized.

