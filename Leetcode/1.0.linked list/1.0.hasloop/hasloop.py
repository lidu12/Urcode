class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        new_node = Node(value)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
ll = LinkedList(3)
ll.append(2)
ll.append(0)
ll.append(-4)
tail = ll.head
while tail.next:
    tail = tail.next
tail.next = ll.head.next  # Create cycle
print(ll.has_loop())  # Output: True
