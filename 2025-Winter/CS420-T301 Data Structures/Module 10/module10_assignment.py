import random

class SkipNode:
    def __init__(self, level, key):
        self.key = key
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level, probability): 
        """
        Initialize your data structure here.
        """
        self.max_level = max_level
        self.probability = probability
        self.header = SkipNode(self.max_level, -1)
        self.level = 0

    def __randomLevel(self):
        """
        Randomly choose a level for a new node based on probability.
        """
        lvl = 0
        while random.random() < self.probability and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, key):
        """
        Insert a key into the SkipList.
        """

        current = self.header
        update = [None] * (self.max_level + 1)
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        
        new_level = self.__randomLevel()

        if (new_level > self.level):
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.header
            self.level = new_level
        
        new_node = SkipNode(new_level, key)

        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, key):
        """
        Search for a key in the SkipList.
        """
        current = self.header

        for i in range(self.level, -1, -1):
            while current.forward[i] is not None and current.forward[i].key < key:
                current = current.forward[i]

        current = current.forward[0]
        return current is not None and current.key == key

    def delete(self, key):
        """
        Delete a key from the SkipList.
        """

        current = self.header
        update = [None] * (self.max_level + 1)

        # Step 1: Locate the node (track predecessors at each level)
        for i in range(self.level, -1, -1):
            while current.forward[i] is not None and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        # Candidate node is the next node on level 0
        target = current.forward[0]
        if target is None or target.key != key:
            return False  # not found

        # Step 2: Remove the node by updating pointers
        for i in range(self.level + 1):
            if update[i].forward[i] == target:
                update[i].forward[i] = target.forward[i]

        # Step 3: Reduce current level if highest levels are empty
        while self.level > 0 and self.header.forward[self.level] is None:
            self.level -= 1

        return True
            

class SelfAdjustingList:
    def __init__(self):
        self.list = []

    def access(self, key):
        """
        Access an element and adjust its position in the list.
        """
        if key not in self.list:
            return False
        
        self.list.remove(key)
        self.list.insert(0, key)

        return True

    def insert(self, key):
        """
        Insert an element into the list.
        """
        
        if key in self.list:
            self.list.remove(key)
        self.list.insert(0, key)
        
    def delete(self, key):
        """
        Delete an element from the list.
        """

        if key not in self.list:
            return False
        
        self.list.remove(key)