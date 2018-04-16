#!/usr/bin/env python
"""mapper3.py"""

import sys, os
# input comes from STDIN (standard input)
for line in sys.stdin:
    try:
        file_name = os.environ['mapreduce_map_input_file']
    except KeyError:
        file_name = os.environ['map_input_file']
    file_name = file_name.split("/")[-1]
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print ('%s\t%s' % (file_name+"_&_"+word, 1))