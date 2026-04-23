class DynamicArray:
    def __init__(self):
        self.array = [None] * 1 
        self.count = 0
        self.capacity = 1

    def add(self, item):
        """
        Add item to the dynamic array.
        """
        if self.count == self.capacity:
            self._resize(2 * self.capacity)  

        self.array[self.count] = item
        self.count += 1

    def get(self, index):
        """
        Get the item at the specified index.
        """
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")
        
        return self.array[index]

    def remove(self, index):
        """
        Remove the item at the specified index.
        """
        if index < 0 or index >= self.count:
            raise IndexError("Index out of bounds")

        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]

        self.count -= 1

    def _resize(self, new_capacity):
        """
        Resize the internal array to the new capacity.
        """
        new_array = [None] * new_capacity
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity 


class DisjointSet:
    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.array = [i for i in range(size)]

    def find(self, x):
        """
        Find the root of the set in which element x is present.
        """
        if self.array[x] != x:
            self.array[x] = self.find(self.array[x])
        return self.array[x]

    def union(self, x, y):
        """
        Perform the union of two sets in which elements x and y are present.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.array[root_x] = root_y

class BloomFilter:
    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.bit_array = [0] * size

    def _hash1(self, item):
        return hash(str(item)) % self.size

    def _hash2(self, item):
        return hash("salt1" + str(item)) % self.size

    def _hash3(self, item):
        return hash("salt2" + str(item)) % self.size

    def add(self, item):
        """
        Add an item to the Bloom Filter.
        """
        indexes = [self._hash1(item), self._hash2(item), self._hash3(item)]
        for index in indexes:
            self.bit_array[index] = 1

    def check(self, item):
        """
        Check if an item is present in the Bloom Filter.
        """
        indexes = [self._hash1(item), self._hash2(item), self._hash3(item)]
        for index in indexes:
            if self.bit_array[index] == 0:
                return False
        return True