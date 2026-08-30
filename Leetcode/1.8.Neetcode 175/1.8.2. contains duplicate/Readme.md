# LeetCode #217 — Contains Duplicate

## Problem

Given an integer array `nums`, return `True` if any value appears at least twice. Return `False` if every element is distinct.

### Example

```text
Input:  nums = [1, 2, 3, 1]
Output: True
```

The value `1` appears twice.

## Approach

Use a **Hash Set** to keep track of numbers we have already seen.

1. Create an empty set.
2. Loop through each number in `nums`.
3. If the number is already in the set, return `True`.
4. Otherwise, add it to the set.
5. If no duplicate is found, return `False`.



## Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

## Data Structure

**Hash Set (`set`)**
