# -*- coding: utf-8 -*-
import string
import pandas as pd

def find_ngrams(filepath, output, n):
    """ Finds all n-grams in a text sample and returns the probability matrix
    for that text sample. Also returns an n-gram dictionary, which tells you
    how often each n-gram occurs in the text."""

    with open(filepath, 'r') as myfile:
        text = myfile.read().replace('\n', '')

    exclude = set(string.punctuation)

    text = ''.join(ch for ch in text if ch not in exclude) #exclude punctuation
    text = ''.join([i for i in text if not i.isdigit()]) #exclude numbers
    text = text.lower() #make all text lowercase

    #initialize data structures
    ngram_dict = {}
    row_col = []

    #find all unique symbols in the text samples. row_col will serve as the
    #row and column labels of prob_mat
    for letter in text:
        if letter not in row_col:
            row_col.append(letter)

    #initialize the probability matrix as a pandas dataframe to allow for easy
    #column/row lookup
    prob_mat = pd.DataFrame(0, index=row_col, columns=row_col)

    for letter in range(len(text)-n):
        next_letter = text[letter+1]
        prob_mat[text[letter]][next_letter] += 1 #increase count by 1

        ngram = text[letter:letter+n] #take a slice from letter to next_letter
        try: ngram_dict[ngram] += 1 #increase dictionary count by one
        except KeyError: ngram_dict[ngram] = 1 #if it doesn't exist, add it and
                                                #make it equal to one

    cols = list(prob_mat.columns.values)

    #normalize across all columns to get probabilities
    prob_mat[cols] = prob_mat[cols].div(prob_mat[cols].sum(axis=1), axis=1)

    #prob_mat.to_csv(output)

    return ngram_dict, row_col, prob_mat #returns everything as a tuple

if __name__ == "__main__":
    print (find_ngrams("Hawaiian_Train.txt", "hawaiian.csv", 2))
