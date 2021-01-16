What would the simplest usable chat program look like?  In 1999 [IN
wrote a chat server in C in a .signature][0]:

    char a[99]="  KJ",d[999][16];main(){int s=socket(2,1,0),n=0,z,l,i;*(short*)a=2;
    if(!bind(s,a,16))for(;;){z=16;if((l=recvfrom(s,a,99,0,d[n],&z))>0){for(i=0;i<n;
    i++){z=(memcmp(d[i],d[n],8))?z:0;while(sendto(s,a,l,0,d[i],16)<0);}z?n++:0;}}}

[0]: http://canonical.org/~kragen/puzzle2.html

The client is four lines of C:

    char a[99]="  KJ";main(int c,char**v){int s=socket(2,1,0);char*p,*t=strchr(*++v
    ,'@'),*o=a+4;*(short*)a=2;p=t;while(*p)(*p++&48)-48?*o++=atoi(p):0;connect(s,a,
    16);strncpy(a,v[1],7);a[7]=':';a[8]=32;if(fork())while((c=read(0,a+9,90))>0)(
    write(s,a,c+9)>0)||exit(0);else while((c=read(s,a,99))>0)write(1,a,c);}

This was for Solaris, where `SOCK_DGRAM` was 1, rather than 2 as in
Linux `<bits/socket.h>`.  Both the client and the server are
vulnerable to buffer overflows, the server manifests a single chat
channel, there are no private messages, there's no recovery from
packet loss, and the server just keeps sending to disconnected clients
forever.  Nevertheless, under favorable circumstances, these two
programs do manifest a usable text chat system over TCP/IP.

If you have a shared Unix filesystem you can use a three-line shell
script for a client and need no server:

    #!/bin/sh
    : ${1?"usage: $0 nick [chan]"} ${chan=${2-/tmp/chat}}
    sleep 1; tail -f "$chan" & pid=$?; trap "kill $pid" 0
    while read t; do echo "<$1> $t"; done >> "$chan"

This inherits the Unix filesystem’s permissions, the Unix terminal’s
line editing, and whatever networking your filesystem supports, and it
should be reliable up to messages of `PIPE_BUF` size.

In 2008 I wrote [an IRC client in 40 lines of shell script][1]:

    #!/bin/sh
    # In the grim future of the Debian netinst disk, there is only nc.
    # And dd and sh, of course.
    : ${2?"Usage: $0 ircserver nickname"}
    ircserver="$1"
    nickname="$2"
    grimdir="`dirname "$0"`"
    case "$grimdir" in /*) ;; *) grimdir="../$grimdir" ;; esac

    tmpdir=".tmp.grimirc.$$"
    mkdir "$tmpdir"
    cd "$tmpdir"
    trap 'cd ..; rm -rf "$tmpdir"' 0

    (echo user grimirc hostname "$ircserver" :grimirc user
    echo nick "$nickname"
    > grimirc-responses
    tail -f grimirc-responses &
    while read command
            do case "$command" in
            /join*) echo "joining">/dev/tty
                    set $command; currentchan="$2"
                    echo "$command" > .grimtmp
                    dd bs=1 skip=1 < .grimtmp 2>/dev/null;;
            /*) echo "$command" > .grimtmp
                     dd bs=1 skip=1 < .grimtmp 2>/dev/null;;
            *) echo "PRIVMSG $currentchan :$command"
            esac
    done) | "$grimdir/grimdebuglog" | nc "$ircserver" 6667 | while read response
            do echo "$response"
            case "$response" in
            "PING "*) echo "responding to ping"
                    set $response
                    shift
                    echo "PONG $*" >> grimirc-responses
            esac
    done

[1]: https://web.archive.org/web/20140409022246/http://lists.canonical.org/pipermail/kragen-hacks/2008-February/000480.html

So, suppose we want to build a small program that implements something
like Van Jacobson’s CCN, with “interest” packets that get replied to
with matching “data” packets or forwarded to where you think they
might find those packets.  That would make it pretty easy to implement
a chat system, wouldn’t it?  One that really worked?  How hard would
that be to implement?