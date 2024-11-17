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
    
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result+=str(temp_node.value)
            temp_node=temp_node.next
            if temp_node==self.head:
                break
            result+='->'
        return result
        
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
    #Time complexity: O(1)
    #Space complexity: O(1)
        
cslinkedlist=CSLinkedList()
cslinkedlist.append(10)
cslinkedlist.append(20)
cslinkedlist.append(30)
cslinkedlist.append(40)
print(cslinkedlist)
print(cslinkedlist.head.value)
print(cslinkedlist.head.next.value)
print(cslinkedlist.tail.value)