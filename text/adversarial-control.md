Model predictive control is now the standard approach to control
systems: given a model of the system and an objective function, you
use an optimization algorithm to seek a behavior that maximizes your
objective by modeling the effects of different candidate behaviors on
the system.

The reinforcement learning problem is in some sense more general, in
the sense that in model predictive control, the control system is
given a model of the system being controlled (the "plant") which is
presumed to be correct, so it can predict the effects of its actions,
but a reinforcement learner doesn't initially know what behaviors will
have what effects; it must build that world model by observing the
results of different behaviors.  This means that it benefits greatly
from doing some undirected exploration, focusing its actions on the
parts of the possibility space where its predictions are the least
confident.

This is somewhat disquieting for someone contemplating control systems
for a chemical plant or a satellite, where incorrect control commands
could end a million-dollar mission or cause a toxic-waste release into
the neighborhood.  But of course it is not only undirected exploration
of the system's parameter space that can cause such results; running a
model predictive control system with an incorrect model can also cause
them.

The amount of undirected exploration that is needed diminishes over
time as the control system solidifies its system model, a process
sometimes called "system identification" in the literature on
dynamical systems modeling and control theory, so one way this can be
handled is by initially training the control system in some sort of
"sandbox" where its ability to cause damage is limited; the humans
call this "childhood" when they provide it for their larvae.

Another safety strategy is to focus experimentation on the
possibilities that your existing system model tells you have low
probability of causing significant harm, but which have high
uncertainty in some other dimension that isn't so costly.  Call this
"safe experiment design": a human might use high-powered lasers to can
observe effects only observable with high-powered lasers, but wear the
correct laser goggles to reduce the chance of being blinded in the
process.

But a third, and I think most important, strategy for this kind of
system identification is *dreaming*, and generative adversarial
networks (GANs) are a strategy used with great success for dreaming in
the world of artificial neural networks.  Essentially the idea of a
GAN is to optimize a generative model of some kind of probability
distribution, such as the probability distribution of photographs of
dogs, or the probability distribution of satellite telemetry traces,
by playing off two networks against one another: a generator and a
discriminator.  The generator generates random deviates from its
approximation of the distribution, and the discriminator distinguishes
these adversarial inputs from real training-set inputs.

You alternately optimize these two networks, typically with some
variant of gradient descent driven by automatic differentiation.  By
carrying out automatic differentiation all the way through the
generator and discriminator, we can find the gradient of the
generator's parameters that would worsen the discriminator's ability
to discriminate, using that to drive an optimization algorithm like
Adam; and by differentiating just through the discriminator, we can
find the gradient of the discriminator's parameters that would improve
its ability to discriminate.  It's important to optimize these
somewhat in lockstep; if either network gets too far ahead of the
other, the loser will stop improving.  If done correctly, the
generator produces inputs that are very, very difficult to distinguish
from real inputs from the training set.

(The typical "networks" here are standard ANNs, where matrix
multiplies and weight-vector additions alternate with ReLU and maybe
convolutional and pooling stages, but almost any computational model
could potentially be used.  Being differentiable enables the use of
derivative-based optimization algorithms, and it's important to have
enough expressivity to reasonably represent the distribution in
question but not so much that you overfit the training set, but there
is an enormous field of unexplored models here.)

As far as I know, nobody is using GANs for system identification for
control systems, much less model predictive control in particular.
There are several particular ways I think it would be useful to apply
such "adversarial control".

1. You can use a GAN to produce a black-box system model from the
    observed behavior, which you use in the usual model-predictive
    way: use any standard optimization algorithm to compute a control
    strategy (in the sense of a sequence of planned control outputs)
    that maximizes your utility function (or, equivalently, minimizes
    your cost or loss function), by using the generator from the GAN
    to predict what would happen if each candidate strategy were
    followed.  The generator normally needs to be stochastic, since
    there are always unobserved variables driving the behavior seen in
    the training set, and so it's possible to get estimates of
    uncertainty --- at least by drawing several deviates from the
    generator and looking at their spread.

    It's fairly straightforward to use this to assess the "risk" of
    the candidate strategy --- you just look at the spread of
    objective-function evaluations, or possibly even the derivative of
    the objective function with respect to the hidden variables that
    you feed to the generator to make it act stochastic --- but I feel
    like there's also some way to derive from this the "learning
    value" of the proposed strategy as an experiment.  I think the
    story is that you first differentiate the objective function (over
    the whole distribution the generator can generate), or possibly
    its derivative with respect to those hidden variables, with
    respect to the parameters of your *generator*, to get a gradient
    that tells you which parameters of your generative model are most
    important to simulate accurately; and then you assess the learning
    value of the proposed control strategy by calculating how much
    you're likely to update those parameters with that strategy.

    That is, you're looking for parameters of your generator which the
    outcome of this experiment would nudge in a way that makes a
    significant difference in your objective function in some
    scenarios, but ideally not the scenario you're facing at the
    moment (the safe experiment design problem).  By dreaming of being
    chased by monsters (a scenario drawn from your generator in which
    a bad strategy results in you dying horribly) you learn which
    aspects of reality your generator needs to model better, and so
    what you should try to find out by taking actions in real life;
    for example, you may want to look under your bed, because it's a
    safe thing to do, but if there are monsters there, you will see
    them and can update your system model in a way that will greatly
    increase your utility.

    This is not a metaphor; I'm proposing that the humans' neurology
    actually works in the way similar to what I'm describing above,
    [though it doesn't use automatic differentiation and
    backprpagation][0], and that is why they literally look under
    their beds for monsters; or at least that this formalism is a good
    way to get similar kinds of intelligent behavior.

2. You can use a GAN to optimize a control network built out of
    whatever components are inexpensive in your deployment context,
    such as transistors, resistors, capacitors, and diodes, or Mark
    Tilden's BEAM-robotics Nv neurons, or opamps, or FPGA LUTs and
    flip-flops, or links and kinematic pairs, by simulating different
    such candidate control networks in a wide variety of scenarios and
    scoring their performance on an objective function.  The appeal of
    this approach is that it allows you to build a control system that
    can handle low-level control tasks with very low latency and low
    cost, while being itself controlled by a higher-level control
    system which provides them with some kind of time-varying set
    point.  A feedback loop consisting of a few RF transistors and
    some passives has a potential latency in the nanoseconds rather
    than the milliseconds typical of hard-real-time software control
    loops, but it will necessarily be wildly nonlinear and have many
    unpredictable characteristics due to manufacturing variation,
    aging, and temperature.

3. Applying the adversarial-control approach recursively, in order to
    accurately model your control network, you can build a generative
    adversarial model of your circuit components and of circuits built
    from them: the discriminator tries to distinguish data measured
    from real circuits processing real signals from simulations
    generated by the generator, while the generator tries to simulate
    the real circuit so faithfully that the discriminator can't tell
    the difference.

4. In a further level of self-reference, if the discriminator is a
    recursive neural network or other dynamical system, we can give it
    another tool to beat the generator with: let it generate test
    signals to feed into the circuit and observe the response, thus
    exploring corners of the circuit's behavior that the generator
    hasn't yet succeeded in simulating.  (In some cases you will have
    to optimize the discriminator not to generate signals that your
    simulations suggest will damage the circuit.)

5. If both your control network and your generator are themselves
    differentiable, you can differentiate not just your objective
    system but the system's state vector with respect to *either* the
    initial system state vector *or* the hidden-variable inputs that
    make the generator stochastic, which has an established name that
    I forget.  (Sometimes people talk about things like "the latent
    space of faces", and though I think that's more a variational
    autoencoder kind of thing than a GAN kind of thing, that's the
    kind of hidden variables I'm talking about.)  One potential
    benefit of this is that it allows you to make statements about the
    stability of your control-stabilized system in a way that you
    can't with standard MPC.  Another is that it makes the kind of
    experiment design that I described in point #1 above amenable to
    gradient-driven optimization, because you can tell how to tweak
    your control network so that it will spontaneously engage in safe
    experiments.

[0]: https://www.nature.com/articles/s41593-021-00857-x

****

In the case of time series, both the generator and the controller will
generally need some history to start from rather than just a single
observed state vector, because they need to infer the state of some
variables in the system that are not directly observable.  For
example, if something has been warming up significantly even though
you aren't applying heat, maybe there's an unobserved heat source in
contact with it; the generator needs to simulate this situation for
the purpose of evaluating strategies, and the controller needs to take
it into account when formulating them, applying less heat than it
would otherwise.  And if you're planning a candidate toolpath or
simulating its effects, you'll need to know at what height the tool
touched off on the touch-off sensor, even if that was several minutes
ago.

Controlling digital fabrication is a particularly important
application because it enables the materialization of controllers, and
it is particularly interesting in several ways.  It includes
parameters that vary over a wide range of timescales, which is
especially challenging to simulate: a machine may wear out year by
year; the air around a machine may be hotter in summer than in winter,
causing parts to cool down slower; a tool may wear as it cuts, getting
progressively shorter and rougher minute by minute; the temperature of
a tool or hotend may increase second by second; and a tool that chips
will suddenly cut differently.  It normally takes into account many
physical phenomena: vibrational modes of parts, rigidity of machines,
temperatures, electric currents, side forces, measurement error,
acceleration force, etc.  And the objective function to optimize may
shoot through the entire design process: for example, how can we
position such-and-such a thing under such-and-such loads for the
lowest manufacturing cost?
