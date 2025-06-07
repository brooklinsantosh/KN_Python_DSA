""" 
GCD of Two Numbers
Problem Description:

You are given two integers n and m. Your task is to find the GCD of these two numbers. The GCD is the largest positive integer that 
divides both numbers without leaving a remainder. Do not use any built-in functions and do not use recursion.
"""

def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD of n and m.
    """
    if n<m:
        n,m = m,n
    while m>0:
        n,m = m, n%m
    return n

if __name__ == "__main__":
    print(gcd(56,98))
