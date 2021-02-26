PCB contract manufacturers like JLCPCB (“CMs”) can not only cut out
your circuit board to specified shapes with a router (2-mm endmill),
but also score it with V-grooves on one or both sides, so you can
break it into panels.  Looking at the Boréas Technology evaluation
board, I see that it’s scored this way on one side to be able to break
it into three boards, but has traces across the scoring on the
opposite side of the board, so *until* you *do* break it into panels
this way, it’s a single board; but once you do, you can reconnect the
previously-connected pieces at a distance using a cable, or use them
separately.  Among other things, this approach is useful for
testability.

Other forms of panelization include routing that leaves tabs
(“tab-routing”) and drilling a series of holes, called “mouse bites,”
most often used to weaken a tab, avoiding the need to score it with a
knife, cut with diagonal cutters, or use a [depaneling nibbler][9].
Mouse bites in particular can create curved breakaway edges, and they
leave a rough edge on the board after breaking, which can be useful or
harmful.  JLCPCB in particular is willing to do some amount of
tab-routing without increasing their price of US$2 for 10 boards of
100 mm × 100 mm.  There are [established panelization guidelines][11].

[9]: https://www.eevblog.com/forum/projects/snap-off-pcb-sections-mouse-bites-vs-solid-tabs/msg3383966/
[11]: https://www.electronicdesign.com/technologies/boards/article/21801451/pcb-designers-need-to-know-these-panelization-guidelines

SparkFun has a whole “ProtoSnap” product line based on this idea;
[their ProtoSnap Pro Mini][5], for example, had an Arduino Pro Mini
SBC already wired up to a USB-to-serial converter, two actuators, two
sensors, and a prototyping area, and their [LilyPad ProtoSnap Plus][6]
has a LilyPad similarly preconnected to several sensors and actuators
and conductive-thread connectors, which can then be broken apart at
the tabs and reconnected elsewhere, like in your clothes.

[5]: https://www.sparkfun.com/products/retired/10889
[6]: https://www.sparkfun.com/products/14346

LED tape often comes with similar cut points, where you can cut it
with scissors to a given length, but if you don’t, the whole tape can
be hooked up to from 2–4 wires.  (Such tapes might cost [US$19 for
5 m][0], [US$43 for 5 m][1], or [US$17 for 4½ m][2] at retail here in
Argentina.)  “Flat flex PCBs” are printed on thin Kapton and commonly
used as connector cables, and can be cut with scissors in a similar
fashion.

[0]: https://articulo.mercadolibre.com.ar/MLA-787222000-tira-de-led-pixel-5v-5050-30-ledxm-inteligente-ws2812-ip20-_JM
[1]: https://articulo.mercadolibre.com.ar/MLA-787221816-tira-de-led-pixel-5v-5050-60-ledxm-inteligente-ws2812-ip20-_JM
[2]: https://articulo.mercadolibre.com.ar/MLA-825408790-tira-led-luces-colores-autoadhesivas-exterior-control-remoto-_JM

And, of course, prototyping perfboard is pretty easy to cut along the
perforation lines.

There’s also [a technique to allow electrical continuity across
V-scores cut on both sides of a board: a plated-through hole][4] that
the V-score runs through, so the plating in the hole electrically
bridges the V-score.

[4]: https://www.youtube.com/watch?v=V5BDcEqEaKg

Circuit board “edge connectors” are interesting to mention in this
connection: ISA cards, PCI cards, DIMMs, and many USB-A devices have
no separate connector, just exposed copper, either on one side of the
board or both.  (Zebra-strip, Z-tape, and pogo-pin “connectors” on
PCBs are also commonly just exposed copper.)  Such connectors can be
provided at a place that’s exposed by snapping at such V-grooves.

You could imagine designing a circuit board that works as a whole, but
can also be broken into smaller circuit boards, or cut with scissors,
to get more reconfigurability.

Custom PCB manufacturing is amazingly cheap; [TrickyNekro reports €10
for 100 boards of 38 mm × 18 mm each][3], plus normally US$20 for
“shipping”.  And if the panel size is *exactly* 100 mm × 100 mm, they
used to not charge *anything* for V-scoring (though [reportedly that
was only if all the boards in the panel were identical, and they now
charge something like US$8 for V-scoring][8], while [others report
problems getting JLC to V-score][10]), although I don’t know if there
was a limit to how many lines you could request on your “board outline
layer (\*.GKO)”.  In the same thread, georges80 reports 3–4 day
turnaround to the US West Coast, paying:

* US$20 for “the protos” (???)
* US$32 for “10 pieces with 3 [2-layer] boards on a panel with ‘jlpcb’
  panelization which is v-scored”
* US$68 for 25 165 mm × 75 mm panels of 10 [2-layer] boards each,
  including paying extra white solder mask

[3]: https://www.eevblog.com/forum/projects/jlcpcb-opinions-and-more/
[8]: https://www.youtube.com/watch?v=iYrUztOn3dU "How to manually panelize PCBs, 02018-11-21"
[10]: https://old.reddit.com/r/PrintedCircuitBoard/comments/a9mgfk/how_to_indicate_vcuts_for_jlcpcb/

And blazini36 reports getting 10 100 mm × 75 mm prototyping boards for
US$27, including shipping and an extra US$8 for the boards being blue,
in 3 days, on several occasions, while OSH Park wanted to charge them
US$300 and delay 12 days.  Battlecoder reports that they paid US$12
for 10 prototype boards, and had to wait a month, because JLCPCB
doesn’t have free shipping to their (unspecified) country.

Nobody in the thread is sure if they can do V-scores at arbitrary
angles as well as straight across.

It occurs to me that this sort of thing might also be useful for
*mechanical* construction, although the shapes you can V-score are
even more limited than the shapes you can laser-cut — no sharp curves
or inside corners.  JLCPCB uses a cutting wheel to cut the V-scores so
you can’t even do curves.  But if you can get some slots routed out in
addition to the V-scores, you could get a pretty productive
“construction set” pretty cheap.  (You’d have to wear gloves to keep
the fiberglass out of your fingers.)  And then you can solder the
joints to hold the assembled pieces in place, like the FR4 mill.

If you could get a 100-mm-square panel panelized with V-scores into a
hundred 10-mm-square pieces, which would take 18 V-scores (higher than
the usual 5 or so, but not by that much) it seems like you could get a
pretty large set of circuit components.  With 2.54-mm-spaced holes
along the edge (which I think normally costs extra) you could have six
breadboard-compatible/Dupont-cable-compatible pins on each such
microboard.  Backing off a little bit, if you only panelized the panel
into 50 10 mm × 20 mm pieces (13 V-scores), you could have 6
breadboard pins along each edge and a 4-pin USB-A connector at one end
of the board.

Going to the extreme, [SparkFun sells a US$8 perfboard totally
crisscrossed with V-scores][7] so you can break it into 1250 pieces.

[7]: https://www.sparkfun.com/products/13268