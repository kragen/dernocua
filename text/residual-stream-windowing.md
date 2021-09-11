Suppose you want to transmit video data for a windowing system, but
you want something that’s simpler and less CPU-hungry than H.264
encoding.  Could you simply transmit a stream of lossily-encoded
residuals?

PNG doesn’t really compress image data, necessarily; what it
compresses, like a lot of lossy audio and video codecs, are the
prediction residuals from some pixel predictor (called “filters” and
defined in §6.1 of the PNG spec), an approach Paeth calls
“prediction-correction coding,” a term which has not caught on.  These
predictors are specified on a per-scanline basis:

- 0: predict 0, so the residual is the original pixel value, and we
  *are* compressing the original image data;
- 1: predict the pixel to the left, or zero if it’s the first pixel on
  the line, so the residuals are the pairwise differences between
  pixels on the line;
- 2: predict the corresponding pixel in the line above, or 0 on the
  first line, so the residuals are the pairwise differences between
  pixels in a column;
- 3: predict the average of prediction #1 and prediction #2, rounded
  down;
- 4: predict the Paeth predictor, a choice of one of the three pixels
  above, to the left, and above and to the left, depending on a simple
  linear calculation on those three pixels that estimates the local
  gradient.  This is a slight variation on the predictor Paeth
  published in “Image File Compression Made Easy”, chapter 9 of
  _Graphics Gems II_; he calls the gradient estimation calculation the
  “poor man’s Laplacian”.

The Paeth predictor is almost never much worse than any of the
previous four alternatives, but often it’s slightly worse, and you can
of course construct examples where it’s arbitrarily worse; you could
get a simpler graphics file format by using the Paeth predictor alone,
as Paeth does in his chapter, and it would compress only a little
worse than PNG.  In fact, for small enough images, it might compress
better, because PNG specifies the predictor to use at the beginning of
each scan line, which adds extra data to compress.

Now, in PNG, these residuals are compressed *losslessly*, so the
previous decompressed pixels input to the decompressor’s predictor are
exactly equal to the original image input pixels.  So the benefit for
PNG is primarily that things like continuous gradients become
repeating patterns.

A potentially much more exciting application is the residual-coding
approach used for lossy video encoding, where instead of compressing
the exact residual sequence, we compress a crude, low-bandwidth
approximation of the residual sequence.  This means that the
decompressor’s predictor is working from pixels corrupted by the
approximation noise, so to get the system to work optimally, we need
to include the lossy-encoding step inside the feedback loop of the
compressor’s predictor, so that the “context pixels” it’s predicting
from are the same corrupted pixels the decompressor will see, rather
than the original image pixels.  This ensures that the errors will not
accumulate nonlinearly.

In the context of encoding a video stream, particularly of a windowing
system, it would be useful to use the previous frame, or *a* previous
frame, as context as well.  If a screen region is unchanged from the
previous frame, the predictor will predict its contents perfectly, so
if there was no error in the previous frame, all the residuals will be
zeroes, which will compress very well.  If it’s unchanged from the
previous frame, but the previous frame was corrupted by lossy
compression, then the residuals that are transmitted will reduce the
error.

You could conceivably have 9 neighboring pixels in the previous frame
and 4 neighboring pixels in the current frame to use as a
“neighborhood” for your prediction.  (Normal video codecs also use
motion compensation, but continuous motion is less common in GUIs
(though modern GUIs use it a bit more).)  You could use those 13
values to compute a least-squares approximation of the
four-dimensional gradient and average, or just 7 of them (like Paeth’s
3), or you could use any four of them (the symmetrical choice would be
the corresponding pixels in the previous row, column, and frame, and
the diagonal pixel in the previous frame, but that doesn't give you
any information about whether pixels are changing frame to frame).
Moreover, you could very reasonably use a measure of the neighborhood
diversity to choose whether to do Paeth’s trick of choosing one of
them or to use the gradient extrapolation in the continuous domain.

Once you have your prediction, you need to code your residual lossily.
I think doing this in YUV space is probably perceptually desirable,
because it allows you to trade off more Y bits against less UV bits.
In many frames, you could use literally zero UV bits for many of the
pixels, as long as you eventually send some UV bits for them so that
they will converge to the correct color.