from typing import List

def selection_sort(lst: List[int]) -> List[int]:
    """
    Sorts a list of integers in ascending order using the Selection Sort algorithm.

    Parameters:
    lst (List[int]): The list of integers to be sorted.

    Returns:
    List[int]: The sorted list in ascending order.
    
    Note:
    - This function performs the sort in-place.
    - The returned list is the same object as the input list.
    """
    n = len(lst)
    for i in range(n):
        curr_min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[curr_min_idx]:
                curr_min_idx = j
        lst[i], lst[curr_min_idx] = lst[curr_min_idx], lst[i]
    return lst


if __name__ == "__main__":
    lst = [64, 34, 25, 12, 22, 90, 11]
    print("Sorted list:", selection_sort(lst))
