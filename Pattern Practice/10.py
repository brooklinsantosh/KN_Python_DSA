""" 
Problem Description:
You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part 
(the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. 
Each row should be centered with appropriate spaces.
"""

def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    upper_part = [' '*(n-1-i)+'*'*(1+(i*2))+' '*(n-1-i) for i in range(n-1)]
    middle_part = ['*'*((2*n)-1)]
    lower_part = upper_part[::-1]

    return upper_part+middle_part+lower_part

if __name__ == "__main__":
    res = generate_diamond(5)
    for r in res:
        print(r)