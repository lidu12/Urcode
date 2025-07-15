class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
                  
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        else:
            self.__r_insert(self.root, value)  

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, node):
        if node is None:
            return None
    
        temp = node.left
        node.left = self.__invert_tree(node.right)
        node.right = self.__invert_tree(temp)
        
        return node
def print_tree_preorder(node):
    if node is None:
        return
    print(node.value, end=" ")
    print_tree_preorder(node.left)
    print_tree_preorder(node.right)

def simple_invert_test():
    print("\n--- Simple Invert Test ---")
    bst = BinarySearchTree()
    bst.r_insert(10)
    bst.r_insert(5)
    bst.r_insert(20)

    print("\nBefore invert (Pre-order):")
    print_tree_preorder(bst.root)   # Should print: 10 5 20

    bst.invert()

    print("\nAfter invert (Pre-order):")
    print_tree_preorder(bst.root)   # Should print: 10 20 5

simple_invert_test()
