""" 
Check if a List is a Subset of Another List (Brute Force Approach)

You are given two lists of integers. Write a Python program that checks whether the first list is a subset of the second list 
using a brute-force approach, without using the in keyword. A list is considered a subset if all elements of the first list are present 
in the second list.
"""

def is_subset(lst1, lst2):
    res = True
    for l1 in lst1:
        for l2 in lst2:
            if l1==l2:
                res = True
                break    
            else:
                res = False
    
    return res

if __name__ == "__main__":
    print(is_subset(lst1 = [1, 2, 3], lst2 = [1, 2, 3, 4, 5]))