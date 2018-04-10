#!/usr/bin/python
import os
import sys

def get_sectors(inp):
    foo = inp.split('; ')
    startsectors = []

    for line in foo:
        if line.startswith('partition'):
            bar = line.split(', ')

            for t in bar:
                if t.startswith('startsector'):
                    startsectors.append(int(t.split(' ')[1]))

    return startsectors

if __name__ == '__main__':
    if len(sys.argv) < 3:
        f = sys.stdin
    else:
        f = open(sys.argv[2], 'r')
    for line in f:
        print get_sectors(line)
            
