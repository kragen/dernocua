As I wrote in <https://news.ycombinator.com/item?id=26525837> residue
number systems with many small bases are not well suited to day-to-day
human use; they’re more confusing than systems with a smaller number
of bases.  So, for example, the Maya tzolk’in residue number system
calendar uses bases 13 and 20, necessitating at least 20 digits
(though in fact the Maya used different digits for the two cycles, one
being an ordinary numeral and the other being the name of one of 20
natural phenomena).  Small bases also tend to vary a lot from digit to
digit; in that post I suggested using bases 5, 6, 8, 9, and 11, but
that means that you need at least 11 digits, but can only use 5 of
them in the fastest-cycling digit, wasting more than a whole bit of
encoding space.

The conventional way to solve this problem is to use another number
system for the individual digits.  For example, the 13 day numbers of
the Maya were 𝋡 𝋢 𝋣 𝋤 𝋥 𝋦 𝋧 𝋨 𝋩 𝋪 𝋫 𝋬 𝋭, which are written in base 5
(and 1-origin — Dijkstra would not approve), and the Babylonians used
up to 14 cuneiform strokes to form their sexagesimal digits: up to
five “ten” strokes, and up to nine “one” strokes.  And Wilhelm Fliess
wrote his cocaine-fueled biorhythm numbers, counting days modulo 23
and 28, pairs of Western Arabic digits, as do modern biorhythm
scammers, adding a 33-day cycle.  So day 10000 of a person’s life
might be represented as 18(P), 4(E), 1(I), because 10000 % 23 = 18,
10000 % 28 = 4, and 10000 % 33 = 1, although it’s more common for
biorhythm scammers to just plot some sine waves.

Applying the RNS principle recursively
--------------------------------------

This is a fascinating alternative.  For example, suppose we have 16₁₀
digits, like the corners of a tesseract, or conventional sexadecimal
symbols.  With two of them we can represent a number mod 240₁₀ with
its moduli relative to 15₁₀ and to 16₁₀:

    00 11 22 33 44 55 66 77 88 99 aa bb cc dd ee
    f0 01 12 23 34 45 56 67 78 89 9a ab bc cd de
    e0 f1 02 13 24 35 46 57 68 79 8a 9b ac bd ce
    d0 e1 f2 03 14 25 36 47 58 69 7a 8b 9c ad be
    c0 d1 e2 f3 04 15 26 37 48 59 6a 7b 8c 9d ae 
    b0 c1 d2 e3 f4 05 16 27 38 49 5a 6b 7c 8d 9e
    a0 b1 c2 d3 e4 f5 06 17 28 39 4a 5b 6c 7d 8e
    90 a1 b2 c3 d4 e5 f6 07 18 29 3a 4b 5c 6d 7e 
    80 91 a2 b3 c4 d5 e6 f7 08 19 2a 3b 4c 5d 6e
    70 81 92 a3 b4 c5 d6 e7 f8 09 1a 2b 3c 4d 5e
    60 71 82 93 a4 b5 c6 d7 e8 f9 0a 1b 2c 3d 4e
    50 61 72 83 94 a5 b6 c7 d8 e9 fa 0b 1c 2d 3e
    40 51 62 73 84 95 a6 b7 c8 d9 ea fb 0c 1d 2e
    30 41 52 63 74 85 96 a7 b8 c9 da eb fc 0d 1e
    20 31 42 53 64 75 86 97 a8 b9 ca db ec fd 0e
    10 21 32 43 54 65 76 87 98 a9 ba cb dc ed fe

Now we apply the recursive step, bottom up.  An additional such pair
can represent the number mod 239: 00 00, 11 11, 22 22, ... dc dc, ed
ed, fe 00, 00 11, 11 22, ... ed dc, fe ed, 00 00.  This lets us
represent 57’360₁₀ numbers in four digits.  A second recursive step
represents a number in this way directly and also modulo 57’359₁₀, so
that following ed dc ed dc, we have not fe ed fe ed but fe ed 00 00.
This can represent numbers up to 3’290’112’240₁₀ in eight digits: 31.6
bits of information, only 1.2% less than a binary place-value
notation.

Extension to multiple precision
-------------------------------

It also has a straightforward rule for abbreviating small numbers: to
extend a small positive number to a longer version, the longer version
of the number just has more copies of the same number, in a way
analogous to zero-extending or sign-extending in conventional
place-value systems.  So 3 can be validly represented, for example, as
33, 33 33, or 33 33 33 33, and a4 is the same as a4 a4 or a4 a4 a4 a4.
In the notation used in the above counts, I am extending numbers to
the right rather than, as is conventional, on the left, but the
extension algorithm is the same either way.

Sign testing is straightforward and efficient
---------------------------------------------

The rule to determine the *sign* of a number, which is an enormous
problem with residue number systems in general, is easy but not
totally trivial.  You subtract the two halves of the number from one
another and use the sign of the result.  So, for example, ed dc is
negative, because dc - ed = fe, which is negative because e - f = f,
which is negative because I said so.  You can choose where to put the
window where positive numbers wrap around to negative, but as long as
you have at least *some* negative numbers this approach will give you
the right subtraction sign if you do the arithmetic with sufficient
precision.

I’m not sure how to do ordinary arithmetic though!
--------------------------------------------------

I thought the usual digit-by-digit methods of residue number systems
would apply in a trivial way here because of the simple recursive
construction, but they don’t.  05 a8 5a fd multiplied by a4 3e a4 3e,
for example, is 05 15 c2 ca: 320’000₁₀ × 6154₁₀ = 1’969’280’000₁₀.
For the first two digits we can just multiply corresponding digits:
0·a = 0, 5·4 = 5 (mod 15₁₀).  But to compute that a8·3e (218₁₀·179₁₀)
should give us ‘15’ (mod 239; 65₁₀), we cannot just multiply a·3 mod
16₁₀ and 8·e mod 15₁₀, which would give us e7, the wildly different
number 142₁₀.  That’s because 218₁₀·179₁₀ = 39’022₁₀, which is
163₁₀·239₁₀ + 65₁₀ or 162₁₀·240₁₀ + 142₁₀.

To put it another way, a8 a8 · 3e 3e = e7 15.  But how do we calculate
that “15”?  It happens that 15 - e7 = 65₁₀ - 142₁₀ (+ 239) = 162₁₀,
because each lap around the racetrack, the mod-239₁₀ number gained one
on the mod-240₁₀.  So if we could somehow calculate that it took 162₁₀
= 2c laps to get to e7, we could add those differences back in and get
the right answer: 2c + e7 = 15, where the first digits add mod 16₁₀
and the second digits add mod 15₁₀.

But how on Earth do you calculate that within the RNS without falling
into an infinite regress of four-digit multiplications?

For *addition*, I think the problem may be easier.  Let’s divide
positive from negative numbers as equally as possible, rather than
taking advantage of the window-choosing freedom I described above.
Then, if we add two numbers of the same sign and get a number of the
opposite sign, I think we can conclude that we’ve lapped around the
racetrack, going one way or the other — but only once.
