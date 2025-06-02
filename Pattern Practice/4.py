""" 
Problem Description:

You are given an integer n. Your task is to return a right-angled triangle pattern of '*' where each side 
has n characters, represented as a list of strings. The triangle has '*' characters, starting with 1 star 
in the first row, 2 stars in the second row, and so on until the last row has n stars.
"""

def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """

    return ['*'*i for i in range(1, n+1)]

if __name__ == "__main__":
    print(generate_triangle(3))