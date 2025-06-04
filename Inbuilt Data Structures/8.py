""" 
Merge Two Sorted Lists
You are given two sorted lists of integers. Write a Python function to merge these two sorted lists into 
one sorted list. The resulting list should also be in non-decreasing order.
"""

def merge_two_sorted_lists(list1, list2):
    pointer1 = 0
    pointer2 = 0
    res = []
    while pointer1 < len(list1) and pointer2 < len(list2):
        if list1[pointer1]<list2[pointer2]:
                res.append(list1[pointer1])
                pointer1 = pointer1+1
        elif list1[pointer1]>list2[pointer2]:
            res.append(list2[pointer2])
            pointer2 = pointer2+1
            
    while pointer1 < len(list1):
        res.append(list1[pointer1])
        pointer1 += 1

    while pointer2 < len(list2):
        res.append(list2[pointer2])
        pointer2 += 1
    
    return res

if __name__ == "__main__":
    print(merge_two_sorted_lists([1, 3, 5],[2, 4, 6]))