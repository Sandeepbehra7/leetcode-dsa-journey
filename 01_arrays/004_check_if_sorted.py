"""
Problem: Check if Array is Sorted

Given a list of integers, determine if the array is sorted
in non-decreasing (ASC) or non-increasing (DESC) order.

Example:
Input:  [1, 2, 2, 3]
Output: True (ASC)

Approach 1: Iterative Check (Optimal)
    - Compare adjacent elements
    - Exit early if order is violated
    - Time Complexity: O(n)
    - Space Complexity: O(1)

Approach 2: Using Sorting (Not Optimal)
    - Compare with sorted version
    - Time Complexity: O(n log n)
    - Space Complexity: O(n)

Edge Cases:
    - Empty list → True
    - Single element → True
    - Duplicate elements allowed
"""


# Approach 1 (Optimal)
def is_sorted(arr, order="ASC"):
    """
    Checks if array is sorted.

    :param arr: List[int]
    :param order: "ASC" or "DESC"
    :return: bool
    """
    if len(arr) <= 1:
        return True

    if order == "ASC":
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False

    elif order == "DESC":
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                return False

    else:
        raise ValueError("Order must be 'ASC' or 'DESC'")

    return True


# Approach 2 (Not Optimal)
def is_sorted_using_sort(arr, order="ASC"):
    """
    Checks if array is sorted using sorting.

    :param arr: List[int]
    :param order: "ASC" or "DESC"
    :return: bool
    """
    if order == "ASC":
        return arr == sorted(arr)
    elif order == "DESC":
        return arr == sorted(arr, reverse=True)
    else:
        raise ValueError("Order must be 'ASC' or 'DESC'")


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 4]

    print("ASC (Optimal):", is_sorted(arr, "ASC"))
    print("DESC (Optimal):", is_sorted(arr, "DESC"))

    print("ASC (Sort):", is_sorted_using_sort(arr, "ASC"))
    print("DESC (Sort):", is_sorted_using_sort(arr, "DESC"))