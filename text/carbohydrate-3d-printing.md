I was thinking about simple sugar syrup, which has a glass transition
around room temperature or even below depending on the water content
(the eutectic point is 60% sucrose and -9.5°, but at that
concentration the [glass transition is about -90°][1], rising above 0°
[around 85% sugar and increasing to 52° at 100% sugar][2]), and which
can either be easily crystallizable or stable against crystallization
depending on its specific composition.  (Using isomalt, which normally
only crystallizes in a hydrated form, rather than or in addition to
sucrose is one approach popular for keeping sugar art from
crystallizing; hydrolyzing some of the sucrose with lemon juice is
another, and mixing in some high-fructose corn syrup is a third.)

[1]: https://www.doitpoms.ac.uk/tlplib/biocrystal/water-sucrose.php
[2]: http://imartinez.etsiae.upm.es/~isidoro/bk3/c07sol/Solution%20properties.pdf

The first 3-D printer I ever saw was the CandyFab 4000, which melted
sugar with hot air, which [happens at 160° to 186° in a very complex
way][0], at which temperature the sugar caramelizes fairly rapidly,
enough to produce a noticeable discoloration in the few seconds the
CandyFab 4000 kept the sugar molten.

[0]: https://pubs.acs.org/doi/10.1021/jf3002526

But in sugar art, sugar glass is maintained in its rubbery, plastic
state at room temperature with the addition of water.

Glasses drop dramatically in viscosity above their glass transition
temperatures.  So, for example, syrup of 60 wt% sugar has [113
centipoise at 10°][3], but 56.7 cP at 20°, 34.0 cP at 30°, 21.3 cP at
40°, 14.1° at 50°, and 4.17 cP at 90°.  Moho says that, [at 76%][4],
the viscosity at 30° is 1200 cP, dropping to 510 cP at 40°, 250 cP at
50°, 130 cP at 60°, and 47 at 80°.  He gives no viscosity at 20°, so
presumably it's effectively no longer a syrup for confectionery
purposes.

However, [PLA extrusion normally happens at 3-20 kilopoise, i.e.,
300-2000 Pa s][5].  This is in the range Moho gives for toffee fondant
mass (Table A1.34, p. 572): 17%-water Kis-Kis toffee mass is 2.48 Pa s
(2480 centipoise) at 60° and 0.26 Pa s at 100°, while 8%-water Kis-Kis
toffee is 487.8 Pa s at 70° and 43.0 Pa s at 90°.  [Wikipedia claims
toffee is more like 1% water][6], the "hard crack" stage (boiling at
146°-154°), so perhaps "toffee mass" is a different substance.

[3]: https://www.engineeringtoolbox.com/sugar-solutions-dynamic-viscosity-d_1895.html
[4]: https://onlinelibrary.wiley.com/doi/pdf/10.1002/9781444320527.app1 "Confectionery and Chocolate Engineering: Principles and Applications, Ferenc Á. Moho, 02010"
[5]: https://core.ac.uk/download/pdf/163105304.pdf "Influence of printing parameters on the stability of deposited beads in fused filament fabrication of poly(lactic) acid, p. 13, section 'shear rate and viscosity of the polymer in the liquefier'"
[6]: https://en.wikipedia.org/wiki/Candy_making#Sugar_stages

Regardless of exactly how much water is needed to plasticize sugar to
an extrudable stage, it's clear that such a level does exist, and the
resulting substance hardens rapidly as it cools.

[Pok Yin Victor Leung investigated hard-crack candy printing in
02017][7] as a more accessible model for printing optics in soda-lime
glass, using sucrose and high-fructose corn syrup gravity-fed from a
reservoir maintained at 98° with a PID controller with only a manual
valve.  He got beautiful results but reports that the shining golden
objects thus printed were deliquescent.

[7]: https://dspace.mit.edu/bitstream/handle/1721.1/115176/Leung-Sugar%203D%20Printing_%20Additive%20Manufac.pdf?sequence=1&isAllowed=y

A standard candy sealing process is "hard sugar panning", in which
hard sticky candy balls are rolled around in syrup which crystallizes
on the surface as it dries, sometimes in many layers added over weeks;
this is how "jawbreakers" and M&Ms are made.  If the syrup used is a
non-crystallizing syrup like glucose syrup, the process becomes "soft
panning", and powdered sugar can harden it, producing jellybeans.
Such crystallization would be undesirable for Leung's purpose of 3-D
printing optics, but it would solve the deliquescence problem.

There are a variety of other possible ways to harden such a surface
besides dusting it with sugar, though.  Shellac, for example, is
commonly used in candymaking, with zein as an up-and-coming
alternative that also leaves the result edible.  You could also
include sodium alginate in the syrup and harden the surface with
calcium ions, or vice versa, or include something that hardens instead
of deliquescing when it reacts with water from the air.  Or perhaps
you could wash the surface with a desiccant such as ethanol or a
strong solution of muriate of lime.

Of course, if edibility is not a requirement, there are lots of
coatings you can use.  Possibilities for hardening systems to use as
coatings include molten wax, cyanoacrylate, plaster of paris, spray
paint, resins that polymerize on the object (such as silicone, epoxy,
or acrylic), polymers dissolved in a solvent (such as acrylics, ABS,
or polystyrene, dissolved for example in acetone or gasoline), lime
concrete, OPC concrete, geopolymer concrete, or soluble silicates such
as that of sodium (perhaps desolubilized by polyvalent cations added
to the syrup).  In addition to using these hardening systems simply as
coatings, you can also just pour them over the printed sugar object,
embedding it in a block; once this block has solidified, you can
dissolve the sugar out of it with enough flowing water, ideally warm.

Some of these coating systems include free water, which poses a
potential problem: at the interfacial layer between the hardening
system and the sugar object, water will be migrating out of the
hardening system and into the sugar, swelling and liquefying the
sugar, while diminishing the water available to the hardening system,
potentially impeding its hardening.  This may be actually desirable,
acting as a sort of inbuilt mold release and avoiding the need to melt
or dissolve the sugar out of the hardening system's product; even if
not, the affected layer may be thin enough to be acceptable.

In other cases, it may be possible for the hardening system to
actually *extract* the water it needs from the sugar object; for
example, methyl cyanoacrylate or the usual silyl acetates that
comprise acetoxy-cure silicones (largely methyl triacetoxysilane, I
think) will happily steal water in such a situation, and I think
plaster of Paris can too.  So it may be possible for them to be
applied as a bath or powder coat and selectively harden on the surface
of the printed object.

A totally different approach is to postprocess the print to get rid of
the sugar, which is especially appealing if the sugar syrup is mostly
used as a plasticizing and sticky carrier for a solid particulate
"filler" that is the real printing payload, much like epoxy is used in
JB Weld or PLA is used in brass-filled PLA filament.  (Such fillers,
in addition to adding numerous useful properties to the resulting
object, may help to make the melt thixotropic, easing the compromise
between flowing easily through the hotend nozzle and staying in place
once extruded.)  The easiest way to remove the sugar is to heat the
piece to caramelize it, eventually producing carbon.  If it's thin
enough and it's heated slowly enough, this can be done without
provoking water-vapor bubbles.

(Are we blowing hot and cold with one breath here?  Why won't the
syrup clog up the extruder if heating it caramelizes it?  It might not
work, but my thought is that in the extruder it's potentially only hot
for a few seconds, during which time it is under a lot of shear
stress, while we can keep it at a lower temperature overnight or
longer with very little stress in order to caramelize it.)

I haven't had much luck getting caramelized sugar to stick quartz sand
together, but it's well known how difficult it is to get it off steel
or stainless steel, often requiring lye.

In addition to solid fillers, another possible additive to improve
thixotropy of water-plasticized sugars is emulsified oil, as in
mayonnaise, though of course in mayonnaise it's soluble protein that's
being plasticized by the water, not sugars.  Oil droplets dispersed in
an emulsion can give rise to quasi-elastic behavior.

I thought the same was true of [dulce de leche][8], but that turns out
to be wrong.  Dulce de leche is an emulsion, but it is also a much
more complex system containing proteins and polysaccharides which form
a gel structure; it's normally 6-8% fat and 31-34% water.  This is not
enough fat to give the emulsion quasi-elastic behavior; instead it is
pseudoplastic like molten polymers made of long linear molecules that
form ephemeral entanglements, and also forms a gel.

[8]: https://ri.conicet.gov.ar/handle/11336/103304 "Physicochemical and Rheological Characterization of 'Dulce de Leche', Ranalli, Andres, Califano 02011, CC-BY-NC-SA"

A different family of carbohydrate 3-D printing is suggested by pasta
and flubber, which are made out of starch granules and water; the
starch granules can be suspended in water by purely mechanical means.
Heating the water enables it to dissolve the starch granules, in a
process called starch gelatinization, and the resulting viscous
solution of amylose and amylopectin (boh polysaccharides) behaves much
like a sugar syrup.

There are various ways to crosslink these starch molecules to reduce
their solubility, including using glow discharge plasma, phosphorus
oxychloride (POCl3), citric acid (with a sodium hypophosphite
catalyst), sodium trimetaphosphate, boric acid, formaldehyde, and
sucrose oxidized by periodate cleavage with sodium periodate to form
random aldehydes; and polyols like glycerol or sorbitol can be used to
plasticize the resulting insoluble plastic.  Glyoxal, the simplest
dialdehyde (and essentially nontoxic, 3300 mg/kg) is consumed in mass
quantities to thus crosslink starches for sizing paper and textiles.
Glutaraldehyde (plantar wart remover, also used in tanning leather,
and as a biocide in fracking) seems like it should work.
