"""Check for anagrams
Problem Description:

You are given two strings s and t. Your task is to determine if string t is an anagram of string s. 
An anagram is a word or phrase formed by rearranging the characters of a different word or phrase, using 
all the original characters exactly once.
"""

def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """

    # if len(t)!=len(s):
    #     return False
    
    # chars = [c for c in s]
    
    # for char in t:
    #     if char in chars:
    #         chars.remove(char)
    #     else:
    #         return False
            
    # return True

    from collections import Counter

    return Counter(s)==Counter(t)

if __name__ == "__main__":
    s = "nagaram"
    t = "anagram"
    print(is_anagram(s,t))
