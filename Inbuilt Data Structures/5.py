""" 
Reverse a List (Non-Slicing Approach)
You are given a list of integers. Write a Python program that reverses the list 
without using slicing (lst[::-1]). The program should return the reversed list.
"""

def reverse_list(lst):
    # list comprehension
    # time complexity O(n)
    # return [lst[i] for i in range(len(lst)-1, -1, -1)]

    # Two pointer approach
    start = 0
    end = len(lst)-1

    while start<end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst

if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4, 5]))