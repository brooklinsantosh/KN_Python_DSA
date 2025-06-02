"""
Problem Description:
You are given two integers, n and m. Your task is to return a rectangle pattern of '*', where n represents 
the number of rows (length) and m represents the number of columns (breadth). 
"""

""" 
Start
    loop through n
    append m times *
    return
End
"""

def generate_rectangle(n, m):
    """
    Function to return a rectangle pattern of '*' with length n and breadth m as a list of strings.
    
    Parameters:
    n (int): The number of rows in the rectangle.
    m (int): The number of columns in the rectangle.
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle pattern.
    """

    return ['*'*m for _ in range(n)]


if __name__ == "__main__":
    generate_rectangle(4,5)