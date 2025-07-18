# Merge Function

## Description:
The `merge()` function takes two **sorted** lists and merges them into one single sorted list.

It uses a two-pointer technique to compare elements from both lists and build a new list called `combined` in ascending order.

## Parameters:
- `list1`: A list of sorted numbers.
- `list2`: Another list of sorted numbers.

## How It Works:
1. Start with the first element of each list.
2. Compare the current elements from both lists.
3. Add the smaller one to the result list (`combined`).
4. Move to the next item in the list from which you took the smaller value.
5. After one list is finished, add the remaining items from the other list.
6. Return the combined sorted list.

## Example:
```python
merge([1,2,7,8], [3,4,5,6])
# Output: [1, 2, 3, 4, 5, 6, 7, 8]
