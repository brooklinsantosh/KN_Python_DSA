""" 
Decimal to Binary
Problem Description:

You are given an integer n. Your task is to return its binary representation as a string. Do not use any built-in functions for conversion.
"""

def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    if n==0:
        return '0'
    bin = ''
    sign = '-' if n<0 else ''
    n=abs(n)
    while n>0:
        bin = str(n%2) + bin
        n=n//2
    return sign+bin

if __name__ == "__main__":
    print(int_to_binary(0))
