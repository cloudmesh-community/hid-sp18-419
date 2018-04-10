#!/usr/bin/env python

'''
trainingMapper.py
Author: Min Chen <mc43@iu.edu>
Date: 2018-04-06
Last change: 2018-04-10

The input of this file is from stdin, which reads from the directory of training data
The output of this file serves as input for trainingReducer.py
'''


import sys, re
import string

def getToken(input):
    negateset = set(
        ["no", "not", "'t", "don't", "aren't", "isn't", "doesn't", "didn't", "cannot", "won't",
         "none", "nobody", "nobody", "nothing", "neither", "nowhere", "never", "wasn't",
         "shouldn't", "wouldn't", "couldn't", "can't", "hadn't" "rarely", "seldom", "hardly",
         "scarcely"])

    stoplist = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're",
                    "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he',
                    'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it',
                    "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
                    'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those',
                    'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
                    'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
                    'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with',
                    'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
                    'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
                    'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where',
                    'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other',
                    'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
                    'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've",
                    'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn',
                    "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn',
                    "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't",
                    'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn',
                    "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn',
                    "wouldn't", "can't", "cannot"])
    # tokenize the input by space
    allTokens = input.split(" ")

    # turn all tokens into lower case
    allTokens = [token.lower() for token in allTokens]

    # place holders for negate markers
    negate = []

    # place holders for final token list
    final_tokens = []

    #regex for alphabetical token
    punct = re.compile("^[A-Za-z].*")

    #loop over all tokens
    for i in range(len(allTokens)):
        # mark negation
        if (allTokens[i] in negateset) and (i < len(allTokens) - 1):
            j = i + 1
            while ((j < len(allTokens)) and (allTokens[j] not in string.punctuation) and (
                        allTokens[j] not in negateset)):
                negate.append(j)
                j += 1

        # if tokens not in stoplist and not in punctuation and start with alphabet
        if (allTokens[i] not in stoplist) and (allTokens[i] not in string.punctuation) and (
                punct.match(allTokens[i])):
            #check negation mark
            if i in negate:
                #negated
                final_tokens.append("NOT_" + allTokens[i])
            else:
                #not negated
                final_tokens.append(allTokens[i])

    return final_tokens


def read_input(file):
    for line in file:
        yield getToken(line)

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