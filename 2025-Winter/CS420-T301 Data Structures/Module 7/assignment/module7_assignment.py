## Author: Lane Dorscher
## Date: 2/8/2026


## Cool learning about how this works directly. I've used Java's HashMap and C#'s Dictionary but to learning the HOW it makes it more efficient is pretty neat.
## Programmers understood that hashing an object to a numeric indicies would potentially create duplicate values so having the key/pair stored in a linked list
## associated with the hashed value makes it much more efficient to search through the key/value pairs having the same hash.


class HashTable:
    def __init__(self, size=100):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        """
        Insert a (key, value) pair into the hash table.
        """
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]): 
            if k == key:
                self.table[index][i] = (key, value)
                return

        self.table[index].append((key, value))

    def get(self, key):
        """
        Retrieve the value associated with the given key.
        """
        index = self._hash(key)

        for k, v in self.table[index]:
            if k == key:
                return v

        # Nothing matched
        return None

    def remove(self, key):
        """
        Remove the (key, value) pair associated with the given key.
        """
        index = self._hash(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return




def is_anagram(s1, s2):
    """
    Check if two strings are anagrams of each other.
    """
    if len(s1) != len(s2):
        return False

    sorted1 = sorted(s1)
    sorted2 = sorted(s2)

    return sorted1 == sorted2
