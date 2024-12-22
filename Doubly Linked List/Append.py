class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
    #Time complexity: O(1)
    #Space complexity: O(1)
                
d_linked_list = DoublyLinkedList()
d_linked_list.append(10)
d_linked_list.append(20)
print(d_linked_list.head.value)