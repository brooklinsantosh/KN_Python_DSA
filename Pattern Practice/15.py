""" 
Number Pyramid Pattern
Problem Description:
You are given an integer n. Your task is to return a pyramid pattern of numbers, where each row contains 
increasing numbers starting from 1 up to the row number, and the pyramid is centered with leading spaces.
"""

def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    res = []
    for i in range(1,n+1):
        res.append(' '*(n-i)+' '.join([str(j) for j in range(1,i+1)])+' '*(n-i))
    return res


if __name__ == "__main__":
    res = generate_number_pyramid(4)
    for r in res:
        print(r)