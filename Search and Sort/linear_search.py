from typing import List

def linear_search(arr: List[int], target: int) -> int:
    """
    Performs a linear search on the given list for the target value.

    Parameters:
    arr (List[int]): The list to search through.
    target (int): The value to search for.

    Returns:
    int: The index of the target if found, else -1.
    """
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1
