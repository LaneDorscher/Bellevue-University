# Author: Lane Dorscher
# Date: 12/20/2025

def array_sum(arr):
    """
    Calculate and return the sum of elements in an array 'arr'.
    """

    sum = 0
    for num in arr:
        # if (not isinstance(num, (int, float))) ## since it's not asked of the assignment, I commented it out. But this would prevent addition of non numeric values
        #     continue
        sum += num
    return sum

def find_middle_node(linked_list):
    """
    Find and return the middle node of a singly linked list.
    If the list has an even number of nodes, return the second middle node.
    """

    slow = linked_list
    fast = linked_list

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow

def remove_duplicates_from_sorted_array(arr):
    """
    Given a sorted array, remove the duplicates in-place such that each element appears only once.
    Return the new length of the array.
    """

    if len(arr) == 0: 
        return 0
    
    write_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[write_index] = arr[i]
            write_index += 1
    
    return write_index
