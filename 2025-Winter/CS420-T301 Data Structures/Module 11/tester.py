# ----------------------------------------------------------
# Filename: tester.py
# Authors: Nasheb Ismaily [v1], Rob Flowers [v2]
# ----------------------------------------------------------

import tests
from module11_assignment import *

def run_tests_dyn():
    total_tests = passed_tests = 0

    print(f"\nTesting Dynamic Array...")

    for result, expected, message in tests.test_dynamic_array():
        total_tests += 1
        try:
            assert result == expected
            print(f"Test {total_tests}: Correct. ({message})")
            passed_tests += 1
        except AssertionError:
            print(f"Test {total_tests}: Incorrect. Expected: {expected}, Got: {result} ({message})")

    print(f"Passed {passed_tests} of {total_tests} tests.")


def run_tests_disjoint():
    total_tests = passed_tests = 0

    print(f"\nTesting Disjoint Set and Bloom Filter...")

    for result, expected, message in tests.test_disjoint_set() + tests.test_bloom_filter():
        total_tests += 1
        try:
            assert result == expected
            print(f"Test {total_tests}: Correct. ({message})")
            passed_tests += 1
        except AssertionError:
            print(f"Test {total_tests}: Incorrect. Expected: {expected}, Got: {result} ({message})")

    print(f"Passed {passed_tests} of {total_tests} tests.")


if __name__ == "__main__":
    run_tests_dyn()
    run_tests_disjoint()
