""" 
Hollow Inverted Right Triangle
Problem Description:
You are given an integer n. Your task is to return a hollow inverted right-angled triangle pattern of '*', 
where the first row contains n stars, while the inner rows contain a star at the beginning and end, 
with spaces in between. The triangle should be left-aligned.
"""

def generate_hollow_inverted_right_angled_triangle(n):
    """
    Function to return a hollow inverted right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    res = []
    for i in range(n,0,-1):
        if i==n:
            res.append('*'*n)
        elif i==1:
            res.append('*')
        else:
            res.append('*'+' '* (i-2)+ '*')
    return res

if __name__ == "__main__":
    res = generate_hollow_inverted_right_angled_triangle(4)
    for r in res:
        print(r)