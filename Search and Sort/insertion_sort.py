from typing import List

def insertion_sort(lst: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using the Insertion Sort algorithm.

    Parameters:
    lst (List[int]): The list of integers to sort.

    Returns:
    List[int]: The sorted list in ascending order.
    
    Note:
    - This function sorts the list in-place.
    - Insertion Sort is efficient for small or nearly sorted datasets.
    """
    n = len(lst)
    for i in range(1, n):
        curr = lst[i]
        j = i - 1
        
        # Shift elements of the sorted portion that are greater than key
        while j >= 0 and lst[j] > curr:
            lst[j + 1] = lst[j]
            j -= 1
        
        # Insert the key into the correct position
        lst[j + 1] = curr

    return lst


if __name__ == "__main__":
    lst = [64, 34, 25, 12, 22, 90, 11]
    print("Sorted list:", insertion_sort(lst))
