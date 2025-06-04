""" 
Hollow Right Triangle
Problem Description:
You are given an integer n. Your task is to return a hollow right-angled triangle pattern of '*', where the 
first and last rows contain stars, while the inner rows contain a star at the beginning and end, with spaces 
in between. The triangle should be right-aligned.
"""

def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    if n==1:
        return ['*']
    first_row = ['*']
    hollow_rows = ['*'+' '*(i-1)+'*' for i in range(1,n-1)]
    last_row = ['*'*n]
    return first_row + hollow_rows + last_row

if __name__ == "__main__":
    res = generate_hollow_right_angled_triangle(1)
    for r in res:
        print(r)
