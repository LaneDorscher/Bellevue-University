
from sys import maxsize

def find_max_min(numbers):
    """
    Find the maximum and minimum numbers in a list.
    Return them as a tuple (max, min).
    """

    ## validate argument
    if not numbers or len(numbers) == 0:
        return (None, None)
    
    min_number = maxsize  ## intialize min as the max integer value from the system
    max_number = -maxsize - 1 ## initialize max as the minimum integer value from the system

    for num in numbers:
        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num
    return (max_number, min_number)

def check_symmetry(string):
    """
    Check if the given string is symmetrical.
    Return True if it is, False otherwise.
    """
    
    start = 0
    end = len(string) - 1

    while (start <= end):
        if (string[start] != string[end]):
            return False
        
        start = start + 1
        end = end - 1
    return True


def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into a single sorted list.
    Return the merged sorted list.
    """

    merged_list = []
    index1 = 0
    index2 = 0

    while index1 < len(list1) and index2 < len(list2) :
        if list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        else:
            merged_list.append(list2[index2])
            index2 += 1

    while index1 < len(list1):
        merged_list.append(list1[index1])
        index1 += 1

    while index2 < len(list2):
        merged_list.append(list2[index2])
        index2 += 1

    return merged_list
