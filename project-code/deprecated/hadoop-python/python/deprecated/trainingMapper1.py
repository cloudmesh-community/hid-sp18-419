#!/usr/bin/env python

'''
trainingMapper.py
Author: Min Chen <mc43@iu.edu>
Date: 2018-04-06
Last change: 2018-04-07

The input of this file is from stdin, which reads from the directory of training data
The output of this file serves as input for trainingReducer.py
'''


import sys
from tokens import TOKENS

def read_input(file):
    for line in file:
        yield TOKENS(line).get_tokens()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for tokenlist in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for
        # trainingReducer.py
        # tab-delimited; the trivial word count is 1
        for token in tokenlist:
            print ('%s%s%d' % (token, separator, 1))

if __name__ == "__main__":
    main()