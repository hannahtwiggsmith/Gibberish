import json
import pandas as pd
from ngrams import find_ngrams

def convert(input_filename, output_filename):
    # df = pd.read_csv(input_filename)
    # blah = []
    # start = True
    # for row in df.itertuples():
    #     if start:
    #         start = False
    #         continue
    #     else:
    #         current = row.letters
    #         #print(row._fields)
    #         for column, value in zip(row._fields[2:], row[2:]):
    #             blah.append([current, column, value])
    #
    # print(blah)

    _,_,df = find_ngrams(input_filename,output_filename, 2)
    #print(df)
    print(list(df.columns.values))

    df.drop(list(df.columns.values)[-1], axis=1)
    print(df)

if __name__ == "__main__":
    convert("../texts/English_Train.txt", "../vis_data/vis_english.csv")
