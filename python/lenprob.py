# -*- coding: utf-8 -*-
import string
import pandas as pd

def find_lengths(filepath):
    """Assembles a matrix of probabilities that a word of one length will be
    followed by a word of another length"""

    with open(filepath, 'r') as myfile:
        text = myfile.read().replace('\n', '')

    exclude = set(string.punctuation)

    text = ''.join(ch for ch in text if ch not in exclude) #exclude punctuation
    text = ''.join([i for i in text if not i.isdigit()]) #exclude numbers
    text = text.lower() #make all text lowercase

    text = text.split()

    #initialize the probability matrix as a pandas dataframe to allow for easy
    #column/row lookup
    len_prob_mat = pd.DataFrame(0, index=range(1,10), columns=range(1,10))

    for word in range(len(text)-1):
        next_word = text[word+1]
        try:
            len_prob_mat[len(text[word])][len(next_word)] += 1 #increase count by 1
        except:
            pass


    cols = list(len_prob_mat.columns.values)

    #normalize across all columns to get probabilities
    len_prob_mat[cols] = len_prob_mat[cols].div(len_prob_mat[cols].sum(axis=1), axis=1)

    len_prob_mat.to_csv('english.csv')

    return len_prob_mat

if __name__ == "__main__":
    print find_lengths("../texts/English_Train.txt")
