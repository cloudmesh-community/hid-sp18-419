#!/usr/bin/env python
'''
trainingReducer2.py
Author: Min Chen <mc43@iu.edu>
Date: 2018-04-07
Last change: 2018-04-07

The input of this file is the output of trainingMapper2
The output is the total vocabulary and total token counts for computing the likelihood in the
testing phase.
'''


from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)
    # groupby groups multiple word-count pairs by word,
    # and creates an iterator that returns consecutive keys and their group:
    #   current_word - string containing a word (the key)
    #   group - iterator yielding all ["&lt;current_word&gt;", "&lt;count&gt;"] items
    total_vocabulary = 0
    total_tokens = 0
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            #print ("%s%s%d" % (current_word, separator, total_count))
            total_tokens += total_count
            total_vocabulary += 1
        except ValueError:
            # count was not a number, so silently discard this item
            pass
    print("%s%s%d" % ("total_vocabulary%", separator, total_vocabulary))
    print("%s%s%d" % ("total_tokens%", separator, total_tokens))

if __name__ == "__main__":
    main()