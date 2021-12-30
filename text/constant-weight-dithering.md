Suppose you want to encode some digital data in a one-bit-deep
(black-and-white, no grey) image, but you want the image to also
depict something; to make this simpler, let’s say that what it depicts
is independent of the data encoded.  One way to do this is with M-of-N
or constant-weight codes.

Consider a 2×2-pixel area of this image; there are 16 possible
patterns: one all black, four three black and one white, six two black
and two white, four three white and one black, and one all white.
This gives you five possible levels of brightness for this 2×2-pixel
area, but three of these levels have multiple possible ways to achieve
them.  With conventional dithering, you use the choice among them to
improve the high-frequency reproduction of the image — the precise
locations of edges and things like that.

Suppose, instead, that you dither the image down to a 5-level
grayscale image, then replace each pixel of the 5-level grayscale with
one of these 2×2 blocks, with the appropriate brightness.  You can use
a 1-of-4 code, a 2-of-4 code, or a 3-of-4 code (the complement of the
1-of-4 code) within these blocks to encode arbitrary data.  The 2-of-4
code gives you lg 6 = 2.58 bits per block, while the other two give
you 2 bits per block.  If the image’s contrast is destretched enough
to put essentially all of the dithered 5-level pixels within that
range of grays, you might get about 2.2 bits per 4-pixel block, which
is 0.55 bits per pixel.  That is, a slight majority of the data in the
final image is devoted to encoding your chosen data.  (By histogram
equalization you can arrange to distribute the image brightness across
the available levels in almost any conceivable nontrivial way,
though possibly at the cost of beauty or comprehensibility.)

If instead of 2×2 blocks we use 3×3 blocks, then instead of 1 4 6 4 1
possibilities at the different gray levels, we have 1 9 36 84 126 136
84 36 9 1, allowing us to encode respectively 0, 3.17, 5.17, 6.39,
6.98, 6.98, 6.39, 5.17, 3.17, and 0 bits, averaging 4.34 bits per
9-pixel block; if we exclude the ends, it’s 5.43 bits, or 0.60 bits
per pixel, 10% better than the 2×2 case with less compromise of the
contrast.  With a little more compromise on contrast, you can probably
push that past 6 bits per 9×9, 0.67 bits per pixel.  The tradeoff, of
course, is that you’ve lost more than half of the spatial resolution
previously devoted to encoding the carrier image, in the sense that
you’re encoding less than half as many 9-level grayscale pixels as you
were 5-level grayscale pixels.

This can be straightforwardly extended to the case of non-monochrome
images.  Instead of 2 possibilities per pixel, you might have 4 (RGB),
5 (CMYK), 8 (superposable RGB), 16 (superposable CMYK), or more, so
each of the constant-weight codes you’re using to encode the data is
no longer a *binary* constant-weight code, and the reduced-palette
image you’re encoding from is no longer grayscale.

In most practical uses of this method, you would need error correction
coding.

It’s possible that this method is already covertly in use for printer
tracking dots, with the justification being the prevention of
counterfeiting paper money.  Other possible uses include:

- Provenance information, such as EXIF data, in a photograph, which
  ought to only be done by the voluntary choice of the photographer;
- A machine-readable circuit model in a circuit schematic;
- A machine-readable version of a program in a printed program
  listing;
- Including a machine-readable version of a program in the program’s
  *output*;
- For example, including the equations and parameters used to generate
  a fractal image in the rendered fractal;
- Steganographic communication between people seeking privacy;
- Including a machine-readable data table in a data plot;
- Privacy-invading watermarking uses similar to the tracking-dots
  approach mentioned above, allowing the producer of many versions of
  an image to track down the first step of path by which a particular
  image made it to a particular recipient;
- Watermarks claiming credit or copyright, like [the easter egg in
  Commodore PET Basic Version 2 which would display “MICROSOFT!” when
  you typed “WAIT6502,1”][0] or [the Stolen From Apple logo in the
  Macintosh firmware following the Franklin Ace lawsuit][1].

[0]: https://www.pagetable.com/?p=43
[1]: https://www.folklore.org/StoryView.py?story=Stolen_From_Apple.txt
