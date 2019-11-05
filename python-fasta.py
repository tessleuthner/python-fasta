#!/usr/bin/env python

import sys

def read_fasta(filename):
    seq = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            seq = seq + line #only keep the line if it's not an identifier line that begins with '>'
    f.close()
    return seq
print(read_fasta(sys.argv[1]))
