import pandas as pd
import numpy as np


def cleaning(raw_csv, base_address):
    cleaning_df = pd.read_csv(raw_csv)
    # print(cleaning_df.shape)
    cleaning_df.drop("Unnamed: 10", axis=1, inplace=True)
    # print(cleaning_df.shape)
    cleaning_df.replace(np.nan, 0, inplace=True)
    # print(cleaning_df.shape[1])

    '''Discarding those candidates who haven't given their marks of their Graduation and Post Graduation'''
    for index in range(cleaning_df.shape[1]):
        if cleaning_df['Performance_PG'][index] == 0 and cleaning_df['Performance_UG'][index] == 0:
            cleaning_df.drop(index, inplace=True)

    columns_to_be_removed = ["Current City", "Degree", "Stream", "Current Year Of Graduation",
                             "Performance_12", "Performance_10", "Performance_PG", "Performance_UG"]
    cleaning_df.drop(columns_to_be_removed, axis=1, inplace=True)
    # cleaning_df.drop([columns_to_be_removed], axis = 1)
    cleaning_df.to_csv(base_address+"Role_Assignment/Dataset/cleaned_csv.csv")
