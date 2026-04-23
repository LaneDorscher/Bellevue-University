# ----------------------------------------------------------
# Filename: tester.py
# Author: OpenAI
# ----------------------------------------------------------

import tests

from week2_assignment import *

def run_tests(test_cases, function_to_test):
    total_tests = sum(len(test_cases[func]) for func in test_cases)
    test_counter = 0
    passed_tests = 0

    for func in test_cases:
        for case in test_cases[func]:
            test_counter += 1
            args, expected = case[:-1], case[-1]
            try:
                if func == "calculate_execution_time":
                    start = time.time()
                    function_to_test[func](*args)
                    elapsed_time = time.time() - start
                    got = round(elapsed_time)
                else:
                    if isinstance(args, tuple):
                        got = function_to_test[func](*args)
                    else:
                        got = function_to_test[func](args)

                if got == expected:
                    passed_tests += 1
                    print(f"Test {test_counter}/{total_tests}: Correct.")
                else:
                    print(f"Test {test_counter}/{total_tests}: Incorrect. Expected: {expected}, Got: {got}")

            except Exception as e:
                print(f"Test {test_counter}/{total_tests}: Error occurred: {e}")

    print(f"Passed {passed_tests} of {total_tests} tests.")


if __name__ == "__main__":
    test_cases = {
        "calculate_execution_time": tests.test_calculate_execution_time(),
        "bubble_sort": tests.test_bubble_sort(),
        "insertion_sort": tests.test_insertion_sort(),
        "fibonacci_recursive": tests.test_fibonacci_recursive()
    }

    functions_to_test = {
        "calculate_execution_time": calculate_execution_time,
        "bubble_sort": bubble_sort,
        "insertion_sort": insertion_sort,
        "fibonacci_recursive": fibonacci_recursive
    }

    run_tests(test_cases, functions_to_test)
