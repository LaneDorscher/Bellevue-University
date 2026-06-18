import tests
from week10_assignment import *
import traceback

def run_tests(test_cases, function_to_test):
    total_tests = sum(len(test_cases[func]) for func in test_cases)
    test_counter = 0
    passed_tests = 0

    for func in test_cases:
        for case in test_cases[func]:
            test_counter += 1
            args, expected = case[:-1], case[-1]
            try:
                got = function_to_test[func](*args)
                if got == expected:
                    passed_tests += 1
                    print(f"Test {test_counter}/{total_tests}: Correct.")
                else:
                    print(f"Test {test_counter}/{total_tests}: Incorrect. Expected: {expected}, Got: {got}")

            except Exception as e:
                print(f"Test {test_counter}/{total_tests}: Error occurred: {e}")
               ## print(f"  -> Link: {traceback.format_exc()}")

    print(f"Passed {passed_tests} of {total_tests} tests.")


if __name__ == "__main__":
    test_cases = {
        "ford_fulkerson": tests.test_ford_fulkerson(),
    }

    functions_to_test = {
        "ford_fulkerson": ford_fulkerson,
    }

    run_tests(test_cases, functions_to_test)
