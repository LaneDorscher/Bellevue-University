# Title: factorial.py
# Original Author: Professor Krasso
# Original Date: 8/11/2023

# Modifiying Author: Lane Dorscher
# Modified Date: 11/16/2025


# Description:
# This program calculates the factorial of a number using recursion and improves
# efficiency by using memoization to store previously computed factorials.
# Memoization prevents redundant evaluations that would occur in a naive recursive
# implementation, which is especially important for larger input values.

def factorial(n, memo={}):
    """Compute factorial with memoization to avoid redundant evaluations."""
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = n * factorial(n - 1, memo)
    return memo[n]

# Demonstration call to factorial(3)
print("Demonstration: factorial(3) =", factorial(3))

# User input section
try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        print("The factorial of", num, "is", factorial(num))
except:
    print("Input must be a number and cannot be empty")

# -------------------------------
# Normal order evaluation can cause recursive functions to perform redundant
# calculations by repeatedly expanding function calls instead of computing them once.
# Using factorial(3) as an example, without memoization, the same recursive calls
# would be recalculated unnecessarily. Python uses applicative order evaluation,
# but memoization further improves efficiency by storing already computed factorials,
# ensuring that each value is calculated only once. Using a local memo dictionary makes 
# the function self-contained, prevents side effects from other parts of the program, 
# improves reusability, and keeps the code cleaner and easier to maintain 
# compared to using a global dictionary.
