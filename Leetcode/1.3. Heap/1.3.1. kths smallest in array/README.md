
This project implements a **MaxHeap** data structure in Python and uses it to solve the problem of finding the *k-th smallest* element in an unsorted list.

## Features

- **MaxHeap class** with:
  - `insert(value)`: Adds a value while maintaining the heap property.
  - `remove()`: Removes and returns the maximum value.

- **find_kth_smallest(nums, k)** function:
  - Uses a MaxHeap of size *k* to efficiently find the k-th smallest element.

## How It Works

1. Insert all elements into the heap.
2. Maintain only *k* elements in the heap (remove the largest when size exceeds *k*).
3. At the end, the root of the heap is the k-th smallest element.
