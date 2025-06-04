""" 
Problem Description
You are given an integer n. Your task is to return an inverted pyramid pattern of '*', where each side 
has n rows, represented as a list of strings. The first row has 2n - 1 stars, the second row has 2n - 3 stars, 
and so on, until the last row has 1 star, with each row centered using spaces.
"""

def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    return [' '*(n-1-i)+'*'*(1+(i*2))+' '*(n-1-i) for i in range(n-1,-1,-1)]

if __name__ == "__main__":
    res = generate_inverted_pyramid(5)
    for r in res:
        print(r)