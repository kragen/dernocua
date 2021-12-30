Emacs has some key commands involving pressing multiple keys at once
that are sometimes described as “chord commands”, which can be pretty
inconvenient to type.  I’m using C-M-v to scroll down the other
window, for example, and M-{ and M-} to move by paragraphs, which
require the shift key.  I also use M-< and M-> to move to the
beginning or end of file pretty often.  M-^ (M-shift-6) joins lines
together, which I do regularly.  M-% (M-shift-5) is search and
replace, which I use pretty often.  M-| (M-shift-\\) passes the region
to a shell command.  C-M-w does “append-next-kill”, which is
occasionally useful.  M-: (M-shift-;) is the eval-expression command,
which I probably use as often as M-x.  C-@ and C-_ are common commands
that would be similarly inconvenient, but fortunately C-SPC and C-/ do
the same thing.  I occasionally use C-M-left and C-M-right to move
over parenthesized expressions.

Key sequences like the infamous C-x 8 RET, C-x 8 _ a, C-x RET C-\\,
and so on, are also inconvenient; of course, like the chords, they’re
hard to discover; but also you have to type them in the right order,
which slows you down, it’s a real pain to do one of them repeatedly,
and they amount to a short-lived modal interaction, which causes mode
errors.

So in some ways the chords are preferable, but they cause repetitive
stress injury.  Also, in one way, even the chords are not real chords:
on a piano it doesn’t matter if you hit the G key 4 milliseconds
before the C key or 4 milliseconds after, but Emacs definitely cares a
lot about whether you press A and then Ctrl, or Ctrl and then A.  So
even the chords are slower than they need to be.

But there are about 132 keybindings in global-map and another 32 in
esc-map, plus more commands provided by one mode or another (`apropos`
finds 3685 commands currently loaded), and only about 88 keys on this
keyboard, most of which normally have to be used for writing.  Most of
the ones that aren’t for writing (Esc, F3, Insert, the arrow keys,
etc.) are in very inconvenient places.  So it would seem that
inconvenient chords or key sequences are inevitable.

But can we do better?

The home row has 12 keys on it, if we omit the nonstandard position of
\\, and there are another 24 keys almost as easily reachable above and
below, plus the space bar, the )} key, and on this keyboard the ><
key, for a total of 39.  In a spectacular feat of perversity, this
doesn’t include the number keys, Esc, Enter, Backspace, Ctrl, Alt, or
the left Shift key.  But it does include Tab and the worthless Caps
Lock.  (I usually press Alt with my spacebar thumb, so maybe we have
40 convenient keys.)

It occurs to me that a much more manageable sort of chord would be one
where you simultaneously press some magic “command key” and one *or
more* keys for the command.  So, for example, Alt-Q might be one
command (and should act identical regardless of whether you press the
Alt first or the Q first), and Alt-Q-O might be another command (the
same command as Alt-O-Q).  So any permanent effects of the command
wouldn’t take effect until you started releasing keys.  (They could
totally change your view, though, since that’s reversible.)

Here are the keys conveniently reachable by each finger:

- left pinky (6): tab, capslock, <, q, a, z
- left ring (3): w, s, x
- left middle (3): e, d, c
- left index (6): r, f, v, t, g, b
- left thumb (2): leftalt, space
- right thumb: nothing except space
- right index (6): y, h, n, u, j, m
- right middle (3): i, k, ,
- right ring (3): o, l, .
- right pinky (6): (, ), ;, ', /, rightshift (disregarding the nonstandard \\)

If the left pinky is tied up with capslock, then there are 3 × 3 × 6 ×
2 × 6 × 3 × 3 × 6 = 34992 possible capslock-based chord commands, and
there’s an even larger number of chords accessible with Alt as the
command key, but we probably want to limit ourselves to chords that
don’t involve too many fingers, both due to human limitations and due
to key jamming and ghosting.  Even chords that involve only two
fingers can be awkward; try Alt-E-X, for example.

A very simple sort of first-level command set is the number of chords
that involve Alt, one key from the left hand, and one key from the
right hand, since those are all guaranteed to be easy to type.  There
are 17 left-hand non-thumb keys (15 if we remove capslock and the
Spanish-keyboard-only <) and 18 right-hand non-thumb keys, giving 306
commands.  This is a promising number of commands, and I think that
key jamming and ghosting won’t be a problem at all on any reasonable
computer keyboard with Alt plus two regular keys.

You’d think that in 02021 keyboards would handle at least three, but
in fact even without Alt, this keyboard gets key jamming between Q and
S when A is depressed, between A and W when S is depressed, between Z
and S when X is depressed, and so on.  Perhaps more alarmingly, FGH,
HJK, CVB, and VNM also form such jamming triples, even though they’re
physically all in separate columns of the keyboard.  It may not be a
coincidence that these all include pairs of keys that are supposed to
be pressed with the same finger (FG, HJ, VB, and NM respectively); the
keyboard may be designed (using the term generously) for correct
touch-typing technique.  Still, it makes me worry that some common
keyboard out there will jam on easy-to-type combinations like FJK.

I think that generally the difficult-to-type chords are difficult to
type because they have fingers of the same hand two rows apart: QV,
ZT, WC, XR, Y., but not QF, AV, ZG, AT, WD, SC, SR, XF, YL, or J..  I
think this gives a large number of four-key chords in consisting of
Alt with the thumb, one key or two keys in adjacent rows or the same
row on the fingers of one hand, and one key or two keys in adjacent
rows or the same row on the fingers of the other hand.  Crudely I
guesstimate that this is about five thousand combinations.
