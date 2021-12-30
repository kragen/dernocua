Electrochemical machining cuts almost any metal, has reasonably high
material removal rates, has no side loading or heat affected zone, and
permits cutting fairly free-form parts in 3-D, much like CNC milling.
But in its ordinary form it can’t cut parts with complex internal
spaces, and in a pure 3-axis form it can’t even cut overhangs.

Watching demo videos of ZURAD Engineering’s ECM jet-cutting machines,
though, it occurred to me that we can go further still.  If we use ECM
cut layers of the 3-D shape we want, then stack them up, we should be
able to get not only much freer-form shapes, but also effectively a
higher material removal rate, since we only need to remove a perimeter
of stock around the shape of each layer, while if we were cutting the
same part out of a solid block of stock, we’d have to remove all the
material all the way to the surface of the stock.

There are many possible ways to manage the layer stackup, but locator
pins for alignment and thin plastic backing for each layer seem like
one straightforward option; the pins can instead be replaced with thin
strips that are cut out with ECM in the same way..  The plastic
backing can be burned away after the layers are stacked up.

After roughing out the shape in layers this way and stacking them up,
you can do the final precision shaping work with ECM on the stacked-up
part.

[ZURAD’s soon-to-be-open-source ZURAD Two EC Jet Cutter][0] evidently
cuts 1mm-thick sheet steel with a gentle stream of water with 100
grams of NaCl per liter of water (or was it 200?), with the metal
nozzle about 2.5 mm away from the steel.  For some reason he positions
the sheet steel horizontally instead of vertically.  The video looks
like it cuts at about 2mm/sec, but at one point the guy holds up a
part (“a simple mechanical pawl”) with a perimeter of about 100mm, and
says it took an hour and a half to cut completely through, so maybe it
took 50 passes.  I have no idea what current or voltage he’s seeing;
on his die-sink ECM machine he uses 12 volts.

[0]: https://www.youtube.com/watch?v=jTk1wRwtbQ4
