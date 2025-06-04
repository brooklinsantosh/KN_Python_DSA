""" 
Problem Description:

You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows, 
represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the 
second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.
"""

def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    return [' '*(n-1-i)+'*'*(1+(i*2))+' '*(n-1-i) for i in range(n)]

if __name__ == "__main__":
    res = generate_pyramid(5)
    for r in res:
        print(r)