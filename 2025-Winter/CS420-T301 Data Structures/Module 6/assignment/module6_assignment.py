class MinHeap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heap = []

    def insert(self, element):
        """
        Inserts an element into the heap.
        """
        self.heap.append(element)
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self):
        """
        Removes and returns the minimum element from the heap.
        """
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        # Swap first and last elements
        temp = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap[-1] = temp

        min_value = self.heap.pop()

        # Restore min-heap property starting from root
        self._bubble_down(0)
        return min_value

    def get_min(self):
        """
        Returns the minimum element from the heap without removing it.
        """
        if not self.heap:
            return None
        return self.heap[0]

    # ---------- Helper Methods ----------

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2

        while index > 0 and self.heap[index] < self.heap[parent_index]:
            
            temp = self.heap[index]
            self.heap[index] = self.heap[parent_index]
            self.heap[parent_index] = temp

            index = parent_index
            parent_index = (index - 1) // 2

    def _bubble_down(self, index):
        size = len(self.heap)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            temp = self.heap[index]
            self.heap[index] = self.heap[smallest]
            self.heap[smallest] = temp

            
            index = smallest


def find_kth_largest(nums, k):
    min_heap = MinHeap()

    for num in nums:
        min_heap.insert(num)         
        if len(min_heap.heap) > k:   
            min_heap.extract_min()  

    return min_heap.get_min() if min_heap.heap else None
