# ----------------------------------------------------------
# Filename: tests.py
# Author: OpenAI
# ----------------------------------------------------------

def test_longest_common_subsequence():
    cases = [
        ("ABCDGH", "AEDFHR", "ADH"),    # Test 1
        ("AGGTAB", "GXTXAYB", "GTAB"),  # Test 2
        ("", "AEDFHR", ""),             # Test 3
        ("ABCDGH", "", ""),             # Test 4
        ("ABC", "ABC", "ABC"),          # Test 5
        ("ABCDEFGH", "IJKLMNOP", ""),   # Test 6
        ("XMJYAUZ", "MZJAWXU", "MJAU"), # Test 7
        ("A", "A", "A"),                # Test 8
        ("B", "A", ""),                 # Test 9
        ("ABCDE", "ACE", "ACE")         # Test 10
    ]
    return cases

def test_knapsack():
    cases = [
        ([10, 20, 30], [60, 100, 120], 50, 220),   # Test 11
        ([], [], 50, 0),                          # Test 12
        ([10, 20, 30], [60, 100, 120], 0, 0),     # Test 13
        ([5, 4, 6, 3], [10, 40, 30, 50], 10, 90), # Test 14
        ([4, 5, 1], [1, 2, 3], 4, 3),             # Test 15
        ([5, 3, 4, 2], [60, 50, 70, 30], 5, 80),  # Test 16
        ([1, 3, 4, 5], [10, 40, 50, 70], 8, 110)  # Test 17
    ]
    return cases

def test_coin_change():
    cases = [
        ([1, 2, 5], 11, 3),  # Test 18
        ([3, 4, 5], 8, 2),  # Test 19
        ([7, 10, 25], 18, -1),  # Test 20
        ([1, 2, 3], 4, 2),      # Test 21
        ([2], 3, -1),           # Test 22
        ([1], 0, 0),            # Test 23
        ([1, 2, 5], 11, 3),     # Test 24
        ([1, 5, 7, 10], 18, 3)  # Test 25
    ]
    return cases
