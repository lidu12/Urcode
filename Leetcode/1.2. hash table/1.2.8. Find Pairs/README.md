# Find Pairs with Given Sum from Two Lists

## Problem
Given two lists of integers, find all pairs `(a, b)` where `a` is from the first list and `b` is from the second list such that `a + b` equals the target value.

## Input
- `arr1`: list of integers
- `arr2`: list of integers
- `target`: integer sum target

## Output
- List of tuples `(a, b)` where each pair sums to `target`.

## Example
```python
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
target = 9

find_pairs(arr1, arr2, target)
# Output: [(3, 6)]
