On Earth we make our photovoltaic panels out of semiconductors,
separating the positive and negative charge collection nets with the
depletion region of a reverse-biased pn semiconductor junction, but in
space we could use photoemission across a vacuum gap; this will
probably give less power per unit area but more power per unit mass
than silicon solar cells, but will be thoroughly dominated by
thin-film cells.

I got this idea from a discussion with Luke Parrish, who suggested
that for space-based PV panels you could just use vacuum.

Basic design
------------

We were discussing [aerographite][0], which has recently been mooted
as a possible solar sail material with 1 kPa UTS and 180 g/m³.  As it
happens, aerographite is fairly conductive (0.2 S/m at that density).

[0]: https://en.wikipedia.org/wiki/Aerographite

You could make a large [photoemissive][8] solar panel, like old
vacuum-tube electric eyes but [backward-biased][2].  [WP claims][1]
that cesium on a silver oxide support gives photoemissivity down into
the infrared, so you could plate such a mixture on the sunward side of
the aerographite support to make a photoemissive cathode, potentially
a gigantic one; [photon energy][3] beyond what is needed to overcome
the work function becomes electron kinetic energy, which can push the
electron uphill against a potential difference to an electron
collector grid anode, which needs to be porous, to let light through,
and spaced far enough away from the cathode with insulating supports
to prevent field emission from stealing the electrons back to the
cathode.  The spacing can be any distance that is small relative to
the mean free path in the vacuum medium.

[1]: https://en.wikipedia.org/wiki/Phototube
[2]: https://en.wikipedia.org/wiki/Work_function#Work_function_of_cold_electron_collector
[3]: https://en.wikipedia.org/wiki/Photon_energy
[8]: https://en.wikipedia.org/wiki/Photoelectric_effect

### The anode grid ###

The spaces in the electron collector grid through which light comes
will also permit the loss of some photoelectrons, perhaps the
majority.  Assuming no charge transfer to the solar wind, the lost
electrons will eventually fall back to the positively-charged PV
panel, some striking the cathode and others the anode.  If it’s
desired to maximize efficiency per area rather than efficiency per
mass, you can extend the grid sunward into a honeycomb which lets
almost all of the light through, while capturing all of the electrons,
except for those emitted at a very small angle to the incoming light.
However, extending the grid “vertically” in this way runs into
diminishing returns very quickly; to maximize the electrons captured
per unit mass of panel, the thickness should be only a little thicker
than the width of the “wires” in the grid in the “horizontal”
direction.

This means that the mesh of the grid should be as fine as possible,
but its holes still need to be large relative to the wavelength of
light and relative to the thickness of its “wires”.  I suspect that
hole diameter on the order of 1–10 μm will be optimal, with “wires” on
the order of 0.1–1 μm “horizontally” and 0.1–3 μm “vertically”.  An
omnitriangulated mesh would be optimal for rigidity; a hexagonal mesh
would be optimal for compliance and wire-to-hole ratio; a square mesh
is in between these extremes.

This works out to be on the order of 1 g/m² for the mesh if it is made
of something like aluminum (2 · 0.3 μm · 1 μm · 3 μm / (3 μm)² · (3
g/cc) = 0.6 g/m²), corresponding to the areal density of a uniform
sheet of about 100 nm.  These dimensions are too small to make use of
the lower density of aerographite itself, because those result from
heterogeneity at larger scales than that.

### The cathode structure ###

If the cathode has 50 nm of low-work-function photoemissive material
plated onto the front of it, which I think is realistic, backed by the
low-density aerographite mentioned above with an areal density of
½ g/m², it would be about 2.8 mm in average thickness.  You would of
course want to give both this cathode and the anode thicker and
thinner parts, like the veins of a dicotyledon leaf or the threads of
ripstop nylon, to reduce their electrical resistance and mechanical
compliance.

It may be important to keep the electrodes cool to avoid loss of the
electrodes from the anode mesh.  Using a high-work-function surface
for the anode and the non-sunward side of the cathode may be helpful
to reduce such losses.

Areal density: 2 g/m³
---------------------

This adds up to an areal density for our orbiting solar panels on the
order of 2 g/m³ or 2 tonnes per km², roughly a hundred times lighter
than conventional silicon solar panels at 100 μm thickness; typically
in space multijunction cells [with efficiency around 30%][4] are used.

Calculating efficiency
----------------------

A km² of sunlight is about 3 megawatts at Earth’s orbital distance, or
much more if you’re closer to the sun, but how much of that can we
really gather?

[4]: https://commons.wikimedia.org/wiki/File:CellPVeff%28rev210104%29.png

This depends on the [quantum efficiency][7] of photoemission from the
cathode (what fraction of photons eject an electron) and the reverse
bias voltage we demand the electrons fight against.  Photons whose
energy is precisely the work function plus the bias voltage are
converted with 100% efficiency; photons at any lower energy are
entirely wasted; any excess photon energy over that minimum is wasted.
(We could imagine multiple cleverly shaped anodes whose electric
fields guide most electrons to the highest-energy anode they’d be able
to reach, but let’s assume we don’t do that.)

[7]: https://en.wikipedia.org/wiki/Photocathode#Quantum_Efficiency_%28QE%29

### Bias voltage limits spectral efficiency to 33% ###

So, too high a bias voltage will produce zero current, but lowering
the bias voltage will eventually produce insufficient additional
current to make up for the energy loss per electron; there’s some
voltage at which we see the maximum power.  (This closely corresponds
to spectrum losses in conventional PV panels.)  This MPPT bias voltage
will be a little lower than the energy of the average photon, which is
[probably about 700 nm][5]; *h c*/700 nm = 1.2398 eV/0.7 ≈ 1.8 eV, so
probably the right bias voltage is on the order of 1.8 V, which is a
conveniently tractable voltage; the [Shockley-Queisser limit][6] is an
efficiency of 33% at a semiconductor bandgap of 1.34 eV, which I think
corresponds to a bias voltage of 1.34 V in this photoemissive panel.

[5]: https://en.wikipedia.org/wiki/Sunlight#Spectral_composition_of_sunlight_at_Earth%27s_surface
[6]: https://en.wikipedia.org/wiki/Shockley%E2%80%93Queisser_limit

I think the recombination losses found in semiconductor PV cells do
not have much of an analogue in this device; the space charge is
entirely negative, and the only way electrons can “recombine” after
leaving the cathode is to fall back onto it, either because they
lacked the energy to reach the anode or because they went through
holes in the anode twice.  Presumably there is at least some
probability that they will be “emitted” into the cathode material,
though, where they will immediately “recombine”.

### Quantum efficiency in the single digit percents ###

So, what about the quantum efficiency?  Evidently in silicon PV it’s
around 0.8, but these photoemissive panels might be much worse.  If
their quantum efficiency were, say, 10⁻⁶, they would produce less
electrical energy per mass than conventional silicon cells, rendering
them useless.  Wikipedia says that phototubes typically produce
microamperes, and they typically have a cathode area around 10 cm² and
are typically illuminated by an infrared beam that can’t be much more
than 10 W/m² (or we’d feel it on our skin and possibly damage our
eyes), which puts a lower bound on their QE of about 10 cm² · 10 W/m²
/ 1.7 eV / (μA/e) ≈ 1/6000.  At this QE we would expect 33% ·
1400 W/m² / 6000 ≈ 77 mW/m², which is high enough to be useful but not
high enough to compete with conventional solar cells; dividing by the
estimate above of 2 g/m², we get 39 mW/g, which is much lower than the
areal efficiency of conventional multijunction silicon solar cells,
30% · 1400 W/ m² / (230 g/m²) ≈ 1800 mW/g, 46 times higher.

So this approach can be mass-competitive with multijunction silicon
solar cells if the photoemissive cathode quantum efficiency is more
than about 1/130, i.e., 0.8%.

In fact the [cesium-antimony photocathodes][9] used in the first
commercially successful photomultiplier tubes have a quantum
efficiency of 12% at 400 nm, though the quantum efficiency of earlier
silver-oxide-cesium photocathodes peaked at 0.4% at 800 nm.  So it
seems likely that, using these new ultralight electrode materials,
this photoemissive generator can probably beat silicon PV in power per
unit mass, but it will be significantly inferior in power per unit
area.

[9]: https://en.wikipedia.org/wiki/Photomultiplier_tube#Improved_photocathodes

Thin-film semiconductor PV cells like CIGS can probably beat it in
power per unit mass, too.