Suppose you want constant frame rate video over a bandwidth-limited
channel with very simple encoding and decoding.  Paeth’s predictor
predicts that each new pixel will be equal to one of the three pixels
N, NW, and W of it, based on an estimate of the gradient from those
three pixels, and then you encode, normally, a precise residual from
that prediction.  This approach can be straightforwardly extended to
use a three-dimensional prediction incorporating the previous frame as
well.

However, instead of transmitting a precise residual, you could
transmit a quantized approximate residual.  For example, you could
transmit a choice of 0, ±1, ±4, ±16, or ±64, which is 9 choices, 3.17
bits per pixel per color channel.  If an image holds still for a
little while, it’ll settle down to the correct image fairly quickly.

However, this still sucks, because the compression ratio is less than
a factor of 3.  You can do a little better by transforming to YUV
(16-bit maybe) and subsampling the chroma, but to do a lot better by
some such approach, you need to not transmit any bits for most pixels.

