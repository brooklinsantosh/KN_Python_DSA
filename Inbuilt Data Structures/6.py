""" 
Count Even and Odd Numbers in a List
You are given a list of integers. Write a Python program that counts and returns the number of even and odd 
numbers in the list.
"""

def count_even_odd(lst):
    even_count = odd_count = 0
    for num in lst:
        if num%2 == 0:
            even_count+=1
        else:
            odd_count+=1

    return (even_count, odd_count)

if __name__ == "__main__":
    print(count_even_odd([1, 2, 3, 4, 5]))