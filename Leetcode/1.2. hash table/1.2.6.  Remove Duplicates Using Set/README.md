# Remove Duplicates (Python)

Removes duplicates from a list using a set.  
Returns a new list with unique values.

## Example
Input:  
`[1, 2, 3, 4, 1, 2, 5, 6, 3]`  
Output:  
`[1, 2, 3, 4, 5, 6]` *(order may vary)*

## Code
```python
def remove_duplicates(my_list):
    return list(set(my_list))
