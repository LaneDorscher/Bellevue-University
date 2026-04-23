
from sys import maxsize


array = [1, 2, 3, "4", "233"]




def sum_of_squares(nums):
    """
    Calculate and return the sum of squares of the numbers in the list.
    """   
    sum = 0
    for num in nums:
        sum += (num * num)
    return sum

def string_reversal(s):
    """
    Reverse the given string and return it.
    """
    reversed_string = ""
    for r in range(len(s) - 1, -1, -1): 
        reversed_string += s[r]
    return reversed_string



def find_second_largest(nums):
    """
    Find and return the second largest number in the list.
    If the list is too short, return None.
    """
    if len(nums) < 2:
        return None
    
    smallest_number = -maxsize - 1 ## storing smallest number to avoid recalculating multiple times
    first_max = smallest_number
    second_max = smallest_number

    for number in nums:
        if number > first_max:
            second_max = first_max
            first_max = number
        elif number > second_max and number != first_max:
            second_max = number

    return second_max if second_max != smallest_number else None
