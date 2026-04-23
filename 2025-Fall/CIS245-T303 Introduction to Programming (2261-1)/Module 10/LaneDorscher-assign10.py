# Prompt:
# You will use the base student class you created in Module 9 and create a declared student sub class that inherits from the base student class.
# Your program will use the methods of the student and declared student classes to accomplish the following:
# Prompt the user for the first name, last name, and student declared concentration. Concentration will be a program of study such as cybersecurity or business. 
# If the student is undeclared the user should be able to hit enter with no response to the prompt and the program will automatically assign NA as the declared concentration.
# Create a declared student class that inherits from the student class.
# Create a student object by passing the first and last name to the __init__ method.
# Create a declared student object by passing the concentration to the __init__ method.
# Create a loop that prompts the user for the following: The credits and grade for each course the student has taken.
# Once the user ends the loop, display the student’s cumulative GPA and student year. Student year will be determined per the below:
# - The student is a first year student if credits earned are less than or equal to 33.
# - The student is a second year student if credits earned are less than or equal to 66.
# - The student is a third year student if credits earned are less than or equal to 96.
# - The student is a fourth year student if credits earned are less than 130.
# - The student is a multi-year student if the credits earned are greater than or equal to 130.

## Author: Lane Dorscher
## Date: 11/15/2025

## Program Description:
# This program calculates a student’s cumulative GPA based on courses entered by the user. It supports both undeclared and declared students, tracking their declared concentration if provided. 
# The program prompts for course credits and letter grades, validates input, and computes the GPA dynamically.
#  It also determines the student’s academic year based on total credits and provides a detailed summary including the student’s name, concentration, total credits, GPA, and academic year.

from typing import Optional

class Student:

    GRADE_POINTS = {
        "A": 4.0,
        "B+": 3.5,
        "B": 3.0,
        "C+": 2.5,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.total_grade_points = 0.0
        self.total_credits = 0.0
        self.gpa = 0.0

    def AddCourse(self, credits: float, letter_grade: str):
        """Add a course with given credits and grade point."""
        self.total_grade_points += credits * Student.LetterGradeToPoints(letter_grade)
        self.total_credits += credits
        self.CalculateGPA()

    @staticmethod
    def LetterGradeToPoints(letter_grade:str) -> float:
        if (letter_grade in Student.GRADE_POINTS):
            return Student.GRADE_POINTS[letter_grade]
        return 0.0

    def CalculateGPA(self) -> None:
        """Recalculate the student's GPA."""
        if self.total_credits > 0:
            self.gpa = self.total_grade_points / self.total_credits
        else:
            self.gpa = 0.0

    def GetGPA(self) -> float:
        """Return the current GPA."""
        return self.gpa

    def __str__(self):
        return (
            f"Student: {self.first_name} {self.last_name}\n"
            f"Total Credits: {self.total_credits:.1f}\n"
            f"Cumulative GPA: {self.gpa:.2f}"
        )

    
class Declared_Student(Student):
    def __init__(self, first_name:str, last_name:str, concentration:str):
        Student.__init__(self, first_name, last_name)
        self.concentration = concentration.upper()

    def GetConcentration(self) -> str:
        return self.concentration

    def GetYear(self):
        full_name = f"{self.first_name} {self.last_name}"
               
        if (self.total_credits <= 33):
            return f"{full_name} is a Year One Student"
        elif (self.total_credits <= 66):
            return f"{full_name} is a Year Two Student"
        elif (self.total_credits <= 96):
            return f"{full_name} is a Year Three Student"
        elif (self.total_credits < 130):
            return f"{full_name} is a Year Four Student"
        else:
            return f"{full_name} is a Multi-year Student"
        
    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        concentration_text = (
            "No declared concentration"
            if self.concentration == "NA"
            else f"Concentration: {self.concentration}"
        )

        return (
            f"Student: {full_name}\n"
            f"{concentration_text}\n"
            f"Total Credits: {self.total_credits:.1f}\n"
            f"Cumulative GPA: {self.gpa:.2f}\n"
            f"{self.GetYear()}"
        )


def GetFloatInput(prompt: str, allow_quit: bool = False) -> Optional[float]:
    """Safely get a float input with validation."""

    if allow_quit:
        prompt = prompt + " (or 'q' to quit): "

    while True:
        value = input(prompt).strip()
        if allow_quit and value.lower() in ("q", "quit", "done"):
            return None
        try:
            num = float(value)
            return num
        except ValueError:
            errorMsg = "Invalid input. Please enter a numeric value"
            if (allow_quit):
                errorMsg = errorMsg + " (or 'q' to quit)."
            print(errorMsg)


def GetGradeInput() -> str:
    """Prompt user for a valid letter grade and return its numeric equivalent."""
    while True:
        grade = input("Enter letter grade for that course (A, B+, B, C+, C, D, F): ").strip().upper()
        if grade in Student.GRADE_POINTS:
            return grade
        else:
            print("Invalid grade. Please enter one of: A, B+, B, C+, C, D, F.")


def Main() -> None:
    print("=== Student GPA Calculator ===")

    first_name = input("Enter the student's first name: ").strip()
    last_name = input("Enter the student's last name: ").strip()
    concentration = input("Enter the student's concentration (Enter 'NA' if the student is undeclared): ").strip()
    if (concentration == ""):
        concentration = "NA"

    student = Declared_Student(first_name, last_name, concentration)

    while True:
        
        credits = GetFloatInput("Enter credits for the course", allow_quit=True)
        if credits is None:
            break
        elif (credits <= 0):
            print(f"Credits must be greater than 0. Try again!\n")
            continue

        letter_grade = GetGradeInput()

        student.AddCourse(credits, letter_grade)

    print("\nFinal Results:")
    print(student)


if __name__ == "__main__":
    Main()
