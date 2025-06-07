""" 
Check Palindrome
Problem Description:

You are given a string s. Your task is to check if the string is a palindrome. A string is considered 
a palindrome if it reads the same forward and backward, ignoring spaces, punctuation, and case.
"""

def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    cleaned = ''.join(c for c in s.lower() if c.isalnum())
    left = 0
    right = len(cleaned)-1
    while left<right:
        if cleaned[left]!=cleaned[right]:
            return False
        left+=1
        right-=1
    return True

if __name__ == "__main__":
    print(is_palindrome("A man a plan a canal Panama"))