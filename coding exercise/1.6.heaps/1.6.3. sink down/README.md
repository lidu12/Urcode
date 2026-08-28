## _sink_down(index)
- Private helper to restore the heap property after removal.
- Moves an out-of-place element down the heap until it's larger than both children (for max-heap).
- Used internally after remove().
- Works in O(log n) time because the height of the heap is log n.
