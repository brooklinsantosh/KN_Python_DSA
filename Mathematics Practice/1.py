""" 
Problem Description:

You are given an integer n. Your task is to calculate and return the sum of the first n even natural numbers. 
The even natural numbers are: 2, 4, 6, 8, ...
"""

def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    return sum([i for i in range(2,(n*2)+1,2)])

if __name__ == "__main__":
    print(sum_of_even_numbers(3))