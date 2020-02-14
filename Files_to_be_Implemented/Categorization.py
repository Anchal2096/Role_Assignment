def categorization():
    other_skill_python_class_list = []

    python_class = ["Python (out of 3)", "R Programming (out of 3)", "Deep Learning (out of 3)", "MongoDB (out of 3)",
                    "MySQL (out of 3)"]
    web_development_class = ["PHP (out of 3)", "HTML (out of 3)", "CSS (out of 3)", "JavaScript (out of 3)",
                             "AJAX (out of 3)", "Bootstrap (out of 3)", "Node.js (out of 3)", "ReactJS (out of 3)"]

    other_skill_web_development_class = ["C#.NET", " Adobe Photoshop", "jQuery", "Django", ".NET", "ASP.NET ",
                                         "Search Engine Optimization (SEO)", "UI & UX Design",
                                         "User Interface (UI) Development", "XML", "Angular 2.0", "Dream Weaver"]

    other_skill_python_class = ["Algorithms", "Data Structures", "Data Analytics", "Natural Language Processing (NLP)",
                                "PostgreSQL", "Statistical Modeling", "Deep Learning", "Artifical Intelligence",
                                "Power BI", "Hadoop", "Apache", "MATLAB", "SPSS", "WORD PRESS", "MACHINE LEARNING",
                                "NEURAL NETWORK", "Big Data Analytics", "Flask", "Computer Vision", "Tableau",
                                "Cloud Computing", "Image Processing", "Internet of Things", "Angular JS",
                                "Electron JS"]

    other_skill_python_class_list = [x.lower() for x in other_skill_python_class]
    other_skill_python_class_list = [x.replace(" ", "") for x in other_skill_python_class_list]

    other_skill_web_development_class_list = [x.lower() for x in other_skill_web_development_class]
    other_skill_web_development_class_list = [x.replace(" ", "") for x in other_skill_web_development_class_list]

    # print(other_skill_web_development_class_list)
    return python_class, web_development_class, other_skill_web_development_class_list, other_skill_python_class_list
