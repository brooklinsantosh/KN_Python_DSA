""" 
Find the Largest Element in a List
Write a Python function that finds and returns the largest element in a given list of integers.
"""

def find_largest(numbers):
    #return max(numbers)

    if not numbers:
        return None  

    largest = numbers[0]
    for num in numbers:
        if num>largest:
            largest = num
    return largest
