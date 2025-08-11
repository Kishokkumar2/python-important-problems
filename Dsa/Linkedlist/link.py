class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def add(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            cur = self.head
            while cur.pointer is not None:
                cur = cur.pointer
            cur.pointer = newnode

    def print(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.pointer

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.pointer
            current.pointer = prev
            prev = current
            current = next_node
        self.head = prev

# ✅ Test
link = Linkedlist()
link.add(1)
link.add(2)
link.add(3)
link.add(4)
link.add(5)
link.add(6)

print("Original List:")
link.print()

link.reverse()

print("Reversed List:")
link.print()
