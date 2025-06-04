""" 
Merge Lists to Dictionary
Design a Python function named merge_lists_to_dictionary to merge two lists into a dictionary where elements from the first list act as keys and elements from the second list act as values.
"""

def merge_lists_to_dictionary(keys, values):
    res = {}
    if len(values)!=len(keys):
        return False
    for key,val in zip(keys,values):
        res[key]=val
    return res
        

if __name__ == "__main__":
    print(merge_lists_to_dictionary(['key1', 'key2'],[100]))      