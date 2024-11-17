class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CSLinkedList:
    #No elements in the list
    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0
    
    #One element in the list
    def __init__(self, value):
        newNode = Node(value)
        newNode.next = newNode
        self.head = newNode
        self.tail = newNode
        self.length = 1

cslinkedlist=CSLinkedList(5)
print(cslinkedlist.head.value)