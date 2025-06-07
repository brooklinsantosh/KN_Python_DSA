""" 
Reverse a string
Problem Description:

You are given a string s. Your task is to return the reversed version of the string.
"""

def reverse_string(s):
    """
    Function to return the reversed version of the input string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    res = ""
    for i in range(len(s)):
        res= s[i]+res 
    return res

if __name__ == "__main__":
    print(reverse_string("hello"))
