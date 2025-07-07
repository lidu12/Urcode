# Graph Class - add_edge Method

This method adds an undirected edge between two existing nodes.

## How it works
- Checks if both nodes exist.
- Adds each node to the other's adjacency list.

## Example
graph.add_edge('A', 'B')

## Result
A : ['B']
B : ['A']
