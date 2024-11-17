class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class CSLinkedList:
    #No elements in the list
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self,value):
        if self.length == 0:
            new_node=Node(value)
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node=Node(value)
            self.tail.next=new_node
            self.tail=new_node
            self.tail.next=self.head
        self.length+=1
        
cslinkedlist=CSLinkedList()
cslinkedlist.append(10)
cslinkedlist.append(20)
cslinkedlist.append(30)
cslinkedlist.append(40)
print(cslinkedlist.head.value)
print(cslinkedlist.head.next.value)
print(cslinkedlist.tail.value)