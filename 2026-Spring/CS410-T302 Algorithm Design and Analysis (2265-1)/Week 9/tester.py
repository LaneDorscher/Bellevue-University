import tests
from week9_assignment import *


def run_tests(test_cases, function_to_test):
    total_tests = sum(len(test_cases[func]) for func in test_cases)
    test_counter = 0
    passed_tests = 0

    for func in test_cases:
        for case in test_cases[func]:
            test_counter += 1
            args, expected = case[:-1], case[-1]
            try:
                if func == 'trie_insert':
                    root, key = args
                    function_to_test[func](root, key)
                    got = root
                else:
                    got = function_to_test[func](*args)

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
        "naive_string_matching": tests.test_naive_string_matching(),
        "rabin_karp": tests.test_rabin_karp(),
        "kmp_pattern_preprocessing": tests.test_kmp_pattern_preprocessing(),
        "trie_insert": tests.test_trie_insert(),
    }

    functions_to_test = {
        "naive_string_matching": naive_string_matching,
        "rabin_karp": rabin_karp,
        "kmp_pattern_preprocessing": kmp_pattern_preprocessing,
        "trie_insert": trie_insert,
    }

    run_tests(test_cases, functions_to_test)
