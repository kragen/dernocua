I’ve looked a bit into electrolytic machining (usually “ECM”) of
glass, but I think probably it’s not a good idea; sandblasting
(“abrasive jet machining”) is a dramatically more reasonable idea for
glass.  But I was thinking about marble, and I think electrolytic
machining would probably work really well for marble.

Electrolytic machining of marble and similar basic minerals
-----------------------------------------------------------

Suppose we use a neutral, very dilute NaCl electrolyte, saturating the
pore spaces of the marble, with a high enough overvoltage that most of
the electrolytic product is hydrogen and oxygen (1.23 V) rather than
sodium and chlorine.  At the anode, we produce (conventionally) H⁺
ions and oxygen by stripping an electron from water: 2H₂O → 4e⁻ + 4H⁺
+ O₂.  If the anode is close to the marble or in contact with it,
these H⁺ ions (really hydronium, H₃O⁺) will immediately react with the
CaCO₃ to reform water and carbon dioxide: CaCO₃ + 2H⁺ → H₂O + Ca⁺⁺ +
CO₂.  Thus the marble around the anode will be eroded, neutralizing
the acid and producing CaCl₂.  If the anode is either silver-plated or
made of carbon, I think it will not itself suffer erosion.

We can pump a fresh stream of electrolyte constantly through a hole in
the center of the anode; if the anode is sheathed in an insulator,
such as teflon, the hole in the insulator where the electrolyte
squirts out can ultimately determine where the workpiece erosion
happens, rather than depending on the geometry of the possibly-eroding
anode itself.

I don’t think much chlorine gas will be produced, if any, because the
electrons being sucked out of the anode are coming from the abundant
hydrogen ions, which replace them from the abundant marble, rather
than from the scarce chlorine ions.  If that does turn out to be a
problem, alternative electrolytes exist.

Aside from lime and its carbonates, the same anodic-attack approach
should work with other nonconductive minerals subject to easy acid
attack, such as dolomite (Mg/Ca), siderite (Fe), smithsonite (Zn),
magnesite (Mg), malachite (Cu), azurite (Cu), and perhaps portland
cement (calcium silicate hydrate).

A waste product of strong alkali will form at the cathode, though
perhaps this could be ameliorated with a suitable [buffer, perhaps
based on acetate, citrate, or borate][5], to compensate for the
buffering the carbonate provides to the acid produced at the anode;
lacking this, ultimately the liberated calcium ions will find their
way to the cathode and precipitate slaked lime.

[5]: https://en.wikipedia.org/wiki/Buffer_solution#Simple_buffering_agents

Choice of electrolyte
---------------------

It’s important for the anions in the electrolyte to maintain the
calcium ions in solution, unlike phosphate (apatite), pyrophosphate,
oxalate (weddellite/whewellite), fluoride (fluorite), hydroxide
(slaked lime), sulfate (gypsum), tartrate (beerstone, barely soluble)
or titanate (perovskite).  Chloride is a good choice, but other
choices include bromide, iodide, cyanide, thiocyanate, nitrate,
acetate (34.7 g/100mℓ), [chromate][0] (2.25 g/100mℓ), or [formate][1]
(16 g/100mℓ at 0°).

[0]: https://en.wikipedia.org/wiki/Calcium_chromate
[1]: https://en.wikipedia.org/wiki/Calcium_formate

[Calcium borate is a weird boundary case][2].  In dicalcium
hexaborate, the least soluble borate of calcium, water can dissolve
202mg/100mℓ of boria, which works out to `(* 202 (/ (+ (* 2 40.078) (*
2 15.999) (* 6 10.81) (* 9 15.999)) (+ (* 6 10.81) (* 9 15.999))))` =
310 mg/100mℓ of the salt, though [US Borax][3] gives 470 mg/100mℓ.)
Generally, borates are complicated and not very soluble, much like
silicates, phosphates, and silicoaluminates, because of the
possibility of oligomer or polymer formation.

[2]: https://onlinelibrary.wiley.com/doi/full/10.1002/ep.10058 "Removal of boron from wastewater by precipitation of a sparingly soluble salt, Remy & Muhr 02004"
[3]: https://agriculture.borax.com/USBorax/media/assets/infographics/borates-mineral-solubility.pdf

Choice of anode material
------------------------

It’s simultaneously desirable to use anions that won’t form soluble
salts with the anode material itself, both so you don’t end up with
nasty anode salts all over your nice cut marble, and so you don’t have
to keep feeding in more anode as it’s consumed (and suffering
imprecision from anode wear uncertainty).  A gold-plated anode would
permit the use of just about any electrolyte (except maybe cyanides,
which have other disadvantages), and even [silver should resist
chloride][6] and the other halogens (except fluoride).  Ordinary
copper would permit thiocyanate, and lead might permit the use of
iodide and bromide, though the resulting lead salts would be soluble
enough to pose real risks of contamination.  Because copper is lower
in the reactivity series than hydrogen, you’d think it could avoid
forming copper chloride in this use, but in fact copper plating using
chloride or acetate baths is totally a thing.  I have definitely
anodically destroyed copper in salty vinegar.

[6]: https://www.quora.com/Is-there-any-reaction-between-Silver-and-Hydrochloric-Acid-Ag+HCl

(Of course, graphite or carborundum electrodes will withstand
arbitrary acid or base attack at ordinary temperatures, and platinum
electrodes withstand nearly any reactive environment.)

Here’s a [solubility chart formulated for the purpose][4]:

<table>
<tr><th>(anion)  <th>Magnesium <th>Calcium <th>Gold <th>Copper <th>Lead <th>Silver <th>Tin <th>Iron <th>Nickel
<tr><th>fluoride <td><a href="https://en.wikipedia.org/wiki/Magnesium_fluoride">sS</a>
                               <td><a href="https://en.wikipedia.org/wiki/Calcium_fluoride">I</a>
                                           <td><a href="https://en.wikipedia.org/wiki/Gold%28III%29_fluoride">I</a>
                                                    <td><a href="https://en.wikipedia.org/wiki/Copper(II)_fluoride">sS</a>
                                                               <td><a href="https://en.wikipedia.org/wiki/Lead(II)_fluoride">sS</a>
                                                                        <td><a href="https://en.wikipedia.org/wiki/Silver%28I%29_fluoride">S†</a>
                                                                                   <td><a href="https://en.wikipedia.org/wiki/Tin(II)_fluoride">S</a>
                                                                                           <td><a href="https://en.wikipedia.org/wiki/Iron(II)_fluoride">S</a>
                                                                                                    <td><a href="https://en.wikipedia.org/wiki/Nickel(II)_fluoride">S</a>
<tr><th>chloride<td><a href="https://en.wikipedia.org/wiki/Magnesium_chloride">S</a>
                               <td><a href="https://en.wikipedia.org/wiki/Calcium_chloride">S</a>
                                           <td><a href="https://en.wikipedia.org/wiki/Gold(III)_chloride">S†</a>
                                                    <td><a href="https://en.wikipedia.org/wiki/Copper(II)_chloride">S</a>
                                                               <td><a href="https://en.wikipedia.org/wiki/Lead(II)_chloride">S</a>
                                                                        <td><a href="https://en.wikipedia.org/wiki/Silver_chloride">I</a>
                                                                                   <td><a href="https://en.wikipedia.org/wiki/Tin(II)_chloride">S</a>
                                                                                           <td><a href="https://en.wikipedia.org/wiki/Iron(III)_chloride">S</a>
                                                                                                    <td><a href="https://en.wikipedia.org/wiki/Nickel%28II%29_chloride">S</a>
<tr><th>bromide  <td><a href="https://en.wikipedia.org/wiki/Magnesium_bromide">S</a>
                               <td><a href="https://en.wikipedia.org/wiki/Calcium_bromide">S</a>
                                           <td><a href="https://en.wikipedia.org/wiki/Gold(III)_bromide">sS</a>
                                                    <td><a href="https://en.wikipedia.org/wiki/Copper(II)_bromide">S</a>
                                                               <td><a href="https://en.wikipedia.org/wiki/Lead%28II%29_bromide">sS</a>
                                                                        <td><a href="https://en.wikipedia.org/wiki/Silver_bromide">I</a>
                                                                                   <td><a href="https://en.wikipedia.org/wiki/Tin(II)_bromide">S</a>
                                                                                           <td><a href="https://en.wikipedia.org/wiki/Iron(III)_bromide">S</a>
                                                                                                    <td><a href="https://en.wikipedia.org/wiki/Nickel%28II%29_bromide">S</a>
<tr><th>iodide   <td><a href="https://en.wikipedia.org/wiki/Magnesium_iodide">S</a>
                               <td><a href="https://en.wikipedia.org/wiki/Calcium_iodide">S</a>
                                           <td><a href="https://en.wikipedia.org/wiki/Gold_triiodide">I</a>
                                                    <td><a href="https://en.wikipedia.org/wiki/Copper%28I%29_iodide">I</a>
                                                               <td><a href="https://en.wikipedia.org/wiki/Lead(II)_iodide">sS</a>
                                                                        <td><a href="https://en.wikipedia.org/wiki/Silver_iodide">I</a>
                                                                                   <td><a href="https://en.wikipedia.org/wiki/Tin(II)_iodide">S</a>
                                                                                           <td><a href="https://en.wikipedia.org/wiki/Iron%28II%29_iodide">S</a>
                                                                                                    <td><a href="https://en.wikipedia.org/wiki/Nickel%28II%29_iodide">S</a>
<tr><th>cyanide  <td><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6856803/">S</a>
                               <td><a href="https://en.wikipedia.org/wiki/Calcium_cyanide">S</a>
                                           <td>S</a>
                                                    <td><a href="https://en.wikipedia.org/wiki/Copper%28I%29_cyanide">I</a>
                                                               <td><a href="https://chemistry.stackexchange.com/questions/108993/solubility-of-lead-cyanide">sS?</a>
                                                                        <td><a href="https://en.wikipedia.org/wiki/Silver_cyanide">I</a>
                                                                                   <td>??? <td>???  <td><a href="https://en.wikipedia.org/wiki/Nickel_dicyanide">I</a>
<tr><th>thiocyanate<td><a href="https://www.chemicalbook.com/ChemicalProductProperty_EN_CB3258303.htm">S?</a>
                               <td><a href="https://www.chemicalbook.com/ProductChemicalPropertiesCB1467934_EN.htm">S?</a>
                                           <td>???  <td><a href="https://en.wikipedia.org/wiki/Copper%28II%29_thiocyanate">I</a>
                                                               <td><a href="https://en.wikipedia.org/wiki/Lead%28II%29_thiocyanate">sS</a>
                                                                        <td><a href="https://en.wikipedia.org/wiki/Silver_thiocyanate">sS</a>
                                                                                   <td>sS? <td>S?   <td><a href="https://en.wikipedia.org/wiki/Nickel%28II%29_thiocyanate">S?</a>
<tr><th>acetate  <td><a href="https://en.wikipedia.org/wiki/Magnesium_acetate">S</a>
                               <td><a href="https://en.wikipedia.org/wiki/Calcium_acetate">S</a>
                                           <td><a href="https://www.americanelements.com/gold-acetate-15804-32-7">sS†</a>
                                                    <td><a href="https://en.wikipedia.org/wiki/Copper%28II%29_acetate">S</a>
                                                               <td><a href="https://en.wikipedia.org/wiki/Lead%28II%29_acetate">S</a>
                                                                        <td><a href="https://en.wikipedia.org/wiki/Silver_acetate">I</a>
                                                                                   <td><a href="https://www.americanelements.com/tin-ii-acetate-638-39-1">sS?</a>
                                                                                           <td><a href="https://en.wikipedia.org/wiki/Iron%28II%29_acetate">S</a>
                                                                                                    <td><a href="https://en.wikipedia.org/wiki/Nickel%28II%29_acetate">S</a>
                                                 
<tr><th>chromate <td><a href="https://en.wikipedia.org/wiki/Magnesium_chromate">S</a>
                               <td><a href="https://en.wikipedia.org/wiki/Calcium_chromate">S</a>
                                           <td><a href="https://chempedia.info/info/auric_chromate/">S?†</a>
                                                    <td><a href="https://www.chemicalbook.com/ChemicalProductProperty_EN_CB3890444.htm">I?</a>
                                                               <td><a href="https://en.wikipedia.org/wiki/Lead_chromate">I!</a>
                                                                        <td><a href="https://en.wikipedia.org/wiki/Silver_chromate">I</a>
                                                                                   <td><a href="http://cameo.mfa.org/wiki/Stannic_chromate">sS?</a>
                                                                                           <td><a href="https://en.wikipedia.org/wiki/Iron%28III%29_chromate">R</a>
                                                                                                    <td><a href="https://en.wikipedia.org/wiki/Nickel%28II%29_chromate">sS</a>
<tr><th>formate  <td><a href="https://en.wikipedia.org/wiki/Magnesium_formate">S</a>
                               <td><a href="https://en.wikipedia.org/wiki/Calcium_formate">S</a>
                                           <td><a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.201705557">?†</a>
                                                    <td><a href="https://pubchem.ncbi.nlm.nih.gov/compound/Cupric-formate">S</a>
                                                               <td><a href="https://www.scbt.com/p/lead-ii-formate-811-54-1">S (16 mg/mℓ)</a>
                                                                        <td>??? unstable
                                                                                   <td><a href="https://pubs.rsc.org/-/content/articlelanding/1964/jr/jr9640004801/unauth#!divAbstract">S?</a>
                                                                                           <td><a href="https://srdata.nist.gov/solubility/sol_detail.aspx?sysID=73_28">S</a>
                                                                                                    <td><a href="https://srdata.nist.gov/solubility/sol_detail.aspx?sysID=73_30">S</a>
<tr><th>borate   <td><a href="https://www.chemicalbook.com/ChemicalProductProperty_EN_CB4135142.htm">sS?
                               <td>sS      <td>???  <td><a href="https://www.sciencedirect.com/science/article/abs/pii/S002554081500327X">I†</a>
                                                               <td><a href="https://www.americanelements.com/lead-borate-35498-15-8">S?</a>
                                                                        <td>???    <td><a href="https://pubs.rsc.org/en/content/articlelanding/2019/dt/c9dt01901d#!divAbstract">†</a>
                                                                                           <td><a href="https://www.sciencedirect.com/science/article/abs/pii/S0304885316308605">†</a>
                                                                                                    <td><a href="https://pubs.rsc.org/en/content/articlelanding/2018/ta/c8ta07385f#!divAbstract">†</a>

<tr><th>sulfate  <td><a href="https://en.wikipedia.org/wiki/Magnesium_sulfate">S</a>
                               <td><a href="https://en.wikipedia.org/wiki/Calcium_sulfate">sS</a>
                                           <td><a href="https://onlinelibrary.wiley.com/doi/abs/10.1002/1521-3749%28200109%29627%3A9%3C2112%3A%3AAID-ZAAC2112%3E3.0.CO%3B2-2">R†</a>
                                                    <td><a href="https://en.wikipedia.org/wiki/Blue_vitriol">S</a>
                                                               <td><a href="https://en.wikipedia.org/wiki/Lead_sulfate">sS</a>
                                                                        <td><a href="https://en.wikipedia.org/wiki/Silver_sulfate">sS</a>
                                                                                   <td><a href="https://en.wikipedia.org/wiki/Tin_sulfate">S</a>
                                                                                           <td><a href="https://en.wikipedia.org/wiki/Iron%28II%29_sulfate">S</a>
                                                                                                    <td><a href="https://en.wikipedia.org/wiki/Nickel_sulfate">S</a>
<tr><th>citrate  <td><a href="https://en.wikipedia.org/wiki/Magnesium_citrate_%283:2%29">sS</a>
                              <td><a href="https://en.wikipedia.org/wiki/Calcium_citrate">sS</a>
                                           <td>???  <td><a href="http://www.sciencemadness.org/smwiki/index.php/Copper_citrate">sS</a>
                                                               <td><a href="https://en.wikipedia.org/wiki/Lead_citrate">S</a>
                                                                        <td><a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2590638/">I (285 ppm)</a>
                                                                                   <td>??? <td><a href="https://en.wikipedia.org/wiki/Iron%28III%29_citrate">S</a>
                                                                                                    <td><a href="https://en.wikipedia.org/wiki/Nickel_organic_acid_salts">S</a>
</table>

† indicates compounds that I don’t think will form electrolytically
from unoxidized metal and relevant anions.

[4]: https://en.wikipedia.org/wiki/Solubility_chart

(Ugh, I don’t have zinc in the chart.  But it’s almost the same as
magnesium.  Also, I don’t have tartaric, lactic, and phosphoric
acids.)

I tried reducing the above solubility chart to an easier-to-use form a
few times, but I never succeeded.

Alternative solvents
--------------------

Another approach is to make the electrolyte from ions dissolved in a
polar solvent other than water; for example, anhydrous ammonia,
formamide, tetrahydrofuran, acetone, isopropanol, methyl ethyl ketone,
pyridine, DMSO, dichloromethane, or deep eutectic systems; these will
yield different solubilities for various ionic substances.

For example, [only 0.2 grams of muriate of potassa dissolves in 100 mℓ
of DMSO, and 0.013 g of potash, but it can dissolve 20 g of the iodide
or 30 g of muriate of Mars, while the muriate of lime is entirely
insoluble][10].  In DMSO, hydrated cupric acetate and muriate are
insoluble, but the acetate and muriate of zinc are quite soluble, as
are the muriates of tin, so a copper anode with a zinc-muriate
electrode dissolved in DMSO might be able to electrolytically etch
salts of tin or iron with impunity.

Some solvents may not produce electrolysis products of their own that
are useful for the electrolytic etching process, the way water does;
for example, the anodic reaction converting carbonate ions to oxygen
and carbon breaks apart and then reforms water molecules in the
process.  DMSO in particular seems likely to produce electrolysis
products much more noxious for human life.

[10]: https://www.gaylordchemical.com/content/uploads/2020/08/GC-Literature-102B-ENG-Low.pdf

Etching with a cathode instead of an anode
------------------------------------------

If the electrolytic cell’s cathode rather than its anode were the
active tool, it should work for acidic or amphoteric materials
attacked by strong bases, most notably sapphire ([slowly, at tens of
megapascals and 400° or higher][8]), gibbsite, and amphoteric oxides
like those of zinc (philosopher’s wool, a refractory (1974°)
thermochromic transparent piezoelectric direct-bandgap n-type
semiconductor with a 3.37-eV bandgap), titanium (rutile, a UV-blocking
strongly birefringent photo-superhydrophilic photocatalytic
transparent refractory (1843°) n-type semiconductor with refractive
index 2.61 and a 3.05 eV bandgap which becomes an excellent dielectric
when stoichiometric), tungsten (an electrochromic photocatalytic
semiconductor), vanadium (a refractory (1967°) transparent
semiconductor with an 0.7-eV bandgap that becomes metallic and
IR-reflective in 100 fs above 68°, a temperature that can be adjusted
with tungsten doping), and tin (cassiterite, a refractory (1630°)
n-type semiconductor with a refractive index of 2.0 and a specific
gravity of 7).

The amphoteric oxides can be etched just as well by the anode-acid
process described at the start, but etching them with a cathode means
you can use any metal for the tool electrode, since it won’t be
vulnerable to anodic dissolution.

Metal sulfides might be another candidate.  Leaching with very dilute
alkali has been successfully used to separate [antimony from stibnite
(antimony sulfide) without affecting other metals][7], with etching
speeds around 10 microns per minute.  Alkaline leaching has also been
used to extract lead, tungsten, zinc, vanadium, and chromium from
various ores.  Mostly, though, these processes are very slow.

[7]: https://www.researchgate.net/profile/Emilia-Smincakova/publication/225747528_Leaching_of_Natural_Stibnite_using_Sodium_Hydroxide_Solution/links/5745887208aea45ee854bab6/Leaching-of-Natural-Stibnite-using-Sodium-Hydroxide-Solution.pdf?origin=publication_detail
[8]: https://pubs.acs.org/doi/abs/10.1021/j100798a028

These cathodic etching processes, instead of producing waste alkali at
the cathode, would produce waste acid at the anode, and the same
comments about buffering apply to avoiding undesired acid
accumulations.

More speculative directions to explore
--------------------------------------

A very interesting question for this kind of electrolytic work: these
semiconductors, zinc oxide, rutile, tungsten oxide, vanadia, and
cassiterite, are all immune to anodic dissolution; but they are
amphoteric enough to be unstable for this kind of work.  But perhaps
other nonmetallic semiconductors other than carbon and carborundum,
such as GaN or InP, may be alternative electrode materials.

Pulses of high voltage on small-diameter electrodes should be able to
produce plasma discharges to overcome activation barriers, a sort of
corona-discharge EDM/ECM hybrid, though this would surely also erode
the tool electrodes.
