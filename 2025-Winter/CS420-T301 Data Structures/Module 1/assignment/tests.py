def test_find_max_min():
    return [
        ([1, 2, 3, 4, 5], (5, 1)), # Test 1
        ([5, 4, 3, 2, 1], (5, 1)), # Test 2
        ([-2, -5, -4], (-2, -5)),  # Test 3
        ([10], (10, 10)), # Test 4
        ([], (None, None)) # Test 5
    ]

def test_check_symmetry():
    return [
        ("racecar", True), # Test 6
        ("python", False), # Test 7
        ("", True), # Test 8
        ("radar", True), # Test 9
        ("data", False) # Test 10
    ]

def test_merge_sorted_lists():
    return [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]), # Test 11
        ([], [1, 2, 3], [1, 2, 3]), # Test 12
        ([1, 2, 3], [], [1, 2, 3]), # Test 13
        ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]), # Test 14
        ([-1, 1], [-2, 2], [-2, -1, 1, 2]) # Test 15
    ]
