# ----------------------------------------------------------
# Filename: tests.py
# Author: OpenAI
# ----------------------------------------------------------

import time

def time_sample_function(x):
    time.sleep(x)
    return x

def test_calculate_execution_time():
    cases = [
        (time_sample_function, 1, 1),    # Test 1
        (time_sample_function, 2, 2),    # Test 2
        (time_sample_function, 3, 3),    # Test 3
        (time_sample_function, 4, 4), # Test 4
        (time_sample_function, 5, 5)  # Test 5
    ]
    return cases

def test_bubble_sort():
    cases = [
        ([1, 3, 2], [1, 2, 3]),            # Test 6
        ([7, 8, 9, 11], [7, 8, 9, 11]),    # Test 7
        ([5, 3, 4, 1, 2], [1, 2, 3, 4, 5]),# Test 8
        ([1], [1]),                        # Test 9
        ([], [])                           # Test 10
    ]
    return cases

def test_insertion_sort():
    cases = [
        ([1, 3, 2], [1, 2, 3]),            # Test 11
        ([7, 8, 9, 11], [7, 8, 9, 11]),    # Test 12
        ([5, 3, 4, 1, 2], [1, 2, 3, 4, 5]),# Test 13
        ([], []),                          # Test 14
        ([1], [1])                         # Test 15
    ]
    return cases

def test_fibonacci_recursive():
    cases = [
        (0, 0),                            # Test 16
        (1, 1),                            # Test 17
        (2, 1),                            # Test 18
        (3, 2),                            # Test 19
        (4, 3),                            # Test 20
        (5, 5),                            # Test 21
        (6, 8),                            # Test 22
        (7, 13),                           # Test 23
        (8, 21),                           # Test 24
        (9, 34)                            # Test 25
    ]
    return cases
