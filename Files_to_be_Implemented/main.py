import pandas as pd
from Files_to_be_Implemented import Categorization
from Files_to_be_Implemented.Detailed_Csv_generation import adding_necessary_columns
from Files_to_be_Implemented.Cleaning import cleaning
from Files_to_be_Implemented.Modelling import model
from Files_to_be_Implemented.Saving_the_model import save_model
import warnings

base_address = "F:/Pycharm/"
warnings.simplefilter(action='ignore', category=FutureWarning)


class Role_Assignment:
    def __init__(self):
        self.raw_csv = base_address + "Role_Assignment/Dataset/mavoix_ml_sample_dataset.csv"
        self.cleaned_csv = base_address + "Role_Assignment/Dataset/cleaned_csv.csv"
        self.munged_csv = base_address + "Role_Assignment/Dataset/Munged_csv.csv"
        self.Data_Scientist_marks = 9
        self.Web_Developer_marks = 8
        self.cleaning_csv()
        self.adding_columns()
        self.modelling()
        self.save_model()

    @staticmethod
    def categorization_of_columns():
        Categorization()

    def cleaning_csv(self):
        cleaning(self.raw_csv, base_address)

    def adding_columns(self):
        adding_necessary_columns(self.cleaned_csv, base_address, self.Data_Scientist_marks, self.Web_Developer_marks)

    def modelling(self):
        self.clf = model(self.munged_csv)

    def save_model(self):
        save_model(self.clf, "Role Assignment")


if __name__ == '__main__':
    data_frame = pd.read_excel("F:/Pycharm/Role_Assignment/Dataset/mavoix_ml_sample_dataset.xlsx")
    data_frame.to_csv("F:/Pycharm/Role_Assignment/Dataset/mavoix_ml_sample_dataset.csv")

    Role_Assignment_obj = Role_Assignment()
