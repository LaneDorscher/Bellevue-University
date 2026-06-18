## Author: Lane Dorscher
## Date: 05/13/2026

def naive_string_matching(text, pattern):
    """
    Implement the naive string matching algorithm.
    Return the starting indices of all occurrences of the pattern in the text.
    """
    list = []

    for i in range(0, len(text) - len(pattern) + 1): # add 1 to include 1st character of pattern
        if (text[i:i+len(pattern)] == pattern):
            list.append(i)
    return list

def rabin_karp(text, pattern, d, q):
    """
    Implement the Rabin-Karp string matching algorithm.
    'd' is the number of characters in the input alphabet, and 'q' is a prime number.
    Return the starting indices of all occurrences of the pattern in the text.
    """
    n = len(text)
    m = len(pattern)
    h = pow(d, (m-1), q)
    p=0
    t=0
    occurrences = []

    # create initial hash of pattern and beginning window
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    
    for s in range(n-m+1): ## add 1 to include first character of pattern
        if (p==t):
            is_match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    is_match = False
                    break
            if is_match:
                occurrences.append(s)
        # next window hash
        if s < n - m:
            t = (t - h * ord(text[s])) % q
            t = (t * d + ord(text[s+m])) % q
            t = (t + q) % q
    return occurrences

def kmp_pattern_preprocessing(pattern):
    """
    Preprocess the pattern for the KMP string matching algorithm.
    Return the lps (longest proper prefix which is also a suffix) array.
    """
    n = len(pattern)
    lps = [0] * n
    length = 0
    i = 1

    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def trie_insert(root, key):
    """
    Insert 'key' into the trie rooted at 'root'.
    """
    currentNode = root
    for c in key:
        if c not in currentNode:
            currentNode[c] = {}
        currentNode = currentNode[c]
    currentNode["end_of_word"] = True
    
