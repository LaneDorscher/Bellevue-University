import time

def calculate_execution_time(func, *args):
    """
    Calculate and return the time taken for function 'func' to execute with arguments '*args'.
    """

    start_time = time.time() ## Record the start time 
    func(*args) ## execute function passing in the arguments
    end_time = time.time()  ##record the end time

    execution_time = end_time - start_time  ## calculate difference to get total time of execution
    return execution_time 

def bubble_sort(nums):
    """
    Sort the list 'nums' using the bubble sort algorithm. Return the sorted list.
    """
    n = len(nums)

    for i in range(n): ## for each outer pass, the largest value has bubbled up to the end
        for j in range(0, n - i - 1):   ## therefore the next inner pass doesn't need to check it again
            if nums[j] > nums[j + 1]:  ##if value at index is greater than the next one, swap them
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def insertion_sort(nums):
    """
    Sort the list 'nums' using the insertion sort algorithm. Return the sorted list.
    """
    for i in range(1, len(nums)):
        key = nums[i]       # value to insert into sorted list
        j = i - 1           # previous value in list to compare the key to

        # Shift elements to the right until the correct position for the key is found
        while j >= 0 and key < nums[j]:  
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key   ## insert our key to the right position in the sorted list

    return nums

def fibonacci_recursive(n):
    """
    Return the nth Fibonacci number using a recursive approach.
    """
    if n == 0:      ## safeguard for zero values, return 0
        return 0
    elif n == 1:    ## safeguard against 1 values, returning 1
        return 1
    else:  ##perform the recurstive sum of the pervious 2 numbers
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)