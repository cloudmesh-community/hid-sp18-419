#!/usr/bin/env python
'''
trainingMapper2.py
Author: Min Chen <mc43@iu.edu>
Date: 2018-04-07
Last change: 2018-04-07

The input of this file is the output of trainingReducer1, which contains the list of tokens
considererd from both the positive and negative training datasets.
The output of this file serves as input for trainingReducer2.py
This mapper does a direct mapping which basically combines to input file into one
'''

import sys

def read_input(file):
    for line in file:
        yield line.rstrip().split("\t", 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for line in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print ('%s%s%s' % (line[0], separator, line[1]))

if __name__ == "__main__":
    main()