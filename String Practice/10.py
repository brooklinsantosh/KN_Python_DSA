""" 
Check for Substring
Problem Description:

You are given two strings, s and t. Your task is to determine if the string t is a substring of the string s. 
A substring is a contiguous sequence of characters within a string. Do not use any built-in functions for 
string operations and do not use recursion.
"""

def is_substring(s, t):
    """
    Function to check if string t is a substring of string s without using built-in functions and recursion.
    
    Parameters:
    s (str): The main string.
    t (str): The string to check as a substring.
    
    Returns:
    bool: True if t is a substring of s, False otherwise.
    """
    # if s==t:
    #     return True
    i = 0
    while i<len(s)-len(t)+1:
        print(s[i:i+len(t)])
        if s[i:i+len(t)]==t:
            return True
        i+=1
    return False

if __name__ == "__main__":
    s = "hello world" 
    t = "world"
    print(is_substring(s,t))