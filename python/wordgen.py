# -*- coding: utf-8 -*-
from __future__ import division
import random
import pandas as pd

def weighted_choice(weights):
    """Uses random to return a weighted choice from a list of weights."""
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i

def choose_next(letter, mat):
    """Gets the next letter from the current letter by calling weighted_choice
    on the current letter"""
    builder = mat
    start = [float(i) for i in list(builder[letter])[1:]]
    next_letter = weighted_choice(start)
    return list(builder.index)[next_letter + 1]

def build_word(word_length, df):
    """Constructs a gibberish word by repeatedly calling choose_next"""
    word = ""
    word += choose_next(" ", df) #To get the first letter, use choose_next on a space

    df2 = df.drop(" ")

    while len(word) < word_length:
        word += choose_next(word[-1], df2)

    return word

def build_paragraph(par_length, language):
    """Builds a paragraph by repeatedly calling build_word"""

    #open relevant csv files
    probs = pd.read_csv("../bigram_matrices/"+language+".csv", encoding='utf8', engine='python').set_index("letters")
    lengths = pd.read_csv("../length_matrices/"+language+".csv", encoding='utf8', engine='python')

    par = []
    while len(par) < par_length:
        par.append(build_word(random.randint(2,6), probs))

    return par

def test_words(length, language):
    """Returns percentage of how many words are actual english words"""

    woot = build_paragraph(length, language)

    with open("../test/"+language+"_words.txt", 'r') as f:
        text = f.read().replace('\n', ' ')

    word_list = text.split()
    counter = 0

    for word in woot:
        if word in word_list:
            counter += 1

    return counter/len(woot)


if __name__ == "__main__":
    print test_words(10000, "english")
