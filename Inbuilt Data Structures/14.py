""" 
Merge Dictionaries with Overlapping Keys

Design a Python function named merge_dicts_with_overlapping_keys that merges multiple dictionaries into a single dictionary. 
If a key appears in more than one dictionary, sum up their values.
"""

def merge_dicts_with_overlapping_keys(dicts):
    res = {}
    for dict in dicts:
        for key, val in dict.items():
            if key not in res:
                res[key] = val
            else:
                res[key] = res[key]+val

    return res

if __name__ == "__main__":
    dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
    print(merge_dicts_with_overlapping_keys(dicts))