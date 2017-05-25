from functools import reduce
from pprint import pprint as pp

def count_words(doc):
    """
    Count words in a document
    :param doc: a document file
    :return: a dictionary mapping words
    """
    normalized_document = ''.join(c.lower() if c.isalpha()
                                  else ' ' for c in doc)
    frequencies = {}
    for word in normalized_document.split():
        frequencies[word]= frequencies.get(word, 0) + 1
    return frequencies

documents = [
"It was the best of times, it was the worst of times",
    "it went to the woods becuase I wished to live there",
    "Friends, Romans, Countrymen, lend me your ears; I come to bury Cesar, not to praise him.",
    "I do not like green eggs and ham. I do not like it Sam-I-Am"
]

counts = map(count_words, documents)


def combine_counts(d1, d2):
    """
    Combine iterable information
    :param d1: First Dict
    :param d2: Second Dict
    :return: Combined Dict
    """

    d = d1.copy()
    for word, count in d2.items():
        d[word] = d2.get(word, 0) + count
    return d

def main():
    #c = count_words("It was the best of times, it was the worst of times")
    #print(c)

    total_counts = reduce(combine_counts, counts)
    pp(total_counts)

if __name__ == '__main__':
    main()
    exit(0)