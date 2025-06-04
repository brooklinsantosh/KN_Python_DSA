""" 
Check if All Elements in a List are Unique
You are given a list of integers. Write a Python program that checks if all elements in the list are unique. 
If all elements are unique, return True; otherwise, return False.
"""

def check_unique(lst):
    unique_list = []
    for num in lst:
        if num in unique_list:
            return False
        unique_list.append(num)

    return True

if __name__ == "__main__":
    print(check_unique([1, 2, 3, 4, 5]))