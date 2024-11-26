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
    
    def prepend(self,value):
        new_node=Node(value)
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
        self.length+=1
    #Time complexity: O(1)
    #Space complexity: O(1)
    
    def insert(self, index, value):
        new_node=Node(value)
        if index<0 or index>self.length:
            raise Exception('Invalid index')
        elif index==0:
            if self.length == 0:
                self.head=new_node
                self.tail=new_node
                new_node.next=new_node
            else:
                new_node.next=self.head
                self.head=new_node
                self.tail.next=self.head
        elif index==self.length:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        else:
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
        
cslinkedlist=CSLinkedList()
cslinkedlist.insert(0,10)
cslinkedlist.prepend(5)
cslinkedlist.append(20)
cslinkedlist.append(40)
cslinkedlist.append(50)
print(cslinkedlist)
cslinkedlist.insert(3,30)
print(cslinkedlist)
cslinkedlist.insert(0,0)
print(cslinkedlist)