""" 
Right Angled Triangle II
Problem Description:
You are given an integer n. Your task is to return a right-angled triangle pattern of '*', where each row 
contains stars aligned to the right. The first row has one star, the second row has two stars, and so on, 
until the nth row has n stars.
"""

def generate_right_angled_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    return [' '*(n-i) + '*'*i for i in range(1, n+1)]

if __name__ == "__main__":
    res = generate_right_angled_triangle(5)
    for r in res:
        print(r)