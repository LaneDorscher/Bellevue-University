def test_sum_of_squares():
    return [
        ([1, 2, 3], 14),          # Test 1
        ([], 0),                  # Test 2
        ([-1, -2, -3], 14),       # Test 3
        ([4, 5], 41),             # Test 4
        ([0], 0)                  # Test 5
    ]

def test_string_reversal():
    return [
        ("hello", "olleh"),       # Test 6
        ("", ""),                 # Test 7
        ("a", "a"),               # Test 8
        ("Python", "nohtyP"),     # Test 9
        ("data", "atad")          # Test 10
    ]

def test_find_second_largest():
    return [
        ([1, 3, 4, 5], 4),        # Test 11
        ([5, 4, 3, 2, 1], 4),           # Test 12
        ([1], None),              # Test 13
        ([], None),               # Test 14
        ([2, 3], 2),              # Test 15
        ([-2, -1, -3], -2),       # Test 16

        ([2, 2,2,2,2], None)         # Test 17

    ]
