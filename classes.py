import numpy as np


class Student:  # Student Class
    def __init__(self, name, year):  # The constructor takes 2 args (name,year)
        self.name = name  # Set self.name as name
        self.year = year  # Set self.year as year
        self.grades = []  # Set self.grades as an empty list

    def add_grade(self, grade):  # Add grades to self.grades list
        if type(grade) == Grade:  # Checking if grade is an instance of Grade
            # If yes, add the grade to self.grades
            self.grades.append(grade.score)

    def get_average(self):  # Returns average score
        total_grades = 0  # Setting a variable to add grades
        for grade in self.grades:  # Going trought each grade in self.grades
            total_grades += grade  # Adding each grade to total_grades
        # Return the total divided by the number of grades to get the average
        return total_grades / len(self.grades)


class Grade:  # Grade Class
    minimum_passing = 65  # Setting an attribute as minimum_passing = 65

    def __init__(self, score):  # The constructor takes one argument (score)
        self.score = score  # Setting self.score as score

    def is_passing(self):  # Returns if passing or not
        # Check if self.score >= than minimum_passing
        if self.score >= self.minimum_passing:
            return "Passing !"  # Yes, returns "Passing !"
        return "Not passing..."  # No, returns "Not passing..."


# Create 3 instances of Student as roger, sandro and pieter
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(95))  # Add a 95 percent grade to pieters grades
pieter.add_grade(Grade(50))  # Add a 50 percent grade to pieters grades
pieter.add_grade(Grade(61))  # Add a 63 percent grade to pieters grades

# Getting and printing pieter's average score, rounding it with numpy
print(np.round(pieter.get_average(), 2))
