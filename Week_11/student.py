class Student:
    def __init__(self, name, section, spanish, english, social_studies, science):
        self.name = name
        self.section = section
        self.spanish = spanish
        self.english = english
        self.social_studies = social_studies
        self.science = science

    def calculate_average(self):
        total = self.spanish + self.english + self.social_studies + self.science
        return total / 4