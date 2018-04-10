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
#import zipimport
import string

#importer = zipimport.zipimporter('nltk.mod')
#nltk = importer.load_module('nltk')
#from nltk.tokenize import WordPunctTokenizer


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
                    "wouldn't"])
    # using WordPunctTokenizer from nltk as tokenizer, tokenize the input
    #tokenizer = WordPunctTokenizer()
    #allTokens = tokenizer.tokenize(input)
    allTokens = input.split(" ")

    # turn all tokens into lower case
    allTokens = [token.lower() for token in allTokens]

    # list of negation positions
    negate = []
    for i in range(len(allTokens)):
        if (allTokens[i] in negateset) and (i < len(allTokens) - 1):
            j = i + 1
            while ((j < len(allTokens)) and (allTokens[j] not in string.punctuation) and (
                        allTokens[j] not in negateset)):
                negate.append(j)
                j += 1

    # lemmatization
    #wnl = nltk.WordNetLemmatizer()
    #allTokens = [wnl.lemmatize(t) for t in allTokens]

    # negation
    for j in negate:
        allTokens[j] = "NOT_" + allTokens[j]

    # stopwords
    #allTokens = [token for token in allTokens if token not in stopwords.words('english')]
    allTokens = [token for token in allTokens if token not in stoplist]

    # punctuation
    allTokens = [token for token in allTokens if token not in string.punctuation]

    return  allTokens

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