Some random ideas to try in UIs:

- How about crosshairs instead of a mouse pointer?  Boundaries between
  gradients, maybe, rather than opaque black lines.  Your mouse
  pointer shouldn’t obscure anything, and being able to use it to see
  the alignment between things is occasionally useful.
- Or maybe crosshairs with a vertical line that only goes down?
- what if the crosshairs are done with some kind of filtering that is
  subtle enough that you barely notice it when it's not moving.  like
  an edge enhancement kind of filter say.
- circles are a common alternative for indicating a point in some
  other contexts, like screencasting software and touch ui
- Maybe for 3-D rendering a bit of Lambertian surface bumpmapping
  would help with adding the illusion of 3-D-ness?  If the bumpmapping
  is bandlimited well below the pixel frequency then visual
  discontinuities will coincide with depth discontinuities.  Perlin
  noise maybe?  Simplex noise?  Blue noise?  Ambient occlusion might
  help add depth cues too.
- You can render a sphere as a circle very quickly, but it looks like
  a disc.  If you add an elliptical contour between light and dark,
  though, you can add a lot of spherishness very quickly.  Spheres
  have some merits compared to triangles as 3-D primitives.
- Directly highlighting depth discontinuities with edge features
  (black lines, white lines, Gabors, sincs, whatever) might also
  improve rendering legibility.
- This NeRF stuff produces really impressive 3-D renderings.  Can some
  kind of sparse representation of a radiance field be useful for user
  interfaces too?
- What does a UI for guiding heuristic A*-like search through an
  exponentially large search space look like?
- when exploring a search space covering orders of magnitude through
  manual dimensional search, maybe you can have buttons for ½×, 2×,
  10×, .1×, etc., each accompanied by a preview of the variables of
  interest there.  iphone software often displays the previews as the
  background of the buttons, also handy for things like choosing color
  palettes.
- what would a ui scripting language look like.  like, something for
  easy exploration of different ui dynamics, like a simple game
  scripting language for ui components.  how can we minimize the time
  between coming up with a ui idea and trying it out on yourself.
- low-ui-budget software i see screencasts of on youtube (optistruct,
  notepad plus plus, abaqus, matlab, origamizer, etc.) is mostly a
  fairly small number of ui components that look straight out of
  win95.  pulldown menus, dockable buttonbars, radio buttons with
  black dots inside white circles, checkboxes, gray backgrounds
  everywhere, accelerators, buttons, tab panels, a status line along
  the bottom of the window, dropdowns, dialog boxes, text fields,
  scrollbars, occasionally a slider or spinbutton.  one thing that's
  surprisingly common is a tree control in the left pane.  i suspect
  that a lot of this is stuff that people find very familiar by now
  and so departing from it should be done with care.  even tinkercad
  has a fair bit of this feeling even though it's in the browser.
  catia definitely has its own look but it still has win95-style
  comboboxes with the little downward-pointing isosceles right
  triangle on a gray embossed button and shitty little toolbars around
  the viewport and shitty opaque gray dialog boxes full of forms.
- one way that a lot of this software is kind of nice is that they
  often display what could be tooltips in the status bar.
- meshmixer is a little nicer looking by virtue of, among other
  things, translucency, fewer larger buttons with labels, and more
  visual texture and gradients.  ambient occlusion just about shows up
  in its clicky gui.  prusaslicer also uses translucent overlays (with
  sparklines even) in the corners of the main viewport to good effect,
  and does the smae kind of thing with some dialog boxes.  fusion 360
  of course overlays its tree view on the left side of the viewport
  with cracks but not much translucency.
- iphone software often overlays text labels for buttons in a popup
  menu over the main viewport, so the (often translucent) buttons on
  the menu minimally obscure the main viewport.  though this kind of
  text overlaying thing wouldn't be very useful if what's in the main
  viewport is actually text, in which case reflowing it to miss the
  menu would be more useful.
- also typically instead of radio buttons iphone software has a slidy
  switch thing with a circle that can slide to different positions in
  the radio button group.
- a common fui trope is to put statusbarry things in folder-tab-like
  things with 45° angles protruding onto the main viewport.  also of
  course in fui everything is transparent, blue, and circular.
- slight delays between animating multiple items are common in modern
  chi prototypes and break up the appearance of solidity, reinforcing
  the multiplicity of objects
- graying out the background when a pie menu or similar modal pops up
  is really helpful for focusing attention
- integrating high-res touch surfaces into projected or
  glasses-displayed ar environments can provide higher-resolution and
  lower-latency interaction possibilities, though xiao's work has
  shown that common touch surfaces can't really do any better than
  depth cameras (5mm or so); you need better-quality touch
- just as sound is the lowest-latency interaction modality, vision is
  the highest-bandwidth one, and that's underused at present, in part
  because people aren't chameleons or octopodes.  but they can draw.
  for some reason gesture tracking via camera analysis is still janky and jerky.
