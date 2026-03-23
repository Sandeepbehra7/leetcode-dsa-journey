"""
Problem: Find Maximum Element in Array

Given a list of integers, return the maximum element in the array.

Example:
Input:  [2, 34, 12, 35, 356, 72, 128]
Output: 356

Approach 1: Built-in Function
    - Use Python's built-in max() function
    - Time Complexity: O(n)
    - Space Complexity: O(1)

Approach 2: Iterative Comparison (Optimal)
    - Traverse the array and keep track of the maximum element
    - Time Complexity: O(n)
    - Space Complexity: O(1)

Approach 3: Sorting (Not Optimal)
    - Sort the array and return the last element
    - Time Complexity: O(n log n)
    - Space Complexity: O(1)
    - Not recommended as sorting is unnecessary

Approach 4: Stack-Based (For Learning)
    - Push all elements to stack and pop while tracking max
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    - Not optimal due to extra space usage

Edge Cases:
    - Empty list → return None
    - Single element → return that element
"""


# Approach 1
def max_using_builtin(values):
    """
    Returns the maximum element using built-in function.

    :param values: List[int]
    :return: int or None
    """
    if not values:
        return None

    return max(values)


# Approach 2 (Optimal)
def max_using_iteration(values):
    """
    Returns the maximum element using iteration.

    :param values: List[int]
    :return: int or None
    """
    if not values:
        return None

    highest = values[0]

    for val in values[1:]:
        if val > highest:
            highest = val

    return highest


# Approach 3 (Not Optimal)
def max_using_sorting(values):
    """
    Returns the maximum element by sorting the list.

    :param values: List[int]
    :return: int or None

    Note:
    This method modifies the original list.
    """
    if not values:
        return None

    values.sort()  # O(n log n)
    return values[-1]


# Approach 4 (Stack-Based - Learning Purpose)
def max_using_stack(values):
    """
    Returns the maximum element using a stack.

    :param values: List[int]
    :return: int or None

    Note:
    Uses extra space, not optimal.
    """
    if not values:
        return None

    stack = []

    # Push all elements into stack
    for val in values:
        stack.append(val)

    max_val = stack.pop()

    # Pop elements and track max
    while stack:
        current = stack.pop()
        if current > max_val:
            max_val = current

    return max_val


if __name__ == "__main__":
    values = [2, 34, 12, 35, 356, 72, 128]

    print("Built-in:", max_using_builtin(values))
    print("Iteration (Optimal):", max_using_iteration(values))
    print("Sorting (Not Optimal):", max_using_sorting(values.copy()))
    print("Stack (Learning):", max_using_stack(values))