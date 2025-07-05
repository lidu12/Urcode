# MinHeap README

**MinHeap**: Always keeps the **smallest** value at the root.

- `insert(value)`: Adds value and bubbles up to maintain order.
- Time: O(log n)
- Space: O(n)

**Example:**
```python
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
# [6, 8, 10, 12]
