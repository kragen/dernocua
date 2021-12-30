I composed some lists of words for maximum vividness of random imagery
in minimal letters, then wrote shell scripts to generate random
combinations of them, vaguely like *ars magna Lulli*.

This is potentially useful for encoding passwords or secure content
hashes, or naming novel concepts in a terse way that collides with
minimal existing terminology; “ehate” or “godfat” may not be a good
choice, but “medry” or “linhag” might be okay, especially if you work
a digit in there somewhere.  “Linhag” is just an encoding of the
random number 322442 in base 661, but I’m probably not alone in having
an easier time attaching a novel meaning to “linhag” than to “322442”.
Plus, it’s easier to type.

This is a potentially serious pareidolia hazard for anyone who has
taken a lot of psychedelics or just has natural psychotic tendencies.
Readers in these categories should abstain from reading this in order
to avoid delusions that this document contains secret messages from
God, extraterrestrials, transdimensional machine elves, or the CIA.
Selecting short words uniformly with a PRNG can’t compete for
pareidolia with ELIZA or GPT-2, but it's definitely good enough to
evoke vivid mental imagery.

*Try-hat oat-egg lin-hag apt-zen hip-ale sag-pry if-egg way-ho out-neo
poo-bud ask-emo tip-poo neo-fry flu-cis bye-kev dog-pug cab-try
sun-len cod-foe ex-won wye-dad ash-art or-par lit-oaf min-met lad-tab
fop-dub ack-hit elf-run keg-ha few-pun nor-git!*

3-letter words
--------------

Here’s a list of 661 of the 4031 three-letter words that occurred 5
times or more in the British National Corpus.  I’ve tried to remove
non-words, abbreviations and acronyms not usually pronounced
(including “mrs”), and things that aren’t in most native English
speakers’ vocabularies, as well as the most offensive words, like
“fag”, “wog”, “nig”, and “gyp”.  However, there are still lots of
things in there that might offend someone, including but not limited
to “god”, “ass”, “tit”, “vag”, “goy”, “rim”, “gag”, “fat”, “fop”,
“pus”, “gay”, and “fap”.  I’ve left in many proper nouns
(unfortunately not capitalized, due to the source) as well as some
morphemes that are especially productive in modern English, like
“neo”, “eco”, and “tri”.

This is not suitable as a word-game list for ruling words in or out.
The words do not all have distinct pronunciations, so it is not a good
alternative to the various “biometric word lists” out there like the
S/Key word list.

Selecting one word from this list with uniform probability encodes
9.37 bits of entropy; if we follow it with a space, that’s 4 bytes,
and thus 2.34 bits per character.

Example three-word sequences:

    $ for i in $(seq 10); do echo $(shuf -n 3 3-letter-words | awk '{print $2}'); done
    key hem sun
    fly tag tom
    wad bay dow
    emo ned boo
    vie fen kev
    tri fen ben
    jug mat mid
    ben sag ill
    pan sim tit
    bic doh one

Not all of thes are hits, but it’s presumably easy to imagine Emo Ned
booing, Ben of three swamps, a jug in the middle of a mat, or a pan
that simulates a breast.

Pairs of these words usually form a pronounceable nonexistent English
word:

    $ echo $(for i in $(seq 10); do echo $(shuf -n 2 3-letter-words | 
        awk '{print $2}') | tr -d ' '; done)
    gagkim godfat kinoff yenflu cadice forvex gunark tonroc legten negeco

Here’s the list:

    6187927 the
    2682878 and
    923975 was
    836687 for
    695595 you
    470949 are
    462777 not
    455906 but
    445396 had
    433599 his
    380284 she
    327014 her
    262447 all
    259443 has
    236364 one
    236165 can
    206627 who
    165016 him
    163106 its
    156114 two
    151629 out
    143429 did
    137814 now
    128513 may
    125206 new
    124108 any
    118641 see
    101517 how
    99506 get
    96280 way
    95006 our
    81601 got
    71143 own
    70169 too
    67862 say
    60680 day
    60612 yes
    60358 man
    59364 use
    55001 put
    54610 old
    50877 why
    48851 off
    48189 end
    38892 men
    38769 set
    33752 yet
    30379 six
    27882 war
    27873 car
    26734 saw
    25918 let
    25486 far
    25346 law
    24712 big
    22944 act
    22803 job
    21803 age
    21377 run
    20935 try
    20419 pay
    20274 ten
    19810 ago
    19401 ask
    19161 few
    19047 air
    18885 god
    18820 sir
    18483 lot
    15873 bed
    15695 tax
    15087 top
    14816 art
    14792 cut
    14247 bad
    13539 per
    13290 boy
    12985 bit
    12857 son
    12776 sea
    12766 red
    12470 nor
    12394 low
    12329 buy
    10950 sat
    10817 met
    10520 cup
    10243 oil
    9930 led
    9690 lay
    9552 eye
    9166 arm
    9157 win
    8859 hot
    8766 sun
    8742 ran
    8710 box
    8703 sit
    8619 tea
    8497 won
    8316 sex
    8238 add
    8165 aid
    8063 dog
    7939 key
    7882 mum
    7750 bar
    7549 eat
    7328 gas
    7169 hit
    6846 dad
    6623 dry
    6499 fit
    6101 aim
    6040 due
    5463 die
    5343 leg
    5299 bus
    5166 aye
    5063 tom
    4984 sky
    4909 bag
    4762 net
    4647 via
    4630 row
    4610 lie
    4567 ooh
    4482 odd
    4481 bob
    4341 sum
    4337 joe
    4323 jim
    4242 van
    4009 guy
    3933 ref
    3862 cat
    3839 ice
    3821 pub
    3783 map
    3686 lee
    3491 gun
    3443 sad
    3422 bid
    3401 tim
    3335 gap
    3270 fly
    3228 wet
    3163 ken
    3150 mad
    3150 ben
    3137 hat
    3131 sam
    3106 bay
    2990 pop
    2987 cry
    2876 ear
    2837 fee
    2781 joy
    2770 wan
    2745 fun
    2717 ban
    2678 bet
    2616 rid
    2583 aha
    2582 ill
    2509 egg
    2472 raw
    2425 san
    2395 tie
    2391 sue
    2390 fat
    2382 vat
    2239 mix
    2222 tip
    2155 era
    2120 pen
    2020 pot
    2011 tin
    1985 ray
    1950 ann
    1921 mud
    1895 lad
    1884 pat
    1864 gay
    1806 cap
    1784 roy
    1767 fox
    1765 bye
    1760 ira
    1759 hey
    1756 ate
    1720 pan
    1717 don
    1716 les
    1688 kid
    1686 liz
    1684 tap
    1648 fed
    1646 fig
    1535 pit
    1511 kit
    1480 rob
    1466 lit
    1445 yer
    1430 fan
    1425 cab
    1420 jan
    1410 eve
    1392 inn
    1375 max
    1369 lip
    1369 ham
    1355 ali
    1352 fix
    1320 sin
    1317 yep
    1314 oak
    1305 ace
    1303 bow
    1298 jet
    1269 kim
    1264 owe
    1257 cow
    1255 lap
    1204 rod
    1188 log
    1175 shy
    1172 dot
    1159 pie
    1155 fry
    1143 ted
    1123 pig
    1119 pin
    1112 ash
    1087 lid
    1083 wee
    1057 von
    1032 hut
    1010 lea
    1000 dig
    989 owl
    976 jaw
    974 dan
    959 bat
    950 dos
    947 par
    942 rat
    941 dug
    939 non
    928 fog
    914 ron
    896 leo
    895 ego
    872 fur
    869 meg
    858 rex
    856 hay
    847 wit
    835 pet
    821 gut
    809 kin
    808 dim
    795 del
    781 beg
    780 jam
    771 arc
    748 bin
    738 nil
    734 vic
    729 fax
    723 ski
    721 ram
    714 mug
    706 hip
    699 nod
    695 pro
    694 hid
    687 spy
    682 min
    681 axe
    679 amp
    671 icy
    666 rug
    651 zoo
    651 mac
    650 thy
    649 ink
    646 nut
    644 dee
    640 rub
    639 opt
    630 vet
    628 pad
    628 apt
    626 lou
    614 rev
    608 eva
    605 dip
    601 jar
    600 toe
    588 web
    585 mob
    585 ale
    578 cox
    576 ads
    570 flu
    569 wax
    566 gig
    564 toy
    553 lab
    552 wed
    551 jug
    551 huh
    549 peg
    546 dam
    545 rim
    543 gel
    542 pal
    528 tag
    528 ivy
    527 yen
    526 sly
    523 bee
    521 mid
    521 mat
    521 amy
    518 rio
    510 spa
    510 awe
    506 tug
    503 gin
    502 fen
    501 pam
    493 rot
    492 tee
    486 den
    482 ton
    478 wow
    472 mam
    466 len
    464 ore
    459 nan
    455 kay
    455 con
    453 val
    451 cot
    450 ion
    449 rig
    449 doo
    446 hen
    445 nun
    443 wry
    443 ant
    435 loo
    434 rag
    423 sod
    422 hop
    419 jew
    404 sid
    404 cue
    402 sic
    394 tan
    389 sub
    386 rue
    383 rum
    383 jon
    382 cod
    377 bum
    376 dye
    375 sec
    375 gum
    375 cop
    374 cam
    371 rib
    367 jed
    367 bud
    367 abu
    365 zen
    365 rip
    364 gym
    363 tow
    359 duo
    348 sip
    347 rye
    343 hal
    339 mod
    336 bra
    332 jay
    331 kev
    327 hum
    325 doe
    325 doc
    324 mao
    323 ono
    320 hug
    317 zip
    315 wig
    310 mel
    308 hon
    306 woo
    297 zoe
    297 rap
    297 fin
    295 bug
    295 ass
    293 nay
    293 bog
    291 tub
    289 cis
    283 hem
    278 lag
    278 foe
    278 dup
    270 ebb
    262 dun
    261 mop
    260 sow
    258 nip
    258 bun
    257 chi
    254 hub
    248 rep
    247 gem
    245 wes
    245 lyn
    242 pip
    242 gee
    242 dew
    239 tab
    233 ned
    230 fir
    226 nah
    224 wye
    222 aah
    221 din
    220 sob
    220 lib
    219 boo
    217 ark
    214 vow
    214 roe
    209 sap
    209 ida
    205 tit
    205 hue
    205 elf
    205 coy
    205 ape
    204 ugh
    203 yew
    202 hun
    200 tar
    200 sew
    193 elm
    191 jen
    190 pod
    190 git
    187 cal
    186 nos
    185 vax
    181 alf
    179 ada
    178 paw
    178 cad
    176 pre
    173 lax
    172 oft
    172 dis
    169 pup
    167 ole
    167 koi
    166 nap
    165 pic
    164 pep
    163 jog
    163 emu
    160 pea
    154 sib
    154 lob
    153 eel
    151 pol
    149 tor
    149 rem
    146 gag
    145 lac
    144 jot
    142 lin
    140 eco
    139 hob
    138 sac
    138 pew
    135 wad
    135 orc
    135 aft
    132 pee
    132 ewe
    130 mom
    128 vie
    127 dab
    127 cob
    124 yum
    124 tot
    123 pun
    122 hog
    121 viv
    121 orb
    121 dub
    120 tho
    120 app
    118 jab
    116 gal
    116 cub
    115 cum
    114 ado
    111 yea
    109 jig
    108 sag
    108 imp
    108 ere
    106 ply
    105 yon
    104 urn
    104 mag
    104 hee
    103 fro
    102 pap
    101 soy
    100 dow
    99 gus
    99 bey
    98 sis
    98 fad
    96 rut
    95 nag
    95 hag
    94 pus
    94 alt
    93 woe
    93 doh
    90 pow
    90 fay
    89 dev
    86 ops
    85 wag
    82 pry
    82 pox
    81 yuk
    81 bib
    80 tat
    80 ode
    79 ilk
    78 abe
    75 hah
    71 zia
    71 sax
    71 hoe
    70 lam
    70 kip
    70 keg
    69 lei
    66 goo
    65 oar
    65 mic
    64 sci
    64 fab
    62 mow
    61 sim
    60 poo
    59 arf
    58 jib
    58 bop
    58 alp
    57 tic
    57 ire
    56 nab
    56 gob
    56 cog
    54 cud
    51 maw
    50 tad
    50 jag
    49 ohm
    48 aba
    46 ail
    45 boa
    45 biz
    44 lex
    44 fob
    43 yow
    43 rad
    43 mah
    42 wok
    42 sop
    42 roc
    42 phi
    42 lug
    42 ent
    41 awl
    38 dud
    38 caw
    38 bro
    37 pug
    34 zap
    33 bio
    33 bic
    32 fez
    31 yaw
    31 nib
    30 yak
    30 jut
    29 fop
    28 lux
    27 bah
    26 zed
    26 oaf
    26 moo
    25 tau
    24 tri
    24 gab
    24 fib
    23 ska
    23 hex
    21 zig
    21 elk
    20 mew
    20 het
    20 geo
    19 fap
    18 oat
    18 neo
    17 nix
    17 hew
    17 fam
    17 erg
    15 uzi
    15 foo
    14 yap
    13 tox
    13 org
    13 lye
    12 yup
    12 vex
    12 naw
    12 fie
    12 fem
    12 boi
    11 vag
    11 lol
    11 emo
    9 kia
    9 bub
    8 tux
    8 roo
    8 hod
    8 hep
    6 goy
    6 gnu
    6 ack
    5 zit
    5 neg
    5 glo

2-letter words
--------------

Of the 577 two-letter words with 5 or more occurrences, I selected 46;
a uniform selection encodes 5.52 bits, and so, in three bytes, 1.84
bits per byte.  This is slightly lower entropy density than the
three-letter list; concatenating them produces a tiny increase in
entropy density, and breaks up monospace monotony a lot, but the more
useful use for this list is for when you really want a six-byte or
five-letter phrase instead of a six-letter or seven-byte phrase, and
14.9 bits of entropy is enough.

Some randomly generated phrases:

    $ for i in $(seq 10); do
        echo $((shuf -n 1 2-letter-words; shuf -n 1 3-letter-words) | awk '{print $2}')
    done
    me dry
    ad rim
    eh ate
    am val
    ha paw
    us pew
    go for
    or war
    me sob
    on gay
    $ for i in $(seq 10); do
        echo $((shuf -n 2-letter-words; shuf -n 2 3-letter-words) | awk '{print $2}')
    done
    my cat sum
    of phi ilk
    we zip pay
    ax zoo bun
    am dow yer
    ax zen few
    it met map
    if led roy
    be aah ray
    do why lin
    $ for i in $(seq 10); do
        echo $(cat 2-letter-words 3-letter-words | shuf -n 3 | awk '{print $2}')
    done
    new bow pig
    yak jig dos
    zed koi joe
    oil or sir
    imp am far
    din wes san
    cod ken cal
    pi mao mow
    ah me hal
    fad lyn of
    $ for i in $(seq 50); do echo $(cat 2-letter-words 3-letter-words | shuf -n 2 
        | awk '{print $2}') | tr -d ' '; done | fmt
    wadmad nawfem ayeeel saddog leehop butail deldoc devgit bussag titpry
    bitgit skitau bebus putwin owpup hisbiz irakin hadoc tryan yukugh jibaah
    leetho jugpea yerhis yakpeg actaid feewed zoomod incox rexfib dohyak
    niltry toothe ranrot dandup uziram toymat lowow ahaam beelie dinent
    awemet gutbop suedie poomoo dunspa oarlaw dubyea inktom lidrob
    $ for i in $(seq 32); do echo $(cat 2-letter-words 3-letter-words | shuf -n 2
        | awk '{print $2}') | tr ' ' '-'; done | fmt
    try-hat oat-egg lin-hag apt-zen hip-ale sag-pry if-egg way-ho out-neo
    poo-bud ask-emo tip-poo neo-fry flu-cis bye-kev dog-pug cab-try sun-len
    cod-foe ex-won wye-dad ash-art or-par lit-oaf min-met lad-tab fop-dub
    ack-hit elf-run keg-ha few-pun nor-git

This is the list:

    2941790 of
    2544858 to
    1849882 in
    1089559 it
    998867 is
    697406 on
    681379 he
    664780 be
    507370 by
    478178 at
    406705 as
    370855 or
    358792 we
    344046 an
    280701 do
    237107 if
    212158 so
    209943 no
    156837 up
    152626 my
    139028 me
    90161 go
    78198 us
    68437 oh
    26872 am
    10091 ah
    4721 un
    4436 co
    3618 ha
    3492 eh
    2860 ok
    2005 ad
    1700 ye
    1490 di
    1043 ho
    1026 hi
    834 ex
    615 pi
    476 vs
    420 id
    304 ow
    192 ox
    173 mu
    65 ax
    60 om
    20 ew

This is probably a somewhat suboptimal tradeoff for passwords and hashes
------------------------------------------------------------------------

A better tradeoff for the password or content-hash cases is probably
to use the 2048 most common English words of five letters or less,
which can encode 24 bits of randomness in two words, rather than only
18.7; with my wordlist, for example, 7362508 is “bent ash”, 609933 is
“why stud”, and 11152019 is “ropes cia”.  A 48-bit password, which is
reasonably strong for many purposes if combined with a good PBKDF,
might be “karen sped ah cell”, which I think is a little more
memorable than “gas jug bad bye hee” or “yon sic ow boi mop”, which
are about the same strength.
