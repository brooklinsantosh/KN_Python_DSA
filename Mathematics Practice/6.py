""" 
Binary to Decimal
Problem Description:

You are given a string binary_str representing a binary number. Your task is to convert this binary string to its corresponding decimal integer. 
Do not use any built-in functions for conversion.
"""

def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    bin = int(binary_str) 
    i = 0
    number = 0
    while bin>0:
        number = number + (bin%10)*(2**i)
        bin = bin//10
        i=i+1
    return number

if __name__ == "__main__":
    print(binary_to_decimal("1101"))