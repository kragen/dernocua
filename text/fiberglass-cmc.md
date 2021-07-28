Fiberglass for insulation is super cheap (file `refractories.md`
reports that it’s around US$3/kg) and has substantial tensile
strength, even if it’s not as high as S-glass and M-glass.  Chopped
glass fiber for mixing into plastics as reinforcement (probably
E-glass) [also sells for about US$3/kg][a75] (AR$9975 for 20kg). (I
think fiberglass insulation is A-glass.)  Glass fibers are commonly
used to reinforce organic polymers like epoxy to make them roughly as
strong as steel, but this matrix is itself fairly expensive in bulk;
[6 kg of epoxy from Tienda Bepox costs AR$21000][a72], US$129, or
US$21/kg, seven times the price per unit mass of the fiber
reinforcement.  Polyester resin is significantly cheaper, at
[AR$7300/10kg][a73], US$4.50/kg, but also much more rigid and, I
think, more fragile.  (Vinyl ester and phenolic casting resins are
apparently harder to find, locally at least.)

[a75]: https://articulo.mercadolibre.com.ar/MLA-834281445-hilo-de-fibra-de-vidrio-cortada-20kg-placas-antihumedad-_JM
[a73]: https://articulo.mercadolibre.com.ar/MLA-666422735-10kg-resina-poliester-cristal-_JM
[a72]: https://articulo.mercadolibre.com.ar/MLA-914848579-resina-epoxi-revestimiento-6-kg-cristal-vidrio-liquido-_JM

For polyester thermosets, Matweb [gives useless ranges of 10–123 MPa
for ultimate tensile strength and 54–265 MPa for flexural yield
strength][a76] (implying that at least one polyester thermoset has a
flexural yield strength twice its ultimate tensile strength), and for
“epoxy cure resin” [5–97 MPa and 76–1900 MPa][a77], and for “epoxy,
cast, unreinforced” [8–97 MPa and 14–131 MPa][a78].  And I have no
idea where in these very wide ranges these resins are.

[a78]: http://www.matweb.com/search/DataSheet.aspx?MatGUID=1c74545c91874b13a3e44f400cedfe39
[a77]: http://www.matweb.com/search/DataSheet.aspx?MatGUID=956da5edc80f4c62a72c15ca2b923494
[a76]: http://www.matweb.com/search/datasheet.aspx?matguid=1d92ed366503454ba49b8a44099f90de&n=1&ckck=1

Matweb says fused quartz (Saint-Gobain Quartzel) is [6000 MPa
UTS][a79] and generic A-glass fiber is [3310 MPa UTS][a80], while
Micarta RT500M glass-reinforced epoxy is [only 269 MPa UTS][a81] and
“Goodfellow E-glass/Epoxy composite” is [only 490 MPa UTS][a82].  So
there’s a lot of room for improvement.

[a82]: http://www.matweb.com/search/DataSheet.aspx?MatGUID=89f8b78cfd564d07845a232d22b99519
[a81]: http://www.matweb.com/search/DataSheet.aspx?MatGUID=887a9a6a63bb476d9bf271ba2da40e4e
[a80]: http://www.matweb.com/search/datasheet.aspx?MatGUID=8f9003366c9044bdb91bcd86e1fa6e42
[a79]: http://www.matweb.com/search/DataSheet.aspx?MatGUID=c1880a08cfb948b0b5f2f9d47cc9b130

Could you make a ceramic-matrix composite from insulation fiberglass,
getting the usual cracking-resistance performance improvements of
CMCs, even if the improved performance doesn’t approach the kind of
performance you get out of things like SiC/SiC CMCs?  Could you do it
*cheaply*?

You clearly can’t heat it up to the high temperatures normally
associated with CMC manufacturing; those are over 1000° and glass wool
craps out around 230–260° (reportedly, I haven’t tried, and I suspect
this may just be the max temp of the polymeric sizing — soda-lime
glass normally doesn’t soften until around 700°), while rock wool
(which is also about US$3/kg) should maybe be good to 700°–850°.  So
you might need some kind of hydrothermal process.  Moreover, the
hydrothermal process needs to be gentle enough to not eat the glass
reinforcing fibers, so in particular ordinary portland cement and
carbonation of slaked lime are probably off the table, and so is
anything that involves making silica highly soluble in water.

A few candidate matrix systems:

- Calcined alabaster, of course, though this will never reach very
  high strengths.
- Geopolymer cements with low alkalinity, such as milled metakaolin
  polymerized with modulus-4 sodium silicate (though [Davidovits
  recommends 1.45–1.85][a84]).
- Low-alkalinity waterglass binders.
- Aqueous phosphate cements such as the phosphates of zinc, magnesium,
  or aluminum.
- Sorel cement (pH 8.5 to 9.5 according to Wikipedia).

[a84]: https://www.researchgate.net/profile/Joseph-Davidovits/publication/306946529_Geopolymer_Cement_a_review_2013/links/5bf2cb7c299bf1124fde4512/Geopolymer-Cement-a-review-2013.pdf?origin=publication_detail

To any of these binders you could add functional fillers such as
clays, talc, mica, quartz sand, quartz flour, carborundum, perlite,
vermiculite, glass foam, or sapphire.

Aside from the spatula layup approaches normally used to produce
fiber-reinforced plastics, chopped-fiber mixing is a possibility, and
spin-coating of the binder/filler/fiber mixture would tend to produce
a biaxial orientation of the solids, which would tend to be very
advantageous to both solids density and to applying the strength of
the solids in the appropriate directions.  This approach would be best
at increasing the density of the solids if the binder decreases
greatly in volume after the spinning, for example by dehydrating.

Another way to increase the toughness and flexibility of such a stiff
composite material is to fabricate it in thin sheets and then laminate
them together with a softer or weaker binder.  The binder would tend
to stop crack propagation or at least redirect it parallel to the
surface of the material, and if it is soft rather than just weak it
would tend to shear to allow the overall composite sheet to flex, like
the pages of a book.  Sodium chloride and highly-hydrated sodium
silicate are two candidate binders that might be capable of such
shear, especially over time.

Sizing
------

Normally when you’re making glass-fiber-reinforced things you’re
concerned with sizing the fibers to improve adhesion to the matrix,
because otherwise the low-modulus, low-strength matrix can’t
effectively transfer load to the fibers, and you get pullout failures
at much lower loads than would be needed to actually break the fibers.

In CMCs the objective is the opposite: the matrix has strength
comparable to the fibers, but both the fiber and matrix have the very
low elongation at break characteristic of ceramics.  Instead, the
fibers are incorporated to arrest crack growth by bridging cracks, for
which a much longer length of fiber must be recruited to stretch, for
which the fiber needs to slide through the matrix.  So sizing is
necessary to *weaken* the bond between the fiber and the matrix,
*causing* material failures to be pullout failures — still at a lower
stress than would be needed to break a solid, defect-free block of the
material, but with enormously improved toughness.  This can even
translate to higher tensile and flexural strength in the case of
non-defect-free brittle materials, where microcracks can reduce their
theoretical tensile strength by many orders of magnitude.

So, what kind of sizing could you apply to the glass fibers to weaken
their bond to the matrix?  You want it to be much softer than the
other materials involved, and to completely cover the glass fibers, or
at least almost so, which suggests that you’d like it to be amorphous.
You want it to be water-insoluble so it will survive when the matrix
is infiltrated into the fibers, but applicable hydrothermally rather
than with some kind of white-hot gas or something.  And you want it to
be cheap, which eliminates most organics.  Precipitating amorphous
calcium phosphate or aluminum trihydroxide from aqueous solution might
work; there are also a number of softer insoluble phosphates and
carbonates of polyvalent cations, such as rhodochrosite, siderite,
vivianite, wolfeite, smithsonite, hopeite, malachite, azurite,
magnesite, struvite, and calcite.  Oxide and hydroxide minerals might
also be candidates.

Amorphous deposition isn’t essential, but if we hydrothermally deposit
a crystalline sizing material, there’s a good chance there will be
gaps between the crystals that leave the glass exposed.

Another approach would be to expose the fibers to something that
reacts enthusiastically with the exposed glass (for which there are
relatively few candidates at ordinary temperatures, mostly silanes)
and forms a monolayer on it, and then something else that reacts with
the monolayer, perhaps repeating the process several times.

Infiltrating loose glass fibers very briefly with a low-density hot
plasma of something that’s solid at room temperature might work to
deposit a thin, even layer on the surface of the glass without
damaging it, if the heat in the plasma isn’t sufficient to melt the
glass.  The layer would tend to be of relatively constant thickness
because the places on the glass where the plasma has already frozen
will be hotter than the places it hasn’t frozen yet.  For example,
tenorite and maybe cuprite (Mohs 3.5–4) will tend to precipitate from
a plasma formed by passing too much current through a copper wire
which is allowed to mix with air.  In an inert atmosphere, maybe you
could use vapor of aluminum or zinc.

If the sizing layer is thin compared to the fiber diameter, which
would be necessary in this crazy plasma process but maybe not some of
the others, the cost of the sizing is less of a concern.
