class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

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

    def reverse_between(self, start_index, end_index):
        if not self.head or self.head.next is None or start_index == end_index:
            return

        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy

        prev = dummy
        for _ in range(start_index):
            prev = prev.next

        current = prev.next

        for _ in range(end_index - start_index):
            node_to_move = current.next

            current.next = node_to_move.next
            if node_to_move.next:
                node_to_move.next.prev = current

            node_to_move.next = prev.next
            prev.next.prev = node_to_move

            prev.next = node_to_move
            node_to_move.prev = prev

        self.head = dummy.next
        self.head.prev = None
