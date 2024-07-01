#A linked list is a linear data structure where elements, known as nodes,
# are connected sequentially. Each node consists of two parts:
#Data: The value or information stored in the node.
#Next: A reference (or pointer) to the next node in the sequence.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    #To insert an element at the Beginning of the LinkedList  
    def insert_at_beginning(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            self.head = node
    
    #To print the LinkedList
    def print_list(self):
        if self.head is None:
            print("Linked List is empty")
            return
        current_node = self.head

        while current_node:
            print(current_node.data)
            current_node = current_node.next

    #To insert an element at the end of the LinkedList
    def insert_at_end(self, data):
        if self.head is None :
            self.head = Node(data)
            return
        itr = self.head
        while itr.next:
            itr  = itr.next

        itr.next = Node(data)
    
    #To insert a given list of values
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    #To get the length of the LinkedList
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    
    #To insert an element at a given index
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data)
                node.next = itr.next
                itr.next = node
                return

            itr = itr.next
            count += 1
    
    #To remove an element from the beginning of the LinkedList
    def remove_from_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return
        self.head = self.head.next
    
    #To remove an element from the end of the LinkedList
    def remove_from_end(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        itr = self.head
        while itr.next.next:
            itr =  itr.next
        itr.next = None

    #To remove an element at a given index
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
    
    #To search an element in a Linked list
    def search(self, element):
        current = self.head
        index = 0
        while current is not None:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([2, 4, 5, 7, 9])
    print("Length:",ll.get_length())
    ll.print_list()
    print()
    print(ll.search(15))
   


