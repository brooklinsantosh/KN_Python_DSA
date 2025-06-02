"""
Problem Description: You are given an integer n. Your task is to return a square pattern of size n x n 
made up of the character '*', represented as a list of strings.
"""

def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # res = []
    # for _ in range(n):
    #     res.append('*' * n)
    # return res

    #Simplified version
    return ['*' * n for _ in range(n)]


if __name__ == "__main__":
    print(generate_square(3))