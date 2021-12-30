As I understand it, compliance is the derivative of position with
quasistatic force, and in a linear system this is a constant.
Nonlinear systems have compliance that varies with position; think of
a probe touching skin with subcutaneous fat over muscle and bone.
Compliance is high at first because of the fat, but with larger
displacements the fat is squashed out enough that now you’re measuring
the compliance of the muscle, which increases rapidly with further
displacement.  I suspect that this kind of force-displacement curve is
important to the tactile sensations of softness, hardness, etc.

Generally I think that, if you want to plot the curve, you want to
plot the *derivative* of force against displacement, which is to say,
the compliance as a function of displacement.

Along a second dimension, we have the frequency at which the force is
being applied; for some systems, resonant modes will give very large
“compliances” at some frequencies and smaller ones at other
frequencies, tending to the quasistatic limit as the frequency
approaches zero.  The degree to which the system exhibits these
resonances gives you some information about lossiness in its
elasticity.  A steel spring might have the same compliance as a cotton
pillow, and you can taper the spring to make its compliance vary with
displacement (as mattress makers do routinely), but the cotton pillow
will lack any sharp resonant peaks because it’s very lossy, so you can
easily distinguish them.  This is noticeable if you just tap both
systems with a coin.  Other systems have other characteristic
resonances.  Nonlinearity will produce vibrations at other
frequencies, including harmonics and subharmonics, vaguely like Raman
emission but in the acoustic domain, potentially adding a third
dimension.

This sort of “viscoelasticity spectroscopy” or “compliance
spectroscopy” is potentially useful for a number of different
purposes:

1. Teledildonics.  Nonlinear compliance is crucial to reproducing the
   tactile sensation of touching a human body.
   
2. Somatic and haptic interfaces; by distinguishing a finger pressing
   a button from a palm or a floor pressing it, software can
   distinguish between different actions to take.  Even pressing a
   button with the same finger at different angles can be detected.
   Tiny total internal reflection compound parabolic reflectors could
   be integrated into a button to provide a simultaneous optical
   interface for coupling LED illumination in and out of a finger
   without the discomfort occasioned by the LED bumps traditional in
   pulse oximeters.  This, too, has obvious masturbatory uses: a
   vibrator can be programmed to respond to not only the pressure it’s
   put under but also the compliance curve of the tissues it’s
   stimulating.

3. Material identification.  This is somewhat trickier, because the
   compliance spectrum of an object depends on many things other than
   the material it’s made of; for example, what shape it is, how
   firmly it’s being held, and what it’s being held in.  But with the
   whole 2-D spectrum, it might be feasible to tease out at least a
   guess.

4. Material characterization.  If you make a standard-geometry coupon
   of the material being tested and hold it in a standard way, the
   above variations go away, and you can compute quantitative
   viscoelastic properties of the material.  Alternatively, at high
   enough frequencies, it should be possible to characterize just the
   material in the region around the probe.

5. Object identification.  You can use compliance spectroscopy to
   distinguish multiple objects, even if they are made of the same
   material.
