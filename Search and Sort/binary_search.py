from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """
    Performs binary search on a sorted list to find the target element.

    Parameters:
    arr (List[int]): Sorted list of integers.
    target (int): The element to search for.

    Returns:
    int: Index of target if found, else -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # prevents potential overflow in other languages
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 6, 7, 10, 12,13]
    target = 12
    result = binary_search(arr, target)
    print(f"Target {target} found at index {result}" if result != -1 else "Target not found.")
