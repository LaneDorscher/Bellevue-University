## Author: Lane Dorscher
## Date: 02/22/2026

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False ## word not found
            node = node.children[ch]
        
        return node.is_end_of_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
