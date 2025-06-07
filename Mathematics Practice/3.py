""" 
Check for Prime Number
Problem Description:

You are given an integer n. Your task is to check whether the number is prime or not. A prime number is a number greater than 1 that has 
no divisors other than 1 and itself. Return True if the number is prime, and False otherwise.
"""

def is_prime(n):
    """
    Function to check if a number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    import math
    sqrt_n = int(math.sqrt(n))
    if n<2:
        return False
    for i in range(2,sqrt_n+1):
        if n%i==0:
            return False
    return True

if __name__ == "__main__":
    print(is_prime(4))