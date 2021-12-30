If they are not to be huge, pottery kilns necessarily use a largish
amount of power, because during the peak temperatures of the firing,
they need to maintain their contents at 1000° or so above ambient
temperature.  Under conservative assumptions about the kiln walls
(≈0.1 m², ≈0.1 m, ≈0.5 W/m/K) this requires hundreds or thousands of
watts (500 W in this case; cutting it to 100 W would involve
thickening the effective wall thickness to 0.5 m — over a cubic meter
for an internal volume of just 3 ℓ = spherevol(sqrt(.1m^2/4pi))) or
using refractory insulating vacuum panels which, as far as I know,
don’t exist.  A kiln the size of a domestic microwave oven requires
more like 5 kW and thus cannot run on a regular 120 VAC circuit; it
would need close to 42 amps.

This can be a problem for residential power consumption and wiring
installations.  5 kW is a lot for a single circuit even in 240VAC
countries — though not unheard of, it typically requires a
purpose-installed circuit, which may not be an option for residential
renters.

Firing with fire
----------------

Traditionally pottery was fired with actual fire.  CO₂ has
Δ<sub>f</sub>H<sup>⦵</sup><sub>298</sub> = -393.5 kJ/mol and 12 grams
of carbon per mole, so burning 12 grams of carbon gives you 393.5 kJ,
32.8 kJ/g.  So 5 kW of carbon burning is only 152 mg per second, about
two hours per kilogram of carbon.  Unlike 42-amp electric circuits,
5-kilogram bags of carbon are readily available at convenience stores
around the world, and refining pure carbon from biomass for fuel has
been common practice since long before recorded history.

The combustion of small amounts of fuel can be readily controlled with
much smaller amounts of electrical power, on the order of 1–10 W.

There are three main disadvantages to firing with fire:

- The pottery (or other thing being treated with heat) is exposed to
  the gases from the fire; typically these are reducing gases with
  almost no oxygen and a significant proportion of CO, and there may
  also be ashes, nitrogen oxides, sulfur dioxide, etc.
- It’s difficult to control the heating from the fire.
- The gases have to be released *somewhere*, and they are usually
  toxic.

These three problems can be solved in a variety of ways; here is one
way.

The main combustion chamber
---------------------------

First, to control the amount of heat produced from the fire, you can
restrict the entry of air into the fire.  If the fire is in a
well-insulated chamber, it can remain hot enough to stay alive for
many minutes without any air input at all; even a small air input will
suffice.  The necessary oxygen for 5000 W and thus 152 mg/s is 32/12
of that, or 405 mg/s; oxygen is about 21% of air, so that’s about
1.9 g of air per second, which is about 1.6 ℓ/s, or 3.4 cfm in the
quaint units used for fans.  But less than that should be fed into the
main combustion chamber itself, since the fire there will not produce
entirely CO₂.

(Of course this flow should be under the control of a microcontroller,
like everything else described in this note.)

The afterburner
---------------

Running the fire always in the lean conditions described above ensures
that the exhaust gas is maximally reducing and thus maximally toxic,
though probably devoid of nitrogen oxides.  To diminish the toxicity
of the exhaust gas, it should have more air injected into it in an
“afterburner” to complete the combustion process; this will produce
more heat but, I think, in general reduce the output temperature,
approaching, I think, the adiabatic flame temperature of carbon,
2180°.  By this means the reducing exhaust gas can be converted into
an oxidizing exhaust gas whose only important remaining toxic
component is CO₂; this process also burns off other unwanted materials
like PCAHs and other components of tar, though it introduces nitrogen
oxides.  Further air injection after complete combustion is probably
usually desirable to lower the exhaust temperature to more convenient
levels.

The regenerator
---------------

As I understand it, the standard way to transfer this heat to the
interior of a (non-electric) muffle kiln is to run it through pipes
that heat the kiln.  But the pipe walls are necessarily of fairly
limited surface area, so most of the heat will not be thus
transferred.  A recuperator-type heat exchanger, heating gas to be fed
into the kiln or recirculated through it, is another alternative, and
in file `capillary-heat-exchanger` in Dercuano I explained how to
build one that’s orders of magnitude denser than existing microchannel
heat exchangers.  But what I want to explore here is regenerative heat
exchangers, because those don’t require exotic fabrication technology.

So you run this hot oxidizing exhaust through a regenerator chamber
packed full of refractory balls of, for example, glucina, quartz,
forsterite, mullite, silicon, philosopher’s wool, thoria, sapphire,
chromia, quicklime, fluorspar, zirconia, yttria, carborundum, or
aluminum phosphate.  I don’t know of any other fluorides that are
refractory enough, and I think almost anything that’s not an oxide,
fluoride, or phosphate would be oxidized under these conditions — even
chromium, which would also suffer nitrogen attack.  Carborundum is a
special case because it forms a refractory protective oxide layer.
Silicon and fluorspar are low-melting, 1414° and 1418° respectively,
but the others mentioned have adequate temperatures.

Smaller balls present more surface area to absorb the heat but also
leave smaller spaces for gas flow, with the result that they consume
more head.  High-conductivity materials like glucina (330 W/m/K at
room temperature), carborundum (360–490), or silicon (150) ease this
tradeoff compared to things like sapphire (30), philosopher’s wool
(21), quartz (10?), forsterite (7?), quicklime (6?), mullite (4?),
thoria (4?), or zirconia (2?).  Unless you want to tangle with
glucina, carborundum would seem to be the obvious choice (though
sapphire is the traditional one); its specific heat is 0.67 J/g/K
(3.2 g/cc), while sapphire’s is 0.88 (4.0 g/cc) and glucina’s is about
1.05 (2.9 g/cc).  If we pretend that these numbers don’t vary with
temperature, 100 g of carborundum with ΔT = 1000° could hold 88 kJ, so
mere heat capacity will not require us to use a large regenerator;
each regenerator chamber might contain 10 g of balls.

Periodically you switch the exhaust to the next cold regenerator
chamber; then you flush the remaining exhaust from the hot chamber
with air, which is also oxidizing, and then switch the direction of
airflow and its source destination: now you are flowing air backwards
through the regenerator chamber, from its cold side to its hot side,
from which you direct it into the kiln chamber to heat it up.  The
source of the air can be either the kiln itself or the outside air; in
the latter case, hot air is displaced from the kiln and thus must be
exhausted; this is probably the best source for air for the fire,
since it is already preheated, unless it has unwanted contaminants
from the things in the kiln.

The duration of heating any one regenerator chamber needs to be short
compared to its heat capacity, and the balls need to be small enough
that the biggest temperature gradient in the chamber is from one end
to the other and not from the surface to the center of each ball.

There are many refractory metals with higher thermal conductivity and
high density, including some cheap ones, but I think you would have to
prevent them from ever contacting hot oxidizing atmospheres.  Though
it would be straightforward to ensure that the exhaust gases were
always reducing, the job of the regenerator is to heat up clean air,
so parts of it will inevitably be exposed to hot air.  So I think it
is best to simply lean out the mix in the afterburner so that the
regenerator balls are not subjected to alternating oxidation and
reduction.

If a higher temperature is desired, despite the higher nitrogen oxide
emissions that will result, some of the heated clean air from the
regenerator can be used as the afterburner air.

Exhaust remediation
-------------------

The exhaust and purge air that come out of the regenerator are cool,
but they still contain a lot of carbon dioxide, and probably nitrogen
oxides as well.  Sometimes you can just send it up a chimney or out a
vent, as people do with hot-water heaters and stove hoods.  In cases
where this is problematic, a carbon dioxide scrubber can be used,
though it may need to be rather large: running at 5000 W = 557 mg/s
CO₂ for 12 hours produces 24 kg of CO₂, which would need to be stored
in the scrubber.  A simple soda-lime scrubber contains 56 g/mol of CaO
and can fix 44 g/mol of CO₂, so you’d need 31 kg of soda-lime, which
you would then have to discard.  Other kinds of scrubbers might be
smaller, since they can recycle the absorbent, but they still need
somewhere to store the CO₂.

On the plus side, I think soda lime will also slurp up nitrogen oxides
and sulfur dioxide.  With other kinds of scrubbers,
diesel-engine-style selective catalytic reduction can remove nitrogen
oxides.

Regenerator cleaning
--------------------

If the fuel is coal or charcoal, periodically the regenerators will
get clogged with ash, so they need to be cooled and washed
periodically with acid; vinegar should be perfectly adequate.  If you
used quicklime for the regenerator balls, you’d have to just empty and
refill the regenerator, since quicklime is a significant component of
ash, and anything that would remove it chemically would also remove
the balls.

Alternatively, the kiln could be operated on a liquid fuel such as
gasoline, diesel fuel, or vegetable oil, or on combustible gas, which
would not produce any significant amount of ash.  Then, the only
possible regenerator contamination would be partially burned fuel,
which would burn off fairly quickly, though possibly damaging
protective oxide layers in the regenerator in the process.

Afterburner or no?  Run the main combustion chamber lean?
---------------------------------------------------------

If the kiln thus runs on liquid fuels, you probably don’t want all the
fuel to be in the main combustion chamber — first, because having
several kilograms of hydrocarbons above their flashpoint in your
kitchen is a terrible idea; second, because it would make the kiln
take quite a while to start, because you must heat them above their
flashpoint first; and, third, because this allows you to run its
combustion chamber lean (with excess air) and thus dispense with the
separate afterburner.  This approach may be worthwhile even with solid
fuel, for example passing ground charcoal through a paddle wheel that
prevents reflux of combustion into the fuel supply; this would also
enable the main combustion chamber to be smaller, speeding up startup
and shutdown.

One possible benefit of a separate afterburner is that it, like a
steam-engine injector, it can provide suction.  Its output is hotter
and more voluminous than its input, so if the output channel is wider
than the input channel it might be able to fluidically drive the other
fluid flows in the kiln with suction, permitting the control system to
work merely by constricting valves.  Injecting water into the main
combustion chamber would produce shift gas, shifting a potentially
large amount of the combustion into the afterburner, which may be
useful for this purpose.

Materials
---------

The main combustion chamber and the afterburner are potentially
exposed to temperatures of 2000° or more, and at least the temperature
of the interior of the kiln (normally 1000°–1500°); moreover, they are
exposed to both oxidizing and reducing conditions.  These are the most
challenging conditions, and in the best of conditions, they probably
require regular replacement of the refractory surfaces in question.

Forsterite sand (melting point 1890°) is commonly used in foundry
practice as a refractory, and even cristobalite (quartz’s ghost)
doesn’t melt until 1713°.  Mullite remains solid up to 1840°, sapphire
to 2072°, larnite (the calcium analogue of forsterite) to 2130°,
quicklime to 2613°.  Sands of these minerals (all dirt cheap except
for maybe mullite) would work as replaceable refractory floors for
these chambers, maybe introducing clean air through them.  This will
protect the floor from ground-up or lump coal, but for the ceiling and
walls you still need something more solid.

The cheapest solution would be wall and ceiling tiles of quicklime, or
if the chamber is small enough, just a single block of quicklime.  It
might be harmless for the quicklime to be produced in situ from
calcium carbonate, but in that case it probably needs some kind of
refractory fiber running through it to keep it from crumbling as it
calcines.  [Larnite][0] (dicalcium silicate, Mohs 6, 2130°) would
probably work well for this.  I think it can be conveniently prepared
in a beaker from calcium chloride and sodium silicate, but I don’t
know how you'd bond the resulting grains together afterwards.

[0]: https://en.wikipedia.org/wiki/Calcium_silicate

Except in case of malfunction, the rest of the kiln is only exposed to
temperatures a little higher than the maximum payload temperature, and
exclusively oxidizing atmospheres, so it can be made from almost any
oxygen-resistant refractory material, including those mentioned
earlier for the regenerator balls.

(The high-temperature zone is another argument in favor of running the
main combustion chamber lean and dispensing with the afterburner: run
it lean enough and you only need to deal with those same lower
temperatures.)

Even this zone of moderate heat is too aggressive for organics or most
metals, since it needs to operate at 1000° in oxidizing atmospheres,
and the regenerators are exposed to constant thermal cycling.  Some
sort of ceramic is unavoidable; insulating firebrick might be the
easiest choice, and probably one of the least damaged by thermal
cycling.

The only necessarily hot mechanical parts are the valves on the hot
side of the regenerator chambers, which probably operate pretty often.
But they probably don’t need to be super great valves; a little
leakage would be tolerable.  Incoming air can be driven with muffin
fans, maintaining the whole apparatus at a slight positive gauge
pressure to prevent any need to ever run hot air through any sort of
blower or pump.

Control system
--------------

You need a microcontroller to control everything, which needs,
minimally, an oxygen sensor on the output of the afterburner, a
temperature sensor inside the kiln (perhaps just a quartz-halogen bulb
used as a resistance temperature detector, or a hardware-store
thermocouple of the type used to shut off pilot lights), control of at
least three on-off valves per regenerator chamber or one three-way mux
valve (hot side can connect to burner, purge air, payload, or nothing;
cold side can connect to incoming air or to exhaust output, but that
could be just two check valves), proportional control over the
incoming air fan, and, if you want to run the main combustion chamber
lean, bang-bang control over the fuel injection.  If you don’t, you
also need some kind of proportional control over the extra air
injected into the afterburner chamber.  So that’s an oxygen sensor, a
temperature sensor, nine relays or similar for the valves, and two fan
speed control lines.  Probably it would also be a bad idea to omit
thermal overload switches like those in microwave ovens on the cold
side of the regenerators.

You also need an igniter to start up the main combustion chamber,
which can be done in lots of ways.  If your fuel is gasoline or gas,
maybe you could just use a sparkplug, but in a lot of other cases you
probably want something more like a butane torch.

But that’s just enough to barely work, maybe.  I’d want temperature
*sensors* for the input air, the output of the main combustion
chamber, the output of the afterburner (if separate — another
incentive to delete it), and the input and output of each regenerator
chamber, and a backup temperature sensor inside the kiln chamber to do
an emergency shutdown in case of sensor failure: ten more temperature
channels for a total of 11.  Thermocouples would probably respond
faster than RTDs improvised from quartz-halogen bulbs, despite lower
precision, and apparently commercial RTDs only go up to 500°, which is
freezing cold.

With this collection of temperature sensors the microcontroller can
slightly randomly vary the afterburner injection, the fuel flow, and
the airflow, and infer immediately the derivatives of the resulting
temperatures, and indeed the local linearization of the entire output
transfer function — a trick that is useful for all kinds of control
systems, not just this one.  If there are important hidden variables,
like the temperature of the sand, the humidity of the air, or the
amount of payload in the kiln, you ought to be able to infer their
existence and rough dimensionality from a principal components
analysis or something, and then correct for them.
