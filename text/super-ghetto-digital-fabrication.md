Suppose we have positional control precise to within a few microns,
but not much force, power, rigidity, money, or access to pure
materials.  How can we leverage this into a comprehensive flexible
digital fabrication capability?

Geometry
--------

The standard ghetto metalworking processes are stick welding, bending,
drilling, hammering, and angle grinding.

Digitally-controlled stick welding is maybe a bit difficult, but
should be feasible, since “welding robots” have been a thing for
decades; controlling the power supply should make it much easier to
strike the arc with a TIG-like high-frequency start, you can avoid
sticking the electrode because you don’t need to enable high current
until an impedance measurement shows the electrode has been lifted
from the surface; voltage feedback should provide a trustworthy and
low-latency indication of the arc length once it’s struck; current and
polarity duty cycle can be adjusted rapidly to control electrode
melt-off rate; and precise toolpath control should dramatically
improve weld quality.  To the extent that you can substitute a CO2
hose (“MAG welding”) for standard stick-welding flux, you can avoid
slag that needs to be chipped or ground off; this should be no problem
when welding on steel.  “Short-circuiting metal transfer” as in
MIG/MAG welding should be a possibility.  This kind of process might
allow “stick welding” using plain steel baling wire, and thus 3-D
printing in mild steel.

Model-predictive control of the temperature distribution across the
workpiece, with webcam feedback from surface temperatures, is probably
critical to this.  The dimensional precision of the result will
probably be compromised by the contraction of the deposited metal,
which is one reason welding is conventionally used for permanent
assembly of prefabricated parts rather than large material buildups
(though adequate toolpath planning could potentially reduce this
problem), and the resolution will be limited by the surface tension of
the weld puddle.

Bending of wire, rebar, or sheet-metal strip can be very precise if
you have a good model of the material’s work-hardening properties, and
fairly fast and low-power as well.  But this probably requires
annealing the metal (to eliminate unknown work-hardened zones) and
possibly keeping it hot during fabrication.  Bending of sheet metal is
normally done with sheet-metal brakes, press dies, or beading
machines.  Digital fabrication of press dies is now widespread and can
often use cheap plastics.

Drilling metal is pretty high power and imprecise; it may not be very
suitable for digital fabrication as a general technique, although
digitally controlled drilling might be a useful supplement to other
processes, for example to do initial piercing of a workpiece before
further processing.  Manually drilling metal or wood after holes have
been precisely started by a slower digitally-controlled process is
also likely useful.

Digitally-controlled grinding should in theory be able to generate
very precise geometry (submicron), particularly since the difference
between contact and non-contact between a grinding wheel and the
workpiece is not at all subtle; it is easy and fast to detect either
the light from sparks (maybe 100 microsecond latency) or the sound
(maybe 20 microseconds if you have a microphone on the workpiece).
This should be able to give a pretty good indication of where the
surface of the workpiece is, to within the error of your model of the
grinding wheel’s geometry, and you can go back and measure points on
the workpiece in between grinding passes by detecting its
conductivity.  Large grinding wheels are high power when grinding
continuously (a US$40 Black & Decker G720N 115mm-diameter 11000rpm
angle grinder is 820 W) but not intermittently, and small ones need
not be high power or even noisy.

Digitally controlled hammer forging of metal seems potentially very
promising, especially since it could produce work-hardened results,
but it involves a lot of variables and probably requires annealing
steps.

Aluminum foil should be easy to cut to desired shapes under computer
control with just a razor blade.  If it’s on a softish surface,
running a small hard wheel over it under computer control should be
sufficient to put ribs into it to give it a little bit of rigidity and
define creases for origami panels.  Automatically folding the origami
or assembling the panels is probably pretty difficult, but doing it
manually is certainly practical for initial prototyping.  The precise
origami shapes thus formed can then serve as tiny molds for
inexpensive lightweight castable materials including candle wax, pine
pitch, polyethylene cutting boards, and polypropylene bottle caps and
rope.  If desired, the aluminum foil can then be removed
electrolytically with a saltwater or vinegar electrolyte or
non-electrolytically with lye or muriatic acid.

Aluminum foil can also be cut with low side forces and tiny holes, but
probably lower positional precision, with sparks from a copper point
or graphite electrode.  Normally you would do this in air but doing it
under water or oil may provide better precision.

Mild sheet steel is easy to come by and should be easy to cut
precisely but slowly with electrolytic machining with salt water,
vinegar, or sulfates.  Such cutting can include living hinges that
make it easy to bend the resulting cut sheet into precise shapes.

Shapes roughly fabricated in nearly any metal can be brought to
precise geometry by electrolytic machining or electric discharge
machining, which produce no side forces and no heat-affected zone.

Electrolytic machining of glass may be feasible; see file
`electrolytic-glass-machining.md`.

Styrofoam is easy to come by and can be easily cut under digital
control with a hot wire.  Suitable wire materials that are easy to
come by include copper, steel, stainless steel, and nichrome.

Rigid, brittle fine foams such as some of the materials mentioned
later offer enormous advantages for digital fabrication: they are as
easy to cut to dimension as very soft materials like paraffin wax
(though much more abrasive), or even easier, but retain the
dimensional stability and refractory properties of the corresponding
solid material, which are superior to even some hard metals, and their
Poisson ratio is effectively 0; also, and related to their ease of
cutting, they are much more resistant to fracture propagation than the
corresponding solid materials.  The only traditional materials with
similar properties are Mykron/Mycalex and exotic mica-containing
machinable glass-ceramics.

Corrugated cardboard is very abundant and has a spectacular
strength-to-weight ratio and good dimensional stability in two
dimensions; it can be cut with razor blades to form precise 2-D shapes
and pressed with roller wheels to form precise crease lines, which can
then guide origami assembly.  Thicker corrugated cardboard may require
higher-powered cutting with a wire saw or hacksaw.  Cardboard’s worst
disadvantage is that it is very vulnerable to water.

Pottery clay bodies are readily available and very easily formed or
extruded, although their stickiness can be a problem, and there is
currently no software available that can model their behavior well
enough to control their forming.  If fired, they can produce hard,
refractory, dimensionally stable materials with substantial strength,
but if not fired, they can easily be recycled.

Digitally guided sandblasting (“abrasive jet machining”) requires
compressed air and consumable nozzles, but offers the possibility of
cutting desired geometry into a wide variety of materials, even very
hard ones, as well as selectively abrading surfaces, exposing fresh
unreacted material.  This produces such low side forces and heat loads
that it can be used even on thin glass or eggshells, though getting it
to work on aluminum foil might be too much to ask.  Although it even
works on metals, it is substantially more effective on brittle
materials.  Careful choice of abrasives can make this a
material-selective process; in industry, for example, glass-bead
blasting is used to remove paint without damaging steel, and dry-ice
blasting is used for degreasing without damaging paint.

The easiest abrasive to use for sandblasting is of course silica sand,
but crystalline silica dust causes silicosis, to the point where
sandblasting with silica has been outlawed in many countries.  (This
doesn’t solve the problem if you’re cutting something like granite, of
course, and granite is a very desirable thing to be able to cut
because of its dimensional stability.)  Sapphire, carborundum,
apatite, metal oxides, or powdered waste glass may be preferable
abrasives.

A different way to do digitally controlled abrasive cutting might
involve passing a fabric loop loaded with loose, perhaps wet and
sticky, abrasive across or through the workpiece.  This is pretty
similar to a wire saw, but I think the flat-tape shape of the fabric
potentially provides a better tradeoff between breakage risk and kerf
width.  To make a given cut, the tension on the leading edge of the
fabric needs to be just as high as it would be without all the cloth
behind it, but if that turns out to be too high, the rest of the cloth
doesn’t have to rip as well.

Digitally guided 2-D plasma or oxy-fuel cutting is of course already a
widespread process, and is much faster than most alternatives; laser
cutting is making significant inroads here in recent years, but would
be much more difficult to improvise.

The “[Oogoo][12]” Sugru-like silicone putty mix of cornstarch and
hardware-store silicone caulk is thixotropic with a working time of
minutes to hours (5 minutes with a 1:2 ratio, an hour with a 5:1
ratio), and thus eminently suitable for digital fabrication through
extrusion or forming.

[12]: https://hackaday.com/2010/10/11/oogoo-a-home-made-sugru-substitute/

Plaster of paris can be foamed with baking powder, then cut to shape.
It adheres well to quartz sand, and quartz sand or quartz flour can be
useful functional fillers for it.

Charcoal is an easily cut material related to carbon foam (see below),
but it tends to suffer pervasive cracking from thermal contraction
during its formation, which may limit its uses.

Adding strength to established geometry, or otherwise switching materials
-------------------------------------------------------------------------

A lot of the processes in the previous section for converting digital
data into a physical three-dimensional shape are only applicable to a
narrow range of materials, often with fairly poor properties for
anything besides being shaped.  So it’s important to be able to
transfer a geometry fabricated in one material into some other
material.

Hardware-store silicone caulk is a promising material for molding for
a few different reasons.  It’s capable of holding detail down to the
micron level; it’s fairly inert once set, withstanding, for example,
gasoline; it’s thermally stable up to typically 300° (though the red
high-temperature formulation commonly used for auto repair as “RTV”
goes a bit higher); it’s fairly dimensionally stable (though it does
shrink a little, unlike some other silicones); and it’s elastomeric.
Being elastomeric makes it easy to pry it out of molds made of a
harder material, and also makes it easy to peel molds made out of it
off castings of a harder material.  Also, it won’t remain stuck to
polyethylene or polypropylene, and reportedly also not to PVC or
polycarbonate.

Shapes initially fabricated in aluminum foil can be thickened by
electroplating/electroforming them, most easily in copper or brass.
Although it is important for the copper to form a solid layer, it is
not necessary for it to adhere firmly to the aluminum, as is usually
desired in electroplating processes.  Because the aluminum foil is the
cathode in the electrolytic cell, it is possible to use electrolytes
such as muriatic acid or lye that would normally destroy it
immediately.  A potentially larger concern is the risk of deformation
from the surface tension of water, which can be reduced with
surfactants and the substitution of alcohol for water.

Electroforming on non-conductive shapes is conventionally done with
graphite powder dispersed in some solvent and painted onto the object.
In some cases you can disperse the graphite in a solvent that softens
or dissolves the surface of the object, welding the graphite to it;
dichloromethane is reported to work for PLA.

Polypropylene can be sufficiently stiff for molding of plaster of
Paris or portland-cement concrete, which can provide a polypropylene
part with much greater rigidity and thermal stability than
polypropylene alone.  In the case of plaster, it may be possible to
later strengthen the plaster by filling internal channels in it with
molten metals such as aluminum, brass, or cast iron.

Styrofoam forms, even those that can be cut by hot wires, can be
stacked up into forms for low-temperature molding (for example, of
portland cement or plaster of paris), or they can be wrapped in
papier-mache-family strengthening materials such as cotton cloth
soaked in plaster of Paris or fiberglass window screen soaked in
non-alkaline sodium silicate.

Plaster shapes have little tensile strength or rigidity, but if they
are suitably designed, automatically winding them in pretensioned wire
can improve this.  Steel wire has higher rigidity and less creep than
copper wire but may be harder to find; aluminum wire is available by
dissecting window screens, or the woven screening can be applied
directly.  Winding subsequent layers at different angles, as is done
for glass-fiber pressure tanks, can provide tensile strength in two
dimensions instead of just one.  Brazing or soluble silicates may be
suitable means for obtaining adhesion between layers of winding.

XXX stuccoing

High temperatures
-----------------

A lot of attractive fabrication processes, such as firing clay,
require high temperatures at some stage; so, too, does making many
exotic materials (see section below).  Making equipment that survives
these temperatures requires refractory materials, often insulating
refractories, although in some cases it’s adequate to just use a pile
of quartz sand (good up to 1500°, though not very insulating) or
vermiculite (insulates better, I think good to 1100°).  Aluminum foil
can’t resist high temperatures itself but is often useful for
reflecting back radiant heat, preventing it from being lost.

Ordinary steel works up to about 1200° in a reducing atmosphere, but
carbon dioxide is not sufficiently reducing; in air it starts to
oxidize annoyingly rapidly above about 900°.  Fired clay is the usual
resort for temperatures up to 1100° or so; special clays can reach
much higher than this but are harder to find and to fire.  [Fused
quartz is maybe sometimes good to 1500° and usually to 950°][25], and
is available for example in broken space heaters and halogen light
bulbs, but it’s very difficult to cut or form.  (In some cases the
quartz tubes are adequate.)  Plaster of paris is easily formed before
hydration, and can withstand a few excursions to over 1000°, but is
not durable as a refractory.

[25]: https://www.heraeus.com/en/hca/fused_silica_quartz_knowledge_base_1/properties_1/properties_hca.html#tabs-608478-5

Soluble silicates are hard to find (see below about making them), but
can serve as adhesives for silicates such as quartz.  Typically, in
this use, rather than melting at high temperatures and falling apart,
they form new compounds with the materials they’re uniting.

Carbon foam is an excellent insulating refractory in non-oxidizing
atmospheres (good to 3642°) and can be fabricated easily from bread
dough or pancake batter, which is first heated to dry it and make it
rigid, then heated further to carbonize it.  It is very rigid and thus
easy to cut, but abrasive.  It does not adhere well to untreated
quartz fillers.  Thermoplastics alone are not suitable precursors for
carbon foam; enough thermoset ingredients such as gluten are required
to prevent the object from losing its shape before carbonizing.  If
heated sufficiently in a non-oxidizing atmosphere it may graphitize
and become electrically conductive, depending on its structure.
Carbon dioxide is sufficiently non-oxidizing.

The standard insulating refractory for low-tech pottery kilns in an
oxidizing atmosphere is a conventional pottery clay body (for example,
ball clay tempered with silica and grog) filled with particles of a
sacrificial-filler organic matter such as coffee grounds, sawdust, or
used yerba mate, which burns out upon firing.  In my experiments,
material made with 67% sacrificial filler was quite solid but could be
cut with a thumbnail, while material made with 89% sacrificial filler
was still solid but friable and permitted easy gas passage.  The
firing process produces terrible odors.

[Intumescent moldable “Starlite”-style coatings][15] may be adequate
insulating refractories for bootstrapping high-temperature
capabilities.  The precursor is an aqueous paint or paste of organic
polymers (such as cornstarch and PVA glue, or wheat flour) and blowing
agents.  Sodium bicarbonate is commonly used as a blowing agent.
Borax or boric acid substantially increases the strength of the
resulting carbon foam, and may also help to cross-link PVA in the
paste to prevent cracking from drying.

[15]: https://www.kvpr.org/post/miracle-or-hoax-uc-merced-students-attempt-recreate-remarkable-mysterious-starlite-material

Silicone caulk may work as a precursor material for composites of
graphite and carborundum, foamed or not, when heated.  Acetic-cure
silicone may cure more rapidly and foam in the process if carbonate or
bicarbonate of soda is mixed in; I have not verified this.  Oogoo
confirms that it does cure more rapidly when mixed with cornstarch.

Even if you have an apparatus that can withstand heat, where do you
get the heat?

The traditional approach for millions of years has been fire.
Ordinary butane blowtorches can hypothetically reach 1970°, but
usually don’t, which is why you can’t weld steel with them, and they
have the inconvenience of producing a lot of exhaust.  Oxy-acetylene
torches are easy to buy (though expensive to refuel) and can reach
3500°, and oxyhydrogen torches are easy to make and can reach 2800°.
Anthracite, and thus presumably charcoal, can reach 2180°.

But electric heating is much more convenient; it can be turned on or
off (or anywhere in between) instantly, and it doesn’t produce gases.
Ordinary nichrome heating elements have [maximum service temperatures
ranging from 1000° to 1260°][17], though they don’t melt until almost
1400°.  [Some varieties of Kanthal][18] have service temperatures
ranging from 1300° to 1425°, but these are harder to find.  Halogen
lamps, still available from auto parts stores as headlights even where
they’ve been prohibited for household lighting, and their filaments
may reach 2900°, but their envelopes are only designed to operate
around 500° and are typically made of fused quartz, which melts at
1600°, or aluminosilicate glasses, which melt at only about 800°.

[Carborundum “globar” heating elements are commonly rated to
1625°][19] or [1600°][20], but are also not common household items,
though it might be possible to make one; they consist of a carborundum
tube with a spiral cut in the central portion to increase its
resistance, so that the ends that protrude through the refractory wall
of the furnace can remain cool enough not to melt the metal wires that
connect to them.  The “Globar SR” design has a two-start spiral cut so
that both electrical terminals are on the same end.  Carborundum is
seriously allergic to water vapor.

Historically, the fairly expensive yttria-stabilized zirconia was also
used for globars; they melt at 2715° and have [been experimentally
used for heating up to 2100°][21].  Possibly household ceramic knives
could be used for this, though they might need to be cut to have a
central “hot zone”, similar to carborundum globars.  One disadvantage
is that they need to be preheated (for example with a flame) to become
conductive; historically, their negative temperature coefficient of
resistance was also a drawback (for example, in Nernst illumination
lamps), since it means they require a constant-current source rather
than a constant-voltage source to avoid thermal runaway.
(Carborundum, by contrast, has a positive TCR above 700°, so this
issue doesn’t arise at normal globar service temperatures.)  Nowadays
current regulation, at least, is an easy problem to solve.

[17]: https://www.heating-element-alloy.com/article/nickel-alloys-for-heating.html
[18]: https://www.kanthal.com/globalassets/kanthal-global/downloads/furnace-products-and-heating-systems/heating-elements/metallic-heating-elements/resistance-alloys_s-ka041-b-eng.pdf
[19]: https://www.americanelements.com/silicon-carbide-heating-elements-409-21-2
[20]: https://www.kanthal.com/globalassets/kanthal-global/downloads/furnace-products-and-heating-systems/heating-elements/sic-heating-elements/s-ka046-b-eng-2011-11.pdf
[21]: https://link.springer.com/article/10.1007/BF01289853

Nowadays, high-temperature heating elements are commonly instead the
exotic [MoSi2][22] instead, which is serviceable to [1750°][23] to
[1850°][24].  These are commonly used, for example, for sintering
zirconia itself, which commonly requires 1530°-1700° depending on,
among other things, sintering aids.

[22]: https://en.wikipedia.org/wiki/Molybdenum_disilicide
[23]: https://www.aegisdentalnetwork.com/idt/2017/01/hot-alone-will-not-do-the-trick
[24]: https://www.kanthal.com/en/products/furnace-products/electric-heating-elements/molybdenum-disilicide-heating-elements/

Alternative methods of electrical heating include arc heating with
consumable graphite electrodes and induction heating, neither of which
has an inherent temperature limit of its own; arcs in everyday US$200
plasma cutting torches commonly reach 20000°.  Induction heating can
keep the induction coils outside the hot furnace, and big induction
heating coils are commonly made from copper pipe (at the high
frequencies used for metals above their Curie point, only the skin of
the coil can carry current anyway) with cooling water running through
it.  Induction furnaces in industry commonly maintain metal molten by
heating the liquid metal inductively.

XXX microwave heating

Making exotic materials
-----------------------

Teflon and glass are crucial materials for their nonreactivity at
everyday temperatures.  Glass is widely available and, though it
requires a lot of practice, can be shaped with a US$10 butane torch
from the hardware store (or, traditionally, with an oil lamp and a
blowpipe); teflon can be obtained from discarded laser printer fuser
rollers, and a great deal of electical insulation is also made of
teflon, but I do not know how to distinguish teflon insulation in
discarded cables from the more common PVC.

Graphite is a crucial material for both electrodes and crucibles, the
only viable electrode or refractory for many purposes; welding shops
sell graphite electrodes, but they are graphite composites with poor
stability in reactive environments.  As mentioned above, some organics
can be graphitized in a graphitizing furnace made of carbon foam and
purged with carbon dioxide.  This requires, I think, electric heating
elements that can withstand graphitizing temperatures of 3000° (and
pure graphite itself is the only plausible option), but are more
conductive than the carbon foam itself.  Even if the carbon foam is
made from non-graphitizing carbon, it will conduct electricity once
fired high enough.

Non-graphitizing carbon crucibles, which are more resistant to
reactive environments than graphite, have been historically made from
phenolic resin, then fired at 900° in an inert atmosphere.  Other
thermosets would presumably work too, unless they pyrolyze to
graphitizing carbon (polyurethane foam, as found in pillows and
spray-foam insulation, is a common precursor); if they don’t outgas
too much they might be able to make non-porous non-graphitizing
carbon.

Soluble silicates, especially those that are neutral rather than
strongly alkaline, are likely a crucial enabling material for digital
fabrication for several reasons: they can be used directly as
refractory adhesives (for example, to make a moldable insulating
refractory from garden-store vermiculite); they bind very strongly to
silica and other silicates; when dehydrated to solidity, they can be
expanded from beads into glass foams by the application of heat,
foaming as their water boils; and they can be instantly and directly
cross-linked into insoluble silicates by the provision of polyvalent
cations such as calcium or ferrous ions, as in the traditional
colorful silicate garden, or with carbon dioxide, a feature that
promises to be important for digital fabrication by selective
solidification, perhaps even permitting 3-D printing of soda-lime
glass.  But soluble silicates are difficult to find, so we may have to
make them.

(It may be possible to leach neutral sodium silicate out of corrugated
cardboard.)

The most promising route to soluble silicates seems to be the
digestion of powdered soda-lime glass with warm aqueous alkali over
the course of hours or days.  Alkali requires quite careful handling
and can itself be difficult to obtain; the chlor-alkali process with
graphite electrodes and a porous fired-clay diaphragm can produce it
from table salt, salt-substitute potassium chloride, or alkali
carbonates, and producing it thus *in situ* may be adequate for
digesting the glass, thus avoiding any accumulation of hazardous
alkali.  Unwanted chlorine may be disposed of by passing it over hot
aluminum foil.  The traditional source for alkali is to leach it out
of wood ash, but this is normally slow, dirty, bulky, and expensive.

Although discarded soda-lime glass is abundant, it doesn’t handle
thermal shock or reactive environments well; borosilicate glass is
much more resistant, but hard to find.  Adding borate (in the form of
borax or boric acid) to discarded soda-lime glass seems like a
promising thing to try.

Sapphire is aluminum oxide; industrially this is produced in the Bayer
process by digesting bauxite with alkali to produce a soluble
aluminate, then precipitating gelatinous aluminum hydroxide by cooling
the solution (neutralizing it also works).  This hydroxide (which
crystallizes as gibbsite at a few microns per hour) calcines to
sapphire, completely if held above 1200° for an hour; it is even
possible to [calcine the hydroxide gel to a transparent porous ceramic
at 500° if you keep the electrolyte concentration near an ideal
value][10], though perhaps not if the hydroxide is derived in this
way.  Digesting (readily available) aluminum metal with alkali
produces the same soluble aluminates, and so should be an easy route
to sapphire for use as an abrasive, as a refractory (melts at 2072°),
or for abrasion-resistant ceramics; the sapphire powder sinters to a
ceramic around 1600°.  Its thermal coefficient of expansion is [an
astounding 0.6 ppm/K at ordinary temperatures,][8] though some sources
give higher value such as 7 ppm/K.

[8]: http://epsc511.wustl.edu/Aluminum_Oxides_Alcoa1987.pdf "Oxides and Hydroxides of Aluminum, Wefers and Misra, Alcoa Laboratories, 01987, 100 pp."
[10]: https://link.springer.com/article/10.1007/BF00754473 "Alumina gels that form porous transparent Al2O3, Bulent E. Yoldas, J. Mat. Sci, 10 (01975) 1856-1860"

The so-called “sodium beta alumina” that forms when heating
sodium-rich gelatinous (?) aluminum hydroxide has fast ionic
conductivity for a wide variety of monovalent cations, a property of
great interest for its use as a solid electrolyte (and one which may
be much more accessible than zirconia), used in the sodium-sulfur
battery.

The transformation sequence from the gelatinous hydroxide to sapphire
(alpha-alumina) is astoundingly complex ([8], figure 4.1); the
gelatinous form converts to the poorly ordered eta-alumina (aka
gamma-alumina or gamma-prime alumina) around 375° (or 626°?), which
converts to theta-alumina ([“a better ordered transition form”][8])
around 800°, which finally converts to sapphire around 1120°, while if
instead it is first crystallized as gibbsite (as is usual in the Bayer
process) some of it instead goes by way of chi-alumina and
kappa-alumina.  Six other oxide and hydroxide forms are also
potentially part of the process, depending on impurities and heating
rates.  Contamination with carbon dioxide in this process may result
in incorporation of carbon.

The gibbsite itself is an important functional filler for plastics,
providing strength and especially fireproofing.

Lucalox is another potentially important use for sapphire.

Sapphire can also be crystallized hydrothermally with soda ash above
400° and 200 MPa, but such pressures are challenging.

Another interesting material potentially derived from aluminum
hydroxide is [mullite, the acicular aluminum silicate that accounts
for the legendary refractory performance of Hessian crucibles][9].
Crystallization of mullite from amorphous Al6Si2O13 at 980° [has been
reported][10]; the preparation was a difficult process involving
alkoxides of aluminum and silicon (and the phrase “was put in an open
flask and stirred for three months”), but since mullite is the
stablest alumina/silica compound, perhaps easier routes exist, such as
just firing at 1100°.

[9]: https://en.wikipedia.org/wiki/Hessian_crucible
[10]: https://link.springer.com/article/10.1007/BF01115736 "Formation of mullite and other alumina-based ceramics via hydrolytic polycondensation of alkoxides and resultant ultra- and microstructural effects, Bulent E. Yoldas & Deborah P. Partlow, 01988, J. Mat. Sci. vol. 23, pp. 1895-1900"

Carborundum was initially discovered by heating sand in an iron
crucible with an arc from a carbon electrode submerged in the sand,
carbothermally reducing some of the silica with some of the carbon
from the electrode.  Heating mixed carbon and sand with a submerged
arc sounds easy, and you don’t even need the iron crucible; you just
need two carbon electrodes.

HNO3 was traditionally obtained by XXX

Control and actuation
---------------------

Above I presupposed we could get precise positional control.  But how
could we *get* such positional control?  Norbert Heinz has
demonstrated a series of excellent homemade CNC machining tools made
from hardware-store parts, using the gantry arrangement used by most
existing CNC machines.  Some of them use H-bridge-controlled DC motors
(or steppers) and optical quadrature encoders he has cut out of tin
cans (or [from paper][2]) with [optical sensors from old printers][0].
The shaft rotation is translated to linear motion with leadscrews from
hardware-store allthread; but this feedback measures only the
rotational position of the leadscrew, so it is subject to errors from
deformation of the machine frame and the leadscrew and from backlash,
as well as thermal expansion.

To avoid these errors, you need feedback about the actual position of
the end effector rather than motors that indirectly drive it.  In
theory optical mice have a resolution of a micron or two, but [Heinz
found they lose steps][1].  He has achieved more precise control using
the transparent plastic optical encoder strip from an inkjet printer
to measure the linear position; these are usually 92, 150, or 300
lines per inch.  I can’t find Heinz’s page on the topic, but in 02010
[Michele Lizzit reported 33-micron precision using this method][3].

[0]: https://homofaciens.de/technics-base-circuits-transmissive-optical-sensors_en.htm
[1]: https://homofaciens.de/technics-base-circuits-computer-mouse_en.htm
[2]: https://homofaciens.de/technics-physical-computing-digital-ruler_en.htm
[3]: https://lizzit.it/printer/

Industrial machine tools are now almost universally equipped with a
“DRO”, digital readout, or are fully automatically controlled.  Three
common kinds of DROs exist: using optical “glass scales” similar to
the inkjet-printer encoder strip, using magnetic sensors that read a
strip of alternating magnetizations, and using capacitive sensors that
read a strip of alternating electrical connections.  Digital calipers
with 100-micron precision using this capacitive system are widely
available at retail for about US$8, and are commonly equipped with an
easily-tapped internal SPI data bus, while the other two systems
routinely deliver micron precision.

These approaches can suffer from thermal error when the scale (glass,
plastic, or otherwise) expands or contracts under the influence of
temperature variations.  The traditional solution to this was to keep
the temperature of your metrology lab constant to within a tenth of a
degree, but an alternative is to use laser interferometry, which can
easily deliver submicron precision and is much less affected by
temperature.

The kind of swing-arm arrangement used by manual magnetic 2-D profile
cutting machines, or by hard-disk platter-and-arm arrangements, is
mechanically vastly superior to the gantry arrangement; Melisa Orta
Martínez’s “Haplink” design demonstrates a promising mechanical design
for adapting such a swing-arm arrangement to motor-driven cable
drives.

For precise actuation over short distances, flexures and voice-coil
actuators are probably the best approach.  Hard disks have voice-coil
actuators in them.

Differential roller screws ought to enable far more precise linear
actuation than currently popular systems, but without digital
fabrication, they are very expensive to build.
