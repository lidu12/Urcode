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

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" <-> " if temp.next else "")
            temp = temp.next
        print()

    def partition_list(self, x):
        if not self.head:
            return

        dummy1 = Node(0)  # For < x
        dummy2 = Node(0)  # For >= x
        prev1 = dummy1
        prev2 = dummy2

        current = self.head

        while current:
            next_node = current.next  # Save next node before disconnecting

            # Disconnect current node from its neighbors
            current.prev = None
            current.next = None

            if current.value < x:
                prev1.next = current
                current.prev = prev1
                prev1 = current
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = current

            current = next_node

        # Combine the two lists
        prev1.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = prev1

        self.head = dummy1.next
        if self.head:
            self.head.prev = None

        self.tail = prev2
