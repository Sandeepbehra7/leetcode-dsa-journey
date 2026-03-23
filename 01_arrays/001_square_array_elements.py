"""
Problem: Square Array Elements

Given a list of integers `nums`, return a new list where each element
is the square of the corresponding element in `nums`.

Example:
Input:  [1, 2, 3]
Output: [1, 4, 9]

Approach 1: Create New List
    - Iterate through each element
    - Append squared value to a new list
    - Time Complexity: O(n)
    - Space Complexity: O(n)

Approach 2: Modify In-Place
    - Iterate through indices
    - Replace each element with its square
    - Time Complexity: O(n)
    - Space Complexity: O(1)

Edge Cases:
    - Empty list
    - Single element
    - Negative numbers
"""

# Approach - 1
def square_array_new_list(nums):
    """
    Returns a new list containing squares of elements in nums.

    :param nums: List[int]
    :return: List[int]
    """
    result = []

    for num in nums:
        squared_value = num * num
        result.append(squared_value)

    return result

# Approach - 2
def square_array_in_place(nums):
    """
    Returns the list containing squares of elements in nums.

    :param nums: List[int]
    :return: List[int]

    * This method modifies the input list rather than creating a new list. *
    """
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    return nums

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]

    print("New List Approach:", square_array_new_list(nums))
    print("In-Place Approach:", square_array_in_place(nums.copy())) # We passed nums.copy() so both process can be executed safely.
    
