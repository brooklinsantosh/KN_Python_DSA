""" 
Problem Description:

You are given an integer n. Your task is to return a right-angled triangle pattern where each row contains 
repeated digits. The first row contains the number 1 repeated once, the second row contains the number 2 
repeated twice, and so on until the nth row contains the number n repeated n times.
"""

def generate_number_triangle(n):
    """
    Function to return a right-angled triangle of repeated numbers of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    return [f'{i}'*i for i in range(1,n+1)]

if __name__ == "__main__":
    res = generate_number_triangle(5)
    for r in res:
        print(r)