from nltk.corpus import stopwords
import nltk
nltk.download('wordnet')
import string
from nltk.tokenize import WordPunctTokenizer

class TOKENS(object):
    def __init__(self, input):
        negateset = set(
            ["no", "not", "'t", "don't", "aren't", "isn't", "doesn't", "didn't", "cannot", "won't",
             "none", "nobody", "nobody", "nothing", "neither", "nowhere", "never", "wasn't",
             "shouldn't", "wouldn't", "couldn't", "can't", "hadn't" "rarely", "seldom", "hardly",
             "scarcely"])
        # using WordPunctTokenizer from nltk as tokenizer, tokenize the input
        tokenizer = WordPunctTokenizer()
        allTokens = tokenizer.tokenize(input)

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
        wnl = nltk.WordNetLemmatizer()
        allTokens = [wnl.lemmatize(t) for t in allTokens]

        # negation
        for j in negate:
            allTokens[j] = "NOT_" + allTokens[j]

        # stopwords
        allTokens = [token for token in allTokens if token not in stopwords.words('english')]

        # punctuation
        allTokens = [token for token in allTokens if token not in string.punctuation]

        self.tokens = allTokens

    def get_tokens(self):
        return self.tokens