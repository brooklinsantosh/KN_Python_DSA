from typing import List

def bubble_sort(lst: List[int]) -> List[int]:
    """
    Sorts a list using the Bubble Sort algorithm.

    Parameters:
    lst (List[int]): The list to sort.

    Returns:
    List[int]: The sorted list.
    """
    n = len(lst)
    for i in range(n - 1):
        # print(f"Pass: {i+1}")
        swapped = False  # Optimization: track if any swaps occurred
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
            # print(f"Iteration: {j+1}, lst: {lst}")
        if not swapped:
            break  # List is already sorted
    return lst

if __name__ == "__main__":
    lst = [64, 34, 25, 12, 22, 90, 11]
    print("Sorted list:", bubble_sort(lst))
