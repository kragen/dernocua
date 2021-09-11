I was thinking earlier about “voxel 3-D printing” with spot-welded
bearing balls, where each new ball added to the workpiece is located
by contacts with three existing balls, then spot-welded to each of
them in turn.  That way, the end effector doesn’t need to have
extremely precise location abilities, because the location is in the
precision of the bearing balls, which can easily and very
inexpensively be submicron.

However, spot-welding them will both induce stresses on the structure
as the nugget expands and then contracts, and also reduces the
precision of the distance between the centers of the balls; the bigger
the spot welds, the bigger this effect.  And with any practical size
of spot weld, the resulting structure will be much weaker than .
Also, it requires high power input from the end effector, even though
it’s electrical power.

The standard mechanical-engineering solution to locating and fastening
parts accurately is to use locator pins (or other features) separate
from the fasteners, such as screws.  By chamfering or tapering locator
features, it becomes possible to assemble parts with greater precision
than the precision of the manipulators, in the same way that the balls
in my first paragraph would provide high precision.  Somewhat
analogously, the position of a lathe saddle can be indicated much more
precisely by a dial indicator (or, nowadays, a digital readout) than
by the graduations on the handwheel, because (aside from backlash) the
kinematic chain of the dial indicator does not have to bear the load
of feeding the tool into the work.

The wedging action of a tusk-tenon joint makes such a permanent joint
for a somewhat related reason: the load on the joint is orthogonal to
the direction of movement of the wedge, so it does not tend to
dislodge it.

So I think that perhaps the best way to assemble things for a
permanent, rigid mechanical connection is:

1. Position them in a precise place using positioning features such as
   a Maxwell kinematic coupling.

2. Hold them in that place using a fastening system that can handle
   all the variations in position that the positioning system can
   produce, without producing large enough loads during the holding
   operation to create positioning errors.  For example, two parallel
   plates sliding against one another are a planar joint, with three
   degrees of freedom, until one or more screws through oversize holes
   in one into tapped holes in the other add enough friction to
   prevent movement.  A spherical ball-and-socket joint also has three
   degrees of freedom until enough friction is similarly added.  With
   a serial kinematic chain of three joints (of two or three degrees
   of freedom), you can provide all six degrees of freedom; putting
   them close together and putting more than one such chain in
   parallel can provide greater rigidity.  (There might be a way to do
   it with just two joints, but I can’t see it.)

3. Lock the holding/fastening mechanism with something adequately
   permanent, like self-propagating high-temperature synthesis to fuse
   parts together, some safety lockwire, a jam nut, or just a circlip
   or similar spring.  The loads will be borne by the
   holding/fastening mechanism, not by the positioning mechanism or by
   the locking mechanism, because the locking mechanism only serves to
   prevent the fastening mechanism from coming unfastened.

These three functions are not always so independent; in a four-jaw
lathe chuck, for example, each jaw fulfills both the positioning
function (when the other jaw is far away) and the holding function
(when it’s adding pressure to the part and thus friction to both the
part and the other jaw).  But I think separating them will generally
improve precision.  At times, in a lathe chuck, the moving function in
two rotational degrees of freedom is provided by tapping the workpiece
up against the flat face of the chuck, before holding the part in
place by tightening the jaws.

You could perhaps drench the balls in a viscous liquid that later
forms a glass, which can perhaps later be annealed into a
glass-ceramic, so that they are positioned by the precise Hertzian
contact between the balls, but then held in place by the glass or
glass-ceramic matrix.  This will work best if the matrix is nearly as
hard as the balls (in the sense of Young’s modulus) or even harder.
In effect, the matrix foam is the real object; the balls are just
there to provide it with precise dimensions, and they could be hollow
bubbles or even removed entirely after the matrix hardens.  Hollow
fused-quartz bubbles would probably be especially useful for this
purpose.
