## Author: Lane Dorscher
## Date: 04/29/2026
## Program name: week7_assignment.py

def selection_sort(nums):
    """
    Implement the selection sort algorithm to sort the list 'nums' in ascending order.
    Return the sorted list.
    """
    n = len(nums)
    for i in range(n-1):
        for x in range(i, n):
            if nums[i] > nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
    return nums

def quick_sort(arr):
    """
    Implement the quick sort algorithm to sort the list 'arr' in ascending order.
    Return the sorted list.
    """
    if len(arr) <= 1:      # ← this is mandatory
        return arr
    
    ## Choose a pivot
    pivotElement = sorted([arr[0], arr[len(arr)//2], arr[-1]])[1]

    ## Partition elements
    pivotArr = [[], [], []]  ## 0 = left, 1 = middle, 2 = right
    for element in arr:
        if (element < pivotElement):
            pivotArr[0].append(element) ## capture elements less than the pivot
        elif (element > pivotElement):
            pivotArr[2].append(element) ## capture elements greater than the pivot
        else:
            pivotArr[1].append(element) ## capture the elements sharing a value with the pivot.
    
    return quick_sort(pivotArr[0]) + pivotArr[1] + quick_sort(pivotArr[2])


def binary_search_first_occurrence(arr, x):
    """
    Implement a variation of binary search to find the first occurrence of 'x' in the sorted list 'arr'.
    Return the index of the first occurrence of 'x'. If 'x' is not present in 'arr', return -1.
    """

    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if (arr[mid] == x):
            result = mid
            high = mid - 1
        elif (arr[mid] < x):
            low = mid + 1
        else:
            high = mid - 1
    return result
