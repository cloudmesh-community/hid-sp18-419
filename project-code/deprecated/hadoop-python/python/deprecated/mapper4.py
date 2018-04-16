#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys, os

def read_input(file):
    for line in file:
        # split the line into words
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    try:
        file_name = os.environ['mapreduce_map_input_file']
    except KeyError:
        file_name = os.environ['map_input_file']
    file_name = file_name.split("/")[-1]
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            print ('%s%s%d' % (file_name + "_&_" + word, separator, 1))

if __name__ == "__main__":
    main()