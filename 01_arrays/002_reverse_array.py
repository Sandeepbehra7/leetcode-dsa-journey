"""
Problem: Reverse Array

Given a list of integers, reverse the array.

Example:
Input:  [1, 2, 3, 4]
Output: [4, 3, 2, 1]

Approach 1: Slicing (Extra Space)
    - Create a reversed copy using slicing
    - Time Complexity: O(n)
    - Space Complexity: O(n)

Approach 2: List Comprehension (Extra Space)
    - Build a new reversed list manually
    - Time Complexity: O(n)
    - Space Complexity: O(n)

Approach 3: Two Pointer (In-Place)
    - Swap elements from both ends
    - Time Complexity: O(n)
    - Space Complexity: O(1)

Approach 4: Built-in reverse() (In-Place)
    - Uses Python's internal implementation
    - Time Complexity: O(n)
    - Space Complexity: O(1)

Edge Cases:
    - Empty list
    - Single element
    - Large input
"""


# Approach 1
def reverse_using_slicing(arr):
    return arr[::-1]


# Approach 2
def reverse_using_comprehension(arr):
    return [arr[-i] for i in range(1, len(arr) + 1)]


# Approach 3
def reverse_in_place_two_pointers(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# Approach 4
def reverse_in_place_builtin(arr):
    arr.reverse()
    return arr


if __name__ == "__main__":
    arr = [1, 2, 4, 5, 6, 8]

    print("Slicing:", reverse_using_slicing(arr))
    print("Comprehension:", reverse_using_comprehension(arr))
    print("Two Pointers:", reverse_in_place_two_pointers(arr.copy()))
    print("Built-in Reverse:", reverse_in_place_builtin(arr.copy()))