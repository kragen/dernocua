USB adds a 0 bit after 6 (or 5?) consecutive 1s.  Does this create a
timing channel attack?  Is there a two-out-of-5-code-like approach
that avoids this?

A timing-channel attack would occur when some kind of private data is
being transmitted in cleartext over the channel, such as a password or
an encryption key, and an attacker can observe the *length* or
*timing* of the transmission but not its content.  It would be
especially helpful to the attacker if they could somehow send data
that was concatenated with, or especially interspersed with, the
bitstuffed data, repeatedly, because that would allow them to
determine that a particular bit was a 1 by inserting several 1s before
it.  Although this sounds far-fetched, several vulnerabilities of this
sort have been found in SSL and TLS.  Still, USB seems likely to be
less vulnerable.

Many other line protocols instead use constant-overhead encodings like
8b/10b encoding to ensure adequate state changes and line balance at a
modest efficiency cost.  This approach is guaranteed to not create a
timing-channel vulnerability in this way.  FC, DVI, HDMI, DisplayPort,
FireWire, SATA, and USB3 all use 8b/10b.