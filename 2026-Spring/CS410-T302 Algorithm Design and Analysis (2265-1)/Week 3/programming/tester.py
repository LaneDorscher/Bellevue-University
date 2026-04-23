# ----------------------------------------------------------
# Filename: tester.py
# Author: OpenAI
# ----------------------------------------------------------

import tests
from week3_assignment import merge_sort, quick_sort, binary_search

def run_tests(test_cases, function_to_test):
    total_tests = sum(len(test_cases[func]) for func in test_cases)
    test_counter = 0
    passed_tests = 0

    for func in test_cases:
        for case in test_cases[func]:
            test_counter += 1
            args, expected = case[:-1], case[-1]
            try:
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
        "merge_sort": tests.test_merge_sort(),
        "quick_sort": tests.test_quick_sort(),
        "binary_search": tests.test_binary_search()
    }

    functions_to_test = {
        "merge_sort": merge_sort,
        "quick_sort": quick_sort,
        "binary_search": binary_search
    }

    run_tests(test_cases, functions_to_test)
