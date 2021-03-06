I want to learn Rust, so I’m reading the Rust book by Steve Klabnik,
Carol Nichols, et al., and I’m going to try writing an IRC bot in it.
I’ve done a few basic Rust tutorials in previous years, and I had a
Rust compiler installed in /usr/local/bin, but it’s from 02016.

_The Rust Programming Language_ book is very approachable,
but it’s a bit slow-paced and
patronizing.  Maybe it would be great if I were extremely insecure
about my abilities.  [The _Rust Reference_][13] is maybe closer to what
I want, but [the 57-page _Rust for the Polyglot Programmer_][14] is a
night-and-day improvement over either as a starting point.  For
example, after only 23 pages, it tells me, “There is no inheritance,”,
and on the next page, “this is how `for x in y` loops work: `y` must
`impl IntoIterator`”. These are things I’ve been wondering about
through hundreds of pages of TRPL.  However, it is very much not
self-contained, so it is only a starting point.

[13]: https://doc.rust-lang.org/stable/reference/
[14]: https://diziet.dreamwidth.org/10210.html

Installing Rust was kind of a pain in the ass and needed 294–1190 MB
--------------------------------------------------------------------

First, I got rustup:

    curl https://sh.rustup.rs > rustup.sh

Rustup insisted I uninstall the five-years-ago Rust, so I did:

    sudo /usr/local/lib/rustlib/uninstall.sh

Then I tried installing rust, but because I “only” had half a gig
free, it failed:

    $ sh rustup.sh
    info: downloading installer
    Warning: Not enforcing strong cipher suites for TLS, this is potentially less secure
    Warning: Not enforcing TLS v1.2, this is potentially less secure

    Welcome to Rust!

    This will download and install the official compiler for the Rust
    programming language, and its package manager, Cargo.

    Rustup metadata and toolchains will be installed into the Rustup
    home directory, located at:

      /home/user/.rustup
    ...
    1) Proceed with installation (default)
    2) Customize installation
    3) Cancel installation
    >1

    info: profile set to 'default'
    ...
    info: installing component 'rust-docs'
     10.2 MiB /  17.0 MiB ( 60 %)   7.3 MiB/s in  1s ETA:  0s
    info: rolling back changes
    error: failed to extract package (perhaps you ran out of disk space?): No space left on device (os error 28)
    $ df -h .
    Filesystem               Size  Used Avail Use% Mounted on
    /dev/mapper/debian-root  225G  214G  517M 100% /

At this point I had deleted my previous Rust installation with no way
to get it back, but wasn’t able to install the current Rust.

I was spending 3.2 gigs on the linux-2.6 Git repo that I hadn’t
updated since 02014, so I deleted that.  Even if half a fucking
gigabyte isn’t enough space for a fucking compiler, 3.7 gigs should
be.  That’s four times the size of my first Linux box.

This time I tried the “minimal” profile instead, too.  And it “only”
needed 294 megs:

      stable-x86_64-unknown-linux-gnu installed - rustc 1.55.0 (c8dfcfe04 2021-09-06)


    Rust is installed now. Great!

    To get started you may need to restart your current shell.
    This would reload your PATH environment variable to include
    Cargo's bin directory ($HOME/.cargo/bin).

    To configure your current shell, run:
    source $HOME/.cargo/env

Before:

    $ df -k .
    Filesystem              1K-blocks      Used Available Use% Mounted on
    /dev/mapper/debian-root 235891480 220134444   3774396  99% /

After:

    $ df -k .
    Filesystem              1K-blocks      Used Available Use% Mounted on
    /dev/mapper/debian-root 235891480 220427872   3480968  99% /

Hmm, maybe I’ll try a fatter profile then:

    warning: Updating existing toolchain, profile choice will be ignored

Hmm, maybe not?  I can’t find the uninstall script this time (it turns
out the command is `rustup self uninstall` as explained on p. 13 of
the book, which I hadn’t gotten to yet) so I’ll just delete it by
hand:

    $ rm -rf ~/.rustup ~/.cargo
    $ df -k .
    Filesystem              1K-blocks      Used Available Use% Mounted on
    /dev/mapper/debian-root 235891480 220014156   3894684  99% /
    $ sh rustup.sh
    ...
    info: profile set to 'complete'
    info: setting default host triple to x86_64-unknown-linux-gnu
    info: syncing channel updates for 'stable-x86_64-unknown-linux-gnu'
    info: latest update on 2021-09-09, rust version 1.55.0 (c8dfcfe04 2021-09-06)
    warning: Force-skipping unavailable component 'miri-x86_64-unknown-linux-gnu'
    warning: Force-skipping unavailable component 'rust-analyzer-preview-x86_64-unknown-linux-gnu'
    ...
      stable-x86_64-unknown-linux-gnu installed - rustc 1.55.0 (c8dfcfe04 2021-09-06)
    ...
    Rust is installed now. Great!
    ...
    $ df -k .
    Filesystem              1K-blocks      Used Available Use% Mounted on
    /dev/mapper/debian-root 235891480 221200928   2707912  99% /

So this time it’s using 1.19 gigs because I set the profile to
`complete`.

### hello, world ###

But now it’s working:

    : user@debian:~/devel/dev3; . ~/.cargo/env 
    : user@debian:~/devel/dev3; cat hello.rs 
    fn main() {
        println!("hello, {}", "world");
    }
    : user@debian:~/devel/dev3; rustc hello.rs 
    : user@debian:~/devel/dev3; ./hello
    hello, world

#### Hello World is Fucking Huge ####

> Smaller runtimes have fewer features but have the advantage of
> resulting in smaller binaries. Smaller binaries make it easier to
> combine the language with other languages in more contexts. While
> many languages are okay with increasing the runtime in exchange for
> more features, Rust needs to have nearly no runtime, and cannot
> compromise on being able to call into C in order to maintain
> performance.

— *The Rust Programming Language*, §4.1 “Using threads to run code
simultaneously”, p. 423

    : user@debian:~/devel/dev3; ls -l hello
    -rwxr-xr-x 1 user user 3439804 Oct  6 22:50 hello

That’s a completely unreasonable size, roughly two and a half floppy
disks for “hello, world”, between three and five orders of magnitude
larger than is needed, but it does run.  And compiling it takes about
250 milliseconds; again, three to five orders of magnitude slower than
compiling a three-line program ought to be, but tolerable.

This is mostly (>90%) debug info.  Unfortunately, the remainder is
still almost 300K, between two and four orders of magnitude too big:

    : user@debian:~/devel/dev3; ls -l hello
    -rwxr-xr-x 1 user user 3439804 Oct  7 23:00 hello
    : user@debian:~/devel/dev3; strip hello
    : user@debian:~/devel/dev3; ls -l hello
    -rwxr-xr-x 1 user user 297312 Oct  7 23:01 hello

Different optimization levels unsurprisingly don’t make much difference:

    : user@debian:~/devel/dev3; rustc -C opt-level=s hello.rs
    : user@debian:~/devel/dev3; ls -l hello
    -rwxr-xr-x 1 user user 3438548 Oct  7 23:03 hello
    : user@debian:~/devel/dev3; rustc -C opt-level=z hello.rs
    : user@debian:~/devel/dev3; ls -l hello
    -rwxr-xr-x 1 user user 3438615 Oct  7 23:04 hello
    : user@debian:~/devel/dev3; rustc -C opt-level=3 hello.rs
    : user@debian:~/devel/dev3; ls -l hello
    -rwxr-xr-x 1 user user 3438552 Oct  7 23:04 hello
    : user@debian:~/devel/dev3; strip hello
    : user@debian:~/devel/dev3; size hello
       text	   data	    bss	    dec	    hex	filename
     281780	  11288	    576	 293644	  47b0c	hello

Apparently [I’d have to not use the prebuilt libstd to fix this, which
requires nightly Rust][1], but that still leaves a 51-kilobyte
executable, or use `#![no_std]` to not use libstd at all.
[Dynamically linking libstd *by default* isn’t an option because Rust
doesn’t have an ABI][2], but [you *can* dynamically link with `-C
prefer-dynamic`][4], which gives you a 10-kilobyte stripped binary
which by default doesn’t work because it doesn’t know where to find
Rust’s libstd:

    : user@debian:~/devel/dev3; rustc -C prefer-dynamic hello.rs
    : user@debian:~/devel/dev3; strip hello
    : user@debian:~/devel/dev3; ls -l hello
    -rwxr-xr-x 1 user user 10456 Oct  7 23:26 hello
    : user@debian:~/devel/dev3; ldd hello
            linux-vdso.so.1 =>  (0x00007fff26df3000)
            libstd-008055cc7d873802.so => not found
            libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f05ead14000)
            libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f05ea987000)
            /lib64/ld-linux-x86-64.so.2 (0x00007f05eb12d000)
    : user@debian:~/devel/dev3; ./hello
    ./hello: error while loading shared libraries: libstd-008055cc7d873802.so: cannot open shared object file: No such file or directory
    : user@debian:~/devel/dev3; LD_LIBRARY_PATH=/home/user/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/lib ./hello
    hello, world

That seems pretty reasonable.

[1]: https://github.com/johnthagen/min-sized-rust#optimize-libstd-with-build-std
[2]: https://news.ycombinator.com/item?id=23498254
[4]: https://news.ycombinator.com/item?id=16736725

There are, however, some other reasons that Rust compilation output is bloated:

    0000000000003b00 <_ZN4core3ptr9const_ptr33_$LT$impl$u20$$BP$const$u20$T$GT$4cast17h2979c04ce50f48ccE>:
        3b00:       48 89 f8                mov    %rdi,%rax
        3b03:       c3                      retq
        3b04:       90                      nop
        3b05:       90                      nop
        3b06:       90                      nop
        3b07:       90                      nop
        3b08:       90                      nop
        3b09:       90                      nop
        3b0a:       90                      nop
        3b0b:       90                      nop
        3b0c:       90                      nop
        3b0d:       90                      nop
        3b0e:       90                      nop
        3b0f:       90                      nop

### Holy shit, thirty thousand HTML files? ###

For some reason the `rustup doc` command just opens some kind of Wine
error dialog telling me how to install Wine.  But it looks like the
docs are here:

    : user@debian:~/devel/dev3; find /home/user/.rustup/ -name '*.html' | random 5000
    /home/user/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/share/doc/rust/html/core/arch/x86_64/fn._pdep_u32.html
    /home/user/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/share/doc/rust/html/core/arch/x86_64/fn._mm512_mask_reduce_add_pd.html
    /home/user/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/share/doc/rust/html/core/arch/aarch64/fn.vaddv_s32.html
    /home/user/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/share/doc/rust/html/core/arch/aarch64/fn.vaddl_s32.html
    /home/user/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/share/doc/rust/html/core/arch/aarch64/fn.vmlsl_u32.html
    /home/user/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/share/doc/rust/html/core/core_arch/arm_shared/neon/generated/fn.vqrdmlahq_laneq_s32.html
    /home/user/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/share/doc/rust/html/core/core_arch/x86/avx512vbmi2/fn._mm512_mask_compress_epi16.html
    : user@debian:~/devel/dev3; find /home/user/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/share/doc/rust/html/ | wc
      30223   30223 3819176

Thirty.  Thousand.  Files.  *Of documentation alone*.  Evidently, it’s
mostly one file per assembly-language instruction on any of the
supported architectures.  What have I done?

    : user@debian:~/devel/dev3; find ~/.rustup ~/.cargo | wc
      31994   31994 4029266

Oh, I guess that’s not so bad, then.

    : user@debian:~/devel/dev3; firefox /home/user/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/share/doc/rust/html/index.html 

Well, that works.  Nice comprehensive and polished documentation, too,
looks like.

### My very first crate ###

Let’s try making a crate.  I don’t want to proliferate Git repos,
because then I can forget to check things in or push them, so I’m
using my standard hellbox repo:

    : user@debian:~/devel/dev3; cargo new --vcs none hello_cargo
         Created binary (application) `hello_cargo` package

(The Rust book says to use `--bin` but `cargo new --help` says that’s
the default.)

    : user@debian:~/devel/dev3; cd hello_cargo/
    : user@debian:~/devel/dev3/hello_cargo; cat > hello.rs
    fn main() {
            println!("hello, world");
    }
    : user@debian:~/devel/dev3/hello_cargo; ls
    Cargo.toml  hello.rs  src
    : user@debian:~/devel/dev3/hello_cargo; mv hello.rs src/.
    : user@debian:~/devel/dev3/hello_cargo; mv src/hello.rs src/main.rs
    : user@debian:~/devel/dev3/hello_cargo; cat Cargo.toml 
    [package]
    name = "hello_cargo"
    version = "0.1.0"
    edition = "2018"

    # See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

    [dependencies]
    : user@debian:~/devel/dev3/hello_cargo; cargo build
       Compiling hello_cargo v0.1.0 (/home/user/devel/dev3/hello_cargo)
        Finished dev [unoptimized + debuginfo] target(s) in 0.72s
    : user@debian:~/devel/dev3/hello_cargo; ls
    Cargo.lock  Cargo.toml  src  target
    : user@debian:~/devel/dev3/hello_cargo; find target/
    target/
    target/.rustc_info.json
    target/debug
    target/debug/.fingerprint
    target/debug/.fingerprint/hello_cargo-cb8f156fc8def340
    target/debug/.fingerprint/hello_cargo-cb8f156fc8def340/bin-hello_cargo
    target/debug/.fingerprint/hello_cargo-cb8f156fc8def340/invoked.timestamp
    target/debug/.fingerprint/hello_cargo-cb8f156fc8def340/bin-hello_cargo.json
    target/debug/.fingerprint/hello_cargo-cb8f156fc8def340/dep-bin-hello_cargo
    target/debug/incremental
    target/debug/incremental/hello_cargo-3fhio3llrdrxv
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w.lock
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/3n8baekyl6jfd1zt.o
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/dep-graph.bin
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/5893w20ken98e8mr.o
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/15pcyh12hnx9h9yu.o
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/work-products.bin
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/2zukcvf9271rij44.o
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/3jf4rvldk0nwopmj.o
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/query-cache.bin
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/3vvwo10tkawer2dj.o
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/497974iq30wb32q0.o
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/2pe66p99jtgk2gt2.o
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/4moexls4ruzzyfmb.o
    target/debug/incremental/hello_cargo-3fhio3llrdrxv/s-g31wqj1itv-18kv17w-3u24lffwq59u4/56vc5hmppbu1ww1q.o
    target/debug/build
    target/debug/.cargo-lock
    target/debug/hello_cargo.d
    target/debug/deps
    target/debug/deps/hello_cargo-cb8f156fc8def340
    target/debug/deps/hello_cargo-cb8f156fc8def340.d
    target/debug/examples
    target/debug/hello_cargo
    target/CACHEDIR.TAG
    : user@debian:~/devel/dev3/hello_cargo; ./target/debug/hello_cargo 
    hello, world

Hmm, seems okay.  A bit voluminous, I guess, but that’s a small price
to pay if it speeds up builds and/or makes them more reliable.

Because I said `--vcs none` it didn’t create a .gitignore, so I do:

    : user@debian:~/devel/dev3/hello_cargo; echo target > .gitignore

Then I can add it to git, which I do, and then I can clone:

    : user@debian:~/devel/dev3/hello_cargo; cd ../..
    : user@debian:~/devel; time git clone dev3 dev3.copy
    ...
    real	0m2.890s
    ...
    : user@debian:~/devel; cd dev3.copy
    : user@debian:~/devel/dev3.copy; cd hello_cargo/
    : user@debian:~/devel/dev3.copy/hello_cargo; cargo build
       Compiling hello_cargo v0.1.0 (/home/user/devel/dev3.copy/hello_cargo)
        Finished dev [unoptimized + debuginfo] target(s) in 0.72s
    : user@debian:~/devel/dev3.copy/hello_cargo; ./target/debug/
    build/        deps/         examples/     .fingerprint/ hello_cargo   incremental/  
    : user@debian:~/devel/dev3.copy/hello_cargo; ./target/debug/hello_cargo 
    hello, world

Good enough.  And it’s nice that it records the versions of
dependencies I’m building with in `Cargo.lock` by default.

There’s a `cargo run`:

    : user@debian:~/devel/dev3/hello_cargo; cargo run
        Finished dev [unoptimized + debuginfo] target(s) in 0.00s
         Running `target/debug/hello_cargo`
    hello, world
    : user@debian:~/devel/dev3/hello_cargo; rm -rf target
    : user@debian:~/devel/dev3/hello_cargo; cargo run
       Compiling hello_cargo v0.1.0 (/home/user/devel/dev3/hello_cargo)
        Finished dev [unoptimized + debuginfo] target(s) in 0.71s
         Running `target/debug/hello_cargo`
    hello, world

Oof, 710 ms to build a three-line program.  Four lines of code
compiled per second.  This is *not* going to be fun.  Oddly, the
release build happens faster, so possibly that was just a measurement
error:

    : user@debian:~/devel/dev3/hello_cargo; cargo run --release
       Compiling hello_cargo v0.1.0 (/home/user/devel/dev3/hello_cargo)
        Finished release [optimized] target(s) in 0.30s
         Running `target/release/hello_cargo`
    hello, world

Cross-compiling depends on the C toolchain (and other things)
-------------------------------------------------------------

It seems like the Rust compiler I installed includes every Rust
backend known to history or myth:

    : user@debian:~/devel/dev3; rustc --print target-list| wc
        166     166    4022
    : user@debian:~/devel/dev3; rustc --print target-list| random 32
    mips64-unknown-linux-muslabi64
    mipsisa64r6el-unknown-linux-gnuabi64
    powerpc64-wrs-vxworks
    x86_64-unknown-illumos

But because the binaries link with libc, you need to have a GCC or
similar toolchain installed for the target platform:

    : user@debian:~/devel/dev3; rustc --target s390x-unknown-linux-gnu hello.rs
    error[E0463]: can't find crate for `std`
      |
      = note: the `s390x-unknown-linux-gnu` target may not be installed
      = help: consider downloading the target with `rustup target add s390x-unknown-linux-gnu`

    error: aborting due to previous error

    For more information about this error, try `rustc --explain E0463`.
    : user@debian:~/devel/dev3; rustup target add s390x-unknown-linux-gnu
    info: downloading component 'rust-std' for 's390x-unknown-linux-gnu'
    info: installing component 'rust-std' for 's390x-unknown-linux-gnu'
     22.9 MiB /  22.9 MiB (100 %)  11.2 MiB/s in  1s ETA:  0s
    : user@debian:~/devel/dev3; rustc --target s390x-unknown-linux-gnu hello.rs
    error: linking with `cc` failed: exit status: 1
      |
      = note: "cc" "hello.hello.996e1e6f-cgu.0.rcgu.o" "hello.hello.996e1e6f-
    ...
    e.rlib" "-Wl,-Bdynamic" "-lgcc_s" "-lutil" "-lrt" "-lpthread" "-lm" "-ldl" "
    -lc" "-Wl,--eh-frame-hdr" "-Wl,-znoexecstack" "-L" "/home/user/.rustup/toolc
    hains/stable-x86_64-unknown-linux-gnu/lib/rustlib/s390x-unknown-linux-gnu/li
    b" "-o" "hello" "-Wl,--gc-sections" "-pie" "-Wl,-zrelro" "-Wl,-znow" "-nodef
    aultlibs"
      = note: /usr/bin/ld: hello.hello.996e1e6f-cgu.0.rcgu.o: Relocations in generic ELF (EM: 22)
              hello.hello.996e1e6f-cgu.0.rcgu.o: could not read symbols: File in wrong format
              collect2: error: ld returned 1 exit status


    error: aborting due to previous error

This failure left a debris of 11 `hello.*.rcgu.o` files built for the
S/390, perhaps as a debugging aid.

Among the more exciting targets included are x86_64-fuchsia,
wasm32-wasi, wasm32-unknown-emscripten, riscv32i-unknown-none-elf,
riscv64gc-unknown-linux-gnu, nvptx64-nvidia-cuda, mipsel-sony-psp,
arm-linux-androideabi, and avr-unknown-gnu-atmega328.  I actually have
the cross-compiling toolchain for the AVR, but trying to get Rust
working for it fails in an excitingly different way:

    : user@debian:~/devel/dev3; rustup target add avr-unknown-gnu-atmega328
    error: toolchain 'stable-x86_64-unknown-linux-gnu' does not contain component 'rust-std' for target 'avr-unknown-gnu-atmega328'
    note: not all platforms have the standard library pre-compiled: https://doc.rust-lang.org/nightly/rustc/platform-support.html

(Here by “excitingly” I mean “disappointingly”.)

Notes on things that surprised me about the language
----------------------------------------------------

I’d say “notes about the language” but I’m not going to attempt to
describe the whole language, except very cursorily: the atomic
(“scalar”) types are {u,i}{8,16,32,64,size}, Unicode codepoints
(“char”), f{32,64}, and boolean.  Built-in aggregate types (“compound
types” — oddly not “vector”, which is a standard library growable
array, as in the STL) are tuples, strings, arrays, structs (chapter
5), enums (ADTs, chapter 6), plus references, mutable references, and,
rarely, pointers.  Hmm, what about traits and functions?  Looks like
closure types are trait types (Fn, FnMut, FnOnce).

Some of what follows probably sounds critical and might inspire
Rustaceans to feel defensive.  I’d suggest they don’t read it, because
it’s not about Rust; it’s about me.

It’s nice to be able to use underscores in numbers.  Binary literals
(0b101) are nice.  Array literals [x, y, z] are nice.  String
formatting with `println!` (and `format!`, and even `panic!`) is nice.
Snake case is nice.  Array indexes are checked at runtime, panicking
like .expect() when out of bounds.  Type inference is nice, but
unfortunately it doesn’t extend to formal parameters or function
return types, making the subroutine mechanism a more costly form of
generalization than it would be.  Implicit return and closure syntax,
OTOH, reduce the cost of the subroutine mechanism, and it’s nice that
implicit return is just a special case of a more general `progn`
mechanism.  (Closure syntax *does* receive the benefit of type
inference.)  Unparenthesized conditions in `if` and `while` are nice.
Conditional expressions are nice, even if they do have to be made out
of blocks.  Not sure I like the `else if` special-case syntax, but I
guess it’s easy to read and remember.  `for`-`in` is nice; not sure
about the explicit `.iter()`.  The `(1..4).rev()` syntax for a `Range`
is nice.

I was thinking that maybe the cmp method from std::cmp::Ordering
implied that there was no operator overloading, but evidently that’s
not true; `std::ops::Add<T>` is the trait of things that overload `+`.
And `Vec` overloads `[]`, which is even better news for nefarious EDSL
purposes.  (Though Rust’s macro system is probably a more capable way
of doing EDSLs.)

In general the error messages are really excellent:

    : user@debian:~/devel/dev3; rustc add.rs
    error: return types are denoted using `->`
     --> add.rs:1:13
      |
    1 | fn f(i: i32): i32 {
      |             ^ help: use `->` instead

Though not always:

    thread 'main' panicked at 'index out of bounds: the len is 1
    but the index is 1', /stable-dist-rustc/build/src/libcollections/
    vec.rs:1307

That’s... not a useful error location.

This is a very groovy way to *almost* implicitly propagate an
exception:

    fn run(config: Config) -> Result<(), Box<Error>> {
        let mut f = File::open(config.filename)?;

That sneaky little byte `?` means “return the result if it’s an
error”.

I like the fact that each file forms a namespace of its own by
default.  I dislike the fact that apparently the crate name has
nothing to do with the filename.

I wonder if instead of a `&` sigil for borrowing an immutable
reference and no sigil for consumption or copying (the difference
between them being only whether the object has the `Copy` trait) the
unmarked case should be borrowing an immutable reference, while
copying and consumption each have their own sigils.  Mina suggested
that consumption should use an arrow; instead of `let s2 = s1` you
could say `let s2 ← s1` to emphasize the “movement” aspect of the
value; in other consumption contexts (arguments, returns) that
wouldn’t quite work, but `let s2 = ←s1` would.

Syntactically, I am not a fan of the paamayim nekudotayim, but I guess
it could be worse; VMS used $.

It’s interesting that library functions are private (like C file
`static`, I guess?) by default, if you don’t prefix them with `pub`.
`pub fn foo`, etc.

Recursive deref coercion for arguments surprised me.

### Unhandled results are just a warning ###

Unhandled result failures warn by default, which is nice:

    : user@debian:~/devel/dev3; rustc greet.rs
    warning: unused `Result` that must be used
     --> greet.rs:6:4
      |
    6 |    io::stdin().read_line(&mut s);
      |    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      |
      = note: `#[warn(unused_must_use)]` on by default
      = note: this `Result` may be an `Err` variant, which should be handled

    warning: 1 warning emitted

But it was only a warning:

    : user@debian:~/devel/dev3; ./greet
    hi, what is your name?
    bob
    hello, bob
    !

There’s a linter standardly installed with the compiler called
“Clippy”; I’m not sure if this is a Clippy warning or not.

### Unicode handling?  Well, shit, at least it’s not Python ###

The Rust book says:

> *Note: `std::env::args` will panic if any argument contains invalid
> Unicode.  If you need to accept arguments containing invalid
> Unicode, use `std::env::args_os` instead. That function returns
> OsString values instead of String values.  We’ve chosen to use
> `std::env::args` here for simplicity because `OsString` values
> differ per-platform and are more complex to work with than `String`
> values.*

So, on the plus side, at least command-line argument handling isn’t
*completely* broken in order to enable portability to broken operating
systems.  On the other hand, the easiest interface to command-line
argument apparently *is* broken.  I don’t understand why I should
suffer because other people use Microsoft Windows.

But hey.  At least I think my Rust programs won’t crash while
attempting to print a crash traceback because the traceback contains a
non-ASCII character, which is actually a thing that has happened to me
with Python 3.  And probably there won’t be files I can’t open in Rust
because their names aren’t UTF-8.  And I’m pretty sure my Rust
programs won’t stop compiling if I put curly quotes inside my comments,
which happened to me a lot in Python 2.

### Strings ###

The str/String distinction is a bit of a hassle.  Nice that str (and
maybe String?) has .lines() iterator and a .contains() method, and
that String (and maybe str?) can be sliced by bytes.  .to\_lowercase()
is a longish method name but not commonly enough used to merit a more
ambiguous name.

### Iterators ###

Python’s iterator design is one of its strongest points, and Rust’s
iterator design is one of *its* strongest points.  Both are external
iterators (they don’t receive a closure to evaluate on each item, so
you can build fairly general converging dataflow trees from them).
And they are very similar, consisting of only a `next()` method
(renamed `__next__()` in Python 3 for dubious reasons) that either
returns the next item or fails (with None in Rust, StopIteration in
Python) and implicitly mutates the iterator.

It’s interesting that `Vec` “is an iterator” (you can directly iterate
over it with for-in) but the book implies some built-in collections
aren’t; you need to call .iter() on them.  Though, which built-in
collections were they?  Arrays evidently *can* be directly iterated
over.  The default way of iterating over `Vec` is I think its .iter()
method; it also has `.into_iter()`, which consumes the vec, and
`.iter_mut()`, which returns an iterator of mutable references.

The `next()` method in the `Iterator` trait takes a mutable self
reference, which makes it surprising that you can usefully make an
immutable iterator reference.

Python added generators fairly soon after iterators, allowing you to
implement an iterator as a coroutine, which greatly improved the
clarity of iterator transformation.  Soon after that it added
generator expressions, which are still terser.

Python’s iterators are somewhat bug-prone because you can confuse them
with collections and attempt to use them again after they’ve already
been fully consumed, in which case they will generally appear to be
empty.  Java’s iterator design solved this by not treating iterators
themselves as iterable, at the cost of not being able to deal with
sequences like lines from an input file.  I think this bug-proneness
is less of a concern in Rust because normally anything that iterates
over an iterator will consume and drop the iterator; it won’t be
satisfied with a borrowed mutable reference.

Another bug that Rust is better at detecting than Python is creating a
lazy iterator and then never consuming it, because at least iterator
adaptors are `#[warn(unused_must_use)]`, like Err.

Because Rust has traits instead of just protocols, things like map(),
filter(), enumerate(), zip(), sum(), reduce() (called .fold()),
collect() (like Python `list()`, `dict()`, etc.),
and skip() (like APL drop I guess) are methods on the iterator trait
with default implementations, not functions in a global namespace.
This helps to reduce nesting compared to Python, though a Python genex
is still usually shorter and clearer.

Interestingly, both .collect() and .sum() have ad-hoc polymorphism on
their return type, similar to Perl’s scalar vs. list context, but
generalized.  Any type that implements the FromIterator trait can be
returned from .collect(); any type that implements Sum can be returned
from .sum() (and similarly for Product and .product()).

There is some implicit lifting into the Result and Option monads for,
e.g., .sum() and .product().

In addition to what STL calls input and output (see below!) iterators,
I think Rust iterators can be forward iterators (by implementing Copy
or Clone) and random-access iterators (with the `Step` trait).

#### Writing through iterators ####

Because Rust iterators can yield mutable references, you can use them
as cursors into data structures you’re mutating as well, like C++
forward iterators.  This is something Python iterators can’t do.  This
took me 20 minutes of struggling through compiler errors, but I did
finally get it to work:

    fn copy_iter<T: Copy>(src: &mut dyn Iterator<Item=&T>,
                          dest: &mut dyn Iterator<Item=&mut T>) {
        loop {
            match (src.next(), dest.next()) {
                (Some(s), Some(d)) => *d = s.clone(),
                (_, _) => return,
            }
        }
    }

    fn main() {
        let mut v1 = vec![3, 4, 1];
        let v2 = vec![10, 20, 100];
        let mut i = v1.iter_mut();
        i.next();

        copy_iter(&mut v2.iter(), &mut i);
        println!("Now it's {:?}", v1);      // outputs: Now it's [3, 10, 20]
    }

That, uh, doesn’t really emit reasonable code for `copy_iter`, though.
It *does* get specialized for the `i32` integers it’s being invoked
with, but, oddly enough, not for vector iteration, presumably because
of `dyn`:

    0000000000002cb0 <_ZN4iter9copy_iter17h5fd7a53461d29648E>:
        2cb0:       48 83 ec 58             sub    $0x58,%rsp
        2cb4:       48 89 7c 24 28          mov    %rdi,0x28(%rsp)
        2cb9:       48 89 74 24 30          mov    %rsi,0x30(%rsp)
        2cbe:       48 89 54 24 38          mov    %rdx,0x38(%rsp)
        2cc3:       48 89 4c 24 40          mov    %rcx,0x40(%rsp)
        2cc8:       48 8b 44 24 30          mov    0x30(%rsp),%rax
        2ccd:       48 8b 7c 24 28          mov    0x28(%rsp),%rdi
        2cd2:       ff 50 18                callq  *0x18(%rax)
        2cd5:       48 89 44 24 20          mov    %rax,0x20(%rsp)
        2cda:       48 8b 44 24 40          mov    0x40(%rsp),%rax
        2cdf:       48 8b 7c 24 38          mov    0x38(%rsp),%rdi
        2ce4:       ff 50 18                callq  *0x18(%rax)
        2ce7:       48 89 44 24 18          mov    %rax,0x18(%rsp)
        2cec:       48 8b 44 24 18          mov    0x18(%rsp),%rax
        2cf1:       48 8b 4c 24 20          mov    0x20(%rsp),%rcx
        2cf6:       48 89 4c 24 48          mov    %rcx,0x48(%rsp)
        2cfb:       48 89 44 24 50          mov    %rax,0x50(%rsp)
        2d00:       b8 01 00 00 00          mov    $0x1,%eax
        2d05:       31 c9                   xor    %ecx,%ecx
        2d07:       48 83 7c 24 48 00       cmpq   $0x0,0x48(%rsp)
        2d0d:       48 0f 44 c1             cmove  %rcx,%rax
        2d11:       48 83 f8 01             cmp    $0x1,%rax
        2d15:       75 17                   jne    2d2e <_ZN4iter9copy_iter17h5fd7a53461d29648E+0x7e>
        2d17:       b8 01 00 00 00          mov    $0x1,%eax
        2d1c:       31 c9                   xor    %ecx,%ecx
        2d1e:       48 83 7c 24 50 00       cmpq   $0x0,0x50(%rsp)
        2d24:       48 0f 44 c1             cmove  %rcx,%rax
        2d28:       48 83 f8 01             cmp    $0x1,%rax
        2d2c:       74 05                   je     2d33 <_ZN4iter9copy_iter17h5fd7a53461d29648E+0x83>
        2d2e:       48 83 c4 58             add    $0x58,%rsp
        2d32:       c3                      retq
        2d33:       48 8b 7c 24 48          mov    0x48(%rsp),%rdi
        2d38:       48 8b 44 24 50          mov    0x50(%rsp),%rax
        2d3d:       48 89 44 24 08          mov    %rax,0x8(%rsp)
        2d42:       e8 09 0e 00 00          callq  3b50 <_ZN4core5clone5impls52_$LT$impl$u20$core..clone..Clone$u20$for$u20$i32$GT$5clone17h4244c5f4dce8d8e8E>
        2d47:       89 44 24 14             mov    %eax,0x14(%rsp)
        2d4b:       48 8b 44 24 08          mov    0x8(%rsp),%rax
        2d50:       8b 4c 24 14             mov    0x14(%rsp),%ecx
        2d54:       89 08                   mov    %ecx,(%rax)
        2d56:       e9 6d ff ff ff          jmpq   2cc8 <_ZN4iter9copy_iter17h5fd7a53461d29648E+0x18>
        2d5b:       90                      nop
        2d5c:       90                      nop
        2d5d:       90                      nop
        2d5e:       90                      nop
        2d5f:       90                      nop

I mean, reading through the code, it’s not *totally* appalling, but
does this function really need an almost-90-byte stack frame?  And
what’s going on here?

        2ce7:       48 89 44 24 18          mov    %rax,0x18(%rsp)
        2cec:       48 8b 44 24 18          mov    0x18(%rsp),%rax

And this in particular is kind of an embarrassing way to compile `*d =
s.clone()` in a production compiler optimizing for size:

        2d33:       48 8b 7c 24 48          mov    0x48(%rsp),%rdi
        2d38:       48 8b 44 24 50          mov    0x50(%rsp),%rax
        2d3d:       48 89 44 24 08          mov    %rax,0x8(%rsp)
        2d42:       e8 09 0e 00 00          callq  3b50 <_ZN4core5clone5impls52_$LT$impl$u20$core..clone..Clone$u20$for$u20$i32$GT$5clone17h4244c5f4dce8d8e8E>
        2d47:       89 44 24 14             mov    %eax,0x14(%rsp)
        2d4b:       48 8b 44 24 08          mov    0x8(%rsp),%rax
        2d50:       8b 4c 24 14             mov    0x14(%rsp),%ecx
        2d54:       89 08                   mov    %ecx,(%rax)

I’d think something like this would be more reasonable:

        mov 0x48(%rsp), %rdi    # s
        callq _ZN4core5clone5impls52_$LT$impl$u20$core..clone..Clone$u20$for$u20$i32$GT$5clone17h4244c5f4dce8d8e8E #WTAF
        mov 0x50(%rsp), %rcx    # d
        mov %eax, (%rcx)        # *d = ...

That’s with `-C prefer-dynamic -C opt-level=s`.  Without the
optimization the executable is three times the size.  opt-level=3
doesn’t help but opt-level=1 is actually a little better, except that
its invocation of the `next()` method is much worse:

    00000000000013a0 <_ZN4iter9copy_iter17h5fd7a53461d29648E>:
        13a0:       41 57                   push   %r15
        13a2:       41 56                   push   %r14
        13a4:       41 54                   push   %r12
        13a6:       53                      push   %rbx
        13a7:       50                      push   %rax
        13a8:       49 89 f6                mov    %rsi,%r14
        13ab:       49 89 ff                mov    %rdi,%r15
        13ae:       66 90                   xchg   %ax,%ax
        13b0:       e8 8b ff ff ff          callq  1340 <_ZN91_$LT$core..slice..iter..Iter$LT$T$GT$$u20$as$u20$core..iter..traits..iterator..Iterator$GT$4next17h074db47cc7af8891E>
        13b5:       49 89 c4                mov    %rax,%r12
        13b8:       4c 89 f7                mov    %r14,%rdi
        13bb:       e8 b0 ff ff ff          callq  1370 <_ZN94_$LT$core..slice..iter..IterMut$LT$T$GT$$u20$as$u20$core..iter..traits..iterator..Iterator$GT$4next17h50a12d7708b22495E>
        13c0:       4d 85 e4                test   %r12,%r12
        13c3:       74 17                   je     13dc <_ZN4iter9copy_iter17h5fd7a53461d29648E+0x3c>
        13c5:       48 89 c3                mov    %rax,%rbx
        13c8:       48 85 c0                test   %rax,%rax
        13cb:       74 0f                   je     13dc <_ZN4iter9copy_iter17h5fd7a53461d29648E+0x3c>
        13cd:       4c 89 e7                mov    %r12,%rdi
        13d0:       e8 ab fd ff ff          callq  1180 <_ZN4core5clone5impls52_$LT$impl$u20$core..clone..Clone$u20$for$u20$i32$GT$5clone17hb0e95370c1e5efa8E>
        13d5:       89 03                   mov    %eax,(%rbx)
        13d7:       4c 89 ff                mov    %r15,%rdi
        13da:       eb d4                   jmp    13b0 <_ZN4iter9copy_iter17h5fd7a53461d29648E+0x10>
        13dc:       48 83 c4 08             add    $0x8,%rsp
        13e0:       5b                      pop    %rbx
        13e1:       41 5c                   pop    %r12
        13e3:       41 5e                   pop    %r14
        13e5:       41 5f                   pop    %r15
        13e7:       c3                      retq

(Maybe all those extra `mov`s disappear into register renaming in
early stages of execution, though.)

(On the plus side, compiling this 17-line program
at any optimization level takes 280–290 ms,
barely longer than the 230 ms to compile the three-line hello-world
program.  So it’s compiling... about 300 lines a second?  Probably
that’s just happenstance and the actual amount of code is a minimal
factor here.)

The explicit call to .iter() is necessary; maybe coercion to iterators
happens automatically in for-in loops for `Vec`, but not here:

    error[E0277]: `Vec<{integer}>` is not an iterator
      --> iter.rs:17:15
       |
    17 |     copy_iter(&mut v2, &mut i);
       |               ^^^^^^^ `Vec<{integer}>` is not an iterator
       |
       = help: the trait `Iterator` is not implemented for `Vec<{integer}>`
       = note: required for the cast to the object type `dyn Iterator<Item = &_>`

The body of the loop is stupid, though, because it’s explicitly
calling .clone() on a `Copy` instance; it should instead say

    match (src.next(), dest.next()) {
        (Some(s), Some(d)) => *d = *s,
        (_, _) => return,
    }

and, with this fix, the function is inlined into main() as it should
be, and fully unrolled, and I think maybe dead-store-eliminated as
well.  This also works:

    while let (Some(s), Some(d)) = (src.next(), dest.next()) {
        *d = *s;
    }

And so does this:

    for (s, d) in src.zip(dest) {
        *d = *s;
    }

FFI Callability
---------------

One of the major draws of Rust for me is interoperability: [being able
to call code from other languages][4] and [being able to call code in
other languages][3].

It’s not obvious how you invoke the Rust compiler to build a .o file
you can link with C, though.  All in all this seems like an
underdocumented aspect of Rust.

[3]: https://doc.rust-lang.org/stable/reference/items/external-blocks.html#abi
[4]: https://docs.rust-embedded.org/book/interoperability/rust-with-c.html

The following seems to work (see [SO question][8]), but involves
compiling four lines of code into a 20-megabyte library which adds 4.7
megs to the binary, and adds dependencies on libpthreads, libdl, libm,
and librt to the C code:

[8]: https://stackoverflow.com/questions/63617012/creating-and-linking-static-rust-library-and-link-to-c

    : user@debian:~/devel/dev3; cat add2.rs
    #[no_mangle]
    pub extern "C" fn add(a: i32, b: i32) -> i32 {
        a + b
    }
    : user@debian:~/devel/dev3; rustc --crate-type=staticlib add2.rs
    : user@debian:~/devel/dev3; ls -l libadd2.a
    -rw-r--r-- 1 user user 19493732 Oct  7 23:51 libadd2.a
    : user@debian:~/devel/dev3; cat calladd2.c
    #include <stdio.h>

    int add(int a, int b);          /* prototype for function written in Rust */

    int main(int argc, char **argv) {
      printf("3 + 4 = %d\n", add(3, 4));
      return 0;
    }
    : user@debian:~/devel/dev3; cc -L. calladd2.c -ladd2 -lpthread -ldl -lm -lrt
    : user@debian:~/devel/dev3; ls -l a.out
    -rwxr-xr-x 1 user user 4689773 Oct  7 23:52 a.out
    : user@debian:~/devel/dev3; ./a.out
    3 + 4 = 7

(It sort of works with `cc -static` but gives terrifying warnings.)

So it seems like doing this in practice would involve doing some of
the things mentioned in the “Hello World is Fucking Huge” section
above.  Until your library is hundreds of thousands of lines of code,
anyway.

[Fontdue](https://github.com/mooman219/fontdue) is a TrueType
rasterizer written this way (a `no_std` crate) to facilitate calling
from C.  It seems like I could probably learn a lot from things like
that about how to pull this off.

However, it’s notable that building libraries like this evidently
doesn’t rely on having a working GCC toolchain, so cross-compiling is
easier for building C-callable libraries than for building
executables:

    : user@debian:~/devel/dev3; rustc --crate-type=staticlib \
        --target s390x-unknown-linux-gnu add2.rs
    : user@debian:~/devel/dev3; ls -l libadd2.a
    -rw-r--r-- 1 user user 37002666 Oct  8 00:13 libadd2.a
    : user@debian:~/devel/dev3; ar tv libadd2.a
    rw-r--r-- 0/0   1640 Dec 31 21:00 1969 add2.add2.a3d9fba4-cgu.0.rcgu.o
    rw-r--r-- 0/0   2288 Dec 31 21:00 1969 add2.1o36m3z73gy3kp52.rcgu.o
    ...[188 lines omitted]...
    : user@debian:~/devel/dev3; ar x libadd2.a add2.add2.a3d9fba4-cgu.0.rcgu.o
    : user@debian:~/devel/dev3; ls -l add2.add2.a3d9fba4-cgu.0.rcgu.o
    -rw-r--r-- 1 user user 1640 Oct  8 00:14 add2.add2.a3d9fba4-cgu.0.rcgu.o
    : user@debian:~/devel/dev3; file add2.add2.a3d9fba4-cgu.0.rcgu.o
    add2.add2.a3d9fba4-cgu.0.rcgu.o: ELF 64-bit MSB relocatable, IBM S/390, version 1 (SYSV), not stripped

I don’t have cross-platform binutils installed, though:

    : user@debian:~/devel/dev3; objdump -d add2.add2.a3d9fba4-cgu.0.rcgu.o

    add2.add2.a3d9fba4-cgu.0.rcgu.o:     file format elf64-big

    objdump: can't disassemble for architecture UNKNOWN!

Creature comforts and affordances
---------------------------------

I’d really like to have Hypothesis.  [Rik de Kort has ported
minithesis](https://github.com/Rik-de-Kort/minithesis-rust) but
doesn’t recommend using it; he recommends the Hypothesis-inspired
[proptest](https://docs.rs/proptest/0.10.1/proptest/) ([docs][7]) or
[quickcheck](https://docs.rs/quickcheck/0.9.2/quickcheck/) instead,
which latter is by BurntSushi (Andrew Gallant, the ripgrep guy) and
also comes recommended by DRMacIver.  There are [efforts to provide
proptest via symbolic execution in KLEE][6].

[6]: https://alastairreid.github.io/why-not-both/
[7]: https://altsysrq.github.io/proptest-book/proptest/tutorial/macro-proptest.html

It’s nice that there’s a standard test setup: the `#[cfg(test)]`
attribute on a `mod`, the `#[test]` attribute on each test function,
the `assert!` macro (or just `panic!`), and `cargo test` to run the
lot (implicitly all in parallel!).  I don’t think the Rust book’s
recommendation to put the tests `mod` in `src/lib.rs` is optional or
not; XXX try it.  I like the recommendation to put unit tests in the
same file as the implementation; I guess Cargo enforces the putting of
integration tests in a `tests/` directory and `extern crate` importing
your library module?  XXX try a different directory.

### Deep equality and deep printing ###

One of the big advances in Python over Perl for me was deep equality
and printing by default (for lists, tuples, and dicts), The semantics
of equality used by `assert_eq!` are those of `==`, which comes from
the `PartialEq` trait.  As with printing, Rust doesn’t do the deep
comparison thing for structs and enums unless you opt into it with
`#[derive(..., PartialEq)]`.  Not sure yet about the semantics of
these with built-in arrays, slices, tuples, and hash maps.  XXX try
it.  Vec evidently has a useful debug print format.

Vec and std::collection::HashMap at least do the deep equality thing
by default.  Given this code:

    let xs = vec![3, 8, 12];

    let mut ys = vec![3, 8];
    ys.push(13);
    assert_eq!(xs, ys);

We get this behavior:

    : user@debian:~/devel/dev3; ./veciter
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `[3, 8, 12]`,
     right: `[3, 8, 13]`', veciter.rs:6:5
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

And similarly for HashMap.  It formats okay with `{:?}` too.

### Backtraces ###

It’d be nice to have a stack data dump like Python `cgitb`, but I’m
not sure to what extent that’s implementable in Rust.  With
`RUST_BACKTRACE=1` in the environment, you do get some kind of
backtrace, but it doesn’t display the values of local variables, and
if you compile without `-g` it won’t even show you the line number in
your code where it failed:

    : user@debian:~/devel/dev3; RUST_BACKTRACE=1 ./veciter
    thread 'main' panicked at 'assertion failed: `(left == right)`
      left: `[3, 8, 12]`,
     right: `[3, 8, 13]`', veciter.rs:6:5
    stack backtrace:
       0: rust_begin_unwind
                 at /rustc/c8dfcfe046a7680554bf4eb612bad840e7631c4b/library/std/src/panicking.rs:515:5
       1: core::panicking::panic_fmt
                 at /rustc/c8dfcfe046a7680554bf4eb612bad840e7631c4b/library/core/src/panicking.rs:92:14
       2: core::panicking::assert_failed_inner
       3: core::panicking::assert_failed
       4: veciter::main
       5: core::ops::function::FnOnce::call_once
    note: Some details are omitted, run with `RUST_BACKTRACE=full` for a verbose backtrace.

The suggested `RUST_BACKTRACE=full` gives you more stack frames,
machine-code addresses, and compilation hashes, but not more
variables, e.g.,

      17:     0x7ff3987a1c61 - veciter::main::hdfeb52505aea83ac
                                   at /home/user/devel/dev3/veciter.rs:6:5

This would be useful if I were debugging the compiler or build system
but not if the bug is in my code.

### Etc. ###

Failing full backtraces, what does the debugger look like?  [Evidently
(Rust’s fork of) GDB and (Rust’s MacOS-only fork of) LLDB are
supported][10], and Tom Tromey has been working on it, but DWARF can’t
represent traits yet.

There are some wrappers installed by Rustup (or Cargo?) that don’t
work:

    : user@debian:~/devel/dev3; rust-gdb
    gdb: unrecognized option '-iex'
    Use `gdb --help' for a complete list of options.
    : user@debian:~/devel/dev3; rust-lldb
    lldb not found! Please install it.

You'd think there would be a `rustfilt` analogous to `c++filt` for the
name mangling, but there doesn’t seem to be.

[There’s a crate called coredump to dump core on panic][11], which is
potentially a useful alternative to full backtraces, if you have a
working debugger, anyway.

Printf debugging in tests is feasible but requires `cargo test --
--nocapture`.

[10]: https://rustc-dev-guide.rust-lang.org/debugging-support-in-rustc.html
[11]: https://lib.rs/crates/coredump

A lot of the things I’m accustomed to in the Python standard library
(JSON, XML, HTTP) aren’t in the Rust standard library; you’re supposed
to get them from Cargo.  But which crates (packages) do I use in Cargo
for these things?  For example, apparently [ureq is a lot smaller than
reqwest for HTTP][0].

[0]: https://arusahni.net/blog/2020/03/optimizing-rust-binary-size.html

I guess one possibility is to look at exemplary Rust projects and see
what dependencies *they* use.  ripgrep, for example, has 46
dependencies (!).  Among them are the FNV hash function used by the
Rust compiler, `atty` (which provides various OS-specific cversions of
`isatty`), `libc` (a wrapper around libc), `itoa` (a faster version
than the `fmt::Formatter` version), `memmap2` (a fork of memmap-rs,
supporting mmap and similar facilities on other OSes), `ryu` (for
float-to-string conversion), and `serde` (similar to pickle).  This
gives something of a flavor of the stuff left out of the standard
library.

_Rust for the Polyglot Programmer_ recommends crates called `slab`,
`slotmap`, and `generational_arena` for memory management;
`itertools`; the locking-primitives crate `parking_lot`; the `tokio`
runtime for async programs; the alternative `smol`; `pin-project` and
`pin-project-lite` for dealing with some obscure async problems;
`futures`; `cxx`, for calling C++; `inline-python` and `pyo3` for
calling Python; `wasm-bindgen`, `web-sys`, and `rusty_v8` for WASM and
the web; `j4rs` and `jni` for calling Java; `fehler`, `thiserror`,
`eyre`, and/or `anyhow` for error handling; `num`, `num-traits`, and
`num-derive` for numerical code and integer conversion; `index_vec`,
`arrayvec`, and `indexmap` for containers; `easy-ext`; `rayon` and
`crossbeam` for multi-thread parallelism; `chrono` and `chrono-tz` for
datetime; `libc` or `nix`; `lazy_static` and `once_cell`; `log`;
`tracing`; `regex`; `lazy-regex`; `glob`; `tempfile`; `rand` (also
recommended by TRPL); `either`; `void`; `ndarray`; `ndarray-linalg`;
`ring`; `rustls`; `bstr`; `bytemuck`; `serde`, mentioned above, but
also with the objective of data *interchange with other languages*,
saying they are “considerably better for many tasks than anything
available in any other programming environment”; `reqwest` or `ureq`;
`hyper` for raw HTTP; `rocket`, `actix-web`, `rouille` (sync), or
`warp` as a web server framework; `structop` and `clap` or `argparse`
for command-line parsing; etc.  It also suggests looking at “recent
downloads” on crates.io to see what other people are using.  It
specifically recommends avoiding `wasm-pack` and `stdweb`.

I think the easiest way to make Cargo get the source for a package is
to add it as a dependency to a project.
