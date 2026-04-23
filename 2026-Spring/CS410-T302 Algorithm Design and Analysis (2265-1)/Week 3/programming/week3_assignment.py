# ----------------------------------------------------------
# Filename: week3_assignment.py
# Author: Lane Dorscher
# Date: 04/03/2026
# ----------------------------------------------------------

def merge_sort(arr):
    """
    Sort 'arr' using the merge sort algorithm and return the sorted array.
    """
    
    if (len(arr) <= 1):
        return arr
    
    mid_index = len(arr) // 2
    first_half = merge_sort(arr[:mid_index])
    second_half = merge_sort(arr[mid_index:])
    
    sorted_list = []
    i = 0
    j = 0
    
    while (i < len(first_half) and j < len(second_half)):
        if first_half[i] < second_half[j]:
            keyToAppend = first_half[i]
            i += 1
        else:
            keyToAppend = second_half[j]
            j += 1
        sorted_list.append(keyToAppend)
       
    ## add anything left over 
    sorted_list += second_half[j:]
    sorted_list += first_half[i:]
    
    return sorted_list
    

def quick_sort(arr):
    """
    Sort 'arr' using the quick sort algorithm and return the sorted array.
    """
    
    if len(arr) <= 1:
        return arr
       
    pivot = arr[len(arr) // 2]
    pivotArr = [] ## assignment said pick an element but there could be more than 1 element with the same value, this will capture them.
    p1 = []
    p2 = []
    
    for element in arr:
        if (element < pivot):
            p1.append(element)
        elif (element > pivot):
            p2.append(element)
        else: 
            ## capture elements with the SAME value as the pivot (no need to sort them)
            pivotArr.append(element)
    
    return quick_sort(p1) + pivotArr + quick_sort(p2)

def binary_search(arr, x):
    """
    Find 'x' in sorted 'arr' using binary search. Return the index of 'x', or -1 if not found.
    """
    
    ## assumes array is pre-sorted
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if (arr[mid] == x):
            return mid
        elif (arr[mid] < x):
            low = mid + 1
        else: 
            high = mid - 1
            
    return -1
    
    
    
    
    
