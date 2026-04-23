# student.py
# Author: Lane Dorscher
# Date: 10/12/2025
# Description:
# Demonstrates the creation of an abstract class and a concrete class in Python.

from abc import ABC, abstractmethod

# Abstract class
class Student(ABC):
    @abstractmethod
    def take_test(self):
        pass

# Concrete class
class PythonStudent(Student):
    def take_test(self):
        print("Student takes a Python Test!")

def main():
    student = PythonStudent()
    student.take_test()

if __name__ == "__main__":
    main()