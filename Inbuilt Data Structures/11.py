""" 
Merge Three Dictionaries

Design a Python function named merge_three_dictionaries to merge exactly three dictionaries into one.
"""

def merge_three_dictionaries(dict1, dict2, dict3):
    return dict1 | dict2 | dict3

if __name__ == "__main__":
    print(merge_three_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})) 