""" 
Count Vowels in a string
Problem Description:

You are given a string s. Your task is to count the number of vowels (both uppercase and lowercase) in the 
string and return the total count.
"""

def count_vowels(s: str):
    """
    Function to count the number of vowels in the input string.
    
    Parameters:
    s (str): The input string to check for vowels.
    
    Returns:
    int: The count of vowels in the input string.
    """
    vowels = ['a','e','i','o','u']
    vowels_count = 0
    for char in s.lower():
        if char in vowels:
            vowels_count+=1
    return vowels_count
