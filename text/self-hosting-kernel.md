Last time I talked to Jeremiah Orians about it, the stage0-posix
project required only the following system calls of a POSIX kernel, up
to M2-Planet+mescc-tools:

* execve(), fork(), waitpid(), exit()
* brk()
* open(), close(), read(), write()
* lseek()
* chmod()

execve(), fork(), waitpid(), and exit() are used in a stereotyped
manner for spawning a child process running a new program, then
waiting for it to exit(); and chmod() is only used to make a file
executable.

He said mescc-tools-extra+Kaem also needs:

* fchmod()
* access()
* chdir(), fchdir()
* mkdir() (in particular for extracting tarballs)
* mknod()
* getcwd() (traditionally a library function implemented with stat())
* umask()
* uname() (to find out what the architecture is)

Mes proper and probably tcc also needs:

* unlink()
* ioctl() (specifically isatty(), to find out whether a shell is interactive)
* stat()
* fsync(), though of course this can be a no-op

In particular it doesn’t require pipes or I/O redirection.
