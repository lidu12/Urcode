class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def swap_pairs(self):
        if not self.head or not self.head.next:
            return

        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy

        prev = dummy
        current = self.head

        while current and current.next:
            first = current
            second = current.next

            # Swap the pair
            prev.next = second
            second.prev = prev

            first.next = second.next
            if second.next:
                second.next.prev = first

            second.next = first
            first.prev = second

            # Move to the next pair
            prev = first
            current = first.next

        # Reset head and detach dummy
        self.head = dummy.next
        self.head.prev = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=" <-> " if temp.next else "")
            temp = temp.next
        print()
