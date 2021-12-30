Iron is a pretty economically attractive material: extremely abundant
([5.6% of Earth’s crust][18], [32% of Earth][19]), moderately
refractory (doesn’t melt until 1600°), can form carbides called
“cementite” that make it into a very hard and strong “alloy” called
steel (arguably really a cermet), and can be heat-treated to increase
its hardness further.  But could we make “steels” based on other
similar metals, if we had enough of them?  I think we could.

[18]: https://en.wikipedia.org/wiki/Abundance_of_elements_in_Earth's_crust
[19]: https://en.wikipedia.org/wiki/Abundance_of_the_chemical_elements#Earth

Ridiculously oversimplified steel
---------------------------------

Steel is a very complex system, and I am doing it a bit of an
injustice by simplifying its behavior to just “derives its strength
from cementite”.

Regular iron cementite (Fe₃C) [has a “hardness” of 7–11 GPa][0], which
I take to mean that its ultimate tensile strength is 7–11 GPa.  [Jiang
and Srivilliputhur][3] calculate ideal tensile strengths for cementite
between 15 and 30 GPa in different directions, though I haven’t really
read their paper.  When steel changes phase from austenite to ferrite,
the solubility of carbon in the iron phase drops greatly,
precipitating submicron-thickness layers of cementite alternating with
ferrite in a structure called “pearlite”.  (I don’t think they’re thin
enough to be [below the flaw-tolerant critical size, which is
estimated at 30 nm for goethite fibers][1] such as those found in
limpet teeth, but [which exists for any material][2]; nacre actually
uses 200–500-nm-thick crystals, similar to the thickness of cementite
layers in some pearlite.  The cementite layers in bainite might be
thin enough to be flaw-tolerant.)  As a consequence, [pearlite wires
can reach tensile strengths over 6 GPa][4].  But cementite is unstable
above 723°, so steels become soft and malleable when they transition
to the austenitic phase.

[0]: https://www.tf.uni-kiel.de/matwis/amat/iss/kap_7/articles/umemoto_cementite.pdf "Mecanical [sic] Properties of Cementite and Fabrication of Artificial Pearlite, by M. Umemoto, Y. Todaka and K. Tsuchiya, Materials Science Forum Vol.426-432 (02003) pp.859-864"
[1]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4387522/
[2]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC156246/ "Materials become insensitive to flaws at nanoscale: Lessons from nature, by Huajian Gao, Baohua Ji, Ingomar L. Jäger, Eduard Arzt, and Peter Fratzl, PMCID: PMC156246, PMID: 12732735, Proc Natl Acad Sci U S A. 02003 May 13; 100(10): 5597–5600, 10.1073/pnas.0631609100"
[3]: https://www.researchgate.net/figure/Fe3C-under-tensile-and-shear-deformations-a-Stress-strain-curves-under-100-010-and_fig2_236192150
[4]: https://en.wikipedia.org/wiki/Pearlite "Segregation stabilizes nanocrystalline bulk steel with near theoretical strength, by Li, Y.; Raabe, D.; Herbig, M. J.; Choi, P.P.; Goto, S.; Kostka, A.; Yarita, H.; Bochers, C.; Kirchheim, R., 02014, Physical Review Letters, 113 (10): 106104, Bibcode:2014PhRvL.113j6104L, doi:10.1103/PhysRevLett.113.106104, PMID 25238372."

Tungsten and the chromium group
-------------------------------

Mushet steel, the nascent form of high-speed steel, includes 1.5–2.5%
carbon, 4–12% tungsten, which also forms a hard carbide with carbon,
and 2–4% manganese.  As I understand it, the manganese makes it
austenitic at room temperature, allowing it to be air-hardened without
quenching and to have much greater toughness than earlier hardened
steels.  I think that most of the carbon in Mushet steel and similar
high-speed steels ends up in tungsten carbide rather than carbides of
iron or manganese, and that nearly all the tungsten does.

Tungsten carbide’s tensile strength is normally cited as being only
around 0.4 GPa, but because it’s a brittle ceramic, I suspect that
number is dominated by flaw-sensitivity.  It doesn’t decompose until
2800°, and I think this is why Mushet steel and the modern high-speed
steels that are based on tungsten remain hard at high temperatures.

I think you could probably make a “steel” consisting of tungsten and a
little carbon.  The solubility of small amounts of carbon in tungsten
rises up to 2715°, so you could probably get some kind of interspersed
pearlite-like microstructure by quenching tungsten down to a lower
temperature.  It wouldn’t have to be anywhere near room temperature;
quenching it to 1091° in molten magnesium or 907° in molten zinc would
be just fine.  (There’s a second tungsten carbide, but it only becomes
important at higher concentrations.)  But at room temperature tungsten
is kind of brittle, and of course tungsten itself is a very rare
element (0.17 ppm of Earth by weight, 1.25 ppm of the crust), which
sometimes matters.

Tungsten is a group-6 transition element, along with chromium,
molybdenum, and the wildly radioactive and presently irrelevant
seaborgium.

Chromium (4700 ppm of Earth, 100 ppm of Earth’s crust) is a bit more
refractory than iron (melting at 1907°), is the base of some stainless
steels, and is commonly plated on top of steel to make it harder,
shinier, and more corrosion-resistant.  In many ways it’s reasonable
to think of it as a sort of half-assed tungsten.  So what about its
carbides?

Well, [chromium has three carbides][31], which are indeed refractory
(1895°, so less refractory than metallic chromium), very hard, and
corrosion-resistant, and they’re commonly used to improve the wear and
corrosion resistance of metals.  So far so good.  I should look up the
chromium–carbon phase diagram.

Molybdenum is damn near as refractory as tungsten itself, melting at
2623°, but also damn near as rare: 1.7 ppm of Earth, 1.2 ppm of its
crust.  Its oxide is a lot more volatile than tungsten’s, limiting its
refractory usefulness in applications exposed to air, but it also has
a very hard refractory (2687°) carbide.  I should look up the relevant
phase diagram.

[31]: https://en.wikipedia.org/wiki/Chromium%28II%29_carbide

Covalent binder alternatives to carbon
--------------------------------------

So far, we’ve looked at carbides of iron, tungsten, chromium, and
molybdenum, all of which are very hard and refractory due in part to
the somewhat covalent character of their bonding.  But there are other
elements that can play a similar role: boron, oxygen, nitrogen, and
sulfur, as well as oxoanions like phosphate.  Some of these are
counterproductive in iron itself: the oxides, nitrides, and sulfide of
iron are all weaker and less refractory than iron itself.  But iron
boride is somewhat of a hit (Vickers hardness of 15–22 GPa, melts at
1389°, [already in use as a steel ingredient for hardness][32] and
[used for surface hardening][33]), and [iron tetraboride is
superhard][130], and, in combination with other metals, some of these
elements produce very interesting ceramics.

[32]: https://en.wikipedia.org/wiki/Boron_steel
[33]: https://en.wikipedia.org/wiki/Boriding
[130]: https://en.wikipedia.org/wiki/Iron_tetraboride

Sticking to just the metals so far mentioned, [tungsten borides have
Vickers hardnesses of 20–30 GPa][34] and WB₄ is described as [“an
inexpensive superhard material” because you can make it with just arc
melting from the elements][35]; [chromium borides are also very hard
and strong][36] and [can be made by SHS][37], [especially if you add
aluminum][38]; and [molybdenum borides are predicted to be
superhard][39] but apparently nobody has managed to produce them in
volume yet.

[34]: https://en.wikipedia.org/wiki/Tungsten_borides
[35]: https://www.pnas.org/content/108/27/10958
[36]: https://en.wikipedia.org/wiki/Chromium%28III%29_boride
[37]: https://www.sciencedirect.com/science/article/pii/B9780128041734000302
[38]: https://www.sciencedirect.com/science/article/pii/S0272884212003197
[39]: https://arxiv.org/abs/1907.05665

As for the oxides, I’ve mentioned the iron oxide goethite above (not
usually thought of as superhard, but the limpets manage); [tungsten
trioxide has 5–7 GPa hardness at 800°][40]; chromium oxides include
chromia (viridian) which melts at 2435° and has Mohs hardness 8 as the
mineral eskolaite; and, though it melts at only 802°, [molybdenum
trioxide has a hardness of 18.7 GPa][41], though [as a mineral it’s
only Mohs 3–4][42].

[40]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3278358/
[41]: https://www.sciencedirect.com/science/article/abs/pii/S0167577X20311253
[42]: https://en.wikipedia.org/wiki/Molybdite

Nitriding, carbonitriding, and nitrocarburizing are commonly used as a
surface hardening process for steel, chromium, and molybdenum, and
nitriding has been used to harden iron since antiquity, with urine,
leather, and hooves being preferred case-hardening ingredients.
Tungsten nitride is also hard, but it decomposes in water, limiting
its use in air-contact applications.

Many elements also have interesting oxynitrides, oxyborides,
borocarbides, boronitrides, borocarbonitrides, carbonitrides, and
oxycarbonitrides.  Oxycarboborides and oxyboronitrides seem to be
either neglected or too difficult to make, and although some
“oxycarbides” are reported (including a molybdenum oxycarbide), many
more are just carbonyls or oxalates, which are neither hard nor
refractory.

Other metals
------------

What about nickel, cobalt, vanadium, manganese, titanium, zirconium,
hafnium, silicon, niobium, and tantalum?  They also form carbides!
That makes 110 more candidate ceramics to investigate!