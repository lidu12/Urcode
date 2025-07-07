# Graph Class - remove_edge Method

This method removes an undirected edge between two nodes.

## How it works
- Checks if both nodes exist.
- Tries to remove each from the other's adjacency list.
- Ignores error if edge doesn't exist.

## Example
graph.remove_edge('A', 'B')

## Result
A : []
B : []
