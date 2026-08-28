# MaxHeap

A simple Python class to implement a Max-Heap data structure.

## Features
- Insert values while maintaining max-heap property.
- Largest value is always at the root.

## Rules
- Each parent node is greater than or equal to its children.
- Stored as a list for easy indexing.

## Usage
- insert(value): Adds a value to the heap.
- Internal methods ensure the heap property is maintained using "bubble up".

## Example
    myheap = MaxHeap()
    myheap.insert(100)
    print(myheap.heap)
