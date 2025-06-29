def reverse(self):
    if not self.head or not self.head.next:
        return

    current = self.head
    temp = None

    while current:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    temp = self.head
    self.head = self.tail
    self.tail = temp
