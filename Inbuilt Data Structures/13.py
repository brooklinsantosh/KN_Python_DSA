""" 
Check if Tuple is Palindromic

Design a Python function named is_palindromic_tuple to check if a tuple is palindromic, 
meaning it reads the same forwards and backwards.
"""

def is_palindromic_tuple(tup):
    start = 0
    end = len(tup) - 1

    while start<end:
        if tup[start]!=tup[end]:
            return False
        start+=1
        end-=1
    return True

if __name__ == "__main__":
    print(is_palindromic_tuple((1, 2, 3, 2, 1)))