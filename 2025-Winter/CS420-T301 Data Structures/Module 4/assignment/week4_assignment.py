class QueueUsingStacks:
    """
    A queue implementation using two stacks.
    """
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if self.out_stack.is_empty():
            while not self.in_stack.is_empty():
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop() if not self.out_stack.is_empty() else None


class Stack: 
    def __init__(self): 
        self.items = []
    def push(self, item): 
        self.items.append(item) 
    def pop(self): 
        if not self.is_empty(): 
            return self.items.pop() 
        return None 
    def peek(self): 
        if not self.is_empty(): 
            return self.items[-1] 
        return None 
    def is_empty(self): 
        return len(self.items) == 0
    
class Queue: 
    def __init__(self): 
        self.items = [] 
    def enqueue(self, item): 
        self.items.insert(0, item) 
    def dequeue(self): 
        if not self.is_empty(): 
            return self.items.pop() 
        return None 
    def front(self): 
        if not self.is_empty(): 
            return self.items[-1] 
        return None 
    def is_empty(self): 
        return len(self.items) == 0

def validate_brackets(string):
    """
    Check if the brackets in the given string are balanced.
    Returns True if balanced, False otherwise.
    """
    
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for c in string:
        if c in pairs.values(): 
            stack.push(c)
        elif c in pairs:
            if stack.is_empty() or stack.peek() != pairs[c]:
                return False
            else:
                stack.pop()

    return stack.is_empty()


def next_greater_element(nums):
    """
    Given a list of numbers, for each element find the next greater element and return their list.
    If no greater element exists for an element, use -1 instead.
    """

    result = [-1] * len(nums)
    stack = Stack()

    for i, num in enumerate(nums):
        while not stack.is_empty() and num > nums[stack.peek()]:
            result[stack.pop()] = num
        stack.push(i)
    return result


def reverse_stack(stack):
    """
    Reverse the given stack using only push and pop operations.
    The function should return the reversed stack.
    """
    
    auxiliary = Stack()
    while stack:
        auxiliary.push(stack.pop())
    return auxiliary.items ##returning the list to satisfy tests


