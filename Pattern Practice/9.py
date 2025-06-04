""" 
Problem Description:
You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, represented as a 
list of strings. Floyd's Triangle is a triangular array of natural numbers where the first row contains 1, 
the second row contains 2 and 3, the third row contains 4, 5, and 6, and so on.
"""

def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    res = []
    num = 1
    for i in range(1,n+1):
        text = ''
        for _ in range(i):
            text+= str(num) + ' '
            num+=1
        res.append(text.rstrip())
    return res

if __name__ == "__main__":
    res = generate_floyds_triangle(5)
    for r in res:
        print(r)