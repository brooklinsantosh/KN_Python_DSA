""" 
Remove Duplicates from a List
You are given a list of integers. Write a Python program that removes any duplicate elements from the list 
and returns a new list with only unique elements. The order of elements in the list should be maintained.
"""

def remove_duplicates(lst):
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)

    return unique_list

if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))