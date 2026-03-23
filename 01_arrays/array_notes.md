# Arrays – Concept Notes

This document contains conceptual understanding gathered while solving array problems.

---

## 1️⃣ Time Complexity Basics

- **O(1)** → Constant time. Execution does not depend on input size.
  - Example: `x = nums[0]`

- **O(n)** → Linear time. Execution depends directly on input size.
  - Example: Iterating through entire list.

- **O(n²)** → Nested loops over same list.
  - Example:
    ```
    for i in nums:
        for j in nums:
    ```

- Sequential loops → Add complexities  
  O(n) + O(n) = O(n)

- Nested loops → Multiply complexities  
  O(n) × O(n) = O(n²)

- In Big-O, we keep the highest order term.

---

## 2️⃣ Space Complexity (Very Important)

Space complexity measures **extra memory used**, not input memory.

We calculate **Auxiliary Space**, meaning:

> Additional memory required to solve the problem.

Example:

### Case 1 – Creating New List

result = []
for num in nums:
result.append(num * num)


- Extra space = O(n)
- Space Complexity = O(n)

---

### Case 2 – Modify In-Place

for i in range(len(nums)):
nums[i] = nums[i] * nums[i]


- No new list created
- Only temporary variables used
- Space Complexity = O(1)

---

## 3️⃣ List Reversal

### Method 1 – Slicing

nums = nums[::-1]

- Creates new list
- Time Complexity: O(n)
- Space Complexity: O(n)

Why?  
Because slicing allocates new memory and copies elements.

---

### Method 2 – In-Place Reverse

nums.reverse()

OR

left = 0
right = len(nums) - 1

while left < right:
nums[left], nums[right] = nums[right], nums[left]
left += 1
right -= 1


- Time Complexity: O(n)
- Space Complexity: O(1)

Why?  
Because elements are swapped within the same list.

---

## 4️⃣ Two Pointer Insight

When reversing an array:

- Total swaps = n // 2
- Middle element (if odd length) remains unchanged

This introduces the **Two Pointer Technique**, which will be heavily used in later problems.

---

## 5️⃣ append() Complexity



nums.append(x)


- Average case → O(1)
- Worst case → O(n) (when resizing happens)
- This is called **Amortized O(1)**

---

## 6️⃣ Printing Complexity



print(nums)


Printing a list of size n takes O(n) time  
because each element must be converted to string and printed.

---

## 7️⃣ Key Takeaways So Far

- Space complexity = extra space used
- Slicing creates new memory
- In-place operations reduce space complexity
- Nested loops multiply complexity
- Sequential loops add complexity
- append() is amortized O(1)
- Reverse in-place uses n//2 swaps