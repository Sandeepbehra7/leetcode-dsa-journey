"""
Problem: Remove Duplicates from Sorted Array

Given a sorted array, remove duplicates in-place such that each element appears only once.

Return the new length of the array.

Example:
Input:  [1, 1, 2, 2, 3]
Output: [1, 2, 3] (length = 3)

Approach 1: Using Extra List (Not Optimal)
    - Store unique elements in new list
    - Time Complexity: O(n²)
    - Space Complexity: O(n)

Approach 2: Using Set (Not Optimal)
    - Convert list to set
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    - Does not preserve order

Approach 3: Two Pointer (Optimal)
    - Overwrite duplicates in-place
    - Time Complexity: O(n)
    - Space Complexity: O(1)

Edge Cases:
    - Empty list
    - Single element
"""


# Approach 1
def remove_duplicates_bruteforce(arr):
    result = []
    for element in arr:
        if element not in result:
            result.append(element)
    return result


# Approach 2
def remove_duplicates_set(arr):
    return list(set(arr))


# Approach 3 (Optimal)
def remove_duplicates_in_place(arr):
    if not arr:
        return 0

    write = 1

    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1

    return write


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3]

    print("Brute Force:", remove_duplicates_bruteforce(arr))
    print("Using Set:", remove_duplicates_set(arr))

    length = remove_duplicates_in_place(arr.copy())
    print("In-Place Result:", arr[:length], "Length:", length)