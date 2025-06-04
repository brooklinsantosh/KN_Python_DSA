""" 
Sandglass Pattern
Problem Description:
You are given an integer n. Your task is to return a sandglass pattern of '*', where the first row contains 
2n - 1 stars and each subsequent row decreases the number of stars by 2, until the last row contains a 
single star. After reaching the smallest width, the pattern then continues with the same number of stars 
increasing back to 2n - 1. The stars in each row should be centered.
"""

def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    upper_part = [' '*(i) + '*'*(((2*n)-1)-(i*2)) + ' '*(i) for i in range(n)]
    lower_part = [' '*(n-1-i)+'*'*(1+(i*2))+' '*(n-1-i) for i in range(1,n)]
    return upper_part + lower_part


if __name__ == "__main__":
    res = generate_sandglass(5)
    for r in res:
        print(r)