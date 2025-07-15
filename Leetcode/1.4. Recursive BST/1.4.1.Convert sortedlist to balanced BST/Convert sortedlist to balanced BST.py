class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # REQUIRED for the test
    def is_balanced(self, node=None):
        def check(node):
            if node is None:
                return True, -1
            left_bal, left_height = check(node.left)
            right_bal, right_height = check(node.right)
            balanced = left_bal and right_bal and abs(left_height - right_height) <= 1
            return balanced, 1 + max(left_height, right_height)
        result, _ = check(self.root if node is None else node)
        return result

    

    # THIS is what you care about
    def sorted_list_to_bst(self, nums):
        self.root = self._build_bst(nums, 0, len(nums) - 1)

    def _build_bst(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = Node(nums[mid])
        node.left = self._build_bst(nums, left, mid - 1)
        node.right = self._build_bst(nums, mid + 1, right)
        return node

bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6, 7])
print("Is balanced:", bst.is_balanced())

