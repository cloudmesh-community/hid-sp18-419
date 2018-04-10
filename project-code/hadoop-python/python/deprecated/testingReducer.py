#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys

def get_pos(filepath):
    pos = {}
    with open(filepath, 'r') as inputFile:
        for line in inputFile:
            token = line.rstrip().split("\t", 1)[0]
            try:
                count = int(line.rstrip().split("\t", 1)[1])
                pos[token] = count
            except ValueError:
                # count was not a number, so silently discard this item
                pass
    return pos

def get_neg(filepath):
    neg = {}
    with open(filepath, 'r') as inputFile:
        for line in inputFile:
            token = line.rstrip().split("\t", 1)[0]
            try:
                count = int(line.rstrip().split("\t", 1)[1])
                neg[token] = count
            except ValueError:
                # count was not a number, so silently discard this item
                pass
    return neg

def get_agg(filepath):
    '''
    total_vocabulary%	184
    total_tokens%	226
    '''
    vocabulary = 0
    tokens = 0
    with open(filepath, 'r') as inputFile:
        for line in inputFile:
            name, value = line.rstrip().split("\t", 1)
            if name == "total_vocabulary%":
                vocabulary = int(value)
            if name == "total_tokens%":
                tokens = int(value)
    return (vocabulary, tokens)

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)


    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print ("%s%s%d" % (current_word, separator, total_count))
        except ValueError:
            # count was not a number, so silently discard this item
            pass

if __name__ == "__main__":
    main()