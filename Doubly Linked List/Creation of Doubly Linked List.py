class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    #No elements in the list
    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0
    
    #One element in the list
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
        
d_linked_list = DoublyLinkedList(10)
print(d_linked_list.head.value)