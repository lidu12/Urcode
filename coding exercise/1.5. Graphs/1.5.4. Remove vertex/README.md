# Graph Class - remove_vertex Method

This method completely removes a node from the graph.

## How it works
- Checks if the node exists.
- Removes this node from all its neighbors' lists.
- Deletes the node from the adjacency list.

## Example
graph.remove_vertex('A')

## Result
A is gone. No node lists A as a neighbor.
