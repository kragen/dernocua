#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys, os, re, stat

import when


def main():
    herefiles = os.listdir('.')

    for line in sys.stdin:
        f = line.split()
        if f[1:2] != ['written']:
            sys.stdout.write(line)
            continue
        pat = re.compile('(?:' + re.escape(f[0]) + r'(?:[.]md)?(?:[.]~\d+)?~?)$')
        
        backups = [n for n in herefiles if pat.match(n)]
        sys.stderr.write('Candidates for %s: %s\n' % (f, backups))
        if backups:             # XXX we should urldecode f[0] but didn’t
            mintime = min(os.stat(n).st_mtime for n in backups)
            date = when.date(mintime)
            sys.stderr.write('oldest date is %s %s\n' % (mintime, date))
            if date < f[2]:
                sys.stderr.write('changing from %s\n' % f[2])
                print(f[0], f[1], date)
                continue

        sys.stdout.write(line)
        
if __name__ == '__main__':
    main()
