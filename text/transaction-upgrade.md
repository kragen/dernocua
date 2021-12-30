The serialization problem
-------------------------

Data serialization is generally interwoven with questions of schema
upgrade.  The conception of a data type changes over time as the
software changes; a field that at one time is an 8-bit unsigned
integer may become a 16-bit signed integer later, then perhaps a
floating-point number.  A floating-point number may become a rational,
or vice versa.  An attribute that is at one point required and scalar
may at another point become optional, multivalued, or time-dependent.
Unencrypted passwords may be replaced by incompetently hashed MD5
passwords, which are replaced by scrypt output or the output of
whatever displaces scrypt, or possibly an SRP authenticator or a set
of authorized public keys.  ASCII strings may become UTF-8 strings, or
strings in some other encoding which is specified by another
previously nonexistent field.  Uncompressed or RLE-compressed image
data may be replaced or supplemented with JPEG data.  A text column
may be supplemented by a full-text index.  A plain string for a
phone-number field may be replaced or supplemented by a foreign key
into the CRM database where we store our phone numbers.

If you write a piece of data to a disk file or send it across a
network or a pipe to another process, the software that reads the data
may not be the same version that writes it.  If the software is
long-lived and thus modified many times, it is inevitable that it will
sometimes be a different version, even if the development history is
linear, which it may not be.

When the software that reads the data is *newer* than the version that
wrote it, for example after an upgrade, it can include code to handle
the older version of the data, though that code is usually poorly
tested and buggy.  But when it’s *older*, there is no such
possibility.  This situation arises when communicating across a
heterogeneous network or when downgrading software.

XXX
