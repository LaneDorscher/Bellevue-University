import tests
from week7_assignment import *

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
        "selection_sort": tests.test_selection_sort(),
        "quick_sort": tests.test_quick_sort(),
        "binary_search_first_occurrence": tests.test_binary_search_first_occurrence(),
    }

    functions_to_test = {
        "selection_sort": selection_sort,
        "quick_sort": quick_sort,
        "binary_search_first_occurrence": binary_search_first_occurrence,
    }

    run_tests(test_cases, functions_to_test)
