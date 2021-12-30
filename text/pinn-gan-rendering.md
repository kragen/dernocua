(This is pretty much talking out of my ass since I’ve never done
anything with neural networks and almost nothing with automatic
differentiation and gradient descent.)

Physics-informed neural networks (PINNs) are an interesting approach
to numerical solution of partial differential equations: you train a
neural network to map (x, y) or (x, y, z, t) values to the value of
the PDE solution.  The training procedure involves running some sample
points through your candidate network and calculating the derivatives
of the output with respect to the input coordinates, thus giving the
derivatives that you’re trying to impose conditions on, and then
calculating a loss based on how far the conditions are from being
true.  You typically need to make sure you have a number of points on
your boundary in your training set in order to sample the boundary
conditions.

A potential question here is how to decide which points to pick,
because it may be the case that it’s easy to get a solution that works
correctly most places but is way off in a few crucial places.  A
solution that seems promising to me is to train a GAN (“generative
adversarial network”) to generate (x, y, z, t) tuples from some random
number; the GAN is optimized to find tuples that produce a large loss
for the PINN.

An interesting thing here is that, unlike more typical ways to
numerically solve PDEs, there’s no sample grid.  The trained network
represents the solution in a fully continuous fashion; you feed it any
arbitrary (x, y) pair and it tells you what it thinks the value is at
that point.

It occurs to me that you ought to be able to use the same approach to
ray-trace a scene or film: train a network to map an (x, y, t) triple
to an (r, g, b) triple in such a way as to minimize the error from
some “ground truth” raytracing.  You feed the same (x, y, t) tuple
into a real raytracer written in the normal way to get the “ground
truth” pixel; by applying automatic differentiation to the raytracer
you can get the color gradient and movement at the sample, and by
applying it twice we can get a Wronskian (?) that tells us how these
gradients are varying.  Then we can compare these results to the
corresponding results from the neural network to compute the loss.

By training a GAN to generate difficult coordinates we can focus our
optimization efforts on the places in the image which are particularly
hard to approximate well, or at any rate particularly poorly
approximated so far.

You might get better results by training a couple of stages of the
raytracing network separately: for example, one stage that maps (x, y,
t) tuples to (x, y, z, t) tuples where the ray intersected something,
then a second stage that transforms these tuples into something like
(x, y, z, u, v, oid, t), and then a third stage that transforms that
into the actual color.  The benefit here is that you can use the
traditional raytracer to train these intermediate tuples.

It might be possible to solve the rendering equation spatially by this
method as well, deriving a neural network to approximate the light
field: at any given point in space, looking in a particular direction,
you see a particular color.  In free space this color is the same that
you would see if you moved in that direction; on a diffuse surface,
looking into the surface, you see the color at the surface illuminated
by the color you’d see integrated over all possible viewing
directions; etc.

For numerical integration, maybe you could train a neural network (or
other universal approximator, such as a spline) to approximate the
indefinite integral of the function you want to integrate, generating
random (or adversarially generated) points at which to compare the
derivative of your approximation with the original function to compute
your loss.  It’s hard to imagine how such an approach could ever be
cheaper than just doing Gaussian quadrature in one dimension, but
maybe if you have multiple independent variables, or if the limits of
integration or a parameter of the function vary?

Another way to apply the PINN idea to rendering is to sample some
pixels from a “real” raytracer, either the conventionally implemented
raytracer or a universal approximator as described above, and then try
to extrapolate the rest of the image from those pixels, in the same
way that a PINN extrapolates the rest of the field from its boundary
conditions.  That is, you train an image-generating network to
generate a visually plausible image that has the correct values at the
sampled pixels, computing its loss from the error at the sampled
pixels and a canned GAN discriminator network (probably a convnet)
that judges visual plausibility.  A second adversarial network can be
used to decide which pixels to sample, looking for pixels with a large
error, since you can sample more “test set” pixels once your
image-generating network is trained.

This might be faster if you start with an image-generating network
that already generates visually plausible images.

Normally you train a PINN simultaneously to satisfy both its
constitutive PDEs (which in the above case are replaced with a
discriminator) and its boundary conditions.  You might be able to get
a speedup on this by starting with a PINN pre-trained for the same
PDEs and retraining it with new arbitrary boundary conditions, but a
different approach is to include some samples from the boundary
conditions among the PINN’s inputs, along with (x, y[, z, t]).  If
this works, it gives you a PINN that solves an entire class of PDE
problems instead of just one, allowing you to change the boundary
conditions without retraining the network.  To get a precise solution,
you still might have to retrain the network.

Training a PINN to produce the SDF of a scene might be an interesting
approach; the SDF is constrained to have value zero at objects’
surfaces, negative inside them, positive outside, and to have a
gradient with magnitude unity *almost everywhere*, in the sense that
the cusps in the SDF (where the gradient has some other value) have
measure zero, unless the surface geometry is fractal.  So, if you’re
just sampling at random, you’ll find those cusps with probability
zero.

A different way to use a PINN as an SDF is as a cheap-to-compute lower
bound, training it to produce the tightest lower bound you can.  Using
interval arithmetic you can exhaustively evaluate the PINN and the
real SDF over various parcels of space and find a bound on the worst
case where the PINN drops below the true SDF; by adding this number to
the PINN’s output, you get a true lower bound.  You can evaluate this
cheap function for most SDF probes, only falling back to the true SDF
(or maybe a small part of the true SDF) when the conservative
approximation falls below 0.

A third approach to render images with a PINN is holographically: to
look for solutions to a wave equation representing the propagation of
waves through the scene.  I think this can be a static field (i.e., a
3-dimensional problem rather than 4-dimensional) if the state
variables at each point are complex rather than real, thus encoding
not only amplitude but phase.  For everyday macroscopic objects,
diffraction effects normally only become noticeable at dramatically
smaller scales than we normally look at (micron-scale, say), so the
wavelength of the waves can usually be considerably longer than that
of light.  With a finite-element or sample-grid representation, this
would reduce the computational effort enormously, but I’m not sure if
it will matter for a PINN.  If it *doesn’t* matter much, that would be
a *huge* advantage for computational holography, which unavoidably
must use light’s real wavelength.

Simulating polarization, for example for compound Fresnel-equation
reflection, probably requires more than the two reals suggested above
per point in the field; I don’t know how many you need.  Doing color
probably requires doing three separate simulations.

It seems likely that three-dimensional or four-dimensional
convolutional neural networks are likely to be useful for PINNs, but
perhaps not as intermediate layers on their own; rather, you might
need some intermediate layers that have convnets *in parallel with*
conventional fully-connected layers.

The standard rendering problem is, given scene geometry (and
materials, etc.), compute one or more 2-D images.  From a certain
point of view, vision is exactly the opposite problem: given one or
more 2-D images, compute the scene geometry.  Gradient descent and
other generic optimization algorithms are thus applicable to turn any
rendering algorithm into a vision algorithm, and they can additionally
be guided by a neural network that is trained to produce geometries
that are more probable (an approximate prior over world scenes).
