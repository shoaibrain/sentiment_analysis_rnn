
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *
import re
from bs4 import BeautifulSoup
import pickle
import os
import glob


def review_to_words(review):
    """This method performs the following operations:
        1. Removes any HTML tags
        2.Converts string to lower case
        3.split string into words
        4.Filters out stop words and performs stemming.
    """
    nltk.download("stopwords", quiet=True)
    stemmer = PorterStemmer()

    text = BeautifulSoup(review, "html.parser").get_text()
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    words = text.split()
    words = [w for w in words if w not in stopwords.words("english")]
    words = [PorterStemmer().stem(w) for w in words]

    return words


def convert_and_pad(word_dict, sentence, pad=500):
    """"This method converts the review to string sequence representation and
        pads the fixed length to 500 words
    """"
    NOWORD = 0
    INFREQ = 1

    working_sentence = [NOWORD] * pad

    for word_index, word in enumerate(sentence[:pad]):
        if word in word_dict:
            working_sentence[word_index] = word_dict[word]
        else:
            working_sentence[word_index] = INFREQ

    return working_sentence, min(len(sentence), pad)
