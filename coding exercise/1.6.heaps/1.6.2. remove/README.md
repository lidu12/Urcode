## remove()
- Removes and returns the maximum value (the root) of the heap.
- Replaces the root with the last element.
- Calls _sink_down() to restore the heap property.
- Maintains the max-heap invariant.
- Returns None if the heap is empty.
