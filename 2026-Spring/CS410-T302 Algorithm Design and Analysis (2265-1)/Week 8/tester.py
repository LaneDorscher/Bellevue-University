import tests
from week8_assignment import *
import copy

def is_key_in_bst(node, key):
    """
    Helper function to check if a key exists in the BST.
    """
    if not node:
        return False
    if node.val == key:
        return True
    elif key < node.val:
        return is_key_in_bst(node.left, key)
    else:
        return is_key_in_bst(node.right, key)

def run_tests(test_cases, function_to_test):
    total_tests = sum(len(test_cases[func]) for func in test_cases)
    test_counter = 0
    passed_tests = 0

    for func in test_cases:
        for case in test_cases[func]:
            test_counter += 1
            args, expected = case[:-1], case[-1]
            try:
                args_copy = copy.deepcopy(args)
                if func == 'insert_bst':
                    result = function_to_test[func](*args_copy)
                    got = is_key_in_bst(result, args[1])
                else:
                    got = function_to_test[func](*args_copy)

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
        "insert_bst": tests.test_insert_bst(),
        "find_max_heap": tests.test_find_max_heap(),
        "is_full_binary_tree": tests.test_is_full_binary_tree(),
        "get_tree_height": tests.test_get_tree_height()
    }

    functions_to_test = {
        "insert_bst": insert_bst,
        "find_max_heap": find_max_heap,
        "is_full_binary_tree": is_full_binary_tree,
        "get_tree_height": get_tree_height
    }

    run_tests(test_cases, functions_to_test)
