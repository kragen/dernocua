I was thinking that on small scales (sub-meter, especially
sub-millimeter) it might be more economical to reduce metals from ores
by aqueous electrowinning than by smelting, because maintaining large
thermal gradients is very difficult.

If the things being constructed are themselves small, the strength of
materials is not very important, because at small scales even very
weak materials are strong enough to hold together except at very large
accelerations.  Metals, however, have some other interesting
properties: they can conduct electricity, they have very low vapor
pressures and so can withstand exposure to space, and they can be
readily shaped by electrochemical machining.

Macroscopically, hardness is very important for abrasion or cutting,
but I suspect that these shaping processes, like sliding-contact
joints, will not be very usable at small scales because of the
rapidity of surface wear and the comparatively large forces involved
in surface contact.  However, at scales above where this is true,
hardness is still important, because it determines what can cut what
else.

Casting and molding are also very important shaping processes at the
human scale.  At submillimeter scales, the same thermal problems that impede XXX

pH, CO2, H2O, O2

pressure

Thermal versus electrical insulation: what about *not* electrowinning?
----------------------------------------------------------------------

Consider the [Ellingham diagram][0] for iron, which shows that
smelting iron requires a temperature of at least 700°, more
practically 1000° or more.  If outside the smelting apparatus the
temperature is 25° then we have some 975° of temperature difference.
If we have a meter of refractory insulation, that’s 975 K/m.
[Vermiculite’s insulating value is about 16-17 K m/W][1], a
conductivity of about 0.06 W/m/K, giving about 60 W/m² with that
gradient, a heat flux which is, in the steady state, uniform
throughout the thickness of the material.  [Aerogel is about three
times as good, insulating firebrick about three times worse,][2] and
most other insulating materials are in between.  The worst insulator
of all, diamond, is about 1000 W/m/K.

[0]: https://en.wikipedia.org/wiki/Ellingham_diagram
[1]: https://en.wikipedia.org/wiki/List_of_insulation_materials
[2]: https://en.wikipedia.org/wiki/List_of_thermal_conductivities

Now suppose we scale the apparatus down by a linear factor of 1000,
cutting the insulation thickness to 1 mm.  Because the thermal
gradient has increased by a factor of 1000, we are now losing 60
kW/m².  This poses a real difficulty inside the apparatus.  Because
the surface area covered by insulation has increased by a factor of a
million (say from 600 m² to 600 mm²) so we are dissipating only one
thousandth as much power as before to maintain the kiln at smelting
temperature; but the volume over which that power must be generated
has diminished by a factor of a billion (say to 1 milliliter),
requiring a million-fold increase in the power density of our heating
elements, say to 35 W/ml, which is achievable but problematic.
Scaling down further rapidly becomes impossible; at 1 micron thickness
we are losing 60 MW/m², which for a 10-micron cube amounts to 36
milliwatts.

It also poses a difficulty outside the apparatus, because removing 60
kW/m² requires either radiation at an uncomfortably high temperature
(“60 suns”, as they say for solar concentrators) or a lot of coolant,
but this is a less serious problem.

Scaling in the opposite direction, we would reach a point where even
shitty insulating materials would thermally insulate adequately.

High-temperature processes are possible in a low-temperature
environment at the micron scale if they can be carried out very
quickly and intermittently.  For example, a cubic micron of material,
weighing on the order of 5 picograms, can be heated to 2000° for a
short period of time with an energy on the order of 10 nanojoules.  It
cools off through conduction with on the order of a milliwatt, so
several milliwatts is required to reach this temperature, which then
cools off on a timescale on the order of a microsecond.  Lasers and
electron beams are straightforwardly capable of being switched with
submicrosecond timescales and delivering such power densities.

Resistance heating is also straightforward.  10 milliwatts at 10 volts
is a milliamp and thus 10 kΩ.  If our joule heater is amorphous carbon
at 6 × 10<sup>-4</sup> Ω m, a 1-micron cube of it would give us 600
ohms; we could either increase the current to 4 mA and reduce the
voltage to 2.4 volts, or we could increase the aspect ratio of the
heating element, but either way it seems clear that we will have no
trouble reaching the desired temperatures on the desired timescale
with easily constructed circuitry.

Electric arcs and pseudosparks are another candidate method for
achieving such temperatures rapidly enough.

By contrast, no metal needs as much as ten volts to reduce it.
[Common insulators][3] have electrical resistivities of
10<sup>11</sup> Ω m and up, the best ones exceeding 10<sup>23</sup> Ω
m, while conductors are in the neighborhood of 10<sup>-9</sup> Ω m.
Ten volts across a millimeter of a 10<sup>15</sup> Ω m substance like
sulfur or dry wood produces a current of about 10 pA/m² and thus 100
pW/m², almost 15 orders of magnitude less than the thermal leakage
calculated above through a thermal insulator for the temperature
needed to smelt iron.  If the linear approximation for conductivity
were accurate this far down, a 1-nanometer-thick layer of such an
insulator would permit only 0.01 mA/m² (and 0.1 mW/m²) of conduction.
In fact [breakdown voltage][4] becomes a much more significant concern
than energy loss to conduction; fused silica can withstand some 500
volts per micron, but other materials are closer to 10, so they’d need
over a micron of insulation.  [At small scales vacuum becomes the best
choice of insulator][5], since most metals don’t suffer field emission
until over a gigavolt per meter, which would be 0.01 microns of
insulating vacuum.

[3]: https://en.wikipedia.org/wiki/Electrical_conductivity
[4]: https://en.wikipedia.org/wiki/Dielectric_strength#Break_down_field_strength
[5]: https://en.wikipedia.org/wiki/Field_electron_emission

A micron-thick wire at 10<sup>-9</sup> Ω m has 1.2 kΩ/m of resistance,
which is an almost entirely insignificant 1.2Ω/mm.  So electrical
transmission is not perfectly efficient but it does not pose
feasibility problems for micron-scale electrowinning in the way that
thermal conductivity does for micron-scale carbothermic reduction.

Metal selection
---------------

The eight ancient metals are iron, gold, copper, lead, tin, silver,
mercury, and, in India, zinc.  Today I think the most important metals
are aluminum, iron, copper, zinc, tin, tungsten, nickel, chromium,
lead, cobalt, molybdenum, vanadium, magnesium, titanium, platinum,
gold, zirconium, and the semimetals carbon and silicon.  LME’s
“non-ferrous” category includes aluminium, copper, zinc, nickel, lead,
tin, aluminium alloy, NASAAC (“North American Special Aluminum Alloy
Contract”), “aluminium premiums”, alumina, and aluminium scrap;
“precious” is gold, silver, platinum, and palladium; and “EV”
(“electric vehicle”) is cobalt, molybdenum, and lithium.

Of course many other metallic elements are widely used, in an oxidized
form, such as calcium, sodium, and potassium, and there are niche uses
of almost all of the metals.  But what I’m mostly concerned with here
is *reducing* metals from their oxidized form.

Aluminum
--------

Aluminum is resistant to corrosion in air, nearly as abundant as iron,
and although it is not as strong as steel per volume, it is stronger
per weight, much easier to shape, and more conductive per mass than
copper.  It also has an astoundingly high boiling point, 2470°, and an
extremely useful oxide.  65 million tonnes are mined per year, and it
costs about US$2/kg.

Unfortunately, there is no known way to electrowin aluminum in an
aqueous solution; metallic aluminum has a -2.33-volt standard
electrode potential to reduce to hydroxyls, while hydrogen is only
-2.23 volts, so aluminum will steal oxygens from hydronium.  Instead
aluminum is electrowon by dissolving alumina in cryolite
Na<sub>3</sub>AlF<sub>6</sub>, which requires a temperature around
1000°; neat cryolite melts at 1012°, but the eutectic is only 960°.

Of my list of “important metals” above, magnesium, titanium, and
zirconium have the same problem, but the others should *all* be
electrowinnable with low-temperature processes.

Alternative processes for reducing aluminum might include plasma
electrolysis, mass spectrometry, electron-beam reduction *in vacuo*,
and simple carbothermic reduction using intermittent heating.

Iron
----

Iron is one of the most abundant and strongest metals, and it can
withstand moderate heat (1500° or so without oxygen, much more than
aluminum or brass, though not in the same ballpark as sapphire,
graphite, tungsten, molybdenum, etc.).  It’s the main metal used for
construction and machinery, having mostly displaced the more expensive
bronze and brass as the humans improved their techniques for shaping
the more stubborn iron.  A couple billion tonnes of it are mined per
year, and I think scrap iron costs about 25¢/kg (US$213/ton in 02020).

Electrolytic iron is commercially used in cases that require
especially high purity or small particles, such as cereal
fortification, powder metallurgy, or high-coercivity powdered-iron
magnetic cores.

[US Patent 4,134,800][6] from 01979, by Prasanna K. Samal and Erhard
Klar, describes one process, using a bath of ferrous sulfate (36-40
g/l of iron ion) and ammonium sulfate (24-28 g/l of ammonia ion), with
1.4-1.6 grams of iron per gram of ammonium, a pH of 5.6-6.0, a
temperature of 38°-49°, and 18-26 amps per square foot (194-280 A/m²),
which they say isn’t critical.  Their declared aim was to make the
iron more brittle so it could be ground, which they hoped to achieve
by iron hydroxide formation.  As a “prior art bath” they gave as an
example 50 g/l ferrous ions, 13 g/l ammonia ions, pH 5.4, 38°-43°, 22
A/ft² (237 A/m²).  They carefully didn’t mention their voltage,
electrode spacing, agitation, aeration, electrolytic cell size (1
liter or 1 tonne?), or Faraday efficiency, and they didn’t mention any
other additives, which hopefully they didn’t have.

[6]: https://patents.google.com/patent/US4134800A/en

If you had sulfate, you could presumably digest iron ores with it and
then follow this process.  In fact, you could probably continuously
digest iron oxides in the sulfate electrolysis bath.

Samal and Klar cite patents 2,464,168 (Fansteel, 01949), 2,481,079
(Chrysler, 01945), and 2,626,895 (Fansteel, 01944).  A little further
searching turns up patents 1,782,909 (Pike, 01930), 2,464,889 (Pike
and Schoder, Tacoma Powdered Metals, 01949), 2,503,235 (Cain, Sulphide
Ore Process Co., 01950), 1,162,150 (Estelle, 01915), 2,538,990 (Trask,
Buel Metals, 01951), 3,041,253 (Audubert and Lacheisserie, 01962) and,
for nickel, patents 3,414,486 (Nordblom and Bodamer, ESB, 01968) and
[483,639][7] (Strap, 01892).

[7]: https://patents.google.com/patent/US483639A/en

The Estelle patent is particularly interesting for being over a
century old and claiming to make iron pyrite an economic source of
iron, which it is not at present (though the name of Cain’s company
above suggests it used to be).  He was electrolyzing ferrous
chloride, formed by digesting the pyrite with muriatic acid, and then
recycling the resulting ferric chloride solution into muriatic acid
and ferrous chloride by reducing it with sulphuretted hydrogen
(produced in the first step), producing sulfur as a byproduct.  He
says that nickel, cobalt, and zinc can be co-precipitated with the
iron, but the zinc is easily enough driven off.

Cain’s patent is especially helpful in telling us that at the time
(01946) there were two main processes for electrodeposition of iron,
one involving the dissolution of an iron anode and one that doesn’t
(because it’s digesting an oxide or something similar); and that
usually you use an asbestos anode bag to contain the crap formed on
the anode.  He says it’s good to keep the pH below 2 with muriatic
acid.  (You’ll pardon me if I prefer polyethylene or polyester to
asbestos.)

Audubert and Lacheisserie (concerned with fine particle size) say you
can use most ferrous salts, but sulfate and chloride are best, and
that if you’re getting oxidized iron, either you have oxygen dissolved
in the bath or you have too much ferric iron, and that they use 0.65
volts.

Anyway, so it seems like it’s slightly tricky, but not nearly as
tricky as you’d assume from the negative standard electrode potential
of iron.  And I guess it would have to be not that tricky for Edison’s
nickel-iron battery to be rechargeable.

Copper
------

While iron is crucial for moderate temperatures and strength, the much
less abundant copper is crucial for electrical conductivity,
low-friction bearing surfaces for iron parts, corrosion resistance in
oxygen atmospheres, and high thermal conductivity for heat exchangers.
25 million tonnes are produced per year; it costs US$6.20/kg.

Copper is so easy to electrodeposit (and electro-etch) that it’s
easier to enumerate the cases where it *won’t* work: where you’re
trying to form an adherent deposit on an electrode that copper will
spontaneously oxidize, such as iron, and when the anions in your
electrolyte don’t form a soluble copper salt (among the usual
suspects, these are iodide (mostly), cyanide (without enough ammonia),
thiocyanate, hydroxide (i.e. bases or just water), oxalate (again,
without enough ammonia), and phosphate).  The USGS says that there are
currently 3 electrolytic refineries for copper in the US and 14
electrowinning facilities.

Zinc
----

Zinc is used to add corrosion resistance to iron in oxygen atmospheres
(its main industrial use today), in Zamak, as an alloying element for
copper to form brass, and in its oxidized form, as a white pigment.
It has a remarkably low boiling point, 907°.  12 million tonnes are
produced per year; it costs US$2.40/kg.

Despite the name “galvanization”, zinc coating was originally done not
as electroplating but as a hot-dip process, which is still the most
common way to do it today.  But electroplating zinc is also a common
thing to do, and there’s lots of historical work on producing zinc
powder electrolytically.

“Zamak” is a family of low-temperature zinc-based casting alloys, some
of which have strength comparable to steel; Zamak 2 (4% aluminum, 2.7%
copper, 0.04% magnesium) has a tensile strength of 330 MPa, a Young’s
modulus of 96 GPa, and melts over the range 379-390°.  Unfortunately
the aluminum is a necessary component, and slight lead impurities will
wreck Zamak with zinc pest.

### Brass ###

In modern practice, brass (about 20% zinc, US$5.40/kg) has mostly been
displaced by steel, which is stronger, harder, stiffer, lighter, and
cheaper (more than 20× cheaper by weight), and, in high-carbon cases,
can be hardened by heat treatment.  But brass still has many
small-volume niches.

It is enormously easier than steel to cast or, especially with a bit
of lead, to cut.

It’s more corrosion-resistant in oxygen atmospheres and in water,
especially salt water; “admiralty brass” is 70% copper, 29% zinc, and
1% tin (see below) and is an especially good formulation for this.

Brass has higher thermal and electrical conductivity than steel, and
so in particular it lasts much longer for EDM electrodes.

It has much lower friction on steel than steel does, so it can be used
for plain bearings (journals), as a cheaper and less durable
alternative to bronze (though babbitt is often better still).

It’s used as a solder to join steel parts (“brazing”), which allows a
stronger connection than bolts, with lower temperatures and less
distortion than welding, and it can join a wider collection of
materials than welding, including tungsten carbide (see below).

Because it’s softer than steel, brass doesn’t produce sparks
and doesn’t mar steel surfaces, so in some environments and for some
purposes brass hammers and other tools are preferred to steel.

Finally, its yellow color is often used for aesthetic purposes.  With
just zinc and copper, you can make silver (zinc), red (copper), and
yellow (brass).

### Galvanizing ###

Galvanized steel, steel coated with zinc, has mostly replaced tinplate
as an anti-corrosion coating.  Zinc is somewhat toxic in food (the
oral rat LD50 of the highly soluble zinc chloride is 350 mg/kg, and
it’s also used topically to induce skin necrosis in “black salves”)
and produces toxic fumes when heated near its boiling point, so this
isn’t done for tin cans or cooking pots, but it’s widespread for
things like buildings.  As mentioned above, this is usually done as a
hot-dip thing, but it can be done through electrodeposition.

Tin
---

Tin is crucial for soldering electronics; alloyed with copper it is
bronze; alloyed with copper and antimony it is babbitt; coating steel
it prevents corrosion; and it melts at only 232°.  The largest of its
many uses today is as a nontoxic anti-corrosion coating for steel in
“tin” cans.  Bronze can withstand both higher temperatures and more
stress than brass, while retaining brass’s easy castability.  Babbitt,
which makes the best plain bearings, is tin with 2.5-5% copper
(occasionally as high as 8.5%) and 4-8.5% antimony.  Some 0.3 million
tonnes of tin are mined per year, and it costs about US$18/kg.

You might think its numerous oxidation states (2+ (stannous) and 4+
(stannic), sometimes + and 3+, as well as neutral and negative states)
would make it difficult to electrowin.  The sulfate, bromide,
chloride, and fluoride, all divalent, are water-soluble; the iodide is
mildly so, and the bromide is additionally soluble in donor solvents
like DMSO.  There are also a tetravalent bromide, chloride, fluoride,
iodide, sulfide (sphalerite), and nitrate; the tetravalent chloride is
a liquid that mixes with all kinds of nonpolar liquids, and the
tetrabromide is also water-soluble.  The nitrate is, unusually,
unstable in water.  The sulfate is preferred when stannic ions are
undesired, because there is no stannic sulfate.

[Tin electroplating is widely practiced][50] using acid baths (I’m
guessing sulfuric), alkaline baths (I’m guessing stannate; you can get
sodium stannate by digesting tin with lye), and methylsulphonic acid
baths.  It’s often codeposited with lead, copper, silver, zinc, and/or
bismuth.

[50]: https://www.sharrettsplating.com/blog/the-tin-plating-process-a-step-by-step-guide/

Tungsten
--------

Tungsten has the highest melting point of any metal (3422°), almost as
high as carbon’s sublimation temperature of 3642° and the melting
points of tantalum hafnium carbide (3990°), tantalum carbide (3880°),
and hafnium carbide (3928°), though well short of tentative results
for [hafnium carbonitride][66] (4200°).  Tungsten also has the highest
boiling point of all elements, an astounding 5930°.  It’s an essential
ingredient in high-speed steel, though vanadium and molybdenum can
replace it to some extent, and tungsten carbide (the main current use
of tungsten) has largely replaced high-speed steel in modern
steel-cutting practice.  It’s also essential to TIG welding and
important in vacuum tubes and incandescent lights.  Some 84000 tonnes
are mined per year, 80% in China, but I don’t know what it costs.

[66]: https://phys.org/news/2020-05-scientists-heat-resistant-material.html "Fabrication of ultra-high-temperature nonstoichiometric hafnium carbonitride via combustion synthesis and spark plasma sintering, by Veronika S. Buinevich et al., Ceramics International (2020), 10.1016/j.ceramint.2020.03.158"

Carbides of vanadium, molybdenum, niobium, and the titanium-group
metals are possible substitutes for tungsten carbide.

The current industrial process for smelting tungsten is long and
involved, but the main article of commerce is tungsten trioxide, which
is then either carbothermally reduced or reduced with hydrogen.

[Experiments have been made in electrowinning of tungsten][52] at
1080°, but also [US patent 2,384,301][53] (Harford, 01944) and others
describe electrodeposition methods for reducing tungsten.  Harford
recommends complexing your tungsten with 25% ethylenediamine in water,
using 25 A/ft², but he explains that people previously just used
cyanide.

[52]: https://www.911metallurgist.com/electrolysis-tungsten-metal-tungsten-carbide/
[53]: https://patents.google.com/patent/US2384301

The titanium group
------------------

I think low-temperature electrowinning of titanium, zirconium, and
hafnium is basically a lost cause with current electrochemistry.  This
is a real shame, because titanium is as strong as iron and much
lighter.

Perhaps even more interesting than the metals, though, are the
carbides, nitrides, borides, and oxides of this group, which are
[outstanding materials in many ways][72]: ultra-high temperature
ceramics, superhard, transformation-toughened, solid electrolytes,
photocatalysts, super-high-kappa dielectrics, resistant to chemical
attack, high-conductivity semiconductors, etc.  They are often
produced from the metals, but for example zirconium diboride can be
made from refined zirconia, boria, and metallic magnesium, or from
boron and zirconia, or boron carbide and zirconia.  Nitrides can be
made by reacting the oxides with ammonia or nitrogen, etc.

[72]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6747801/

However, of the oxides, only titania (rutile or anatase) occurs in
nature.  Zirconia (mixed indiscriminately with hafnia) is obtained
from zirconium silicate (zircon or jargoon) by calcining.

Electrowinning to separate metals
---------------------------------

In most cases it’s difficult to electrodeposit alloys; metals tend to
get separated from each other by the process.  Sometimes this is
because of differing solubilities; lead sulfates, for example, are
insoluble, so lead won’t electrodeposit from a sulfate bath.
(Chromium has both soluble and insoluble sulfates, and of course
barium and calcium have insoluble sulfates, but they’re too reactive
to electrodeposit from water.)  But that’s not unique to
electrochemistry; that’s just regular heap-leach mining chemistry.

The much more interesting fact is that by setting the voltage low
enough, you can generally electrodeposit *just a single metal* from an
electrolyte containing different kinds of cations, because no two
metals have exactly the same electrode potential.  This is potentially
*very* interesting: it’s a high-throughput, high-efficiency, small,
low-temperature way to separate many different ionic species.  It
won’t work for every case, because of considerations like those
mentioned above for iron.  But it will work in many cases.

By the same token, it’s often possible to dissolve just one metal out
of an alloy anode by setting the voltage at the right level.

Single displacement and the Tree of Saturn
------------------------------------------

In general if a metal can be electrowon it can also be precipitated by
a single displacement reaction from a more reactive metal.  [Standard
electrode potentials][1] include:

<table>
<tr><th>solutes<th>metal<th>E°/V<th>electrons
<tr><td>Li<sup>+</sup> + <i>e</i><sup>-</sup>
    <td>Li(s)
    <td>-3.0401
    <td>1
<tr><td>Na<sup>+</sup> + <i>e</i><sup>-</sup>
    <td>Na(s)
    <td>-2.71
    <td>2
<tr><td>Mg<sup>2+</sup> + 2<i>e</i><sup>-</sup>
    <td>Mg(s)
    <td>-2.372
    <td>2
<tr><td>Al<sup>3+</sup> + 3<i>e</i><sup>-</sup>
    <td>Al(s)
    <td>-1.662
    <td>3
<tr><td>Ti<sup>2+</sup> + 2<i>e</i><sup>-</sup>
    <td>Ti(s)
    <td>-1.63
    <td>2
<tr><td>Zr<sup>4+</sup> + 4<i>e</i><sup>-</sup>
    <td>Zr(s)
    <td>-1.45
    <td>4
<tr><td>V<sup>2+</sup> + 2<i>e</i><sup>-</sup>
    <td>V(s)
    <td>-1.13
    <td>2
<tr><td>2H<sub>2</sub>O + 2<i>e</i><sup>-</sup>
    <td>H<sub>2</sub>(g) + 2OH<sup>-</sup>
    <td>-0.8277
    <td>2
<tr><td>Zn<sup>2+</sup> + 2 <i>e</i><sup>−</sup>
    <td>Zn(s)
 	<td>-0.7618
 	<td>2
<tr><td>Ta<sup>3+</sup> + 3 <i>e</i><sup>−</sup>
    <td>Ta(s)
 	<td>-0.6
 	<td>3
<tr><td>Fe<sup>2+</sup> + 2 <i>e</i><sup>−</sup>
    <td>Fe(s)
 	<td>-0.44
 	<td>2
<tr><td>Co<sup>2+</sup> + 2 <i>e</i><sup>−</sup>
    <td>Co(s)
 	<td>-0.28
 	<td>2
<tr><td>Ni<sup>2+</sup> + 2 <i>e</i><sup>−</sup>
    <td>Ni(s)
 	<td>-0.25
 	<td>2
<tr><td>Sn<sup>2+</sup> + 2 <i>e</i><sup>−</sup>
    <td>Sn(s)
 	<td>-0.13
 	<td>2
<tr><td>Pb<sup>2+</sup> + 2 <i>e</i><sup>−</sup>
    <td>Pb(s)
 	<td>-0.126
 	<td>2
<tr><td>2H<sup>+</sup> + 2 <i>e</i><sup>−</sup>
    <td>H<sub>2</sub>(g)
 	<td>0
 	<td>2
<tr><td>Cu<sup>2+</sup> + 2 <i>e</i><sup>−</sup>
    <td>Cu<sup>+</sup>
 	<td>+0.159
 	<td>1
<tr><td>Cu<sup>2+</sup> + 2 <i>e</i><sup>−</sup>
    <td>Cu(s)
 	<td>+0.337
 	<td>2
<tr><td>O<sub>2</sub>(g) + 2H<sub>2</sub>O + 4<i>e</i><sup>-</sup>
    <td>4OH<sup>-</sup>
 	<td>+0.401
 	<td>4
<tr><td>Cu<sup>+</sup> +  <i>e</i><sup>−</sup>
    <td>Cu(s)
 	<td>+0.52
 	<td>1
<tr><td>Ag<sup>+</sup> +  <i>e</i><sup>−</sup>
    <td>Ag(s)
 	<td>+0.7996
 	<td>1
<tr><td>Au<sup>3+</sup> + 3 <i>e</i><sup>−</sup>
    <td>Au(s)
 	<td>+1.52
 	<td>3
</table>

[1]: https://en.wikipedia.org/wiki/Standard_electrode_potential_(data_page)

So, if you have some divalent lead salt such as lead acetate in water,
and you put a less noble metal into the water, such as aluminum,
titanium, zirconium, vanadium, zinc, tantalum, iron, cobalt, nickel,
or even tin, you should expect the lead to precipitate, dissolving the
other metal into the water; this is the famed Tree of Saturn of the
alchemists, and when instead done with a soluble salt of silver, it is
the Tree of Diana.  The same thing explains the immersion plating of
silver ions onto copper with brief immersion [at 50° to 60°][2],
immersion plating of gold onto copper at 80° to 90°, [immersion
plating of gold onto nickel][3], and so on.

[2]: https://www.corrosionpedia.com/definition/660/immersion-plating
[3]: https://en.wikipedia.org/wiki/Electroless_nickel_immersion_gold

As I understand it, the difficulty in electrowinning aluminum,
magnesium, and the titanium-group metals is precisely that they have a
more negative electrode potential than hydrogen, so they form an
“immersion plating” of hydrogen, consuming the water and the metal.
Normally they are protected from this reaction by an impermeable oxide
layer, so they don’t dissolve spontaneously in water the way lithium
and sodium do.

So, in theory, you ought to be able to precipitate out any of the
nobler metals from solution by starting with a hunk of zinc.
