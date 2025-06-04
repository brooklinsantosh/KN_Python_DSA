""" 
Find Maximum Difference Between Two Consecutive Elements (Brute Force Approach)

You are given a list of integers. Write a Python program to find the maximum difference between 
two consecutive elements in the list using a brute-force approach. The difference is defined as the 
absolute value of the difference between two consecutive elements.
"""

def max_consecutive_difference(lst):
    max_diff = 0
    for i in range(len(lst)-1):
        if abs(lst[i]-lst[i+1]) > max_diff:
            max_diff = abs(lst[i]-lst[i+1])

    return max_diff

if __name__ == "__main__":
    print(max_consecutive_difference([1, 7, 3, 10, 5]))