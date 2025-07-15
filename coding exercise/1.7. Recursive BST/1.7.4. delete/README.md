delete_node for Binary Search Tree
✅ Purpose
Deletes a value from a Binary Search Tree (BST), while keeping the tree sorted.

✅ How It Works

Starts at the root and searches for the value.

Uses recursion to go left or right.

Once found, handles three cases:

No children: Removes the node.

One child: Connects parent directly to the child.

Two children:

Finds the smallest value in the right subtree.

Replaces the node’s value with it.

Deletes that smallest value.