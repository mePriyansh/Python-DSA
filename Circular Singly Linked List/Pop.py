class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
        
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
    
    def traverse(self):
        temp_node=self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node=temp_node.next
            if temp_node==self.head:
                break
            
    #Time complexity: O(n)
    #Space complexity: O(1)
    
    def search(self,target):
        current=self.head
        while current is not None:
            if current.value==target:
                return True
            current=current.next
            if current==self.head:
                break
        return False
    
    #Time complexity: O(n)
    #Space complexity: O(1)
    
    def get(self,index):
        if index==-1:
            return self.tail
        elif index<-1 or index>=self.length:
            raise Exception('Invalid index')
        current=self.head
        for _ in range(index):
            current=current.next
        return current
    
    #Time complexity: O(n)
    #Space complexity: O(1)
    
    def set_values(self,index,value):
        current=self.get(index)
        if current:
            current.value=value
            return True
        return False
    
    #Time complexity: O(n)
    #Space complexity: O(1)
    
    def pop_first(self):
        popped_node=self.head
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
            popped_node.next=None
        self.length-=1
        return popped_node
    
    #Time complexity: O(1)
    #Space complexity: O(1)
    
    def pop(self):
        popped_node=self.tail
        if self.length==0:
            return None
        elif self.length==1:
            self.head=self.tail=None
        else:
            temp_node=self.head
            while temp_node.next is not self.tail:
                temp_node=temp_node.next
            temp_node.next=self.head
            self.tail=temp_node
        self.length-=1
        return popped_node
    
    #Time complexity: O(n)
    #Space complexity: O(1)
        
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
print(cslinkedlist.pop())
print(cslinkedlist)