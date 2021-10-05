I hacked together a Python script to analyze the syllabic structure
and pronunciation of Spanish text at the phoneme level, which it seems
to get about 97% right, about one error every 30 words.  It thinks
each syllable consists of a (possibly empty) onset, a (nearly always
empty) liquid, a vowel nucleus (which may be a diphthong), and a
(usually empty) coda.

Here’s some example output, containing asterisks where it failed:

> divide.^[173]​ /di-bi-de/ Los /los/ detalles /de-ta-ʃes/ del /del/
  ciclo /si-klo/ celular /se-lu-laɾ/ solo /so-lo/ han /an/ sido
  /si-do/ investigados /in-bes-ti-ga-dos/ en /en/ el /el/ género
  /xe-ne-ɾo/ Sulfolobus, /sul-fo-lo-bus/ siendo /sien-do/ similares
  /si-mi-la-ɾes/ a /a/ los /los/ de /de/ bacterias /bak-te-ɾias/ y /i/
  eucariontes: /e-u-ka-ɾion-tes/ los /los/ cromosomas /kɾo-mo-so-mas/
  se /se/ replican /re-pli-kan/ desde /des-de/ múltiples /mul-ti-ples/
  puntos /pun-tos/ de /de/ partida /paɾ-ti-da/ (origen /o-ɾi-xen/ de
  /de/ replicación) /re-pli-ka-sion/ usando /u-san-do/ ADN /ad-\*/
  polimerasas /po-li-me-ɾa-sas/ que /ke/ son /son/ similares
  /si-mi-la-ɾes/ a /a/ las /las/ enzimas /en-si-mas/ equivalentes
  /e-ki-ba-len-tes/ eucarióticas.^[174]​ /e-u-ka-ɾio-ti-kas/ Sin /sin/
  embargo, /em-baɾ-go/ las /las/ proteínas /pɾo-tei-nas/ que /ke/
  dirigen /di-ɾi-xen/ la /la/ división /di-bi-sion/ celular,
  /se-lu-laɾ/ como /ko-mo/ la /la/ proteína /pɾo-tei-na/ FtsZ
  /\*-\*-\*-\*/

It’s using mostly IPA, except for č (“ch”) and ñ.  You can see it
screwing up on a couple of words.

Based on this sort of analysis, it produces the following statistics,
which I think are probably in the right ballpark, although it doesn’t
recognize “ai” or “ui” as valid diphthongs, and the significant
figures are mostly noise:

      onsets:  : 19.17%  t: 11.42%  d:  9.20%  s:  8.86%  k:  8.68%  l:  7.93%
              n:  6.30%  m:  6.02%  p:  5.56%  b:  4.21%  ɾ:  4.18%  f:  2.35%
              g:  2.03%  x:  1.64%  r:  1.14%  č:  0.69%  ʃ:  0.48%  ñ:  0.14%
     liquids:  : 94.46%  ɾ:  4.26%  l:  1.28% 
      nuclei: e: 28.16%  a: 26.47%  o: 19.84%  i: 12.79%  u:  5.91% io:  2.16%
             ia:  1.86% ie:  1.29% ue:  0.80% ua:  0.49% ei:  0.19% uo:  0.05%
       codas:  : 62.14%  s: 15.65%  n: 10.11%  ɾ:  5.72%  l:  2.40%  m:  1.51%
              k:  1.32% ks:  0.47%  d:  0.20%  p:  0.20% ns:  0.13%  g:  0.08%
              b:  0.05% 
      phones: e: 13.14%  a: 12.44%  s: 10.84%  o:  9.52%  i:  7.90%  n:  7.14%
              ɾ:  6.11%  l:  5.01%  t:  4.93%  k:  4.52%  d:  4.06%  m:  3.25%
              u:  3.13%  p:  2.49%  b:  1.84%  f:  1.01%  g:  0.91%  x:  0.71%
              r:  0.49%  č:  0.30%  ʃ:  0.21%  ñ:  0.06% 

This doesn’t capture all the structure of Spanish syllables; for
example, only some onsets can be followed by liquids.  But it is at
least suggestive that the syllable structure is potentially
exploitable for both encoding and human input methods (as,
undoubtedly, stenographers already do.)  The most common nucleus is
/e/, followed closely by /a/, which between them capture the majority
of syllables.  The majority of syllables start with a vowel (19% empty
onset) or either /t/, /d/, /s/, or /k/ (usually spelled “c” or “qu”),
nearly all syllables lack a liquid following the onset, and the
majority of codas are empty.  So a syllable containing only “e” is
5.01 bits, one containing only “a” is 5.12 bits, the syllable “te” is
5.75 bits, and “tes” (as in *eucariontes* or *equivalentes*) is 7.74
bits.  By contrast, a memoryless code represents “e” as 2.93 bits,
more efficiently, but “tes” as 10.5 bits, because “t” almost never
occurs at the end of a syllable, and “s” is much more common in the
coda.

(Actually, my program doesn’t allow it to, so it can’t parse
“habitat”, but it only very rarely encounters such a word.)

“bes” is 9.16 bits analyzed as a syllable, or 11.90 bits as three
separate letters.  “ti” is 6.87 bits as a syllable or 8.00 bits as two
separate letters.  “ga” is 8.31 bits as a syllable or 9.79 bits as two
separate letters.  So I guess often you could save about 20% of the
effort that way.

However, the sort of long tail of diphthongs and multi-consonant codas
is crushing my hopes for a human-written “relative positional”
notation in which the same symbol is used for consonants in some
places and vowels in others, and only the order of the symbols
distinguishes between those meanings.  I feel like it would just be
too hard to learn given that all of the following occur in existing,
if archaic, words: “crue” (“crueza”), “cruen” (“cruenta”), “cue”
(“cuero”), “cuen” (“cuenta”), “que” (“que”), “quen” (“aquende”), “cu”
(“culo”), “cun” (“secundaria”), and “cuns” (“circunscribir”,
“circunstancia”).  (I’m not totally sure bout “crueza” and “cruenta”,
which I think might be three syllables.)

At the end of my program’s output it says:

    bits per phone 3.879586262782223
    bits per letter 3.586046123445401

This is 3.9 bits per phoneme (such as /ɾ/, /k/, or /e/) and 3.6 bits
per letter (such as “h” or “c”), based on independently entropy-coding
each letter.  This is about 25% smaller than just flattening the usual
Spanish alphabet, abcdefghijlmnñopqrstuvxyz, (to which we might
reluctantly add k and w) because lg 27 ≈ 4.75 bits per letter, and the
diaeresis for things like *cigüeño* and *bilingüe*; standardly we
would also add áéíóúý, but I’m ignoring that here.

A pure Hamming phonetic code might assign 3-bit codes to /e/ and /a/,
4-bit codes to [soin], 5-bit codes to [ɾltkdmu], 6-bit codes to [pb],
7-bit codes to [fgx], an 8-bit code to [r] (“rr”), 9-bit codes to č
[tʃ] “ch” and ʃ “ll”, and an 11-bit code to ñ.  This would still leave
448 11-bit codes unassigned and would use 4.32 bits per phone or 3.99
bits per letter:

    (- 2048 (+ 1 (* 4 2) (* 8 1) (* 16 3) (* 32 2) (* 64 7) (* 128 4)
                 (* 256 2)))  ; 448

    (+ (* 3 .1314) (* 3 .1244) (* 4 .1084) (* 4 .0952) (* 4 .0790) (* 4 .0714)
       (* 5 .0611) (* 6 .0501) (* 5 .0493) (* 5 .0452) (* 5 .0406) (* 5 .0325)
       (* 5 .0313) (* 6 .0249) (* 6 .0184) (* 7 .0101) (* 7 .0091) (* 7 .0071)
       (* 8 .0049) (* 9 .0030) (* 9 .0021) (* 11 .0006))  ; 4.3196

    (+ (* 1 .1314) (* 1 .1244) (* 1 .1084) (* 1 .0952) (* 1 .0790) (* 1 .0714)
       (* 1 .0611) (* 1 .0501) (* 1 .0493) (* 1 .0452) (* 1 .0406) (* 1 .0325)
       (* 1 .0313) (* 1 .0249) (* 1 .0184) (* 1 .0101) (* 1 .0091) (* 1 .0071)
       (* 1 .0049) (* 1 .0030) (* 1 .0021) (* 1 .0006))   ; 1.0001

However, whether for human interface stuff or for data compression,
there’s no reason to restrict yourself to radix 2 nowadays; IBM’s
arithmetic-encoding patents are long expired, and I’m typing this on a
100-key keyboard, though the home row and the keys above and below are
only about radix 33.  Still, it’s a good ballpark that [ea] should be
the easiest to write, followed by [soinɾltkdmu], and then [pb],
requiring about twice as much effort as [ea], then [fgxr], then “ch”
(č) requiring about three times as much effort as [ea], then finally
[ʃñ].

You might omit č entirely, just spelling it out as /tʃ/, although that
would be pretty rough on speakers of other dialects of Spanish, even
worse than lumping [z] in with [s].

If we wanted to divide this up in some sort of rational and
easy-to-learn way, we might try to express [pbfgxrčʃñ] as some kind of
modified version of [soinɾltkdmu], which could be divided up into
vowels [oiu], sonorants [lmnd], plosives [ɾtk], and the sibilant [s].
(Spanish /d/ has a fricative allophone [ð] and a plosive allophone
[d].)  There’s inevitably going to be significant tension between
fluent writing and ease of learning.
