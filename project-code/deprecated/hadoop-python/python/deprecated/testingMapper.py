#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys, os
from tokens import TOKENS

def main(separator='\t'):
    # input comes from STDIN (standard input) and get the tokens for classification
    data = TOKENS(sys.stdin.read())
    allTokens = data.get_tokens()
    # get the file name
    try:
        file_name = os.environ['mapreduce_map_input_file']
    except KeyError:
        file_name = os.environ['map_input_file']
    file_name = file_name.split("/")[-1]

    for token in data:
        print ('%s%s%d' % (file_name, separator, token))

if __name__ == "__main__":
    main()