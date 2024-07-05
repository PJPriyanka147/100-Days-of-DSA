class Node:
    def __init__(self, element, next):
        self.element = element
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size == 0
    
    def addlast(self, e):
        node = Node(e, None)
        if self.isempty():
            self.head = node
        else :
            self.tail.next = node
        self.tail = node
        self.size += 1

    def display(self):
        p = self.head
        while p:
            print(p.element, end='-->')
            p = p.next
        print()

L = LinkedList()
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.display()