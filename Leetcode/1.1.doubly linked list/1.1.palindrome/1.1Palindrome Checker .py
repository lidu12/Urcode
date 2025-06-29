class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def is_palindrome(self):
        if self.length <= 1:
            return True

        left = self.head
        right = self.tail

        for _ in range(self.length // 2):
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev

        return True
dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(2)
dll.append(1)

print(dll.is_palindrome())  # Output: True

dll2 = DoublyLinkedList(1)
dll2.append(2)
dll2.append(3)
dll2.append(4)
dll2.append(5)

print(dll2.is_palindrome())  # Output: False
