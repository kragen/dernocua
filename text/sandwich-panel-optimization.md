[Wikipedia says the stiffness of a sandwich panel][4] is ½(f(2h +
f)²C) where C is, I think, the stiffness (Young’s modulus) of the face
materials, f is the thickness of the face, and h is half the thickness
of the foam (or similar filling).  This is ½C(4fh² + 4f²h + f³), which
is roughly 2Cfh² if h is big enough relative to f.  If you want to
maximize stiffness for a given (areal) density, then ρ₀f + ρ₁h is some
constant total density k, half our total density budget (here ρ₀ is
the density of the face material and ρ₁ the density of the filling),
so f = k/ρ₀ - (ρ₁/ρ₀)h, and the stiffness is 2C(k/ρ₀ - (ρ₁/ρ₀)h)h².
To find the maximum we can drop out the constant 2C/ρ₀ and set the
derivative with respect to h to zero; differentiating (k - ρ₁h)h²,
getting -ρ₁h² + (k - ρ₁h)·2h = -ρ₁h² + 2hk - 2ρ₁h² = 2hk - 3ρ₁h².
This derivative obviously has a zero at h=0, where the stiffness is
also zero, and the other extremum will be when 0 = 2k - 3ρ₁h, 2k =
3ρ₁h, h = 2k/3ρ₁ = ⅔k/ρ₁.

[4]: https://en.wikipedia.org/wiki/Sandwich_theory

I must be doing something wrong.  This says the filling should just be
⅔ of the total mass, regardless of the density or modulus of the face
material.  Stiffness, fine, that’s just a constant linear factor on
the stiffness you get at any point along the tradeoff spectrum.  But
shouldn’t it depend on the density of the face material?  No, because
higher density just gives you proportionally less face material and
thus less stiffness, so it's also just a constant linear factor.

And I guess this is actually correct.  If ⅓ of your mass is in the
faces, then making the faces 2% thicker makes the panel 2% stiffer,
but steals 1% of the mass from the filling, making the panel 1%
thinner.  Since stiffness is quadratic in thickness, that 1% thinning
reduces the stiffness by 2% (actually 1.99%), and the resulting
stiffness is only 99.9702% of the original thickness.  A similar thing
happens if you make the faces 2% thinner.

Interestingly, this generalizes to properties other than density that
scale with the volume of the material as well, in particular cost.  If
you want to maximize sandwich panel stiffness with given materials at
a given cost, you should have ⅓ of the cost in the faces, ⅔ in the
filling.  This is applicable to the roofing problem in file
`leaf-vein-roof.md`.