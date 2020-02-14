import pandas as pd
from Files_to_be_Implemented import Categorization
from Files_to_be_Implemented.Detailed_Csv_generation import adding_necessary_columns
from Files_to_be_Implemented.Cleaning import cleaning
from Files_to_be_Implemented.Modelling import model

base_address = "F:/Pycharm/"


class Role_Assignment:
    def __init__(self):
        self.raw_csv = base_address + "Role_Assignment/Dataset/mavoix_ml_sample_dataset.csv"
        self.cleaned_csv = base_address + "Role_Assignment/Dataset/cleaned_csv.csv"
        self.munged_csv = base_address + "Role_Assignment/Dataset/Munged_csv.csv"
        self.Data_Scientist_marks = 10
        self.Web_Developer_marks = 8
        self.cleaning_csv()
        self.adding_columns()
        self.modelling()

    @staticmethod
    def categorization_of_columns():
        Categorization()

    def cleaning_csv(self):
        cleaning(self.raw_csv, base_address)

    def adding_columns(self):
        adding_necessary_columns(self.cleaned_csv, base_address, self.Data_Scientist_marks, self.Web_Developer_marks)

    def modelling(self):
        model(self.munged_csv)


if __name__ == '__main__':
    data_frame = pd.read_excel("F:/Pycharm/Role_Assignment/Dataset/mavoix_ml_sample_dataset.xlsx")
    data_frame.to_csv("F:/Pycharm/Role_Assignment/Dataset/mavoix_ml_sample_dataset.csv")

    Role_Assignment_obj = Role_Assignment()
