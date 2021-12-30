Fung published [“the simplest (and most surprising) sorting algorithm
ever”][0] this year.

[0]: https://arxiv.org/abs/2110.01111

The algorithm from the paper is indeed an astonishingly simple sorting
algorithm, and it is indeed surprising that it works, particularly
since at first glance it would appear to sort the array *backwards*
(see the paper):

    void
    cantbelievesort(int *p, size_t n)
    {
      int tmp;
      for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) {
          if (p[i] < p[j]) tmp = p[i], p[i] = p[j], p[j] = tmp;
        }
      }
    }

That’s 10 lines of code according to David A. Wheeler’s ‘SLOCCount,’
though arguably 9 would be fairer. Its cyclomatic complexity is 3,
with a deepest statement nesting level of 4, and it has 5 variables:
three locals plus two arguments.

    0000000000001369 <cantbelievesort>:
        1369:	f3 0f 1e fa          	endbr64 
        136d:	48 89 f8             	mov    %rdi,%rax
        1370:	4c 8d 0c b7          	lea    (%rdi,%rsi,4),%r9
        1374:	49 39 c1             	cmp    %rax,%r9
        1377:	74 23                	je     139c <cantbelievesort+0x33>
        1379:	31 d2                	xor    %edx,%edx
        137b:	48 39 f2             	cmp    %rsi,%rdx
        137e:	74 16                	je     1396 <cantbelievesort+0x2d>
        1380:	8b 08                	mov    (%rax),%ecx
        1382:	44 8b 04 97          	mov    (%rdi,%rdx,4),%r8d
        1386:	44 39 c1             	cmp    %r8d,%ecx
        1389:	7d 06                	jge    1391 <cantbelievesort+0x28>
        138b:	44 89 00             	mov    %r8d,(%rax)
        138e:	89 0c 97             	mov    %ecx,(%rdi,%rdx,4)
        1391:	48 ff c2             	inc    %rdx
        1394:	eb e5                	jmp    137b <cantbelievesort+0x12>
        1396:	48 83 c0 04          	add    $0x4,%rax
        139a:	eb d8                	jmp    1374 <cantbelievesort+0xb>
        139c:	c3                   	retq

With gcc -Os 9.3.0, that’s 52 bytes, 19 instructions.  gcc -Os has
regressed; in 4.7.2, that used to be 44 bytes, 17 instructions:

    4007cc:       31 c0                   xor    %eax,%eax
    4007ce:       eb 22                   jmp    4007f2 <cantbelievesort+0x26>
    4007d0:       8b 0c 87                mov    (%rdi,%rax,4),%ecx
    4007d3:       44 8b 04 97             mov    (%rdi,%rdx,4),%r8d
    4007d7:       44 39 c1                cmp    %r8d,%ecx
    4007da:       7d 07                   jge    4007e3 <cantbelievesort+0x17>
    4007dc:       44 89 04 87             mov    %r8d,(%rdi,%rax,4)
    4007e0:       89 0c 97                mov    %ecx,(%rdi,%rdx,4)
    4007e3:       48 ff c2                inc    %rdx
    4007e6:       eb 02                   jmp    4007ea <cantbelievesort+0x1e>
    4007e8:       31 d2                   xor    %edx,%edx
    4007ea:       48 39 f2                cmp    %rsi,%rdx
    4007ed:       75 e1                   jne    4007d0 <cantbelievesort+0x4>
    4007ef:       48 ff c0                inc    %rax
    4007f2:       48 39 f0                cmp    %rsi,%rax
    4007f5:       75 f1                   jne    4007e8 <cantbelievesort+0x1c>
    4007f7:       c3                      retq   

However, arguably, *this* sort routine is even *simpler*. It may or
may not be surprising that it works:

    void
    dumbsort(int *p, size_t n)
    {
      int tmp;
      for (size_t i = 1; i < n; i++) {
        if (p[i] < p[i-1]) tmp = p[i], p[i] = p[i-1], p[i-1] = tmp, i = 0;
      }
    }

I don’t think I invented it, but I can’t remember who did.

By the same metric, that’s only 8 lines of code (also only 8 by my
“fairer” metric), its cyclomatic complexity is only 2, its deepest
statement nesting level is only 3, and it has only 4 variables (the
same two arguments, but two locals instead of three). It compiles to
only 15 amd64 instructions, occupying only 43 bytes:

      4007f8:       b8 01 00 00 00          mov    $0x1,%eax
      4007fd:       eb 1e                   jmp    40081d <dumbsort+0x25>
      4007ff:       4c 8d 04 87             lea    (%rdi,%rax,4),%r8
      400803:       48 8d 54 87 fc          lea    -0x4(%rdi,%rax,4),%rdx
      400808:       41 8b 08                mov    (%r8),%ecx
      40080b:       44 8b 0a                mov    (%rdx),%r9d
      40080e:       44 39 c9                cmp    %r9d,%ecx
      400811:       7d 07                   jge    40081a <dumbsort+0x22>
      400813:       45 89 08                mov    %r9d,(%r8)
      400816:       31 c0                   xor    %eax,%eax
      400818:       89 0a                   mov    %ecx,(%rdx)
      40081a:       48 ff c0                inc    %rax
      40081d:       48 39 f0                cmp    %rsi,%rax
      400820:       72 dd                   jb     4007ff <dumbsort+0x7>
      400822:       c3                      retq

Or, with more recent gcc, 55 bytes, 18 instructions:

    000000000000139d <dumbsort>:
        139d:	f3 0f 1e fa          	endbr64 
        13a1:	b8 01 00 00 00       	mov    $0x1,%eax
        13a6:	48 39 f0             	cmp    %rsi,%rax
        13a9:	73 28                	jae    13d3 <dumbsort+0x36>
        13ab:	48 8d 14 85 00 00 00 	lea    0x0(,%rax,4),%rdx
        13b2:	00 
        13b3:	4c 8d 04 17          	lea    (%rdi,%rdx,1),%r8
        13b7:	48 8d 54 17 fc       	lea    -0x4(%rdi,%rdx,1),%rdx
        13bc:	41 8b 08             	mov    (%r8),%ecx
        13bf:	44 8b 0a             	mov    (%rdx),%r9d
        13c2:	44 39 c9             	cmp    %r9d,%ecx
        13c5:	7d 07                	jge    13ce <dumbsort+0x31>
        13c7:	45 89 08             	mov    %r9d,(%r8)
        13ca:	31 c0                	xor    %eax,%eax
        13cc:	89 0a                	mov    %ecx,(%rdx)
        13ce:	48 ff c0             	inc    %rax
        13d1:	eb d3                	jmp    13a6 <dumbsort+0x9>
        13d3:	c3                   	retq   

[Dylan16807 points out][1] that if you tail-recurse to restart the
function instead of resetting the index, it gets even simpler.

[1]: https://news.ycombinator.com/item?id=28795143
