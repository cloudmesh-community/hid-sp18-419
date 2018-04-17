#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter
import sys
import math

def get_model(filepath):
    sent = {}
    vocabulary = set()
    total = 0
    with open(filepath, 'r') as inputFile:
        for line in inputFile:
            token = line.rstrip().split("\t", 1)[0]
            vocabulary.add(token)
            try:
                count = int(line.rstrip().split("\t", 1)[1])
                sent[token] = count
                total += count
            except ValueError:
                # count was not a number, so silently discard this item
                pass
    return sent, vocabulary, total

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_mapper_output(sys.stdin, separator=separator)

    #read in the training model
    pos, vocabulary_pos, total_pos = get_model("pos.txt")
    neg, vocabulary_neg, total_neg = get_model("neg.txt")
    vocabulary= vocabulary_pos.union(vocabulary_neg)
    V = len(vocabulary)
    denominator_pos = math.log(total_pos + V)
    denominator_neg = math.log(total_neg + V)
    total_pos = 0
    total_neg = 0
    for current_file, group in groupby(data, itemgetter(0)):
        log_likelihood_pos = 0
        log_likelihood_neg = 0
        try:
            for current_file, token in group:
                if token in vocabulary:
                    if token in pos:
                        log_likelihood_pos += math.log(pos[token]+1) - denominator_pos
                    else:
                        log_likelihood_pos += math.log(1) - denominator_pos
                    if token in neg:
                        log_likelihood_neg += math.log(neg[token] + 1) - denominator_neg
                    else:
                        log_likelihood_neg += math.log(1) - denominator_neg
            if log_likelihood_pos > log_likelihood_neg:
                print("%s%s%s" % (current_file, separator, "positive"))
                total_pos += 1
            else:
                print("%s%s%s" % (current_file, separator, "negative"))
                total_neg += 1
        except:
            pass
    print("%s%s%d" % ("total number of positive document: ", separator, total_pos))
    print("%s%s%d" % ("total number of negative document: ", separator, total_neg))

if __name__ == "__main__":
    main()