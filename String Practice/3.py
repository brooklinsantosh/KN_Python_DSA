""" 
Check for same strings
Problem Description:

You are given two strings s and t. Your task is to check if the two strings are equal. Two strings are 
considered equal if they have the same length and the same characters at each position. You are not allowed 
to use any built-in string comparison functions.
"""

def are_equal_strings(s, t):
    """
    Function to check if two strings are equal without using built-in functions.
    
    Parameters:
    s (str): The first string.
    t (str): The second string.
    
    Returns:
    bool: True if the strings are equal, False otherwise.
    """
    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        if s[i]!= t[i]:
            return False
        
    return True