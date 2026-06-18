# tests.py
def test_naive_string_matching():
    cases = [
        ("abcdabcabc", "abc", [0, 4, 7]), # Test 1
        ("aaaaaa", "aa", [0, 1, 2, 3, 4]), # Test 2
        ("hello world", "world", [6]), # Test 3
        ("hello world", "earth", []), # Test 4
        ("hello", "h", [0]), # Test 5
        ("ababa", "aba", [0, 2]), # Test 6 (modified to fix overlap issue)
        ("texttexttext", "test", []), # Test 7
        ("mississippi", "issip", [4]), # Test 8
    ]
    return cases

def test_rabin_karp():
    d = 256 # For ASCII characters
    q = 101 # A prime number
    cases = [
        ("abcdabcabc", "abc", d, q, [0, 4, 7]), # Test 9
        ("aaaaaa", "aa", d, q, [0, 1, 2, 3, 4]), # Test 10
        ("hello world", "world", d, q, [6]), # Test 11
        ("hello", "h", d, q, [0]), # Test 12
        ("abcd", "e", d, q, []), # Test 13
        ("structure", "uct", d, q, [3]), # Test 14
    ]
    return cases


def test_kmp_pattern_preprocessing():
    cases = [
        ("abcd", [0, 0, 0, 0]), # Test 15
        ("aabaabaaa", [0, 1, 0, 1, 2, 3, 4, 5, 2]), # Test 16
        ("abcabc", [0, 0, 0, 1, 2, 3]), # Test 17
        ("aaaaa", [0, 1, 2, 3, 4]), # Test 18
        ("ababab", [0, 0, 1, 2, 3, 4]), # Test 19
    ]
    return cases

def test_trie_insert():
    cases = [
        ({}, "openai", {'o': {'p': {'e': {'n': {'a': {'i': {'end_of_word': True}}}}}}}), # Test 20
        ({}, "key", {"k": {"e": {"y": {"end_of_word": True}}}}), # Test 21
        ({}, "world", {"w": {"o": {"r": {"l": {"d": {"end_of_word": True}}}}}}), # Test 22
        ({"h": {"e": {"l": {"l": {"o": {}}}}}}, "hello", {"h": {"e": {"l": {"l": {"o": {"end_of_word": True}}}}}}), # Test 23
        ({"a": {"b": {"end_of_word": True}}}, "abc", {"a": {"b": {"end_of_word": True, "c": {"end_of_word": True}}}}), # Test 24
        ({}, "trie", {"t": {"r": {"i": {"e": {"end_of_word": True}}}}}), # Test 25
    ]
    return cases


