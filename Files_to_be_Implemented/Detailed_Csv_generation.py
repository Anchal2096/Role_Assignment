import pandas as pd
from Files_to_be_Implemented.Categorization import categorization


def adding_necessary_columns(cleaned_csv, base_address, Data_Scientist_marks, Web_Developer_marks):
    add_col_df = pd.read_csv(cleaned_csv)
    """matriculation_percentage calculation
    matriculation_marks = []
    for index in range(add_col_df.shape[0]):
        list_marks = list(add_col_df["Performance_10"][index])
        for index_data in range(len(list_marks)):
            if list_marks[index_data] == "/":
                matriculation_marks.append("".join(list_marks[0:index_data]))
    print(matriculation_marks)"""

    python_class, web_development_class, other_skill_web_development_class, other_skill_python_class = categorization()
    """counting total points and eligibility in data science"""
    marks_obtained = 0
    Data_Scientist_skill = []
    Data_Scientist_Total = []

    for column in python_class:
        # for rows in range(add_col_df.shape[0]):
        marks_obtained = marks_obtained + (add_col_df[column])
    python_marks = list(marks_obtained)
    # print(python_marks)

    for each_candidate in range(add_col_df.shape[0]):
        skills = str(add_col_df["Other skills"][each_candidate])
        skills = skills.split(",")
        skills = [x.lower() for x in skills]
        skills = [x.replace(" ", "") for x in skills]

        skills = set(skills)
        # print(skills)
        other_skill_python_class = set(other_skill_python_class)
        # print(other_skill_python_class)
        Data_Scientist_skill.append(len(skills.intersection(other_skill_python_class)))

    # print(Data_Scientist_skill)
    for index in range(0, len(Data_Scientist_skill)):
        Data_Scientist_Total.append(Data_Scientist_skill[index] + python_marks[index])

    # print(Data_Scientist_Total)
    # first column added
    add_col_df["Data_Scientist_Total"] = Data_Scientist_Total

    """counting total points and eligibility of web development"""

    marks_obtained = 0
    Web_Development_skill = []
    Web_Development_Total = []

    python_class, web_development_class, other_skill_web_development_class, other_skill_python_class = categorization()
    for column in web_development_class:
        # for rows in range(add_col_df.shape[0]):
        marks_obtained = marks_obtained + (add_col_df[column])
    web_development_marks = list(marks_obtained)
    # print(web_development_marks)

    for each_candidate in range(add_col_df.shape[0]):
        skills = str(add_col_df["Other skills"][each_candidate])
        skills = skills.split(",")
        skills = [x.lower() for x in skills]
        skills = [x.replace(" ", "") for x in skills]

        skills = set(skills)
        # print(skills)
        other_skill_web_development_class = set(other_skill_web_development_class)
        # print(other_skill_python_class)
        Web_Development_skill.append(len(skills.intersection(other_skill_web_development_class)))

    # print(Web_Development_skill)
    for index in range(0, len(Web_Development_skill)):
        Web_Development_Total.append(Web_Development_skill[index] + web_development_marks[index])

    # print(Web_Development_Total)
    # first column added
    add_col_df["Web_Development_Total"] = Web_Development_Total

    Web_Development_Eligibility = []
    Data_Scientist_Eligibility = []

    for marks in Data_Scientist_Total:
        if marks >= Data_Scientist_marks:
            Data_Scientist_Eligibility.append(1)
        else:
            Data_Scientist_Eligibility.append(0)

    for marks in Web_Development_Total:
        if marks >= Web_Developer_marks:
            Web_Development_Eligibility.append(1)
        else:
            Web_Development_Eligibility.append(0)

    # print(Data_Scientist_Eligibility)
    # print(Web_Development_Eligibility)
    add_col_df["Web_Development_Eligibility"] = Web_Development_Eligibility
    add_col_df["Data_Scientist_Eligibility"] = Data_Scientist_Eligibility

    """Assigning the post to the selected candidates 
    0 : Not Eligible
    1 : Data Scientist
    2 : Web developer
    3 : Both """

    Assigning_post = []
    for eligible in range(len(Data_Scientist_Eligibility)):
        if Data_Scientist_Eligibility[eligible] == 0 and Web_Development_Eligibility[eligible] == 0:
            Assigning_post.append(0)
        if Data_Scientist_Eligibility[eligible] == 1 and Web_Development_Eligibility[eligible] == 0:
            Assigning_post.append(1)
        if Data_Scientist_Eligibility[eligible] == 0 and Web_Development_Eligibility[eligible] == 1:
            Assigning_post.append(2)
        if Data_Scientist_Eligibility[eligible] == 1 and Web_Development_Eligibility[eligible] == 1:
            Assigning_post.append(3)
    # print(Assigning_post)

    add_col_df["Post Assigned"] = Assigning_post
    add_col_df.drop("Unnamed: 0.1", axis=1, inplace=True)
    add_col_df.drop("Unnamed: 0", axis=1, inplace=True)

    add_col_df.to_csv(base_address + "Role_Assignment/Dataset/Munged_csv.csv")
