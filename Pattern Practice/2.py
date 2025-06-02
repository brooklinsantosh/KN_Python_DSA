"""
    Problem Description:
    You are given an integer n. Your task is to return a hollow square pattern of size n x n made up 
    of the character '*', represented as a list of strings. The hollow square has '*' on the border, 
    and spaces ' ' in the middle (except for side lengths of 1 and 2).
"""


""" 
Start
    loop through n
    if first and last interation
        print '*' * n
    else 
        create ' ' * n and repace the first and last index with *
    append the string to list
    return the created list
End
"""

def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    res = []
    for i in range(n):
        if i==0 or i==n-1:
            res.append('*'*n)
        else:
            res.append(''.join('*' + ' ' * (n - 2) + '*'))
    return res

if __name__ == "__main__":
    print(generate_hollow_square(5))