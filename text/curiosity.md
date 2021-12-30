Watching a talk by Deepak Pathak about “Learning to Generalize Beyond
Training” where he’s talking about helping reinforcement learners
perform better in the world by making them do non-goal-directed
exploration.

Pathak shows two photos, one of a toddler playing with her toy plane
wearing goggles, another of a young woman standing in front of a
fighter jet, and says, “In the real world, the reward could be delayed
by days, months, or years, such that it’s hard to project back to
where you are.  So how does this child over here know how should she
[sic] act to become pilot [sic] 20 years later?  Does she optimize any
reward and backprop all the way to her childhood?  Well, not quite.”
He cites Alison Gopnik’s work claiming that children are not driven by
extrinsic goals, but by intrinsic curiosity.  “Maybe by not giving
goals to the agent you are making it not overfit to the task.”

(And that explains why people learn so poorly when motivated by
extrinsic rewards, probably.  They’re overfitting.)

He then outlines some approaches for choosing what actions a
reinforcement learner should take to do “goal-free exploration”, which
in a sense is experiment design.

Pathak actually cited a dozen papers on curiosity and intrinsic
motivation (Poupart et al. 02006, Lopes et al. 02012, Bellemare et
al. 02016, Oh et al. 02015, Tang et al. 02016, Ostrovski et al. 02017,
Schmidhuber 01991, Schmidhuber 02010, Stadie et al. 02015, Houthooft
et al. 02016, Mohamed et al. 02015, Gregor et al. 02017) and said that
the originality of his approach was that his agent has no extrinsic
goals at all.

It occurs to me that there’s probably some kind of way to bend
gradient descent and its children to this task.  If you have some kind
of differentiable model (an ANN or whatever) of cause and effect in
your world, you can use it to maximize a reward (and children do of
course take goal-directed actions, for example to get food or to earn
their parents’ approval) by using gradient descent to seek the optimal
action: you compute the gradient of utility with respect to your
vector of planned action parameters, then revise the plan to increase
utility.  And you can optimize it to be a better fit to your existing
database of real-world experiences: you compute the gradient of
prediction error with respect to your world-model parameters (ANN
biases and weights or whatever), and adjust the parameters to decrease
prediction error.  So what does curiosity look like in this framework?

I think you can handle this with gradient descent as well.  If you
dream up scenarios in the world, for example by generating plausible
predictions forward from some arbitrary state, then you can ask your
model what will happen in those dreams, and perhaps in particular what
actions would be best.  In cases where your world model provides very
vague predictions (this may require that in some sense it gives you
Bayesian probabilities) you can compute that you are ignorant, and you
can use automatic differentiation to figure out which of the
parameters of your world model are responsible for that ignorance ---
dimensions in which your existing prediction error has a very small
gradient, but there is a large gradient in the dream.  Then, to be
curious, you can try to create situations in the real world that you
find unpredictable in the same way the dream was unpredictable, where
there are plausible outcomes that maximize the magnitude of the
resulting update in those ignorant parameters.

Or you could perhaps just choose actions whose results you cannot
predict.  But that might be more difficult: if you weight by utility,
you will be choosing the actions that are the most unsafe, and if you
don’t weight at all, you will just be choosing the actions that will
produce the brightest colors or loudest noises or most edges, whatever
your input feature space is.  So it might be best to leave the
generation of unsafe scenarios to your dreams, then permit the dreams
to inform you of which parameters of the world to be curious about so
that you can design experiments to investigate them in a safe way.

This formulation of dreaming or fantasizing is vaguely similar to the
concept of a generative adversarial network as a dreamer.

The phenomenon of “flow” suggests that there’s a nonmonotonic aspect
to intrinsic motivation in the humans: when prediction error is really
high, they lose interest in the task (it’s too hard) and when it’s
really low, they pay attention to other things (it’s too easy).
Pathak’s formulation seems to lack that nonmonotonicity: his agents
get more interested when things get more unpredictable.

Entropic formulations of the prediction problem (like, I think, about
half the papers Pathak cites) offer a different candidate for the goal
of curiosity: you want to improve your model of the world by reducing
the entropy of the past, so that it now seems obvious that the things
that happened were going to happen (“hindsight bias”).  But does that
mean you should look for parts of your model that are training slowly
because their gradients with respect to your training data are very
low, and try to do experiments that impact them?  It seems that
perhaps those are the parameters least likely to help you at
re-encoding the past with lower entropy.
