PBKDF content addressing with keyphrase hashcash: a non-blockchain attack on Zooko’s Triangle
=============================================================================================

This note provides a cryptographically secure, moderately
decentralized way to link moderately human-memorable strings like
b8://grain-more-state-court/GenevievesDeliciousPies or
b8://lucy-cure-tommy-rinse/Francisco.H.Walz to public keys or other
data, without a blockchain or other consensus-arbitration mechanism,
at the cost of a few thousand dollars of proof-of-work for each
four-word keyphrase such as b8://grain-more-state-court/ or
b8://lucy-cure-tommy-rinse/, which creates a namespace of unlimited
size that can be securely delegated.  Brute-force attacks on the
system’s cryptographic integrity are calculated to have infeasibly
large costs under standard assumptions, while intermediaries can
efficiently verify the integrity of data they convey, preventing the
propagation of malicious or accidentally corrupted data.

I was writing file `drama-word-list.md`, and I was thinking about how
a password using a reasonable PBKDF can be a lot shorter than a secure
content hash, even one that’s only secure against second-preimage
attacks.  For example, in [“How you should set up a
full-disk-encryption passphrase on a laptop”][0], I recommended
encrypting your disk with 2¹⁶ iterations of PBKDF2 (because LUKS
doesn’t support [scrypt][11], though [apparently LUKS2 has since added
argon2i support][1]) and a 72-bit-of-entropy six-word passphrase.

[0]: http://canonical.org/~kragen/cryptsetup.html
[1]: https://news.ycombinator.com/item?id=21793705 "Comment on the orange website by loeg on 2019-12-15T01:13:26"
[11]: https://www.gwern.net/docs/www/www.tarsnap.com/3f71c4a12cedf4c287d36304ace73e2cb5173d9f.pdf "Stronger Key Derivation via Sequential Memory-Hard Functions, by Colin Percival, 02009"

This suggests the idea: can we use a PBKDF for content-addressing by
hash?

It turns out that not only can you use a PBKDF like scrypt to expand a
human-memorable password into a larger, strong hash; you can also use
a PBKDF to compress a larger, strong hash into a human-memorable
keyphrase.  This gives you a decentralized, human-*memorable*, secure
naming system, but the resulting names are generally not
human-*meaningful*.

It turns out that a hashcash-like approach to keyphrase stretching is
in some ways much better than an approach that relies only on the
cost-factor parameter of PBKDFs.

Using a PBKDF for content-addressing by hash
--------------------------------------------

You hash a massive blob of content, or maybe somebody’s public key,
using something fast like SHA-256 or BLAKE3, then run the result
through a memory-hard PBKDF like scrypt or [Argon2][2], then encode
the result with some kind of human-readable word list, like the S/Key
or Diceware word lists.  This could potentially greatly reduce the
human effort involved in using such hashes, at the expense of computer
effort.

[2]: https://github.com/P-H-C/phc-winner-argon2

Memory-hard key derivation functions are designed to increase the cost
of a brute-force attack by requiring large, fast memory.  Right now a
4 GiB RAM stick costs US$15 and is normally depreciated over 3 years,
or US$5 per year, which works out to about 160 nanodollars per second
for 4 GiB or 4.6 attodollars per bit-second.  Probably in practice the
cost of using this memory is around four times this because of the
cost of the non-RAM parts of the computer and of the electrical energy
to run it, but this conservative 4.6 attodollars per bit-second is the
estimate I’ll use below.

Suppose we assume that the crypto works according to the standard
conjectures, and we’re willing to demand that a legitimate participant
in the system employ 4 GiB of RAM for 128 seconds to verify a hash,
which is 20 microdollars for an attacker with warehouse-scale
computers stuffed full of RAM cracking hashes.  Suppose we are content
with resisting up to a quadrillion dollars’ worth of attack (many
years of current human economic productivity), a quadrillion dollars
buys you 2.2 × 10³² bit-seconds of RAM, or 4.9 × 10¹⁹ of these
128-second-4-GiB hashes.  That’s about 2⁶⁵·⁴ hashes.  So to resist a
second-preimage attack, a hash would only need 66 bits.

Therefore, 2⁷² possible human-readable hash identifiers would be
adequate to resist a quadrillion-dollar attack.  A random 72-bit
number like 3943234810267769014593 can be represented in many
different ways, including the following:

    In hex: d5c3 603f c8fd 3889 41
    In the first half of the alphabet to avoid cusswords, like Chrome: cjakmgljchceddegilkk
    In lowercase letters, ideal for a cellphone keyboard: cjdhebmuvttqrjlx
    In lowercase letters and digits: n46ukw493t154x
    In letters and digits: 1dMffgtrOWF5T
    In letters, digits, hyphen, and underscore, like YouTube: RsdwfYzZe8B1
    In printable ASCII: j4l'/~4%s6t
    In 12-bit words of 5 letters or less: todd guide port ros iron tubes
    In the S/Key word list: BEE DEAF MULL WIRE FEAT SONG MEN

I think that, of these, at least “Todd guide port ROS iron tubes” and
“bee deaf mull wire feat song men” are things that a person could
reasonably memorize, though not without effort.

If instead of a quadrillion dollars we’re willing to succumb to
single-target second-preimage attacks of a billion dollars or more, we
can drop 20 bits.  46 bits of hash instead of 66 bits: “pork bring
extra asset” or “ni death col batty”, say.

I’m assuming here that the work factor of the PBKDF in question (the
number of iterations or whatever) is fixed up front and doesn't have
to be incorporated into the human-memorized key.  But it wouldn’t have
to be; you could reserve, for example, 4 bits of the human-memorable
key for the natural logarithm of the amount of work required in
gigabyte-seconds, thus permitting adjustment of the time required to
try a single hash from 1 gigabyte-second to 3269000 gigabyte-seconds.
This involves making the phrases longer on average, but note that my
“46-bit” phrases above already have 2 bits of slack, and my 72-bit
phrases have 6 bits of slack.

In many scenarios, the document being identified by such an identifier
is necessarily public, and so is the algorithm, so that anyone can
spend 128 seconds to verify that the document produces the correct
hash.  This means that an attacker knows not only the desired
(truncated) PBKDF *output* but also the PBKDF *input*, which is the
file’s hash using BLAKE3 or SHA-256 or whatever.  If the attacker can
find a second preimage of *that* hash, they don’t need to run the
PBKDF even once — they just run the other, much faster hash function,
potentially a much larger number of times.  But the 256-bit output
size of BLAKE3 and SHA-256 is large enough to make that infeasible,
more than compensating for the enormously higher speed of these hash
functions.  (This is the same property that makes client offload
secure for password authentication.)

A useful aspect of content-addressable schemes in general is that
network intermediaries providing a storage service can authenticate
that files they cache are valid — they haven’t been corrupted either
by a malicious attacker or by, for example, cosmic rays hitting RAM.
If such authentication is infeasible or too expensive, they won’t do
it, and so a querent requesting a file by content-hash from an
intermediary is likely to get useless data that they eventually
reject.

With the scheme described above, verifying the hash costs 512
GiB-seconds of work, so we’d like the granularity of hashed files to
be fairly large.  If there are 8192 intermediaries and 524288
end-users in the world, and you do 512 GiB-seconds of work to compute
an independent phrase for a file you want to publish on that network,
instead of just getting someone else to include its hash in their own
file, in some sense you’re imposing 512×(8192+524288) GiB-seconds of
work on the rest of the world.  Maybe it would be nice if there was
some way the original publisher could shoulder a disproportionate
share of that security burden.  As it turns out, there is; see below
about leading-zeroes phrase stretching.

As explained later, having a large number of files identified by
keyphrases in this way would make the system more vulnerable to
brute-force attacks, so it is desirable to use the human-memorable
hash for only the root of some kind of large Merkle DAG.  It might
contain, for example, a public key for everyone in your city, or the
entire corpus of Project Gutenberg or Wikipedia.  This property gives
the protocol a flavor more anarcho-syndicalist than individualist.

(Of course, the hashes connecting the nodes in the Merkle DAG should
be normal, full-sized hashes of 256 bits or so, not these expensively
stretched hashes.)

If the hashed data is some kind of efficiently traversable namespace,
it can assign human-memorable names to other particular blobs,
including public keys, IP addresses, and other identifiers.  So
instead of identifying someone as b8://ni-death-col-batty/ we identify
them as b8://ni-death-col-batty/paul-hannigan, then Paul can share the
cost of setting up ni-death-col-batty with everyone else in that
namespace.

If the hashed data is a public key, the retrieve-by-content-hash
storage network can be supplemented by a retrieve-by-public-key-hash
storage network, which distributes streams of blobs that have been
signed by a given private key.  In this way, such stable, unchanging
keyphrases can securely identify a time-varying data resource.

To some extent this reintroduces the potential problem that
decentralized naming systems are supposed to guard against:
participants in ni-death-col-batty may disagree about which “Paul
Hannigan” should get the right to determine the binding of
b8://ni-death-col-batty/paul-hannigan.  Wherever there is community
property, there is conflict.  But it’s not as bad as in, for example,
the DNS, where if ICANN is persecuting Paul, no domain name for him
will remain stable for long.

Hashcash-like leading-zeroes phrase stretching
----------------------------------------------

I think there *is* a way to get the original publisher to shoulder a
disproportionate share of the security burden, with an approach
similar to Hashcash or Bitcoin’s proof-of-work function.  Suppose
that, to *create* a valid phrase, you have to do not *one* PBKDF
verification, but a probabilistically large number of them, say,
8192 — possibly in parallel, so this need not necessarily add latency,
just cost.  This can be done by only accepting as valid PBKDF outputs
that begin with, say, 13 zero bits.  As with Hashcash and Bitcoin, you
can do this by varying a nonce that you include in the hashed data,
thus producing 8192 different PBKDF outputs.  If one of them begins
with a leader of 13 zero bits, you take its last, say, 48 bits, and
encode them as above as a phrase; any with a 1 bit in its first 13
bits are rejected.

The procedure for verifying a file that purportedly matches a
keyphrase such as “thorn foyer debut arson” is to hash the file with
your fast file-hashing algorithm such as BLAKE3, run your PBKDF such
as Argon2 on the hash for 512 GiB-seconds, and then verify that the
leading 13 bits are 0 and the trailing 48 bits encode to “thorn foyer
debut arson”.  This costs the verifier only 512 GiB-seconds (0.002¢),
but costs the original publisher 4096 GiB-seconds (0.016¢), and
increases the cost of finding a second preimage by brute force by that
same factor of 8192 (to 2⁶¹ runs of the PBKDF, 2⁷⁰ GiB-seconds, 2¹⁰⁰
byte-seconds, which works out to US$47 trillion), without lengthening
the human-memorable phrase.

That’s probably far too easy, though.  Maybe a more reasonable
phrase-stretching difficulty factor would be a week on this old 16-GiB
laptop: 2²³ GiB seconds = 2⁵³ byte-seconds (33¢).  We could reduce the
verification effort to, say, 8 GiB seconds (0.32 microdollars), so
we’d need 2²⁰ tries to produce a valid phrase: 20 leading zeroes in
the PBKDF output.  If we keep using 48-bit phrases like “spade will of
force”, then a brute-force second-preimage attack would take on
average 2⁶⁷ PBKDF invocations, each costing 8 GiB seconds, which is
also 2¹⁰⁰ byte-seconds as in the example above.

A larger hashcash-like difficulty factor might be desirable, both to
reduce the number of trusted keyphrases floating around out there by
incentivizing people to band together a bit more (thus reducing the
number of targets for a shotgun bruteforce attack, as explained
below), and also to shorten the keyphrases.  For example, if we
reduced the keyphrase to 36 bits of entropy (“grips halt seed”, “spelt
spear pose”, “thank graph ready”) and increased the difficulty by
another 13 bits (8192×, to 2³⁶ GiB seconds, 2⁶⁶ byte seconds), then
publishing a file would cost US$2700, while a brute-force
second-preimage attack would cost 2³⁶ times as much: US$190 trillion.
US$2700 of computation would be a significant incentive to pay someone
else to include your key in their file rather than publish your own
file, but it’s still low enough to ensure dissidents could establish a
memorable identity.

Such a small keyspace of course implies that unless the total number
of keyphrases ever created is small compared to 2¹⁸ = 262144, there
are likely to be collisions; this suggests that perhaps three words is
too optimistic, since that’s only US$700 million (of legitimate users
creating keyphrases) at current prices.  If it costs US$2700 to create
a four-word keyphrase, then the 2²⁴ or so that would make a collision
likely would amount to an investment of US$45 billion from the
system’s legitimate users.  The fourth word would raise the cost of a
brute-force second-preimage attack to the cost of creating 2⁴⁸
keyphrases: US$760 quadrillion.

(2³⁶ GiB seconds would be 2³² seconds for this laptop, roughly 136
years.  Or 136 such laptops could do it in a year.)

Leading-zeroes phrase stretching *instead of* a PBKDF cost factor
-----------------------------------------------------------------

Is there any reason to use *both* a PBKDF *and* a phrase-stretching
leading zero count?  Well, it's desirable to use a memory-hard PBKDF
like scrypt or Argon2 to make the attack memory-hard instead of only
CPU-hard, thus preventing vulnerability to future ASICs like Deep
Crack.

But, suppose that, while still doing 2⁵³ byte-seconds of work to
compute the keyphrase, we reduce the PBKDF work factor to, say, 10
milliseconds on this laptop, so that converting a file hash to the
PBKDF hash from which the phrase is extracted takes only 10
milliseconds (0.16 GiB-seconds) instead of 500 milliseconds, as in my
example above.  To compensate, we increase the difficulty from 20 bits
to 26 bits: instead of an average of 2²⁰ nonces, my laptop will have
to try 2²⁶ nonces before hitting on one with the requisite pattern of
26 leading zeroes in the output from its PBKDF (Argon2 or whatever).

That makes things easier for users and intermediary nodes, because
it’s 50 times easier to verify that a file matches a keyphrase; does
it make things any easier for attackers?

Well, attackers also have to try 2²⁶ nonces for every one that is a
valid keyphrase, and, as before, they will have to compute on average
2⁴⁸ such keyphrases before they finally find a second preimage.  So
the situation for the attacker has not improved at all: they still
have to do the same amount of work, it’s just that it’s divided into
50 times or 64 times as many separate nonces.

Weaknesses
----------

### Attacking many hashes at once ###

If there are many unsalted hashes, the attacker might attack them all
simultaneously.  For example, if there are 2⁴⁰ public keys in use,
each retrievable by its own keyphrase, or 2⁴⁰ documents, and the
attacker wins if they succeed in counterfeiting any one of them, their
attack speeds up by a factor of 2⁴⁰.  And salting is not really a
solution, since the salt would have to be part of the human-memorized
authenticator; it’s equivalent to just using more hash bits.

I think the best defense for this is to have relatively few
human-memorable keyphrases, each identifying a large namespace, as
explained above, by increasing the cost to create each keyphrase.

Consider the parameters suggested above: the difficulty is set to
US$2700 to create each passphrase, and 48 bits of keyphrase are used,
for a cost of US$760 quadrillion to find a particular second preimage.
If there are 1000 known keyphrases and an attacker would be content to
find any of them, then the cost plummets to US$760 trillion; if a
million keyphrases exist, then it totally collapses to only US$760
billion, which is still more than a casual attacker will spend.  As
noted above, though, soon after that point, at only around 2²⁴
keyphrases created, accidental collisions begin to occur, at which
point the cost of an intentional shotgun attack is still US$45
billion.

So, with those parameters, there’s still a reasonable degree of attack
resistance up to the limit of the system being able to function at
all.

### Collision attacks ###

The birthday paradox pops up in another context as well.

In some circumstances, second-preimage attacks are not the only
attack; birthday-paradox collision attacks have been demonstrated in
practice against TLS, for example, where an attacker generates two
certificate signing requests: one for their legitimate domain, and one
for the domain they want to spoof, which hash to the same hash.  The
certifying authority signs the legitimate one, but the CA signature
enables them to masquerade as the other domain.

Resisting such collision attacks would require twice as many bits, and
would thus double the length of the passphrase, so this scheme should
probably not be used to defend against a second-preimage attack.
Alternatively, you could use keyphrases of 6–12 words instead of 3–6.

### Quantum attacks ###

As I understand it, Grover’s algorithm can find a second preimage in
the same O(√N) time required to find a birthday attack, so if quantum
computers scale up, this system would require keyphrases of 6–12 words
instead of 3–6.

Although Merkle graphs are in general relatively postquantum-safe if
the hashes are big enough, any public-key cryptosystems used with this
system would need to be postquantum-safe for the system as a whole to
resist quantum computation attacks.

### Parameter downgrade attacks ###

If the difficulty is encoded in a keyphrase — as in my above example
with encoding the PBKDF cost parameter in 4 of its bits, or just by
virtue of its length — attackers who want to mount collision attacks
could use intentionally weak keyphrases.  This is not a concern for
second-preimage attacks, but it’s a concern anytime producing two
colliding files would be a concern.

Possible extensions inspired by time-lock encryption
----------------------------------------------------

[Someone, maybe Gwern,][6] proposed a one time-lock encryption
protocol that I will inaccurately summarize as follows.  The speaker
computes 1024 random encryption keys for a symmetric cryptosystem and
computes 1024 truncated versions by, for example, zeroing the last 20
bits of each key.  Then, in parallel, they encrypt each truncated key
with the non-truncated version of the previous key (except for the
first truncated key, which has no previous key).  They concatenate the
unencrypted first truncated key with the 1023 encrypted keys, followed
by a payload, encrypted with the last key; this is what they publish.

[6]: https://www.gwern.net/Self-decrypting-files#chained-hashes

This takes them 1024× the work of encrypting a single key, but since
they do it in parallel on 1024 processors, it doesn’t add latency.

To decrypt the payload, the recipient must try (on average) 2¹⁹
possible completions for the first key in order to decrypt the second
key, 2¹⁹ possible completions for the second key in order to decrypt
the third key, and so on.  We assume they can distinguish a correct
decryption from a decryption attempt with the wrong key.  In the end
they have done 2²⁹ decryption attempts and can finally decrypt the
payload; if they have 2¹⁹ processors they can do this in only 1024
times the time to perform a single decryption.  Unless they have
enough processors to search the whole keyspace, this is necessarily a
serial process: they cannot do it faster because they don’t know the
*N* - 20 bits of the second key until they have finished guessing the
first key, etc.

(Of course 1024 can be expanded to a larger number such as 1048576,
and you can use a deliberately slow cryptosystem such as a quadrillion
rounds of AES-ECB with the same key, or a quadrillion rounds of
SHA-256 on a “key” to derive a key that’s used for AES-ECB.)

It would be nice to somehow apply this idea in reverse to the hashcash
problem: we would like attackers to have to work serially to create a
second-preimage key, but listeners and possibly legitimate publishers
to somehow be able to do whatever processing they need to do in
parallel.  If there’s a way to do this, it might add another 10–30
effective bits to the keyphrase.

Gwern also mentions [Gregory Maxwell’s suggestion, possibly
anticipated by Ke et al.,][7] to do something analogous with ECC
cryptography.  In many ECC systems, including Curve25519, public keys
are in an almost 1-1 correspondence with bitstrings of a certain
length, so you can generate a random bitstring that is a valid public
key and encrypt something to it.  If someone takes the time to
bruteforce the private key — not feasible for Curve25519, but of
course feasible for elliptic curves over small enough Galois
fields — they can then read the message.

Maxwell suggested a Bitcoin-like blockchain in which miners compete to
publish the next private key for a predetermined infinite sequence of
random bitstrings taken as public keys; this provides an incentive
structure that makes it likely for a predetermined sequence of certain
private keys to be published at certain times in the future, and the
only way to get all the keys needed to unlock something sooner than
the miners do is to have more ECDLP computrons than they do.

This is vaguely similar to the chained-symmetric-keys approach.  Could
it be applied to this namespace-claiming problem, maybe not using a
predetermined infinite sequence?

[7]: https://www.gwern.net/Self-decrypting-files#pooling-key-cracking

Generically I think the answer is that the publisher needs to publish
some kind of noninteractive, easily verifiable zero-knowledge proof
that demonstrates that they know something “about” that keyphrase that
is computationally difficult to discover.  They start with some secret
information, which they never reveal, from which the keyphrase is
derived, and which is used to sign the file the keyphrase names.
There’s an obvious approach that doesn’t work: you generate a private
key, compute the public key from it, append a signature and the public
key to the file, append a nonce, hash it, and if the result isn’t a
valid passphrase try a new nonce, for 150 CPU-years.  This doesn’t
work because a different public key would work just as well, so it
doesn’t make a second-preimage attack any harder.
