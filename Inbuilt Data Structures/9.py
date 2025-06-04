""" 
Rotate a List (Without Slicing)
You are given a list of integers and an integer k. Write a Python function to rotate the list to the right 
by k positions without using slicing. A rotation shifts elements from the end of the list to the front.
"""

def rotate_list(lst, k):
    # res = []
    # start_idx = len(lst)-k
    # for _ in range(len(lst)):
    #     res.append(lst[start_idx])
    #     if start_idx!= len(lst)-1:
    #         start_idx+=1
    #     else:
    #         start_idx =0
    # return res
    if not lst:
        return []
    
    # Modulo to handle the case where k is greater than the length of the list
    k = k % len(lst)
    
    # Brute force approach using loops
    for _ in range(k):
        last_element = lst.pop()  # Remove the last element
        lst.insert(0, last_element)  # Insert it at the front
        print(lst)
    
    return lst

if __name__ == "__main__":
    print(rotate_list([1, 2, 3, 4, 5],2))