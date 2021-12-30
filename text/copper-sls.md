Copper selective laser sintering and similar powder-bed processes have
some interesting benefits.  Metal powder for 3-D printers apparently
costs US$300-600 per kg, but copper is easy to powder
electrolytically.  Also, copper powder is not an explosive hazard in
air as most other metal powders are.  It’s not quite noble enough to
sinter in air, but you should be able to sinter it in nitrogen (Cu3N
does exist at room temperature, but decomposes with a little heating
and is [estimated to have a positive enthalpy of formation around
+74.5 kJ/mol][0], being a potential conductive copper ink material by
this route, and is consequently difficult to synthesize, requiring
either sputtering or both pre-oxidized copper and pre-cracked
nitrogen), or possibly even a reduced-oxygen air atmosphere or carbon
dioxide.

[0]: https://www.sciencedirect.com/science/article/pii/S2187076414000876 "Synthesis of Cu3N from CuO and NaNH2, Miura, Takei, Kumada, Journal of Asian Ceramic Societies, Volume 2, Issue 4, December 2014, pp. 326-328, 10.1016/j.jascer.2014.08.007, CC-BY-NC-ND"

Lasers are a desirable way to pattern the surface because they can
achieve high precision and high power in a small area, which is
particularly important for very thermally conductive metals like
copper.  Possible alternatives include electron beams (in vacuum),
arcs, localized electrodeposition (in an electrolyte), and an
inkjet-printed light-absorbing layer followed by illumination with a
strobe light.

This last alternative requires delivering enough heat in the light of
the strobe to melt or at least sinter the surface copper layer before
the heat can diffuse out of the surface layer into the bulk material,
similar to skin burns from the flash of an atomic bomb; but it does
need to diffuse to the non-illuminated side of the copper particles in
the surface layer.  Air-gap flashes can achieve 500 ns speed, but
typically their emission spectrum has a lot of blue and green, which
might be suboptimal, since copper’s reflectivity is not very high in
those colors, and we want the un-inked copper to be reflective.
Doping the plasma with something like strontium, lithium, or sodium
might help to increase emissivity in the red and green, increasing the
contrast between the ink and the copper.  (Carbon dioxide mostly emits
at 4300 nm, but I don’t think you can get enough power out of it.)

Copper melts at 1084.62°, boils at 2562°, has a heat capacity of
24.440 J/mol/K near room temperature, and weighs 8.96 g/cc and 63.546
g/mol.  This works out to 0.385 J/g/K or 3.45 J/cc/K, and so reaching
the melting point (almost necessary for sintering) starting from 20°
requires about 400 J/g or 3.7 kJ/cc.  Its thermal conductivity is 401
W/m/K, and this is the point at which I suddenly wish I understood the
heat equation.

(You don’t really want to melt it, but if you did, its heat of fusion
would be another 13.26 kJ/mol = 0.2087 J/g = 1.87 J/cc.)

Because I don’t understand the heat equation very well, I’m going to
work with a really dumb approximation to get a feel for orders of
growth.

Suppose we have an 0.1-mm surface molten layer of copper (plus an
insignificant amount of carbon susceptor) which ranges from 1100° to
2200°, and the 0.1-mm layer below it ranges from 20° to 1100°, and
that the specific heat and conductivity numbers are unchanged over
this range (which they aren’t, of course, but this is an
approximation).  The thermal gradient then is 11 MK/m, giving us a
heat flow of 4.4 GW/m², or in less overwhelming terms, 4.4 J/m²/ns.
Moreover the thermal energy present (disregarding the heat of fusion)
is 3.7 kJ/cc × 0.2 mm = 740 kJ/m², 74 J/cm².  So reaching a situation
somewhat like this would require depositing those 740 kJ/m² at at
least 4.4 GW/m², which requires a flash of less than 0.17 ms.

A faster flash could melt a thinner surface layer, which would contain
less energy (proportional to the thickness of the surface layer) and
conduct it away from the surface faster (inversely proportional to
that same thickness).  So, for example, for an 0.01 mm layer, ten
times thinner, you would need to deliver only 74 kJ/m², but at 44
GW/m², so instead of 0.17 ms you would need to do it in 0.0017 ms, a
hundred times faster, which is getting down to the limits of what an
air-gap flash can do.

This approach would probably require stepping a focused area over the
copper surface and emitting repeated flash pulses, both in order to
keep the energy of a given flash manageably low, and in order to
bombard the copper from many directions with the light from a small
flash tube in order to be able to achieve a high temperature.

Of course, a Q-switched laser can produce much faster pulses, and much
brighter than a blackbody, albeit at much lower efficiency.  And a
gas-discharge laser might be limited to millisecond or longer pulses,
depending on the gas’s relaxation time, but you can easily focus it
into a 50-micron-diameter area, so even a 10-joule pulse gives you 5
GJ/m² and 5 TW/m², a couple of orders of magnitude higher than you
need to melt the surface of copper.
