# ----------------------------------------------------------
# Filename: tester.py
# Author: OpenAI
# ----------------------------------------------------------

import tests
from week4_assignment import *


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
        "longest_common_subsequence": tests.test_longest_common_subsequence(),
        "knapsack": tests.test_knapsack(),
        "coin_change": tests.test_coin_change()
    }

    functions_to_test = {
        "longest_common_subsequence": longest_common_subsequence,
        "knapsack": knapsack,
        "coin_change": coin_change
    }

    run_tests(test_cases, functions_to_test)
