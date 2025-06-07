""" 
Count words in a string
Problem Description:

You are given a string s. Your task is to count the number of words in the string and return the total count. A word is defined 
as a sequence of characters separated by spaces.
"""

def count_words(s):
    """
    Function to count the number of words in the input string.
    
    Parameters:
    s (str): The input string to check for words.
    
    Returns:
    int: The count of words in the input string.
    """
    # words = s.split(' ')
    # for word in words:
    #     word = ''.join(char for char in word.replace(" ","") if char.isalnum())
    # cleaned = [word for word in words if word ]

    # return len(cleaned)
    count = 0
    in_word = False

    for char in s:
        if char!= ' ':
            if not in_word:
                in_word = True
                count+=1
        else:
            in_word = False

    return count