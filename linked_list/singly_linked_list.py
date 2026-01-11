#implementation of singly linked list

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)


singlyLinkedlist = SL()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

singlyLinkedlist.head = node1
node1.next= node2
node2.next= node3
node3.next =node4
singlyLinkedlist.tail = node4

print(singlyLinkedlist)